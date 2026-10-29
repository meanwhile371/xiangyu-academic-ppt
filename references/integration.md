# 两套完整技能如何协作

## 所有权

完整源代码位于 `vendor/`，由 `upstream-lock.json` 固定版本。原文件不修改，原许可证、署名、赞助说明、模板、脚本和共享依赖不删除。整合只发生在此仓库的新增文件中。

| 任务 | 首要负责人 | 完整入口 |
|---|---|---|
| 论文精读、研究问题、方法与证据 | Nature Reader | `vendor/nature-skills/skills/nature-reader/SKILL.md` |
| 论文类型、汇报叙事、选图与学术审查 | Nature Paper2PPT | `vendor/nature-skills/skills/nature-paper2ppt/SKILL.md` |
| 图表与引用专项分析 | 对应 Nature 技能 | `vendor/nature-skills/skills/nature-figure/`、`nature-citation/`、`nature-ref-verifier/` |
| 版式、模板、SVG、PPTX制作与原生修改 | PPT Master | `vendor/ppt-master/skills/ppt-master/SKILL.md` |
| 图片还原独立流程 | 选择一个还原引擎 | Nature Image2PPT 或 PPT Master 的 Image to PPTX |
| 逐页讲稿与 LaTeX PDF | 本附加层 | `references/speech-and-latex.md` |

根据各技能 manifest 的相对路径逐步加载。Nature 的 `nature-shared` 与其他全部技能均在完整仓库中，保持同级关系。

## 组合模式的接口

Nature 输出的内容计划应交代：

- 当前论文类型与汇报目的。
- 一句话核心问题，以及各章节的前后关系。
- 每页想说明的结论、证据出处和图表位置。
- 公式使用的模型、符号、假设和结论指标。
- 图源、原图面板、裁剪范围与不可丢失的上下文。
- 术语表、适用条件和仍未解决的来源问题。

这些是内容接口，不是第二套页面状态机。随后由 PPT Master 接管制作路由、页面计划、SVG、备注、动画和最终导出。它要求哪些计划文件，就使用哪些文件，不平行维护相互矛盾的页面清单。

## 冲突处理

**引擎。** Nature Paper2PPT 默认用 python-pptx 构建；组合模式明确选择 PPT Master 的制作引擎。保留 Nature 的阅读、叙事、选图和学术检查，构建部分交给 PPT Master。不得在同一成果上先 SVG 导出，再用 python-pptx 重写整稿。用户单独要求 Nature 原生模式时，执行它完整的独立流程。

**路由。** 已有 PPTX 的局部修改、原稿套用和页序调整，按 PPT Master 的 Edit Native PPTX 处理，使用 round-trip 工作区。全稿重构、图片还原和可复用模板创建，分别按其路由表处理。原件导入警告不等于原件一定丢失，必须检查最终恢复状态。

**图片还原。** Nature Image2PPT 有自己的 CLI、页面 manifest 和状态目录。使用它时遵守其自包含边界，不能让 PPT Master 读取或改写相同页面状态。需要后续独立修改时，先完成该任务并导出，再把成品作为新任务输入。

**确认。** 原技能的确认关卡保留原文。当前用户更具体的要求与已明确给出的持续授权决定是否需要再次询问；不能把一次授权扩展为上传新材料、付费生图或公开发布其他内容的无限授权。尚未得到答复的必要问题不能用等待时间替代批准。

**渲染。** Nature 的轻量跨平台默认与本对话要求的视觉精修可以共存：先使用已有可用渲染器；用户明确要求高保真或密集改版时，对改页做真实渲染。PowerPoint可用时可用其渲染结果检查；不可用则如实记录所用引擎及限制，不宣称检查过桌面显示。

**范围。** 一份课程作业和一项原创研究不适用同一套创新性要求。按本次用途决定深度，不为封面更名或小幅排版追加实验、论文重写或审稿工程。

## 完整性失败

`verify_bundle.py` 失败时，先恢复或初始化固定子模块。PPT Master 的 attribution guard 非零时停止该技能，按原要求处理，不能移除检查或改写署名。上游更新通过独立维护变更修改锁文件并重新验证，正常制作任务不追踪浮动主分支。
