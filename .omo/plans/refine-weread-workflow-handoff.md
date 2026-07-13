# refine-weread-workflow-handoff - Work Plan

## TL;DR (For humans)

**What you'll get:** A small, targeted revision to the generic WeRead prompt and the 《人生》 prompt so complex tasks always go through planning, Momus/Metis/Oracle review, incorporated fixes, explicit authorization, and the correct start-work entry for the current client.

**Why this approach:** The current prompts mix internal skill names, client command syntax, Git checkpoints, and shortcut templates. This plan separates those gates so future runs do not confuse “plan approved” with “execute now,” or one client’s command prefix with a universal rule.

**What it will NOT do:** It will not edit either prompt before user approval, require manual switching to Prometheus/Atlas, delete useful shortcut templates, or remove 《人生》 regression samples.

**Effort:** Short
**Risk:** Medium - the main risk is writing a command spelling or workflow gate that is too specific to one client and later misleads execution.
**Decisions to sanity-check:** Keep auxiliary prompts as bounded shortcuts; describe start-work as a runtime/client entry with examples rather than one universal literal command; make Momus/Metis/Oracle review mandatory for complex-task plans.

Your next move: approve this reviewed plan, or request changes. Implementation will not start until you explicitly approve. Full execution detail follows below.

---

> TL;DR (machine): Short/Medium-risk documentation workflow update for two prompt files; no target edits until reviewed by Momus/Metis/Oracle and approved by the user.

## Review receipts

| reviewer | session | verdict | incorporated changes |
|---|---|---|---|
| Momus | `ses_0a5499651ffesB30TYH5vqujdE` | OKAY | Filled TL;DR, tightened QA wording, and removed dependency/parallelization ambiguity. |
| Metis | `ses_0a5498f15ffehz4HXGf2LMWjIb`; post-fix PASS `ses_0a4de11d3ffe7Bc1evi853CXdf` | REJECT before fixes, PASS after fixes | Added generic section 0.1, 《人生》 phase-entry and auxiliary-section work, exact regression-label preservation checks, safer commit strategy, and natural-language execution-intent wording; post-fix review confirmed the seven blockers are resolved. |
| Oracle | `ses_0a5498e8bffeM7qeoNeqhGqdje` | PASS with hardening | Added review receipt requirement and all-occurrences command-syntax audit. |

## Scope

### Must have

- Record that this plan itself was reviewed by Momus, Metis, and Oracle; blockers from Metis and hardening suggestions from Oracle/Momus are incorporated before presenting the plan to the user.
- Update `微信读书通用提示词.md` so complex-task planning rules require: draft plan, Momus + Metis + Oracle review, incorporate findings, present reviewed plan, then execute only after explicit authorization.
- Update `微信读书通用提示词.md` top entrance gate as well as section 12.2: remove `/shared/start-work` from any user-facing or task-gate wording.
- Update `微信读书通用提示词.md` so start-work wording is client/runtime aware: use the current registered start-work entry; examples may include the user’s `/start-work <plan-name>` and the skill-doc `$start-work <plan-name>`, but neither should be presented as universal across all clients.
- Preserve natural-language execution intent: “开始执行计划” or “start work” can be treated as an intent signal, but still must route through the current runtime’s registered start-work entry.
- Update `微信读书通用提示词.md` so the user does not need to manually switch to Prometheus or Atlas in ordinary use; Hephaestus may route into planning/execution workflows.
- Update `微信读书通用提示词.md` section 13 so auxiliary prompts are explicitly “shortcut task templates” that do not bypass AGENTS, task entrance gates, complex-task planning, three-agent review, QA, Git authorization, or explicit execution authorization.
- Update `路遥/人生/《人生》微信读书提示词.md` to match the reusable workflow fixes while preserving 《人生》 paths, examples, theme wording, and regression samples.
- Update `路遥/人生/《人生》微信读书提示词.md` phase-entry conditions so they require stage-switch QA, and only require Git checkpoint completion when the current user instruction explicitly authorizes commit/push.
- Update `路遥/人生/《人生》微信读书提示词.md` so phase-switch QA remains mandatory but commit/push are conditional on current explicit Git authorization.
- Update `路遥/人生/《人生》微信读书提示词.md` auxiliary prompt section so its seven snippets are bounded shortcuts, not workflow overrides.
- Remove or soften mechanical complexity triggers in 《人生》 prompt, especially the “3 cards” threshold and unqualified “不降低数量”; replace with complexity based on core-card entanglement, multi-file/multi-stage work, structure changes, or explicit quality emphasis, while preserving “do not omit in-scope user material”.

