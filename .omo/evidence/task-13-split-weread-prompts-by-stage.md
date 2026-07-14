# Task 13 Evidence, split-weread-prompts-by-stage

Source snapshot used:

- Immutable source of truth: `/home/king/github/growing-myself/.omo/evidence/split-weread-prompts-by-stage/source/《人生》微信读书提示词.before.md`
- Stage 4 source ranges used: `957-1156`
- Stage 4 shortcut bodies used: `1245-1255`
- Preservation ledger source: `/home/king/github/growing-myself/.omo/evidence/task-8-split-weread-prompts-by-stage.md`
- Fixture source: `/home/king/github/growing-myself/.omo/evidence/fixtures/add-whole-book-consolidation-model.md`
- Snapshot gate re-read before writing: Task 8 evidence contains `SNAPSHOT_VERBATIM_BEFORE_REWRITE: PASS`.

Applicable AGENTS.md:

- Required root rule file: `/home/king/github/growing-myself/AGENTS.md`
- Same-book rule file check: `/home/king/github/growing-myself/路遥/人生/AGENTS.md` was absent in Task 8 evidence and is still absent in this execution state, so this task uses root `AGENTS.md` only and records the absence inside the Stage 4 inheritance block.
- Explicitly not imported: `/home/king/github/growing-myself/路遥/平凡的世界/AGENTS.md` and any sibling-book `AGENTS.md`.

Files changed:

- `/home/king/github/growing-myself/路遥/人生/《人生》微信读书提示词-第四阶段-全书收束整合.md`
- `/home/king/github/growing-myself/.omo/evidence/task-13-split-weread-prompts-by-stage.md`
- `/home/king/github/growing-myself/.omo/notepads/split-weread-prompts-by-stage/learnings.md` (append-only, one single line)

Commands run:

- `functions.glob` on `.omo/evidence/**/*task*8*split-weread-prompts-by-stage*.md`
- `functions.glob` on `.omo/evidence/**/*split-weread-prompts-by-stage*.md`
- `functions.glob` on `.omo/notepads/split-weread-prompts-by-stage/*.md`
- `functions.glob` on `路遥/人生/AGENTS.md`
- `functions.glob` on `.omo/plans/**/*.md`
- `functions.glob` on `.omo/evidence/fixtures/add-whole-book-consolidation-model.md`
- `functions.read` on `/home/king/github/growing-myself/AGENTS.md`
- `functions.read` on `/home/king/github/growing-myself/.omo/evidence/task-8-split-weread-prompts-by-stage.md`
- `functions.read` on `/home/king/github/growing-myself/.omo/evidence/fixtures/add-whole-book-consolidation-model.md`
- `functions.read` on `.omo/notepads/split-weread-prompts-by-stage/{learnings,problems,issues,decisions}.md`
- `functions.read` on `/home/king/github/growing-myself/.omo/evidence/split-weread-prompts-by-stage/source/《人生》微信读书提示词.before.md` ranges `957-1176` and `1245-1264`
- `functions.read` on `/home/king/github/growing-myself/.omo/evidence/task-8-split-weread-prompts-by-stage.md` range `261-381`
- `functions.read` on `/home/king/github/growing-myself/.omo/plans/split-weread-prompts-by-stage.md` range `240-319`
- `GIT_MASTER=1 git grep -F --untracked -n "阅读现场档案" -- "路遥/人生/《人生》微信读书提示词-第四阶段-全书收束整合.md"`
- `GIT_MASTER=1 git grep -F --untracked -n "文章素材索引" -- "路遥/人生/《人生》微信读书提示词-第四阶段-全书收束整合.md"`
- `GIT_MASTER=1 git grep -F --untracked -n "人物线" -- "路遥/人生/《人生》微信读书提示词-第四阶段-全书收束整合.md"`
- `GIT_MASTER=1 git grep -F --untracked -n "城乡主题" -- "路遥/人生/《人生》微信读书提示词-第四阶段-全书收束整合.md"`
- `GIT_MASTER=1 git grep -F --untracked -n "尊严主题" -- "路遥/人生/《人生》微信读书提示词-第四阶段-全书收束整合.md"`
- `GIT_MASTER=1 git grep -F --untracked -n "爱情线" -- "路遥/人生/《人生》微信读书提示词-第四阶段-全书收束整合.md"`
- `GIT_MASTER=1 git grep -F --untracked -n "知识分子困境" -- "路遥/人生/《人生》微信读书提示词-第四阶段-全书收束整合.md"`
- `GIT_MASTER=1 git grep -F --untracked -n "写法线索" -- "路遥/人生/《人生》微信读书提示词-第四阶段-全书收束整合.md"`
- `GIT_MASTER=1 git grep -F --untracked -n "内部整合台账" -- "路遥/人生/《人生》微信读书提示词-第四阶段-全书收束整合.md"`
- `GIT_MASTER=1 git grep -F --untracked -n "一卡双归宿" -- "路遥/人生/《人生》微信读书提示词-第四阶段-全书收束整合.md"`
- `GIT_MASTER=1 git grep -F --untracked -n "fixture" -- "路遥/人生/《人生》微信读书提示词-第四阶段-全书收束整合.md"`
- `GIT_MASTER=1 git grep --untracked -E -n '全局重跑第三阶段|文章素材索引.*替代卡片|AI修正.*覆盖.*我的原想法|source ID.*文章方向锚点' -- "路遥/人生/《人生》微信读书提示词-第四阶段-全书收束整合.md"`
- `GIT_MASTER=1 git diff --no-index --check /dev/null "路遥/人生/《人生》微信读书提示词-第四阶段-全书收束整合.md"`
- `python3 - <<'PY' ... required heading and order coverage for Stage 4 ... PY`
- `python3 - <<'PY' ... nine fixture case coverage in fixture file and Stage 4 prompt ... PY`
- `functions.read` on `/home/king/github/growing-myself/路遥/人生/《人生》微信读书提示词-第四阶段-全书收束整合.md`
- `functions.lsp_diagnostics` on `/home/king/github/growing-myself/路遥/人生/《人生》微信读书提示词-第四阶段-全书收束整合.md`
- `functions.lsp_diagnostics` on `/home/king/github/growing-myself/.omo/notepads/split-weread-prompts-by-stage/learnings.md`

Read-based QA notes:

## Semantic coverage reread

- The file starts with an inheritance block, not a generic title. It includes router path, stage purpose, required pre-reads, exact input/output files, conflict rule, trigger, task boundary, Must NOT list, and QA evidence path.
- The inheritance block explicitly records the Task 8 same-book `AGENTS.md` absence instead of inventing a dependency.
- The execution order is explicit and correct: `内部整合台账` first, `阅读现场档案` second, `文章素材索引` third, then `阅读轨迹与判断变化` and `待回看 / 归档不迁移`.
- The Stage 3 and Stage 4 boundary is not vague. The prompt authorizes only local补迁 / 重迁 under four conditions and repeats that Stage 4 does not globally rerun Stage 3.
- The formal-note boundary is explicit. `source ID` / `range` / `chapterUid` / `bookId` / status fields / interface coordinates are confined to the internal ledger and forbidden from reader-visible anchors.
- The Stage 4 shortcut bodies were preserved as file-local execution text, but stale numeric references to source sections were removed from target wording.

## Heading coverage

| heading or structure check | result | status |
|---|---|---|
| `## 内部整合台账` | present | PASS |
| `## 一卡双归宿` | present | PASS |
| `### 一、阅读现场档案` | present | PASS |
| `### 二、文章素材索引` | present | PASS |
| `### 三、阅读轨迹与判断变化` | present | PASS |
| `### 四、待回看 / 归档不迁移` | present | PASS |
| `## 《人生》文章素材索引表` | present | PASS |
| `## fixture 对照与 Stage 4 QA` | present | PASS |
| `### 读完整本书后执行全书收束整合` | present | PASS |
| `### 读完整本书后回看我的阅读风格` | present | PASS |
| `阅读现场档案` appears before `文章素材索引` | `True` in scripted order check | PASS |

