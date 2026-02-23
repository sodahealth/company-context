---
name: getstarted
description: Platform front door — detects mode (first-time, returning, new hire) and routes to the appropriate onboarding or session flow
---

# /getstarted — Evermore Platform Front Door

This skill is the entry point every time an employee starts a Claude session at Evermore.
It detects who the user is, determines which experience they need, and routes them to
the right flow. It replaces the previous single-path onboarding with a three-mode
detection system.

**Three modes:**

| Mode | Who | What happens |
|------|-----|-------------|
| **Mode 1** | Existing employee, first time on platform | Full onboarding: intro, setup, proactive suggestions, first conversation |
| **Mode 2** | Returning user | Session launcher: status update, pending tasks, quick launch |
| **Mode 3** | New hire (started within 30 days) | Company introduction, tool setup, team intro, first task |

---

## Phase 0: Mode Detection

Run these three checks in sequence. Do NOT display any of this detection logic to
the user — they should experience a seamless greeting, not a diagnostic checklist.

### Check 1: Platform marker in CLAUDE.md

Read the file `~/.claude/CLAUDE.md` using the Read tool.

- Look for the marker `<!-- BEGIN EVERMORE PLATFORM -->` anywhere in the file content.
- If the file does not exist, or the marker is not found: **platform_setup = false**
- If the marker exists: **platform_setup = true**

### Check 2: Profile and start date

Call the `get_content` MCP tool with path `people/me` to retrieve the caller's profile.

- If the tool succeeds: note all available fields (name, role, department, systems,
  manager, team, start_date)
- If the tool fails: proceed without profile data (you will ask for context manually)
- If `start_date` is present and is within the last 30 days (relative to today):
  **new_hire = true**
- Otherwise: **new_hire = false**

Also attempt to call the `get_employee_profile` MCP tool for the richer Cosmos-backed
profile (HR data, Entra data, communication patterns, prior enrichment). If it fails,
continue with the basic profile only. Do not surface failures to the user.

### Check 3: Session history

Check whether prior enrichment data exists in the Cosmos profile (from Check 2). If
the `get_employee_profile` response contains prior enrichment fields (challenges,
processes, focus_areas, etc.) with real data, the user has run /getstarted before.

- If prior enrichment exists with substantive data: **returning = true**
- If no prior enrichment or empty: **returning = false**

Also check: if `platform_setup = true` and the platform section in CLAUDE.md contains
an identity block, the user has been onboarded before: **returning = true**.

### Mode routing

Apply these rules in order:

1. If `platform_setup = false`: **Mode 1** (First-time existing employee)
2. If `platform_setup = true` AND `new_hire = true` AND `returning = false`: **Mode 3** (New hire onboarding)
3. If `platform_setup = true` AND `returning = true`: **Mode 2** (Returning user)
4. If `platform_setup = true` AND `returning = false` AND `new_hire = false`: **Mode 2** (Returning user — platform was set up but no enrichment yet; treat as returning, not re-onboarding)

Proceed to the section for the detected mode.

---

## Mode 1: First-Time Existing Employee Onboarding

This is the full onboarding experience for an employee who has been at Evermore but
is using the Claude platform for the first time.

### Step 1 — Gather Context

Use the profile data from Phase 0 (Check 2). You should have:

- **Name** — greet them by first name
- **Role / title** — understand what they do
- **Department** — determines their context repo and language preferences
- **Manager** — who they report to
- **Team members** — who they work with
- **Systems / applications** — tools they use daily
- **Discovery profile** — if available, enrichment from a prior discover sess

If the MCP call failed and you have no profile data, ask the user directly:

> "Welcome! I'm going to get you set up on the Evermore platform. First, can you
> tell me your name, your role, and which team you're on?"

Also attempt to pull department-specific context by calling `search` via the MCP tool
(Knower) for their department's reference documents (ref-systems, ref-team, ref-processes).
This gives you richer context for personalization.

### Step 2 — Platform Introduction

Deliver the platform introduction, personalized to the user. Do NOT read this verbatim
as a script — adapt it naturally based on who they are and what department they are in.

**Core message:**

