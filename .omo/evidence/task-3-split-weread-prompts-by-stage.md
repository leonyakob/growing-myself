# Task 3 Evidence, split-weread-prompts-by-stage

Source snapshot used:

- Immutable snapshot: `/home/king/github/growing-myself/.omo/evidence/split-weread-prompts-by-stage/source/微信读书通用提示词.before.md`
- Stage 1 plan anchors: `/home/king/github/growing-myself/.omo/plans/split-weread-prompts-by-stage.md:182-188`
- Task 1 move ledger: `/home/king/github/growing-myself/.omo/evidence/task-1-split-weread-prompts-by-stage.md`, especially `Stage 1` mapping and the Stage 1 rows in `Normative-language preservation ledger`.
- Stage 1 source ranges used for drafting: snapshot lines `157`, `164`, `189`, `233`, `303`, `332`, `572`, `594`, plus the Stage 1 ledger assignment that maps `157-355` and `572-657` into this file.

Applicable AGENTS.md:

- `/home/king/github/growing-myself/AGENTS.md`
- Generic Stage 1 work uses root `AGENTS.md` only.
- Not applicable and not imported: any `路遥/人生/**` file, `/home/king/github/growing-myself/路遥/人生/AGENTS.md`, or any sibling-book rules.

Files changed:

- `/home/king/github/growing-myself/微信读书通用提示词-第一阶段-生成中间整理稿.md`
- `/home/king/github/growing-myself/.omo/evidence/task-3-split-weread-prompts-by-stage.md`
- `/home/king/github/growing-myself/.omo/notepads/split-weread-prompts-by-stage/learnings.md` (append-only)

Commands run:

- `functions.read("/home/king/github/growing-myself/AGENTS.md")`
- `functions.read("/home/king/github/growing-myself/.omo/plans/split-weread-prompts-by-stage.md")`
- `functions.read("/home/king/github/growing-myself/.omo/evidence/task-1-split-weread-prompts-by-stage.md")`
- `functions.read("/home/king/github/growing-myself/.omo/evidence/split-weread-prompts-by-stage/source/微信读书通用提示词.before.md")`
- `functions.read("/home/king/github/growing-myself/微信读书通用提示词.md")`
- `functions.read("/home/king/github/growing-myself/.omo/notepads/split-weread-prompts-by-stage/learnings.md")`
- `functions.read("/home/king/github/growing-myself/.omo/notepads/split-weread-prompts-by-stage/issues.md")`
- `functions.read("/home/king/github/growing-myself/.omo/notepads/split-weread-prompts-by-stage/decisions.md")`
- `functions.read("/home/king/github/growing-myself/.omo/notepads/split-weread-prompts-by-stage/problems.md")`
- `functions.read("/home/king/github/growing-myself/微信读书通用提示词-第一阶段-生成中间整理稿.md")`
- `GIT_MASTER=1 git grep -F --untracked -n "/book/bookmarklist" -- "微信读书通用提示词-第一阶段-生成中间整理稿.md"`
- `GIT_MASTER=1 git grep -F --untracked -n "/review/list/mine" -- "微信读书通用提示词-第一阶段-生成中间整理稿.md"`
- `GIT_MASTER=1 git grep -F --untracked -n "/book/readreviews" -- "微信读书通用提示词-第一阶段-生成中间整理稿.md"`
- `GIT_MASTER=1 git grep -F --untracked -n "颜色默认流向" -- "微信读书通用提示词-第一阶段-生成中间整理稿.md"`
- `GIT_MASTER=1 git grep -F --untracked -n "想法类别" -- "微信读书通用提示词-第一阶段-生成中间整理稿.md"`
- `GIT_MASTER=1 git grep -F --untracked -n "卡片判断" -- "微信读书通用提示词-第一阶段-生成中间整理稿.md"`
- `GIT_MASTER=1 git grep -F --untracked -n "下次接着整理位置" -- "微信读书通用提示词-第一阶段-生成中间整理稿.md"`
- `GIT_MASTER=1 git grep -F --untracked -n "AI修正" -- "微信读书通用提示词-第一阶段-生成中间整理稿.md"`
- `GIT_MASTER=1 git grep -F --untracked -n "正式阅读笔记才是长期" -- "微信读书通用提示词-第一阶段-生成中间整理稿.md"`
- `GIT_MASTER=1 git grep -F --untracked -n "迁移到正式阅读笔记" -- "微信读书通用提示词-第一阶段-生成中间整理稿.md"`
- `GIT_MASTER=1 git diff --no-index --check /dev/null "微信读书通用提示词-第一阶段-生成中间整理稿.md"`  first run caught trailing whitespace on two quote placeholders.
- `GIT_MASTER=1 git diff --no-index --check /dev/null "微信读书通用提示词-第一阶段-生成中间整理稿.md"`  rerun after patch, no output.

Heading coverage:

| snapshot heading | source lines | target heading / area | coverage note |
|---|---:|---|---|
| `## 5. 数据抓取硬约束` | `157-163` | `## 3. API 与数据边界` | 两个主接口和工作流被拆开讲清。 |
| `### 5.0 中间整理稿与正式阅读笔记的数据边界` | `164-188` | `## 2. 中间整理稿与长期笔记的数据边界` | 保留工作台和长期笔记边界，明确本阶段不写正式阅读笔记。 |
| `### 5.1 跨段划线与想法匹配规则` | `189-231` | `## 5. 划线与想法匹配规则` | 精确 / 跨段 / 重叠 / 文本判断匹配完整保留。 |
| `### 5.2 同位置其他书友高赞想法默认伴随抓取规则` | `233-299` | `## 6. 同位置其他书友高赞想法默认伴随抓取规则` | 官方公开版定位、接口分工、候选池、状态分类都有落点。 |
| `## 6. 颜色默认流向` | `303-328` | `## 7. 颜色默认流向` | 保留颜色名，不只保留数字。 |
| `## 7. 想法类别与卡片类型` | `332-355` | `## 8. 想法类别` + `## 9. 卡片判断` | 想法类别和后续处理类型分开写，边界更清楚。 |
| `## 9. 第一阶段：生成中间整理稿` | `572-592` | `## 10. 第一阶段执行模板` | 第一阶段执行口令完整转入。 |
| `### 中间整理稿格式` | `594-657` | `## 11. 中间整理稿格式` | 中间稿骨架、本轮索引、`下次接着整理位置` 都在。 |

