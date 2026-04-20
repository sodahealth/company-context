# Checkpoint: WI-20

## Status

- **WI-20: ask_patterns frontmatter on company-wide prompts** — COMPLETE, committed

## What Was Done

1. Added YAML frontmatter with `ask_patterns` arrays to both company-wide prompts:
   - `prompts/engage.md` — 18 patterns covering onboarding, new hire, platform intro, team engagement
   - `prompts/problem-mapping.md` — 16 patterns covering help requests, broken tools, service tickets
2. Updated `scripts/build-catalog.py` to include `ask_patterns` in catalog entries when present
3. Regenerated `catalog.json` — verified both prompts' patterns appear in catalog
4. Ruff format + check clean
5. Committed as `beacd04` on branch `coder/2026-04-20-wi-20`

## What Remains

- Push branch to remote (`git push -u origin coder/2026-04-20-wi-20`)
- Open PR against `main`
- No Jira comment needed (no PLAN issue number found in work plan)

## Blocked By

Session governance hook blocks `git push` for `coder-dispatched` role. Needs a session with `coder` or `solutions-engineer` role to push and open PR.

## Resume Command

```bash
cd ~/code/sessions/company-context--coder-2026-04-20-wi-20
git push -u origin coder/2026-04-20-wi-20
gh pr create --title "feat(prompts): add ask_patterns for deterministic routing (WI-20)" --body "$(cat <<'PREOF'
## Summary

- Added `ask_patterns` frontmatter arrays to company-wide prompts (`engage.md`, `problem-mapping.md`) enabling Phase 1 deterministic ask→prompt routing per ADR-6f0f81c0
- Updated `build-catalog.py` to propagate `ask_patterns` into `catalog.json`
- Regenerated catalog

## Work Plan

`work-plans/2026-04-20-ema-canonical-knowledge-interface.md` — WI-20

## Test plan

- [x] `python3 scripts/build-catalog.py` succeeds with 0 validation errors
- [x] `catalog.json` contains `ask_patterns` for both prompts
- [x] Patterns are lowercase case-insensitive substrings
- [x] Ruff format + check clean

🤖 Generated with [Claude Code](https://claude.com/claude-code)
PREOF
)"
```
