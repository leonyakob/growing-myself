# Task 6 Evidence, split-weread-prompts-by-stage

Source snapshot used:

- Immutable snapshot: `/home/king/github/growing-myself/.omo/evidence/split-weread-prompts-by-stage/source/微信读书通用提示词.before.md`
- Snapshot scope used for this task: lines `977-1106`, with plan anchors at `977`, `981`, `983`, `992`, `1000`, `1015`, `1033`, `1056`, `1071`, `1083`, `1093`.
- Move ledger used: `/home/king/github/growing-myself/.omo/evidence/task-1-split-weread-prompts-by-stage.md`
- Fixture source used for dry-run model coverage: `/home/king/github/growing-myself/.omo/evidence/fixtures/add-whole-book-consolidation-model.md`

Applicable AGENTS.md:

- `/home/king/github/growing-myself/AGENTS.md`
- Generic Stage 4 work uses root `AGENTS.md` only.
- Explicitly not imported: any `路遥/人生/**` file, `/home/king/github/growing-myself/路遥/人生/AGENTS.md`, sibling-book AGENTS rules, or book-specific regression sentinels.

Files changed:

- `/home/king/github/growing-myself/微信读书通用提示词-第四阶段-全书收束整合.md`
- `/home/king/github/growing-myself/.omo/evidence/task-6-split-weread-prompts-by-stage.md`
- `/home/king/github/growing-myself/.omo/notepads/split-weread-prompts-by-stage/learnings.md` (append-only)

Commands run:

- `functions.read` `/home/king/github/growing-myself/AGENTS.md`
- `functions.read` `/home/king/github/growing-myself/.omo/plans/split-weread-prompts-by-stage.md`
- `functions.read` `/home/king/github/growing-myself/.omo/evidence/task-1-split-weread-prompts-by-stage.md`
- `functions.read` `/home/king/github/growing-myself/.omo/evidence/split-weread-prompts-by-stage/source/微信读书通用提示词.before.md` with Stage 4 range `977-1126`
- `functions.read` `/home/king/github/growing-myself/.omo/evidence/fixtures/add-whole-book-consolidation-model.md`
- `functions.read` `/home/king/github/growing-myself/.omo/notepads/split-weread-prompts-by-stage/learnings.md`
- `functions.read` `/home/king/github/growing-myself/.omo/notepads/split-weread-prompts-by-stage/issues.md`
- `functions.read` `/home/king/github/growing-myself/.omo/notepads/split-weread-prompts-by-stage/decisions.md`
- `functions.read` `/home/king/github/growing-myself/.omo/notepads/split-weread-prompts-by-stage/problems.md`
- `functions.read` `/home/king/github/growing-myself/微信读书通用提示词-第四阶段-全书收束整合.md`
- `functions.read` `/home/king/github/growing-myself/.omo/evidence/task-6-split-weread-prompts-by-stage.md`
- `GIT_MASTER=1 git grep -F --untracked -n "阅读现场档案 + 文章素材索引" -- "微信读书通用提示词-第四阶段-全书收束整合.md"`
- `GIT_MASTER=1 git grep -F --untracked -n "卡片档案为底座，文章素材索引为上层导航" -- "微信读书通用提示词-第四阶段-全书收束整合.md"`
- `GIT_MASTER=1 git grep -F --untracked -n "内部整合台账" -- "微信读书通用提示词-第四阶段-全书收束整合.md"`
- `GIT_MASTER=1 git grep -F --untracked -n "多轴" -- "微信读书通用提示词-第四阶段-全书收束整合.md"`
- `GIT_MASTER=1 git grep -F --untracked -n "一卡双归宿" -- "微信读书通用提示词-第四阶段-全书收束整合.md"`
- `GIT_MASTER=1 git grep -F --untracked -n "fixture" -- "微信读书通用提示词-第四阶段-全书收束整合.md"`
- `GIT_MASTER=1 git grep -F --untracked -n "归档不迁移" -- "微信读书通用提示词-第四阶段-全书收束整合.md"`
- `GIT_MASTER=1 git grep --untracked -E -n '全局重跑第三阶段|文章素材索引.*替代卡片|AI修正.*覆盖.*我自己写的内容' -- "微信读书通用提示词-第四阶段-全书收束整合.md"`
- `GIT_MASTER=1 git diff --no-index --check /dev/null "微信读书通用提示词-第四阶段-全书收束整合.md"`
- `GIT_MASTER=1 git diff --no-index --check /dev/null ".omo/evidence/task-6-split-weread-prompts-by-stage.md"`
- `GIT_MASTER=1 git diff --no-index --check /dev/null ".omo/notepads/split-weread-prompts-by-stage/learnings.md"`
- `functions.lsp_diagnostics` `/home/king/github/growing-myself/微信读书通用提示词-第四阶段-全书收束整合.md`
- `functions.lsp_diagnostics` `/home/king/github/growing-myself/.omo/evidence/task-6-split-weread-prompts-by-stage.md`
- `functions.lsp_diagnostics` `/home/king/github/growing-myself/.omo/notepads/split-weread-prompts-by-stage/learnings.md`

