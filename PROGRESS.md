# WI-2677f309 — /getstarted Profile Integration + Enrichment Writeback

## Status: Complete

## What changed

### A. `skills/getstarted/SKILL.md`
- Expanded from 2-step to 4-step flow:
  - Step 1: `get_content` for basic profile (existing, unchanged)
  - Step 2 (NEW): `get_employee_profile` for rich Cosmos profile — graceful fallback if unavailable
  - Step 3: `get_content` for onboarding prompt (existing, now passes both profiles as context)
  - Step 4 (NEW): `write_employee_enrichment` with collected session data — silent failure handling
- Added guidance on when to skip enrichment (short/empty conversations)
- Updated "What This Skill Does NOT Do" to note profile/enrichment internals are not exposed

### B. `prompts/engage.md`
- Added **Profile Context** section before mode routing with:
  - Data source descriptions (HR, Entra, communication, prior enrichment)
  - Instructions for natural personalization (don't dump data, weave into conversation)
  - Cold-start handling (no profile = more manual questions, enrichment becomes first data point)
- **Mode A** updates: HR data pre-fill, skip known info, Entra sign-in for account verification, channel suggestions from communication patterns
- **Mode B** updates: Prior enrichment references, tool-aware questions from Entra data, tiered fallback (rich profile > basic profile > no profile)
- **Mode C**: Added enrichment collection step (C7)
- **Mode D** updates: Team composition from profile data, communication pattern references, prior enrichment as validation starting point
- Added **Enrichment Collection** step (A7, B7, C7, D7) to all four modes with mode-specific guidance
- Added two new rules to "What NOT to Do": don't expose raw profile data, don't write empty enrichment

## Files changed
- `skills/getstarted/SKILL.md`
- `prompts/engage.md`
- `PROGRESS.md` (this file)
