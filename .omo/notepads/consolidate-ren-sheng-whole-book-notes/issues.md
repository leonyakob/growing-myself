# Issues

## 2026-07-16 Start-work initialization
- `.omo/boulder.json` also contains unrelated active/paused works. This invocation explicitly selected `consolidate-ren-sheng-whole-book-notes`; do not mutate or resume the other plans.
- `.omo/start-work/ledger.jsonl` contains historical entries for another plan. New entries must always carry this plan path and must append without rewriting history.
- Existing dirty and runtime continuation paths are unknown until delegated Todo 0 captures the NUL-safe preflight baseline.
