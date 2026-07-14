# Task 14 Evidence, split-weread-prompts-by-stage

Source snapshot used:

- Immutable Wave 2 snapshot for rule provenance: `/home/king/github/growing-myself/.omo/evidence/split-weread-prompts-by-stage/source/《人生》微信读书提示词.before.md`
- Live files verified in this hard gate:
  - `/home/king/github/growing-myself/路遥/人生/《人生》微信读书提示词.md`
  - `/home/king/github/growing-myself/路遥/人生/《人生》微信读书提示词-第一阶段-生成中间整理稿.md`
  - `/home/king/github/growing-myself/路遥/人生/《人生》微信读书提示词-第二阶段-优化中间整理稿.md`
  - `/home/king/github/growing-myself/路遥/人生/《人生》微信读书提示词-第三阶段-迁移到正式阅读笔记.md`
  - `/home/king/github/growing-myself/路遥/人生/《人生》微信读书提示词-第四阶段-全书收束整合.md`
- Prior Wave 2 evidence re-read for inheritance expectations: `/home/king/github/growing-myself/.omo/evidence/task-8-split-weread-prompts-by-stage.md` through `/home/king/github/growing-myself/.omo/evidence/task-13-split-weread-prompts-by-stage.md`
- Stage 4 fixture source re-read: `/home/king/github/growing-myself/.omo/evidence/fixtures/add-whole-book-consolidation-model.md`

Applicable AGENTS.md:

- Required root rule file: `/home/king/github/growing-myself/AGENTS.md`
- Same-book conditional rule file remains execution-time only: `/home/king/github/growing-myself/路遥/人生/AGENTS.md`
- Task 8 recorded that same-book `AGENTS.md` was absent at snapshot time, so this hard gate treats root `AGENTS.md` as the only live rule source and verifies that no file invents same-book contents.
- Explicitly excluded: `/home/king/github/growing-myself/路遥/平凡的世界/AGENTS.md` and any sibling-book `AGENTS.md`

Files changed:

- `/home/king/github/growing-myself/.omo/evidence/task-14-split-weread-prompts-by-stage.md`
- `/home/king/github/growing-myself/.omo/notepads/split-weread-prompts-by-stage/learnings.md` (append-only, one line)

Commands run:

- `functions.codegraph_codegraph_explore("《人生》微信读书提示词.md 第一阶段 第二阶段 第三阶段 第四阶段 task-14-split-weread-prompts-by-stage.md")` -> no relevant code found, so the QA continued with Read / Bash.
- `functions.read` on:
  - `/home/king/github/growing-myself/.omo/plans/split-weread-prompts-by-stage.md` ranges covering Task 14 and final success criteria
  - `/home/king/github/growing-myself/路遥/人生/《人生》微信读书提示词.md`
  - `/home/king/github/growing-myself/路遥/人生/《人生》微信读书提示词-第一阶段-生成中间整理稿.md`
  - `/home/king/github/growing-myself/路遥/人生/《人生》微信读书提示词-第二阶段-优化中间整理稿.md`
  - `/home/king/github/growing-myself/路遥/人生/《人生》微信读书提示词-第三阶段-迁移到正式阅读笔记.md`
  - `/home/king/github/growing-myself/路遥/人生/《人生》微信读书提示词-第四阶段-全书收束整合.md`
  - `/home/king/github/growing-myself/.omo/evidence/task-8-split-weread-prompts-by-stage.md`
  - `/home/king/github/growing-myself/.omo/evidence/task-9-split-weread-prompts-by-stage.md`
  - `/home/king/github/growing-myself/.omo/evidence/task-10-split-weread-prompts-by-stage.md`
  - `/home/king/github/growing-myself/.omo/evidence/task-11-split-weread-prompts-by-stage.md`
  - `/home/king/github/growing-myself/.omo/evidence/task-12-split-weread-prompts-by-stage.md`
  - `/home/king/github/growing-myself/.omo/evidence/task-13-split-weread-prompts-by-stage.md`
  - `/home/king/github/growing-myself/.omo/evidence/fixtures/add-whole-book-consolidation-model.md`
  - `/home/king/github/growing-myself/.omo/notepads/split-weread-prompts-by-stage/{learnings,issues,problems,decisions}.md`