Exact-source-rule preservation samples:

1. Snapshot `166-168` preserved in target `41-49`: `中间整理稿是可回源的工作台...` and `技术字段不能替代划线原文，不默认写入正文，也不能以标题或编号形式伪装成证据层。`
2. Snapshot `185` preserved in target `53` and `196`: `不要只输出我的想法` and `必须同时获取两路数据` / `必须同时调用 /book/bookmarklist 和 /review/list/mine`.
3. Snapshot `247-248` preserved in target `83-88`: 不得因为个人笔记 bookId 下 `/book/bestbookmarks` 为空，或个人 range 直接调用 `/book/readreviews` 返回错误，就判定同位置没有高赞想法。
4. Snapshot `299` preserved in target `148`: `高赞想法只能作为外部读者材料，不得替代我的感受、问题和判断。`
5. Snapshot `591` preserved in target `208`: `如果文件不存在就新建；如果已存在，就追加为新一轮整理。不要修改其他文件。`

Read-based QA notes:

- 读回成稿后，继承块位于文件开头，包含 router path、阶段目的、必读文件、输入材料、输出文件格式、router-wins 冲突规则、任务边界、Must NOT、QA evidence path，满足新会话入口要求。
- `## 2` 到 `## 6` 把 Stage 1 的核心拆成三条边界线：中间稿与长期笔记边界、个人数据与公开版定位边界、个人想法与外部读者材料边界。没有把 Stage 2 的文学深挖和 Stage 3 的正式迁移混进执行正文。
- `## 4. 官方公开版 bookId 映射规则` 明确区分个人笔记 bookId、官方公开版 bookId 和两者关系，且保留“待确认”状态，没有借用任何《人生》专属 ID。
- `## 7`、`## 8`、`## 9` 都停在轻量预分类，没有把“想法类别”和“卡片判断”写成深度优化动作。
- `## 10. 第一阶段执行模板` 明确要求同时抓 `/book/bookmarklist` 和 `/review/list/mine`，并把 `/book/readreviews` 放在“稳定映射后才调用”的位置，符合 Stage 1 只做筛取和初筛的边界。
- `## 11. 中间整理稿格式` 保留了阅读顺序、`颜色默认流向`、`想法类别`、`卡片判断`、外部读者状态和 `下次接着整理位置`，可以直接作为中间稿落盘骨架。
- `## 12. 第一阶段 QA` 不是字面重复，而是把 Stage 1 完成条件收束成一份执行后检查清单，特别检查“没有进入第二阶段深度评价，没有执行 AI修正，没有写迁移到正式阅读笔记的动作”。
- 通读未发现《人生》人物、bookId、样本 ID、路径污染，也未发现 sibling-book AGENTS 规则混入。

Per-token checks:

| token | sample hit lines | status |
|---|---|---|
| `/book/bookmarklist` | `8, 61, 74, 196` | PASS |
| `/review/list/mine` | `8, 62, 73, 196` | PASS |
| `/book/readreviews` | `8, 68, 76, 85, 134, 145` | PASS |
| `颜色默认流向` | `150, 152, 154, 202, 237, 285` | PASS |
| `想法类别` | `167, 169, 202, 238, 285` | PASS |
| `卡片判断` | `178, 180, 202, 239, 285` | PASS |
| `下次接着整理位置` | `11, 204, 225, 276, 288` | PASS |

Boundary checks:

| literal token | sample hit lines | classification | note |
|---|---|---|---|
| `AI修正` | `12, 291` | boundary-only OK | 只出现在 Must NOT 和 QA 禁行句里，没有作为执行动作。 |
| `正式阅读笔记才是长期` | `45` | boundary-only OK | 只用于说明中间稿与长期笔记的边界。 |
| `迁移到正式阅读笔记` | `12, 49, 291` | boundary-only OK | 只出现在禁止句和边界句里，没有把 Stage 3 动作塞进 Stage 1。 |

Whitespace check:

- First `git diff --no-index --check` result: `FAIL`, two trailing whitespace hits at target lines `243` and `247`.
- Fix applied: removed the two trailing spaces after Markdown quote placeholders.
- Second `git diff --no-index --check` result: `PASS`, no output.

PASS:

- PASS: Stage 1 prompt was created from the immutable snapshot + Task 1 ledger, not from later router edits.
- PASS: the file begins with an inheritance block that includes all required items.
- PASS: API/data boundaries, matching rules, official/public bookId mapping rules, color default flow, idea categories, card types, Stage 1 execution template, intermediate draft format, and Stage 1 QA are all present.
- PASS: required literal-token checks each have a concrete hit and are paired with read-based semantic QA.
- PASS: boundary-sensitive literals are present only as boundary warnings, not as forbidden execution leakage.
- PASS: final untracked-safe whitespace check is clean.

Follow-ups / unresolved risks:

- Non-blocking: the prompt uses a generic QA evidence-path pattern plus the current split-task example. Future non-split executions should replace `<current-task>` with the active task evidence file name.
- Non-blocking: `bookId关系` is recorded in the intermediate-draft format, but the real execution still depends on the caller actually confirming or marking `待确认` before pulling public highlights.
