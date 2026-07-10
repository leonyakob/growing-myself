# revise-ren-sheng-round4-notes - Work Plan

## TL;DR (For humans)

**What you'll get:** 一次针对《人生》第4轮正式阅读笔记的深度返工：不控长度，重新盘点第4轮全部材料，把被压缩掉的主卡、完整卡、外部读者原话、问题链、回答和可扩写方向补回正式笔记。

**Why this approach:** 第4轮的问题不是局部漏几句，而是迁移时整体压缩过度。正确修法是先全量重分级 001-132，再按材料价值重建第4轮正式笔记结构，并先写完整替换草稿，草稿通过覆盖检查后才替换正式笔记。

**What it will NOT do:** 不控制字数，不设置核心卡或完整卡上限，不把外部读者原话改成“有读者说”的摘要，不在卡片或外部读者条目里保留点赞数、bookId、chapterUid、抓取状态等接口痕迹，不改动前三轮正文。

**Effort:** XL
**Risk:** Medium - 材料量大，必须用覆盖表和替换草稿防止再次摘要化、吞卡或漏卡。
**Decisions to sanity-check:** 是否接受“全量重分级 + 先写替换草稿 + 深度扩容”的返工方式；是否先继续跑高精度审查到 OKAY，再开始执行。

Your next move: 等高精度计划审查通过后，再选择是否开始执行返工。

---

> TL;DR (machine): XL doc-only revision plan for `路遥/人生/《人生》阅读笔记.md` round 4, source `路遥/人生/《人生》中间整理稿.md` round 4, no length cap, full reclassification, evidence draft before formal replacement.

## Scope

### Must have

- 只返工 `路遥/人生/《人生》阅读笔记.md` 中 `## 第4轮阅读笔记：第十三章至第二十三章` 及其下属第4轮部分。
- 以 `路遥/人生/《人生》中间整理稿.md` 的第4轮材料 001-132 为唯一源材料，不重新抓微信读书接口，不改中间稿。
- 先做第4轮材料全量去向表：001-132 每条都必须有正式笔记去向，包括文章核心候选、完整阅读卡、人物主线卡、轻卡存档、主题素材库、暂不迁移原因。
- 不设文章核心候选数量上限，不设完整阅读卡数量上限，不控制笔记长度。最终卡片数量由材料价值决定。
- 至少复核中间稿已标出的 6 张主卡候选：009、030、039、048、053、117。不得因现有正式稿已有 5 张核心卡就跳过 030。
- 逐条复核中间稿完整卡候选，重点防止高价值完整卡被人物总卡、轻卡或素材库吞掉。
- 大规模改写前，先在 `.omo/evidence/task-4-round4-replacement-draft.md` 写出新的第4轮完整替换草稿，并附 001-132 去向汇总。草稿覆盖检查通过后，才替换正式笔记中的第4轮区块。
- 正式阅读笔记里的核心卡、主卡和关键完整卡必须保留四段式：`我自己写的内容 / AI评价 / AI修正 / AI补充`。
- `我自己写的内容` 必须完整保留用户原想法的语气、怒气、疑问、口语和现场感，只允许极少量错别字修正。
- 每张核心卡、主卡和关键完整卡必须恢复：
  - 问题链升级（沿原问题）
  - 当前回答（沿原问题）
  - 另一条升级问题链（新增角度）
  - 当前回答（新增角度）
  - 可扩写方向
  - 同书内部联动
  - 跨作品联动
- 每张核心卡、主卡和关键完整卡应保留 1-3 条最有价值的外部读者原话，格式轻量化：`回声 / 补充 / 挑战 / 校正 / 反向提醒：“原话” 简评：...`。
- 正式笔记中的外部读者材料不保留点赞数，不保留抓取状态，不保留 bookId，不保留 chapterUid，不保留 range。唯一例外：第4轮阅读范围标题和文末“下次接着整理位置”游标可以保留必要的 `chapterUid` / `range`。
- 外部读者原话不能统一挪到文末素材库。高价值外部评论应跟随对应卡片出现；文末只保留无法归入单卡但有全局分歧价值的少量外部材料。
- AI修正和AI补充必须减少模板化表达，重点清理连续出现的“不是……而是……”“不只是……而是……”“真正……不是……而是……”句式。
- 保留用户有生命力的表达，不把笔记改成说明书或论文腔。
- 文末只保留最新下次接着整理位置：第二十三章 / `chapterUid=26` / `range=8942-8951` 之后。
- 返工完成后做内容 QA，不只做 Markdown 或 Git 检查。

