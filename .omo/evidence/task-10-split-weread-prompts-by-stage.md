# Task 10 Evidence, split-weread-prompts-by-stage

Source snapshot used:

- Immutable snapshot: `/home/king/github/growing-myself/.omo/evidence/split-weread-prompts-by-stage/source/《人生》微信读书提示词.before.md`
- Task 8 preservation ledger: `/home/king/github/growing-myself/.omo/evidence/task-8-split-weread-prompts-by-stage.md`
- Task 10 plan anchors: `/home/king/github/growing-myself/.omo/plans/split-weread-prompts-by-stage.md:238-244`
- Drafting source rule: this task used the immutable snapshot plus the Task 8 move ledger as source of truth. `/home/king/github/growing-myself/路遥/人生/《人生》微信读书提示词.md` was treated as an inherited router path to read before execution, not as drafting source.

Applicable AGENTS.md:

- `/home/king/github/growing-myself/AGENTS.md`
- `/home/king/github/growing-myself/路遥/人生/AGENTS.md` is execution-time conditional only. Task 8 recorded that same-book `AGENTS.md` was absent at snapshot time, so this Stage 1 prompt preserves the conditional read rule without inventing the file.
- Explicitly not imported: any sibling-book `AGENTS.md`, especially `/home/king/github/growing-myself/路遥/平凡的世界/AGENTS.md`.

Files changed:

- `/home/king/github/growing-myself/路遥/人生/《人生》微信读书提示词-第一阶段-生成中间整理稿.md`
- `/home/king/github/growing-myself/.omo/evidence/task-10-split-weread-prompts-by-stage.md`
- `/home/king/github/growing-myself/.omo/notepads/split-weread-prompts-by-stage/learnings.md` (append-only)

Commands run:

- `functions.glob("/home/king/github/growing-myself/.omo/notepads/split-weread-prompts-by-stage/*.md")`
- `functions.grep("Task 10|task-10|10\\.", path="/home/king/github/growing-myself/.omo", include="*.md")`
- `functions.read("/home/king/github/growing-myself/AGENTS.md")`
- `functions.read("/home/king/github/growing-myself/.omo/evidence/task-8-split-weread-prompts-by-stage.md")`
- `functions.read("/home/king/github/growing-myself/.omo/evidence/split-weread-prompts-by-stage/source/《人生》微信读书提示词.before.md")`
- `functions.read("/home/king/github/growing-myself/.omo/plans/split-weread-prompts-by-stage.md")`
- `functions.read("/home/king/github/growing-myself/.omo/plans/split-weread-prompts-by-stage.md", offset=238, limit=80)`
- `functions.read("/home/king/github/growing-myself/.omo/notepads/split-weread-prompts-by-stage/learnings.md")`
- `functions.read("/home/king/github/growing-myself/.omo/notepads/split-weread-prompts-by-stage/problems.md")`
- `functions.read("/home/king/github/growing-myself/.omo/notepads/split-weread-prompts-by-stage/issues.md")`
- `functions.read("/home/king/github/growing-myself/.omo/notepads/split-weread-prompts-by-stage/decisions.md")`
- `functions.read("/home/king/github/growing-myself/微信读书通用提示词-第一阶段-生成中间整理稿.md")`
- `functions.read("/home/king/github/growing-myself/.omo/evidence/task-3-split-weread-prompts-by-stage.md")`
- `ls "/home/king/github/growing-myself/路遥/人生"`
- `ls "/home/king/github/growing-myself/.omo/evidence"`
- `ls "/home/king/github/growing-myself/.omo/notepads/split-weread-prompts-by-stage"`
- `apply_patch` created `/home/king/github/growing-myself/路遥/人生/《人生》微信读书提示词-第一阶段-生成中间整理稿.md`
- `GIT_MASTER=1 git grep -F --untracked -n "CB_2tb79r78T38k74M75h8iz4C3" -- "路遥/人生/《人生》微信读书提示词-第一阶段-生成中间整理稿.md"`
- `GIT_MASTER=1 git grep -F --untracked -n "25164497" -- "路遥/人生/《人生》微信读书提示词-第一阶段-生成中间整理稿.md"`
- `GIT_MASTER=1 git grep -F --untracked -n "/book/bookmarklist" -- "路遥/人生/《人生》微信读书提示词-第一阶段-生成中间整理稿.md"`
- `GIT_MASTER=1 git grep -F --untracked -n "/review/list/mine" -- "路遥/人生/《人生》微信读书提示词-第一阶段-生成中间整理稿.md"`
- `GIT_MASTER=1 git grep -F --untracked -n "/book/readreviews" -- "路遥/人生/《人生》微信读书提示词-第一阶段-生成中间整理稿.md"`
- `GIT_MASTER=1 git grep -F --untracked -n "第N轮整理" -- "路遥/人生/《人生》微信读书提示词-第一阶段-生成中间整理稿.md"`
- `GIT_MASTER=1 git grep -F --untracked -n "外部读者精彩高赞想法候选" -- "路遥/人生/《人生》微信读书提示词-第一阶段-生成中间整理稿.md"`
- `GIT_MASTER=1 git grep --untracked -E -n 'AI修正|迁移到.*正式阅读笔记|全书收束整合' -- "路遥/人生/《人生》微信读书提示词-第一阶段-生成中间整理稿.md"`
- `GIT_MASTER=1 git diff --no-index --check /dev/null "/home/king/github/growing-myself/路遥/人生/《人生》微信读书提示词-第一阶段-生成中间整理稿.md"`
- `apply_patch` created `/home/king/github/growing-myself/.omo/evidence/task-10-split-weread-prompts-by-stage.md`
- `apply_patch` append-only updated `/home/king/github/growing-myself/.omo/notepads/split-weread-prompts-by-stage/learnings.md`
- `functions.read("/home/king/github/growing-myself/.omo/evidence/task-10-split-weread-prompts-by-stage.md")`
- `GIT_MASTER=1 git diff --no-index --check /dev/null "/home/king/github/growing-myself/.omo/evidence/task-10-split-weread-prompts-by-stage.md"`
- `GIT_MASTER=1 git diff --check -- ".omo/notepads/split-weread-prompts-by-stage/learnings.md"`
- `functions.lsp_diagnostics("/home/king/github/growing-myself/路遥/人生/《人生》微信读书提示词-第一阶段-生成中间整理稿.md")`
- `functions.lsp_diagnostics("/home/king/github/growing-myself/.omo/evidence/task-10-split-weread-prompts-by-stage.md")`
- `functions.lsp_diagnostics("/home/king/github/growing-myself/.omo/notepads/split-weread-prompts-by-stage/learnings.md")`

Heading coverage:

| snapshot heading | source lines | target heading / area | coverage note |
|---|---:|---|---|
| `## 4. 数据抓取硬约束` | `127-133` | `## 3. 中间整理稿与正式稿的数据边界` + `## 4. 数据抓取与匹配规则` | 两个主接口、数据口径和 Stage 1 只整理的范围都保留了。 |
| `### 4.0 中间整理稿与正式稿的数据边界` | `134-157` | `## 3. 中间整理稿与正式稿的数据边界` | 中间稿保留技术字段、正式稿不默认保留接口字段、默认以“我的想法”为主索引都落下来了。 |
| `### 4.1 跨段划线与想法匹配规则` | `159-201` | `### 4.2 划线与想法匹配顺序` + `### 4.3 每条整理材料至少保留的信息` | 精确 / 跨段 / 重叠 / 文本判断匹配、人工确认标记、只输出本轮新增内容全部保留。 |
| `### 4.2 同位置其他书友高赞想法默认伴随抓取规则` | `203-269` | `## 5. 导入版到官方公开版的同位置映射工作流` | 双 `bookId`、章节标题与文本重叠映射、接口分工、候选池、筛选规则和输出状态都在。 |
| `## 5. 颜色默认流向` | `273-298` | `## 6. 颜色默认流向` | 颜色名与默认流向保留，且明确输出时不只写数字。 |
| `## 6. 想法类别与卡片类型` + `### 6.1` + `### 6.2` | `302-325` | `## 7. 想法类别` + `## 8. 卡片判断` | 想法类别与卡片判断拆开写，仍停在轻量预分类层。 |
| `## 8. 第一阶段：生成中间整理稿` | `540-562` | `## 9. 第一阶段执行模板` | 执行模板保留同时抓两路数据、先映射再抓公开想法、只写中间稿的边界。 |
| `### 中间整理稿格式` | `564-633` | `## 10. 中间整理稿格式` | 整理说明、轮次、单条骨架、本轮索引和 `下次接着整理位置` 都保留。 |
| `# 路遥《人生》中间整理稿` + `## 整理说明` | `567-576` | `## 10. 中间整理稿格式` 内的标题与整理说明 | 顶部书名、双 `bookId`、bookId 关系和游标位置都可直接落盘。 |
| `## 第N轮整理：范围说明` + `### 001. 章节名 / range` | `577-617` | `## 第N轮整理：范围说明` + `### 001. 章节名 / range` + `### 有想法但划线匹配待确认` | 轮次结构原样保留，并补出 snapshot 规则要求的待确认小节。 |
| `## 本轮索引` 及其子项 | `618-632` | `## 本轮索引` 与各子项 | `轻卡清单`、`完整卡候选`、`主卡候选`、`暂存素材`、`外部读者精彩高赞想法候选`、`颜色统计`、`下次接着整理位置` 全在。 |

