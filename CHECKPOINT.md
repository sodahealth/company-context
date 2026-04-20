# Checkpoint — WI-21

## Completed WIs
- **WI-21**: CODEOWNERS for company-context — DONE and committed (`d9d3332`)

## What was done
- Updated `.github/CODEOWNERS` to add all 9 department folders (care, finance, leadership, mx, peopleops added; hps, growth, engineering, shared already existed)
- Added explicit onboarding skill review gates: `/skills/getstarted/` (IT-owned), `/skills/growth-feedback/` (IT + product co-owned)
- Verified branch protection already enforces CODEOWNERS review (`require_code_owner_reviews: true`)

## Remaining
- Push branch `coder/2026-04-20-wi-21` and open PR against `main`
- No Jira Story link found in work plan — Jira comment step skipped

## Resume command
```bash
git push -u origin coder/2026-04-20-wi-21
gh pr create --title "feat(codeowners): department + skill review gates (WI-21)" --body "..."
```
