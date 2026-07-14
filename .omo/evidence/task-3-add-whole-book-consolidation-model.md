# Task 3 evidence: whole-book consolidation shortcuts

## Scope

- Added a `读完整本书后执行全书收束整合` shortcut to both prompt files.
- Ensured shortcuts remain subordinate to task entrance, planning, Momus/Metis/Oracle review, explicit execution authorization, QA, and conditional Git authorization.

## Verification

- `微信读书通用提示词.md` shortcut mentions `阅读现场档案`, `文章素材索引`, `不抹掉阅读过程`, and says complex tasks must complete planning/review/authorization before execution.
- `路遥/人生/《人生》微信读书提示词.md` shortcut mentions `阅读现场档案`, `文章素材索引`, `不抹掉阅读过程`, fixed 《人生》 paths, and technical-field exclusion.
- `路遥/人生/《人生》微信读书提示词.md` shortcut now uses `第四阶段前置检查` with concrete checks instead of undefined fourth-stage `阶段切换 QA`; its auxiliary preamble now says `阶段切换 QA 或第四阶段前置检查`.
- Broad forbidden-pattern scan only matched protective negative rules, not a shortcut that bypasses planning/review/authorization or lets article indexes replace cards.

## Result

PASS. Shortcuts express the new task without bypassing gates or erasing the reading-site archive.
