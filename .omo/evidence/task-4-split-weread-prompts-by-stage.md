# Task 4 Evidence, split-weread-prompts-by-stage

Source snapshot used:

- Immutable snapshot: `/home/king/github/growing-myself/.omo/evidence/split-weread-prompts-by-stage/source/微信读书通用提示词.before.md`
- Move ledger source: `/home/king/github/growing-myself/.omo/evidence/task-1-split-weread-prompts-by-stage.md`
- Stage 2 snapshot ranges used for rewrite: `358-569`, `661-843`
- Required anchor lines re-read from the snapshot: `358`, `366`, `385`, `412`, `425`, `489`, `530`, `661`, `677`, `719`, `747`, `807`, `822`
- Execution note: the live router path `/home/king/github/growing-myself/微信读书通用提示词.md` was treated as target-routing context only. Rewrite content came from the immutable snapshot plus the Task 1 move ledger.

Applicable AGENTS.md:

- `/home/king/github/growing-myself/AGENTS.md`
- Allowed AGENTS-derived additions imported into Stage 2: `五异法扫描`, `问题阶梯（1星-5星）`, `张力地图`, `轻卡/主卡边界`, `细节卡从具体往抽象`, `主题卡从抽象往具体落`, `提问可以跳远，论证不能偷步`, `保留有生命力的句子`, `文本落点`, `另一个角度`, `扩写方向与跨作品联动路径`
- Additional root-AGENTS constraints imported into Stage 2 because they directly govern optimization quality: 保留用户原话、文气后面要有文本落点、文本优先、对轻卡不强行深挖、补充另一个角度、跨作品联动要写明联动路径。
- Not applicable and not imported: any `路遥/人生/**` prompt file, `/home/king/github/growing-myself/路遥/人生/AGENTS.md`, sibling-book AGENTS rules, or live router prose as rewrite source.

Files changed:

- `/home/king/github/growing-myself/微信读书通用提示词-第二阶段-优化中间整理稿.md`
- `/home/king/github/growing-myself/.omo/evidence/task-4-split-weread-prompts-by-stage.md`
- `/home/king/github/growing-myself/.omo/notepads/split-weread-prompts-by-stage/learnings.md` (append-only)

Heading coverage

| source heading | source lines | target coverage |
|---|---:|---|
| `## 8. 文学分析质量规则` | `358-364` | `## 文学分析质量规则` plus the stage-wide highest-principle paragraphs at target lines `39-45` |
| `### 8.1 证据锚点与文本落点` | `366-383` | `### 证据锚点与文本落点` at target lines `47-64` |
| `### 8.2 人物心理要写出过程，不要直接贴标签` | `385-410` | same-title heading at target lines `66-77` |
| `### 8.3 文本歧义与心理雾区不能一笔带过` | `412-423` | same-title heading at target lines `79-90` |
| `### 8.4 完整卡和主卡候选必须打开矛盾` | `425-438` | same-title heading at target lines `92-105` |
| `### 8.5 AI 要提供表达增量` | `440-459` | same-title heading at target lines `107-120` |
| `### 8.6 AI 可以反驳，但必须指出缺失的分析环节` | `461-479` | same-title heading at target lines `122-134` |
| `### 8.7 大胆分析，但不要省掉过程` | `481-487` | same-title heading at target lines `136-142` |
| `### 8.8 升级问题链后必须给出阶段性回答` | `489-528` | same-title heading at target lines `144-173`, plus full answer template at `157-163` |
| `### 8.9 AI修正必须深化，不只是整理语序` | `530-541` | same-title heading at target lines `175-186` |
| `### 8.10 文学表达不是轻卡专属` | `543-557` | same-title heading at target lines `188-202` |
| `### 8.11 分析后命名，而非先命名硬套` | `559-568` | same-title heading at target lines `204-213` |
| `## 10. 第二阶段：优化中间整理稿` | `661-675` | inheritance block at target lines `1-21`, stage title at `23`, and execution prompt block at `25-37` |
| `### 10.1 本轮优化前诊断` | `677-717` | `## 本轮优化前诊断` at target lines `231-258`, plus the self-check moved into `## 第二阶段 QA` at `387-405` |
| `### 10.2 轻卡优化规则` | `719-745` | `## 轻卡优化规则` at target lines `260-286` |
| `### 10.3 完整卡 / 主卡优化规则` | `747-805` | `## 完整卡 / 主卡优化规则` at target lines `288-346` |
| `### 10.4 暂存素材处理规则` | `807-820` | `## 暂存素材处理规则` at target lines `348-363` |
| `### 10.5 同位置其他书友高赞想法差异分析规则` | `822-842` | `## 同位置其他书友高赞想法差异分析规则` at target lines `365-385` |
| `AGENTS 核心分析工具箱 + 卡片边界 + 提问与视角补充规则` | `AGENTS.md:14-24`, `99-102` | `### 项目文学分析工具箱，执行时必须显式使用` at target lines `215-229`, plus complete-card template lines `314-325` and QA lines `401-403` |

