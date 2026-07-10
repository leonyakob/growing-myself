# 《人生》第4轮最终内容 QA（Todo 10）

- Plan source: `.omo/plans/revise-ren-sheng-round4-notes.md` Todo 10.
- Formal note audited: `路遥/人生/《人生》阅读笔记.md` 第4轮正式区块。
- Supporting artifacts audited: `.omo/evidence/task-1-round4-inventory.md`, `.omo/evidence/task-2-round4-classification.md`, `.omo/evidence/task-4-round4-replacement-draft.md`, `.omo/evidence/task-5-round4-core-cards.md`, `.omo/evidence/task-6-round4-complete-cards.md`, `.omo/evidence/task-7-round4-light-materials.md`, `.omo/evidence/task-8-round4-external-comments.md`, `.omo/evidence/task-9-round4-tone-cleanup.md`.
- Middle-draft cursor source: `路遥/人生/《人生》中间整理稿.md:15005-15009`.
- Generated excerpt for this QA pass: `.omo/evidence/round4-final-excerpt.md`，对应正式稿 `1701-5400`。
- Scope rule: 本轮只在发现真实、具体、且属于第4轮验收范围内的 defect 时才允许改正式稿。

## PASS / FAIL 总表

| success criterion | result | evidence | notes |
| --- | --- | --- | --- |
| Every source ID `001-132` has a destination | PASS | Primary destination parse found `132/132`; missing `[]`; duplicate primary destinations `0` | 去向由 `## 一` 核心卡 heading、`## 二` 完整卡 heading、`## 三/四/五` 的 `源IDs` 分组 heading 共同解析。 |
| Final formal-note structure matches the accepted migration shape | PASS | `15` article-core, `67` complete cards, `27` 人物主线 source IDs, `15` light source IDs, `8` theme/material source IDs | 与 Todo 2 重分级和本轮既定结构完全一致。 |
| No fixed length cap, no 5+4 compression regression | PASS | Current round4 excerpt is `3700` lines; Todo 1 记录的旧压缩段参考长度是 `539` lines (`1701-2239`) | 强卡规模仍是 `15 + 67`，没有退回旧的 `5 + 4` 压缩形状。 |
| No category drift vs classification ledger | PASS | Category mismatches vs `.omo/evidence/task-2-round4-classification.md` = `0` | 每个 source ID 都落在 Todo 2 指定的类别里。 |
| No category or heading-title drift vs accepted replacement draft | PASS | Primary-category mismatches vs `.omo/evidence/task-4-round4-replacement-draft.md` = `0`; heading-title diffs = `0` | tone cleanup 只改卡内 prose，没有破坏 accepted replacement draft 的 heading 结构。 |
| Protected complete cards remain independent | PASS | `061, 076, 079, 081, 089, 091, 095, 099, 103, 104, 111, 116, 119, 124, 125` 全部仍在 `## 二、完整阅读卡` | 没有被人物主线、轻卡或素材库重新吞掉。 |
| Major-card scaffolding is complete | PASS, after fix | `15/15` article-core cards and `37/37` `Full/Strengthened-T6` complete cards now contain four-part structure and required scaffold markers | 本轮修复了 `086, 087, 089, 091` 的标签型 defect，见下文 defect log。 |
| No forbidden interface traces leaked into round4 external-reader material | PASS | In `.omo/evidence/round4-final-excerpt.md`, grep for `点赞数|抓取状态|官方版定位|bookId=|chapterUid=|range=|有读者说` now returns exactly `1` matching line, and that line is the allowed final cursor exception | 除最终游标 `- 第二十三章 / `chapterUid=26` / `range=8942-8951` 之后。` 外，第4轮卡片正文和外部读者材料仍为 `0` 命中。 |
| No placeholder-style external-comment residue | PASS | `有读者说` 在第4轮 excerpt 内命中 `0` 次 | 外部读者材料仍是原话加简评，没有被压成摘要占位句。 |
| `128` dual-placement rule is preserved | PASS | `128` 的 primary destination 仍在 `## 五、主题素材库 / 待回看 - 6. 乡土接纳与现实分歧素材`；外部读者分歧只留在 `## 六` | 没有 primary destination 重复写，也没有把同一组三条原话双贴。 |
| Intentional non-migrations are named | PASS | None | Todo 2 的 `explicit non-migration reason` 计数仍为 `0`。 |
| Final cursor remains correct | PASS | Formal note tail is `- 第二十三章 / `chapterUid=26` / `range=8942-8951` 之后。` and `- 当前最后一条划线原文：“我的亲人哪……”` | 与 plan 要求的 allowed exception 精确一致。 |

## Defect log

### Defect 1，四张重点完整卡的脚手架标签不统一

- 首次机械审计命中：`086, 087, 089, 091` 被判定缺少 `问题链升级（沿原问题）`。
- Root cause：这四张卡的分析内容已经到位，但标签写成了 `问题链升级（沿原想法）`。最终 QA 合同要求的是显式 `沿原问题` 字段名，所以会被机械审计判成缺项。
- Fix applied：在 `路遥/人生/《人生》阅读笔记.md` 内，仅把这四张卡的该字段名从 `沿原想法` 改成 `沿原问题`。
- Scope check：未改去向，未改判断，未改外部读者原话，未改前三轮。
- Recheck result：PASS，修后 `15/15` article-core 与 `37/37` `Full/Strengthened-T6` complete cards 均通过脚手架扫描。

## Intentional exceptions, not defects

- `128` 继续保留双重用途。source text 留在 `## 五`，全局分歧原话只留在 `## 六`。
- 最终游标现在显式保留唯一允许的元数据例外：`- 第二十三章 / `chapterUid=26` / `range=8942-8951` 之后。` 其余第4轮正文、卡片、外部读者材料仍不允许泄漏界面字段。
- Todo 6 已明示的 `Lighter-A/B/C` 完整卡仍保持较轻。此次 final QA 只强制 article-core 和 `Full/Strengthened-T6` complete cards 满足全脚手架，不把故意保中的完整卡误判成缺陷。

## Mechanical audit facts

- Generated excerpt: `.omo/evidence/round4-final-excerpt.md`
- Excerpt span: `路遥/人生/《人生》阅读笔记.md:1701-5400`
- Excerpt line count: `3700`
- Legacy compressed reference span from Todo 1: `1701-2239`，共 `539` 行
- Round4 section counts:
  - article-core headings: `15`
  - complete-card headings: `67`
  - 人物主线 source IDs: `27`
  - light-card source IDs: `15`
  - theme/material source IDs: `8`
- Primary destination coverage: `132/132`
- Primary destination duplicates: `0`
- Category mismatches vs Todo 2: `0`
- Category mismatches vs accepted replacement draft: `0`
- Heading-title diffs vs accepted replacement draft: `0`
- Allowed `chapterUid/range` hit lines inside the round4 excerpt: `1`（仅最终 cursor 一行）

## Residual risk for Final Verification Wave

- The round4 excerpt still contains many natural `不是……而是……` style lines. The mechanical count for the whole excerpt is `266`, but these hits include user original writing, external-reader original quotes, and some retained analytical contrasts already justified in Todo 9. No concrete new regression was found in this QA pass. Final Verification Wave should still re-scrutinize whether any remaining contrastive line now feels templated after the scaffold-label fix.