### Must NOT have (guardrails, anti-slop, scope boundaries)

- 不控制字数，不压缩为“精选版”，不以正式笔记整洁为由删除训练结构。
- 不设置“核心卡最多 N 张”“完整卡最多 N 张”“每卡最多 N 字”等限制。
- 不把第4轮 132 条材料再次压成摘要清单后就宣布完成。
- 不让 AI修正覆盖用户原文，不改写用户原想法为 AI 口吻。
- 不把外部高赞想法只写成“有读者说……”。必须保留有价值原话。
- 不在正式笔记的卡片正文、AI评价/修正/补充、外部读者条目里出现点赞数、抓取状态、官方版定位、bookId、chapterUid、range 等接口痕迹。唯一例外是第4轮阅读范围标题和文末游标。
- 不把所有外部读者评论统一挪到文末。
- 不把轻卡强行拔高。轻卡可以轻，但高价值完整卡不能被降级成轻卡。
- 不为了去 AI 味删掉问题链、回答、扩写方向和联动。要删模板腔，不删训练骨架。
- 不大幅修改前三轮内容。
- 不提交、不推送，除非用户后续明确要求。

## Verification strategy

> Zero human intervention - all verification is agent-executed.

- Test decision: none + document QA. 这是阅读笔记返工，不写程序测试；验证通过可执行覆盖表、限定区块搜索、逐卡清单和最终阅读面 QA 完成。禁止只写“人工检查通过”。
- Evidence:
  - `.omo/evidence/task-1-round4-inventory.md`
  - `.omo/evidence/task-2-round4-classification.md`
  - `.omo/evidence/task-3-round4-structure.md`
  - `.omo/evidence/task-4-round4-replacement-draft.md`
  - `.omo/evidence/task-5-round4-core-cards.md`
  - `.omo/evidence/task-6-round4-complete-cards.md`
  - `.omo/evidence/task-7-round4-light-materials.md`
  - `.omo/evidence/task-8-round4-external-comments.md`
  - `.omo/evidence/task-9-round4-tone-cleanup.md`
  - `.omo/evidence/round4-final-excerpt.md`
  - `.omo/evidence/final-round4-qa.md`
- Required checks:
  - The 001-132 ledger must contain all numbers 001 through 132. The final QA must list any missing-number query result as empty, not merely assert full coverage.
  - Extract the final fourth-round block to `.omo/evidence/round4-final-excerpt.md`, starting at `## 第4轮阅读笔记：第十三章至第二十三章` and ending after the latest “下次接着整理位置” cursor for 第4轮, or before the next top-level round if one exists.
  - In `.omo/evidence/round4-final-excerpt.md`, search for `点赞数|抓取状态|官方版定位|bookId=|chapterUid=|range=`. Allowed hits are only the reading-range heading and the single final cursor line; card bodies and external-reader entries must have zero hits. The final cursor must exactly point to 第二十三章 / `chapterUid=26` / `range=8942-8951` 之后.
  - For every retained article-core card and key complete card, the evidence checklist must mark present or intentionally not applicable for: `问题链升级（沿原问题）`, `当前回答（沿原问题）`, `另一条升级问题链（新增角度）`, `当前回答（新增角度）`, `可扩写方向`, `同书内部联动`, `跨作品联动`.
  - Search the final fourth-round block for `有读者说` and reject any use that replaced a source external-reader original comment instead of preserving the original comment.
  - Search the final fourth-round block for `不是.*而是`; for each hit, record whether it is necessary or rewrite it.

## Execution strategy

### Parallel execution waves

