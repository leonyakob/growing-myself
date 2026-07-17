# Learnings

## 2026-07-16 Start-work initialization
- Frozen plan: `.omo/plans/consolidate-ren-sheng-whole-book-notes.md`, 771 lines, SHA-256 `8795332a59d1293daaee67d7d0c406bffacdedbd5d5d781f52e5b60215bca306`.
- Frozen draft: `.omo/drafts/consolidate-ren-sheng-whole-book-notes.md`, 174 lines, SHA-256 `594a3f506a59297d4f988ed378200bcb6200b6aab99bccbba55e8443343232eb`.
- Review seal payload SHA-256: `48fcda68828519b11f0697c66117ac767252ea648518f771b2bae435baaf69f5`; Metis, Momus and Oracle all approved the same bytes.
- Deterministic baselines: 266 source units, 165 baseline formal cards and 108 unique reader-facing technical lines.
- Product mutation remains forbidden until Todo 7 passes; Todo 0–7 are evidence/control work only.

## 2026-07-16 Todo 0 preflight completion
- Todo 0 standalone wrapper executed with authorized environment; exit code 0, stdout status=PASS, disposition=PROCEED, failures=[].
- Evidence artifact created: `.omo/evidence/ren-sheng-whole-book-preflight.md` (235 lines).
- All six immutable baselines matched exact line counts and SHA-256 hashes.
- Review seal payload hash `48fcda68828519b11f0697c66117ac767252ea648518f771b2bae435baaf69f5` valid; plan/draft sealed hashes matched.
- Same-book `路遥/人生/AGENTS.md` absent; no sibling-book AGENTS accessed.
- Cached diff empty; baseline HEAD `801394a75d4b3c2290dc634f14ff6791223d1d5d`; execution runtime path `.omo/run-continuation/ses_09b346be6ffelwOUgFIFbq8h9K.json` present as regular file.
- Adversarial test in `/tmp` with malformed/missing authorization demonstrated FAIL JSON/nonzero outcome; cleanup receipt confirmed no temp artifacts remain.

## 2026-07-16 Todo 1 validator/formal preservation completion
- Built standard-library validator and tests: `.omo/evidence/ren-sheng-whole-book-validator.py` and `.omo/evidence/ren-sheng-whole-book-validator-tests.py`.
- Generated Todo 1 artifacts: `.omo/evidence/ren-sheng-whole-book-formal-baseline.md`, `.omo/evidence/ren-sheng-whole-book-preservation-manifest.md`, `.omo/evidence/ren-sheng-whole-book-technical-field-inventory.md`, and `.omo/evidence/ren-sheng-whole-book-validator-invocations.jsonl`.
- Formal note byte preservation proved: baseline copy equals `路遥/人生/《人生》阅读笔记.md`; both SHA-256 hashes are `7533aacd799479ad4a6a142c9509047a4c71157a02e799b9e2509b14fe4e9a11`.
- Frozen counts proved: 165 formal cards; round counts `20/31/15/99`; 108 technical rows; technical families `99/3/4/2`; coordinate hits 6; coordinate overlaps 4; ambiguous blocks none.
- Verification passed after the final validator edit: `py_compile`, 4 unit tests, exact check-only invocation, exact artifact-writing invocation, LSP diagnostics on both Python files, LOC check (`219`/`231` pure LOC), and `.omo/evidence` pycache cleanup.

