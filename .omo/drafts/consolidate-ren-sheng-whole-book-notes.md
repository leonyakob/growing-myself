---
slug: consolidate-ren-sheng-whole-book-notes
status: review-freeze-candidate
intent: clear
review_required: true
pending-action: freeze current plan/draft bytes; run final Metis, Momus and Oracle on identical hashes; create external review seal without editing either file
approach: Preserve the existing four reading rounds as the archive base, build an internal evidence ledger outside the formal note, remove reader-facing technical metadata from the formal note, then append one whole-book consolidation section ordered as 阅读现场档案 → 文章素材索引 → 阅读轨迹与判断变化 → 待回看 / 归档不迁移. Only repair missing, duplicated, semantically wrong, or trajectory-worthy material; do not globally rerun Stage 3.
---

# Draft: consolidate-ren-sheng-whole-book-notes

## Components (topology ledger)

| id | outcome | status | evidence path |
|---|---|---|---|
| C1 | 全书内部整合台账覆盖四轮材料、来源关系、解释关系、归档去向与文章链接 | proposed | `.omo/evidence/ren-sheng-whole-book-consolidation-ledger.md` |
| C2 | 现有四轮卡片继续作为阅读现场档案底座；只补缺、建修订链、去读者可见技术字段，不重复搬运合格卡 | proposed | `路遥/人生/《人生》阅读笔记.md` + `.omo/evidence/ren-sheng-whole-book-archive-audit.md` |
| C3 | 建立六类全书文章素材索引，并全部使用可读卡片锚点、用户原句、张力、证据与缺口 | proposed | `路遥/人生/《人生》阅读笔记.md` + `.omo/evidence/ren-sheng-whole-book-index-audit.md` |
| C4 | 只收真正有价值的误读、犹豫、改判与判断变化，形成可核对的阅读轨迹 | proposed | `路遥/人生/《人生》阅读笔记.md` + `.omo/evidence/ren-sheng-whole-book-trajectory-audit.md` |
| C5 | external-only、弱重复、来源不足材料进入待回看或归档不迁移，不膨胀正式稿 | proposed | `.omo/evidence/ren-sheng-whole-book-consolidation-ledger.md` |
| C6 | 9 个 fixture case、7 个《人生》回归哨兵、结构顺序、技术字段、原文保护和 scope diff 全部通过 agent-executed QA | proposed | `.omo/evidence/final-ren-sheng-whole-book-consolidation-qa.md` |

## Findings (cited)

