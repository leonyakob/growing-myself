# Task 2 Evidence, split-weread-prompts-by-stage

Source snapshot used:

- Immutable snapshot: `/home/king/github/growing-myself/.omo/evidence/split-weread-prompts-by-stage/source/微信读书通用提示词.before.md`
- Move-ledger / authority map: `/home/king/github/growing-myself/.omo/evidence/task-1-split-weread-prompts-by-stage.md`
- Rewrite rule for this task: use the immutable snapshot and Task 1 ledger as source of truth, not the mutable live router after rewrite.

Applicable AGENTS.md:

- `/home/king/github/growing-myself/AGENTS.md`
- Generic router rewrite in this task used root `AGENTS.md` only.
- Not applicable / not imported: any `路遥/人生/**` prompt file, `/home/king/github/growing-myself/路遥/人生/AGENTS.md`, any sibling-book `AGENTS.md`.

Files changed:

- `/home/king/github/growing-myself/微信读书通用提示词.md`
- `/home/king/github/growing-myself/.omo/evidence/task-2-split-weread-prompts-by-stage.md`
- `/home/king/github/growing-myself/.omo/notepads/split-weread-prompts-by-stage/learnings.md` (append-only)

Commands run:

- `GIT_MASTER=1 git grep -F --untracked -n "阶段文件索引（先选阶段）" -- "微信读书通用提示词.md"`
- `GIT_MASTER=1 git grep -F --untracked -n "微信读书通用提示词-第一阶段-生成中间整理稿.md" -- "微信读书通用提示词.md"`
- `GIT_MASTER=1 git grep -F --untracked -n "微信读书通用提示词-第二阶段-优化中间整理稿.md" -- "微信读书通用提示词.md"`
- `GIT_MASTER=1 git grep -F --untracked -n "微信读书通用提示词-第三阶段-迁移到正式阅读笔记.md" -- "微信读书通用提示词.md"`
- `GIT_MASTER=1 git grep -F --untracked -n "微信读书通用提示词-第四阶段-全书收束整合.md" -- "微信读书通用提示词.md"`
- `GIT_MASTER=1 git grep -F --untracked -n "/shared/start-work" -- "微信读书通用提示词.md"`
- `GIT_MASTER=1 git grep -F --untracked -n "裸 start-work" -- "微信读书通用提示词.md"`
- `GIT_MASTER=1 git grep -F --untracked -n "/start work" -- "微信读书通用提示词.md"`
- `GIT_MASTER=1 git diff --check -- "微信读书通用提示词.md"`
- `python3 - <<'PY' ... router links exist + triple-backtick count ... PY`
- `GIT_MASTER=1 git grep --untracked -E -n '第[[:space:]]*[0-9]+(\.[0-9]+)?[[:space:]]*节|§[0-9]+(\.[0-9]+)?' -- "微信读书通用提示词.md"`
- `python3 - <<'PY' ... stale numeric literal spot-check for 第 11 节 / 第 13.2 节 / §11.1 ... PY`
- `GIT_MASTER=1 git diff --no-index --check /dev/null ".omo/evidence/task-2-split-weread-prompts-by-stage.md"`

Heading coverage:

| Snapshot source range | Router target section(s) | Coverage note |
| --- | --- | --- |
| `5-12` | title + 用途 + 核心目标 | 保留用途、核心目标、证据层边界与技术字段边界。 |
| `16-27` | `## 0. 占位说明与路径规则` | 保留占位符规则，并升级为 router + 四阶段专用文件路径集。 |
| `29-40` | `### 0.1 不可降级原则与任务入口门` | 保留入口门、真实性要求、只读咨询边界、执行授权门。 |
| `44-66` | `## 1. 如何用通用提示词生成某本书专用提示词` + `### 专用提示词生成边界与验收门` | 已改成“书目专用 router + 四个书目专用阶段文件”，不再是旧单文件格式。 |
| `69-93` | `## 阶段文件索引（先选阶段）` + `## 2. 四阶段总流程` | 保留四阶段概览与进入方向，长执行正文全部留在阶段文件。 |
| `98-119` | `## 3. 多轮整理规则` | 保留多轮追加、按轮优化、跨轮重整触发条件和游标要求。 |
| `122-153` | `## 4. 阶段切换前 QA 与条件式 Git 检查点` | 保留阶段切换 QA、Git 条件授权和 `GIT_MASTER=1` 提示。 |
| `1109-1157` | `## 5. 复杂任务处理策略` | 保留正常任务 / 复杂任务 / 止损与定点校补，以及计划—审查—执行授权三重门。 |
| `1160-1236` | `## 6. 快捷模板警告与路由提醒` + `## 7. 专用提示词回归样本沉淀规则` | 保留 shortcut-template warning、不能绕门、环境化 start-work 示例边界，以及回归样本沉淀机制。 |