> "Most companies give employees a blank AI session — you start from zero every time.
> We're building something different. Every session at Evermore starts pre-loaded with
> context: who you are, what your team does, what systems exist, what decisions have been
> made. The more people use it, the smarter it gets — not through training, but through
> accumulating structured context that every session draws from.
>
> You're not just using Claude. You're using Claude with Evermore's institutional memory."

**Then personalize** — explain why this matters to THEM based on their department:

- **Engineering / Product:** "For you, that means Claude already knows about Harmony's
  architecture, your team's deployment cadence, and the engineering OKRs. When you ask
  about a system, it knows the context."
- **People Operations:** "For you, that means Claude already knows about the 360 review
  process, your workforce planning work, and the tools you use. When you need help with
  a process, it understands your world."
- **Finance / Accounting:** "For you, that means Claude already knows about the vendor
  contracts, your financial systems, and your reporting cadence. When you ask about a
  contract or process, it has the background."
- **Other departments:** Adapt similarly — reference their specific systems and workflows
  from the profile data.

Keep this to 30 seconds of reading. Do not over-explain.

### Step 3 — Available Commands

Show them what they can do, tailored to their department.

> "Here's what you can do from here:"

List the skills and prompts available for their department. Pull this from the department
context repo if available, or use the general set:

**For all departments:**
- `/getstarted` — Start here each session (this skill — shows status, quick launch)

**Department-specific examples (adapt based on their actual department):**

For **People Operations:**
- "Ask me about any HR process — I have your team's workflows documented"
- "Tell me about a process you'd like to improve and I'll help you think through it"
- "Ask a research question — 'What's our headcount by department?'"
- "Need help preparing a board deck section? Just describe what you need."

For **Finance / Accounting:**
- "Ask about vendor contracts — 'When does the Vonage agreement expire?'"
- "Describe a manual workflow and I'll help you document and improve it"
- "Ask about financial processes — I know your tools and how they connect"
- "Need to look something up? I can search across company knowledge."

For **Engineering / Product:**
- "Ask about architecture — 'How does Harmony's auth flow work?'"
- "Describe a feature or project you want to plan and I'll help decompose it"
- "Ask about engineering processes, deployment, or infrastructure"
- "Check OKR progress or project status"

For **other departments:** Adapt examples to their known systems and workflows.

### Step 4 — Environment Setup

Set up the user's `~/.claude/CLAUDE.md` with the Evermore platform section. This is
a critical step — it ensures every future session has the right context.

**CLAUDE.md merge logic:**

1. Read `~/.claude/CLAUDE.md` if it exists.
2. Look for `<!-- BEGIN EVERMORE PLATFORM -->` and `<!-- END EVERMORE PLATFORM -->` markers.
3. Generate the platform section content (see template below).
4. Apply the merge:
   - **If markers exist:** Replace everything between `<!-- BEGIN EVERMORE PLATFORM -->`
     and `<!-- END EVERMORE PLATFORM -->` (inclusive of markers) with the new platform
     section. Preserve all content before and after the markers.
   - **If file exists but no markers:** Append the platform section to the end of the
     file, preceded by a blank line.
   - **If file does not exist:** Create the file with the platform section as its only
     content.

**Platform section template** (fill from profile data):

```markdown
<!-- BEGIN EVERMORE PLATFORM -->
# Evermore Platform Context

## Who You Are
- **Name:** [full name]
- **Role:** [title / role]
- **Department:** [department]
- **Manager:** [manager name]

## Your Department
- **Context repo:** ~/code/[dept-context-repo]/
- Read your department's CLAUDE.md for domain-specific instructions and conventions.

## Available Skills
- `/getstarted` — Start here each session for status updates and quick launch

[Add department-specific skills if known, e.g.:]
[- `/help` — Ask for help with any process (People Ops)]

## Session Tips
- Start each session with `/getstarted` for a status update and quick launch
- For research questions, just ask — the platform has access to company knowledge via Knower
- For automation requests, describe the process you want to improve in plain language
- Claude remembers context between messages in a session, but each new session starts fresh from your context files

## Language Preferences
[For non-engineering departments (People Ops, Finance, etc.):]
- Use plain, non-technical language in all explanations
- Describe outcomes and results, not implementation details
- When technical work is needed behind the scenes, explain what will happen, not how it is built
- Avoid jargon like "repo", "PR", "deploy", "endpoint" — use everyday equivalents

[For engineering departments:]
- Technical language is fine — use standard engineering terminology
- Reference repos, PRs, and infrastructure directly
- Include code examples and architecture details when relevant
<!-- END EVERMORE PLATFORM -->
```