## Exact-source-rule preservation samples

1. Snapshot `959-971`: trigger, whole-book-only scope, default model, fixed paths, and reader-visible technical-field ban all survive in the inheritance block plus `本阶段的默认模型`.
2. Snapshot `997-1023`: `source status` / `archive disposition` / `evidence role` / `article links` / `trajectory flags` / `external-reader relation` survive as an explicit multi-axis ledger table and ordered decision rule.
3. Snapshot `1040-1046`: `阅读现场档案` before `文章素材索引`, and `文章素材索引` uses readable card anchors rather than `source ID` / `range`, survive in both the output skeleton and the QA checklist.
4. Snapshot `1083-1120`: duplicate handling, corrected-judgment revision chains, same-scene deduping across different `source ID` / `range`, and misreading-repair structure survive in `重复卡、改判链与误读修正`.
5. Snapshot `1122-1155`: external-reader anti-bloat rules and nine-case fixture QA survive as a dedicated `fixture` table plus a self-check list.

## Literal token verification

| token | semantic location in Stage 4 prompt | status |
|---|---|---|
| `阅读现场档案` | default model, execution order, output skeleton, fixture table, QA checklist, execution shortcut | PASS |
| `文章素材索引` | default model, Must NOT boundary, output skeleton, article table, anti-bloat rules, fixture table, QA checklist, execution shortcut | PASS |
| `人物线` | article direction inheritance, article table, duplicate-rule routing | PASS |
| `城乡主题` | article direction inheritance, article table, duplicate-rule routing | PASS |
| `尊严主题` | article direction inheritance, article table | PASS |
| `爱情线` | article direction inheritance, article table | PASS |
| `知识分子困境` | article direction inheritance, one-card-two-destinations example, article table | PASS |
| `写法线索` | article direction inheritance, article table, duplicate-rule routing | PASS |
| `内部整合台账` | precheck, execution order, dedicated section, duplicate rules, external-reader boundary, fixture cases, execution shortcut | PASS |
| `一卡双归宿` | dedicated section and navigation-boundary explanation | PASS |
| `fixture` | pre-read path, precheck, dedicated QA heading, nine-case table | PASS |

## Nine fixture cases reread

| fixture case | reread result | status |
|---|---|---|
| Case 1, partially migrated card | prompt requires补 readable evidence in `阅读现场档案` and forbids treating old AI summary as the full card | PASS |
| Case 2, duplicate same quote + same insight | prompt requires representative-card merge and forbids duplicate formal-note inflation | PASS |
| Case 3, duplicate same quote + changed judgment | prompt requires revision chain and routes the old/new split into archive plus reading trajectory | PASS |
| Case 4, same scene with different source ID/range | prompt requires same-scene semantic dedupe and forbids technical-coordinate duplication | PASS |
| Case 5, early misreading corrected later | prompt preserves the full misreading chain and its value instead of deleting it | PASS |
| Case 6, external high-like challenge | prompt keeps user card as main anchor and hangs the outside view as `挑战` | PASS |
| Case 7, external-only strong comment | prompt keeps it in internal ledger or wait-list until a user anchor exists | PASS |
| Case 8, light card used as article evidence but not upgraded | prompt preserves light-card identity even when article-linked | PASS |
| Case 9, final-note bloat prevention / archive-discard-with-reason | prompt explicitly authorizes `归档不迁移` for low-information weak cards | PASS |

## Positive dry-run