- Required per-token proof commands, one literal token per command:
  - `GIT_MASTER=1 git grep -F --untracked -n "CB_2tb79r78T38k74M75h8iz4C3" -- "路遥/人生/《人生》微信读书提示词.md" "路遥/人生/《人生》微信读书提示词-第一阶段-生成中间整理稿.md" "路遥/人生/《人生》微信读书提示词-第二阶段-优化中间整理稿.md" "路遥/人生/《人生》微信读书提示词-第三阶段-迁移到正式阅读笔记.md" "路遥/人生/《人生》微信读书提示词-第四阶段-全书收束整合.md"`
  - `GIT_MASTER=1 git grep -F --untracked -n "25164497" -- "路遥/人生/《人生》微信读书提示词.md" "路遥/人生/《人生》微信读书提示词-第一阶段-生成中间整理稿.md" "路遥/人生/《人生》微信读书提示词-第二阶段-优化中间整理稿.md" "路遥/人生/《人生》微信读书提示词-第三阶段-迁移到正式阅读笔记.md" "路遥/人生/《人生》微信读书提示词-第四阶段-全书收束整合.md"`
  - `GIT_MASTER=1 git grep -F --untracked -n "ID 003" -- "路遥/人生/《人生》微信读书提示词.md" "路遥/人生/《人生》微信读书提示词-第一阶段-生成中间整理稿.md" "路遥/人生/《人生》微信读书提示词-第二阶段-优化中间整理稿.md" "路遥/人生/《人生》微信读书提示词-第三阶段-迁移到正式阅读笔记.md" "路遥/人生/《人生》微信读书提示词-第四阶段-全书收束整合.md"`
  - `GIT_MASTER=1 git grep -F --untracked -n "ID 006" -- "路遥/人生/《人生》微信读书提示词.md" "路遥/人生/《人生》微信读书提示词-第一阶段-生成中间整理稿.md" "路遥/人生/《人生》微信读书提示词-第二阶段-优化中间整理稿.md" "路遥/人生/《人生》微信读书提示词-第三阶段-迁移到正式阅读笔记.md" "路遥/人生/《人生》微信读书提示词-第四阶段-全书收束整合.md"`
  - `GIT_MASTER=1 git grep -F --untracked -n "ID 021" -- "路遥/人生/《人生》微信读书提示词.md" "路遥/人生/《人生》微信读书提示词-第一阶段-生成中间整理稿.md" "路遥/人生/《人生》微信读书提示词-第二阶段-优化中间整理稿.md" "路遥/人生/《人生》微信读书提示词-第三阶段-迁移到正式阅读笔记.md" "路遥/人生/《人生》微信读书提示词-第四阶段-全书收束整合.md"`
  - `GIT_MASTER=1 git grep -F --untracked -n "ID 109" -- "路遥/人生/《人生》微信读书提示词.md" "路遥/人生/《人生》微信读书提示词-第一阶段-生成中间整理稿.md" "路遥/人生/《人生》微信读书提示词-第二阶段-优化中间整理稿.md" "路遥/人生/《人生》微信读书提示词-第三阶段-迁移到正式阅读笔记.md" "路遥/人生/《人生》微信读书提示词-第四阶段-全书收束整合.md"`
  - `GIT_MASTER=1 git grep -F --untracked -n "ID 117" -- "路遥/人生/《人生》微信读书提示词.md" "路遥/人生/《人生》微信读书提示词-第一阶段-生成中间整理稿.md" "路遥/人生/《人生》微信读书提示词-第二阶段-优化中间整理稿.md" "路遥/人生/《人生》微信读书提示词-第三阶段-迁移到正式阅读笔记.md" "路遥/人生/《人生》微信读书提示词-第四阶段-全书收束整合.md"`
  - `GIT_MASTER=1 git grep -F --untracked -n "刘玉海救灾处" -- "路遥/人生/《人生》微信读书提示词.md" "路遥/人生/《人生》微信读书提示词-第一阶段-生成中间整理稿.md" "路遥/人生/《人生》微信读书提示词-第二阶段-优化中间整理稿.md" "路遥/人生/《人生》微信读书提示词-第三阶段-迁移到正式阅读笔记.md" "路遥/人生/《人生》微信读书提示词-第四阶段-全书收束整合.md"`
  - `GIT_MASTER=1 git grep -F --untracked -n "黄亚萍的物质付出" -- "路遥/人生/《人生》微信读书提示词.md" "路遥/人生/《人生》微信读书提示词-第一阶段-生成中间整理稿.md" "路遥/人生/《人生》微信读书提示词-第二阶段-优化中间整理稿.md" "路遥/人生/《人生》微信读书提示词-第三阶段-迁移到正式阅读笔记.md" "路遥/人生/《人生》微信读书提示词-第四阶段-全书收束整合.md"`
