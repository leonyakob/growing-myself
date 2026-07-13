---
slug: refine-weread-workflow-handoff
status: awaiting-approval
intent: clear
pending-action: user approval before editing target prompt files
approach: Adjust only the generic and 《人生》 WeRead prompt workflow rules; require Momus/Metis/Oracle plan review before complex-task execution; clarify start-work as a client/runtime entry rather than a universal literal command; wait for user approval before editing either prompt.
---

# Draft: refine-weread-workflow-handoff

## Components (topology ledger)

| id | outcome | status | evidence path |
|---|---|---|---|
| C1 | Generic prompt workflow wording is corrected without overfitting to one command prefix | active | .omo/plans/refine-weread-workflow-handoff.md |
| C2 | Generic auxiliary templates are reframed as bounded shortcuts, not workflow overrides | active | .omo/plans/refine-weread-workflow-handoff.md |
| C3 | 《人生》 prompt is synchronized with the same workflow fixes while preserving book-specific regressions | active | .omo/plans/refine-weread-workflow-handoff.md |
| C4 | Mandatory plan-review chain is explicit: Momus + Metis + Oracle, incorporated findings, then explicit execution authorization | active | .omo/plans/refine-weread-workflow-handoff.md |

## Open assumptions (announced defaults)

| assumption | adopted default | rationale | reversible? |
|---|---|---|---|
| `mous` in the user's wording | Treat as Momus, the plan critic/reviewer | Prior conversation used Momus for plan review; available agent list includes `momus` | Yes |
| start-work command spelling | Do not hard-code `$start-work` as the only user-facing command; write “use the current client’s registered start-work entry,” with examples including the user's `/start-work <plan-name>` and the skill-doc `$start-work <plan-name>` where that syntax is active | Skill docs show `$start-work`; user reports slash command works in daily environment; prompt should not encode a false cross-client universal | Yes |
| manual agent switching | State no manual switch to Prometheus/Atlas is normally required; planning and execution are skill/workflow roles | Skills are loaded by task intent; user works primarily through Hephaestus-Deep | Yes |

## Findings (cited - path:lines)

- `微信读书通用提示词.md:29-39` already contains a top task entrance gate, but it says read-only consulting does not trigger `/shared/start-work`, which still treats an internal skill ID as user-facing wording.
- `微信读书通用提示词.md:1003-1011` currently says `/shared/start-work` is the exact skill name and command spelling, while rejecting `/start work`; this overstates one internal skill identifier as a user-facing command.
- `微信读书通用提示词.md:1019-1073` keeps useful auxiliary prompt snippets, but does not explicitly say they remain subject to the task entrance gate and complex-task gate.
- `路遥/人生/《人生》微信读书提示词.md:29` says complex execution must use `start-work`, without distinguishing a user-facing command from a skill/runtime entry.
- `路遥/人生/《人生》微信读书提示词.md:43-52` phase entry conditions still reference Git checkpoints as phase prerequisites.
- `路遥/人生/《人生》微信读书提示词.md:82-118` still treats phase transition as a Git commit/push checkpoint; generic prompt has already moved toward conditional Git authorization.
- `路遥/人生/《人生》微信读书提示词.md:971-979` still includes the mechanical “3 cards” threshold and unqualified `start-work` wording.
- `路遥/人生/《人生》微信读书提示词.md:998-1040` has seven useful auxiliary snippets but lacks a boundary header.
- `路遥/人生/《人生》微信读书提示词.md:1044-1054` contains seven book-specific regression labels that must be preserved exactly in substance and by label.
- `shared/start-work` skill documentation shows usage as `$start-work [plan-name]`, but the user reports routine client usage as `/start-work <plan-name>`; therefore the prompts should describe the action as the current registered start-work entry and include examples, not claim a single global prefix.

## Review receipts

| reviewer | session | verdict | incorporated changes |
|---|---|---|---|
| Momus | `ses_0a5499651ffesB30TYH5vqujdE` | OKAY | Filled TL;DR, tightened QA wording, and removed dependency/parallelization ambiguity. |
| Metis | `ses_0a5498f15ffehz4HXGf2LMWjIb`; post-fix PASS `ses_0a4de11d3ffe7Bc1evi853CXdf` | REJECT before fixes, PASS after fixes | Added generic section 0.1, 《人生》 phase-entry and auxiliary-section work, exact regression-label preservation checks, safer commit strategy, and natural-language execution-intent wording; post-fix review confirmed the seven blockers are resolved. |
| Oracle | `ses_0a5498e8bffeM7qeoNeqhGqdje` | PASS with hardening | Added review receipt requirement and all-occurrences command-syntax audit. |

## Decisions (with rationale)

1. Use the user’s required review chain as a hard rule for complex-task plans: after drafting a plan, dispatch Momus, Metis, and Oracle; incorporate their findings into the plan; only then present the reviewed plan for user confirmation.
2. Separate three gates everywhere: plan approval, review completion, and execution authorization. Plan approval alone does not execute; “审查补全后执行” can authorize execution only after review findings are incorporated.
3. Replace false command precision with runtime-aware wording: “调用当前客户端注册的 start-work 执行入口（例如本项目用户常用的 `/start-work <plan-name>`；若某环境说明为 `$start-work <plan-name>`，按该环境使用）”. Explicitly forbid treating `/shared/start-work`, `/start work`, or bare `start-work` as universal command spellings, while preserving natural-language “开始执行计划 / start work” as execution-intent signals that still require runtime routing.
4. Keep auxiliary prompt sections, but add a boundary header: they are shortcut templates for task scope, not authorization to skip planning, review, QA, Git rules, or explicit execution.
5. Synchronize 《人生》 prompt with generic prompt only for reusable workflow rules; preserve 《人生》 paths, theme language, and known regression samples.

## Scope IN

- Plan edits for `/home/king/github/growing-myself/微信读书通用提示词.md`.
- Plan edits for `/home/king/github/growing-myself/路遥/人生/《人生》微信读书提示词.md`.
- Mandatory plan-review wording: Momus + Metis + Oracle, findings incorporated before handoff.
- Command wording that accommodates the user’s slash-command workflow without contradicting skill-doc examples.
- Auxiliary prompt section boundary and deduplication guidance.
- Conditional Git checkpoint wording in 《人生》 prompt.
- Exact preservation checks for seven 《人生》 regression sample labels.

## Scope OUT (Must NOT have)

- Do not edit either prompt until the user explicitly approves this reviewed plan.
- Do not remove 《人生》 book-specific regression samples.
- Do not introduce a requirement for the user to manually switch to Prometheus-Plan Builder or Atlas-Plan Executor.
- Do not claim `$start-work` is universally required, and do not claim `/shared/start-work` is a user command.
- Do not reject natural-language “开始执行计划 / start work” as execution intent; only avoid treating it as a universal literal command.
- Do not commit or push unless the user explicitly asks after implementation.
- Do not stage `.omo` planning/evidence artifacts by default if the user only asks to commit implemented prompt changes.

## Open questions

None. The user’s preference is clear: keep Hephaestus workflow, require Momus/Metis/Oracle review for complex plans, and support the slash-style start-work command they use while acknowledging environment-specific syntax.

## Approval gate

status: awaiting-approval

When the user approves, implementation may edit only the two target prompt files according to `.omo/plans/refine-weread-workflow-handoff.md`. Approval of this plan does not itself mean commit/push authorization.