- `路遥/人生/《人生》中间整理稿.md:1-15009` 已完整读到 EOF；第4轮 001-132 的索引、卡片分级和外部读者补正汇总位于 `14733-15009`。
- `路遥/人生/《人生》阅读笔记.md:1-5930` 已完整读到 EOF；现有正式稿仍按四轮组织，轮次起点为 `3`、`557`、`1238`、`1701`，第4轮已经扩展为 15 张文章核心候选、67 张完整卡、人物主线、轻卡、主题素材和全局外部材料（`1701-5930`）。
- 只读确定性审计修正了早先的不完整计数：正式稿有 99 条无空格 `源ID/源IDs` 标题（含 1 条 `external-源ID` 重叠）、3 条有空格 `源 ID` 分组标题、4 条 `chapterUid/range` 行、2 条额外裸坐标轮次标题，共 108 条唯一 reader-facing 行；裸坐标共 6 条，其中 4 条与 metadata 行重叠。第四阶段规则明确这些只能进入内部台账，不得进入读者可见正文或文章 anchors：`路遥/人生/《人生》微信读书提示词-第四阶段-全书收束整合.md:87-125`。
- 中间稿可由固定 parser 枚举 266 个 canonical source units：R1=54、R2=52、R3=28、R4=132；正式稿可由固定 parser 枚举 165 张 baseline formal cards：R1=20、R2=31、R3=15、R4=99。
- 第四阶段要求先建内部台账，再处理阅读现场档案，最后处理文章索引；正式收束部分顺序固定为阅读现场档案、文章素材索引、阅读轨迹与判断变化、待回看/归档不迁移：同文件 `140-174`。
- 六类默认文章方向已经由规则确定：人物线、城乡主题、尊严主题、爱情线、知识分子困境、写法线索：同文件 `176-187`。
- 重复、同场景、改判和误读必须先分 `source relation`，再分 `interpretation relation`；不能按不同 source ID/range 机械拆卡：同文件 `189-229`。
- 外部读者材料必须从属于用户卡；external-only 强材料不能直接成为主证据；合格卡不因全书收束而再次复制：同文件 `231-242`。
- `.omo/evidence/fixtures/add-whole-book-consolidation-model.md:1-215` 已给出 9 个 deterministic case，覆盖部分迁移、重复、改判、同场景、早期误读、外部挑战、external-only、轻卡索引用法和正式稿防膨胀。
- 既有 `.omo/plans/add-whole-book-consolidation-model.md` 已完成第四阶段提示词与 fixture 建模；既有 `.omo/plans/revise-ren-sheng-round4-notes.md` 的 todos 已全部勾选，当前正式稿已是第4轮返工后的结果。本计划不得重复执行这两项已完成工作。
- Git 当前已有一项与本计划无关的预存修改：`.omo/run-continuation/ses_0a00ec516ffewmDIxM2zMRTrXV.json`。后续 worker 必须保留并排除它，不能覆盖、回滚、暂存或提交。

## Adopted defaults

| topic | adopted default | rationale |
|---|---|---|
| 全书结构落点 | 保留四轮正文作为阅读现场档案底座，在现有文末追加一个 `## 全书收束整合`；新部分按固定四段顺序组织 | 避免重写四轮档案，也符合“合格卡不重复搬运” |
| 技术字段 | 先在内部台账保留 source mapping，再按 108 行 exact before/after inventory 从读者可见正式稿清除 source ID/range/chapterUid/bookId/status/QA/interface 字段 | 完整审计已覆盖无空格、有空格、external 前缀、metadata 和坐标-only 五类，第四阶段规则明确禁止泄漏 |
| 卡片处理 | 已合格卡只建 readable anchor 和文章链接；仅对缺证据、重复、语义错误、改判链和应迁未迁材料局部处理 | 不全局重跑第三阶段，不重复洗稿 |
| 文章索引 | 固定六个顶层方向；每条写核心问题、可读锚点、用户原句、张力、可用证据、缺失证据，不复制整卡、不写文章草稿 | 规则已经给出确定表形 |
| 阅读轨迹 | 只保留能说明读法变化的误读/修正；普通主题文章默认使用修正后判断 | 避免机械罗列过程 |
| 外部读者材料 | 有用户锚点时才随卡或随索引使用；external-only 进入内部台账或待回看；同质材料留代表、相反且贴文本者并存 | 保护用户主体性并防膨胀 |
| 测试策略 | 无程序测试；采用 agent-executed 文档 QA、fixture dry-run、哨兵抽读、完整 read-back、精确禁用字段扫描和 Git scope/diff 检查 | 任务是 Markdown 内容整合，质量门必须验证内容而非只验证格式 |

## Planned execution shape

