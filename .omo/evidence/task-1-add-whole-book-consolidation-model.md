# Task 1 evidence: generic prompt fourth-stage model

## Scope

- Updated `微信读书通用提示词.md` only for the generic prompt portion.
- Updated the entrance gate task-type list to explicitly include `第四阶段（全书收束整合）`.
- Added `## 12. 第四阶段：读完整本书后的全书收束整合` after the third-stage migration rules.
- Renumbered following sections to `13`, `14`, and `15`.

## Verification

- Read-back confirmed the new section defines `阅读现场档案 + 文章素材索引`, `卡片档案为底座，文章素材索引为上层导航`, `一卡双归宿`, `内部整合台账`, `source status`, `archive disposition`, and `文章素材索引只引用卡片，不吞掉卡片`.
- Read-back confirmed `微信读书通用提示词.md:33` now names `第四阶段（全书收束整合）` in the task entrance gate.
- The section distinguishes third-stage migration from fourth-stage whole-book consolidation and says fourth stage must not globally re-run third-stage migration.
- The formal-note skeleton places `阅读现场档案` before `文章素材索引` and includes `阅读轨迹与判断变化` plus `待回看 / 归档不迁移`.
- Broad forbidden-pattern scan only matched protective negative rules such as “不能/不得/没有”, not affirmative bad rules.
- `GIT_MASTER=1 git diff --check -- 微信读书通用提示词.md` passed with no output.
- `lsp_diagnostics` has no configured Markdown server, so no Markdown LSP diagnostics are available.

## Result

PASS. Generic prompt now contains the approved fourth-stage model and guardrails.
