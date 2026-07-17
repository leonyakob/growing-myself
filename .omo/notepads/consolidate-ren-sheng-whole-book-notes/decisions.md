# Decisions

## 2026-07-16 Start-work initialization
- Execute in the current project directory because no `--worktree` was requested; do not create a branch, commit or push.
- The only reading-material target is `路遥/人生/《人生》阅读笔记.md`; every other persistent output must match the plan's exact `.omo/evidence/` allowlist.
- Preserve the sealed plan, draft and review seal byte-for-byte throughout execution.
- Treat API interruptions, task aborts, wrong-agent metadata and missing final messages as NO_RESULT, never as success or failure verdicts.
- Root Atlas only orchestrates and edits `.omo/` control state; all implementation and QA are delegated.