### Must NOT have (guardrails, anti-slop, scope boundaries)

- Must not edit either target prompt before this plan is reviewed and the user approves implementation.
- Must not delete the useful auxiliary prompt snippets wholesale; only bound, rename, and deduplicate them where needed.
- Must not remove 《人生》 known regression samples or replace them with generic examples.
- Must not say `/shared/start-work` is a user-facing command.
- Must not say bare `start-work` is enough to execute a plan.
- Must not reject natural-language “开始执行计划 / start work” as an intent signal; only reject it as a universal literal command spelling.
- Must not require manual switching to Prometheus-Plan Builder or Atlas-Plan Executor as a normal user step.
- Must not commit or push unless the user explicitly asks after implementation.
- Must not stage `.omo` plan/evidence artifacts by default if the user only asks to commit the implemented prompt changes.

## Verification strategy

> Zero human intervention - all verification is agent-executed.

- Test decision: none; this is Markdown prompt editing. Verification is structural diff review, targeted read-back, string checks, and `git diff --check`.
- Evidence: `.omo/evidence/task-<N>-refine-weread-workflow-handoff.md`

## Execution strategy

### Parallel execution waves

- Pre-execution review wave, completed before this approval gate: Momus (`ses_0a5499651ffesB30TYH5vqujdE`), Metis (`ses_0a5498f15ffehz4HXGf2LMWjIb`), and Oracle (`ses_0a5498e8bffeM7qeoNeqhGqdje`) independently reviewed this plan. Metis blockers and Oracle/Momus hardening requests are incorporated here.
- Implementation Wave 1 can edit the generic prompt and the 《人生》 prompt in parallel only if workers coordinate non-overlapping files.
- Final verification wave must read both changed prompt sections and confirm that the rules are consistent across files but not over-copied.

### Dependency matrix

| Todo | Depends on | Blocks | Can parallelize with |
| --- | --- | --- | --- |
| 1 | Reviewed plan approved by user | 4, F1-F4 | 2, 3 |
| 2 | Reviewed plan approved by user | 4, F1-F4 | 1, 3 |
| 3 | Reviewed plan approved by user | 4, F1-F4 | 1, 2 |
| 4 | 1, 2, 3 | F1-F4 | none |

## Todos

- [ ] 1. Generic prompt: clarify complex-task planning, review, and execution handoff
  What to do / Must NOT do: In `微信读书通用提示词.md`, revise both the top entrance gate and the complex-task handoff around section 12.2. Required wording: complex tasks that require a plan must go through plan draft -> Momus + Metis + Oracle review -> incorporate findings into the plan -> present reviewed plan -> execute only after explicit user authorization. Clarify that the user normally does not manually switch agents; Hephaestus may route to planning/execution workflows. Replace command wording with a client/runtime-aware start-work entry: mention the user’s slash-style `/start-work <plan-name>` as a valid example in their workflow and the skill-doc `$start-work <plan-name>` as an environment-specific example; explicitly say prompts must not treat `/shared/start-work`, `/start work`, or bare `start-work` as universal command spellings. Preserve natural-language “开始执行计划 / start work” as execution-intent signals that still require runtime routing. Must NOT claim one prefix is globally required.
  Parallelization: Wave 1 | Blocked by: reviewed plan approved by user | Blocks: 4, F1-F4
  References (executor has NO interview context - be exhaustive): `微信读书通用提示词.md:29-39`; `微信读书通用提示词.md:985-1011`; `shared/start-work` skill usage says `$start-work [plan-name]`; user reports `/start-work <plan-name>` as routine client command.
  Acceptance criteria (agent-executable): Read back section 0.1 and section 12.2 and confirm they contain `Momus`, `Metis`, `Oracle`, `审查意见`, `明确授权`, `当前客户端`, and `start-work`; confirm the entire file no longer contains `/shared/start-work`.
  QA scenarios (name the exact tool + invocation): happy: `GIT_MASTER=1 git diff -- 微信读书通用提示词.md` shows only workflow wording changes; failure: `GIT_MASTER=1 git grep -n '/shared/start-work\|/start work 是\|start-work 只是含义不明' -- 微信读书通用提示词.md` must return no forbidden command-claim lines. Evidence `.omo/evidence/task-1-refine-weread-workflow-handoff.md`.
  Commit: N | docs(weread): refine generic workflow handoff

