# Task 4 evidence: whole-book consolidation model fixture QA

Verdict: PASS.

Scope: hands-on prompt/docs QA only. No WeRead API calls, no reading-note edits, and no prompt-file edits were performed in this task. The only edited file is this evidence ledger.

## Inputs read

- Approved plan: `.omo/plans/add-whole-book-consolidation-model.md`, especially task 4 acceptance criteria at lines 179-184 and final success criteria at lines 201-210.
- Fixture matrix: `.omo/evidence/fixtures/add-whole-book-consolidation-model.md`, all nine cases at lines 5-215.
- Generic prompt: `微信读书通用提示词.md`, fourth-stage model at lines 977-1106 and shortcut at lines 1204-1208.
- 《人生》 prompt: `路遥/人生/《人生》微信读书提示词.md`, current top flow at lines 34-57, book-specific fourth-stage model at lines 952-1151, auxiliary preamble at line 1207, and shortcut at lines 1245-1248.

## Fixture dry-run table

| # | Fixture case | Deterministic outcome from fixture | PASS/FAIL | Matching prompt rule(s) | Forbidden failure blocked |
|---|---|---|---|---|---|
| 1 | Partially migrated card | `source status`: 已在正式笔记中，但需补 readable evidence / 用户原句 / 外部原话；archive: 保留为完整卡，只补字段；formal note: 在阅读现场档案补回引文和用户原句；article index: 用短引文和原始触动引用，不复制整卡。 | PASS | Generic prompt: internal/formal boundary and original user text preservation at lines 992-999; source-status axis at lines 1004-1013; archive-first/index-second model at lines 1015-1022. 《人生》 prompt: boundary at lines 969-981; partial-migration branch at lines 989-990 and 998-1001. | The fixture forbids treating an AI summary as a complete card; both prompts require readable evidence and preserve `我自己写的内容`. |
| 2 | Duplicate same quote + same insight | `source status`: 中间稿与正式稿重复，需合并或建立修订链；archive: choose one representative card, merge duplicate only in internal ledger; formal note: keep one representative card; article index: cite representative card only. | PASS | Generic prompt: duplicate decision tree at lines 1056-1070, especially same quote + same judgment representative handling at lines 1065-1066. 《人生》 prompt: duplicate rules at lines 1078-1100. | The fixture forbids placing both duplicate cards in the formal note; both prompts route duplicate metadata to the internal ledger, not reader-facing text. |
| 3 | Duplicate same quote + changed judgment | `source status`: 正式稿旧判断已被后文修正，保留为阅读轨迹；archive: build revision chain, preserve early and later cards; formal note: current card plus concise trajectory; article index: default to later judgment, link early misreading only for reading-trajectory article. | PASS | Generic prompt: corrected judgment must become a revision chain at line 1066 and misreading structure at lines 1071-1081. 《人生》 prompt: changed judgment cannot be merged into one smooth conclusion at lines 1099-1115. | The fixture forbids silently deleting the early reading; both prompts require `当时的读法` and later correction when judgment changes. |
| 4 | Same scene with different source ID/range | `source status`: duplicate / merge-or-chain; archive: treat as one scene card if action chain and tension match; formal note and article index: use scene name plus quote snippet, not source ID/range. | PASS | Generic prompt: readable anchors cannot be `source ID`/`range` at line 996; same scene with different technical coordinates is one scene card at line 1067. 《人生》 prompt: article anchor must be readable, not `source ID`/`range`, at lines 1041 and 1125; same-scene rule at line 1101. | The fixture forbids counting the same scene twice just because technical source coordinates differ; both prompts distinguish text scene from technical location. |
| 5 | Early misreading corrected later | `source status`: 正式稿旧判断已被后文修正，保留为阅读轨迹；archive: keep misreading chain; formal note: write `当时的读法 / 后来出现的证据 / 全书后的修正 / 误读的价值`; article index: use correction by default, use misreading chain only for reading-process article. | PASS | Generic prompt: fourth stage must preserve early shallow judgments and later corrections at line 990; misreading structure and article-use rule at lines 1071-1081. 《人生》 prompt: misreading structure and article-use rule at lines 1105-1115; QA requires preserving reading change at lines 1145-1150. | The fixture forbids treating the misreading as waste; both prompts make reading trajectory a first-class output section. |
| 6 | External high-like challenge | `source status`: 已在正式笔记中，结构合格，只补文章索引；archive: user card remains the main card and external thought is a challenge relation; formal note: user card first, optional external challenge; article index: user card as main anchor plus challenge note. | PASS | Generic prompt: external echo/challenge cannot replace user card at line 1069; external material cannot become user judgment at lines 1086-1088. 《人生》 prompt: external material cannot become first-person judgment at lines 1121-1123. | The fixture forbids rewriting an external comment as “我其实一直觉得...”; both prompts keep external-reader identity explicit. |
| 7 | External-only strong comment | `source status`: 仅外部读者材料，无用户卡片锚点；archive: internal ledger only, independent/external, wait for user anchor; formal note: not in reading-site archive; article index: cannot be main evidence until linked to a user card. | PASS | Generic prompt: external-only material is internal-ledger first and cannot be article-index main anchor at line 1086. 《人生》 prompt: external-only strong material goes to internal ledger or pending/discard area, not formal main evidence, at line 1122; source-status value at lines 998-1005. | The fixture forbids fabricating a user card from external-only material; both prompts require a user-card anchor before formal/index use. |
| 8 | Light card used as article evidence but not upgraded | `source status`: 中间稿已优化，尚未迁移；archive: 保留为轻卡; formal note: keep it as light card; article index: may cite as atmosphere/style/opening evidence. | PASS | Generic prompt: light card cited by article index may remain light at line 1085; archive identity precedes article links at lines 1015-1022. 《人生》 prompt: article-index use does not upgrade archive identity at lines 1020-1031, especially line 1028. | The fixture forbids expanding a light card into a fake complete card; both prompts preserve light-card status. |
| 9 | Final-note bloat prevention / archive-discard-with-reason | `source status`: 已在正式笔记中，结构合格，只补文章索引；archive: 归档不迁移 with reason; formal note: omit from body, at most one short reason in pending/discard section; article index: do not include weak duplicate. | PASS | Generic prompt: formal skeleton includes `待回看 / 归档不迁移` at lines 1050-1054; not every card must enter body and article index must not copy full card bodies or weak duplicates at lines 1089-1090. 《人生》 prompt: pending/discard section at lines 1074-1075 and no re-copying stable cards at line 1127. | The fixture forbids padding the formal note with low-information duplicate material; both prompts explicitly prevent bloat. |

