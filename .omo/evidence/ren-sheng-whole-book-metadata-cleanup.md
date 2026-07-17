# Ren Sheng whole-book metadata cleanup

Status: PASS

## Scope gate

- Todo 7 QA artifact: `.omo/evidence/ren-sheng-whole-book-candidate-qa.md`; status field read as `PASS`.
- Part A rows applied: 108.
- Part B repair/new-card fragments: none; applied fragments: 0.
- Todo 9 section `## 全书收束整合`: not appended.

## Hashes and modeled-post proof

- Formal reviewed baseline SHA-256: `7533aacd799479ad4a6a142c9509047a4c71157a02e799b9e2509b14fe4e9a11`.
- Formal post-cleanup SHA-256: `105f638d03e54fecf771f143aa0cc3292682084fa1e69601218b3f78b77ebcd0`.
- Source draft SHA-256: `dadd95ed30f06b20f61dec7409cd8ff317b33132c33be616c8b0af000b248ef0`; expected immutable source hash preserved.
- Modeled post SHA-256: `105f638d03e54fecf771f143aa0cc3292682084fa1e69601218b3f78b77ebcd0`.
- Modeled-post equality: `True`. Current formal note equals Todo 1 baseline after exactly the 108 Part A replacements, so unaffected bytes and Round 1-4 order are preserved.
- Prefix/no-append confirmation: modeled post contains no `## 全书收束整合`; current formal note contains no `## 全书收束整合`.

## Counts

- Technical inventory family counts: `source_id=99 / spaced_source_id=3 / metadata=4 / coordinate_only=2` (`99/3/4/2`).
- Coordinate hits: `6`.
- Coordinate overlaps: `4`.
- Baseline-card checks: `165` preservation rows and `165` anchor rows; expected post-transform cards `165`, `N_new=0`.
- Applied-row pre-transform single-hit checks: `108/108`.
- Old internal-before post-cleanup hits: `0`.

## Target-surface forbidden token scan

| pattern | hits |
|---|---:|
| 源ID | 0 |
| 源IDs | 0 |
| external-源ID | 0 |
| chapterUid | 0 |
| bookId | 0 |
| raw range= | 0 |
| coordinate residue | 0 |

Total target-surface hits: `0`.

## Application ledger