- Required whitespace and stale-reference commands:
  - `GIT_MASTER=1 git diff --check -- "路遥/人生/《人生》微信读书提示词.md"`
  - `GIT_MASTER=1 git diff --no-index --check /dev/null "路遥/人生/《人生》微信读书提示词-第一阶段-生成中间整理稿.md"`
  - `GIT_MASTER=1 git diff --no-index --check /dev/null "路遥/人生/《人生》微信读书提示词-第二阶段-优化中间整理稿.md"`
  - `GIT_MASTER=1 git diff --no-index --check /dev/null "路遥/人生/《人生》微信读书提示词-第三阶段-迁移到正式阅读笔记.md"`
  - `GIT_MASTER=1 git diff --no-index --check /dev/null "路遥/人生/《人生》微信读书提示词-第四阶段-全书收束整合.md"`
  - `GIT_MASTER=1 git grep --untracked -E -n '第[[:space:]]*[0-9]+(\.[0-9]+)?[[:space:]]*节|§[0-9]+(\.[0-9]+)?' -- "路遥/人生/《人生》微信读书提示词.md" "路遥/人生/《人生》微信读书提示词-第一阶段-生成中间整理稿.md" "路遥/人生/《人生》微信读书提示词-第二阶段-优化中间整理稿.md" "路遥/人生/《人生》微信读书提示词-第三阶段-迁移到正式阅读笔记.md" "路遥/人生/《人生》微信读书提示词-第四阶段-全书收束整合.md"`
- Structural QA scripts:
  - `python3 - <<'PY' ... validate router table headers, all Markdown links, code-fence balance, fixed paths, conflict rules, article directions, fixture path, and all 9 fixture-case labels ... PY`
  - `python3 - <<'PY' ... extract heading inventory for router + 4 stage files ... PY`
- Generic contamination direction check:
  - `GIT_MASTER=1 git grep --untracked -E -n "CB_2tb79r78T38k74M75h8iz4C3|25164497|高加林|巧珍|黄亚萍|刘玉海救灾处|ID 003|ID 117" -- "微信读书通用提示词.md" "微信读书通用提示词-第一阶段-生成中间整理稿.md" "微信读书通用提示词-第二阶段-优化中间整理稿.md" "微信读书通用提示词-第三阶段-迁移到正式阅读笔记.md" "微信读书通用提示词-第四阶段-全书收束整合.md"`
