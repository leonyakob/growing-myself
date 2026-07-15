---
slug: clean-weread-split-artifacts
status: reviewed-ready-for-user-approval
intent: clear
review_required: true
pending-action: user reviews three-review-approved .omo/plans/clean-weread-split-artifacts.md; execution happens only in a separate execution session after user approval
approach: targeted markdown cleanup of stale split-task engineering artifacts; no prompt architecture rewrite and no reading-material edits
---

# Draft: clean-weread-split-artifacts

## Components (topology ledger)
<!-- Lock the SHAPE before depth. One row per top-level component that can succeed or fail independently. -->
<!-- id | outcome (one line) | status: active|deferred | evidence path -->

| id | outcome | status | evidence path |
| --- | --- | --- | --- |
| C1 | Generic stage prompt QA evidence lines no longer point to historical `split-weread-prompts-by-stage` files | active | `/home/king/github/growing-myself/.omo/evidence/task-clean-weread-split-artifacts.md` |
| C2 | 《人生》 stage prompt QA evidence lines and second-stage QA record sentence no longer point to historical split-task evidence | active | `/home/king/github/growing-myself/.omo/evidence/task-clean-weread-split-artifacts.md` |
| C3 | 《人生》 `Task 8` / `snapshot` / `ledger` / `Wave 2` wording is replaced with stable long-term guardrail text | active | `/home/king/github/growing-myself/.omo/evidence/task-clean-weread-split-artifacts.md` |
| C4 | Router, stage boundaries, AGENTS literary rules, 《人生》 bookIds and regression sentinels are preserved | active | `/home/king/github/growing-myself/.omo/evidence/task-clean-weread-split-artifacts.md` |

## Open assumptions (announced defaults)
<!-- Record any default you adopt instead of asking, so the user can veto it at the gate. -->
<!-- assumption | adopted default | rationale | reversible? -->

| assumption | adopted default | rationale | reversible? |
| --- | --- | --- | --- |
| User wants a plan, not execution | Write only `.omo` plan/draft; do not edit target prompt files in this session | User explicitly said they will run another execution session after review | yes |
| QA evidence wording | Use current-task/plan evidence if specified; otherwise final response lists QA pass/fail; never reuse historical split-task evidence | Prevents future agents from writing ordinary reading-task QA into split-task evidence files | yes |
| `AGENTS.md` wording | Replace `Task 8` history with stable “read only if file exists; do not fabricate rules” wording | Keeps the safety rule without preserving split-execution history | yes |
| Review level | Completed new Momus + Metis + Oracle reviews before handoff | User explicitly asked to send Momus/Metis/Oracle to review this plan carefully | yes |

## Findings (cited - path:lines)

- `微信读书通用提示词-第一阶段-生成中间整理稿.md:13` still references the historical split-task evidence file after otherwise good dynamic QA wording.
- `微信读书通用提示词-第二阶段-优化中间整理稿.md:21`, `微信读书通用提示词-第三阶段-迁移到正式阅读笔记.md:11`, and `微信读书通用提示词-第四阶段-全书收束整合.md:11` point directly to historical split-task evidence.
- `路遥/人生/《人生》微信读书提示词-第一阶段-生成中间整理稿.md:14`, `路遥/人生/《人生》微信读书提示词-第二阶段-优化中间整理稿.md:24`, `路遥/人生/《人生》微信读书提示词-第三阶段-迁移到正式阅读笔记.md:25`, and `路遥/人生/《人生》微信读书提示词-第四阶段-全书收束整合.md:26` point directly to historical split-task evidence.
- `路遥/人生/《人生》微信读书提示词-第二阶段-优化中间整理稿.md:442` tells the agent to record runtime QA into the historical split-task evidence file.
- `路遥/人生/《人生》微信读书提示词.md:43`, `路遥/人生/《人生》微信读书提示词-第一阶段-生成中间整理稿.md:7`, `路遥/人生/《人生》微信读书提示词-第二阶段-优化中间整理稿.md:9`, `路遥/人生/《人生》微信读书提示词-第三阶段-迁移到正式阅读笔记.md:10`, and `路遥/人生/《人生》微信读书提示词-第四阶段-全书收束整合.md:10` contain `Task 8` / `snapshot` / `ledger` / `快照` execution-history wording.
- `路遥/人生/《人生》微信读书提示词-第二阶段-优化中间整理稿.md:23` contains `不得修改其他 Wave 2 文件。`, which is a split-plan artifact rather than durable scope wording.
- API interruption note: the earlier API interruption is not a subtask result and is not prompt-file evidence. Current progress was confirmed from disk; the plan/draft had not persisted and was re-scaffolded.
- New Metis review session `ses_09bccc041ffe87RwV31f7iAnkF` returned NOT OK initially due to dependency/QA/success-criteria issues; those findings were folded into the current plan.

## Decisions (with rationale)

