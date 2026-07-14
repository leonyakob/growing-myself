---
slug: split-weread-prompts-by-stage
status: awaiting-approval
intent: clear
review_required: false
pending-action: await user approval of reviewed plan; execution requires later explicit start-work authorization
approach: one total plan with two sequential waves; split generic WeRead prompt first, pass hard QA, then split 《人生》 prompt with the same router/stage architecture
---

# Draft: split-weread-prompts-by-stage

## Components (topology ledger)

| id | outcome | status | evidence path |
|---|---|---|---|
| C1 | 通用微信读书提示词由一个总入口和四个阶段执行工单组成；总入口保留权威规则和路由，阶段文件承接具体执行。 | active | `.omo/evidence/task-1-split-weread-prompts-by-stage.md` |
| C2 | 通用拆分必须先独立通过 QA，确认路由、继承、阶段边界和链接完整后，才允许进入《人生》拆分。 | active | `.omo/evidence/task-7-split-weread-prompts-by-stage.md` |
| C3 | 《人生》微信读书提示词按同一结构拆分，但保留固定路径、双 bookId、主题方向和 7 个回归风险样本。 | active | `.omo/evidence/task-8-split-weread-prompts-by-stage.md`; `.omo/evidence/task-14-split-weread-prompts-by-stage.md` |
| C4 | 最终只产出提示词拆分和 QA 证据，不整理微信读书材料、不改中间稿、不改正式阅读笔记。 | active | `.omo/evidence/final-review-split-weread-prompts-by-stage.md` |

## Open assumptions (announced defaults)

| assumption | adopted default | rationale | reversible? |
|---|---|---|---|
| 阶段文件命名 | 采用原总文件名 + `-第一阶段-生成中间整理稿.md` 等后缀；不新建深层目录。 | 文件仍在原位置附近，便于用户手动找到；不改变书目目录结构。 | yes |
| 总入口长度 | 总入口保留跨阶段权威规则、路由、冲突处理和阶段链接；不强求压成极短索引。 | 总提示词被用户定位为“权威规则 / 路由器”，不能为了短而丢规则。 | yes |
| 阶段提示词自足程度 | 每个阶段提示词必须可作为新 session 启动器，但开头明确要求先读总入口；冲突时总入口优先。 | 兼顾可执行性与单一权威来源，避免阶段文件互相漂移。 | yes |
| 通用与《人生》的执行顺序 | Wave 1 先拆通用，硬 QA 后 Wave 2 再拆《人生》。 | 用户已确认该顺序；《人生》应继承通用拆分经验，避免两边同时错。 | no |
| 审查要求 | 已按用户后续要求启动 Momus / Metis / Oracle 高精审查；所有 CHANGES_REQUIRED 必须吸收或由用户显式豁免后，才能把 plan 交给执行 session。 | 用户明确要求“派mous/metis/oracle仔细审核这个计划，查漏补缺完善这个计划”。 | no |

## Findings (cited - path:lines)

- `微信读书通用提示词.md:1` 到 `微信读书通用提示词.md:13` 定义了通用提示词用途、核心目标、正式稿证据层和技术字段边界。
- `微信读书通用提示词.md:29` 到 `微信读书通用提示词.md:40` 已有不可降级原则、任务入口门、计划审查和只读咨询边界，必须保留在总入口中。
- `微信读书通用提示词.md:69` 到 `微信读书通用提示词.md:93` 已形成四阶段总流程，是拆分为四个阶段工单的主轴。
- `微信读书通用提示词.md:122` 到 `微信读书通用提示词.md:153` 规定阶段切换 QA 与条件式 Git 检查点，属于总入口与阶段文件都必须引用的跨阶段门。
- `微信读书通用提示词.md:157` 到 `微信读书通用提示词.md:300` 是第一阶段数据抓取、合并、同位置高赞想法和外部读者边界的重规则，应迁入第一阶段文件，同时在总入口保留摘要和链接。
- `微信读书通用提示词.md:358` 到 `微信读书通用提示词.md:569` 是第二阶段文学分析质量规则，必须保留为第二阶段的核心质量门。
- `微信读书通用提示词.md:572` 到 `微信读书通用提示词.md:844` 是第一、第二阶段具体执行模板，可拆入对应阶段文件。
- `微信读书通用提示词.md:846` 到 `微信读书通用提示词.md:974` 是第三阶段迁移、回源预检和防回归 QA，必须拆入第三阶段文件。
- `微信读书通用提示词.md:977` 到 `微信读书通用提示词.md:1106` 是第四阶段全书收束模型，必须拆入第四阶段文件，并继续引用 fixture。
- `微信读书通用提示词.md:1109` 到 `微信读书通用提示词.md:1236` 是大任务、辅助模板和专用提示词回归样本机制；总入口保留机制，辅助模板可保留在总入口或按阶段链接。
- `路遥/人生/《人生》微信读书提示词.md:1` 到 `路遥/人生/《人生》微信读书提示词.md:19` 固定了《人生》用途、路径和核心目标。
- `路遥/人生/《人生》微信读书提示词.md:213` 到 `路遥/人生/《人生》微信读书提示词.md:219` 固定《人生》个人导入版 bookId 与官方公开版 bookId 的关系，不能在拆分中丢失。
- `路遥/人生/《人生》微信读书提示词.md:540` 到 `路遥/人生/《人生》微信读书提示词.md:633` 是《人生》第一阶段执行模板。
- `路遥/人生/《人生》微信读书提示词.md:637` 到 `路遥/人生/《人生》微信读书提示词.md:822` 是《人生》第二阶段执行模板。
- `路遥/人生/《人生》微信读书提示词.md:825` 到 `路遥/人生/《人生》微信读书提示词.md:954` 是《人生》第三阶段迁移与防回归 QA。
- `路遥/人生/《人生》微信读书提示词.md:957` 到 `路遥/人生/《人生》微信读书提示词.md:1156` 是《人生》第四阶段全书收束整合规则。
- `路遥/人生/《人生》微信读书提示词.md:1259` 到 `路遥/人生/《人生》微信读书提示词.md:1269` 是《人生》7 个已知回归风险样本，必须保留在《人生》总入口并被阶段文件引用。

