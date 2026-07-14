# Task 9 Evidence, split-weread-prompts-by-stage

Source snapshot used:

- Immutable snapshot: `/home/king/github/growing-myself/.omo/evidence/split-weread-prompts-by-stage/source/《人生》微信读书提示词.before.md`
- Preservation ledger: `/home/king/github/growing-myself/.omo/evidence/task-8-split-weread-prompts-by-stage.md`
- Plan anchor: `/home/king/github/growing-myself/.omo/plans/split-weread-prompts-by-stage.md` around Task 9 and final verification requirements.
- Rewrite source of truth for the router was the immutable snapshot plus Task 8 preservation facts, not the mutable live router after rewrite.

Applicable AGENTS.md:

- Required root rule file: `/home/king/github/growing-myself/AGENTS.md`
- Same-book conditional rule file: `/home/king/github/growing-myself/路遥/人生/AGENTS.md` only if it exists at execution time. Task 8 recorded that it did not exist at snapshot time, so this router keeps the conditional wording and does not invent its contents.
- Explicitly not imported: `/home/king/github/growing-myself/路遥/平凡的世界/AGENTS.md` and any sibling-book `AGENTS.md`.

Files changed:

- `/home/king/github/growing-myself/路遥/人生/《人生》微信读书提示词.md`
- `/home/king/github/growing-myself/.omo/evidence/task-9-split-weread-prompts-by-stage.md`
- `/home/king/github/growing-myself/.omo/notepads/split-weread-prompts-by-stage/learnings.md` (append-only)

Commands run:

- `functions.codegraph_codegraph_explore` with query `路遥/人生/《人生》微信读书提示词.md router markdown task 9`.
- `functions.read` on `/home/king/github/growing-myself/.omo/evidence/split-weread-prompts-by-stage/source/《人生》微信读书提示词.before.md`
- `functions.read` on `/home/king/github/growing-myself/.omo/evidence/task-8-split-weread-prompts-by-stage.md`
- `functions.read` on `/home/king/github/growing-myself/.omo/plans/split-weread-prompts-by-stage.md`
- `functions.read` on the four existing 《人生》 stage prompt files.
- `functions.read` on `/home/king/github/growing-myself/微信读书通用提示词.md`
- `ls ".omo/evidence"`
- `ls ".omo/notepads/split-weread-prompts-by-stage"`
- `GIT_MASTER=1 git grep -F --untracked -n "阶段文件索引（先选阶段）" -- "路遥/人生/《人生》微信读书提示词.md"`
- `GIT_MASTER=1 git grep -F --untracked -n "《人生》微信读书提示词-第一阶段-生成中间整理稿.md" -- "路遥/人生/《人生》微信读书提示词.md"`
- `GIT_MASTER=1 git grep -F --untracked -n "《人生》微信读书提示词-第二阶段-优化中间整理稿.md" -- "路遥/人生/《人生》微信读书提示词.md"`
- `GIT_MASTER=1 git grep -F --untracked -n "《人生》微信读书提示词-第三阶段-迁移到正式阅读笔记.md" -- "路遥/人生/《人生》微信读书提示词.md"`
- `GIT_MASTER=1 git grep -F --untracked -n "《人生》微信读书提示词-第四阶段-全书收束整合.md" -- "路遥/人生/《人生》微信读书提示词.md"`
- `GIT_MASTER=1 git grep -F --untracked -n "ID 003" -- "路遥/人生/《人生》微信读书提示词.md"`
- `GIT_MASTER=1 git grep -F --untracked -n "ID 006" -- "路遥/人生/《人生》微信读书提示词.md"`
- `GIT_MASTER=1 git grep -F --untracked -n "ID 021" -- "路遥/人生/《人生》微信读书提示词.md"`
- `GIT_MASTER=1 git grep -F --untracked -n "ID 109" -- "路遥/人生/《人生》微信读书提示词.md"`
- `GIT_MASTER=1 git grep -F --untracked -n "ID 117" -- "路遥/人生/《人生》微信读书提示词.md"`
- `GIT_MASTER=1 git grep -F --untracked -n "刘玉海救灾处" -- "路遥/人生/《人生》微信读书提示词.md"`
- `GIT_MASTER=1 git grep -F --untracked -n "黄亚萍的物质付出" -- "路遥/人生/《人生》微信读书提示词.md"`
- `GIT_MASTER=1 git grep -F --untracked -n "CB_2tb79r78T38k74M75h8iz4C3" -- "路遥/人生/《人生》微信读书提示词.md"`
- `GIT_MASTER=1 git grep -F --untracked -n "25164497" -- "路遥/人生/《人生》微信读书提示词.md"`
- `GIT_MASTER=1 git grep --untracked -E -n '第[[:space:]]*[0-9]+(\.[0-9]+)?[[:space:]]*节|§[0-9]+(\.[0-9]+)?' -- "路遥/人生/《人生》微信读书提示词.md"`
- `python3 - <<'PY' ... markdown link resolution for router links ... PY`
- `GIT_MASTER=1 git diff --check -- "路遥/人生/《人生》微信读书提示词.md"`
- `functions.lsp_diagnostics` on `/home/king/github/growing-myself/路遥/人生/《人生》微信读书提示词.md`
- `functions.lsp_diagnostics` on `/home/king/github/growing-myself/.omo/evidence/task-9-split-weread-prompts-by-stage.md`
- `functions.lsp_diagnostics` on `/home/king/github/growing-myself/.omo/notepads/split-weread-prompts-by-stage/learnings.md`
- `GIT_MASTER=1 git diff --no-index --check /dev/null ".omo/evidence/task-9-split-weread-prompts-by-stage.md"`
- `GIT_MASTER=1 git diff --check -- ".omo/notepads/split-weread-prompts-by-stage/learnings.md"`