- Dry-run scenario: user says they finished the whole book and explicitly authorizes whole-book consolidation.
- Observed route from reread: pre-read root `AGENTS.md`, router, intermediate draft, formal note, fixture file, and same-book `AGENTS.md` only if it truly exists; then confirm whole-book trigger; then build `内部整合台账`; then repair or preserve cards in `阅读现场档案`; then build `文章素材索引`; then record only meaningful reading-trajectory and wait-list leftovers.
- Expected visible output from this route: only `/home/king/github/growing-myself/路遥/人生/《人生》阅读笔记.md` changes, with card archive preserved and article links staying navigational.

## Boundary and failure dry-run

- The failure grep returned only boundary statements and QA checklist language, not executable forbidden instructions.
- `全局重跑第三阶段` appears only in prohibitions and boundary reminders.
- `文章素材索引.*替代卡片` appears only in prohibitions and QA checks that say the index must not replace cards.
- `AI修正.*覆盖.*我的原想法` appears only in prohibitions and QA checks that say this must not happen.
- `source ID.*文章方向锚点` appears only in prohibitions, anti-bloat rules, fixture case 4, and QA checks that say this must not happen.
- Failure classification result: every grep hit is `boundary-only OK`. There is no `forbidden instruction FAIL` row.

## Diagnostics and whitespace

| target | command or tool | result | status |
|---|---|---|---|
| Stage 4 prompt | `functions.lsp_diagnostics` | `No LSP server configured for extension: .md` | PASS, no diagnostics available for Markdown |
| learnings append target | `functions.lsp_diagnostics` | `No LSP server configured for extension: .md` | PASS, no diagnostics available for Markdown |
| Stage 4 prompt | `git diff --no-index --check /dev/null` | no output | PASS |

Boundary checks:

- This task did not rewrite `/home/king/github/growing-myself/路遥/人生/《人生》微信读书提示词.md`.
- This task did not create or edit the Stage 1, Stage 2, or Stage 3 《人生》 prompt files.
- This task did not edit generic prompt files.
- This task did not edit `/home/king/github/growing-myself/路遥/人生/《人生》中间整理稿.md` or `/home/king/github/growing-myself/路遥/人生/《人生》阅读笔记.md`.
- This task did not import sibling-book `AGENTS.md` rules.
- Writes were limited to the Stage 4 prompt, this evidence file, and one atomic append to `.omo/notepads/split-weread-prompts-by-stage/learnings.md`.
- The Stage 4 prompt uses file-aware wording and stable section titles. It does not introduce stale source-section references like “第 11 节” into target instructions.

PASS:

- PASS: Task 8 snapshot gate was re-read and verified through `SNAPSHOT_VERBATIM_BEFORE_REWRITE: PASS` before any writing.
- PASS: The Stage 4 prompt begins with the required inheritance block and keeps the required fixed input paths, output path, conflict rule, trigger, task boundary, Must NOT list, and QA evidence path.
- PASS: The prompt preserves the Stage 3 and Stage 4 boundary and authorizes only local补迁 / 重迁 under the allowed conditions.
- PASS: The prompt establishes `内部整合台账`, the required multi-axis fields, `一卡双归宿`, archive-before-index order, the `阅读现场档案` and `文章素材索引` structures, and the full 《人生》 article-direction table.
- PASS: The prompt preserves the seven 《人生》 regression sentinels as inherited book-specific QA material.
- PASS: The prompt references `/home/king/github/growing-myself/.omo/evidence/fixtures/add-whole-book-consolidation-model.md` and covers all nine fixture cases.
- PASS: Per-token `git grep --untracked` verification succeeded for `阅读现场档案`, `文章素材索引`, `人物线`, `城乡主题`, `尊严主题`, `爱情线`, `知识分子困境`, `写法线索`, `内部整合台账`, `一卡双归宿`, and `fixture`.
- PASS: Failure grep hits were all boundary-only and no forbidden executable instruction was introduced.

Follow-ups / unresolved risks:

- Non-blocking: Markdown LSP is not configured in this repo, so diagnostics are limited to “no server configured” plus read-based QA and whitespace checks.
- Non-blocking: Task 14 should still run the cross-file hard QA gate and re-check this prompt against the router and the other stage outputs once they exist.
