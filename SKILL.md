---
name: xiangyu-academic-ppt
description: >-
  Integrate full Nature Skills paper analysis and evidence-led storytelling with
  full PPT Master production for Chinese academic presentations. Use for 论文汇报、
  组会PPT、主题综述汇报、原生PPT模板修改 and slide-matched LaTeX speech scripts.
  Preserve original paper figures and editable content; apply the supplemental
  Xiangyu presentation preferences only within the current user's requested scope.
---

# 学术汇报整合技能

此入口只增加协作规则与个人经验，不替代或删减两套原技能。

- [完整 PPT Master](vendor/ppt-master/skills/ppt-master/SKILL.md)，包括原有脚本、模板、工作流、署名及许可。
- [完整 Nature Skills](vendor/nature-skills/README.md)，保留整仓全部技能和共享依赖。
- [整合分工与冲突处理](references/integration.md)。先读该文件，再加载当前任务真正需要的原技能。
- [对话经验与适用范围](references/conversation-requirements.md)。这是附加层，具体用户当前要求优先。

## 开始工作

1. 确认来源、当前主文件和任务范围。修某一页时复用既有材料，不重新生成全稿。
2. 若 `vendor/` 尚未初始化，运行 `git submodule update --init --recursive`。不能用摘要或自己重写的流程替代缺失原件。
3. 新建学术汇报时，先用 Nature 分析问题、方法、假设、证据与叙事。按论文类型加载片段，建立术语表与图源映射。
4. 由 PPT Master 选择一个制作路由。新建、套现成 PPTX 模板、局部修改、图片还原属于不同任务，按其路由表选择。执行其署名完整性检查，保留原有质量关卡。
5. 结合 [图像与原图规则](references/figures-and-images.md) 和 [排版、理论与衔接](references/design-and-reasoning.md) 制作。原论文图负责证据；生成图负责教学解释。
6. 若需要讲稿，按 [逐页讲稿与 LaTeX](references/speech-and-latex.md) 建立与当前 PPT 一致的逐页内容。是否选讲、总时长和视频时长由本次要求决定。
7. 按 [交付与检查](references/quality-and-delivery.md) 做来源、结构和渲染检查，修复发现的问题，再交付可用文件。

## 执行边界

- 两个生产引擎不能同时改写同一份 PPTX。组合模式由 Nature 提供学术内容，PPT Master 拥有页面状态与最终导出。
- 用户要求原生 Nature 制作或 Nature Image2PPT 时，进入对应独立运行时，不同时运行 PPT Master 的导出状态机。
- 已有明确设计授权时延续授权。需要用户决定的未解决冲突只问关键问题，不重复请求已给过的确认。
- 不虚构文献、数据、推导步骤、工具执行记录或编译成功。没有原文支撑的结果不写成已验证结论。
- 主要交付物是用户要求的 PPTX、PDF 或源码包。审计表可以内部留档，不把 CSV 当成 PPT 的替代交付物。

## 可复用检查工具

- `python scripts/verify_bundle.py`：检查完整原仓库、固定提交、干净上游和本技能引用。
- `python scripts/check_slide_coverage.py --pptx <最终PPTX> --script <逐页讲稿.md> --require-all`：核对实际页数、连续页码与每页讲稿。先使用 `--help` 查看标题格式。

凭证只通过环境变量或仓库外的本地配置传入。不得从历史对话复制密钥，也不把材料、组员身份、私有文件路径或完整聊天记录带入公开仓库。