Heading coverage:

| snapshot block | required preservation fact | router target | status |
|---|---|---|---|
| `5-9` | fixed paths | `## 0. 《人生》固定路径、双 bookId 与执行前必读` | PASS |
| `11-18` | core goals and source-original boundary | top-level `核心目标` | PASS |
| `22-31` | task entry gate | `## 1. 不可降级原则与任务入口门` | PASS |
| `34-59` | four-stage flow and formal-note write gate | top index table + `## 2. 四阶段总流程` | PASS |
| `63-84` | multi-round rules and `下次接着整理位置` | `## 3. 多轮整理规则` | PASS |
| `87-124` | stage-switch QA and conditional Git rules | `## 4. 阶段切换前 QA 与条件性 Git 检查点` | PASS |
| `213-219` | dual `bookId` mapping and official-position warning | `## 0. 《人生》固定路径、双 bookId 与执行前必读` | PASS |
| `374-376` + `391-393` | book-specific literary examples must remain visible | `### 5.1 《人生》专用文学例子仍然可见` | PASS |
| `1048` + `1067-1074` | Stage 4 article-direction summary | `### 5.2 第四阶段文章方向摘要` | PASS |
| `1159-1202` | complex-task planning gate and stop-loss rule | `## 6. 大任务处理策略` | PASS |
| `1205-1255` | shortcut warning and shortcut routing | `## 7. 快捷模板警告与路由提醒` | PASS |
| `1259-1269` | all 7 regression sentinels | `## 8. 《人生》已知回归风险与定点校勘样本` | PASS |

Literal-token verification:

| token | command result summary | status |
|---|---|---|
| `阶段文件索引（先选阶段）` | grep hit at router line `3` | PASS |
| `《人生》微信读书提示词-第一阶段-生成中间整理稿.md` | grep hits in the index table, fixed-path list, stage flow, and shortcut routing | PASS |
| `《人生》微信读书提示词-第二阶段-优化中间整理稿.md` | grep hits in the index table, fixed-path list, stage flow, book-specific example reminder, and shortcut routing | PASS |
| `《人生》微信读书提示词-第三阶段-迁移到正式阅读笔记.md` | grep hits in the index table, fixed-path list, stage flow, and shortcut routing | PASS |
| `《人生》微信读书提示词-第四阶段-全书收束整合.md` | grep hits in the index table, fixed-path list, stage flow, Stage 4 summary, and shortcut routing | PASS |
| `CB_2tb79r78T38k74M75h8iz4C3` | grep hits in the fixed-fact list and dual-bookId summary | PASS |
| `25164497` | grep hits in the fixed-fact list and dual-bookId summary | PASS |
| `ID 003` | grep hit in regression sentinel list | PASS |
| `ID 006` | grep hit in regression sentinel list | PASS |
| `ID 021` | grep hit in regression sentinel list | PASS |
| `ID 109` | grep hit in regression sentinel list | PASS |
| `ID 117` | grep hit in regression sentinel list | PASS |
| `刘玉海救灾处` | grep hit in regression sentinel list | PASS |
| `黄亚萍的物质付出` | grep hit in regression sentinel list | PASS |