All nine fixture cases have deterministic `source status`, `archive treatment`, `formal-note treatment`, `article-index treatment`, and a blocked forbidden failure. There are no ambiguous or subjective-approval-dependent cases.

## Cross-file consistency checks

### 1. Reading-site archive appears before article index

PASS.

- Generic prompt: the fourth-stage flow defines `阅读现场档案 + 文章素材索引` at lines 977-982; the two-layer model lists `阅读现场档案` first and `文章素材索引` second at lines 1019-1022; the formal skeleton puts `### 一、阅读现场档案` before `### 二、文章素材索引` at lines 1038-1042; line 1054 explicitly says the archive must appear before the index.
- 《人生》 prompt: the book-specific model defines the same order at lines 969-981; section 11.5 says the formal note first handles `阅读现场档案`, then `文章素材索引` at lines 1033-1041; the skeleton puts archive before index at lines 1048-1060.

### 2. Article index does not cite only source IDs/ranges or copy full card bodies

PASS.

- Generic prompt: formal anchors must be readable card title / chapter or scene / quote snippet / user sentence fragment, and `source ID` or `range` cannot be reader-facing anchors at line 996; article index shape requires associated card, original touch, evidence role, and missing-evidence field at lines 1024-1031; QA forbids source IDs/ranges in article anchors and copying whole card bodies at lines 1099-1101.
- 《人生》 prompt: article-index unit is a readable card anchor, not `source ID` or `range`, at line 1041; formal article anchors cannot be `ID 003`, `source ID 17`, or `range 233-245` at line 1125; QA forbids copying whole cards or using technical anchors at lines 1147-1148.

### 3. Light cards are not forcibly upgraded

PASS.

- Generic prompt: light cards cited by the article index can remain light and serve atmosphere/style/theme echo/opening roles at line 1085.
- 《人生》 prompt: archive identity remains primary and a light card can be cited without becoming a complete card at lines 1020-1029.

### 4. External-only material cannot become user judgment

PASS.

- Generic prompt: external-only material without a user-card anchor stays in the internal ledger and cannot become first-person user judgment or the article-index main anchor at lines 1086-1087.
- 《人生》 prompt: external-reader material cannot become first-person judgment at line 1121; external-only strong material stays in the internal ledger or pending/discard area until linked to a user card at line 1122.

## Post-fix refresh, 2026-07-14

PASS.