- Wave 1: Inventory and classification. Build the 001-132 destination table, compare fourth-round formal output against middle draft, identify all cards wrongly dropped or downgraded.
- Wave 2: Structure design. Decide the new 第4轮 formal-note architecture from material value, not from a fixed card count.
- Wave 3: Evidence draft. Write the complete replacement 第4轮 section in `.omo/evidence/task-4-round4-replacement-draft.md`; do not edit the formal note yet.
- Wave 4: Draft strengthening passes. Improve the evidence replacement draft for core cards, complete cards, light/material sections, external-reader original comments, and scaffolding while the formal note remains untouched.
- Wave 5: Formal replacement, tone cleanup, and final content QA. Replace the formal 第4轮 block only after draft coverage passes, then verify source coverage, no length compression, no interface metadata leakage, scaffold completeness, tone cleanup, and cursor preservation.

### Dependency matrix

| Todo | Depends on | Blocks | Can parallelize with |
| --- | --- | --- | --- |
| 1 | none | 2, 3, 4 | none |
| 2 | 1 | 3, 4 | none |
| 3 | 2 | 4 | none |
| 4 | 3 | 5, 6, 7, 8, 9, 10 | none |
| 5 | 4 | 8, 9, 10 | 6 after draft exists |
| 6 | 4 | 8, 9, 10 | 5 after draft exists |
| 7 | 4 | 9, 10 | 5 and 6 after draft exists |
| 8 | 5, 6 | 9, 10 | 7 after card destinations known |
| 9 | 5, 6, 7, 8 | 10 | none |
| 10 | 9 | final verification | none |

## Todos

> Implementation + Test = ONE todo. Never separate.

- [x] 1. Build the fourth-round 001-132 destination ledger
  What to do / Must NOT do: Read `路遥/人生/《人生》中间整理稿.md` 第4轮正文 and 第4轮索引, then create `.omo/evidence/task-1-round4-inventory.md` listing every item 001-132 with middle-draft classification, source location, current formal-note destination if any, suspected correct destination, whether external reader material exists, and whether the item contains a middle-draft `可扩写方向`. Must NOT decide by current formal-note structure.
  Parallelization: Wave 1 | Blocked by: none | Blocks: 2, 3, 4
  References: `路遥/人生/《人生》中间整理稿.md:6029`, `路遥/人生/《人生》中间整理稿.md:6055`, `路遥/人生/《人生》中间整理稿.md:14677`, `路遥/人生/《人生》中间整理稿.md:14733`, `路遥/人生/《人生》中间整理稿.md:14735`, `路遥/人生/《人生》中间整理稿.md:14792`, `路遥/人生/《人生》中间整理稿.md:14867`, `路遥/人生/《人生》中间整理稿.md:14880`, `路遥/人生/《人生》中间整理稿.md:15003`, `路遥/人生/《人生》阅读笔记.md:1701`
  Acceptance criteria: `.omo/evidence/task-1-round4-inventory.md` contains rows for 001 through 132, with no missing numbers and no blank destination field.
  QA scenarios: happy: create a `Missing IDs` line in the evidence file and leave it empty only if all 132 IDs are present; failure: if any ID is missing, stop and fill its row before Todo 2.
  Commit: N | document evidence only

- [x] 2. Reclassify fourth-round materials without card-count caps
  What to do / Must NOT do: Using the ledger from Todo 1, reclassify every fourth-round item into article-core candidate, complete reading card,人物主线卡, light card, theme/material bank, or explicit non-migration reason. Must NOT use a quota. Must promote any item that can support an independent question chain or article direction.
  Parallelization: Wave 1 | Blocked by: 1 | Blocks: 3, 4
  References: `AGENTS.md:38`, `AGENTS.md:70`, `AGENTS.md:95`, `路遥/人生/《人生》微信读书提示词.md:280`, `路遥/人生/《人生》微信读书提示词.md:836`, `路遥/人生/《人生》中间整理稿.md:14792`, `路遥/人生/《人生》中间整理稿.md:14867`
  Acceptance criteria: `.omo/evidence/task-2-round4-classification.md` explains each promoted, retained, downgraded, or deferred category; it explicitly states there is no core-card or complete-card maximum.
  QA scenarios: happy: all high-value complete-card candidates have a reasoned destination; failure: if a middle-draft complete card with `可扩写方向` is categorized as light or material bank, record a text-based reason and flag it for Todo 3 review.
  Commit: N | document evidence only

