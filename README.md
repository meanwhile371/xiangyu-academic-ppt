# Xiangyu Academic PPT

将 **Nature Skills 的论文分析与证据叙事**、**PPT Master 的制作与原生编辑**结合起来，再叠加长期修改学术汇报积累的要求。

两套上游以固定提交的完整 Git 子模块保留。没有重写、精简或删除原技能。此仓库新增的内容只有整合入口、经验参考与检查脚本。`Nature` 在这里表示上游项目的名称与学术叙事方法，不代表 Nature 期刊官方认证。

## 安装

需要 Git 和 Python 3.10 或以上。先递归克隆，才能得到两套完整上游。

PowerShell，安装到 Codex 的个人技能目录：

```powershell
git clone --recurse-submodules https://github.com/meanwhile371/xiangyu-academic-ppt.git "$env:USERPROFILE\.codex\skills\xiangyu-academic-ppt"
python "$env:USERPROFILE\.codex\skills\xiangyu-academic-ppt\scripts\verify_bundle.py"
```

macOS / Linux：

```bash
git clone --recurse-submodules https://github.com/meanwhile371/xiangyu-academic-ppt.git ~/.codex/skills/xiangyu-academic-ppt
python3 ~/.codex/skills/xiangyu-academic-ppt/scripts/verify_bundle.py
```

已经普通克隆的用户，在仓库目录运行：

```bash
git submodule update --init --recursive
python scripts/verify_bundle.py
```

GitHub 的 Download ZIP 不包含子模块正文。需要完整离线使用时，先递归克隆并检查，再自行归档该目录。不要使用 `git submodule update --remote`，它会绕开本仓库固定版本。依赖按选中的原技能安装，不自动安装整套科研环境。

## 使用

在新对话中调用 `$xiangyu-academic-ppt`，例如：

> 根据这些论文和指定 PPTX 模板制作中文学术汇报。Nature 分析原理和原始证据，ppt-master 完成排版。保留原论文彩图，理论教学图使用英文黑白。先确认叙事和证据映射，再制作可编辑 PPTX。

> 修改现有 PPT 的封面与贡献表，其他页面、公式、视频和动画保留。沿用已经批准的封面风格。

> 根据最终 PPT 写逐页完整演讲稿，每页都要有，包含参考文献与附录。视频单独计时，允许超时，交付紧凑 LaTeX PDF。

本仓库不预设任何任务都必须 62 页、70 篇文献或 9 分钟。它保存这些要求在原对话中的作用和后续变更，再由当前任务选择适用配置。

## 结构

```text
SKILL.md                         整合入口
references/                      附加要求、经验和冲突处理
scripts/                         完整性与页码检查
vendor/ppt-master/               完整官方仓库，固定提交
vendor/nature-skills/            完整官方仓库，固定提交
upstream-lock.json               来源、版本及文件树记录
THIRD_PARTY_NOTICES.md            上游与第三方许可说明
```

## 工作原则

- 先建立问题、方法、证据和结论的主线，再设计页面。
- 引用回到真实论文，保留条件、指标、样本和比较口径。
- 经典论文原图按原色保留，教学生成图另行标识。
- 信息密度来自有效内容，不靠缩小字号或添加无关装饰填空。
- 原生可编辑文本、公式、表格与流程图优先；论文原图作为忠实图像保留。
- 局部修改只动指定页面，导出后核对未修改页和媒体。
- 完整讲稿覆盖每页；时间不足时明确选讲安排，不能悄悄漏页。
- 对来源、结构和渲染分别检查，不把脚本通过当成视觉通过。

图像 API 使用原技能提供的可配置后端，密钥留在环境变量或仓库外。此仓库不包含历史对话中的 API 地址、密钥、组员身份或私人材料，也不自动向第三方上传任何文档。

## 验证与许可

本仓库附加代码和文档使用 MIT 许可证。PPT Master 原件遵循其 MIT 及嵌套声明；Nature Skills 原件遵循其 Apache-2.0 及各素材声明。子模块中的无明确授权素材不能据上游根许可证推断可以任意再分发，见 [第三方说明](THIRD_PARTY_NOTICES.md)。

完整源项目分别来自 [hugohe3/ppt-master](https://github.com/hugohe3/ppt-master) 和 [Yuan1z0825/nature-skills](https://github.com/Yuan1z0825/nature-skills)。感谢原作者与贡献者。验证范围见 [VALIDATION.md](VALIDATION.md)，未来使用仍需对自己的材料和导出文件检查。
