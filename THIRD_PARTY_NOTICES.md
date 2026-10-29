# 上游与第三方说明

本仓库使用 Git 子模块引用两套完整源项目。子模块是固定提交的独立仓库，没有把其代码改写为本项目原创，也不改变任何上游文件。

## PPT Master

- 原作者与贡献者：Hugo He 及上游贡献者。
- 官方来源：https://github.com/hugohe3/ppt-master
- 许可：MIT，版权与原始LICENSE、技能元数据和署名检查全部保留。
- 原仓库位于 `vendor/ppt-master`，实际技能位于其 `skills/ppt-master`。
- 图标、音效、形状数据等可能有嵌套许可证与NOTICE，继续适用，不能只引用根MIT覆盖一切。
- Python等运行依赖不随本仓库打包。依赖软件的许可证与安装条件需分别遵守。

## Nature Skills

- 原作者与贡献者：Yuan1z0825 及上游贡献者。
- 官方来源：https://github.com/Yuan1z0825/nature-skills
- 固定版本根许可：Apache-2.0，完整LICENSE与各文件声明保持。
- 原仓库位于 `vendor/nature-skills`，包括全部 `skills/`、共享层、脚本、文档与资产。
- `skills/nature-figure/assets/figures4papers/THIRD_PARTY_NOTICES.md` 明确说明部分参考素材没有确认的再分发授权。子模块只引用上游原仓库，不授予复制、修改或发布这些素材的额外许可。不要将其打入本项目自有素材包或用根许可证推断授权。

## 本仓库的新增内容

`SKILL.md`、`references/`、`scripts/`及根说明文件是独立整合层。其MIT许可仅覆盖本项目原创部分。经验文档去除了历史对话中的API密钥、私人路径、成员姓名学号与原始附件。没有上传用户的论文、PPT、报告、图片或完整聊天记录。

子模块引用的完整仓库可能包含并不适用于当前任务的其他功能。保留功能不等于自动执行这些功能，仍需按照原技能路由和用户当前授权选择。