- [x] 3. Design the replacement structure for the formal fourth-round section
  What to do / Must NOT do: Draft the target outline for `## 第4轮阅读笔记：第十三章至第二十三章` based on reclassification. Preserve the current reading range and cursor. The outline should include expanded article-core candidates, expanded complete cards,人物主线 cards only where they do not swallow independent cards, light-card archive, theme/material bank, and global external-reader notes only for non-card-specific materials. Must NOT keep the current 5 core + 4 complete-card shape if the ledger shows it is too small.
  Parallelization: Wave 2 | Blocked by: 2 | Blocks: 4
  References: `路遥/人生/《人生》阅读笔记.md:1701`, `路遥/人生/《人生》阅读笔记.md:1705`, `路遥/人生/《人生》中间整理稿.md:14867`, `路遥/人生/《人生》中间整理稿.md:14792`, `路遥/人生/《人生》微信读书提示词.md:785`
  Acceptance criteria: `.omo/evidence/task-3-round4-structure.md` contains the new heading outline and lists which source IDs feed each heading.
  QA scenarios: happy: every article-core and complete-card heading in the proposed outline has source IDs; failure: any catch-all bucket must be split or justified with exact source IDs.
  Commit: N | document evidence only

- [x] 4. Draft the complete replacement fourth-round section in evidence before editing the formal note
  What to do / Must NOT do: Create `.omo/evidence/task-4-round4-replacement-draft.md` containing the complete proposed replacement for `## 第4轮阅读笔记：第十三章至第二十三章`, including headings, all rebuilt cards, light-card archive, material bank, card-specific external reader entries, any global external reader notes, final cursor, and a 001-132 destination summary. Must NOT edit `路遥/人生/《人生》阅读笔记.md` during this todo.
  Parallelization: Wave 3 | Blocked by: 3 | Blocks: 5, 6, 7, 8, 9, 10
  References: `.omo/evidence/task-1-round4-inventory.md`, `.omo/evidence/task-2-round4-classification.md`, `.omo/evidence/task-3-round4-structure.md`, `路遥/人生/《人生》中间整理稿.md:6029`, `路遥/人生/《人生》中间整理稿.md:14677`, `路遥/人生/《人生》中间整理稿.md:14733`
  Acceptance criteria: `.omo/evidence/task-4-round4-replacement-draft.md` contains a full replacement section and a source-ID mapping table; no formal-note file changes during this todo.
  QA scenarios: happy: the draft's source-ID mapping covers all IDs marked for migration; failure: if a promoted source ID is omitted, add it as a card or write an explicit non-migration reason in the mapping table.
  Commit: N | evidence draft only

- [x] 5. Verify and strengthen article-core and主卡 cards in the replacement draft
  What to do / Must NOT do: In the replacement draft, include all reclassified article-core cards, not just the current five. For each card preserve user original writing, then write AI评价, AI修正, AI补充, split question chains, split current answers,可扩写方向,同书内部联动,跨作品联动, and 1-3 relevant external reader original comments where available. Must NOT delete user anger, jokes, or rhetorical bite.
  Parallelization: Wave 4 | Blocked by: 4 | Blocks: 8, 9, 10
  References: `路遥/人生/《人生》中间整理稿.md:14869`, `路遥/人生/《人生》中间整理稿.md:14870`, `路遥/人生/《人生》中间整理稿.md:14871`, `路遥/人生/《人生》中间整理稿.md:14872`, `路遥/人生/《人生》中间整理稿.md:14873`, `路遥/人生/《人生》中间整理稿.md:14874`, `路遥/人生/《人生》微信读书提示词.md:422`, `路遥/人生/《人生》微信读书提示词.md:690`
  Acceptance criteria: `.omo/evidence/task-5-round4-core-cards.md` lists every article-core card and marks all required scaffold fields present or intentionally not applicable.
  QA scenarios: happy: sample at least 3 rebuilt article-core cards against their middle-draft source and record exact source IDs; failure: if any article-core card lacks external comments despite source having retained comments, record why the comments were filtered.
  Commit: N | evidence/content edit later only