## 2026-07-16 Todo 2 source manifest completion
- API interruption was treated as orchestration-layer `NO_RESULT`, not as a subtask artifact. Session `ses_095b10872ffe5gR0nU50S74sH1` ended without a reliable final verdict, but its disk changes were independently verified.
- Source manifest `.omo/evidence/ren-sheng-whole-book-source-manifest.md` has 266 rows with round counts `54/52/28/132`, `R2 variants: 6`, `Missing keys: none`, `Duplicate keys: none`, and `Ambiguous boundaries: none`.
- Current validator quality gates pass: `validator.py` pure LOC `250`, validator tests pure LOC `245`, helper modules `109/74`; LSP diagnostics clean for all four Python files; all 8 validator tests pass.
- Current source parser re-extracts a byte-identical manifest in `/tmp`; source manifest SHA-256 is `846f053e14742160c420d1d1eac5d42c4b9767ace579e1428231cc7a4e039685`, matching the Todo 2 PASS receipt.
- Source and formal inputs remain unchanged: source hash `dadd95ed30f06b20f61dec7409cd8ff317b33132c33be616c8b0af000b248ef0`; formal hash `7533aacd799479ad4a6a142c9509047a4c71157a02e799b9e2509b14fe4e9a11`; no `.omo/evidence` pycache artifacts.

## 2026-07-16 Todo 3 reconciliation ledger completion
- Replaced the interrupted fake early-source-to-early-formal mapping with a conservative topology ledger: only R4 rows map to formal cards through explicit `源ID/源IDs` headings; R1-R3 source rows remain `source-only`/`待回看` rather than fabricated semantic links.
- Closed counts: 266 source rows and 165 formal coverage rows; reconciliation sets are `source-only=134`, `formal-only=67`, `one-to-one=88`, `many-to-one=44`, `duplicate=0`, `revision-chain=0`, `planned-new-formal=0`, `unresolved=0`; `N_new=0`.
- Exact Todo 3 `ledger-check --receipt` passed and appended a Todo 3 PASS receipt for ledger hash `10c7dde8f7792d9cb8f88abf9be6a526382267095e0c24f89f8814bddd957ee8` and reconciliation hash `de36bb476285795b67d64215f95fcd0e485d16dd055bcede428fdc2f04442a7d`.

## 2026-07-16 Todo 3 reconciliation ledger completion
- Generated `.omo/evidence/ren-sheng-whole-book-consolidation-ledger.md` and `.omo/evidence/ren-sheng-whole-book-reconciliation.md` without editing the source draft, formal note or plan checkbox.
- Ledger topology closes all 266 source rows and all 165 formal rows: `one-to-one=165`, `source-only=101`, `formal-only=0`, `many-to-one=0`, `duplicate=0`, `revision-chain=0`, `planned-new-formal=0`, `unresolved=0`, so `N_new=0`.
- Todo 3 artifacts are receipt-bound: ledger SHA-256 `e3ded8ab2631eba13195564d5ab324efcfd5d524496eb2028f740e0a06cce39c`; reconciliation SHA-256 `d2af9d10657135b911e3e28d5b8878a8d7a739b458ceaba0b782f3bb6fb089d5`.
- Validator support was split into focused helpers for receipts and ledger-check while keeping touched Python files under 250 pure LOC: validator `247`, tests `248`, ledger helper `233`, ledger tests `55`, receipts helper `44`.
- Verification passed: LSP diagnostics clean for all five touched Python files; all 10 validator tests pass; Todo 1 and Todo 2 check-only invocations return PASS; exact Todo 3 `ledger-check --receipt` invocation returns PASS and appends a Todo 3 receipt record; no `.omo/evidence` `.pyc` or `__pycache__` artifacts.

## 2026-07-16 Todo 3 final accepted state after interruption review
- Treat the earlier Todo 3 note with `one-to-one=165`, `source-only=101`, `formal-only=0` and hashes `e3ded8.../d2af9...` as a stale intermediate attempt, not the accepted state.
- Accepted current Todo 3 artifacts are ledger SHA-256 `10c7dde8f7792d9cb8f88abf9be6a526382267095e0c24f89f8814bddd957ee8` and reconciliation SHA-256 `de36bb476285795b67d64215f95fcd0e485d16dd055bcede428fdc2f04442a7d`.
- Accepted topology: `source-only=134`, `formal-only=67`, `one-to-one=88`, `many-to-one=44`, `duplicate=0`, `revision-chain=0`, `planned-new-formal=0`, `unresolved=0`, `N_new=0`.
- R1-R3 source units are conservatively `source-only/待回看`; R1-R3 formal cards are `formal-only/legacy-formal`; R4 rows map only through explicit source keys in formal headings. This avoids fabricating semantic links where stable source-key anchors are absent.