## Read-only research reconciliation

- `bg_f8f975d5` completed and confirmed the load-bearing split map: router keeps shared/public rules; stage files carry stage execution; 《人生》 router must retain fixed paths, both bookIds, book-tuned examples, article-direction table and 7 regression samples; stale-reference QA must target `第 X 节` / `§X` references.
- `bg_dfc7e6c4` aborted with no usable findings. The plan compensates by turning the successful split-constraint map into explicit hard QA gates and by requiring final cross-reference, prompt-surface, fixture and regression checks before completion.

## High-accuracy review receipts

- Requested by user: Momus / Metis / Oracle careful review and plan improvement.
- Momus receipt: `bg_fb958701` / `ses_0a0be802effevLZG8UMPoOoCT1` returned `REJECT`; blocking findings were untracked-file unsafe `git grep` / `git diff --check` checks and vague read-based QA invocations.
- Oracle receipt: `bg_bfb8cf70` / `ses_0a0bd9832ffeveDCOv3ovv2Orh` returned `CHANGES_REQUIRED`; key findings were immutable source snapshots, untracked-file-safe checks, per-token PASS rows, decimal section-reference detection, generic prompt-generation architecture update, Chinese hard-constraint preservation, shortcut-template assignment, stronger prompt-surface QA, AGENTS inheritance, run-continuation baseline, and draft metadata drift.
- Metis receipt: `bg_549675b7` / `ses_0a0be0c42ffe6tD8gDjhyQE1rO` returned `CHANGES_REQUIRED`; key findings were mutable source line drift, approval/execution gate ambiguity, same-book vs sibling `AGENTS.md`, literary-analysis toolbox preservation, target-file discoverability, Markdown link validation, structured evidence schema, run-continuation baseline, grep-only false success, generic/《人生》 contamination, non-fiction caveat, and stale draft state.
- First-round fix summary: amended `.omo/plans/split-weread-prompts-by-stage.md` with critical preflight gates, immutable source snapshots, applicable `AGENTS.md` handling, Chinese hard-constraint ledger, untracked-file-safe verification, per-token PASS rows, structured evidence schema, router stage-selection table, Markdown link/code-fence validation, source snapshot dependencies, prompt-surface dry-run QA, contamination checks, run-continuation baseline, and AGENTS-aware commit guard.
- Second-round Momus receipt: `bg_52c4527c` / `ses_0a0af9914ffe6wbsKNkmiGksb8` returned `REJECT`; blockers were remaining default-regex numeric section checks and literal-token checks that still used alternation / escaped `+` semantics.
- Second-round Oracle receipt: `bg_9998fff3` / `ses_0a0af1498ffehIBXUvuU4B3XXW` returned `CHANGES_REQUIRED`; blockers were decimal section-reference false-pass risk and final QA contradictions around immutable source snapshots / fixture schema / allowed changed files.
- Second-round Metis receipt: `bg_a6d2386d` / `ses_0a0aea4ebffe4R1xTrrbDBfsFs` returned `CHANGES_REQUIRED`; blockers were residual live-source references in downstream todos, stale numeric-section BRE usage, source snapshot scope inconsistency, narrow hard-constraint token coverage, and non-snapshot-derived heading coverage.
- Second-round fix summary: converted downstream todo references to immutable snapshot paths, expanded hard-constraint preservation triggers, made heading coverage snapshot-derived, whitelisted immutable source snapshots in final scope and commit strategy, exempted snapshots / fixtures from structured evidence schema, changed numeric-section checks to explicit `git grep --untracked -E -n '第[[:space:]]*[0-9]+(\.[0-9]+)?[[:space:]]*节|§[0-9]+(\.[0-9]+)?'`, and replaced remaining alternation-based literal checks with per-token `git grep -F --untracked -n` or explicit `-E` regex checks.
- Third-round Momus receipt: `bg_56a64e82` / `ses_0a07d2374ffeKXyEHVKufwmLqb` returned `APPROVE`.
- Third-round Oracle receipt: `bg_1c0b14b5` / `ses_0a07d1be3ffe3cI1B0XREjk6R2` returned `CHANGES_REQUIRED`; blocker was final Git hygiene using an absolute allowlist despite a dirty worktree / run-continuation baseline.
- Third-round Metis receipt: `bg_38c3f0c6` / `ses_0a07d1fbbffe9sfEFezX1ogxW4` returned `CHANGES_REQUIRED`; blockers were untracked-file blindness in status checks, missing pre-rewrite verbatim snapshot proof, Stage 2 AGENTS literary toolbox not hard-gated, and F1 reading evidence too broadly.
- Third-round fix summary: changed all final allowlist/baseline status checks to `GIT_MASTER=1 git status --short --untracked-files=all`, made F5 compare against execution-start full and continuation baselines, added pre-rewrite `sha256sum` / `wc -l` / `cmp -s` snapshot proof with `SNAPSHOT_VERBATIM_BEFORE_REWRITE: PASS`, hard-gated Stage 2 AGENTS toolbox tokens in generic and 《人生》 Stage 2 acceptance criteria, and narrowed F1 to this plan's task/final evidence files only.
- Fourth-round Momus receipt: `bg_2d3b907b` / `ses_0a06d640affeioZOLLqybvmG08` returned `OKAY` with no blocker.
- Fourth-round Oracle receipt: `bg_cd73667f` / retry `ses_0a06c60bcffeSnl1YK3NSKOSqp` returned `CHANGES_REQUIRED`; blockers were generic vs 《人生》 AGENTS scope ambiguity, baseline capture timing / continuation content integrity, and F5 continuation comparison relying on status only.
- Fourth-round Metis receipt: `bg_69638c06` / `ses_0a06d601fffexgjjs2gZh4rM9d` completed without a usable assistant verdict; treat as incomplete, not approval.
- Fourth-round fix summary: clarified that generic prompts read root `AGENTS.md` only while 《人生》 prompts may additionally read same-book `路遥/人生/AGENTS.md`; moved baseline capture before any snapshots/evidence/stage/router writes; added `.omo/evidence/split-weread-prompts-by-stage/run-continuation.before.sha256` creation and final `cmp -s` manifest comparison; added the manifest to F1 schema exemptions and F5 allowed outputs.
- Fifth-round Momus receipt: `bg_dad5c55b` / `ses_0a05f004cffesHx8UcKTkCAy0F` returned `APPROVE`.
- Fifth-round Oracle receipt: `bg_15d128d1` / `ses_0a05edc31ffeHyxJoXHbyXWUdH` returned `CHANGES_REQUIRED`; blocker was final verification being written as a parallel gate instead of F2-F5 serial merge followed by F1 aggregation.
- Fifth-round Metis receipt: `bg_06129329` / `ses_0a05ee03effe6FHPEnPt79F2P2` returned `CHANGES_REQUIRED`; blockers were lack of protected-baseline hashing for already dirty/untracked non-output files and Stage 2 AGENTS toolbox tokens still too coarse.
- Fifth-round fix summary: converted final verification into a two-step gate where F2-F5 may investigate in parallel but must be serially merged into named final-review sections before F1 runs last; added `.omo/evidence/split-weread-prompts-by-stage/protected-baseline.before.sha256`, protected path list evidence, and final `cmp -s` comparison; expanded generic and 《人生》 Stage 2 AGENTS hard-gate tokens to full load-bearing phrases such as `问题阶梯（1星-5星）`, `轻卡/主卡边界`, `细节卡从具体往抽象`, `主题卡从抽象往具体落`, `文本落点`, `另一个角度`, and `扩写方向与跨作品联动路径`.
- Sixth-round Momus receipt: `bg_36f9a086` / `ses_0a053adccffeyqD2TAxf3iYMwz` completed without a usable assistant verdict; treat as incomplete, not approval.
- Sixth-round Oracle receipt: `bg_d21b903b` / `ses_0a053a4f2ffe2e6asIm1nmpIHX` returned `APPROVE`.
- Sixth-round Metis receipt: `bg_022698c9` / `ses_0a053a964ffeOp88fi1dr9HON7` returned `CHANGES_REQUIRED`; blockers were contradictory empty run-continuation manifest handling, protected-baseline false-green risk from incomplete recorded path lists, and Stage 2 splitting the `提问可以跳远，论证不能偷步` rule into loose substrings.
- Sixth-round fix summary: made `.omo/evidence/split-weread-prompts-by-stage/run-continuation.before.sha256` always exist, even for empty baselines; added F5 process-substitution `cmp -s` so zero-row final manifests compare to zero-byte baseline manifests; required Todo 1 evidence to explicitly include plan/draft and every user-approved dirty non-output path in the protected baseline path list; made F5 fail before manifest comparison if required protected paths are absent; replaced split Stage 2 tokens with the full combined AGENTS phrase `提问可以跳远，论证不能偷步` and required a full-phrase PASS row.
- Seventh-round Metis receipt: `bg_322cef47` / `ses_0a0313cc1ffeDs4wk7mySXWaRG` returned `APPROVE` on the sixth-round fixes.
- Seventh-round Oracle receipt: `bg_2d3e1623` / `ses_0a03136cdffeQeJo5HGzBeaFJ7` aborted with `Session error: Aborted`; treated as API/session failure, not an audit verdict.
- Seventh-round Momus receipt: `bg_3e21d96f` / `ses_0a0315f0fffeYD4ht9ZodUJcEs` aborted with `Session error: Aborted`; treated as API/session failure, not an audit verdict.
- Restarted Oracle receipt: `bg_1f00e4a5` / `ses_0a01a8776ffeYwcR6fvZdAoY5r` returned `APPROVE`.
- Restarted Momus receipt: `bg_7963bc52` / `ses_0a01a8e47ffeYr9v0ncZojf00k` returned `APPROVE`.
- Final review status: current `.omo/plans/split-weread-prompts-by-stage.md` has fresh usable approvals from Metis, Oracle, and Momus. The plan is ready for user approval, but approval still does not execute the split or authorize commit/push.