Markdown link-resolution results:

| router link target | resolved path | result | status |
|---|---|---|---|
| `./《人生》微信读书提示词-第一阶段-生成中间整理稿.md` | `/home/king/github/growing-myself/路遥/人生/《人生》微信读书提示词-第一阶段-生成中间整理稿.md` | exists | PASS |
| `./《人生》微信读书提示词-第二阶段-优化中间整理稿.md` | `/home/king/github/growing-myself/路遥/人生/《人生》微信读书提示词-第二阶段-优化中间整理稿.md` | exists | PASS |
| `./《人生》微信读书提示词-第三阶段-迁移到正式阅读笔记.md` | `/home/king/github/growing-myself/路遥/人生/《人生》微信读书提示词-第三阶段-迁移到正式阅读笔记.md` | exists | PASS |
| `./《人生》微信读书提示词-第四阶段-全书收束整合.md` | `/home/king/github/growing-myself/路遥/人生/《人生》微信读书提示词-第四阶段-全书收束整合.md` | exists | PASS |

Exact-source-rule preservation samples:

1. `[17]` `正式阅读笔记必须保留三类原始材料：书籍划线原文、我的原想法、必要的外部读者原话。AI评价、AI修正、AI补充只能建立在这些原文之上，不能替代它们。` -> preserved in top-level `核心目标` item `5`.
2. `[218]` `因此，不能直接用个人导入版 CB_... + chapterUid + range 判定公开想法是否存在。正确流程是：先用个人导入版整理我的阅读现场，再按章节标题、划线原文和文本重叠映射到官方版 25164497 的同一文本位置，最后用官方版 bookId + chapterUid + range 调 /book/readreviews。` -> preserved in `## 0. 《人生》固定路径、双 bookId 与执行前必读`.
3. `[967-971]` `默认模型是“阅读现场档案 + 文章素材索引”。` / `卡片档案为底座，文章素材索引为上层导航。` / `先补齐卡片本体，再为《人生》的文章方向建立导航。` -> preserved in `## 2. 四阶段总流程` and `### 5.2 第四阶段文章方向摘要`.
4. `[1267]` `不要因为句子过于整齐就批评它。应保留这句的文气，再补出使判断成立的文本证据桥梁。` -> preserved verbatim in regression sentinel `ID 117` under `## 8. 《人生》已知回归风险与定点校勘样本`.

Dry-run scenarios:

| scenario type | user request | observed router route | expected boundary | status |
|---|---|---|---|---|
| positive dry-run | `只评价问题质量` | top index table routes to `《人生》微信读书提示词-第二阶段-优化中间整理稿.md` | only Stage 2 evaluation/optimization work is authorized, not formal-note migration | PASS |
| boundary / failure dry-run | `看看我现在该进哪个阶段，先不要改文件` | top index table routes to this router itself | only read-only explanation is authorized, no file edits, no Git, no start-work entry | PASS |

Diagnostics and whitespace checks:

| target | command | result | status |
|---|---|---|---|
| `路遥/人生/《人生》微信读书提示词.md` | `functions.lsp_diagnostics` | `No LSP server configured for extension: .md` | PASS, recorded honestly |
| `.omo/evidence/task-9-split-weread-prompts-by-stage.md` | `functions.lsp_diagnostics` | `No LSP server configured for extension: .md` | PASS, recorded honestly |
| `.omo/notepads/split-weread-prompts-by-stage/learnings.md` | `functions.lsp_diagnostics` | `No LSP server configured for extension: .md` | PASS, recorded honestly |
| `.omo/evidence/task-9-split-weread-prompts-by-stage.md` | `GIT_MASTER=1 git diff --no-index --check /dev/null` | no output | PASS |
| `.omo/notepads/split-weread-prompts-by-stage/learnings.md` | `GIT_MASTER=1 git diff --check --` | no output | PASS |
| `路遥/人生/《人生》微信读书提示词.md` | `GIT_MASTER=1 git diff --check --` | no output | PASS |

Read-based QA notes:

- The live router is now a concise router / authority / stage index, not the old 1269-line mega prompt. The detailed execution bodies were removed from the router and left in the four existing stage files.
- The router begins with `## 阶段文件索引（先选阶段）` and the table covers first-stage organization, second-stage optimization, third-stage formal-note migration, fourth-stage whole-book consolidation, only-organize, only-consulting / status-check, prompt-modification, `只评价问题质量`, `只优化轻卡`, and `全书收束整合`.
- Fixed paths, both `bookId` values, the `章节标题 + 划线原文 + 文本重叠` mapping warning, the Stage 4 direction set, the Stage 2 book-specific examples, and all seven regression sentinels remain visible in the router itself. They are not delegated away to the generic router.
- The router preserves the same-book `AGENTS.md` conditional read wording and explicitly blocks sibling-book `AGENTS.md` import.
- The router-level Git gate now says plainly that no `commit` / `push` happens unless the current user instruction explicitly asks for it.
- Multi-round policy still prioritizes this round's newly added content and still requires `下次接着整理位置` at the end of each round.
- The stale numeric-section grep on the router returned no output, so this rewrite does not introduce `第 X 节` / `§X` style stale cross-file references.
- Markdown LSP is not configured in this workspace. Diagnostics were still run on all changed Markdown files and the absence was recorded instead of being hidden.

Boundary checks:

- This Task 9 rewrite did not edit `/home/king/github/growing-myself/路遥/人生/《人生》中间整理稿.md`.
- This Task 9 rewrite did not edit `/home/king/github/growing-myself/路遥/人生/《人生》阅读笔记.md`.
- This Task 9 rewrite did not edit any generic prompt file.
- This Task 9 rewrite did not edit any other book folder.
- This Task 9 rewrite did not edit `/home/king/github/growing-myself/.omo/plans/split-weread-prompts-by-stage.md`.
- This Task 9 rewrite did not touch `.omo/run-continuation/*.json`.
- The router rewrite used the immutable snapshot and Task 8 preservation ledger as source, not the mutable live router as source text.

PASS:

- PASS: the router now starts with `## 阶段文件索引（先选阶段）` and a four-column routing table.
- PASS: all four required stage-link tokens are present in the router and resolve to existing files.
- PASS: both `CB_2tb79r78T38k74M75h8iz4C3` and `25164497` remain visible in the router with the import-to-official mapping warning.
- PASS: Stage 4 article-direction summary remains visible in the router as `人物线`、`城乡主题`、`尊严主题`、`爱情线`、`知识分子困境`、`写法线索`.
- PASS: the router still carries the two book-specific 《人生》 literary-example reminders instead of deferring everything to the generic router.
- PASS: all seven regression sentinels remain visible in the router, each with book-specific meaning preserved.
- PASS: `GIT_MASTER=1 git diff --check -- "路遥/人生/《人生》微信读书提示词.md"` returned no output.
- PASS: untracked-safe whitespace check for `.omo/evidence/task-9-split-weread-prompts-by-stage.md` returned no output.
- PASS: tracked whitespace check for `.omo/notepads/split-weread-prompts-by-stage/learnings.md` returned no output.
- PASS: Markdown LSP diagnostics are unavailable in this workspace, and that limitation is explicitly recorded for all changed `.md` files.

Follow-ups / unresolved risks:

- Non-blocking: the markdown link-resolution script reports repeated PASS lines because the same relative stage links appear more than once in the router. Unique targets were still resolved and recorded once in the table above.
