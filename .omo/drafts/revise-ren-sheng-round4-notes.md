---
slug: revise-ren-sheng-round4-notes
status: plan-review-rerun-rejected-and-patched
intent: clear
pending-action: rerun codex-ha-review after contradiction patch
approach: 全量重分级《人生》第4轮中间稿 001-132，再重建正式阅读笔记第4轮。不控长度，不设卡数上限。先在 evidence 写完整第4轮替换草稿并通过覆盖检查，再替换正式笔记第4轮区块。补回外部读者原话、双问题链、阶段回答、可扩写方向、同书内部联动和跨作品联动。
---

# Draft: revise-ren-sheng-round4-notes

## Components (topology ledger)

| id | outcome | status | evidence path |
| --- | --- | --- | --- |
| C1 | 第4轮 001-132 全量去向表，确认每条材料的正式笔记归宿 | active | `.omo/evidence/task-1-round4-inventory.md` |
| C2 | 重新分级文章核心、完整卡、人物主线、轻卡、主题素材，不设数量上限 | active | `.omo/evidence/task-2-round4-classification.md` |
| C3 | 重建正式阅读笔记第4轮结构，避免现有 5+4 框架继续吞材料 | active | `.omo/evidence/task-3-round4-structure.md` |
| C4 | 先写完整第4轮替换草稿，再替换正式笔记区块 | active | `.omo/evidence/task-4-round4-replacement-draft.md` |
| C5 | 重写核心卡和完整卡，补回双问题链、回答、可扩写方向和联动 | active | `.omo/evidence/task-5-round4-core-cards.md`, `.omo/evidence/task-6-round4-complete-cards.md` |
| C6 | 外部读者原话回填到对应卡片，保留原话和简评但不要点赞数或接口字段 | active | `.omo/evidence/task-8-round4-external-comments.md` |
| C7 | 清理 AI-template 句式并做最终内容 QA | active | `.omo/evidence/task-9-round4-tone-cleanup.md`, `.omo/evidence/final-round4-qa.md` |

## Open assumptions (announced defaults)

| assumption | adopted default | rationale | reversible? |
| --- | --- | --- | --- |
| 是否控制正式笔记长度 | 不控制长度 | 用户明确重复说明要深度和质量，长度无所谓 | 是，但不建议 |
| 是否保留点赞数 | 卡片和外部读者条目不保留点赞数；阅读范围标题和最终游标可保留必要定位字段 | 用户明确指出正式笔记里点赞数没有用，但整理游标需要定位 | 是，但不建议 |
| 是否固定核心卡数量 | 不设上限 | 当前错误之一就是人为压缩卡数 | 是，但不建议 |
| 是否重新抓微信读书 | 不重新抓取，只用已完成中间稿 | 第4轮中间稿已完成外部读者补正，当前任务是正式笔记返工 | 是 |
| 是否修改前三轮 | 不修改前三轮正文 | 本任务只修第4轮，前三轮只作格式和连续性参照 | 是，需用户另行要求 |
| 是否自动提交 Git | 不提交 | 用户当前只要求计划和审查 | 是，用户可后续要求提交 |

## Findings (cited - path:lines)