- Keep the cleanup narrow: only stale engineering artifacts are targeted, because the previous quality review found the actual split architecture sound.
- Do not normalize all formatting: mixed Chinese/English labels and blockquote inheritance blocks are not execution risks.
- Use sequential edits for overlapping 《人生》 files: Metis flagged that parallel Todo 3/Todo 4 edits would touch the same files.
- Treat prompt-surface QA as agent-executed: final verification must not depend on external confirmation.
- Preserve blockquote prefixes in both generic and 《人生》第四阶段 files.

## Scope IN

- `.omo/plans/clean-weread-split-artifacts.md`
- `.omo/drafts/clean-weread-split-artifacts.md`
- Execution-session target files listed in the plan:
  - `微信读书通用提示词-第一阶段-生成中间整理稿.md`
  - `微信读书通用提示词-第二阶段-优化中间整理稿.md`
  - `微信读书通用提示词-第三阶段-迁移到正式阅读笔记.md`
  - `微信读书通用提示词-第四阶段-全书收束整合.md`
  - `路遥/人生/《人生》微信读书提示词.md`
  - `路遥/人生/《人生》微信读书提示词-第一阶段-生成中间整理稿.md`
  - `路遥/人生/《人生》微信读书提示词-第二阶段-优化中间整理稿.md`
  - `路遥/人生/《人生》微信读书提示词-第三阶段-迁移到正式阅读笔记.md`
  - `路遥/人生/《人生》微信读书提示词-第四阶段-全书收束整合.md`
  - `/home/king/github/growing-myself/.omo/evidence/task-clean-weread-split-artifacts.md` during execution

## Scope OUT (Must NOT have)

- No editing reading notes, middle drafts, formal reading notes, exported WeChat data, or book content.
- No restructuring routers, stage split architecture, or workflow design.
- No changing 《人生》 bookIds, article directions, literary examples, or regression sentinels.
- No creating or assuming `路遥/人生/AGENTS.md`.
- No committing unless the user explicitly asks after execution.

## Open questions

None blocking. User only needs to review and approve/reject this plan before starting a separate execution session.

## Approval gate
status: reviewed-ready-for-user-approval
pending action: user reviews `/home/king/github/growing-myself/.omo/plans/clean-weread-split-artifacts.md`; after approval, a separate execution session may implement it.
<!-- When exploration is exhausted and unknowns are answered, set status: awaiting-approval. -->
<!-- That durable record is the loop guard: on a later turn read it and resume at the gate instead of re-running exploration. -->

## High-accuracy review receipts

- Requested by user: Momus / Metis / Oracle careful plan review.
- Review round 1:
  - Momus `ses_09bbb4ec8ffecvViFiJ1UJ2qqd`: OK.
  - Metis `ses_09bbb49f5ffeKPhuIIH7uYY8wp`: NOT OK. Required owner-visible QA fallback, no-match grep semantics, baseline guardrails, per-string protected checks, exact replacement wording, absolute Read paths.
  - Oracle `ses_09bbb43aaffeNbZdzETzUfdEWt`: NOT OK. Required exact replacement text, no-match exit-code semantics, fresh evidence section, preservation baselines, objective prompt-surface QA.
- Fixes folded into plan:
  - Replaced suggestion-style wording with exact replacement text / replacement maps.
  - Added explicit QA fallback behavior as a visible plan decision.
  - Added no-match `git grep` exit-code semantics and match-count/exit-code evidence requirements.
  - Added fresh evidence run section with timestamp, HEAD, initial status and baseline scans.
  - Added preservation baselines for same-book AGENTS, sibling-book guardrails, bookIds, regression sentinels, article directions and literary rules.
  - Made Read-tool paths absolute and final prompt-surface QA checklist objective.
- Review round 2:
  - Momus `ses_09baaad50ffeet8Da8GgCRU0gL`: REJECT. F4 scope fidelity had to compare against Todo 1 initial status, not unscoped `git diff --name-only`.
  - Metis `ses_09baaa822ffelHwkmcb6IpuBpk`: NOT OK. Todo 4 QA conflicted with Todo 5 `Wave 2` dependency; Todo 5 exact replacement needed nested-list indentation.
  - Oracle `ses_09baaa1dbffe6H0Q5Lj2uaV3Cq`: OK with optional risks.
- Fixes folded into plan after round 2:
  - F4 now compares final `git status --short --untracked-files=all` against Todo 1 initial status and ignores pre-existing dirty paths.
  - Todo 4 now allows `Wave 2` to remain until Todo 5.
  - Todo 5 exact replacement preserves the existing two-space nested-list indentation.
  - Todo 4 replacement map no longer adds `本文件` to first-stage pre-read.
  - Protected checks include article-direction strings.
- Final review round:
  - Momus `ses_09ba18c40ffeiHCgZpxEldagLs`: OK. Previously blocking F4/Todo4/Todo5 points resolved.
  - Metis `ses_09ba184ceffeC5rZSGmhZ09hTi`: OK. No remaining hidden assumption requiring user decision.
  - Oracle `ses_09ba17d73ffesi6cfZi1h31RJu`: OK. No material blockers; plan is safe, scoped and decision-complete for separate execution session.
- Status: three-review-approved; ready for user approval. Execution must still happen in a separate worker session.
