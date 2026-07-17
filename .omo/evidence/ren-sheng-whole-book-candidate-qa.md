# Ren Sheng whole-book candidate QA

Status: PASS

## Reproducible Todo 7 QA matrix

| gate | status | evidence |
|---|---|---|
| preservation hashes | PASS | Formal reviewed baseline `7533aacd799479ad4a6a142c9509047a4c71157a02e799b9e2509b14fe4e9a11`; source/formal manifests parse to 266 source units and 165 formal cards. |
| Part A in-memory transforms | PASS | Applied 108 Part A target-after rows in memory; internal input hits: expected and confined to internal-before (108). |
| Part B repair/new-card fragments | PASS | part_b_fragments=0; zero bound repair/new-card fragments, so no hunk is required. |
| target-bound forbidden hits: 0 | PASS | Scanned Part A target-after, Part B target-after, and Part C for 源ID/chapterUid/bookId/range/coordinate/raw coordinate labels. |
| modeled-post card/anchor cardinality | PASS | 165 + N_new = 165; N_new=0; unresolved=[]; duplicate readable anchors: 0. |
| target-evidence relations | PASS | missing-unbound: 0; missing-repair-approved=0; planned-by-approved-insertion=0. |
| fixture/sentinel policy | PASS | nine fixture PASS (9) and seven sentinel PASS (7) parsed from fixture results. |
| article and trajectory topology | PASS | six article-row PASS (6) and six trajectory-chain PASS (6) verified through candidate and anchor map. |
| copied qualified card bodies | PASS | zero copied qualified card bodies (0); method scanned Part C for `> ` quote lines and card-body markers `**【划线原文】**`, `**【我自己写的内容】**`, `**【我的原想法】**`, `**【AI评价】**`, `**【AI修正】**`, `**【AI补充】**`. |

## Required acceptance fields

- internal input hits: expected and confined to internal-before
- target-bound forbidden hits: 0
- modeled-post card/anchor cardinality: 165 + N_new = 165
- missing-unbound: 0
- unresolved=[]
- duplicate readable anchors: 0
- nine fixture PASS: 9
- seven sentinel PASS: 7
- six article-row PASS: 6
- six trajectory-chain PASS: 6

## Copied-body excerpt check

- Part C is accepted only as whole-book index prose under `## 全书收束整合`, not copied card bodies.
- Excerpt-level negative evidence for a read-only reviewer: the forbidden card-body openers searched were exactly `> `, `**【划线原文】**`, `**【我自己写的内容】**`, `**【我的原想法】**`, `**【AI评价】**`, `**【AI修正】**`, and `**【AI补充】**`; all produced 0 hits in Part C.