- Post-write diagnostics and file-hygiene checks:
  - `functions.lsp_diagnostics("/home/king/github/growing-myself/路遥/人生/《人生》微信读书提示词.md")`
  - `functions.lsp_diagnostics("/home/king/github/growing-myself/路遥/人生/《人生》微信读书提示词-第一阶段-生成中间整理稿.md")`
  - `functions.lsp_diagnostics("/home/king/github/growing-myself/路遥/人生/《人生》微信读书提示词-第二阶段-优化中间整理稿.md")`
  - `functions.lsp_diagnostics("/home/king/github/growing-myself/路遥/人生/《人生》微信读书提示词-第三阶段-迁移到正式阅读笔记.md")`
  - `functions.lsp_diagnostics("/home/king/github/growing-myself/路遥/人生/《人生》微信读书提示词-第四阶段-全书收束整合.md")`
  - `functions.lsp_diagnostics("/home/king/github/growing-myself/.omo/evidence/task-14-split-weread-prompts-by-stage.md")`
  - `functions.lsp_diagnostics("/home/king/github/growing-myself/.omo/notepads/split-weread-prompts-by-stage/learnings.md")`
  - `GIT_MASTER=1 git diff --no-index --check /dev/null ".omo/evidence/task-14-split-weread-prompts-by-stage.md"`
  - `GIT_MASTER=1 git diff --check -- ".omo/notepads/split-weread-prompts-by-stage/learnings.md"`

Per-file heading coverage:

| file | required coverage | observed headings / areas | status |
|---|---|---|---|
| `路遥/人生/《人生》微信读书提示词.md` | router discoverability, fixed paths, dual bookId, stage flow, QA / Git gate, article-direction summary, complex-task gate, regression sentinels | `## 阶段文件索引（先选阶段）`, `## 0. 《人生》固定路径、双 bookId 与执行前必读`, `## 1. 不可降级原则与任务入口门`, `## 2. 四阶段总流程`, `## 3. 多轮整理规则`, `## 4. 阶段切换前 QA 与条件性 Git 检查点`, `## 5. 《人生》专用事实与阶段摘要`, `### 5.1`, `### 5.2`, `## 6. 大任务处理策略`, `## 7. 快捷模板警告与路由提醒`, `## 8. 《人生》已知回归风险与定点校勘样本` | PASS |
| `路遥/人生/《人生》微信读书提示词-第一阶段-生成中间整理稿.md` | inheritance block, fixed paths, Stage 1 entry, data boundary, fetch / match, public-position mapping, color flow, idea / card classification, template, draft format, QA | `## 继承块`, `## 1. 固定路径与书籍身份`, `## 2. 任务入口规则`, `## 3. 中间整理稿与正式稿的数据边界`, `## 4. 数据抓取与匹配规则`, `### 4.1`, `### 4.2`, `### 4.3`, `## 5. 导入版到官方公开版的同位置映射工作流`, `### 5.1-5.4`, `## 6. 颜色默认流向`, `## 7. 想法类别`, `## 8. 卡片判断`, `## 9. 第一阶段执行模板`, `## 10. 中间整理稿格式`, `## 11. 第一阶段 QA` | PASS |
| `路遥/人生/《人生》微信读书提示词-第二阶段-优化中间整理稿.md` | inheritance block, AGENTS toolbox, literary-analysis rules, diagnosis, light-card, complete / main-card, pending-material, external-reader analysis, QA | `# 继承块`, `# 《人生》第二阶段执行提示词，优化中间整理稿`, `## 必须继承的文学分析工具箱`, `## 文学分析质量规则`, `### 证据锚点与文本落点`, `### 人物心理要写出过程，不要直接贴标签`, `### 文本歧义与心理雾区不能一笔带过`, `### 完整卡和主卡候选必须打开矛盾`, `### AI 要提供表达增量`, `### AI 可以反驳，但必须指出缺失的分析环节`, `### 大胆分析，但不要省掉过程`, `### 升级问题链后必须给出阶段性回答`, `### AI修正必须深化，不只是整理语序`, `### 文学表达不是轻卡专属`, `### 分析后命名，而非先命名硬套`, `## 本轮优化前诊断`, `## 第N轮优化前诊断`, `## 轻卡优化规则`, `## 完整卡 / 主卡优化规则`, `## 暂存素材处理规则`, `## 外部读者高赞想法分析规则`, `## 第二阶段 QA` | PASS |
| `路遥/人生/《人生》微信读书提示词-第三阶段-迁移到正式阅读笔记.md` | inheritance block, trigger, formal-note structure, cursor, material destinations, external-reader migration, post-migration QA | `## 继承块`, `# 《人生》第三阶段执行提示词：迁移到正式阅读笔记`, `## 触发门`, `## 固定工作原则`, `## 迁移前回源预检清单`, `## 正式阅读笔记结构`, `## 正式阅读笔记游标更新规则`, `## 所有材料最终都要有归宿`, `## 外部读者精彩高赞想法迁移规则`, `## 迁移后防回归 QA` | PASS |
| `路遥/人生/《人生》微信读书提示词-第四阶段-全书收束整合.md` | inheritance boundary, default model, Stage 3 / 4 split, internal ledger, order, one-card-two-destinations, reading archive, article index, duplicate / misreading rules, bloat control, fixture QA | blockquote inheritance boundary at lines `1-26`, then `## 本阶段的默认模型`, `## 《人生》专属继承约束`, `## 触发门与前置检查`, `## 第三阶段与第四阶段的分工`, `## 执行顺序`, `## 内部整合台账`, `## 一卡双归宿`, `## 正式阅读笔记中的全书结构`, `## 全书收束整合`, `### 一、阅读现场档案`, `### 二、文章素材索引`, `### 三、阅读轨迹与判断变化`, `### 四、待回看 / 归档不迁移`, `## 《人生》文章素材索引表`, `## 重复卡、改判链与误读修正`, `## 外部读者材料与正式稿膨胀防控`, `## fixture 对照与 Stage 4 QA`, `## 可直接复制的执行触发语` | PASS |