- [x] 6. Verify and strengthen complete reading cards, preventing人物主线 swallowing independent cards
  What to do / Must NOT do: In the replacement draft, expand complete reading cards from the reclassification ledger. Cards such as 半截分手话, 巧珍劳动复原, 我还得活人, 克南母亲, 克南坦白, 叔父退回去, 县城变小, 火柴动作, 黄亚萍牺牲, 更爱巧珍, 并非结局, 巧珍求情, 德顺生活哲学 and similar high-value entries must be independently considered.人物主线 cards may summarize arcs, but must not replace independent complete cards.
  Parallelization: Wave 4 | Blocked by: 4 | Blocks: 8, 9, 10
  References: `路遥/人生/《人生》中间整理稿.md:12354`, `路遥/人生/《人生》中间整理稿.md:12671`, `路遥/人生/《人生》中间整理稿.md:12860`, `路遥/人生/《人生》中间整理稿.md:12925`, `路遥/人生/《人生》中间整理稿.md:13234`, `路遥/人生/《人生》中间整理稿.md:13366`, `路遥/人生/《人生》中间整理稿.md:13864`, `路遥/人生/《人生》中间整理稿.md:13934`, `路遥/人生/《人生》中间整理稿.md:14061`, `路遥/人生/《人生》中间整理稿.md:14187`, `路遥/人生/《人生》中间整理稿.md:14551`, `路遥/人生/《人生》阅读笔记.md:2004`
  Acceptance criteria: `.omo/evidence/task-6-round4-complete-cards.md` lists every middle-draft complete-card candidate and its final destination; every retained complete card has required scaffolding unless explicitly marked as lighter完整卡 with reason.
  QA scenarios: happy: compare formal-note complete-card count before and after and record why the new count matches material value; failure: no source item with a middle-draft `可扩写方向` may disappear without explicit destination reason.
  Commit: N | evidence/content edit later only

- [x] 7. Rehome light cards,人物主线 cards, and theme materials without losing reading flow
  What to do / Must NOT do: In the replacement draft, rebuild the fourth-round light-card archive,人物主线 summaries, and theme/material bank after core and complete cards are decided. Light cards should preserve reading现场感 but not be overexpanded. Theme bank should only hold materials that truly serve later essays and do not yet form complete cards.
  Parallelization: Wave 4 | Blocked by: 4 | Blocks: 9, 10
  References: `路遥/人生/《人生》中间整理稿.md:14735`, `路遥/人生/《人生》阅读笔记.md:1871`, `路遥/人生/《人生》阅读笔记.md:2132`, `路遥/人生/《人生》阅读笔记.md:2204`, `AGENTS.md:38`
  Acceptance criteria: `.omo/evidence/task-7-round4-light-materials.md` states why each light-card group is light and why each theme-bank item is not a full card.
  QA scenarios: happy: spot-check at least 10 light-card source IDs against final destinations; failure: if a source light-card actually has a strong question chain or external challenge, reopen classification and move it upward.
  Commit: N | evidence/content edit later only

- [x] 8. Insert external reader original comments in the right cards, with no likes or interface traces
  What to do / Must NOT do: For each retained core and important complete card in the replacement draft, choose 1-3 most useful external reader original comments from the middle draft. Keep the original comment text. Add a concise relation label and a one-sentence evaluation. Must NOT include点赞数, bookId, chapterUid, range, official positioning, or抓取状态. Must NOT summarize the external comments into “有读者说”.
  Parallelization: Wave 4 | Blocked by: 5, 6 | Blocks: 9, 10
  References: `AGENTS.md:82`, `路遥/人生/《人生》中间整理稿.md:14880`, `路遥/人生/《人生》中间整理稿.md:14883`, `路遥/人生/《人生》中间整理稿.md:14990`, `路遥/人生/《人生》微信读书提示词.md:762`, `路遥/人生/《人生》微信读书提示词.md:849`
  Acceptance criteria: `.omo/evidence/task-8-round4-external-comments.md` maps source IDs to chosen external comments and confirms no点赞数 or interface metadata appears in the replacement draft's external-reader entries.
  QA scenarios: happy: every card with source external comments has either 1-3 selected original comments or a written filter reason; failure: if more than 3 comments are needed for a card, justify the exception by distinct interpretive directions.
  Commit: N | evidence/content edit later only