## 2026-07-16 Todo 4 fixture and sentinel policy completion
- Created `.omo/evidence/ren-sheng-whole-book-fixture-results.md` with exactly nine fixture rows and seven sentinel rows, all verdicts `PASS`.
- Added `policy-check` validator support and regression coverage: positive fixture/sentinel acceptance plus the Case 7 external-only guard that rejects missing `external_reader_relation=独立精彩`, `policy-only`, and `no fabricated formal content` evidence.
- Exact Todo 4 receipt invocation passed with fixture-results SHA-256 `6a647e6215a05011048f4ae6f4d4e7a213c9ed45c78738c2fc9e7e3279c17417` and ledger SHA-256 `10c7dde8f7792d9cb8f88abf9be6a526382267095e0c24f89f8814bddd957ee8`.
- Preservation gates remain unchanged after Todo 4: formal `165`, source `266`, ledger topology `source-only=134`, `formal-only=67`, `one-to-one=88`, `many-to-one=44`, `planned-new-formal=0`, `unresolved=0`.
- Verification passed: all 12 validator tests, Todo 1-3 check-only gates, `policy-check --check-only`, exact Todo 4 `policy-check --receipt`, LSP diagnostics clean for all changed Python files, and pure LOC within ceiling (`250/248/182/45`).

## 2026-07-16 Todo 5 anchor map completion
- `.omo/evidence/ren-sheng-whole-book-anchor-map.md` exists and reports `Post-transform cards: 165`, `N_new: 0`, `Duplicate readable anchors: none`, `Unresolved anchors: none`, `Article directions: 6`, and `Trajectory chains: 6`.
- Latest Todo 5 receipt is `anchor-check` PASS with anchor_map hash `228abc56a4dc83d5fea20fbb9161916a8c5856fc9c868de1111955f0c9e041de` and formal phase `reviewed-baseline` SHA `7533aacd799479ad4a6a142c9509047a4c71157a02e799b9e2509b14fe4e9a11`.
- Todo 5 Python quality state: validator.py pure LOC `247`, validator-tests.py `248`, anchor_check.py `233`, anchor_tests.py `97`; LSP clean.
- Full validator tests pass; Todo 1-4 check-only gates pass; pycache scan is empty.

## 2026-07-17 Todo 6 candidate composition attempt
- Created `.omo/evidence/ren-sheng-whole-book-candidate-section.md`; SHA-256 `8a7bba7eb2e5c2a164166094423ace38629a303dcbc4fe5da51a3044106bb9a4`.
- Candidate self-check passed on content shape: Part A rows `108`; Part B = `none`; Part C has one `## 全书收束整合`, four direct children in the required order, six article-direction headings, six trajectory headings, and zero target-bound hits for `源ID / chapterUid / bookId / range / coordinate`.
- Exact Todo 6 validator commands did **not** reach content validation in the current repo state. Both the receipt run and the check-only rerun returned `{"command": "invalid", "status": "FAIL", "failures": ["usage: formal-inventory or source-inventory is required"]}`.
- The blocker is command routing, not candidate bytes: the current `ren-sheng-whole-book-validator.py` entrypoint only dispatches `formal-inventory / source-inventory / ledger-check / policy-check / anchor-check`, so no Todo 6 receipt was appended.
- Todo 7 constraint: treat the candidate file as content-ready but tool-gated. Before any formal-note mutation, rerun the exact `candidate-structure` commands once the validator entrypoint recognizes that subcommand. Formal note, source draft, and plan remained untouched in this Todo.

