# Task 11 Evidence, split-weread-prompts-by-stage

Source snapshot used:

- Immutable snapshot: `/home/king/github/growing-myself/.omo/evidence/split-weread-prompts-by-stage/source/《人生》微信读书提示词.before.md`
- Scope ranges used for drafting: `328-537` and `637-822`
- Preservation ledger: `/home/king/github/growing-myself/.omo/evidence/task-8-split-weread-prompts-by-stage.md`
- Precondition confirmed from Task 8 ledger before writing: `SNAPSHOT_VERBATIM_BEFORE_REWRITE: PASS`
- Allowed extra source material by plan: `/home/king/github/growing-myself/AGENTS.md`, only for the project literary-analysis toolbox inherited into Stage 2.

Applicable AGENTS.md:

- Required root rule file: `/home/king/github/growing-myself/AGENTS.md`
- Execution-time conditional same-book rule file: `/home/king/github/growing-myself/路遥/人生/AGENTS.md` only if it exists when Stage 2 is executed.
- Task 8 preservation fact retained: the same-book `AGENTS.md` was absent when the immutable snapshot and ledger were created, so no same-book rules were invented here.
- Explicitly not imported: sibling-book `AGENTS.md` files.

Files changed:

- `/home/king/github/growing-myself/路遥/人生/《人生》微信读书提示词-第二阶段-优化中间整理稿.md`
- `/home/king/github/growing-myself/.omo/evidence/task-11-split-weread-prompts-by-stage.md`
- `/home/king/github/growing-myself/.omo/notepads/split-weread-prompts-by-stage/learnings.md` (append-only, one new line)

Commands run:

- `functions.read` on `/home/king/github/growing-myself/AGENTS.md`
- `functions.read` on `/home/king/github/growing-myself/.omo/evidence/task-8-split-weread-prompts-by-stage.md`
- `functions.read` on `/home/king/github/growing-myself/.omo/notepads/split-weread-prompts-by-stage/learnings.md`
- `functions.read` on `/home/king/github/growing-myself/.omo/notepads/split-weread-prompts-by-stage/problems.md`
- `functions.read` on `/home/king/github/growing-myself/.omo/notepads/split-weread-prompts-by-stage/issues.md`
- `functions.read` on `/home/king/github/growing-myself/.omo/notepads/split-weread-prompts-by-stage/decisions.md`
- `functions.read` on `/home/king/github/growing-myself/.omo/evidence/split-weread-prompts-by-stage/source/《人生》微信读书提示词.before.md` with ranges `328-537` and `637-822`
- `functions.read` on `/home/king/github/growing-myself/.omo/plans/split-weread-prompts-by-stage.md` range `243-262`
- `functions.read` on `/home/king/github/growing-myself/路遥/人生/《人生》微信读书提示词-第二阶段-优化中间整理稿.md`
- `functions.apply_patch` to add `/home/king/github/growing-myself/路遥/人生/《人生》微信读书提示词-第二阶段-优化中间整理稿.md`
- `functions.apply_patch` to add this evidence file and append one line to `learnings.md`
- `GIT_MASTER=1 git grep -F --untracked -n "高加林" -- "路遥/人生/《人生》微信读书提示词-第二阶段-优化中间整理稿.md"`
- `GIT_MASTER=1 git grep -F --untracked -n "巧珍" -- "路遥/人生/《人生》微信读书提示词-第二阶段-优化中间整理稿.md"`
- `GIT_MASTER=1 git grep -F --untracked -n "强烈" -- "路遥/人生/《人生》微信读书提示词-第二阶段-优化中间整理稿.md"`
- `GIT_MASTER=1 git grep -F --untracked -n "不知为什么" -- "路遥/人生/《人生》微信读书提示词-第二阶段-优化中间整理稿.md"`
- `GIT_MASTER=1 git grep -F --untracked -n "本轮优化前诊断" -- "路遥/人生/《人生》微信读书提示词-第二阶段-优化中间整理稿.md"`
- `GIT_MASTER=1 git grep -F --untracked -n "AI轻评" -- "路遥/人生/《人生》微信读书提示词-第二阶段-优化中间整理稿.md"`
- `GIT_MASTER=1 git grep -F --untracked -n "AI修正" -- "路遥/人生/《人生》微信读书提示词-第二阶段-优化中间整理稿.md"`
- `GIT_MASTER=1 git grep -F --untracked -n "当前回答（沿原问题）" -- "路遥/人生/《人生》微信读书提示词-第二阶段-优化中间整理稿.md"`
- `GIT_MASTER=1 git grep -F --untracked -n "外部读者高赞想法分析" -- "路遥/人生/《人生》微信读书提示词-第二阶段-优化中间整理稿.md"`
- `GIT_MASTER=1 git grep -F --untracked -n "五异法扫描" -- "路遥/人生/《人生》微信读书提示词-第二阶段-优化中间整理稿.md"`
- `GIT_MASTER=1 git grep -F --untracked -n "问题阶梯（1星-5星）" -- "路遥/人生/《人生》微信读书提示词-第二阶段-优化中间整理稿.md"`
- `GIT_MASTER=1 git grep -F --untracked -n "张力地图" -- "路遥/人生/《人生》微信读书提示词-第二阶段-优化中间整理稿.md"`
- `GIT_MASTER=1 git grep -F --untracked -n "轻卡/主卡边界" -- "路遥/人生/《人生》微信读书提示词-第二阶段-优化中间整理稿.md"`
- `GIT_MASTER=1 git grep -F --untracked -n "细节卡从具体往抽象" -- "路遥/人生/《人生》微信读书提示词-第二阶段-优化中间整理稿.md"`
- `GIT_MASTER=1 git grep -F --untracked -n "主题卡从抽象往具体落" -- "路遥/人生/《人生》微信读书提示词-第二阶段-优化中间整理稿.md"`
- `GIT_MASTER=1 git grep -F --untracked -n "提问可以跳远，论证不能偷步" -- "路遥/人生/《人生》微信读书提示词-第二阶段-优化中间整理稿.md"`
- `GIT_MASTER=1 git grep -F --untracked -n "保留有生命力的句子" -- "路遥/人生/《人生》微信读书提示词-第二阶段-优化中间整理稿.md"`
- `GIT_MASTER=1 git grep -F --untracked -n "文本落点" -- "路遥/人生/《人生》微信读书提示词-第二阶段-优化中间整理稿.md"`
- `GIT_MASTER=1 git grep -F --untracked -n "另一个角度" -- "路遥/人生/《人生》微信读书提示词-第二阶段-优化中间整理稿.md"`
- `GIT_MASTER=1 git grep -F --untracked -n "扩写方向与跨作品联动路径" -- "路遥/人生/《人生》微信读书提示词-第二阶段-优化中间整理稿.md"`
- `GIT_MASTER=1 git grep --untracked -E -n "请把 .* 正式阅读笔记|更新到 /home/king/github/growing-myself/路遥/人生/《人生》阅读笔记.md" -- "路遥/人生/《人生》微信读书提示词-第二阶段-优化中间整理稿.md"`
- `GIT_MASTER=1 git diff --no-index --check /dev/null "路遥/人生/《人生》微信读书提示词-第二阶段-优化中间整理稿.md"`
- `lsp_diagnostics` on `/home/king/github/growing-myself/路遥/人生/《人生》微信读书提示词-第二阶段-优化中间整理稿.md`
- `lsp_diagnostics` on `/home/king/github/growing-myself/.omo/evidence/task-11-split-weread-prompts-by-stage.md`
- `lsp_diagnostics` on `/home/king/github/growing-myself/.omo/notepads/split-weread-prompts-by-stage/learnings.md`
- `GIT_MASTER=1 git diff --no-index --check /dev/null ".omo/evidence/task-11-split-weread-prompts-by-stage.md"`
- `GIT_MASTER=1 git diff --check -- ".omo/notepads/split-weread-prompts-by-stage/learnings.md"`

Heading coverage:

| target area | stage file lines | coverage note | status |
|---|---:|---|---|
| Inheritance block | `1-24` | Begins the file and contains router path, stage purpose, required pre-reads, exact input/output files, conflict rule, task boundary, Must NOT list, and QA evidence path. | PASS |
| Root AGENTS toolbox block | `43-57` | Includes all required toolbox phrases, with execution-facing usage notes. | PASS |
| Literary-analysis quality rules | `59-265` | Carries Stage 2 depth rules, evidence anchoring, psychology process, tension opening, current-answer structure, AI修正 deepening, and naming-after-analysis rule. | PASS |
| 本轮优化前诊断 | `267-307` | Preserves diagnosis template, batching advice, and 10-point self-check. | PASS |
| Light-card rules | `309-335` | Preserves `AI轻评` structure and anti-overexpansion boundary. | PASS |
| Complete / main-card rules | `337-399` | Preserves `AI评价` / `AI修正` / `AI补充` / current-answer structure and external-reader analysis slot. | PASS |
| Pending-material rules | `401-416` | Preserves non-forcing future-destination treatment for 暂存素材. | PASS |
| External-reader high-like idea analysis | `418-438` | Preserves five-way classification plus anti-replacement boundary. | PASS |
| Stage 2 QA | `440-451` | Preserves book-specific example retention, formal-note prohibition, and toolbox coverage check. | PASS |