Heading coverage

| snapshot heading | source line | target coverage | note |
|---|---:|---|---|
| `## 12. 第四阶段：读完整本书后的全书收束整合` | 977 | prompt title + entry block at lines `13-19` | Stage 4 only, self-contained entry preserved. |
| `### 12.1 第三阶段与第四阶段的边界` | 983 | `## 1. 第三阶段与第四阶段的边界` at lines `21-26` | Includes explicit no-global-rerun boundary. |
| `### 12.2 产物边界：内部整合台账与正式阅读笔记` | 992 | `## 2. 产物边界，内部整合台账与正式阅读笔记` at lines `30-37` | Separates technical ledger from readable formal note. |
| `### 12.3 多轴台账，不用单一“最终状态”替代材料` | 1000 | `## 3. 先建多轴内部整合台账` at lines `39-50` | Multi-axis table preserved and execution order restated. |
| `### 12.4 一卡双归宿，与两层正式稿结构` | 1015 | `## 4. 一卡双归宿，与两层正式稿结构` at lines `54-68` | Keeps card archive first, article index second. |
| `### 12.5 全书收束后的正式阅读笔记骨架` | 1033 | `## 5. 全书收束后的正式阅读笔记骨架` at lines `72-95` | Readable final-note skeleton preserved. |
| `## 全书收束整合` skeleton block | 1036-1052 | code block at lines `75-93` | `阅读现场档案` precedes `文章素材索引`. |
| `### 12.6 判重、回源与修订链规则` | 1056 | `## 6. 判重、回源与修订链规则` at lines `97-108` | Duplicate, same-scene, and external-reader attachment rules preserved. |
| `### 12.7 误读修正与阅读轨迹写法` | 1071 | `## 7. 误读修正与阅读轨迹写法` at lines `112-120` | Misreading chain preserved instead of flattened. |
| `### 12.8 轻卡、外部读者材料与防膨胀规则` | 1083 | `## 8. 轻卡、外部读者材料与防膨胀规则` at lines `124-131` | Light-card and external-reader anti-bloat rules preserved. |
| `### 12.9 全书收束整合 QA` | 1093 | `## 10. fixture-based QA` at lines `144-166` plus `## 11. 完成标准` at `168-176` | Dry-run QA and completion gate preserved. |

Per-token verification

| token | result | hit lines in target | note |
|---|---|---|---|
| `阅读现场档案 + 文章素材索引` | PASS | `17`, `172` | Standard model and completion standard both retain the phrase. |
| `卡片档案为底座，文章素材索引为上层导航` | PASS | `17` | Exact required phrase retained. |
| `内部整合台账` | PASS | `7`, `30`, `32`, `37`, `39`, `95`, `106`, `127`, `138`, `154`, `166`, `175` | Multi-hit across inheritance block, rules, execution order, and completion standard. |
| `多轴` | PASS | `39`, `41` | Heading and explanatory sentence both hit. |
| `一卡双归宿` | PASS | `54`, `56` | Heading plus definition retained. |
| `fixture` | PASS | `5`, `142`, `144`, `146`, `176` | Pre-read, execution order, QA heading, QA intro, and completion standard all hit. |
| `归档不迁移` | PASS | `46`, `91`, `130`, `138`, `154`, `156`, `166`, `175` | Present in ledger values, final-note skeleton, anti-bloat rules, fixture QA, and completion standard. |