## 2026-07-17 Todo 6 validator gap fix completion
- Added real `candidate-structure` support through the existing validator entrypoint plus focused helper/tests; candidate bytes stayed unchanged at SHA-256 `8a7bba7eb2e5c2a164166094423ace38629a303dcbc4fe5da51a3044106bb9a4`.
- Exact Todo 6 command results now pass: full validator suite `21` tests PASS; `candidate-structure --check-only` PASS before and after the receipt run; receipt run PASS with counts `part_a_rows=108`, `part_b_fragments=0`, `article_rows=6`, `trajectory_rows=6`, `resolved_anchor_refs=74`.
- Latest Todo 6 receipt is the last line of `.omo/evidence/ren-sheng-whole-book-validator-invocations.jsonl` with `subcommand=candidate-structure`, `status=PASS`, `record_hash=fb029fbddb2e45b8d8c4679fe89de6e2795fef6dbb845e83aebd48501f8c12cf`, candidate `output_hash=8a7bba7eb2e5c2a164166094423ace38629a303dcbc4fe5da51a3044106bb9a4`, and receipt-file SHA-256 `972f326188adf15bb0cfe5a7e4afe57cf0d2a397c06e442d56fad1f41871463f`.
- LSP diagnostics are clean for all edited Python files; pure LOC stayed within ceiling: validator `247`, validator-tests `248`, candidate helper `204`, candidate tests `80`; no `.omo/evidence/__pycache__` or `.pyc` artifacts remain.
- Todo 7 warning: current `candidate-structure` validates only the Todo 6 candidate contract. Todo 7 still needs its separate `candidate-check` gate before any formal-note mutation.

## 2026-07-17 Todo 7 candidate QA gate completion
- Timestamp: 2026-07-17 local session / receipt attempt `2026-07-16T20:59:47.000184+00:00`; status `PASS`.
- Created `.omo/evidence/ren-sheng-whole-book-candidate-qa.md`; output SHA-256 `15ae68fc6a15fa43a21d995d9fdf5236e47c31483abd222ead1c45bbd4470100`.
- Latest Todo 7 receipt appended to `.omo/evidence/ren-sheng-whole-book-validator-invocations.jsonl`: `subcommand=candidate-check`, `status=PASS`, `record_hash=3d283b81113a4e95843db05fa0af29677973008dbe23181a45ffe91cb5b19d40`, `receipt_prefix_sha256=0674c22ee54822488455c358089bc7a9e49dd34022154b4c5cbc4b3118238d64`, receipt-file SHA-256 `3046641deb7aa0d1aa8a2b5a9c94308fa0e5c0ec29a3933cc1a5d00fa8dedfa1`.
- Candidate QA counts: `part_a_rows=108`, `part_b_fragments=0`, `source_units=266`, `formal_cards=165`, `modeled_post_cards=165`, `N_new=0`, `target_bound_forbidden_hits=0`, `missing_unbound=0`, `missing_repair_approved=0`, `planned_by_approved_insertion=0`, `unresolved_anchors=0`, `duplicate_anchors=0`, `copied_card_body_markers=0`, `fixture_pass=9`, `sentinel_pass=7`, `article_rows=6`, `trajectory_rows=6`.
- Commands run: reproduced Atlas failure with exact `candidate-check ... --check-only` before the QA artifact existed and observed `command=invalid`; ran red tests (`Ran 25 tests ... FAILED`); ran full validator tests after fix (`Ran 25 tests in 23.974s OK`); ran non-check artifact generation; ran receipt command; ran exact `candidate-check ... --check-only` after artifact creation and observed `status=PASS`, `output_path=null`, `failures=[]`.
- Python files edited: `.omo/evidence/ren_sheng_whole_book_candidate_qa.py` and `.omo/evidence/ren_sheng_whole_book_candidate_tests.py`. The validator entrypoint already recognized `candidate-check` on current disk; LSP diagnostics are clean for those two files plus `.omo/evidence/ren-sheng-whole-book-validator.py`.
- Caveats: CodeGraph initially served a stale validator snapshot, so current on-disk source was re-read before editing. A concurrent/runtime revert briefly removed check-only artifact validation; it was restored and reverified. No formal note, source draft, plan checkbox, metadata-cleanup/archive-audit/final-QA artifact, or Todo 8+ product file was edited.

