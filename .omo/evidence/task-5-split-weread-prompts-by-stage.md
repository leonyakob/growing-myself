# Task 5 Evidence, split-weread-prompts-by-stage

Source snapshot used:

- Immutable snapshot: `/home/king/github/growing-myself/.omo/evidence/split-weread-prompts-by-stage/source/微信读书通用提示词.before.md`
- Move ledger: `/home/king/github/growing-myself/.omo/evidence/task-1-split-weread-prompts-by-stage.md`
- Stage 3 source anchors required by the plan and this task: snapshot lines `846`, `869`, `879`, `918`, `930`, `943`, `963`.
- Execution rule followed here: Stage 3 prompt prose was written from the immutable snapshot plus the Task 1 move ledger only. The live router path `/home/king/github/growing-myself/微信读书通用提示词.md` was treated as target authority for inheritance and conflict resolution, not as mutable source material.

Applicable AGENTS.md:

- `/home/king/github/growing-myself/AGENTS.md`
- Generic Stage 3 work uses root `AGENTS.md` only.
- Not imported: any `路遥/人生/**` file, any sibling-book `AGENTS.md`, any book-specific path or regression sample.

Files changed:

- `/home/king/github/growing-myself/微信读书通用提示词-第三阶段-迁移到正式阅读笔记.md`
- `/home/king/github/growing-myself/.omo/evidence/task-5-split-weread-prompts-by-stage.md`
- `/home/king/github/growing-myself/.omo/notepads/split-weread-prompts-by-stage/learnings.md` (append-only)

Commands run:

- `GIT_MASTER=1 git grep -F --untracked -n "迁移前回源预检" -- "微信读书通用提示词-第三阶段-迁移到正式阅读笔记.md"`
- `GIT_MASTER=1 git grep -F --untracked -n "正式阅读笔记结构" -- "微信读书通用提示词-第三阶段-迁移到正式阅读笔记.md"`
- `GIT_MASTER=1 git grep -F --untracked -n "下次接着整理位置" -- "微信读书通用提示词-第三阶段-迁移到正式阅读笔记.md"`
- `GIT_MASTER=1 git grep -F --untracked -n "所有材料最终都要有归宿" -- "微信读书通用提示词-第三阶段-迁移到正式阅读笔记.md"`
- `GIT_MASTER=1 git grep -F --untracked -n "迁移后防回归 QA" -- "微信读书通用提示词-第三阶段-迁移到正式阅读笔记.md"`
- `GIT_MASTER=1 git grep -F --untracked -n "全书收束整合" -- "微信读书通用提示词-第三阶段-迁移到正式阅读笔记.md"`
- `GIT_MASTER=1 git grep -F --untracked -n "文章素材索引" -- "微信读书通用提示词-第三阶段-迁移到正式阅读笔记.md"`
- `GIT_MASTER=1 git diff --no-index --check /dev/null "/home/king/github/growing-myself/微信读书通用提示词-第三阶段-迁移到正式阅读笔记.md"`
- `GIT_MASTER=1 git diff --no-index --check /dev/null "/home/king/github/growing-myself/.omo/evidence/task-5-split-weread-prompts-by-stage.md"`
- `GIT_MASTER=1 git diff --no-index --check /dev/null "/home/king/github/growing-myself/.omo/notepads/split-weread-prompts-by-stage/learnings.md"`
- `functions.read("/home/king/github/growing-myself/AGENTS.md")`
- `functions.read("/home/king/github/growing-myself/.omo/plans/split-weread-prompts-by-stage.md")`
- `functions.read("/home/king/github/growing-myself/.omo/evidence/task-1-split-weread-prompts-by-stage.md")`
- `functions.read("/home/king/github/growing-myself/.omo/evidence/split-weread-prompts-by-stage/source/微信读书通用提示词.before.md", offset=846, limit=150)`
- `functions.read("/home/king/github/growing-myself/微信读书通用提示词-第三阶段-迁移到正式阅读笔记.md")`
- `functions.read("/home/king/github/growing-myself/.omo/evidence/task-5-split-weread-prompts-by-stage.md")`