Exact-source-rule preservation samples

1. Snapshot line `981`: `第四阶段的标准模型是 **阅读现场档案 + 文章素材索引**。核心原则是：**卡片档案为底座，文章素材索引为上层导航**。`
   - Target line `17`: exact phrase preserved verbatim.
2. Snapshot line `988`: `第四阶段不是把第三阶段全局重跑一遍。除非材料缺失、重复、语义错误、判断已被后文修正，或被明确标记为待重迁，否则不要整体重迁已有正式稿。`
   - Target line `24`: preserved in equivalent Stage 3/4 boundary wording with no broadening of Stage 4 scope.
3. Snapshot line `997`: `原始 “我自己写的内容” 必须保留，AI修正只能另写，不能覆盖原文。`
   - Target line `33`: preserved in product-boundary rules.
   - Target line `130`: reinforced in anti-bloat rules for post-whole-book corrections.
4. Snapshot line `1022`: `文章素材索引只引用卡片，不吞掉卡片。`
   - Target line `59`: preserved and tightened with an explicit anti-replacement sentence.
5. Snapshot line `1097`: `QA 未通过时，不得把全书收束整合视为完成。`
   - Target lines `140`, `176`: preserved in execution-order gate and completion standard.

Fixture coverage

| case | fixture heading | expected preservation in prompt | covered by target lines |
|---:|---|---|---|
| 1 | `Case 1, partially migrated card` | Partial migration cannot treat an old AI summary as enough. Need readable evidence and user original sentence back in archive first. | `24-25`, `30-37`, `138-140`, `146` |
| 2 | `Case 2, duplicate same quote + same insight` | Same-quote same-judgment duplicates must select a representative card and move the rest to internal ledger, not crowd the formal note. | `97-108`, `129`, `147` |
| 3 | `Case 3, duplicate same quote + changed judgment` | Same-quote changed judgment must become a revision chain, not a silently flattened final conclusion. | `104-105`, `112-120`, `148` |
| 4 | `Case 4, same scene with different source ID/range` | Same scene with different technical anchors is treated as one scene card if action chain and tension match. | `106`, `149` |
| 5 | `Case 5, early misreading corrected later` | Early misreading stays visible as reading trajectory, not deleted as low-quality residue. | `26`, `112-120`, `150` |
| 6 | `Case 6, external high-like challenge` | External challenge may illuminate the user card, but cannot replace the user card as formal-note主体. | `34`, `108`, `126`, `151` |
| 7 | `Case 7, external-only strong comment` | External-only material without a user anchor stays in internal ledger or `待回看 / 归档不迁移`, not as formal-note main evidence. | `127-130`, `152`, `154` |
| 8 | `Case 8, light card used as article evidence but not upgraded` | Light cards may be cited by article index without forced promotion to complete cards. | `124`, `153`, `161` |
| 9 | `Case 9, final-note bloat prevention / archive-discard-with-reason` | `归档不迁移` is a valid destination for low-information duplicates, and anti-bloat reasoning stays out of reader-visible technical ledger format. | `89-95`, `129-130`, `154`, `164` |

Read-based QA notes:

- Inheritance block exists at lines `1-11` and contains router path, stage purpose, required pre-reads, exact inputs/outputs, router-wins conflict rule, task boundary, Must NOT list, and QA evidence path.
- The Stage 3/4 boundary is explicit at lines `21-26`. It says Stage 4 is not a global rerun of Stage 3 and limits rework to missing, duplicated, semantically wrong, revised, or explicitly pending-remigration material.
- Internal ledger vs. formal-note boundary is explicit at lines `30-37` and reinforced at line `95`. Technical fields stay internal; readable anchors stay in the formal note.
- The required whole-book model appears exactly at line `17`, and the readable output order is enforced again at lines `72-93` and `158`.
- `阅读现场档案` comes before `文章素材索引` both in prose and in the final-note skeleton. The article index is consistently described as navigation only, not a replacement for cards.
- `多轴` handling is not reduced to a single status flag. The table at lines `43-48` preserves `source status`, `archive disposition`, `evidence role`, `article links`, `trajectory flags`, and `external-reader relation`.
- `一卡双归宿` is preserved as an archive-first rule, not as permission to skip the archive layer.
- The prompt stays generic. No 《人生》 names, bookIds, article directions, regression sample IDs, or sibling-book AGENTS rules were introduced.