1. 冻结两份源材料，创建仅位于 `.omo/evidence/` 的全书内部整合台账；台账至少记录 Stage 4 规定的八类轴，不进入正式稿。
2. 以现有四轮正式卡为 archive base，逐项判定“合格只补索引 / 缺 readable evidence / 重复或修订链 / 尚未迁移 / external-only / 待回看”；先完成台账和 dry-run，不编辑正式稿。
3. 先形成正式稿候选 patch/evidence，机械移除 reader-facing 技术字段，并只补 Stage 4 需要的缺口；保留所有 `划线原文`、`我自己写的内容/我的原想法` 和必要外部原话，AI修正不得覆盖用户原文。
4. 在现有四轮档案之后追加 `## 全书收束整合`，先写阅读现场档案导航/补充，再写六类文章素材索引，再写有价值的阅读轨迹，最后写待回看/归档不迁移。
5. 逐项跑 9 个 fixture case；对 `ID 003`、`ID 006`、`ID 021`、`ID 109`、`ID 117`、`刘玉海救灾处`、`黄亚萍的物质付出` 做定点抽读，验证有无过度概括、错误合并、误删改判、轻卡强升、外部材料越权和技术字段泄漏。
6. 最终做完整 read-back、结构顺序检查、108 行技术字段归零、266-source/165-baseline-card 闭包、transformed-prefix 字节相等、baseline-relative scope audit；不 commit、不 push。

## Scope IN

- 未来执行时只修改正式阅读材料：`/home/king/github/growing-myself/路遥/人生/《人生》阅读笔记.md`。
- 规划、内部台账、候选 patch 和 QA 证据只写入 `.omo/`。
- 全书四轮现有卡片的 reader-facing metadata 清理、可读锚点建立、局部补证、重复/修订链处理。
- 六类文章素材索引、阅读轨迹与判断变化、待回看/归档不迁移。
- 9 个 fixture case 与 7 个《人生》回归哨兵验证。

## Scope OUT (Must NOT have)

- 不修改 `路遥/人生/《人生》中间整理稿.md`、任何提示词文件、fixture 原文件或其他书目。
- 不读取或导入 `路遥/平凡的世界/AGENTS.md`。
- 不重新调用微信读书接口，不抓取新材料。
- 不全局重跑第三阶段，不重写所有合格卡，不把四轮档案压成摘要或文章。
- 不把 `文章素材索引` 写成文章草稿，不复制整张卡，不用 source ID/range 作为锚点。
- 不强行升级轻卡，不把 external-only 内容伪装成用户判断，不用 AI修正覆盖用户原文。
- 不覆盖、回滚、暂存或提交预存 dirty-worktree 文件。
- 不 commit、不 push，除非用户在执行完成后另行明确要求。

## Open questions

None blocking. The requested endpoint, fixed section order, source files, formal target, six article directions, fixture model, regression sentinels, review requirement, and no-execution/no-Git boundaries are already explicit. Reversible implementation details use the defaults above.

## Approval gate

status: approved

Approval received from the user. This authorizes generation and review of `.omo/plans/consolidate-ren-sheng-whole-book-notes.md` only; execution and edits to reading materials remain unauthorized.

## Interruption recovery checkpoint

