---
slug: ren-sheng-stage5-question-compression
status: reviewed
intent: clear
review_required: true
pending-action: none - reviewed canonical plan is ready for user handoff; Stage 5 execution still requires separate start-work entry
approach: Create a Stage 5 execution plan that compresses the existing four-round and Stage 4 whole-book materials for Lu Yao's 《人生》 into exactly three essay-grade core questions, with evidence/counterevidence, tension map, five-anomaly close reading, writing conversion, Lu Yao writing-method dossier, cross-work links, and strict no-file-edit/no-fake-evidence guardrails.
---

# Draft: ren-sheng-stage5-question-compression

## Components (topology ledger)
<!-- id | outcome (one line) | status: active|deferred | evidence path -->

| id | outcome | status | evidence path |
| --- | --- | --- | --- |
| C1 | Source/rule grounding preserves project rules, 《人生》 stage boundaries, and Stage 4 as navigation only | active | `.omo/evidence/ren-sheng-stage5-question-compression/task-01-source-ledger.md` |
| C2 | Candidate question pool maps Stage 4 article index back to original cards and user live sentences | active | `.omo/evidence/ren-sheng-stage5-question-compression/task-03-question-pool.md` |
| C3 | Exactly three non-overlapping 5-star core questions are selected with explicit reject reasons for near-duplicates | active | `.omo/evidence/ren-sheng-stage5-question-compression/task-06-core-question-selection.md` |
| C4 | Each core question receives evidence/counterevidence tables, strength/threat ratings, and待原文复核 flags | active | `.omo/evidence/ren-sheng-stage5-question-compression/task-07-evidence-counterevidence.md` |
| C5 | Whole-book tension map and five-anomaly close-reading points stay grounded in scenes, actions, words, and cards | active | `.omo/evidence/ren-sheng-stage5-question-compression/task-08-tension-map.md`; `.omo/evidence/ren-sheng-stage5-question-compression/task-09-five-anomaly.md` |
| C6 | Writing conversion, Lu Yao writing-method dossier, cross-work links, and final response do not flatten user voice | active | `.omo/evidence/ren-sheng-stage5-question-compression/task-10-writing-conversion.md`; `.omo/evidence/ren-sheng-stage5-question-compression/task-12-final-output.md` |

## Open assumptions (announced defaults)
<!-- Record any default you adopt instead of asking, so the user can veto it at the gate. -->
<!-- assumption | adopted default | rationale | reversible? -->

| assumption | adopted default | rationale | reversible? |
| --- | --- | --- | --- |
| Stage 5 output location | Worker writes intermediate evidence under `.omo/evidence/ren-sheng-stage5-question-compression/` and presents the final Stage 5 deliverable in the final response; it does not edit `路遥/人生/《人生》阅读笔记.md` | User approved only `.omo` plan creation and review; project rules require explicit instruction before modifying reading materials | yes |
| Core-question count | Exactly 3 final questions | User's current Stage 5 brief requires three core questions | yes, only by user scope change |
| Evidence standard | Card/scene anchors are allowed; exact quotation must be marked `待原文复核` when not rechecked in the source text | Prevents fake precision while allowing planning from existing note material | yes |
| External reader material | Only challenges/supplements user-card evidence; never becomes main user judgment | Root and WeRead rules forbid external comments replacing user voice | no for this plan |
| Git | No stage/commit/push | User did not authorize Git; plan work is `.omo` only | yes with explicit Git authorization |

## Findings (cited - path:lines)