- Generic entrance gate now names the fourth-stage task explicitly: `微信读书通用提示词.md:33` lists `第四阶段（全书收束整合）` among task types.
- 《人生》 top flow is now four-stage: `路遥/人生/《人生》微信读书提示词.md:34-36` says `## 1. 四阶段总流程` and `整理《人生》微信读书材料时分四阶段`.
- 《人生》 fourth-stage flow is present in the top flow: `路遥/人生/《人生》微信读书提示词.md:53-57` defines `第四阶段：读完整本书后的全书收束整合`, its entrance condition, inputs, and exit condition.
- 《人生》 auxiliary preamble uses the corrected gate phrase: `路遥/人生/《人生》微信读书提示词.md:1207` says shortcut templates remain subject to `阶段切换 QA 或第四阶段前置检查`.
- 《人生》 whole-book shortcut uses the corrected pre-check phrase: `路遥/人生/《人生》微信读书提示词.md:1248` requires `第四阶段前置检查与执行授权`, then names the minimum pre-check contents.
- Fixture dry-run conclusions remain PASS: the wording fixes only clarify entrance/check labels and do not alter the nine case outcomes, archive-before-index rule, article-index citation rule, light-card rule, or external-only material rule recorded above.
- Prompt files were not edited during this refresh; only this evidence ledger was updated.

## Command/check receipts

All commands below produced no output, which means no whitespace-error lines were reported.

| Check | Command | Result |
|---|---|---|
| Worktree status for tracked/untracked scope | `GIT_MASTER=1 git status --short` | PASS. Relevant status: the two prompt files are modified; `.omo/plans/add-whole-book-consolidation-model.md`, `.omo/evidence/fixtures/`, and `.omo/evidence/task-0` through `task-4` evidence files are untracked. Unrelated `.omo/run-continuation/` and `.omo/drafts/` entries also exist and were not edited by this task. |
| Requested tracked diff whitespace check | `GIT_MASTER=1 git diff --check -- "微信读书通用提示词.md" "路遥/人生/《人生》微信读书提示词.md" ".omo/plans/add-whole-book-consolidation-model.md"` | PASS. No whitespace errors reported. Note: Git status shows the plan file is untracked, so this exact command cannot inspect the plan file contents; a no-index check for the plan is recorded below. |
| Fixture no-index whitespace check | `GIT_MASTER=1 git diff --no-index --check -- /dev/null ".omo/evidence/fixtures/add-whole-book-consolidation-model.md"` | PASS. No whitespace errors reported. |
| Task 0 evidence no-index whitespace check | `GIT_MASTER=1 git diff --no-index --check -- /dev/null ".omo/evidence/task-0-add-whole-book-consolidation-model.md"` | PASS. No whitespace errors reported. |
| Task 1 evidence no-index whitespace check | `GIT_MASTER=1 git diff --no-index --check -- /dev/null ".omo/evidence/task-1-add-whole-book-consolidation-model.md"` | PASS. No whitespace errors reported. |
| Task 2 evidence no-index whitespace check | `GIT_MASTER=1 git diff --no-index --check -- /dev/null ".omo/evidence/task-2-add-whole-book-consolidation-model.md"` | PASS. No whitespace errors reported. |
| Task 3 evidence no-index whitespace check | `GIT_MASTER=1 git diff --no-index --check -- /dev/null ".omo/evidence/task-3-add-whole-book-consolidation-model.md"` | PASS. No whitespace errors reported. |
| Task 4 evidence no-index whitespace check, pre-receipt update | `GIT_MASTER=1 git diff --no-index --check -- /dev/null ".omo/evidence/task-4-add-whole-book-consolidation-model.md"` | PASS. No whitespace errors reported. |
| Approved plan no-index whitespace check | `GIT_MASTER=1 git diff --no-index --check -- /dev/null ".omo/plans/add-whole-book-consolidation-model.md"` | PASS. No whitespace errors reported. Added because `git status --short` shows the plan is untracked, while the requested `git diff --check -- ...` only inspects tracked changes. |
| Evidence read-back | `read(filePath="/home/king/github/growing-myself/.omo/evidence/task-4-add-whole-book-consolidation-model.md")` | PASS. Confirmed the file contains all nine fixture rows, cross-file checks, receipts, and no prompt edits. |
| Markdown diagnostics | `lsp_diagnostics(filePath="/home/king/github/growing-myself/.omo/evidence/task-4-add-whole-book-consolidation-model.md", severity="all")` | Not applicable for Markdown in this repo: no LSP server is configured for `.md`. |
| Task 4 evidence no-index whitespace check, final after receipt update | `GIT_MASTER=1 git diff --no-index --check -- /dev/null ".omo/evidence/task-4-add-whole-book-consolidation-model.md"` | PASS. No whitespace errors reported. |

## Blocking issues

None found.