Exact-source-rule preservation samples:

1. Snapshot `136-137` preserved in target `54-58`: `中间整理稿是可回源的工作台...正式阅读笔记...不默认保留接口字段` 被落成 Stage 1 数据边界，而不是被弱化成一般说明。
2. Snapshot `155-157` preserved in target `62-71` and `231-241`: `不要只输出我的想法`、`必须同时获取两路数据`、`默认尝试抓取同位置其他书友高赞想法` 都保留，并且继续落进执行模板。
3. Snapshot `218` preserved in target `137` and `235`: `先用个人导入版整理我的阅读现场，再按章节标题、划线原文和文本重叠映射到官方版 25164497 的同一文本位置，最后用官方版 bookId + chapterUid + range 调 /book/readreviews。`
4. Snapshot `229-234` preserved in target `233-235`: 第一阶段先做轻量预分类，且此分类只服务于整理调度和高赞想法抓取深度，不等同于第二阶段深度评价。
5. Snapshot `261-269` preserved in target `175-183` and `288-298`: 五种输出状态与“高赞想法只能作为外部读者材料，不得替代我的感受、问题和判断”都保留到了正文与中间稿骨架里。

Read-based QA notes:

- Task 8 evidence contains `SNAPSHOT_VERBATIM_BEFORE_REWRITE: PASS` at lines `23-25`, so this task used a confirmed verbatim snapshot, not a mutable derivative.
- Task 8 evidence also maps 《人生》 Stage 1 to snapshot ranges `127-325` and `540-633`, and states that Stage 1 carries data fetching, matching, range-merging, color/category/type judgment, import-to-official public-position lookup, external-reader candidate collection, and intermediate-draft format only. The created prompt follows that exact boundary.
- Plan lines `154-158` show Tasks `9-13` are blocked only by Task `8`. Since Task `8` passed, Wave 2 stage-writing tasks may proceed. This task used that dependency state, not any later router rewrite, as its go signal.
- The stage file begins with a full inheritance block containing router path, stage purpose, required pre-reads, exact inputs, exact output, router-wins conflict rule, task boundary, Must NOT list, and QA evidence path, which matches the plan contract for fresh-session use.
- The prompt preserves the fixed paths from snapshot lines `5-9`, both exact `bookId` values, and the chapter-title plus quote-overlap mapping workflow before `/book/readreviews`.
- Stage 1 remains explicitly first-stage only. The body only authorizes organize, fetch, match, official-position map, light pre-classify, and write intermediate draft. It does not authorize deep literary optimization, formal-note migration, or book-end consolidation.
- Boundary-sensitive literals `AI修正`、`迁移到正式阅读笔记`、`全书收束整合` appear only in Must NOT and QA stop-lines, not as executable work.
- Same-book `AGENTS.md` is preserved as execution-time conditional only. No sibling-book rule import was introduced.
- LSP diagnostics were attempted on all three modified Markdown files. This repo currently has no `.md` LSP configured, so diagnostics returned “No LSP server configured for extension: .md” for each file. That is recorded as tooling state, not as a content error.