- Root project rules define this as writer-driven thematic reading, not academic polishing; the aim is to preserve user's living literary response while making analysis deeper and more text-grounded: `AGENTS.md:3-12`.
- Required analysis tools are 五异法、问题阶梯、张力地图: `AGENTS.md:14-18`.
- Card handling requires light/main distinction and detail-vs-theme directionality: `AGENTS.md:20-24`.
- WeRead handling must preserve user划线/想法, distinguish task boundaries, avoid overwriting user voice, and treat external high-like comments only as external reader material: `AGENTS.md:26-84`.
- Reading-note evaluation and question work must be concrete, evidence-based, and include question quality, counter-angles, writing direction, and cross-work paths without piling book names: `AGENTS.md:86-102`.
- Archival edits require explicit user instruction and must preserve four-part structure; current Stage 5 plan therefore must not edit the reading note unless separately authorized: `AGENTS.md:104-117`.
- 《人生》 router fixes the formal note path and confirms the book-specific `AGENTS.md` should be read only if it exists; it also forbids sibling-book rule leakage: `路遥/人生/《人生》微信读书提示词.md:28-45`.
- The router states analysis quality, textual evidence, and user intent outrank speed/format, and complex tasks must be planned, reviewed by Momus/Metis/Oracle, and only then execution can start through the runtime's actual start-work entry: `路遥/人生/《人生》微信读书提示词.md:55-64`.
- The router's Stage 4 summary says Stage 4 is `阅读现场档案 + 文章素材索引`, and explicitly says the article index cites cards but must not swallow them: `路遥/人生/《人生》微信读书提示词.md:83-88`.
- 《人生》 inherited article directions are 人物线、城乡主题、尊严主题、爱情线、知识分子困境、写法线索: `路遥/人生/《人生》微信读书提示词.md:146-158`.
- 《人生》 regression sentinels include ID 003, ID 006, ID 021, ID 109, ID 117, 刘玉海救灾处, and 黄亚萍的物质付出: `路遥/人生/《人生》微信读书提示词.md:221-231`.
- Stage 4 file defines the consolidation purpose and Must NOT list: no global Stage 3 rerun, no whole-note rewrite, no article-index replacing cards, no AI correction covering user words, no technical IDs in reader-facing body: `路遥/人生/《人生》微信读书提示词-第四阶段-全书收束整合.md:1-27`.
- Stage 4's core model is card archive as foundation, article index as navigation: `路遥/人生/《人生》微信读书提示词-第四阶段-全书收束整合.md:31-40`.
- Stage 4 explicitly preserves six article directions and the four-round reading progression: `路遥/人生/《人生》微信读书提示词-第四阶段-全书收束整合.md:42-57`.
- Stage 4 execution order and one-card-two-destinations rule prevent the article index from taking over card identity: `路遥/人生/《人生》微信读书提示词-第四阶段-全书收束整合.md:78-140`.
- Stage 4 article-index table fields already model core question, card anchor, original trigger, tension, usable evidence, and missing evidence: `路遥/人生/《人生》微信读书提示词-第四阶段-全书收束整合.md:185-197`.
- Stage 4 QA fixtures and self-checks are the immediate guardrail set for Stage 5 reuse: `路遥/人生/《人生》微信读书提示词-第四阶段-全书收束整合.md:253-282`.
- The reading note itself contains four rounds plus a Stage 4 whole-book consolidation: `路遥/人生/《人生》阅读笔记.md:3-6040`.
- Round 1 anchors include family root, county/town identity, self-respect contrast, toothbrush/secret-love card, Huang Yaping projection, and Qiaozhen action-love card: `路遥/人生/《人生》阅读笔记.md:13-293`.
- Round 2 anchors include the kiss-as-resume card, Qiaozhen education wound, specific care chain, relationship publicity/responsibility, village spectatorship, and Qiaozhen's self-blame/action: `路遥/人生/《人生》阅读笔记.md:567-1207`.
- Round 3 anchors include same-bike-different-hearts, faraway desire after love's comfort fails, Deshun's methods/philosophy/deep feeling, and Qiaozhen's subjectivity absorbed by love: `路遥/人生/《人生》阅读笔记.md:1248-1460`.
- Round 3 also gives method and correction anchors: modern civilization responsibility, Ga Jialin's one night of endurance, `有时`, `臭香哲学`, and the question of where city fire will burn: `路遥/人生/《人生》阅读笔记.md:1550-1697`.
- Round 4 anchors include borrowed power, `乡巴佬`, mutual excitement, Huang Yaping's value map, `让我好好想一想`, the ethics of breaking with Qiaozhen, class language, door-match shame, downstage risk, Deshun's conscience judgment, county-space distortion, Kenan ethics, the final `更爱巧珍` self-defense, and ending philosophy: `路遥/人生/《人生》阅读笔记.md:1701-2257`.
- Round 4 has 67 detailed scene cards and character-line supplements that can serve as evidence pools: `路遥/人生/《人生》阅读笔记.md:2294-5420`.
- Stage 4 consolidation already summarizes reading-site archive, article-material index, six directions, evidence gaps, and reading-trajectory corrections: `路遥/人生/《人生》阅读笔记.md:5932-6040`.

## Decisions (with rationale)

- D1: Stage 5 must start from Stage 4 index but trace every candidate back to original cards. Rationale: Stage 4 itself says the article index only points to cards and must not replace them.
- D2: The final output must contain exactly three core questions, not six article directions. Rationale: Stage 4's six directions are a navigation field; Stage 5's value is compression and prioritization.
- D3: The executor must build a reject ledger for unchosen candidate questions. Rationale: without reject reasons, overlapping themes such as 高加林身份羞耻、爱情位置、城乡欲望 can quietly become three versions of the same question.
- D4: Evidence and counterevidence must be graded. Rationale: Stage 5 needs essay-worthiness, not only notes; counterevidence protects against moral simplification.
- D5: User live sentences must be protected before analytical rewriting. Rationale: root rules explicitly treat the user's文气 and living sentences as strengths.
- D6: No product-note edits in this plan. Rationale: the user approved `.omo` planning and review, not archival updates or Stage 5 execution.
- D7: High-accuracy review is required now. Rationale: the user explicitly requested Momus/Oracle complete review on the canonical plan file.

## Scope IN

- Create and review `.omo/plans/ren-sheng-stage5-question-compression.md`.
- Plan a future worker execution for Stage 5 of 路遥《人生》: full-book question compression and writing conversion.
- Include exact source files, stage boundaries, output contract, quality gates, evidence/counterevidence requirements, and final verification criteria.
- Use current materials only: existing reading note, Stage 4 consolidation, project/book WeRead prompt files, and root rules.