Boundary checks:

- No rewrite of `/home/king/github/growing-myself/微信读书通用提示词.md`.
- No creation or edit of Stage 1, Stage 2, or Stage 3 prompt files.
- No touch to any `路遥/人生/**` file.
- No modification of actual reading notes, intermediate drafts, or formal reading notes.
- No edit to `.omo/run-continuation/*.json`.
- No commit, stage, push, or destructive git command.
- Generic Stage 4 prompt continues to require root `AGENTS.md` only.

Failure-grep classification

Command:

`GIT_MASTER=1 git grep --untracked -E -n '全局重跑第三阶段|文章素材索引.*替代卡片|AI修正.*覆盖.*我自己写的内容' -- "微信读书通用提示词-第四阶段-全书收束整合.md"`

| target line | matched text summary | classification | reason |
|---:|---|---|---|
| 10 | Must NOT line contains `全局重跑第三阶段` / `文章素材索引替代卡片` / `AI修正覆盖我自己写的内容` as prohibitions | boundary-only OK | Negative boundary language in inheritance block, not execution instruction. |
| 24 | `本阶段不是全局重跑第三阶段` | boundary-only OK | Explicit Stage 3/4 boundary. |
| 59 | `不得让文章素材索引替代卡片` inside article-index definition | boundary-only OK | Negative anti-replacement rule. |
| 72 | `文章索引不能替代卡片` in final-note-order paragraph | boundary-only OK | Negative anti-replacement reminder tied to output order. |

Whitespace check

- Command: `GIT_MASTER=1 git diff --no-index --check /dev/null "微信读书通用提示词-第四阶段-全书收束整合.md"`
- Result: no output, interpreted as `PASS` with no whitespace errors in the new Stage 4 prompt file.
- Command: `GIT_MASTER=1 git diff --no-index --check /dev/null ".omo/evidence/task-6-split-weread-prompts-by-stage.md"`
- Result: no output, interpreted as `PASS` with no whitespace errors in the new Task 6 evidence file.
- Command: `GIT_MASTER=1 git diff --no-index --check /dev/null ".omo/notepads/split-weread-prompts-by-stage/learnings.md"`
- Result: no output, interpreted as `PASS` with no whitespace errors in the append-only learnings file.

Diagnostics note

- `lsp_diagnostics` was invoked on all three modified Markdown files.
- Result for each file: no Markdown LSP server is configured in this workspace, so no syntax diagnostics were available. This is a tooling absence, not a reported file error.

PASS:

- PASS: Stage 4 prompt begins with the required inheritance block and keeps router authority explicit.
- PASS: required phrases `阅读现场档案 + 文章素材索引`, `卡片档案为底座，文章素材索引为上层导航`, `内部整合台账`, `多轴`, `一卡双归宿`, `fixture`, and `归档不迁移` all appear in the final target file.
- PASS: Stage 4 explicitly forbids treating article index as a card substitute and forbids AI rewrites from overwriting `我自己写的内容`.
- PASS: read-based QA confirms `阅读现场档案` comes before `文章素材索引`, and the article index is navigation only.
- PASS: all nine fixture classes from `.omo/evidence/fixtures/add-whole-book-consolidation-model.md` are recorded in this evidence and tied to concrete prompt lines.
- PASS: failure-grep hits are all negative-boundary hits, classified `boundary-only OK`, with no forbidden instruction found.
- PASS: no scope drift into router rewrite, other stage prompts, `路遥/人生/**`, reading-note files, or `.omo/run-continuation`.
- PASS: read-back was performed on the final Stage 4 prompt and the final Task 6 evidence file.

Follow-ups / unresolved risks:

- Non-blocking: this task verifies the standalone Stage 4 file only. Router-level link validation and cross-stage integrity still belong to later generic hard QA.
- Non-blocking: final review of this prompt in Task 7 should re-check contamination and link behavior once the rest of the generic stage files exist.
- Blocking threshold: if later verification finds missing fixture coverage, missing inheritance-block fields, or any hit reclassified as `forbidden instruction FAIL`, Task 6 must lose PASS.