Per-token checks:

| token | sample hit lines | status |
|---|---|---|
| `CB_2tb79r78T38k74M75h8iz4C3` | `9, 21, 134, 137, 235, 259, 334` | PASS |
| `25164497` | `9, 22, 135, 137, 235, 260, 334` | PASS |
| `/book/bookmarklist` | `9, 64, 77, 141, 231` | PASS |
| `/review/list/mine` | `9, 65, 78, 142, 231` | PASS |
| `/book/readreviews` | `9, 130, 137, 145, 158, 180, 235, 334` | PASS |
| `第N轮整理` | `264` | PASS |
| `外部读者精彩高赞想法候选` | `241, 319, 336` | PASS |

Boundary checks:

| literal token | sample hit lines | classification | note |
|---|---|---|---|
| `AI修正` | `13, 339` | boundary-only OK | 只出现在 Must NOT 和 QA 禁行句里，没有作为执行动作。 |
| `迁移到正式阅读笔记` | `13, 339` | boundary-only OK | 只出现在禁止句里，Stage 1 没有引入迁移动作。 |
| `全书收束整合` | `13, 339` | boundary-only OK | 只出现在禁止句里，Stage 1 没有引入第四阶段动作。 |

Dry-run QA scenarios:

- Positive dry-run scenario: 用户说“只整理《人生》本轮新增微信读书笔记，顺手补同位置高赞想法，但先不要评价”。按本提示词，应先读根 `AGENTS.md`、router、以及同书 `AGENTS.md` 若它执行时存在；输入是 router、已有 `/home/king/github/growing-myself/路遥/人生/《人生》中间整理稿.md` 游标、个人导入版 `/book/bookmarklist` 与 `/review/list/mine`、官方公开版辅助接口；唯一输出是 `/home/king/github/growing-myself/路遥/人生/《人生》中间整理稿.md`；允许的动作只有抓取、匹配、轻量预分类、公开版定位和落盘。
- Boundary/failure dry-run scenario: 用户说“把这一轮先 AI修正，再迁移到正式阅读笔记，最后做全书收束整合”。按本提示词，这三个动作都在 Must NOT 和 QA 禁行边界里，Stage 1 不能执行，必须停在第一阶段边界并改走后续阶段提示词。

Whitespace checks:

| target | command style | result | status |
|---|---|---|---|
| stage file `/home/king/github/growing-myself/路遥/人生/《人生》微信读书提示词-第一阶段-生成中间整理稿.md` | `git diff --no-index --check /dev/null` | no output | PASS |
| evidence file `/home/king/github/growing-myself/.omo/evidence/task-10-split-weread-prompts-by-stage.md` | `git diff --no-index --check /dev/null` | no output | PASS |
| append-only notepad `/home/king/github/growing-myself/.omo/notepads/split-weread-prompts-by-stage/learnings.md` | tracked `git diff --check --` | no output | PASS |

PASS:

- PASS: the Stage 1 prompt was created from the immutable snapshot and Task 8 preservation ledger, not from the mutable live router as drafting source.
- PASS: the file begins with the required inheritance block and preserves the fixed paths, dual `bookId`, import-to-official mapping workflow, data boundaries, matching rules, color default flow, idea categories, card types, Stage 1 template, and intermediate-draft format.
- PASS: Stage 1 is explicitly limited to organize, fetch, match, light pre-classify, and write intermediate draft only.
- PASS: each required literal token has a concrete hit and is paired with read-based semantic QA.
- PASS: boundary-sensitive literals are present only as boundary warnings, not as forbidden execution leakage.
- PASS: untracked-safe whitespace checks passed for the stage file and evidence file, and the append-only notepad diff check is clean.

Follow-ups / unresolved risks:

- Non-blocking: Task 9 has not rewritten the 《人生》 router yet. This Stage 1 prompt already references the exact router path and router-wins rule, but Task 14 should still cross-check final router and stage wording together.
- Non-blocking: `/home/king/github/growing-myself/路遥/人生/AGENTS.md` is still absent in the Task 8 execution record. If that file appears later, actual execution should read it then, but this split task must not invent its contents today.
