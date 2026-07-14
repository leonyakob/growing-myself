# Task 0 evidence: dry-run fixture

## Scope

- Created `.omo/evidence/fixtures/add-whole-book-consolidation-model.md` before target prompt edits.
- Covered nine deterministic whole-book consolidation cases.

## Verification

- Read-back confirmed all nine `## Case` entries are present.
- `GIT_MASTER=1 git grep --no-index -n 'source status\|archive treatment\|formal-note treatment\|article-index treatment\|forbidden failure' -- .omo/evidence/fixtures/add-whole-book-consolidation-model.md` showed all required headings in every case.
- `GIT_MASTER=1 git diff --no-index --check -- /dev/null .omo/evidence/fixtures/add-whole-book-consolidation-model.md` passed with no output.
- `lsp_diagnostics` has no configured Markdown server, so no Markdown LSP diagnostics are available.

## Result

PASS. The fixture exists, has nine concrete cases, and preserves `划线原文` + `我自己写的内容` for every non-external-only case. The external-only case is explicitly labeled and forbids rewriting external material as the user's first-person judgment.