Per-token PASS rows for required sentinel / bookId checks:

| token | grep-observed live rule / inherited sentinel locations | semantic classification | status |
|---|---|---|---|
| `CB_2tb79r78T38k74M75h8iz4C3` | router lines `37`, `49`; Stage 1 lines `9`, `21`, `134`, `137`, `235`, `259`, `334` | live dual-bookId rule in router, live Stage 1 execution and QA rule in inherited Stage 1 prompt | PASS |
| `25164497` | router lines `38`, `50`; Stage 1 lines `9`, `22`, `135`, `137`, `235`, `260`, `334` | live dual-bookId rule in router, live public-position mapping and QA rule in inherited Stage 1 prompt | PASS |
| `ID 003` | router line `224`; Stage 4 lines `48`, `239` | router regression sentinel plus Stage 4 inherited sentinel / anti-anchor rule | PASS |
| `ID 006` | router line `225`; Stage 4 line `49` | router regression sentinel plus Stage 4 inherited sentinel list | PASS |
| `ID 021` | router line `226`; Stage 4 line `50` | router regression sentinel plus Stage 4 inherited sentinel list | PASS |
| `ID 109` | router line `227`; Stage 4 line `51` | router regression sentinel plus Stage 4 inherited sentinel list | PASS |
| `ID 117` | router line `228`; Stage 4 line `52` | router regression sentinel plus Stage 4 inherited sentinel list | PASS |
| `刘玉海救灾处` | router line `229`; Stage 4 line `53` | router regression sentinel plus Stage 4 inherited sentinel list | PASS |
| `黄亚萍的物质付出` | router line `230`; Stage 4 line `54` | router regression sentinel plus Stage 4 inherited sentinel list | PASS |

Markdown link validation:

| source file | validation result | status |
|---|---|---|
| router `《人生》微信读书提示词.md` | router table header `| 用户意图 | 应打开的文件 | 允许产出 | 禁止事项 |` exists; all Markdown links resolve to existing stage files under `/home/king/github/growing-myself/路遥/人生/`; repeated links are duplicates of the same four valid targets | PASS |
| Stage 1 | no Markdown links present, so no unresolved relative links | PASS |
| Stage 2 | no Markdown links present, so no unresolved relative links | PASS |
| Stage 3 | no Markdown links present, so no unresolved relative links | PASS |
| Stage 4 | no Markdown links present, so no unresolved relative links | PASS |