## Decisions (with rationale)

1. **总入口不退化成目录页。** 它必须继续保存核心目标、不可降级原则、任务入口门、阶段路由、冲突优先级、Git/执行授权边界、复杂任务计划门和回归样本机制；否则阶段文件很容易变成互相不一致的独立提示词。
2. **阶段文件是“执行工单 / 新 session 启动器”。** 每个阶段文件开头必须写清：适用总入口、必须先读的文件、阶段输入、阶段输出、禁止事项、QA 门、证据路径和“若与总入口冲突，以总入口为准”。
3. **通用拆分先于《人生》拆分，并设硬 QA。** 通用文件拆错会污染《人生》拆分；因此 Wave 1 通过后才能进入 Wave 2。
4. **《人生》专用拆分保留书目专属事实，不把它抽回通用。** 包括固定路径、双 bookId、人物/主题方向、第四阶段表格方向和 7 个回归风险样本。
5. **不在本计划里执行拆分，也不沉淀“从开始优化提示词到最后拆分提示词”的方法论。** 用户已确认：先制定拆分 plan；真正拆分在新 session 执行；完整提示词优化思路等拆完后再统一沉淀。

## Scope IN

- 写一个可交给新 session 执行的总计划：`.omo/plans/split-weread-prompts-by-stage.md`。
- 计划覆盖两个 sequential wave：先通用，后《人生》。
- 计划指定所有目标文件名、依赖关系、阶段边界、QA gate、证据路径和禁止事项。
- 计划要求执行者只改提示词拆分相关文件与 `.omo/evidence`，不得处理阅读材料。

## Scope OUT (Must NOT have)

- 不在当前 session 修改 `微信读书通用提示词.md` 或 `路遥/人生/《人生》微信读书提示词.md` 的正文内容。
- 不创建阶段提示词文件；这些属于新 session 执行计划时的工作。
- 不修改《人生》中间整理稿、正式阅读笔记、其他书目提示词或其他阅读材料。
- 不提交 `.omo/run-continuation/*.json`。
- 不把 `/shared/start-work` 写成用户命令；只能说“当前客户端注册的 start-work 执行入口”，必要时举 `/start-work <plan-name>` 或 `$start-work <plan-name>` 为环境示例。

## Open questions

None. Defaults above are reversible except the user-confirmed two-wave order and hard QA gate.

## Approval gate

status: awaiting-approval

The amended plan is written at `.omo/plans/split-weread-prompts-by-stage.md`. Next user decision after review completion: approve the amended plan for a later execution session or request further changes. Approval of this plan does not execute the split and does not authorize commit/push.