Exact-source-rule preservation samples:

1. Snapshot `374-376` kept at stage lines `103-107`: the 高加林 / 巧珍心理过程例子 survives as a book-specific middle-layer example, not as a generic slogan.
2. Snapshot `391-393` kept at stage lines `120-122`: the `强烈 / 最好 / 不知为什么 / 老半天 / 不怕我不要你了吗` 心理雾区例子 survives with the why-this-word-matters rule attached.
3. Snapshot `643-650` kept at stage lines `34-41`: keep original thoughts unchanged, write AI material below, classify cards first, and do not touch the formal note.
4. Snapshot `701-721` kept at stage lines `315-335`: `AI轻评` + `AI优化表达` survive together with the explicit “do not force full problem-chain / cross-work expansion” rule.
5. Snapshot `731-785` kept at stage lines `345-399`: `AI评价` / `AI修正` / `可入笔记的文学表达` / `AI补充` survive together with `当前回答（沿原问题）` and `另一个角度`.

Read-based QA notes:

- Stage 2 begins with the inheritance block, not with a generic title page. The boundary information is visible before any execution prose starts.
- The stage prompt keeps the execution target fixed to `/home/king/github/growing-myself/路遥/人生/《人生》中间整理稿.md` and names `/home/king/github/growing-myself/路遥/人生/《人生》阅读笔记.md` only as a forbidden output.
- The prompt preserves the two 《人生》-specific literary examples in analysis sections and again in the QA section, which makes accidental generic flattening harder.
- Root `AGENTS.md` toolbox items are not scattered as loose nouns only. They are gathered into an explicit toolbox block and echoed in the QA checklist.
- The stage prompt tells the executor to keep my original thoughts unchanged and place all AI material below them. This is stated in the inheritance block, the execution boundary list, and the QA section.
- Light-card handling still protects lightness. Complete-card handling still forces text anchoring, psychological process, tension, and staged answers. 暂存素材 still remains a future-destination area, not a forced analysis dump.
- `lsp_diagnostics` was run on all three modified Markdown files. This workspace has no Markdown LSP server configured, so the diagnostics tool returned a tooling-availability notice rather than file errors. Read-based QA and whitespace checks therefore carry the correctness load for this Markdown-only task.

Positive dry-run:

- Light-card dry-run: if a card is only a气氛触动句, the prompt routes it into `AI轻评` plus `AI优化表达`, requires a short 文本落点, keeps one有生命力的句子, and explicitly says not to force full problem chains or跨作品联动.
- Complete-card dry-run: if a card already contains a multi-branch question, the prompt routes it into `AI评价` / `AI修正` / `可入笔记的文学表达` / `AI补充`, then requires `问题链升级（沿原问题）`, `另一条升级问题链（新增角度）`, `当前回答（沿原问题）`, `当前回答（新增角度）`, and `后文待回看`.
- External-reader dry-run: if the intermediate draft already carries same-position high-like ideas, the prompt classifies them as 回声 / 补充 / 挑战 / 反向解释 / 独立精彩, while keeping them subordinate to my original thought and the AI sections.

Boundary/failure dry-run:

- Formal-note failure dry-run: if an executor tries to turn Stage 2 into a migration step, the inheritance block and Stage 2 QA both stop it by naming the formal note path as forbidden output. The failure grep below returned no Stage 3 execution instruction.
- Generic-flattening failure dry-run: if an executor tries to replace 《人生》-specific psychology with abstract labels, the prompt still forces the 高加林 / 巧珍 example and the `强烈 / 最好 / 不知为什么 / 老半天 / 不怕我不要你了吗` example to remain visible.
- Light-card over-expansion failure dry-run: if an executor starts forcing every light card into a full card, the light-card rule block explicitly says not to force complete question chains, staged answers, or cross-work linkage there.

Literal preservation verification:

| token | representative stage line(s) | verification note | status |
|---|---:|---|---|
| `高加林` | `107, 120, 449` | Book-specific psychology example and QA sentinel retained. | PASS |
| `巧珍` | `98, 104, 107, 120, 449` | Book-specific psychology example retained in both rule body and QA. | PASS |
| `强烈` | `120, 449` | Psychological fog example retained in body and QA. | PASS |
| `不知为什么` | `111, 120, 394, 449` | Ambiguity rule and example both retained. | PASS |
| `本轮优化前诊断` | `35, 267, 446` | Execution gate, section heading, and QA check all present. | PASS |
| `AI轻评` | `316` | Light-card structure retained verbatim. | PASS |
| `AI修正` | `229, 231, 238, 298, 355, 395, 438` | Deepening rule, diagnosis check, template slot, and anti-replacement rule all present. | PASS |
| `当前回答（沿原问题）` | `190, 204, 222, 303, 369, 398` | Stage-answer structure survives in rule, self-check, and template. | PASS |
| `外部读者高赞想法分析` | `40, 376, 418, 438` | Boundary rule, template slot, dedicated rule section, and anti-replacement clause all present. | PASS |
| `五异法扫描` | `47, 448` | Toolbox and QA echo present. | PASS |
| `问题阶梯（1星-5星）` | `48, 448` | Toolbox and QA echo present. | PASS |
| `张力地图` | `49, 448` | Toolbox and QA echo present. | PASS |
| `轻卡/主卡边界` | `50, 448` | Toolbox and QA echo present. | PASS |
| `细节卡从具体往抽象` | `51, 448` | Toolbox and QA echo present. | PASS |
| `主题卡从抽象往具体落` | `52, 448` | Toolbox and QA echo present. | PASS |
| `提问可以跳远，论证不能偷步` | `53, 448` | Full combined AGENTS phrase retained verbatim. | PASS |
| `保留有生命力的句子` | `54, 448` | Toolbox and QA echo present. | PASS |
| `文本落点` | `55, 65, 80, 330, 389, 448` | Toolbox term, section heading, and execution requirements all present. | PASS |
| `另一个角度` | `56, 155, 365, 448` | Toolbox term, expression-increment rule, and template slot all present. | PASS |
| `扩写方向与跨作品联动路径` | `57, 399, 448` | Toolbox term and complete-card requirement both present. | PASS |

Combined AGENTS phrase verification:

| exact phrase | representative stage line(s) | anti-false-pass note | status |
|---|---:|---|---|
| `提问可以跳远，论证不能偷步` | `53, 448` | Verified as the full combined phrase, not as separated substring fragments. | PASS |

Boundary checks:

- This task did not rewrite `/home/king/github/growing-myself/路遥/人生/《人生》微信读书提示词.md`.
- This task did not create or edit Stage 1, Stage 3, or Stage 4 prompt files.
- This task did not edit generic prompt files.
- This task did not edit `/home/king/github/growing-myself/路遥/人生/《人生》中间整理稿.md` or `/home/king/github/growing-myself/路遥/人生/《人生》阅读笔记.md`.
- The stage prompt explicitly forbids writing to the formal-note path and keeps all execution inside Stage 2.
- Target wording avoids stale copied snapshot subsection numbers. The prompt uses descriptive headings instead of stale numeric cross-references.
- Failure grep for `请把 .* 正式阅读笔记|更新到 /home/king/github/growing-myself/路遥/人生/《人生》阅读笔记.md` returned no output, so no Stage 3 execution instruction leaked into Stage 2.

Whitespace checks:

| target | command style | result | status |
|---|---|---|---|
| stage file `路遥/人生/《人生》微信读书提示词-第二阶段-优化中间整理稿.md` | `git diff --no-index --check /dev/null` | no output | PASS |
| evidence file `.omo/evidence/task-11-split-weread-prompts-by-stage.md` | `git diff --no-index --check /dev/null` | no output | PASS |
| append-only notepad `.omo/notepads/split-weread-prompts-by-stage/learnings.md` | tracked `git diff --check --` | no output | PASS |

PASS:

- PASS: Task 8 precondition was checked before writing, and `SNAPSHOT_VERBATIM_BEFORE_REWRITE: PASS` is explicitly recorded as the gating source fact.
- PASS: the Stage 2 prompt begins with the required inheritance block and keeps the fixed intermediate path, required pre-reads, exact input/output files, conflict rule, task boundary, Must NOT list, and QA evidence path.
- PASS: read-based semantic QA confirms Stage 2 keeps my original thoughts unchanged, writes AI material below them, preserves book-specific examples, carries the root AGENTS toolbox, and forbids formal-note writes.
- PASS: all required literal tokens, including the full combined phrase `提问可以跳远，论证不能偷步`, are present with one PASS row each.
- PASS: failure grep for forbidden Stage 3 execution wording returned no output.
- PASS: untracked-safe whitespace checks passed for the stage file and evidence file, and the append-only notepad diff check is clean.
- PASS: `lsp_diagnostics` was invoked on all modified files. No Markdown LSP server is configured in this workspace, so there are no LSP error rows to clear, but the invocation result is recorded honestly.

Follow-ups / unresolved risks:

- Non-blocking: the repo may still contain unrelated dirty files outside this task. This task stayed inside the approved write set.
- Non-blocking: Task 14 should still rerun hard QA against this Stage 2 prompt, especially because several required literals also appear in the QA section by design.
