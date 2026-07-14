# Task 2 evidence: 《人生》 prompt fourth-stage model

## Scope

- Updated `路遥/人生/《人生》微信读书提示词.md` only for the book-specific prompt portion.
- Updated the top-level summary from `三阶段总流程` to `四阶段总流程` and added the fourth-stage summary entry.
- Added `## 11. 第四阶段：读完整本书后的全书收束整合` after the third-stage migration rules.
- Preserved fixed paths for `/home/king/github/growing-myself/路遥/人生/《人生》中间整理稿.md` and `/home/king/github/growing-myself/路遥/人生/《人生》阅读笔记.md`.
- Renumbered following sections to `12`, `13`, and `14`.

## Verification

- Read-back confirmed the new section defines `阅读现场档案 + 文章素材索引`, `一卡双归宿`, `内部整合台账`, `source status`, `archive disposition`, and `文章素材索引只引用卡片，不吞掉卡片`.
- Read-back confirmed the entrance gate task-type list now includes `第四阶段（全书收束整合）`, and the top flow says `四阶段总流程`.
- The section includes 《人生》-specific article directions: 人物线、城乡主题、尊严主题、爱情线、知识分子困境、写法线索.
- The formal-note skeleton places `阅读现场档案` before `文章素材索引` and includes `阅读轨迹与判断变化` plus `待回看 / 归档不迁移`.
- Regression labels remained present: `ID 003`, `ID 006`, `ID 021`, `ID 109`, `ID 117`, `刘玉海救灾处`, `黄亚萍的物质付出`.
- `GIT_MASTER=1 git diff --check -- 路遥/人生/《人生》微信读书提示词.md` passed with no output.
- `lsp_diagnostics` has no configured Markdown server, so no Markdown LSP diagnostics are available.

## Result

PASS. 《人生》 prompt now contains the approved fourth-stage model with fixed paths and regression labels preserved.