| row | families | application_count | internal-before post hits | target-after present at modeled replacement | note |
|---:|---|---:|---:|---|---|
| 5 | range, coordinate, chapterUid | 1 | 0 | yes | ok |
| 557 | coordinate | 1 | 0 | yes | ok |
| 559 | range, coordinate, chapterUid | 1 | 0 | yes | ok |
| 1238 | coordinate | 1 | 0 | yes | ok |
| 1240 | range, coordinate, chapterUid | 1 | 0 | yes | ok |
| 1704 | 源ID | 1 | 0 | yes | ok |
| 1742 | 源ID | 1 | 0 | yes | ok |
| 1784 | 源ID | 1 | 0 | yes | ok |
| 1825 | 源ID | 1 | 0 | yes | ok |
| 1866 | 源ID | 1 | 0 | yes | ok |
| 1909 | 源ID | 1 | 0 | yes | ok |
| 1948 | 源ID | 1 | 0 | yes | ok |
| 1987 | 源ID | 1 | 0 | yes | ok |
| 2024 | 源ID | 1 | 0 | yes | ok |
| 2061 | 源ID | 1 | 0 | yes | ok |
| 2098 | 源ID | 1 | 0 | yes | ok |
| 2139 | 源ID | 1 | 0 | yes | ok |
| 2182 | 源ID | 1 | 0 | yes | ok |
| 2220 | 源ID | 1 | 0 | yes | ok |
| 2257 | 源ID | 1 | 0 | yes | ok |
| 2296 | 源ID | 1 | 0 | yes | ok |
| 2333 | 源ID | 1 | 0 | yes | ok |
| 2367 | 源ID | 1 | 0 | yes | ok |
| 2406 | 源ID | 1 | 0 | yes | ok |
| 2446 | 源ID | 1 | 0 | yes | ok |
| 2478 | 源ID | 1 | 0 | yes | ok |
| 2512 | 源ID | 1 | 0 | yes | ok |
| 2550 | 源ID | 1 | 0 | yes | ok |
| 2588 | 源ID | 1 | 0 | yes | ok |
| 2626 | 源ID | 1 | 0 | yes | ok |
| 2661 | 源ID | 1 | 0 | yes | ok |
| 2703 | 源ID | 1 | 0 | yes | ok |
| 2741 | 源ID | 1 | 0 | yes | ok |
| 2779 | 源ID | 1 | 0 | yes | ok |
| 2817 | 源ID | 1 | 0 | yes | ok |
| 2853 | 源ID | 1 | 0 | yes | ok |
| 2889 | 源ID | 1 | 0 | yes | ok |
| 2925 | 源ID | 1 | 0 | yes | ok |
| 2963 | 源ID | 1 | 0 | yes | ok |
| 3000 | 源ID | 1 | 0 | yes | ok |
| 3038 | 源ID | 1 | 0 | yes | ok |
| 3076 | 源ID | 1 | 0 | yes | ok |
| 3114 | 源ID | 1 | 0 | yes | ok |
| 3154 | 源ID | 1 | 0 | yes | ok |
| 3192 | 源ID | 1 | 0 | yes | ok |
| 3230 | 源ID | 1 | 0 | yes | ok |
| 3268 | 源ID | 1 | 0 | yes | ok |
| 3307 | 源ID | 1 | 0 | yes | ok |
| 3345 | 源ID | 1 | 0 | yes | ok |
| 3385 | 源ID | 1 | 0 | yes | ok |
| 3425 | 源ID | 1 | 0 | yes | ok |
| 3465 | 源ID | 1 | 0 | yes | ok |
| 3506 | 源ID | 1 | 0 | yes | ok |
| 3547 | 源ID | 1 | 0 | yes | ok |
| 3581 | 源ID | 1 | 0 | yes | ok |
| 3615 | 源ID | 1 | 0 | yes | ok |
| 3653 | 源ID | 1 | 0 | yes | ok |
| 3690 | 源ID | 1 | 0 | yes | ok |
| 3724 | 源ID | 1 | 0 | yes | ok |
| 3759 | 源ID | 1 | 0 | yes | ok |
| 3799 | 源ID | 1 | 0 | yes | ok |
| 3834 | 源ID | 1 | 0 | yes | ok |
| 3862 | 源ID | 1 | 0 | yes | ok |
| 3896 | 源ID | 1 | 0 | yes | ok |
| 3933 | 源ID | 1 | 0 | yes | ok |
| 3970 | 源ID | 1 | 0 | yes | ok |
| 4008 | 源ID | 1 | 0 | yes | ok |
| 4043 | 源ID | 1 | 0 | yes | ok |
| 4082 | 源ID | 1 | 0 | yes | ok |
| 4121 | 源ID | 1 | 0 | yes | ok |
| 4160 | 源ID | 1 | 0 | yes | ok |
| 4200 | 源ID | 1 | 0 | yes | ok |
| 4242 | 源ID | 1 | 0 | yes | ok |
| 4281 | 源ID | 1 | 0 | yes | ok |
| 4317 | 源ID | 1 | 0 | yes | ok |
| 4357 | 源ID | 1 | 0 | yes | ok |
| 4398 | 源ID | 1 | 0 | yes | ok |
| 4430 | 源ID | 1 | 0 | yes | ok |
| 4462 | 源ID | 1 | 0 | yes | ok |
| 4503 | 源ID | 1 | 0 | yes | ok |
| 4543 | 源ID | 1 | 0 | yes | ok |
| 4583 | 源ID | 1 | 0 | yes | ok |
| 4621 | 源ID | 1 | 0 | yes | ok |
| 4658 | 源ID | 1 | 0 | yes | ok |
| 4695 | 源ID | 1 | 0 | yes | ok |
| 4720 | 源ID | 1 | 0 | yes | ok |
| 4745 | 源ID | 1 | 0 | yes | ok |
| 4770 | 源 ID | 1 | 0 | yes | ok |
| 4773 | 源ID | 1 | 0 | yes | ok |
| 4795 | 源ID | 1 | 0 | yes | ok |
| 4839 | 源ID | 1 | 0 | yes | ok |
| 5103 | 源ID | 1 | 0 | yes | ok |
| 5177 | 源ID | 1 | 0 | yes | ok |
| 5275 | 源ID | 1 | 0 | yes | ok |
| 5420 | 源 ID | 1 | 0 | yes | target string also pre-existed in R1-R3; modeled replacement occurrence is exact |
| 5423 | 源ID | 1 | 0 | yes | ok |
| 5523 | 源ID | 1 | 0 | yes | ok |
| 5659 | 源ID | 1 | 0 | yes | ok |
| 5709 | 源ID | 1 | 0 | yes | ok |
| 5749 | 源 ID | 1 | 0 | yes | target string also pre-existed in R1-R3; modeled replacement occurrence is exact |
| 5752 | 源ID | 1 | 0 | yes | ok |
| 5810 | 源ID | 1 | 0 | yes | ok |
| 5833 | 源ID | 1 | 0 | yes | ok |
| 5856 | 源ID | 1 | 0 | yes | ok |
| 5879 | 源ID | 1 | 0 | yes | ok |
| 5902 | 源ID | 1 | 0 | yes | ok |
| 5917 | external-源ID, 源ID | 1 | 0 | yes | ok |
| 5929 | range, coordinate, chapterUid | 1 | 0 | yes | ok |

## Mismatch disposition

- Unapproved mismatches: none.
- Global target-after duplicate note: rows `5420` and `5749` have target strings already used by earlier round section headings; this is not a content mismatch because byte-for-byte modeled-post equality proves only the approved R4 grouped headings changed.
