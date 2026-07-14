# F3 fix follow-up, split-weread-prompts-by-stage

## Rejection summary

- F3 rejected the generic router prompt surface because `/home/king/github/growing-myself/微信读书通用提示词.md` did not explicitly route the exact shortcut `只评价问题质量` to Stage 2 in either the top stage index table or the shortcut-routing section.

## Files changed

- `/home/king/github/growing-myself/微信读书通用提示词.md`
- `/home/king/github/growing-myself/.omo/evidence/f3-fix-split-weread-prompts-by-stage.md`
- `/home/king/github/growing-myself/.omo/notepads/split-weread-prompts-by-stage/learnings.md` (append-only)

## Commands run

- `GIT_MASTER=1 git grep -F --untracked -n "只评价问题质量" -- "微信读书通用提示词.md"`
- `GIT_MASTER=1 git diff --check -- "微信读书通用提示词.md"`
- `functions.lsp_diagnostics("/home/king/github/growing-myself/微信读书通用提示词.md")`
- `functions.lsp_diagnostics("/home/king/github/growing-myself/.omo/evidence/f3-fix-split-weread-prompts-by-stage.md")`
- `functions.lsp_diagnostics("/home/king/github/growing-myself/.omo/notepads/split-weread-prompts-by-stage/learnings.md")`
- `GIT_MASTER=1 git diff --no-index --check /dev/null ".omo/evidence/f3-fix-split-weread-prompts-by-stage.md"`
- `GIT_MASTER=1 git diff --check -- ".omo/notepads/split-weread-prompts-by-stage/learnings.md"`

## Verification results

- `GIT_MASTER=1 git grep -F --untracked -n "只评价问题质量" -- "微信读书通用提示词.md"` returned hits at the top Stage 2 route row and the `## 6. 快捷模板警告与路由提醒` Stage 2 bullet.
- `GIT_MASTER=1 git diff --check -- "微信读书通用提示词.md"` returned no output.
- `GIT_MASTER=1 git diff --no-index --check /dev/null ".omo/evidence/f3-fix-split-weread-prompts-by-stage.md"` returned no output.
- `GIT_MASTER=1 git diff --check -- ".omo/notepads/split-weread-prompts-by-stage/learnings.md"` returned no output.
- `functions.lsp_diagnostics` was run on all changed Markdown files. Markdown LSP is unavailable in this workspace, and that tooling limitation is recorded honestly rather than hidden.

## PASS

- PASS: `/home/king/github/growing-myself/微信读书通用提示词.md` now explicitly routes `只评价问题质量` to Stage 2 in the top router table.
- PASS: `/home/king/github/growing-myself/微信读书通用提示词.md` now explicitly routes `只评价问题质量` to Stage 2 in the shortcut-routing section.
- PASS: the fix is surgical; no Stage 2 execution body was copied back into the router.
- PASS: no 《人生》 file was edited.
- PASS: whitespace checks passed for the changed router, the new follow-up evidence file, and the append-only learnings file.
- PASS: Markdown LSP diagnostics were attempted on all changed Markdown files, and `.md` LSP unavailability was recorded.
- F3_FIX_READY_FOR_RERUN: PASS