- [ ] 2. Generic prompt: bound auxiliary prompt templates without deleting their useful shortcuts
  What to do / Must NOT do: In `微信读书通用提示词.md`, retitle or preface section 13 as shortcut templates that remain subordinate to AGENTS.md, task entrance gates, complex-task planning, mandatory three-agent plan review, QA, Git authorization, and execution authorization. Keep the useful snippets: only整理, only判卡, only轻卡, only完整卡/主卡, chapter scan, judgment-based external-reader query, whole-book reading-style review. Deduplicate migration precheck/post-QA snippets by pointing them back to section 11 if they merely restate section 11; do not remove the underlying requirements from section 11.
  Parallelization: Wave 1 | Blocked by: reviewed plan approved by user | Blocks: 4, F1-F4
  References (executor has NO interview context - be exhaustive): `微信读书通用提示词.md:1019-1073`; `微信读书通用提示词.md:862-967` for section 11 migration rules.
  Acceptance criteria (agent-executable): Read back section 13 and confirm it explicitly says templates do not bypass complex-task planning/review/execution authorization. Confirm at least five shortcut snippets remain.
  QA scenarios (name the exact tool + invocation): happy: `read(filePath="/home/king/github/growing-myself/微信读书通用提示词.md", offset=1019, limit=70)` confirms the boundary preface and at least five snippets; failure: `GIT_MASTER=1 git grep -n '绕过.*复杂任务\|绕过.*审查\|直接执行计划' -- 微信读书通用提示词.md` must not reveal a contradictory shortcut. Evidence `.omo/evidence/task-2-refine-weread-workflow-handoff.md`.
  Commit: N | docs(weread): bound auxiliary shortcuts

- [ ] 3. 《人生》 prompt: synchronize workflow, command, conditional Git, and auxiliary shortcuts
  What to do / Must NOT do: In `路遥/人生/《人生》微信读书提示词.md`, update the task entrance gate, phase-entry conditions, phase-switch Git section, complex-task section, and auxiliary prompt section. Replace unqualified `start-work` with runtime/client-aware start-work wording consistent with the generic prompt. Add the mandatory Momus + Metis + Oracle review chain for complex plans. Change stage-switch Git checkpoint from automatic commit/push to mandatory QA plus conditional commit/push only when current user instruction explicitly authorizes Git. In section 12, add a boundary preface saying the seven snippets are shortcuts only and do not bypass section 0 entrance gates, section 11 complex-task planning, Momus/Metis/Oracle review, explicit execution authorization, phase-switch QA, conditional Git authorization, AGENTS.md, or 《人生》 regression samples. Must preserve all fixed paths, 《人生》-specific theme language, and known regression samples.
  Parallelization: Wave 1 | Blocked by: reviewed plan approved by user | Blocks: 4, F1-F4
  References (executor has NO interview context - be exhaustive): `路遥/人生/《人生》微信读书提示词.md:22-30`; `路遥/人生/《人生》微信读书提示词.md:43-52`; `路遥/人生/《人生》微信读书提示词.md:82-118`; `路遥/人生/《人生》微信读书提示词.md:967-989`; `路遥/人生/《人生》微信读书提示词.md:998-1040`; `路遥/人生/《人生》微信读书提示词.md:1044-1054`.
  Acceptance criteria (agent-executable): Read back sections 0, 1, 3, 11, 12, and 13; confirm automatic commit/push wording is gone; confirm phase entry conditions say QA is mandatory and Git checkpoint only applies when the current user explicitly authorizes commit/push; confirm `Momus`, `Metis`, and `Oracle` appear in the complex-task plan rule; confirm all seven auxiliary snippets remain; confirm all seven regression sample labels remain: `ID 003`, `ID 006`, `ID 021`, `ID 109`, `ID 117`, `刘玉海救灾处`, `黄亚萍的物质付出`.
  QA scenarios (name the exact tool + invocation): happy: `GIT_MASTER=1 git diff -- 路遥/人生/《人生》微信读书提示词.md` shows workflow wording only; failure: `GIT_MASTER=1 git grep -n '执行阶段必须使用 `start-work`\|处理 3 张以上完整卡\|不降低数量，不降低深度' -- 路遥/人生/《人生》微信读书提示词.md` must return no stale workflow lines. Evidence `.omo/evidence/task-3-refine-weread-workflow-handoff.md`.
  Commit: N | docs(ren-sheng): sync workflow gates