- [x] 9. Apply the replacement draft to the formal note and clean AI-template tone
  What to do / Must NOT do: After Todos 4-8 pass, replace only the formal note's fourth-round section with the evidence draft. Then review the rebuilt fourth-round section for repeated `不是……而是……`, `不只是……而是……`, abstract labels, and explanatory classroom tone. Rewrite template-heavy sentences into text-grounded, vivid, but accurate prose. Must NOT remove analysis depth, question chains, current answers, or external-reader原话.
  Parallelization: Wave 5 | Blocked by: 5, 6, 7, 8 | Blocks: 10
  References: `AGENTS.md:13`, `AGENTS.md:145`, `路遥/人生/《人生》微信读书提示词.md:463`, `路遥/人生/《人生》微信读书提示词.md:474`, `路遥/人生/《人生》阅读笔记.md:1701`, `路遥/人生/《人生》阅读笔记.md:2229`
  Acceptance criteria: `.omo/evidence/task-9-round4-tone-cleanup.md` records before/after examples of at least 10 high-impact tone cleanups or states fewer were needed after reconstruction.
  QA scenarios: happy: all remaining `不是.*而是` hits in the final fourth-round excerpt are listed as necessary or rewritten; failure: if one card has repeated template sentences, rewrite before final QA.
  Commit: N | no commit unless user requests

- [x] 10. Final fourth-round content QA and cursor verification
  What to do / Must NOT do: Verify the full fourth-round section against the plan, the middle-draft ledger, and the user complaints. Confirm every source item 001-132 has a destination, no fixed length cap was applied, no interface traces leaked into formal note external comments, all major cards have full scaffolding, and the final cursor remains correct.
  Parallelization: Wave 5 | Blocked by: 9 | Blocks: final verification
  References: `.omo/evidence/task-1-round4-inventory.md`, `.omo/evidence/task-2-round4-classification.md`, `.omo/evidence/task-4-round4-replacement-draft.md`, `路遥/人生/《人生》阅读笔记.md:1701`, `路遥/人生/《人生》中间整理稿.md:15005`
  Acceptance criteria: `.omo/evidence/final-round4-qa.md` contains a pass/fail table for all success criteria and names any intentional non-migrations.
  QA scenarios: happy: run the Required checks listed in `## Verification strategy` and paste key findings into evidence; failure: any missing scaffolding or missing source destination triggers a targeted fix before declaring done.
  Commit: N | no commit unless user explicitly requests

## Final verification wave

> Runs after ALL todos. ALL must APPROVE before final report. No human approval gate is required inside execution; if any verifier rejects, fix the document and rerun the verifier before reporting completion.

- [x] F1. Plan compliance audit: Verify the final fourth-round section satisfies every Must have and Must NOT have above, especially no length cap and no fixed card count.
- [x] F2. Source coverage audit: Verify 001-132 all appear in the destination ledger and every migrated or non-migrated decision is accounted for.
- [x] F3. Reading-surface QA: Read the final fourth-round note as a long-form reading notebook and verify it no longer feels like a compressed summary.
- [x] F4. Scope fidelity: Confirm only the fourth-round section of `路遥/人生/《人生》阅读笔记.md` changed, plus `.omo/evidence` artifacts created during execution.

## Commit strategy

- Do not commit automatically.
- If the user later requests Git commit and push, use `GIT_MASTER=1` for every git command.
- Stage only the intended files: `路遥/人生/《人生》阅读笔记.md` and any user-approved `.omo/evidence` or plan artifacts if the user wants them tracked. Do not stage unrelated reading materials.
- Expected commit style if requested later: plain English or Chinese matching recent repo style, for example `Update 人生 fourth-round reading notes revision`.

## Success criteria

- 第4轮正式笔记不再是 5 张核心卡 + 4 张完整卡的压缩版本，而是按 001-132 材料价值重新分级后的完整返工版本。
- 所有第4轮中间稿材料都有去向说明。
- 高价值主卡和完整卡不被人物主线、轻卡或素材库吞掉。
- 核心卡、主卡和关键完整卡都包含沿原问题问题链、当前回答、新增角度问题链、新增角度回答、可扩写方向、同书内部联动、跨作品联动。
- 外部读者材料保留原话和简评，但不保留点赞数或接口字段。
- 用户原文表达没有被 AI修正覆盖。
- AI-template 句式明显减少，文气和文本落点增强。
- 第4轮最终游标正确：第二十三章 / `chapterUid=26` / `range=8942-8951` 之后。
- 未修改其他书目，未误改前三轮正文。