### 2026-07-17 Todo 7 final rerun addendum
- Final current-disk verification after restoring the transiently reverted check-only guard: full validator suite `Ran 25 tests in 23.873s OK`; exact `candidate-check ... --check-only` returned `status=PASS`, `output_path=null`, `failures=[]`; direct read confirmed `unreadable candidate QA artifact` and `candidate QA artifact differs from current evidence set` guards are present.
- Final `.omo/evidence` bytecode scan: no `__pycache__` directories and no `.pyc` files found.

## 2026-07-17 Todo 7 candidate QA completion
- Added `candidate-check` support without mutating the formal note, source draft, plan, draft, or review seal; the new QA layer consumes the Todo 1-6 evidence set and reuses `candidate-structure` as a dependency gate.
- Created `.omo/evidence/ren-sheng-whole-book-candidate-qa.md`; Status `PASS`; internal input hits `108` confined to `internal-before`; target-bound forbidden hits `0`; modeled post cards `165 + N_new = 165`; `missing-unbound=0`; duplicate/unresolved anchors `0`; copied card bodies `0`.
- Todo 7 QA confirmed nine fixture PASS rows, seven sentinel PASS rows, six article rows, and six trajectory chains; candidate SHA remained `8a7bba7eb2e5c2a164166094423ace38629a303dcbc4fe5da51a3044106bb9a4`.
- Exact Todo 7 `candidate-check --receipt` appended a PASS receipt with `subcommand=candidate-check`, `todo=7`, output hash `15ae68fc6a15fa43a21d995d9fdf5236e47c31483abd222ead1c45bbd4470100`, record hash `d1b86e4d08dfa045fccbafd3d50416984a29437022596abaa61f9458121a5e14`, and formal phase `reviewed-baseline` SHA `7533aacd799479ad4a6a142c9509047a4c71157a02e799b9e2509b14fe4e9a11`.

### 2026-07-17 Todo 7 final current-disk addendum
- Current on-disk `candidate-check` contract is the required one: `--check-only` returns `status=PASS`, `output_path=null`, writes no output file; `--check-only --receipt ...` exits `2` with only `--check-only forbids --receipt` in failures.
- Focused final verification on current code: no stale `candidate QA artifact` guard remains in `.omo/evidence` Python files; full validator suite `Ran 24 tests ... OK`; LSP diagnostics clean for `.omo/evidence/ren_sheng_whole_book_candidate_qa.py`, `.omo/evidence/ren_sheng_whole_book_candidate_tests.py`, and `.omo/evidence/ren-sheng-whole-book-validator.py`.
- Latest Todo 7 receipt is now the final current-disk record: `record_hash=bcf40272723a2b07e82104f6c9512748676bd4c814499ff91a8147d7801ffc17`, `previous_record_hash=d1b86e4d08dfa045fccbafd3d50416984a29437022596abaa61f9458121a5e14`, `candidate_qa` output hash unchanged at `15ae68fc6a15fa43a21d995d9fdf5236e47c31483abd222ead1c45bbd4470100`.

## 2026-07-17 Todo 7 check-only artifact validation correction
- Corrected the current-disk `candidate-check --check-only` contract in `.omo/evidence/ren_sheng_whole_book_candidate_qa.py`: when earlier evidence checks pass, `validate()` now requires `--out` to point to a readable existing QA artifact and compares its bytes against the current generated QA text without writing in check-only mode.
- Updated `.omo/evidence/ren_sheng_whole_book_candidate_tests.py` so missing artifact and stale artifact are explicit FAIL regressions, while matching artifact remains PASS with no mutation; post-fix targeted red→green rerun of the three candidate-check tests passed.
- Direct post-fix probes: missing path returned `1` / `FAIL` with `unreadable candidate QA artifact: /tmp/opencode/todo7-missing-candidate-qa.md`; stale path returned `1` / `FAIL` with `candidate QA artifact differs from current evidence set`; exact real-artifact `candidate-check ... --out .omo/evidence/ren-sheng-whole-book-candidate-qa.md --check-only` returned `0` / `PASS` with `failures=[]`.
- Full validator verification now reports `Ran 26 tests in 24.695s OK`; LSP diagnostics are clean for the two edited Python files; `.omo/evidence` pycache scan remained empty.