Commands run:

- `GIT_MASTER=1 git grep -F --untracked -n "文学分析质量规则" -- "微信读书通用提示词-第二阶段-优化中间整理稿.md"`
- `GIT_MASTER=1 git grep -F --untracked -n "本轮优化前诊断" -- "微信读书通用提示词-第二阶段-优化中间整理稿.md"`
- `GIT_MASTER=1 git grep -F --untracked -n "AI轻评" -- "微信读书通用提示词-第二阶段-优化中间整理稿.md"`
- `GIT_MASTER=1 git grep -F --untracked -n "AI修正" -- "微信读书通用提示词-第二阶段-优化中间整理稿.md"`
- `GIT_MASTER=1 git grep -F --untracked -n "当前回答（沿原问题）" -- "微信读书通用提示词-第二阶段-优化中间整理稿.md"`
- `GIT_MASTER=1 git grep -F --untracked -n "同位置其他书友高赞想法分析" -- "微信读书通用提示词-第二阶段-优化中间整理稿.md"`
- `GIT_MASTER=1 git grep -F --untracked -n "五异法扫描" -- "微信读书通用提示词-第二阶段-优化中间整理稿.md"`
- `GIT_MASTER=1 git grep -F --untracked -n "问题阶梯（1星-5星）" -- "微信读书通用提示词-第二阶段-优化中间整理稿.md"`
- `GIT_MASTER=1 git grep -F --untracked -n "张力地图" -- "微信读书通用提示词-第二阶段-优化中间整理稿.md"`
- `GIT_MASTER=1 git grep -F --untracked -n "轻卡/主卡边界" -- "微信读书通用提示词-第二阶段-优化中间整理稿.md"`
- `GIT_MASTER=1 git grep -F --untracked -n "细节卡从具体往抽象" -- "微信读书通用提示词-第二阶段-优化中间整理稿.md"`
- `GIT_MASTER=1 git grep -F --untracked -n "主题卡从抽象往具体落" -- "微信读书通用提示词-第二阶段-优化中间整理稿.md"`
- `GIT_MASTER=1 git grep -F --untracked -n "提问可以跳远，论证不能偷步" -- "微信读书通用提示词-第二阶段-优化中间整理稿.md"`
- `GIT_MASTER=1 git grep -F --untracked -n "保留有生命力的句子" -- "微信读书通用提示词-第二阶段-优化中间整理稿.md"`
- `GIT_MASTER=1 git grep -F --untracked -n "文本落点" -- "微信读书通用提示词-第二阶段-优化中间整理稿.md"`
- `GIT_MASTER=1 git grep -F --untracked -n "另一个角度" -- "微信读书通用提示词-第二阶段-优化中间整理稿.md"`
- `GIT_MASTER=1 git grep -F --untracked -n "扩写方向与跨作品联动路径" -- "微信读书通用提示词-第二阶段-优化中间整理稿.md"`
- `GIT_MASTER=1 git grep --untracked -E -n '请写入：.*正式阅读笔记|更新到.*正式阅读笔记' -- "微信读书通用提示词-第二阶段-优化中间整理稿.md"`
- `GIT_MASTER=1 git diff --no-index --check /dev/null "微信读书通用提示词-第二阶段-优化中间整理稿.md"`
- `GIT_MASTER=1 git diff --no-index --check /dev/null ".omo/evidence/task-4-split-weread-prompts-by-stage.md"`
- `GIT_MASTER=1 git diff --no-index --check /dev/null ".omo/notepads/split-weread-prompts-by-stage/learnings.md"`
- `lsp_diagnostics("/home/king/github/growing-myself/微信读书通用提示词-第二阶段-优化中间整理稿.md", severity="all")`
- `lsp_diagnostics("/home/king/github/growing-myself/.omo/evidence/task-4-split-weread-prompts-by-stage.md", severity="all")`
- `lsp_diagnostics("/home/king/github/growing-myself/.omo/notepads/split-weread-prompts-by-stage/learnings.md", severity="all")`
- `functions.read("/home/king/github/growing-myself/.omo/evidence/split-weread-prompts-by-stage/source/微信读书通用提示词.before.md", offsets covering Stage 2 source ranges)`
- `functions.read("/home/king/github/growing-myself/AGENTS.md")`
- `functions.read("/home/king/github/growing-myself/.omo/evidence/task-1-split-weread-prompts-by-stage.md")`
- `functions.read("/home/king/github/growing-myself/微信读书通用提示词-第二阶段-优化中间整理稿.md")`