- 根规则要求保留用户真实、有文气的反应，先保留有生命力的句子，再补分析，不能改成说明书：`AGENTS.md:7` 至 `AGENTS.md:15`。
- 根规则要求主卡围绕核心问题展开证据、判断、问题链和文章方向，轻卡不强行深挖：`AGENTS.md:38` 至 `AGENTS.md:45`。
- 根规则要求外部高赞想法只作为外部读者材料，不得替代用户自己的感受、问题和判断：`AGENTS.md:82` 至 `AGENTS.md:91`。
- 根规则要求读书笔记评价包含问题质量、问题链优化、补充角度、可扩写方向、跨作品联动和综合卡片类型：`AGENTS.md:95` 至 `AGENTS.md:106`。
- 《人生》专用提示词写明正式阅读笔记是长期保留文档，中间稿是临时工作台：`路遥/人生/《人生》微信读书提示词.md:11` 至 `路遥/人生/《人生》微信读书提示词.md:17`。
- 《人生》专用提示词要求复杂任务先制定计划，且“不降低数量，不降低深度，只改变执行组织方式”：`路遥/人生/《人生》微信读书提示词.md:870` 至 `路遥/人生/《人生》微信读书提示词.md:903`。
- 第4轮中间稿正文从第4轮整理开始，001 至 132 覆盖第十三章至第二十三章：`路遥/人生/《人生》中间整理稿.md:6029` 至 `路遥/人生/《人生》中间整理稿.md:14677`。
- 第4轮中间稿索引显示材料共 001-132，并已经有轻卡、完整卡候选、主卡候选、外部读者高赞想法候选等完整索引：`路遥/人生/《人生》中间整理稿.md:14733` 至 `路遥/人生/《人生》中间整理稿.md:15009`。
- 第4轮中间稿主卡候选为 009、030、039、048、053、117：`路遥/人生/《人生》中间整理稿.md:14867` 至 `路遥/人生/《人生》中间整理稿.md:14874`。
- 第4轮正式阅读笔记当前只有 5 张文章核心候选和 4 张完整阅读卡，明显少于材料密度：`路遥/人生/《人生》阅读笔记.md:1711` 至 `路遥/人生/《人生》阅读笔记.md:1866`，`路遥/人生/《人生》阅读笔记.md:2004` 至 `路遥/人生/《人生》阅读笔记.md:2129`。

## Decisions (with rationale)

- Decision: 返工不是补丁式修几段，而是重建第4轮正式笔记。Rationale: 当前错误是全局压缩和卡片降级，不是个别字段遗漏。
- Decision: 先做 001-132 去向表。Rationale: 防止再次漏迁、吞卡、用人物线替代完整卡。
- Decision: 核心卡和完整卡数量由材料价值决定。Rationale: 用户明确不要控制长度，前三轮密度也证明少章节可以有更多主卡。
- Decision: 先写完整替换草稿再改正式笔记。Rationale: 这是 Codex reject 后新增的安全阀，防止大规模编辑时又边写边压缩。
- Decision: 外部读者材料采用轻格式原话，不要接口字段。Rationale: 用户要的是外部读者正文和简评，不是点赞数和抓取元数据。
- Decision: AI修正做去模板化，不删除训练骨架。Rationale: 用户反感的是 AI 味句式，不是问题链和分析结构。
- Decision: 计划执行时只改第四轮正式笔记部分。Rationale: 保持范围清楚，避免污染前三轮。
- Decision: 正式笔记只在阅读范围标题和最终游标中保留 `chapterUid` / `range`，卡片正文和外部读者条目一律清掉接口痕迹。Rationale: 避免“不得出现接口字段”和“必须保留整理游标”互相冲突。
- Decision: 先完成 evidence 替换草稿的卡片、外部读者和脚手架强化，再一次性替换正式第4轮区块。Rationale: 避免 Wave 4 提前替换正式笔记、Todo 9 才替换正式笔记的执行矛盾。
- Decision: 最终验证由 agent 执行到通过，不设置中途人工批准门。Rationale: 计划必须可执行，用户只在最终报告后决定是否继续下一阶段。

## Scope IN

- `.omo/plans/revise-ren-sheng-round4-notes.md`
- `.omo/drafts/revise-ren-sheng-round4-notes.md`
- 未来执行时的 `路遥/人生/《人生》阅读笔记.md` 第4轮部分
- 未来执行时的 `.omo/evidence/task-*-round4-*.md` QA 证据

## Scope OUT (Must NOT have)

- 不改 `路遥/人生/《人生》中间整理稿.md`
- 不重新调用微信读书接口
- 不改其他书目
- 不提交 Git，除非用户明确要求
- 不重写前三轮正式笔记正文
- 不在正式阅读笔记的卡片正文或外部读者条目中保留点赞数、抓取状态、bookId 等接口痕迹；阅读范围标题和最终游标例外

## Open questions

- 无阻塞问题。用户已经明确关键偏好：不控长度、不要点赞数、保留外部高赞正文、任务复杂必须先计划。

## Approval gate

status: plan-review-rerun-rejected-and-patched
pending user decision: rerun high-accuracy plan review after contradiction patch, then decide whether to execute.
