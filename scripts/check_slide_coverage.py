#!/usr/bin/env python3
"""Check slide-matched Markdown speech headings against the actual PPTX roster."""
import sys
import io
if __name__ == "__main__" and hasattr(sys.stdout, "buffer"):
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")
if __name__ == "__main__" and hasattr(sys.stderr, "buffer"):
    sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding="utf-8", errors="replace")
import argparse
import collections
import json
from pathlib import Path
import re
import xml.etree.ElementTree as ET
from zipfile import ZipFile, BadZipFile


def audit(pptx, script, require_all=False):
    ns = {"p": "http://schemas.openxmlformats.org/presentationml/2006/main"}
    with ZipFile(pptx) as package:
        doc = ET.fromstring(package.read("ppt/presentation.xml"))
        count = len(doc.findall("./p:sldIdLst/p:sldId", ns))
    if count == 0:
        raise ValueError("PPTX没有页面")
    text = Path(script).read_text(encoding="utf-8-sig")
    headings = list(re.finditer(r"^#{1,6}[ \t]+第[ \t]*(\d+)[ \t]*页(?:[ \t]+([^\r\n]*))?[ \t]*$", text, re.M))
    numbers = [int(match.group(1)) for match in headings]
    observed = set(numbers)
    expected = set(range(1, count + 1))
    duplicates = sorted(n for n, c in collections.Counter(numbers).items() if c > 1)
    empty = []
    for index, match in enumerate(headings):
        end = headings[index + 1].start() if index + 1 < len(headings) else len(text)
        body = text[match.end():end]
        body = re.sub(r"【操作[：:].*?】", "", body, flags=re.S)
        if len(re.findall(r"[\w\u3400-\u9fff]", body)) < 5:
            empty.append(int(match.group(1)))
    errors = []
    if not numbers:
        errors.append("没有找到讲稿标题，请使用 '# 第1页 标题' 格式")
    if duplicates:
        errors.append("存在重复页码")
    if empty:
        errors.append("存在缺少实质正文的页码")
    if observed - expected:
        errors.append("讲稿包含超出PPT范围的页码")
    if numbers != sorted(numbers):
        errors.append("讲稿顺序与PPT页码顺序不一致")
    if require_all and expected - observed:
        errors.append("完整讲稿缺页")
    return {"status": "failed" if errors else "passed", "ppt_pages": count,
            "speech_sections": len(numbers), "missing": sorted(expected - observed),
            "unexpected": sorted(observed - expected), "duplicates": duplicates,
            "empty": empty, "errors": errors,
            "scope": "只检查页码与正文存在性，不验证科学内容或PDF版面"}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--pptx", required=True, type=Path)
    parser.add_argument("--script", required=True, type=Path, help="UTF-8 Markdown，标题如 '# 第1页 开场'")
    parser.add_argument("--require-all", action="store_true", help="缺少任何PPT页码时返回失败")
    parser.add_argument("--output", type=Path, help="可选JSON报告，只写明确指定的文件")
    args = parser.parse_args()
    try:
        report = audit(args.pptx, args.script, args.require_all)
    except (OSError, ValueError, KeyError, BadZipFile, ET.ParseError) as exc:
        print(json.dumps({"status": "failed", "message": str(exc)}, ensure_ascii=False), file=sys.stderr)
        return 1
    encoded = json.dumps(report, ensure_ascii=False, indent=2)
    if args.output:
        args.output.write_text(encoded + "\n", encoding="utf-8")
    print(encoded)
    return 0 if report["status"] == "passed" else 1


if __name__ == "__main__":
    raise SystemExit(main())