- API interruption classification: transport failure only; it is not a subagent output, verdict, approval, rejection, timeout verdict, or evidence.
- Main-plan generation: completed. Current plan remains 771 lines after runtime-state and validator-contract closure, with Phase 4 semantics, 266/165/108 baselines, collision-first Todo 0, target+evidence scope, execution/reviewer runtime state machines, phase-aware receipts, archive/prefix/suffix QA, review seal, HEAD/refs baseline, one controlled transient `/tmp` snapshot exception and three mutually exclusive invalidation classes.
- Source grounding: completed; both core materials were read to EOF before plan generation.
- User approval gate: completed; approval authorizes plan generation/review only.
- Session `ses_09b33977dffeKwhrnH765UkEF1`: completed Sisyphus-Junior session. It first performed the read-only Git check, then returned a gap review against the then-empty scaffold. It is not an actual Metis session and must not be recorded as a Metis receipt.
- Sisyphus gap result: completed and integrated. Its P0/P1 findings drove the preservation manifest, 001-132/R1-R3 ledger, unique readable anchors, fixture/sentinel tables, hard execution gate, dirty-worktree allowlist and content-preservation QA now present in the plan.
- Sisyphus deterministic baseline audit: completed in the reused session. It returned six exact reviewed hashes, the 108-line inventory, 266-source parser, 165-card parser and baseline-relative Git facts. Three malformed local Python attempts were explicitly discarded as no-result; the successful rerun is the only audit basis. No API/transport failure occurred in that subtask.
- Actual Metis first review: completed in `ses_09acc7715ffeYZUcbWUFwKzBGl` with verdict `BLOCKED`. It identified eight blockers: missing R1-R3 source closure; incomplete 103/105 technical baseline; impossible whole-candidate zero-token gate; insufficient source-side preservation proof; incomplete ledger enums/state matrix; nondeterministic card/hash/prefix preservation; missing planning-time hashes; and dirty-worktree scope conflict.
- Metis-fix revision: completed. The plan now covers 266 source units and 165 baseline cards, fixes the technical union at 108 exact rows, separates internal-before from target-after scans, adds source/target evidence checks and complete enums, fixes parser/hash/prefix grammar, pins six planning-time SHA-256 values, and uses NUL-safe baseline-relative Git scope checks with evidence-path collision handling.
- Failed patch classification: one large `apply_patch` attempt failed because its context did not match and changed no file. It is neither an applied revision nor any subagent output.
- First Metis re-review attempt: interrupted/no-result. The session read/hash audit completed, but the assistant message ended before any `APPROVED/BLOCKED` verdict. This is recorded only as an API/transport interruption and not as review evidence.
- Actual Metis second verdict: completed in the same session with `BLOCKED`. It explicitly confirmed all original eight blockers were closed, then found three new state-machine issues: `mapped-partial` could not legally carry an approved missing block into repair; `new-card` had no legal source-status path; and new cards with `article_links=none` could be omitted from the anchor map.
- Second Metis-fix revision: completed. The plan now separates current and modeled-post target-evidence states, permits only hunk-bound `missing-repair-approved`, adds `planned-new-formal` with future anchor/insertion requirements, validates all modeled-post evidence, and builds/rechecks anchors over `165 + N_new` cards regardless of article links.
- Actual Metis final re-review: completed in `ses_09acc7715ffeYZUcbWUFwKzBGl` with explicit `APPROVED`. It verified the hunk-bound mapped-partial path, planned-new-formal/new-card path, complete `165 + N_new` post-transform anchor model, all prior 266/165/108/hash/scope fixes, dependencies and success criteria. This is plan approval only, not execution authorization.
- Attempted dual-review dispatch classification: not a Momus or Oracle review. Both calls incorrectly reused the active Metis `task_id`; the first therefore continued Metis and returned `BLOCKED`, while the second was rejected by the active-session gate before a reviewer session started. Neither result may be recorded under Momus/Oracle.
- Latest Metis continuation verdict: `BLOCKED` with three issues: the plan had replaced rather than preserved Phase 4 semantic axes; Todo 3 said seven while listing eight reconciliation sets; approved brief C2 named an archive-audit path outside the hard allowlist.
- Third Metis-fix revision: completed. The 333-line plan now preserves the eight authoritative Phase 4 axes (`source status`, archive identity, evidence role, article links, trajectory flags, external relation, source relation and interpretation relation), separates workflow/topology/action, specifies primary-set exclusivity and secondary-tag overlaps for eight reconciliation sets, and adds `.omo/evidence/ren-sheng-whole-book-archive-audit.md` to Scope/Todo 8/final QA as the explicit C2 evidence.
- Momus high-accuracy review: not started; no Momus session exists to resume.
- Oracle independent review: not started; the rejected active-gate call created no Oracle verdict/session.
- Latest Metis semantic-axis re-review: completed with explicit `APPROVED` on the 333-line plan. It verified the eight authoritative axes, eight-set overlap model, C2 archive-audit production/verification and all previous 266/165/108/hash/repair/new-card/anchor/scope gates. This approval is plan-only.
- Repeated misroute classification: several attempted Momus/Oracle calls still carried the Metis task ID and therefore returned Metis metadata or active-gate rejection. None counts as Momus or Oracle review, regardless of text claiming otherwise.
- Actual Momus review: completed in the genuinely new session `ses_09a30aecdffePeDBjiZPFgPwm4` with `BLOCKED`. It independently confirmed hashes, 266/165/108, fixtures/sentinels and citations, then found two QA-executability blockers: Todos 0-10 lacked concrete validator/invocations, and F1-F5 lacked exact reviewer calls/steps/receipt paths.
- Momus-fix revision: completed. The current plan allowlists a standard-library validator, tests, byte-for-byte formal baseline and five review receipts; defines validator exit codes/subcommands/read-only mode; supplies exact commands/inputs/outputs/PASS conditions for every Todo; binds Todo 1 to `shared/programming` and tests; and gives F1-F5 exact fresh-Oracle calls, read-only steps, approval/no-result rules and independent evidence paths without circularly editing final QA.
- Actual Momus first re-review: completed in `ses_09a30aecdffePeDBjiZPFgPwm4` with `BLOCKED`. It confirmed the initial two QA gaps were substantially addressed, then found three contract contradictions: invocation JSON was being appended into verified inputs and Todo 0 lacked a standalone JSON/NUL-safe wrapper; Todo 8 prefix-check lacked ledger/formal-manifest/anchor inputs; F4 reapplied pre-transform logic to the final file and the immutable-wave repair rules conflicted.
- Second Momus-fix revision: completed. The current plan uses a separate allowlisted JSONL invocation receipt, an exact standalone Todo 0 collision/hash/NUL-safe/per-path wrapper, independent baseline copy, receipt-aware tests, complete Todo 8 inputs, `final-anchor-check` for the already transformed final note, and explicit wave IDs/input hashes/invalidation boundaries. Within an active wave only receipts may append; BLOCKED first ends/invalidates the wave, then fixes and a new five-session wave begin.
- Actual Momus second re-review: completed in `ses_09a30aecdffePeDBjiZPFgPwm4` with `BLOCKED`. It confirmed the independent JSONL, complete Todo 8 inputs, final-anchor-check and wave invalidation were substantially present, then found three remaining contracts: Todo 0 checked authorization/same-book rules before collision and could exit without JSON/preflight policy fields; append-only JSONL lacked latest-current-hash PASS semantics after red/retries; final-wave snapshot/receipt creation and per-prompt wave checks were not executable, and success wording crossed invalidated waves.
- Third Momus-fix revision: completed. Todo 0 now checks collision first with zero file output, then always writes PASS/STOPPED JSON/preflight including authorization, precedence, sibling attestation, same-book EOF disposition, hashes and Git baseline. Invocation JSONL now has attempt IDs, input/output hashes, supersession and latest-current-hash PASS selection. The validator now defines snapshot-create/check, review-receipt-append, wave-invalidate and final-anchor-check; every Oracle prompt carries literal wave ID/snapshot hash check; exact commands and fixed receipt mappings are given; invalidated waves are excluded from final success.
- Actual Momus third re-review: completed in `ses_09a30aecdffePeDBjiZPFgPwm4` with `BLOCKED`. It confirmed Todo 0/Todo 8/final-anchor/wave structure was largely closed, then found two remaining issues: latest-current-hash receipts could not survive legitimate formal-note phase changes and Todo 10 self-referenced the live JSONL; the reviewer append shell could delete the only serialized result and return success after append failure.
- Fourth Momus-fix revision: completed. Invocation records now use stable inputs plus named formal phases (`reviewed-baseline`, `cleaned-prefix`, `final-suffix-appended`) and an append-only receipt prefix/hash chain; Todo 10 binds to the pre-append JSONL prefix, and F2 verifies prefix-plus-record. Wave snapshots explicitly hash the invocation JSONL. Reviewer result handling now uses strict shell, validates append stdout and an independent receipt-check before deleting `/tmp`, preserves temp on failure, and atomically records wrong-agent/timeout/missing-final as NO_RESULT. Todo 0 also captures Git command return codes into its always-written post-collision JSON.
- Actual Momus fourth re-review first attempt: upstream WebSocket reset after file reads, with no final assistant verdict. Session read confirmed an empty final assistant turn; it is recorded only as API/transport NO RESULT.
- Actual Momus final retry: completed in the same real Momus session with explicit `APPROVED`. It verified stable-vs-phase inputs, baseline→cleaned-prefix→final-suffix chain, Todo 10 `receipt_prefix_sha256 + latest record`, invocation JSONL snapshot inclusion, strict receipt shell, independent receipt-check, temp retention and atomic NO_RESULT normalization. No new blocker remained.
- Attempted fresh Oracle classification: the call incorrectly carried the real Momus task ID, so metadata proves it was another Momus continuation, not Oracle. It returned `BLOCKED` on one valid issue: input drift made snapshot-check fail before receipt append, while regular invalidation required that impossible receipt, deadlocking the wave.
- Fifth Momus-fix revision: completed. The validator now has a no-receipt `wave-drift-invalidate` path that requires an intact ACTIVE snapshot plus proven expected/observed hash mismatch. The parent checks before every Oracle task and again before receipt append; pre-task drift skips review, post-task drift stores the serialized result as invalidated-wave context, atomically invalidates, and only then permits fixes/new wave. Non-drift BLOCKED still uses checked receipt plus regular invalidation.
- Actual Momus drift re-review: completed in `ses_09a30aecdffePeDBjiZPFgPwm4` with explicit `APPROVED`. It verified pre/post task snapshot checks, no-receipt drift invalidation prerequisites, serialized result retention, strict-shell temp handling, regular receipt-bound BLOCKED invalidation, NO_RESULT separation, phase-aware hash chain and final success rules. No new blocker remained.
- Misrouted Oracle attempts: calls carrying the Momus task ID correctly returned NO RESULT and are not Oracle receipts.
- Actual independent Oracle first review: completed in fresh session `ses_099d3f86bffeuM1a5jdQbUxSqm` with `BLOCKED`. It independently reproduced the six hashes and 266/165/108 facts, then found three control gaps: derived allowlist omitted the formal target; execution was not sealed to final plan/draft plus three approvals; F5 could not prove literal no-commit/no-push from status/diff alone.
- Oracle-fix revision: completed. Todo 0 now records `allowed_changed_paths = formal target + evidence` and treats any planned-output node type as collision. A separate post-review seal binds canonical payload, frozen plan/draft hashes and role-correct unconditional Metis/Momus/Oracle messages; Todo 0 validates it. Preflight/Todo 10/F5 now record and compare exact HEAD plus complete local refs; no-push remains an enforced prohibition rather than an unprovable post-state assertion.
- First frozen-byte Metis review: completed against the former 694-line plan/154-line draft with `BLOCKED`. It confirmed every other gate but proved fresh F1-F5 sessions create post-preflight `.omo/run-continuation/<session_id>.json` nodes that the strict target+evidence scope would reject. This was a genuine subagent verdict, not the later API interruption.
- Runtime-path fix revision: completed. Ordinary changed paths remain exactly target+evidence. Todo 0 separately binds the exact main execution session continuation path as identity/type-fixed but platform-mutable. Each fresh reviewer gets a pre-task `/tmp` runtime snapshot; post-task registration permits zero or one exact session-ID node, freezes child hash, binds runtime/result/receipt, and rejects any broad or extra path. Runtime ledger is excluded from immutable wave inputs but checked before every receipt and by F5; unauthenticated path drift is terminal and never deleted to fake cleanliness.
- API interruption classification: the most recent interruption happened in the main planning flow after runtime-path patches; no subagent was running or returned a verdict at that moment. It is neither Metis output nor any approval/rejection.
- Second frozen-byte Metis review: completed against the former 754-line plan/161-line draft with `BLOCKED`. It found three runtime-state contradictions: active-wave text allowed only receipt appends while runtime ledger had to append; zero-node NORESULT with empty session metadata could not register; execution-runtime could be absent at preflight but final check demanded literal type equality.
- Runtime-state fix revision: completed. Active wave now allows only current-wave receipts plus runtime ledger appends. Zero-node NORESULT always gets a nullable-path registration even with empty session ID; only a new node requires matching session metadata. Todo 0 records execution-runtime initial state/kind/hash, and runtime checks allow only absent→regular or regular→regular at the exact session path. All other states/types/paths remain forbidden.
- Third frozen-byte Metis review: completed against the former 771-line plan/166-line draft with unconditional `APPROVED` on hashes `175621...dfbd` and `7c4b59...1aedd`.
- Third frozen-byte Momus review: completed against those same bytes with `BLOCKED`. It found two validator-contract contradictions: persistent-output-only Scope wording rejected the required runtime snapshot `/tmp` file; `wave-drift-invalidate` claimed to be the sole no-receipt invalidator while runtime drift had a second legitimate no-receipt transition.
- Validator/invalidation fix revision: completed. `review-runtime-snapshot` now has the only strictly templated, exclusive-create, regular non-symlink `/tmp` exception with tests and cleanup/failure-retention rules. Invalidation is explicitly partitioned into INPUT_DRIFT, RUNTIME_PATH_DRIFT and receipt-bound reviewer BLOCKED; wrong class/proof fails, and active-wave snapshot mutation is limited to those terminal transitions.
- Freeze protocol restart: Momus BLOCKED invalidated the prior same-byte approval set. This draft update is the new last permitted plan/draft mutation. Metis, Momus and Oracle must read identical new bytes and unconditionally APPROVE; afterward only the external review seal may be created.
- Resume point: recompute stable hashes, obtain same-hash Metis/Momus/Oracle approvals, then create/validate the review seal. Any BLOCKED restarts the full frozen-byte review only after fixes.

