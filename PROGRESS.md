# WI-14, WI-15, WI-16, WI-17 — /getstarted Skill Rewrite (Three-Mode Detection)

## Status: Complete

## What changed

### `skills/getstarted/SKILL.md` — Full rewrite

Replaced the previous single-path onboarding skill (4 steps, one flow) with a three-mode
detection system that serves first-time employees, returning users, and new hires.

#### Phase 0: Mode Detection (WI-14)
- Three-check detection sequence:
  1. Read `~/.claude/CLAUDE.md` for `<!-- BEGIN EVERMORE PLATFORM -->` marker
  2. Pull `people/me` via MCP for profile data and `start_date`
  3. Check session history via Cosmos enrichment data
- Mode routing table:
  - No marker → Mode 1 (first-time existing employee)
  - Marker + start_date within 30 days + no prior enrichment → Mode 3 (new hire)
  - Marker + returning → Mode 2 (returning user)
  - Marker + no enrichment + not new hire → Mode 2 (don't re-onboard)
- Detection logic is internal — users see a seamless greeting, not diagnostics

#### Mode 1: First-Time Existing Employee (WI-15)
Seven-step onboarding flow:
1. **Gather context** — people/me + get_employee_profile + Knower search for department docs
2. **Platform introduction** — vision statement personalized by department
3. **Available commands** — department-specific skill list with 3-4 real examples
4. **Environment setup** — CLAUDE.md marker-based merge logic:
   - If markers exist: replace content between them (preserves surrounding content)
   - If file exists but no markers: append platform section
   - If no file: create with platform section
   - Platform section includes identity, department, skills, session tips, language preferences
   - Language preferences adapt: non-technical for People Ops/Finance, technical for Engineering
5. **Learn + proactive suggestions** — top 3 pain points with tiered confidence:
   - High = from discovery profile (explicit evidence)
   - Medium = from access patterns and behavioral data
   - Low = role-based assumptions (acknowledged as such)
6. **First conversation** — routes to department prompt or workflow
7. **Enrichment writeback** — write_employee_enrichment with session data

#### Mode 2: Returning User Session Launcher (WI-16)
Five-step daily session flow:
1. **Identify and greet** — time-of-day aware greeting (no default "good morning")
2. **Frequency adaptation** — adjusts behavior based on recency:
   - Already ran today: skip status, go straight to "What would you like to work on?"
   - First of day: full brief
   - 3+ days gap: comprehensive catch-up
3. **Status update** — work tracker items, automation request statuses, PRs (technical), new context docs, notifications
4. **Pending tasks** — incomplete items from last session, follow-ups, deadlines
5. **Quick launch** — most-used workflows as options, "Continue where you left off"

#### Mode 3: New Hire Onboarding (WI-17)
Eight-step flow (Steps 1-4 shared with Mode 1, then diverges):
1-4. Same as Mode 1 (gather context, platform intro, commands, environment setup)
5. **Company introduction** — company overview/mission from Knower, team intro (manager, teammates, key people), department context
6. **Tool setup assistance** — expected tool stack from ref-systems.md, access verification per tool, gap flagging to IT
7. **First task** — common team workflows (not pain points — new hires don't have them yet), or manager's instructions
8. **Enrichment writeback** — same as Mode 1 Step 7

### Design decisions

- **CLAUDE.md merge is in the skill, not a separate function** — WI-18 specifies the merge logic as a reusable function in evermore-agent, but the skill describes the merge behavior inline so Claude can execute it directly. When the evermore-agent function lands, the skill can call it instead. For now the skill is self-contained per the issue scope.
- **Enrichment writeback preserved** from the previous skill version — it is the mechanism that lets Mode 2 detect returning users.
- **Tone guidelines at the bottom** serve as a cross-cutting concern — they apply to all three modes. Non-engineering departments get plain language; engineering gets technical terms.
- **"What This Skill Does NOT Do"** section updated to reflect three-mode behavior.

## Files changed
- `skills/getstarted/SKILL.md` — full rewrite (135 lines → 580 lines)
- `PROGRESS.md` — this file (replaced previous WI-2677f309 progress)

## Work items addressed
- **WI-14:** /getstarted skill rewrite — three-mode detection
- **WI-15:** Mode 1 — First-time existing employee onboarding
- **WI-16:** Mode 2 — Returning user session launcher
- **WI-17:** Mode 3 — New hire onboarding

## References
- Work plan: `it-ops-context/work-plans/2026-02-23-department-rollout-chris-regina-shaun.md`
- Issue: #279
- Related WI-18 (CLAUDE.md merge logic in evermore-agent) is a separate dispatch