**Important:** Never delete existing content in the user's CLAUDE.md. The merge is
additive (append) or replacement (within markers only). Personal notes, project
instructions, and other content outside the markers are always preserved.

After writing CLAUDE.md, confirm to the user:

> "I've set up your platform configuration. Each time you start a session, Claude will
> know who you are and what tools you use."

Do NOT dump the contents of what you wrote. Keep it conversational.

### Step 5 — Learn About Them + Proactive Suggestions

Now shift from setup to conversation.

> "Now that you're set up, I'd love to learn more about what you do day-to-day so I
> can be more useful to you."

Analyze everything you know about them — profile, systems, discovery data, department
patterns, communication patterns — and generate their top 3 pain point suggestions
with honest confidence levels.

**Confidence level definitions:**
- **High** — Based on explicit data from a discovery session or their own prior statements.
  You have direct evidence this is a pain point.
- **Medium** — Based on patterns in their department access map, app usage, or
  communication patterns. For example, high usage of Forms + SharePoint + Excel suggests
  manual data compilation. You are inferring from behavioral data.
- **Low** — Based on common pain points for their job function and department. These
  are role-based assumptions, not evidence. Be transparent about that.

Present the suggestions:

> "Based on what I know about your role and the systems you work with, here are some
> areas where I think I could help the most:"
>
> 1. **[Pain point description]** — confidence: high
>    [1-sentence explanation of why this was identified, citing the evidence source]
>
> 2. **[Pain point description]** — confidence: medium
>    [1-sentence explanation, referencing the pattern or data source]
>
> 3. **[Pain point description]** — confidence: low
>    [1-sentence explanation, acknowledging this is a role-based assumption]
>
> "Would any of these ring true? Or is there something else entirely that eats up
> your time?"

Listen to their response. If they confirm a pain point, pivot to helping with it.
If they redirect, follow their lead.

If you have NO data to generate suggestions (profile unavailable, no discovery data),
skip the suggestions and ask open-ended questions instead:

> "What does your typical week look like? What takes up the most time? What would you
> love to spend less time on?"

### Step 6 — First Conversation

Whatever they want to work on becomes their first real session. Route to the appropriate
mode:

- If they want research or a question answered: answer it using Knower search and
  department context.
- If they describe a process to improve: interview them about it, document it, and
  explain that you can route an automation request to the platform team.
- If they want to explore: suggest trying one of the examples from Step 3.

This is a natural handoff — the onboarding is complete and the user is now in a
working session.

### Step 7 — Write Enrichment Data

After the conversation wraps up (or at a natural stopping point), write enrichment
data back via the `write_employee_enrichment` MCP tool.

Structure the payload from what the employee shared:

```json
{
  "challenges": ["list of challenges they mentioned"],
  "processes": ["workflows and processes they described"],
  "friction_points": ["pain points and frustrations"],
  "tools_mentioned": ["tools and systems they referenced"],
  "focus_areas": ["their stated priorities"],
  "notes": "free-form summary of key takeaways from the onboarding session"
}
```

Only include fields with real substance. Skip the writeback entirely if the conversation
was too short to collect meaningful data. Handle failures silently — do not tell the
user about enrichment mechanics.

---

## Mode 2: Returning User Session Launcher

This mode runs when an already-onboarded user starts a new session. It is a quick
status briefing and launch pad, not a re-onboarding. Keep it efficient.

### Step 1 — Identify and Greet

Use the profile data from Phase 0 (Check 2). Greet the user by first name.

**Time-of-day awareness:** Do NOT default to "Good morning." Check the current time
and adapt your greeting:

- Before 12pm: "Morning, [name]." or similar
- 12pm-5pm: "Hey [name]." or "Afternoon, [name]."
- After 5pm: "Hey [name], working late?" or "Evening, [name]."

