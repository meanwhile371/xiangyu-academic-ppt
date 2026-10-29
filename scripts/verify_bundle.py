#!/usr/bin/env python3
"""Verify pinned complete upstream checkouts without installing or modifying them."""
import sys
import io
if __name__ == "__main__" and hasattr(sys.stdout, "buffer"):
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")
if __name__ == "__main__" and hasattr(sys.stderr, "buffer"):
    sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding="utf-8", errors="replace")
import argparse
import json
import os
from pathlib import Path
import subprocess

ROOT = Path(__file__).resolve().parent.parent


def git(directory, *arguments):
    proc = subprocess.run(
        ["git", "-C", str(directory), *arguments],
        stdout=subprocess.PIPE, stderr=subprocess.PIPE, timeout=120,
    )
    if proc.returncode:
        raise RuntimeError("Git检查失败：" + " ".join(arguments[:2]))
    return proc.stdout


def verify():
    lock = json.loads((ROOT / "upstream-lock.json").read_text(encoding="utf-8"))
    findings = []
    for upstream in lock["upstreams"]:
        directory = ROOT / upstream["path"]
        if not (directory / ".git").exists():
            raise RuntimeError(f"{upstream['path']}未初始化，请运行git submodule update --init --recursive")
        sha = git(directory, "rev-parse", "HEAD").decode().strip()
        if sha != upstream["commit"]:
            raise RuntimeError(f"{upstream['name']}提交与锁文件不一致")
        tree = git(directory, "rev-parse", "HEAD^{tree}").decode().strip()
        if tree != upstream["tree"]:
            raise RuntimeError(f"{upstream['name']}文件树不一致")
        paths = [p.decode("utf-8") for p in git(directory, "ls-files", "-z").split(b"\0") if p]
        if len(paths) != upstream["tracked_files"]:
            raise RuntimeError(f"{upstream['name']}跟踪文件数量不一致")
        missing = [p for p in paths if not os.path.lexists(directory / p)]
        if missing:
            raise RuntimeError(f"{upstream['name']}缺失{len(missing)}个跟踪文件")
        if git(directory, "status", "--porcelain", "--untracked-files=no").strip():
            raise RuntimeError(f"{upstream['name']}原件有修改，请恢复或单独记录维护变更")
        for entrypoint in upstream["entrypoints"]:
            if not (directory / entrypoint).is_file():
                raise RuntimeError(f"{upstream['name']}入口缺失：{entrypoint}")
        findings.append({"name": upstream["name"], "commit": sha, "tracked_files": len(paths), "clean": True})

    recursive = git(ROOT, "submodule", "status", "--recursive").decode("utf-8")
    if any(line[:1] in ("-", "+", "U") for line in recursive.splitlines()):
        raise RuntimeError("存在未初始化、冲突或版本不一致的子模块")

    guard = ROOT / "vendor/ppt-master/skills/ppt-master/scripts/attribution_guard.py"
    proc = subprocess.run([sys.executable, str(guard)], stdout=subprocess.PIPE, stderr=subprocess.PIPE, timeout=120)
    if proc.returncode:
        raise RuntimeError("PPT Master署名完整性检查未通过；未绕过该检查")

    required = [
        "SKILL.md", "agents/openai.yaml", "references/integration.md",
        "references/conversation-requirements.md", "references/figures-and-images.md",
        "references/design-and-reasoning.md", "references/speech-and-latex.md",
        "references/quality-and-delivery.md", "THIRD_PARTY_NOTICES.md",
    ]
    for name in required:
        if not (ROOT / name).is_file():
            raise RuntimeError("缺少整合文件：" + name)
    return {"status": "passed", "upstreams": findings, "attribution_guard": "passed"}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--json", action="store_true", help="输出JSON结果")
    args = parser.parse_args()
    try:
        report = verify()
    except (OSError, RuntimeError, ValueError, subprocess.SubprocessError) as exc:
        print(json.dumps({"status": "failed", "message": str(exc)}, ensure_ascii=False) if args.json else str(exc), file=sys.stderr)
        return 1
    print(json.dumps(report, ensure_ascii=False, indent=2) if args.json else "完整性检查通过：两套固定版本原仓库、全部跟踪文件及PPT Master署名关卡均正常。")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
