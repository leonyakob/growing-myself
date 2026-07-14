# Task 12 Evidence, split-weread-prompts-by-stage

Source snapshot used:

- Immutable snapshot: `/home/king/github/growing-myself/.omo/evidence/split-weread-prompts-by-stage/source/《人生》微信读书提示词.before.md`
- Authoritative source range: `825-954`
- Preservation ledger: `/home/king/github/growing-myself/.omo/evidence/task-8-split-weread-prompts-by-stage.md`
- Task 8 gate rechecked before writing: `SNAPSHOT_VERBATIM_BEFORE_REWRITE: PASS`
- Source-of-truth rule followed here: Stage 3 wording came from the immutable snapshot range plus the Task 8 Stage 3 ledger and inheritance facts, not from the mutable live router body.

Applicable AGENTS.md:

- Required root rule file: `/home/king/github/growing-myself/AGENTS.md`
- Same-book rule file policy preserved: `/home/king/github/growing-myself/路遥/人生/AGENTS.md` is read only if it exists at execution time.
- Task 8 execution-state fact preserved verbatim in the new Stage 3 prompt: same-book `AGENTS.md` was absent when the snapshot was frozen, so no same-book rule was invented.
- Explicitly not imported: sibling-book `AGENTS.md`, including `/home/king/github/growing-myself/路遥/平凡的世界/AGENTS.md`.

Files changed:

- `/home/king/github/growing-myself/路遥/人生/《人生》微信读书提示词-第三阶段-迁移到正式阅读笔记.md`
- `/home/king/github/growing-myself/.omo/evidence/task-12-split-weread-prompts-by-stage.md`
- `/home/king/github/growing-myself/.omo/notepads/split-weread-prompts-by-stage/learnings.md` (append-only single line)

Commands run:

- `functions.read` on `/home/king/github/growing-myself/AGENTS.md`
- `functions.read` on `/home/king/github/growing-myself/.omo/evidence/task-8-split-weread-prompts-by-stage.md`
- `functions.read` on `/home/king/github/growing-myself/.omo/plans/split-weread-prompts-by-stage.md` offsets `1-240` and `241-331`
- `functions.read` on `/home/king/github/growing-myself/.omo/evidence/split-weread-prompts-by-stage/source/《人生》微信读书提示词.before.md` offset `825`, limit `140`
- `functions.read` on `/home/king/github/growing-myself/.omo/notepads/split-weread-prompts-by-stage`, `decisions.md`, `issues.md`, `problems.md`, and `learnings.md`
- `functions.read` on `/home/king/github/growing-myself/路遥/人生`
- `functions.read` on `/home/king/github/growing-myself/路遥/人生/《人生》微信读书提示词-第三阶段-迁移到正式阅读笔记.md`
- `GIT_MASTER=1 git grep -F --untracked -n "迁移前回源预检清单" -- "路遥/人生/《人生》微信读书提示词-第三阶段-迁移到正式阅读笔记.md"`
- `GIT_MASTER=1 git grep -F --untracked -n "正式阅读笔记结构" -- "路遥/人生/《人生》微信读书提示词-第三阶段-迁移到正式阅读笔记.md"`
- `GIT_MASTER=1 git grep -F --untracked -n "正式阅读笔记游标更新规则" -- "路遥/人生/《人生》微信读书提示词-第三阶段-迁移到正式阅读笔记.md"`
- `GIT_MASTER=1 git grep -F --untracked -n "所有材料最终都要有归宿" -- "路遥/人生/《人生》微信读书提示词-第三阶段-迁移到正式阅读笔记.md"`
- `GIT_MASTER=1 git grep -F --untracked -n "外部读者精彩高赞想法迁移规则" -- "路遥/人生/《人生》微信读书提示词-第三阶段-迁移到正式阅读笔记.md"`
- `GIT_MASTER=1 git grep -F --untracked -n "迁移后防回归 QA" -- "路遥/人生/《人生》微信读书提示词-第三阶段-迁移到正式阅读笔记.md"`
- `GIT_MASTER=1 git grep -F --untracked -n "全书收束整合" -- "路遥/人生/《人生》微信读书提示词-第三阶段-迁移到正式阅读笔记.md"`
- `GIT_MASTER=1 git grep -F --untracked -n "文章素材索引" -- "路遥/人生/《人生》微信读书提示词-第三阶段-迁移到正式阅读笔记.md"`
- `GIT_MASTER=1 git grep --untracked -E -n '第[[:space:]]*[0-9]+(\.[0-9]+)?[[:space:]]*节|§[0-9]+(\.[0-9]+)?' -- "路遥/人生/《人生》微信读书提示词-第三阶段-迁移到正式阅读笔记.md"`
- `GIT_MASTER=1 git diff --no-index --check /dev/null "/home/king/github/growing-myself/路遥/人生/《人生》微信读书提示词-第三阶段-迁移到正式阅读笔记.md"`
- `GIT_MASTER=1 git diff --no-index --check /dev/null "/home/king/github/growing-myself/.omo/evidence/task-12-split-weread-prompts-by-stage.md"` (pre-creation probe failed because the file did not yet exist, then rerun after creation)
- `ls "/home/king/github/growing-myself/.omo/notepads/split-weread-prompts-by-stage"`
- `python3 -c 'import os; path="/home/king/github/growing-myself/.omo/notepads/split-weread-prompts-by-stage/learnings.md"; line="- 2026-07-14 Task 12：book-specific Stage 3 要把“我的原想法”稳稳留在“我自己写的内容”里，同时让“全书收束整合 / 文章素材索引”只留作第四阶段边界句，才能既保原文又不越阶段。\n"; fd=os.open(path, os.O_WRONLY | os.O_APPEND); os.write(fd, line.encode("utf-8")); os.close(fd)'`
- `GIT_MASTER=1 git diff --check -- ".omo/notepads/split-weread-prompts-by-stage/learnings.md"`
- `lsp_diagnostics` on `/home/king/github/growing-myself/路遥/人生/《人生》微信读书提示词-第三阶段-迁移到正式阅读笔记.md`
- `lsp_diagnostics` on `/home/king/github/growing-myself/.omo/evidence/task-12-split-weread-prompts-by-stage.md`
- `lsp_diagnostics` on `/home/king/github/growing-myself/.omo/notepads/split-weread-prompts-by-stage/learnings.md`