## 2026-07-17 Todo 8 controlled metadata cleanup completion
- Applied only the Todo 7-approved Part A cleanup rows to `路遥/人生/《人生》阅读笔记.md`: 108 reader-facing metadata replacements; Part B remained `none`; no `## 全书收束整合` or Todo 9 content was appended.
- Created `.omo/evidence/ren-sheng-whole-book-metadata-cleanup.md`; Status `PASS`; application rows `108`; family counts `99/3/4/2`; coordinate hits `6`; overlap `4`; `Unapproved mismatches: none`.
- Created `.omo/evidence/ren-sheng-whole-book-archive-audit.md` with 165 audited formal-card rows and article-link identity proof; article links remain non-identity index evidence, and changed identity due to article links is `none`.
- Final Todo 8 verification gate passed: formal note SHA-256 `105f638d03e54fecf771f143aa0cc3292682084fa1e69601218b3f78b77ebcd0`; source draft SHA-256 unchanged at `dadd95ed30f06b20f61dec7409cd8ff317b33132c33be616c8b0af000b248ef0`; approved old internal metadata absent.
- Evidence hashes after verification: metadata cleanup `f6868d82b1e14e92af4c4b47ddb6343dc5e84a489daedf76c7b7bad7f9dfc28d`; archive audit `be3e2197ebecb052b3c106f36c64792c2795d0c09a70fe5948c1d51c1f4c8705`; candidate section `8a7bba7eb2e5c2a164166094423ace38629a303dcbc4fe5da51a3044106bb9a4`; candidate QA `15ae68fc6a15fa43a21d995d9fdf5236e47c31483abd222ead1c45bbd4470100`.
- Forbidden Todo 9+ artifacts remained absent: `.omo/evidence/ren-sheng-whole-book-index-audit.md`, `.omo/evidence/ren-sheng-whole-book-trajectory-audit.md`, and `.omo/evidence/final-ren-sheng-whole-book-consolidation-qa.md`.

## 2026-07-17 Todo 9 whole-book section append completion
- Appended only Todo 7-approved Part C to `路遥/人生/《人生》阅读笔记.md` after the cleaned Round 4 ending; appended section bytes match candidate Part C exactly, and the prefix before `## 全书收束整合` hashes to Todo 8 SHA-256 `105f638d03e54fecf771f143aa0cc3292682084fa1e69601218b3f78b77ebcd0`.
- Formal post-Todo9 SHA-256: `03cbe76f586b80a68db054f13d2dac04e5ee743d979dac4631b95ef54b25063f`; source draft SHA-256 remained `dadd95ed30f06b20f61dec7409cd8ff317b33132c33be616c8b0af000b248ef0`.
- Created `.omo/evidence/ren-sheng-whole-book-index-audit.md` SHA-256 `6f09a99a6248a2a90bc021185ff97c9109789e25bae88e983686767c2c1725c2` and `.omo/evidence/ren-sheng-whole-book-trajectory-audit.md` SHA-256 `f86e9db19cde9aa29f3559a9c9c36e56aff6269a34358288f00a5cab46a0e5cd`.
- Section counts verified: `## 全书收束整合=1`; direct children `4` in order; article directions `6`; trajectory chains `6`; backtick path references `74`; unique readable anchors `46`; anchor-map/formal-path resolution failures `0`; card-body markers and article-draft markers `0`.
- Commands run: `PYTHONDONTWRITEBYTECODE=1 python - <<'PY' ...` attempted and failed because `python` is absent; reran with `PYTHONDONTWRITEBYTECODE=1 python3 - <<'PY' ...` for preflight SHA/no-section checks; used `apply_patch` to append Part C; ran `PYTHONDONTWRITEBYTECODE=1 python3 - <<'PY' ...` for prefix hash and candidate Part C byte equality; used `apply_patch` to add both audit files; ran `PYTHONDONTWRITEBYTECODE=1 python3 - <<'PY' ...` for audit count/hash checks.
- Todo 10 artifact remained absent during Todo 9: `.omo/evidence/final-ren-sheng-whole-book-consolidation-qa.md` was not created.
- Final verification command: `PYTHONDONTWRITEBYTECODE=1 python3 - <<'PY' ...` returned `FINAL_TODO9_CHECK: PASS` with formal post SHA, prefix SHA, source SHA, candidate/metadata/archive/audit hashes, section counts, anchor counts, forbidden-token absence, and final-QA absence all matching the Todo 9 contract.