Per-token verification

| token | result | evidence hit |
|---|---|---|
| `文学分析质量规则` | PASS | target lines `39`, `292` |
| `本轮优化前诊断` | PASS | target lines `30`, `231` |
| `AI轻评` | PASS | target line `267` |
| `AI修正` | PASS | target lines `175`, `177`, `184`, `186`, `306`, `343`, `385`, `391` |
| `当前回答（沿原问题）` | PASS | target lines `146`, `160`, `320`, `346`, `396` |
| `同位置其他书友高赞想法分析` | PASS | target lines `327`, `385` |
| `五异法扫描` | PASS | target lines `217`, `401` |
| `问题阶梯（1星-5星）` | PASS | target lines `218`, `401` |
| `张力地图` | PASS | target lines `219`, `401` |
| `轻卡/主卡边界` | PASS | target lines `220`, `401` |
| `细节卡从具体往抽象` | PASS | target line `221` |
| `主题卡从抽象往具体落` | PASS | target line `222` |
| `提问可以跳远，论证不能偷步` | PASS | target line `223`, full combined phrase present as one literal, not split substrings |
| `保留有生命力的句子` | PASS | target lines `224`, `402` |
| `文本落点` | PASS | target lines `47`, `62`, `225`, `281`, `337`, `402` |
| `另一个角度` | PASS | target lines `226`, `316`, `403` |
| `扩写方向与跨作品联动路径` | PASS | target lines `227`, `325`, `403` |

Exact-source-rule preservation samples

1. Snapshot `381-383`: `完整卡、主卡候选和正式阅读笔记中的核心卡，必须至少绑定一个可回到原文的证据锚点...文学作品侧重词语、动作、人物心理和叙事结构；非虚构作品侧重概念、论证、证据、结构、修辞和隐含前提。` -> preserved at target lines `62-64`, including the generic cross-genre caveat.
2. Snapshot `491-498`: `AI 必须继续补“当前回答（沿原问题）”“当前回答（新增角度）”和必要的“后文待回看”。` -> preserved at target lines `146-163`, then repeated in the complete-card template at `318-322`.
3. Snapshot `667-674`: `不要覆盖我的原想法，所有 AI 优化都写在原想法下方。...不要改写正式阅读笔记。` -> preserved twice, once in the inheritance block at target lines `14-16`, once in the execution block at `29-36`.
4. Root `AGENTS.md:100-102`: `提问可以跳远，论证不能偷步` and the requirement to补一个视角、写明联动路径 -> preserved at target lines `223`, `226-227`, and complete-card fields `316-325`.

Read-based QA notes:

- Read-based structure QA: the file begins with an inheritance block, and that block contains the router path, stage purpose, required pre-read files, exact input/output, router-wins conflict rule, task boundary, Must NOT list, and QA evidence path.
- Read-based boundary QA: the prompt only authorizes updating `{中间稿路径}`. It explicitly forbids writing or generating any formal reading note file, and it does not instruct Stage 3 migration or Stage 4 consolidation.
- Read-based preservation QA: the execution block and Must NOT list both preserve the core Stage 2 rule that original user thoughts remain in place and all AI material is written below them.
- Read-based semantic QA: the quality section keeps evidence anchors, psychology-process analysis, ambiguity handling, contradiction opening, AI expression increment, rebuttal-with-missing-step, question-chain plus current-answer, AI修正 deepening, and naming-after-analysis as separate controllable rules, not as flattened summaries.
- Read-based AGENTS QA: the Stage 2 prompt imports the root AGENTS toolbox as an explicit required tool section, not as vague inspiration. The full combined phrase `提问可以跳远，论证不能偷步` appears as one literal line.
- Read-based cross-genre QA: the prompt stays generic. It preserves both halves of the caveat, literary works emphasize words, actions, psychology, and narrative structure; non-fiction emphasizes concepts, argument, evidence, structure, rhetoric, and implicit premises.
- Read-based card-boundary QA: light cards keep `AI轻评` and `AI优化表达` only, while complete/main cards must carry `AI评价`, `AI修正`, `可入笔记的文学表达`, question chains, current answers, and optional external-reader analysis.
- Positive dry-run scenario: opening this file in a new session with an existing `{中间稿路径}` leads to a Stage 2-only flow, diagnose first, then optimize light cards, complete/main cards, pending material, and external-reader differences, all inside the intermediate draft.
- Boundary dry-run scenario: if the operator tries to use this prompt to push content into a formal reading note, the inheritance block and prompt body refuse that boundary, and the failure grep below confirms there is no `请写入：...正式阅读笔记` or `更新到...正式阅读笔记` execution wording.

Boundary checks:

- No rewrite of `/home/king/github/growing-myself/微信读书通用提示词.md`.
- No creation or edit of Stage 1, Stage 3, or Stage 4 files.
- No touch to any `路遥/人生/**` path.
- No write to any formal reading note or live intermediate draft during this task. Only the Stage 2 prompt, this evidence file, and the append-only notepad entry are changed.
- No edit to `.omo/run-continuation/*.json`.
- No commit, stage, push, or destructive Git command.
- No contamination from 《人生》 names, bookIds, sample IDs, or sibling-book rules.

Failure grep result

- Command: `GIT_MASTER=1 git grep --untracked -E -n '请写入：.*正式阅读笔记|更新到.*正式阅读笔记' -- "微信读书通用提示词-第二阶段-优化中间整理稿.md"`
- Output: no matches
- Classification: PASS, no Stage 3 execution instruction leaked into the Stage 2 prompt.

Follow-ups / unresolved risks:

- Non-blocking: Stage 7 generic hard QA will still need to verify this file in cross-file context with the router and the other stage prompts when they exist.
- Non-blocking: the repo started dirty and contains many unrelated untracked files. This task stayed within the allowed file list.
- Non-blocking: Markdown LSP diagnostics were attempted on all three changed `.md` files, but this workspace has no `.md` LSP server configured, so there is no language-server error surface to report.

PASS:

- PASS: Stage 2 prompt was created from the immutable generic snapshot plus the Task 1 move ledger, with root `AGENTS.md` explicitly recorded as the only allowed extra source.
- PASS: the new file starts with the required inheritance block and keeps the router-wins conflict rule.
- PASS: the prompt preserves original user thoughts, writes AI material below them, and does not instruct any formal-note write.
- PASS: all required Stage 2 tokens are present, including the full combined phrase `提问可以跳远，论证不能偷步`.
- PASS: the AGENTS literary-analysis toolbox is present as explicit execution guidance, not as a generic aside.
- PASS: the generic cross-genre caveat is preserved, so the rules are not novel-only.
- PASS: final untracked-safe whitespace checks on the Stage 2 prompt, this evidence file, and the append-only learnings file all returned no output.
- PASS: the forbidden Stage 3 execution grep returned no matches.