Read-based QA notes:

- 已通读重写后的 `/home/king/github/growing-myself/微信读书通用提示词.md` 全文。Router 以 `## 阶段文件索引（先选阶段）` 开头，紧接四列表格，满足 discoverability gate。
- Router 保留的是 authority / index / route，而不是阶段执行正文：Stage 1-4 的长执行体只在对应阶段文件中展开；router 只留摘要、进入条件、退出条件、边界提醒和文件级跳转。
- “如何生成专用提示词” 已改写为未来书目必须生成 **一个书目专用 router + 四个书目专用阶段提示词**；不再允许回到旧的单文件 mega prompt。
- 快捷模板已从“直接执行正文”改成“路由提醒”：`只整理`、`只优化轻卡`、`迁移前回源预检`、`读完整本书后执行全书收束整合` 等都明确指向具体阶段文件。
- 复杂任务规则保留了 Momus / Metis / Oracle 审查门，以及“currently registered start-work entry for this client”边界；没有把 `/shared/start-work`、`裸 start-work`、`/start work` 包装成普适用户命令。
- Evidence file 的 no-index whitespace check 曾抓到四条 exact-source sample 行尾空格；已删除后再次复检，避免把证据文件本身留成假 PASS。

Positive dry-run route scenario:

| 场景 | 应走路由 | 允许产出 | 禁止事项 |
| --- | --- | --- | --- |
| 第一阶段整理本轮新增材料 | `微信读书通用提示词-第一阶段-生成中间整理稿.md` | 中间整理稿、本轮索引、轻量预分类、`下次接着整理位置` | 不得做深度评价，不得写正式阅读笔记 |
| 第二阶段优化中间整理稿 | `微信读书通用提示词-第二阶段-优化中间整理稿.md` | 在 `{中间稿路径}` 原条目下补 `AI轻评` / `AI评价` / `AI修正` / `AI补充` / 问题链和阶段性回答 | 不得迁移到正式阅读笔记，不得做第四阶段 whole-book consolidation |
| 第三阶段迁移到正式阅读笔记 | `微信读书通用提示词-第三阶段-迁移到正式阅读笔记.md` | 回源预检清单、正式阅读笔记更新、迁移后 QA、单条最新游标 | 不得执行全书收束整合，不得用 AI 内容覆盖原文 |
| 第四阶段全书收束整合 | `微信读书通用提示词-第四阶段-全书收束整合.md` | 阅读现场档案、文章素材索引、阅读轨迹与判断变化、待回看 / 归档不迁移 | 不得全局重跑第三阶段，不得让文章素材索引吞掉卡片 |
| `只整理，不评价` | `微信读书通用提示词-第一阶段-生成中间整理稿.md` | 第一阶段整理与轻量预分类 | 不得补 `AI评价` / `AI修正` / `AI补充` |
| `只咨询规则` / `状态检查` | router `微信读书通用提示词.md` | 只读解释、阶段判断、执行前提醒 | 不触发文件编辑、Git 操作或任何执行入口调用 |
| `提示词修改` | router `微信读书通用提示词.md`，必要时再打开对应阶段文件 | 路由规则改写、authority rule 修订、文件级跳转调整 | 不得顺手整理阅读材料，不得把阶段执行正文重新抄回总入口 |
| `生成某本书的专用提示词` | router `微信读书通用提示词.md` | 生成一个书目专用 router + 四个书目专用阶段提示词 | 不得沿用旧单文件格式，不得混入其他书目的事实或回归样本 |

Boundary / failure dry-run scenario:

- 场景：用户只说“/shared/start-work”或“/start work”，并未完成计划审查或明确执行授权。
- 读后判断：router 只把这些字面量放在警告句里，说明它们不是通用用户指令；必须回到复杂任务门，先检查是否已有审查后的计划，以及当前客户端是否存在已注册入口。
- 分类：`/shared/start-work`、`裸 start-work`、`/start work` 三个 forbidden universal-command literals 都只出现在 negative boundary wording 里，作用是“不要把它们当成通用命令”，不是在教用户普适执行入口。
- 结果：这是 failure / hold boundary，而不是直接执行入口。

Exact-source-rule preservation samples:

1. Snapshot exact source: `正式阅读笔记必须保留可读证据层：书籍划线原文、我自己写的原想法，以及确有保留价值的外部读者原话。AI评价、AI修正、AI补充只能建立在这些原文之上，不能替代它们。`
   Preserved in router: `微信读书通用提示词.md:23`.
2. Snapshot exact source: `划线无法回源、bookId 映射不明、接口失败或资料不完整时，必须保留真实状态，不得猜测、补写或伪造对应材料。`
   Preserved in router: `微信读书通用提示词.md:52`.
3. Snapshot exact source: `只有用户明确授权执行，才进入执行阶段。`
   Preserved in router: `微信读书通用提示词.md:54`.