Keep the greeting short — one line, not a paragraph.

### Step 2 — Frequency Adaptation

Determine how recently the user last ran a session. Use these signals:

- **Prior enrichment timestamp** from Cosmos profile (if available)
- **Session history** — if the platform section in CLAUDE.md was recently updated
- **Explicit check:** If you can determine this is a second+ run today, adapt accordingly

**Adaptation rules:**

| Last session | Behavior |
|-------------|----------|
| Already ran today | Skip status update entirely. Go straight to "What would you like to work on?" |
| Yesterday or earlier today (first of day) | Full brief — status update + pending tasks + quick launch |
| 3+ days since last session | Comprehensive catch-up — slightly more detail on what changed |

If you cannot determine when they last ran a session, default to the full brief.

### Step 3 — Status Update (skip if already ran today)

Compile a brief status update from available sources. Present it as a concise bulleted
list, not a wall of text.

**What to include (if available):**

- **Work Tracker items** — call `search` via MCP (Knower) for work tracker items linked
  to their department or projects. Summarize status changes, completed items, new items.
- **Automation request updates** — if they have submitted automation requests in prior
  sessions (from enrichment data), check for status updates.
- **PRs merged** — for technical users only: if they work on code repos, note any
  recently merged PRs on projects they are linked to.
- **New context documents** — if new knowledge docs or reference material was added to
  their department context repo since their last session, note it briefly.
- **Notifications** — any messages or items routed to them.

**Presentation:**

> "Here's where things stand:"
>
> - [status item 1]
> - [status item 2]
> - [status item 3]

If nothing has changed or no data is available, say so briefly:

> "Nothing new since your last session."

Do NOT fabricate status updates. Only report what you can verify from available data.

### Step 4 — Pending Tasks

Check for incomplete work from previous sessions:

- **From enrichment data:** focus_areas, in-progress items mentioned in prior sessions
- **From work tracker:** items assigned to them that are not complete
- **From session history:** if they mentioned follow-ups or "I'll do this later" items

If there are pending items:

> "Picking up from where you left off:"
>
> - [pending item 1 — brief description]
> - [pending item 2 — brief description]

If no pending items are detected, skip this section entirely.

### Step 5 — Quick Launch

Offer to start working:

> "What would you like to work on?"

Show their most-used workflows as quick-access options. Pull these from:
- Prior enrichment data (what they have worked on before)
- Department-specific common workflows
- Any incomplete items from Step 4

Present as a short list:

> Options:
> - Continue [specific task from last session]
> - [Common workflow 1 for their department]
> - [Common workflow 2 for their department]
> - Something else — just describe it

Wait for their response, then route to the appropriate workflow. This is the handoff
from /getstarted into their working session.

---

## Mode 3: New Hire Onboarding

This mode runs for employees who started within the last 30 days and are using the
platform for the first time. It shares Steps 1-4 with Mode 1 (first-time employee)
but replaces Steps 5-6 with company and team introduction.

### Steps 1-4: Same as Mode 1

Run Mode 1 Steps 1 through 4 exactly as described:
1. Gather context (people/me, department context, discovery profile)
2. Platform introduction (vision statement, personalized relevance)
3. Available commands (department-specific examples)
4. Environment setup (CLAUDE.md merge with platform section)

### Step 5 — Company Introduction

After setup is complete, shift to helping the new hire understand the company.

> "Welcome to Evermore! Since you're new, let me give you a quick tour of the company
> and your team."

**Company overview:**
- Search for company overview and mission documents via the `search` MCP tool (Knower).
  Look for documents about what Evermore does, the product (Harmony), health plans,
  EBT programs.
- Summarize in 3-4 sentences: what the company does, who it serves, what makes it
  different.
- If company knowledge docs are not available, provide a brief overview based on what
  you know from context.

**Team introduction:**
- From the profile data: name their manager and explain their role briefly.
- List team members and their roles: "You'll be working with [name] ([role]),
  [name] ([role]), and [name] ([role])."
- Mention key people outside the team they will interact with, if available from
  department cross-references.
- For each person: one sentence about what they do and how the new hire will work
  with them.