## Review receipts

| reviewer | session | state | verdict / use |
|---|---|---|---|
| Sisyphus-Junior gap + baseline audit | `ses_09b33977dffeKwhrnH765UkEF1` | completed | blank-scaffold BLOCKED findings integrated; later read-only baseline facts integrated; not a Metis receipt |
| Metis first complete-plan review | `ses_09acc7715ffeYZUcbWUFwKzBGl` | completed | BLOCKED with eight actionable issues; all eight addressed in the current plan |
| Metis re-review attempt without verdict | `ses_09acc7715ffeYZUcbWUFwKzBGl` | interrupted/no-result | API/transport interruption only; neither approval nor rejection |
| Metis second explicit verdict | `ses_09acc7715ffeYZUcbWUFwKzBGl` | completed | BLOCKED with three state/anchor issues; all three addressed in the current plan |
| Metis final re-review | `ses_09acc7715ffeYZUcbWUFwKzBGl` | completed | APPROVED; plan-only approval, no execution authorization |
| Misrouted Momus prompt | `ses_09acc7715ffeYZUcbWUFwKzBGl` | completed as Metis | BLOCKED with three semantic/set/path issues; not a Momus receipt |
| Rejected Oracle prompt | no session | no-result | active gate rejected dispatch; not an Oracle receipt |
| Metis semantic-axis re-review | `ses_09acc7715ffeYZUcbWUFwKzBGl` | completed | APPROVED; plan-only approval, no execution authorization |
| Repeated misrouted reviewer prompts | Metis session / rejected active gate | invalid/no-result | never count as Momus or Oracle receipts |
| Actual Momus first review | `ses_09a30aecdffePeDBjiZPFgPwm4` | completed | BLOCKED with two QA invocation/receipt issues; both addressed in current plan |
| Actual Momus first re-review | `ses_09a30aecdffePeDBjiZPFgPwm4` | completed | BLOCKED with three receipt/prefix/final-wave contradictions; all addressed in current plan |
| Actual Momus second re-review | `ses_09a30aecdffePeDBjiZPFgPwm4` | completed | BLOCKED with three Todo0/JSONL/wave-chain issues; all addressed in current plan |
| Actual Momus third re-review | `ses_09a30aecdffePeDBjiZPFgPwm4` | completed | BLOCKED with two phase-hash/receipt-shell issues; both addressed in current plan |
| Actual Momus fourth-review attempt | `ses_09a30aecdffePeDBjiZPFgPwm4` | interrupted/no-result | upstream WebSocket reset; no verdict |
| Actual Momus final retry | `ses_09a30aecdffePeDBjiZPFgPwm4` | completed | APPROVED; unconditional plan approval only |
| Misrouted Oracle prompt | `ses_09a30aecdffePeDBjiZPFgPwm4` | completed as Momus | BLOCKED on input-drift deadlock; not an Oracle receipt; issue fixed |
| Actual Momus drift re-review | `ses_09a30aecdffePeDBjiZPFgPwm4` | completed | APPROVED; unconditional plan approval only |
| Actual independent Oracle first review | `ses_099d3f86bffeuM1a5jdQbUxSqm` | completed | BLOCKED with allowlist/seal/Git-proof issues; all addressed before freeze |
| Final frozen-byte Metis | pending fresh/continued review | pending | must APPROVE exact frozen plan/draft hashes |
| Final frozen-byte Momus | pending fresh/continued review | pending | must APPROVE exact same hashes |
| Final frozen-byte Oracle | reuse `ses_099d3f86bffeuM1a5jdQbUxSqm` | pending | must APPROVE exact same hashes |
| First frozen-byte Metis attempt | `ses_09acc7715ffeYZUcbWUFwKzBGl` | completed | BLOCKED on reviewer runtime-path scope closure; old freeze invalidated and issue fixed |
| Restarted final frozen-byte Metis | reuse `ses_09acc7715ffeYZUcbWUFwKzBGl` | pending | must approve new frozen hashes |
| Restarted final frozen-byte Momus | reuse `ses_09a30aecdffePeDBjiZPFgPwm4` | pending | must approve the same new hashes |
| Restarted final frozen-byte Oracle | reuse `ses_099d3f86bffeuM1a5jdQbUxSqm` | pending | must approve the same new hashes |
| Second frozen-byte Metis attempt | `ses_09acc7715ffeYZUcbWUFwKzBGl` | completed | BLOCKED on active append/zero-node NORESULT/execution-runtime transition; old freeze invalidated and issues fixed |
| Third final frozen-byte Metis | reuse `ses_09acc7715ffeYZUcbWUFwKzBGl` | pending | must approve latest frozen hashes |
| Third final frozen-byte Momus | reuse `ses_09a30aecdffePeDBjiZPFgPwm4` | pending | must approve same latest hashes |
| Third final frozen-byte Oracle | reuse `ses_099d3f86bffeuM1a5jdQbUxSqm` | pending | must approve same latest hashes |
| Third frozen-byte Metis result | `ses_09acc7715ffeYZUcbWUFwKzBGl` | completed | APPROVED on former hashes; superseded because Momus later BLOCKED |
| Third frozen-byte Momus result | `ses_09a30aecdffePeDBjiZPFgPwm4` | completed | BLOCKED on `/tmp` validator exception and invalidator taxonomy; issues fixed |
| Fourth final frozen-byte Metis | reuse `ses_09acc7715ffeYZUcbWUFwKzBGl` | pending | must approve new frozen hashes |
| Fourth final frozen-byte Momus | reuse `ses_09a30aecdffePeDBjiZPFgPwm4` | pending | must approve same new hashes |
| Fourth final frozen-byte Oracle | reuse `ses_099d3f86bffeuM1a5jdQbUxSqm` | pending | must approve same new hashes |