Code-fence validation:

| file | fence count | balanced | status |
|---|---:|---|---|
| router | `0` | yes | PASS |
| Stage 1 | `4` | yes | PASS |
| Stage 2 | `20` | yes | PASS |
| Stage 3 | `4` | yes | PASS |
| Stage 4 | `8` | yes | PASS |

Fixed-path, conflict-rule, and article-direction validation:

| check | observed result | status |
|---|---|---|
| fixed path trio across router + all four stage files | all five files contain `/home/king/github/growing-myself/路遥/人生/《人生》中间整理稿.md`, `/home/king/github/growing-myself/路遥/人生/《人生》阅读笔记.md`, and `/home/king/github/growing-myself/路遥/人生/《人生》微信读书提示词.md` where relevant inherited execution context is defined | PASS |
| router discoverability table | top table exists with required four columns and routes to all four stage files | PASS |
| Stage 1 conflict rule | `如果本阶段提示词与总提示词冲突，以总提示词为准。` present | PASS |
| Stage 2 conflict rule | `如果本提示词与 router 冲突，以 router 为准。` present | PASS |
| Stage 3 conflict rule | `如果本阶段提示词与路由文件冲突，以路由文件为准。` present | PASS |
| Stage 4 conflict rule | `若本文件与 router 冲突，以 router 为准。` present | PASS |
| Stage 4 article directions remain visible | `人物线`、`城乡主题`、`尊严主题`、`爱情线`、`知识分子困境`、`写法线索` all present in router summary and Stage 4 prompt | PASS |

Fixture QA and Stage 4 inheritance validation:

| check | observed result | status |
|---|---|---|
| Stage 4 prompt references fixture file | absolute path `/home/king/github/growing-myself/.omo/evidence/fixtures/add-whole-book-consolidation-model.md` present in Stage 4 pre-read block and QA section | PASS |
| Case 1 | present in Stage 4 fixture table with partially migrated card handling | PASS |
| Case 2 | present in Stage 4 fixture table with duplicate same quote + same insight handling | PASS |
| Case 3 | present in Stage 4 fixture table with changed-judgment revision-chain handling | PASS |
| Case 4 | present in Stage 4 fixture table with same-scene different `source ID/range` dedupe handling | PASS |
| Case 5 | present in Stage 4 fixture table with early misreading preservation handling | PASS |
| Case 6 | present in Stage 4 fixture table with external high-like challenge handling | PASS |
| Case 7 | present in Stage 4 fixture table with external-only strong comment boundary | PASS |
| Case 8 | present in Stage 4 fixture table with light-card-in-index-but-not-upgraded handling | PASS |
| Case 9 | present in Stage 4 fixture table with final-note bloat prevention / `归档不迁移` handling | PASS |

Diagnostics and post-write whitespace:

| target | tool / command | observed result | status |
|---|---|---|---|
| router `《人生》微信读书提示词.md` | `functions.lsp_diagnostics` | `No LSP server configured for extension: .md` | PASS, tooling state recorded honestly |
| Stage 1 | `functions.lsp_diagnostics` | `No LSP server configured for extension: .md` | PASS, tooling state recorded honestly |
| Stage 2 | `functions.lsp_diagnostics` | `No LSP server configured for extension: .md` | PASS, tooling state recorded honestly |
| Stage 3 | `functions.lsp_diagnostics` | `No LSP server configured for extension: .md` | PASS, tooling state recorded honestly |
| Stage 4 | `functions.lsp_diagnostics` | `No LSP server configured for extension: .md` | PASS, tooling state recorded honestly |
| Task 14 evidence | `functions.lsp_diagnostics` | `No LSP server configured for extension: .md` | PASS, tooling state recorded honestly |
| learnings append target | `functions.lsp_diagnostics` | `No LSP server configured for extension: .md` | PASS, tooling state recorded honestly |
| Task 14 evidence | `GIT_MASTER=1 git diff --no-index --check /dev/null` | no output | PASS |
| learnings append target | `GIT_MASTER=1 git diff --check --` | no output | PASS |