Heading coverage:

| snapshot heading / area | target in new Stage 3 prompt | status |
|---|---|---|
| `## 10. 第三阶段：迁移到正式阅读笔记` | `## 继承块` + `# 《人生》第三阶段执行提示词：迁移到正式阅读笔记` + `## 触发门` + `## 固定工作原则` | PASS |
| `### 10.1 迁移前回源预检清单` | `## 迁移前回源预检清单` with internal-only table and `source ID` restriction | PASS |
| `### 10.2 正式阅读笔记结构与去除中间稿痕迹` | `## 正式阅读笔记结构` with five-block structure and formal-note leakage ban | PASS |
| `### 10.3 正式阅读笔记游标更新规则` | `## 正式阅读笔记游标更新规则` with delete-then-append cursor sequence | PASS |
| `### 10.4 所有材料最终都要有归宿` | `## 所有材料最终都要有归宿` with six-way destination table | PASS |
| `### 10.5 外部读者精彩高赞想法迁移规则` | `## 外部读者精彩高赞想法迁移规则` with five relation labels and original-quote rule | PASS |
| `### 10.6 迁移后防回归 QA 与最终验证波次` | `## 迁移后防回归 QA` with source-original, tech-field, and post-migration checks | PASS |

Literal verification:

| token | grep hit | semantic check | status |
|---|---|---|---|
| `迁移前回源预检清单` | line `44` | Internal checklist heading exists and is explicitly marked as non-body material. | PASS |
| `正式阅读笔记结构` | line `60` | Formal-note structure heading exists and contains the five required blocks. | PASS |
| `正式阅读笔记游标更新规则` | line `107` | Cursor section exists and keeps only the latest `下次接着整理位置`. | PASS |
| `所有材料最终都要有归宿` | line `123` | Destination section exists and covers all required material classes. | PASS |
| `外部读者精彩高赞想法迁移规则` | line `136` | External-reader section exists and preserves relation labels plus original-quote rule. | PASS |
| `迁移后防回归 QA` | line `156` | Anti-regression QA section exists and explicitly checks technical-field leakage. | PASS |

Exact-source-rule preservation samples:

1. Snapshot `[827]` `只有当我明确说“把已优化内容更新到正式阅读笔记”时，才执行这一阶段。` -> preserved in the inheritance-block boundary line `17` and the explicit trigger gate at line `33`.
2. Snapshot `[840-842]` `每条迁移材料必须保留书籍划线原文和“我的原想法”...采用“划线原文 / 我自己写的内容 / AI评价 / AI修正 / AI补充”的结构` -> preserved at lines `39-40` and in the structure block at lines `64-79`.
3. Snapshot `[856]` ``source ID` 只在这张清单、回源核对和 QA 中使用，不默认写入正式稿正文。` -> preserved at line `58` and reinforced in the formal-note ban list at lines `91-105` and QA line `163`.
4. Snapshot `[937]` `外部读者原话必须以原话保存，不能概括成“有读者说”。` -> preserved at line `152` with the no-summary rule stated verbatim in effect.
5. Snapshot `[948-949]` `正式稿正文没有 bookId、chapterUid、range...` / `AI修正能独立读懂，有明确文本落点` -> preserved at QA lines `163-164`.

Read-based QA notes:

- The file begins with an inheritance block and includes every required inheritance item: router path, stage purpose, required pre-read files, exact input files, exact output files, conflict rule, task boundary, Must NOT list, and QA evidence path.
- The inheritance block preserves the execution-state fact from Task 8 that same-book `AGENTS.md` was absent when the snapshot was frozen, while still allowing a future execution-time read if that file later appears.
- The new prompt explicitly keeps the formal-note skeleton `划线原文 / 我自己写的内容 / AI评价 / AI修正 / AI补充`, then separately states that `我自己写的内容` must preserve `我的原想法`, which satisfies both the snapshot wording and the root `AGENTS.md` anti-overwrite rule.
- The internal checklist is clearly separated from formal-note body prose. `source ID` is confined to internal checklist or QA only.
- Formal-note body leakage is shut down in two places, the Must NOT block and the body/QA bans, covering `source ID`, `bookId`, `chapterUid`, `range`, likes, fetch status, official-position fields, and other interface fields.
- The Stage 4 boundary is tight: both Stage 4 literals appear on the same inheritance-block line as a not-run-here warning, and nowhere else in the file do they become executable instructions.
- The new Stage 3 file contains no stale numeric section references. The numeric-reference grep returned no hits.
- `lsp_diagnostics` was invoked on all three modified Markdown files. This repo has no Markdown LSP configured, so there were no parse diagnostics to clear; verification therefore relied on full readback, token grep, boundary classification, and whitespace checks.
- Semantic QA was done by rereading the whole stage file after writing, not by grep-only success.

Positive dry-run:

| scenario | expected route from this prompt | observed from readback | status |
|---|---|---|---|
| User says: `请把《人生》中已经优化好的内容整理并更新到阅读笔记里。` | Enter this Stage 3 file, read root `AGENTS.md`, router, intermediate draft, current formal note, build the internal checklist first, then migrate into the fixed output path, and keep only one latest cursor. | The prompt provides the exact trigger gate, fixed input/output paths, internal checklist table, destination rules, and one-cursor rule. | PASS |

Boundary checks:

| check | result | status |
|---|---|---|
| `全书收束整合` grep | single hit at line `17`, only inside the inheritance-block boundary sentence saying this file does not run it | PASS |
| `文章素材索引` grep | single hit at line `17`, only inside the same inheritance-block boundary sentence saying this file does not build it | PASS |
| Boundary / failure dry-run: user says `我已经读完整本《人生》，请执行全书收束整合，并做文章素材索引。` | This file must refuse execution and treat the request as Stage 4 work, not Stage 3 migration. The current prompt text supports that refusal because both literals exist only as not-run-here boundaries. | PASS |
| Boundary / failure dry-run: user says `继续优化中间稿，不要写正式稿。` | This file must not run, because the trigger gate requires an explicit formal-note update request. | PASS |
| Forbidden file-scope check | This task did not rewrite `/home/king/github/growing-myself/路遥/人生/《人生》微信读书提示词.md`, did not create or edit Stage 1, Stage 2, or Stage 4 《人生》 prompt files, and did not edit the intermediate draft or the formal reading note. | PASS |

Whitespace checks:

| target | command style | result | status |
|---|---|---|---|
| `路遥/人生/《人生》微信读书提示词-第三阶段-迁移到正式阅读笔记.md` | `git diff --no-index --check /dev/null` | no output | PASS |
| `.omo/evidence/task-12-split-weread-prompts-by-stage.md` | `git diff --no-index --check /dev/null` | no output | PASS |
| `.omo/notepads/split-weread-prompts-by-stage/learnings.md` | tracked `git diff --check --` | no output | PASS |

PASS:

- PASS: Task 8 evidence was re-read and does contain `SNAPSHOT_VERBATIM_BEFORE_REWRITE: PASS` before any Stage 3 writing.
- PASS: The Stage 3 prompt was written from snapshot range `825-954` and the Task 8 preservation ledger, not from mutable router prose.
- PASS: The inheritance block starts the file and includes router path, purpose, required pre-reads, fixed input/output files, conflict rule, task boundary, Must NOT list, and QA evidence path.
- PASS: The new prompt explicitly preserves `划线原文 / 我自己写的内容 / AI评价 / AI修正 / AI补充`, separately protects `我的原想法`, and forbids technical-field leakage into formal-note body.
- PASS: Required migration headings all have direct token hits and matching read-based semantic coverage.
- PASS: `全书收束整合` and `文章素材索引` are present only as Stage 4 boundary warnings, not as executable instructions.
- PASS: Stale numeric section-reference grep on the new Stage 3 file returned no hits.
- PASS: The shared learnings notepad received one append-only atomic single-line addition.
- PASS: Stage-file no-index whitespace check, evidence-file no-index whitespace check, and tracked notepad diff check all passed.

Follow-ups / unresolved risks:

- Non-blocking: Task 9 and Task 13 have not yet rewritten the 《人生》 router or created the Stage 4 file in this session. This task therefore preserves only the router path and Stage 4 boundary, which is the correct scope for Task 12.
- Non-blocking: Task 14 should later include this Stage 3 file in its hard QA sweep for cross-file inheritance, router routing, and whole-family consistency after the remaining 《人生》 files exist.
- Blocking threshold: if the post-write no-index whitespace rerun for this evidence file fails, or if any later reread finds Stage 4 literals used as executable instructions, Task 12 must be downgraded to `FAIL`.