**Department context:**
- "Here's how [department] fits into the company:"
- Summarize the department's mission, key responsibilities, and how their work
  connects to the company's goals.
- Pull from department context docs (ref-team.md, ref-processes.md) if available.

Keep the company introduction to 2-3 minutes of reading. Be warm and welcoming, not
encyclopedic.

### Step 6 — Tool Setup Assistance

Help the new hire verify they have access to the tools they need.

> "Let me help you check that your tool access is set up."

**Pull the expected tool stack** from their department's ref-systems.md (via Knower
search or department context). For each tool in their expected stack:

1. **Name the tool and what it is for** — in language appropriate to their role.
   - Non-technical: "Rippling is where you'll manage time off, benefits, and payroll info."
   - Technical: "GitHub is where all our code repos live — you'll need access to the
     sodahealth org."

2. **Check access status** — from the profile data (Entra groups, app assignments), note
   whether they likely have access.
   - If access is confirmed: "You're set up with [tool]."
   - If access is unclear: "You should have access to [tool]. If you can't log in,
     let me know and I'll get IT to sort it out."
   - If access appears missing: "It looks like [tool] might not be set up yet. I'll
     flag this for the IT team."

3. **Quick orientation** — one sentence about what they will use this tool for in their
   specific role.

**If access gaps are found:**
- Compile a list of missing or uncertain tool access.
- Offer to route to IT: "Would you like me to flag these for the IT team to set up?"
- If they agree, note the gap in the enrichment data and, if the `search` MCP tool
  is available, look up the IT intake process to route the request.

### Step 7 — First Task

Transition from setup to productive work, framed for a new hire:

> "Now that you're set up, let me help you get started with something useful."

**If their manager gave them specific first tasks** (ask the user):
> "Did your manager mention anything specific they'd like you to start with?"

If yes, help them with that task directly.

**If no specific direction**, provide proactive suggestions framed for a new hire:

> "Here are things your team commonly works on that I can help you with right away:"
>
> 1. **[Common task for their department]**
>    [Brief description of what this involves]
>
> 2. **[Another common task]**
>    [Brief description]
>
> 3. **[Orientation task]**
>    [e.g., "Review the team's key processes" or "Look up recent project status"]

These should come from department context (ref-processes.md, common workflows) rather
than pain point analysis — a new hire does not have pain points yet.

> "Would you like to start with any of these, or explore something else?"

Route their choice into a working session. The onboarding is complete.

### Step 8 — Write Enrichment Data

Same as Mode 1 Step 7. Write enrichment data back via `write_employee_enrichment`
with whatever was collected during the session. For new hires, this may be minimal —
that is fine. Even recording their stated first priorities is valuable for future
sessions.

---

## What This Skill Does NOT Do

- It does not replace department-specific prompts — it routes TO them.
- It does not expose internal platform mechanics (enrichment, Cosmos profiles, mode
  detection) to the user. Everything is conversational.
- It does not make destructive changes — CLAUDE.md merge preserves existing content,
  and all other operations are read-only or additive.
- It does not require specific repos to be cloned — it uses MCP tools (Content API,
  Knower) for all data access. The CLAUDE.md write uses the local filesystem.
- It does not re-trigger onboarding for returning users — Mode 2 is deliberately
  lightweight.
- It works in Claude Code (code tab in Claude Desktop). No external tools or
  interfaces required.

## Tone Guidelines

- **Non-engineering departments (People Ops, Finance, Operations, etc.):**
  Always use plain, non-technical language. Describe what will happen, not how
  it is built. Avoid words like "repo", "deploy", "endpoint", "API", "PR",
  "merge", "pipeline". Use everyday equivalents: "your team's knowledge base"
  instead of "context repo", "send a request" instead of "file a MSG".

- **Engineering / Product:**
  Technical language is appropriate. Reference repos, PRs, architecture, and
  infrastructure directly. Include code references when relevant.

- **All users:**
  Be warm but efficient. Do not over-explain. Respect their time.
  Celebrate when things are working ("You're all set!").
  Be honest about confidence levels and limitations.
  Never fabricate data or pretend to have information you do not have.