4. Snapshot exact source: `回归样本应写明：触发场景、错误类型、必须保留或核对的证据、禁止重犯的处理方式和可验证的通过条件。它服务于该书的后续整理与 QA，不应被复制到通用提示词或其他书目的专用提示词。`
   Preserved in router: `微信读书通用提示词.md:250`.

Boundary checks:

- 未编辑四个 generic stage files。
- 未触碰任何 `路遥/人生/**` 文件。
- 未编辑阅读笔记、中间整理稿、正式阅读笔记或 `.omo/run-continuation/*.json`。
- 未修改 `.omo/notepads/split-weread-prompts-by-stage/decisions.md` 或 `problems.md`。
- Router 中不保留 Stage 1 / 2 / 3 / 4 的长执行正文；只保留路由级摘要和 authority rule。
- Router 活文案中未保留 `第 11 节`、`第 13.2 节`、`§11.1` 这类 stale numeric target wording；相关 spot-check 均为 `ABSENT`。

PASS:

### Required token checks

| Token | Grep result | Status |
| --- | --- | --- |
| `阶段文件索引（先选阶段）` | hit at `微信读书通用提示词.md:3` | PASS |
| `微信读书通用提示词-第一阶段-生成中间整理稿.md` | hits at `:6`, `:7`, `:97`, `:237` | PASS |
| `微信读书通用提示词-第二阶段-优化中间整理稿.md` | hits at `:8`, `:101`, `:238` | PASS |
| `微信读书通用提示词-第三阶段-迁移到正式阅读笔记.md` | hits at `:9`, `:105`, `:233`, `:239`, `:242` | PASS |
| `微信读书通用提示词-第四阶段-全书收束整合.md` | hits at `:10`, `:109`, `:167`, `:233`, `:240`, `:242` | PASS |

### Forbidden universal-command literal checks

| Literal | Grep result | Classification | Status |
| --- | --- | --- | --- |
| `/shared/start-work` | hit at `微信读书通用提示词.md:220` | warning-only OK; explicitly says not to present it as a universal command | PASS |
| `裸 start-work` | hit at `微信读书通用提示词.md:220` | warning-only OK; explicitly says not to present it as a universal command | PASS |
| `/start work` | hit at `微信读书通用提示词.md:220` | warning-only OK; explicitly says not to present it as a universal command | PASS |

### Markdown link-resolution results

| Relative link target | Existence | Resolved path | Status |
| --- | --- | --- | --- |
| `./微信读书通用提示词-第一阶段-生成中间整理稿.md` | EXISTS | `/home/king/github/growing-myself/微信读书通用提示词-第一阶段-生成中间整理稿.md` | PASS |
| `./微信读书通用提示词-第二阶段-优化中间整理稿.md` | EXISTS | `/home/king/github/growing-myself/微信读书通用提示词-第二阶段-优化中间整理稿.md` | PASS |
| `./微信读书通用提示词-第三阶段-迁移到正式阅读笔记.md` | EXISTS | `/home/king/github/growing-myself/微信读书通用提示词-第三阶段-迁移到正式阅读笔记.md` | PASS |
| `./微信读书通用提示词-第四阶段-全书收束整合.md` | EXISTS | `/home/king/github/growing-myself/微信读书通用提示词-第四阶段-全书收束整合.md` | PASS |

### Balanced code fence result

| Check | Result | Status |
| --- | --- | --- |
| triple backtick count | `8` | PASS |
| fence parity | `BALANCED` | PASS |

### Whitespace and stale-reference checks

| Check | Result | Status |
| --- | --- | --- |
| `GIT_MASTER=1 git diff --check -- "微信读书通用提示词.md"` | no output | PASS |
| `GIT_MASTER=1 git diff --no-index --check /dev/null ".omo/evidence/task-2-split-weread-prompts-by-stage.md"` | no output | PASS |
| `GIT_MASTER=1 git grep --untracked -E -n '第[[:space:]]*[0-9]+(\.[0-9]+)?[[:space:]]*节|§[0-9]+(\.[0-9]+)?' -- "微信读书通用提示词.md"` | no output | PASS |
| spot-check `第 11 节` | `ABSENT` | PASS |
| spot-check `第 13.2 节` | `ABSENT` | PASS |
| spot-check `§11.1` | `ABSENT` | PASS |

Follow-ups / unresolved risks:

- Non-blocking: the repo started dirty; this task stayed inside the approved write set of router + Task 2 evidence + append-only learnings.
- Non-blocking: required token greps hit the same stage filename in multiple route contexts, which is expected because the router repeats those links in the top index, the four-stage overview, and shortcut routing reminders.
- Blocking threshold for downstream Task 7: if any later generic hard QA finds a broken relative link, a reintroduced stale numeric section reference, or a restored mega-stage execution body in the router, Task 2 should be treated as regressed.