## Scope OUT (Must NOT have)

- Must not execute Stage 5 content in this planning session.
- Must not edit `/home/king/github/growing-myself/路遥/人生/《人生》阅读笔记.md` or any reading material.
- Must not fetch or invent original novel quotations beyond what the notes contain; if exact novel text is needed, mark `待原文复核`.
- Must not create a fifth-stage prompt file unless the user explicitly requests prompt-file changes.
- Must not run Git stage/commit/push.
- Must not use external reader comments as if they were the user's own judgment.
- Must not collapse Qiaozhen, Huang Yaping, Kenan, Deshun, or village/official characters into props for judging Gao Jialin.

## Open questions

None. The user approved writing the `.omo` plan and requested Momus/Oracle review. Future execution still requires a separate start-work command/entry.

## Approval gate
status: approved-for-plan-file-and-high-accuracy-review

User approval received: “批准写入 .omo 计划文件,让 Momus / Oracle 对这个 canonical plan 文件做完整审核。”

Review receipts will be recorded after Momus and Oracle return.

## Metis gap-analysis receipt

- Reviewer: Metis (`ses_08ba1e178ffetVDAVVVSWhBGk1`)
- Verdict: NEEDS_REVISION
- Main must-fix items integrated into plan:
  1. Final verification F1-F4 now have references, acceptance criteria, happy/failure QA, evidence paths, and `Commit: N`.
  2. Todo 12 now requires reader-facing `自检与可靠性说明`.
  3. Verification strategy and Todos 1/13/F4 now require read-only product-file diff checks.
  4. Final QA now verifies every load-bearing claim traces to original card/scene anchors, not Stage-4-only support.
  5. Core-question count now guards against hidden fourth/fifth core questions in writing branches.
  6. User original sentence / card-novel phrase / AI summary / prohibited memory-quote categories are explicit.
  7. Technical IDs/ranges are fully banned from reader-facing output, including the `待原文复核清单`.
  8. Final verification no longer requires user confirmation to declare an in-scope Stage 5 deliverable complete; extra out-of-scope actions still need approval.

## High-accuracy review receipts

- Round 1 Momus (`ses_08bc3aff7ffeC9jYMRpYWvzhbi`): OKAY / APPROVE. Formal canonical-plan review succeeded after the plan file existed. No blocking issue.
- Round 1 Oracle (`ses_08b40d611ffezEZHH3KsyfetaU`): APPROVE_WITH_REQUIRED_FIXES. Required fixes:
  1. Clarify relative path root or use absolute paths for read-style QA invocations.
  2. Expand no-product-edit check from three named 《人生》 files to full-repo diff allowlist: only `.omo/evidence/ren-sheng-stage5-question-compression/` may change during execution.
  3. Make 五异法 category coverage an acceptance criterion in Todo 9 and final QA.
- Round 1 Oracle fixes integrated into plan:
  1. Verification strategy now declares project root `/home/king/github/growing-myself` for all relative paths and tells workers to prefix it when a tool requires absolute paths.
  2. Product-file integrity now uses full-repo `git diff --name-only` baseline and allows only `.omo/evidence/ren-sheng-stage5-question-compression/` as a worker-created execution path.
  3. Todo 1, Todo 13, and F4 now check full-repo diffs instead of only three named files.
  4. Todo 9, Todo 13, and Success criteria now require 五异法 five-category checklist with `材料不足` reasons when a category cannot be supported.

## High-accuracy review round 2 receipts

- Round 2 Momus (`ses_08b3cadaaffewlpOnJOpqj09L9`): OKAY / APPROVE. Confirmed Round 1 Oracle fixes integrated and found no blocking issue.
- Round 2 Oracle (`ses_08b3cad1bffeOsnszIH1e4X6rN`): APPROVE_WITH_REQUIRED_FIXES. Remaining hard issue: full-repo diff check used `git diff --name-only`, which misses untracked new files.
- Round 2 Oracle fixes integrated into plan:
  1. Product-file integrity now uses `git status --short --untracked-files=all` before and after execution, not `git diff --name-only` alone.
  2. Todo 1, Todo 13, and F4 now explicitly treat untracked files as new paths.
  3. Only worker-caused changed or untracked paths under `.omo/evidence/ren-sheng-stage5-question-compression/` are allowed during Stage 5 execution; any other new/changed/untracked path must be reverted or reported.

## High-accuracy review round 3 receipts

- Round 3 Momus (`ses_08b39dea9ffe4D6vy1TP9Kcn8I`): OKAY / APPROVE. This session initially paused after reading plan/draft because of API interruption; after continuation it returned a valid approval. No blockers.
- Round 3 Oracle (`ses_08b39dc70ffemIK4C9GgO5z0AO`): APPROVE. This session initially paused after reading plan/draft because of API interruption; after continuation it returned a valid approval. No blockers.
- Final high-accuracy status: PASS. Both final Momus and final Oracle approvals exist and are unconditional.