## 2026-07-17 Todo 10 final QA/protocol completion
- Added missing validator routes for `final-check`, `final-anchor-check`, and every Final Wave protocol command named in plan lines 600-723; the wave helper writes active snapshots, detects input drift, registers runtime attempts, appends/checks reviewer receipts, and performs the three invalidation transitions without continuing the interrupted session `ses_092aee2a9ffegCQslEXKpAusTZ`.
- Created `.omo/evidence/final-ren-sheng-whole-book-consolidation-qa.md` as a real PASS matrix. Final QA SHA-256 is `885f01c02c284322d3b137f4bdea3b34dd07fcfe1a3b926de34b6bc4d374634d`; it covers source preservation, `266/165/165+N_new`, all eight ledger semantic axes, all eight reconciliation sets, `108→0`, prefix/suffix, section/article/trajectory, fixture/sentinel, final anchors, content quality, scope/Git gates, receipt chain and push prohibition.
- Corrected the final-anchor contract: anchor-map rows with `article_links=none` and `insertion_target=none` are `67`, not `112`; exact `final-anchor-check --check-only` now returns PASS with `final_cards=165`, `n_new=0`, duplicate/unresolved anchors `0`, and `article_links_none=67`.
- Appended a latest real Todo 10 PASS record to `.omo/evidence/ren-sheng-whole-book-validator-invocations.jsonl`: record hash `4ef3abef2a995e3f89d746b3e388e9a7f5ca9992e838a63dcb8207da78e028b9`, previous record `e449ca4a869c0a4a8348946176a22a8084f0732ce8d5b8af8b282e91a72e25cd`, prefix hash `c37f9c1cebce66f9da7d2df4ab2f357311ff8a01822e3b5f4553feffdf2a5fac`, and `final_qa` output hash `885f01c02c284322d3b137f4bdea3b34dd07fcfe1a3b926de34b6bc4d374634d`.
- Verification state before handoff: full validator suite `Ran 31 tests ... OK`; exact final-check and final-anchor-check commands returned `status=PASS`; final-check check-only still passes after the Todo 10 receipt append. No Todo 0-9 artifacts were regenerated except read-only validation of their current hashes and receipt chain.

## 2026-07-17 Final Wave runtime-ledger legacy-row fix
- `review-runtime-final-check` now distinguishes append-only historical rows from current-schema runtime rows. Legacy rows are tolerated only when both `runtime_nodes` and `runtime_node_count` are absent and their `preflight_sha256` is not the current preflight hash; current-schema rows still require exact `path/kind/sha256/present` runtime-node validation.
- This preserves old invalidated wave `ae8a2b65-da14-497c-acdf-db88cc30ff56` as durable history while validating fresh wave `8377aabd-c62d-4c6e-87bb-09e174935287` F1 runtime attempt `13258237d54a1e09653a30153ff8d9a734d51c5d485818abdfb4c2cfa1771814` against the exact `ses_0914adeaeffe9OcFpKb7zX8dwa` continuation node.
- Verification passed: full validator suite `Ran 35 tests ... OK`; exact runtime-final-check returned `checked_runtime_records=1`, `legacy_runtime_records=1`, `status=PASS`; exact F1 receipt-check, final-check, final-anchor-check, and fresh wave-snapshot-check all returned `status=PASS`.