Heading coverage:

| source heading or rule block | target location | status | note |
|---|---|---|---|
| `## 11. 第三阶段：迁移到正式阅读笔记` | `# 第三阶段：迁移到正式阅读笔记` | PASS | Stage trigger, migration scope, and high-level rules preserved. |
| `### 11.1 迁移前回源预检` | `## 迁移前回源预检` | PASS | Internal checklist preserved and expanded with chapter/range/source-original checks required by this task. |
| `### 11.2 正式阅读笔记结构与去除中间稿痕迹` | `## 正式阅读笔记结构` | PASS | Required order `划线原文 / 我自己写的内容 / AI评价 / AI修正 / AI补充` preserved, plus anti-process-trace rules. |
| `### 11.3 正式阅读笔记游标更新规则` | `## 下次接着整理位置` | PASS | One-live-cursor rule preserved and made explicit. |
| `### 11.4 所有材料最终都要有归宿` | `## 所有材料最终都要有归宿` | PASS | Destination rules preserved for main cards, complete cards, light cards, pending materials, and external-reader materials. |
| `### 11.5 外部读者材料迁移规则` | `## 外部读者材料迁移规则` | PASS | Five relation types and original-quote boundary preserved. |
| `### 11.6 迁移后防回归 QA` | `## 迁移后防回归 QA` | PASS | Post-migration anti-regression checklist preserved. |
| Task 1 move-ledger Stage 3/4 boundary requirement | `## 第三阶段与第四阶段边界` | PASS | Boundary added as required by this task, with Stage 4 literals used only as non-execution warnings. |
| Task 1 duplicated inheritance block requirements | `## 继承块` | PASS | Router path, stage purpose, pre-reads, inputs/outputs, router-wins rule, boundary, Must NOT list, and QA evidence path all present. |

Per-token verification:

| literal token | hit summary | status |
|---|---|---|
| `迁移前回源预检` | hit at lines `40`, `152` | PASS |
| `正式阅读笔记结构` | hit at line `59` | PASS |
| `下次接着整理位置` | hits at lines `93`, `95`, `98`, `103`, `105` | PASS |
| `所有材料最终都要有归宿` | hit at line `108` | PASS |
| `迁移后防回归 QA` | hit at line `142` | PASS |

Exact-source-rule preservation samples:

1. Snapshot line `861`: `每条迁移材料必须先保留书籍划线原文，再保留“我自己写的内容”。不要用 AI修正覆盖原文。`
   - Target: Stage 3 prompt lines `27-28`, `84-85`
   - Status: PASS

2. Snapshot line `862`: `所有迁移卡按“划线原文 / 我自己写的内容 / AI评价 / AI修正 / AI补充”的顺序归档。`
   - Target: Stage 3 prompt lines `28`, `63-80`
   - Status: PASS

3. Snapshot lines `877-878`: `稳定条目编号和技术字段只用于清单、回源核对和 QA，不默认写入正式稿正文。`
   - Target: Stage 3 prompt lines `57`
   - Status: PASS

4. Snapshot lines `945-959`: `外部读者原话必须按原话保存，不得概括成“有读者说”，不得改写为用户第一人称判断。`
   - Target: Stage 3 prompt lines `137-138`
   - Status: PASS

5. Snapshot lines `965-973`: `迁移完成后，逐项完成以下 QA，未通过不得把迁移视为完成。`
   - Target: Stage 3 prompt lines `142-152`
   - Status: PASS

Read-based QA notes:

- The file starts with an inheritance block, not with execution prose. It contains the router path, stage purpose, pre-read files, exact inputs/outputs, router-wins conflict rule, task boundary, Must NOT list, and QA evidence path.
- Trigger gating is explicit. The stage only runs when the user clearly asks to update the formal reading note.
- `迁移前回源预检` is not just a heading token. The section includes a real internal checklist table, chapter/range checks, source-original recovery checks, destination decisions, and an explicit ban on fabricated material.
- `正式阅读笔记结构` preserves the required order `划线原文 / 我自己写的内容 / AI评价 / AI修正 / AI补充`, keeps originals above AI text, and forbids using `AI修正` to replace user originals.
- `下次接着整理位置` is treated as a single live cursor. The stage requires deleting the old cursor before writing the new one, which matches the snapshot's one-cursor rule.
- `所有材料最终都要有归宿` covers light cards, complete cards, main cards, pending materials, external-reader material, and unlocatable thoughts. The text does not reduce Stage 3 to “only migrate the essence.”
- `外部读者材料迁移规则` preserves the external-reader boundary. External-reader quotes stay external-reader quotes, stay in original wording, and are not rewritten into the user's first-person judgment.
- `迁移后防回归 QA` includes the required anti-regression checks for destination completeness, source-original preservation, external-reader original quote integrity, removal of workbench fields, AI readability, light-card proportionality, and checklist reconciliation.
- The Stage 4 boundary is explicit. The prompt mentions `全书收束整合` and `文章素材索引` only as warnings not to execute Stage 4 from this file.
- No 《人生》 examples, bookIds, paths, regression IDs, or sibling-book AGENTS rules appear in the prompt.

Boundary checks:

- No rewrite of `/home/king/github/growing-myself/微信读书通用提示词.md`.
- No creation or edit of Stage 1, Stage 2, or Stage 4 generic prompt files.
- No touch of any `路遥/人生/**` path.
- No modification of actual formal reading notes or intermediate drafts.
- No edit of `.omo/run-continuation/*.json`.
- Generated artifact recorded here: `/home/king/github/growing-myself/.omo/evidence/task-5-split-weread-prompts-by-stage.md`.

Boundary classification for Stage 4 literals:

| literal token | hit line(s) | classification | note |
|---|---:|---|---|
| `全书收束整合` | `10` | boundary-only OK | Must NOT list, says not to execute Stage 4. |
| `全书收束整合` | `36` | boundary-only OK | Dedicated boundary section, says not to execute Stage 4. |
| `全书收束整合` | `154` | boundary-only OK | Final stop rule, says not to continue into Stage 4. |
| `文章素材索引` | `10` | boundary-only OK | Must NOT list, says not to build Stage 4 output. |
| `文章素材索引` | `37` | boundary-only OK | Dedicated boundary section, says not to build Stage 4 output. |
| `文章素材索引` | `154` | boundary-only OK | Final stop rule, says not to build Stage 4 output. |

Follow-ups / unresolved risks:

- Non-blocking risk: this is a generic execution prompt, so `{中间稿路径}` and `{正式笔记路径}` still depend on the caller supplying the correct book-specific files.
- Non-blocking risk: the prompt intentionally does not include whole-book consolidation behavior. That work remains blocked to Stage 4.
- Blocking threshold: if any future verification finds `全书收束整合` or `文章素材索引` used as executable Stage 3 instructions, this task must flip to `FAIL`.

PASS:

- PASS: immutable snapshot plus Task 1 move ledger were used as the only source material for Stage 3 prose.
- PASS: the inheritance block contains all required fields.
- PASS: all five required literal tokens are present, with one recorded PASS row per token.
- PASS: the formal-note structure preserves `划线原文 / 我自己写的内容 / AI评价 / AI修正 / AI补充` in order and preserves source originals.
- PASS: migration trigger, precheck, cursor update, material-destination rules, external-reader migration rules, and anti-regression QA are all present.
- PASS: every Stage 4 boundary literal hit is classified as `boundary-only OK`; no hit instructs the reader to execute Stage 4 from this file.