- [ ] 4. Cross-file consistency audit and final read-back
  What to do / Must NOT do: After todos 1-3, audit both prompts for consistency. Confirm both say complex plans require Momus + Metis + Oracle review before execution; both separate plan approval, review completion, and execution authorization; both avoid claiming a single universal command prefix; both keep auxiliary snippets subordinate to workflow gates. Must NOT homogenize away 《人生》 book-specific regression samples or generic placeholders.
  Parallelization: Final implementation wave | Blocked by: 1, 2, 3 | Blocks: F1-F4
  References (executor has NO interview context - be exhaustive): all changed sections from todos 1-3.
  Acceptance criteria (agent-executable): `GIT_MASTER=1 git diff --check -- 微信读书通用提示词.md 路遥/人生/《人生》微信读书提示词.md` exits 0; all occurrences of `start-work`, `/shared/start-work`, `$start-work`, `/start-work`, `start work`, and `/start work` in both target prompt files are classified as allowed example, forbidden command claim, or explanatory prose; targeted read-back confirms required phrases and forbidden phrases; `git status --short` shows only expected prompt and `.omo` planning/evidence files unless runtime session metadata changes.
  QA scenarios (name the exact tool + invocation): happy: run exact diff-check command and record excerpts; failure: `GIT_MASTER=1 git grep -n 'start-work\|/shared/start-work\|\$start-work\|/start-work\|start work\|/start work' -- 微信读书通用提示词.md 路遥/人生/《人生》微信读书提示词.md` must be classified in evidence and any forbidden command claim blocks completion. Evidence `.omo/evidence/task-4-refine-weread-workflow-handoff.md`.
  Commit: N | docs(weread): verify prompt workflow consistency

## Final verification wave

> Runs after all todos. All must approve before completion.

- [ ] F1. Plan compliance audit: reviewer confirms every Must Have and Must NOT Have is satisfied in the two prompt files.
- [ ] F2. Language quality review: reviewer confirms wording is clear to a future AI/user and does not overfit to one client command prefix.
- [ ] F3. Scenario routing QA: simulate three user utterances against the prompt rules in prose: “只整理”, “复杂任务先计划审查补全后执行”, and “只评价问题质量”; confirm the rules route each correctly.
- [ ] F4. Scope fidelity: reviewer confirms no unrelated reading notes, 《人生》 regression samples, or other book files were modified.

## Commit strategy

No commit during implementation unless the user explicitly asks after approving and reviewing the final diff. If the user asks to commit the implemented prompt change, default to staging only the two target prompt files. Include `.omo/` plan or evidence artifacts only if the user explicitly asks to archive planning/evidence files in Git. Never include unrelated runtime session metadata unless explicitly requested.

## Success criteria

- The reviewed plan has Momus, Metis, and Oracle receipts before implementation begins.
- `微信读书通用提示词.md` and `路遥/人生/《人生》微信读书提示词.md` both encode the user’s mandatory complex-task review chain.
- Both prompts avoid false command certainty: `/shared/start-work` is not presented as a user command, and `$start-work` is not presented as globally mandatory against the user’s slash-command environment.
- Natural-language execution intent remains valid but must route through the current registered start-work entry.
- Auxiliary prompt sections remain useful but cannot bypass planning/review/QA/authorization gates.
- 《人生》 prompt preserves its book-specific paths and all seven regression sample labels.
- No target prompt edits occur until the user approves this reviewed plan.