Read-based QA notes:

- Router-level discoverability passed. The router begins with the required stage-selection table and routes first-stage organization, second-stage optimization, third-stage migration, fourth-stage whole-book consolidation, only-consulting, status-check, and prompt-modification correctly.
- Stage 1 boundary passed on reread. The body authorizes only organize, fetch, match, official-position mapping, light pre-classification, and writing the intermediate draft. `AI修正` / migration / whole-book consolidation appear only in `Must NOT` and QA stop-lines.
- Stage 2 boundary passed on reread. The file keeps my original thoughts unchanged, places AI material below them, preserves the root `AGENTS.md` literary toolbox, and forbids formal-note writes.
- Stage 3 boundary passed on reread. The trigger is explicit, formal-note technical-field leakage is explicitly banned, and `全书收束整合` / `文章素材索引` appear only as fourth-stage boundary warnings.
- Stage 4 boundary passed on reread. The execution order is explicit: `内部整合台账` first, `阅读现场档案` second, `文章素材索引` third, then `阅读轨迹与判断变化` and `待回看 / 归档不迁移`. The prompt authorizes only local补迁 / 重迁 conditions and does not globally rerun Stage 3.
- Regression-sentinel inheritance passed. The router keeps all seven 《人生》 sentinels as router-level authority, and Stage 4 inherits them as book-specific QA material. The dual `bookId` facts stay live in router + Stage 1, where the import-to-official mapping actually matters.
- Generic contamination isolation passed directionally. The combined grep over the generic router and four generic stage files returned no output for representative 《人生》-specific facts and names, so the book-specific facts remain isolated to the 《人生》 outputs. This Task 14 QA also does not edit generic outputs.

Boundary checks:

- No blocking QA failure was found in the five 《人生》 prompt files, so this task did not edit any of them.
- This task did not edit `/home/king/github/growing-myself/路遥/人生/《人生》中间整理稿.md`.
- This task did not edit `/home/king/github/growing-myself/路遥/人生/《人生》阅读笔记.md`.
- This task did not edit generic prompt files.
- This task did not edit `/home/king/github/growing-myself/.omo/plans/split-weread-prompts-by-stage.md`.
- This task did not touch `.omo/run-continuation/*.json`.
- Stale numeric section-reference grep across the five 《人生》 prompt files returned no output, so there is no unclassified `第 X 节` or `§X` failure.

PASS:

- PASS: tracked-router whitespace check returned no output.
- PASS: untracked-safe whitespace checks returned no output for Stage 1, Stage 2, Stage 3, and Stage 4.
- PASS: untracked-safe whitespace check returned no output for Task 14 evidence, and tracked diff check returned no output for the append-only learnings file.
- PASS: router top table has `用户意图 / 应打开的文件 / 允许产出 / 禁止事项` and all four linked stage files resolve correctly.
- PASS: every 《人生》 stage file explicitly says router wins if conflict occurs.
- PASS: fixed paths, dual `bookId`, stage boundaries, article directions, regression sentinels, and fixture coverage all survived hard QA.
- PASS: generic contamination direction check returned no output for representative 《人生》 facts.
- PASS: `lsp_diagnostics` was run on all five 《人生》 prompt files, on Task 14 evidence, and on the changed learnings file. Markdown LSP is unavailable in this workspace, and that tooling-state limitation is recorded instead of being hidden.
- PASS: no blocking QA failure was found, so the split remains eligible for final verification.
- LIFE HARD QA: PASS

Follow-ups / unresolved risks:

- Pending final verification wave only. Task 14 found no blocking defect in the 《人生》 router or stage prompts.
