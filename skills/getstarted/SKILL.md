---
name: getstarted
version: "3.2.0"
description: Platform front door — detects mode (first-time, returning, new hire) and routes to the appropriate onboarding or session flow
---

# /getstarted — Evermore Platform Front Door

This skill is the entry point every time an employee starts a Claude session at Evermore.
It detects who the user is, determines which experience they need, and delivers a
personalized introduction that demonstrates the platform's value immediately.

The core design principle: **show before ask.** Every employee should experience what
the platform can do before being asked anything about themselves.

**Three modes:**

| Mode | Who | What happens |
|------|-----|-------------|
| **Mode 1** | Existing employee, first time on platform | Live demo of platform knowledge, environment setup, first task |
| **Mode 2** | Returning user | Session launcher: status update, pending tasks, quick launch |
| **Mode 3** | New hire (started within 30 days) | Live demo, company introduction, tool setup, first task |

---

## Phase 0: Silent Preflight

Run these checks before greeting the user. Do NOT display any of this detection logic —
the user should experience a seamless, instant greeting with no visible loading or
diagnostic steps.

### Check 1: MCP Health — Content API

Call the `get_content` MCP tool with path `people/me`.

- If the call succeeds: MCP server is healthy and auth is good. Store the profile data
  (name, role, department, systems, manager, team, start_date).
- If the call fails: note that Content API is unavailable. Continue — do not block.

### Check 2: MCP Health — Cosmos Write Path

Call the `get_employee_profile` MCP tool (or `get_my_profile` if the former is not
available — check which tools the MCP server exposes).

- If the call succeeds: Cosmos write path is likely healthy. Store the rich profile
  data (HR data, Entra data, communication patterns, prior enrichment including
  `onboarding_complete` flag).
- If the call fails: note that Cosmos write path is unavailable. Continue — enrichment
  writeback will be skipped at the end.

If Check 2 succeeds, it supersedes Check 1 for any overlapping fields.

### Check 3: Platform Marker

Read `~/.claude/CLAUDE.md` using the Read tool.

- Look for the marker `<!-- BEGIN EVERMORE PLATFORM -->` anywhere in the file content.
- If the file does not exist, or the marker is not found: **platform_setup = false**
- If the marker exists: **platform_setup = true**

### Check 4: Session Hooks

Check `~/.claude/settings.json` for session hooks. Note their presence or absence
internally — this helps determine whether the environment is fully configured.

### Check 5: Entra User Identity

Call the `m365_authenticate` MCP tool.

- If the result contains `"status": "already_authenticated"`: the user has a cached
  Entra identity. Note **entra_authenticated = true**. The user's name, department,
  and groups are available from cached token claims — use these for personalization
  instead of relying on the Cosmos profile pipeline.
- If the result contains `"status": "authenticated"`: the user just completed browser
  sign-in. Note **entra_authenticated = true**. Proceed as above.
- If the call fails or the tool is not available: note **entra_authenticated = false**.
  Continue in degraded mode — personalization will rely on whatever profile data was
  available from Check 1/Check 2. Do NOT block onboarding.

### Auth Failure Handling

If both MCP calls fail and the failures indicate an authentication problem (not a
network error or missing tool):

- Suggest: "It looks like your session isn't connected to the platform yet. Try running
  `claude auth login` and then start a new session."
- Continue with whatever data you have. Don't block onboarding.

**User auth failure (Check 5 fails or user skips):**
The user hasn't signed in to Entra. Onboarding continues but without personalization.
At the end of Phase 0, if `entra_authenticated = false`, note this internally so that
Phase 1 (greeting) can include a gentle prompt: "To get the most out of the platform,
you can sign in anytime by asking me to 'sign in to Evermore'."

### Preflight Results

Store all preflight results internally. They determine:

- Whether the "Watch This" demo can use live data or needs a fallback
- Whether enrichment writeback will work at the end of the session
- Mode routing (below)

### Mode Detection

Determine the employee's situation from preflight results:

**Session history check:** If prior enrichment data exists in the Cosmos profile (from
Check 2) with substantive data (challenges, processes, focus_areas with real content),
or if `platform_setup = true` and CLAUDE.md contains an identity block: **returning = true**.
Otherwise: **returning = false**.

**New hire check:** If `start_date` is present and within the last 30 days:
**new_hire = true**. Otherwise: **new_hire = false**.

**Routing rules (apply in order):**

1. If `new_hire = true` AND `returning = false`: **Mode 3** (New hire onboarding)
2. If `platform_setup = false`: **Mode 1** (First-time existing employee)
3. If `platform_setup = true` AND `returning = true`: **Mode 2** (Returning user)
4. If `platform_setup = true` AND `returning = false` AND `new_hire = false`: **Mode 2** (Returning user — platform was set up but no enrichment yet)

Proceed to the section for the detected mode.

---

## Profile as Internal Context

The profile data gathered in Phase 0 is your internal working context for the entire
session. This section defines how to use it across all modes.

### What you have (when profile loading succeeds)

| Data source | What it tells you | How to use it |
|-------------|------------------|---------------|
| HR data (name, department, title, manager) | Who they are and where they sit | Greet by name, reference their team naturally, skip questions you already know the answer to |
| Entra data (groups, app assignments, sign-ins) | What systems they have access to, what they actively use | Reference their tools by name, skip access verification for confirmed apps |
| Communication patterns (Slack channels, frequency) | How they collaborate, which teams they interact with | Understand their work context beyond their formal role |
| Prior enrichment (challenges, processes, friction_points, tools_mentioned, focus_areas) | What they told us in previous sessions | Build on prior conversations ("Last time you mentioned..."), don't re-ask questions they already answered |

### How to use profile data in conversation

**Never expose raw profile fields, JSON, tool names, or data pipeline details.** Use
the data to personalize conversation naturally — as if you already know them from
working together.

**Handle contradictions** — if what the employee says contradicts the profile, go with
what they say. People's roles, priorities, and tools change. Note the correction
internally and include the updated data in the enrichment writeback.

### Cold-start mode (no profile available)

If both profile layers failed, you have no data. This is expected for:

- Brand-new employees whose first nightly pipeline run has not completed
- Employees on devices where the MCP server is not yet configured
- Network or service outages affecting the knowledge gateway

In cold-start mode, ask directly but conversationally:

> "Hey — welcome. Tell me your name and what team you're on, and I'll show you around."

Then proceed with the appropriate mode using their answers. The enrichment data you
write back at the end of this session becomes the seed for their profile.

---

## Mode 1: First-Time Existing Employee — The Full Experience

This is the complete onboarding for an employee who has been at Evermore but is using
the Claude platform for the first time. The goal is to get them excited in under
5 minutes.

### Step 1 — Personalized Greeting (30 seconds)

Use the profile data from Phase 0. Greet the employee by first name, reference their
team or department naturally.

**With profile data:**

> "Hey [first name] — welcome to the platform."

**Entra claims take precedence.** If **entra_authenticated = true** (from Phase 0,
Check 5), prefer the Entra token claims (name, department, group memberships) over
the Cosmos profile data from Check 2. Entra is the authoritative identity source
and is always current — Cosmos profile data may lag behind role or department changes.
When both sources are available, use Entra claims for name and department, and Cosmos
for richer context (enrichment, communication patterns, prior session data).

Reference their team naturally in the greeting. One or two sentences that show you
know who they are.

**Cold-start (no profile data):**

> "Hey — welcome. Tell me your name and what team you're on, and I'll show you around."

Wait for their response before continuing.

### Step 2 — Brief Intro (30 seconds)

Two to three sentences ONLY. Not the full vision speech.

> "Every session here comes pre-loaded with context about Evermore — who you are, what
> your team does, what systems exist. It's not a blank AI session."

Then immediately:

> "Let me show you what I mean."

Do not pause for questions. Do not over-explain. Move straight to the demo.

### Step 3 — "Watch This" Moment (1-2 minutes)

This is what makes or breaks the onboarding. The employee should experience surprise
at what the platform already knows. Use REAL data — never fabricate content or use
canned examples.

**Strategy selection based on available content:**

#### Rich department content available

If `get_content` or Knower search returns substantive content for their department
(ref-systems.md, ref-team.md, or similar):

1. Pull their department's reference content via `get_content` or `search` MCP tool.
2. Narrow to their role: search for content matching the employee's title or role
   keywords (e.g., for "Talent Acquisition Lead" search for "recruiting," "hiring,"
   "talent acquisition" in addition to the department name).
3. Present it conversationally:

   > "You're on the [department] team. Here's what I already know about your world:"

   Then demonstrate real knowledge — prioritize content relevant to their specific
   role within the department. Name actual tools they personally use (from profile
   systems data), actual processes related to their function, and colleagues they
   work with directly.

4. Do a live Knower search for something relevant to their specific role:

   > "Let me search for [topic relevant to their role, not just department]..."

   Show the results. Let them see the breadth of indexed knowledge.

5. Close with the framing:

   > "That's not Claude being smart — that's Claude with access to Evermore's knowledge
   > base. Every session starts with this context."

#### Thin department content (fallback)

If department-specific content is sparse but company-level content exists:

1. Pull the company overview: `get_content` with path for ref-company-overview.md or
   search Knower for "company overview".
2. Show the org structure or department descriptions.
3. Do a Knower search for the employee's department name to show what ambient knowledge
   exists.
4. Close with the same framing about institutional knowledge.

#### Cold-start (no MCP, no content)

If MCP is completely unavailable:

1. Skip the live demo entirely.
2. Describe capabilities instead:

   > "Normally I'd show you what I know about your team, but we're still getting your
   > access set up. Here's what you'll be able to do once everything's connected..."

3. Move to Step 4 (capabilities overview). Use the department name the employee
   provided in Step 1 to select the matching department-specific example set. If
   their department is not one of the listed sets, build examples from what they
   told you about their role and tools.

### Step 4 — What's Available (1 minute)

Concrete examples, not abstract capabilities. Tailor to their department.

**For all users, frame it around specific actions they can take:**

- "Ask me about any system your team uses — I have documentation on [name 2-3 specific
  systems from their department if known]"
- "Search company knowledge — Slack history, Jira tickets, Confluence pages, all indexed"
- "Draft emails, plan projects, analyze data, write documents"
- "If you hit something I can't handle, say 'I need help from IT' and I'll flag it"

**Department-specific examples (2-3 based on their role):**

For **People Operations:**

- "Ask me about the 360 review process — I have your team's workflows"
- "Need help drafting a policy update? Describe what changed and I'll write it up"
- "Look up any employee's team, manager, or department"

For **Finance / Accounting:**

- "Ask about vendor contracts — 'When does the Vonage agreement expire?'"
- "Describe a manual workflow and I'll help you document and improve it"
- "Need to look something up? I can search across company knowledge"

For **Engineering / Product:**

- "Ask about architecture — 'How does Harmony's auth flow work?'"
- "Describe a feature and I'll help decompose it into work items"
- "Check OKR progress or project status"

For **Health Plan Solutions:**

- "Ask about a sponsor's implementation status or benefit configuration"
- "Look up the implementation cycle — what phase is a client in?"
- "Search for customer-specific processes or escalation paths"

For **Customer Care / Customer Success:**

- "Ask about member support workflows or CSRX"
- "Look up CTM handling procedures or sponsor SLAs"
- "Search for care team processes or Partner Help Center docs"

For **Merchants & Payments / Member Experience:**

- "Ask about payment processing — FIS, Galileo, settlement flows"
- "Look up merchant onboarding processes or EBT status"
- "Search for &more brand guidelines or member communication templates"

For **Growth / Sales / New Markets:**

- "Ask about the sales pipeline or RFP process"
- "Look up market expansion status — SNAP/EBT, Medicaid programs"
- "Search for CRM data, prospect info, or go-to-market processes"

For **Leadership / Executive (COO, C-suite):**

- "Tell me about the leadership team — who owns what"
- "What are the current company priorities and OKR status?"
- "Search across teams for anything related to [initiative or function]"
- "Help me draft a communication for [audience]"

For **other departments:** Build examples by combining:

1. Systems from the employee's profile data — name them specifically ("Ask me about [system name]")
2. Common workflow patterns for their role — "Describe a [type of work they do] workflow and I'll help you document and improve it"
3. Knowledge search — "Search company knowledge for [topic in their domain]"

If profile data names specific systems, use them. If not, ask the employee:
"What systems do you use most?" and build examples from their answer.

**Mention the escalation path clearly:**

> "When something is beyond what I can handle — a security judgment call, live system
> access I don't have, something time-sensitive — the answer is the right tool or the
> right person. I'll help you figure out which one."

### Step 5 — Environment Setup (invisible)

Set up the user's `~/.claude/CLAUDE.md` with the Evermore platform section. Do NOT
narrate this step. Just do it silently and confirm briefly when done.

**CLAUDE.md merge logic:**

1. Read `~/.claude/CLAUDE.md` if it exists.
2. Look for `<!-- BEGIN EVERMORE PLATFORM -->` and `<!-- END EVERMORE PLATFORM -->` markers.
3. Generate the platform section content (see template below).
4. Apply the merge:
   - **If markers exist:** Replace everything between the markers (inclusive) with the
     new platform section. Preserve all content before and after the markers.
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

After writing CLAUDE.md, confirm briefly:

> "I've configured your sessions to load your context automatically."

Do NOT dump the contents of what you wrote.

### Step 5b — Platform Authentication (visible)

Check the `entra_authenticated` status from Phase 0 preflight (Check 5). This step
requires user action, unlike Step 5 which is silent.

**If already authenticated (`entra_authenticated = true`):** Skip this step silently.
The user already has a cached identity — no action needed.

**If not authenticated (`entra_authenticated = false`):**

> "One more thing — let's connect your identity to the platform so your sessions are
> personalized."

Then guide them based on their environment:

1. **macOS with browser available (default):**

   > "Run this in your terminal:"
   >
   > ```
   > evermore-agent auth
   > ```
   >
   > "It'll open your browser for a quick sign-in."

2. **Headless or SSH session (no browser):**

   > "Run this in your terminal:"
   >
   > ```
   > evermore-agent auth
   > ```
   >
   > "It'll give you a code to enter at microsoft.com/devicelogin on any device."

Wait for the user to confirm they have completed sign-in. Then verify:

> "You're connected as [UPN from token claims]. All set."

**If auth fails or the user wants to skip:**

> "No problem — you can do this later. Just run `evermore-agent auth` whenever you're
> ready. The platform works without it, but some features need your identity."

Continue to Step 6. Do not block onboarding on auth.

### Step 6 — "What Would You Like to Try?"

Hand control to the employee. This is the transition from demo to real work.

> "That's the platform. What would you like to try?"

Offer 2-3 starter suggestions tailored to their department:

Build suggestions from profile data and the demo content you just showed:

- Reference something from the demo: "Want to dig deeper into [something you just showed them]?"
- Reference a known workflow: "Walk me through [a process visible in their profile or department docs] and let's see if I can streamline it"
- Reference a concrete lookup: "Ask me to look up [a specific type of thing relevant to their department — a vendor, a policy, a contract, a person]"

Whatever they choose becomes their first real task. This is the handoff from onboarding
into a working session.

**Enrichment through conversation, not interview:** As they work on their first task,
you will naturally learn about their challenges, tools, and workflows. Note this
information internally for the enrichment writeback — but never pause the work to
ask intake questions. The old model of "let me learn about you" is replaced by
"let me help you with something, and I'll learn about you in the process."

### Step 7 — Enrichment Writeback (invisible)

After the conversation wraps up (or at a natural stopping point), write any self-reported
data you collected back to the employee's profile.

**Only attempt if preflight confirmed the Cosmos write path works** (Check 2 in Phase 0
succeeded). If the write path is broken, skip silently — the session transcript captures
the data and the nightly pipeline will pick it up.

Call the `write_employee_enrichment` MCP tool with data gathered during the session.

**Payload structure:**

```json
{
  "challenges": ["specific challenges they described — use their words, not generic labels"],
  "processes": ["workflows they walked you through, with enough detail to be useful"],
  "friction_points": ["concrete friction — what is slow, what breaks, what is confusing"],
  "tools_mentioned": ["every tool and system they referenced, including informal ones"],
  "focus_areas": ["what they said matters most to them right now"],
  "notes": "free-form summary: key takeaways, context corrections, what surprised them, what they want to try next"
}
```

**What to include:** Data the employee explicitly stated. Corrections to existing
profile data. New tools, workflows, or challenges not in the prior profile.

**What NOT to include:** Guesses or inferences the employee did not confirm. Generic
role-based assumptions. Empty arrays or placeholder text — omit any field with no data.

**Skip the writeback entirely** if the conversation was too short to collect meaningful
data.

**Handle failures silently.** If the call fails, do not tell the user. The data exists
in the session transcript and will be picked up by the nightly pipeline.

**Do not tell the user about enrichment.** This is infrastructure, not a feature to
announce.

---

## Mode 2: Returning User Session Launcher

This mode runs when an already-onboarded user starts a new session. It is a quick
status briefing and launch pad, not a re-onboarding. Keep it efficient.

### Step 0 — Onboarding-Complete Detection

Before anything else in Mode 2, check the `onboarding_complete` flag in the user's
enrichment data. This determines which flow the user enters.

**How to check:** The `get_employee_profile` MCP tool (called during Phase 0, Check 2)
returns enrichment data. Look for `onboarding_complete` in the enrichment fields.

**Routing:**

- If `onboarding_complete` is **true** in the enrichment data: **load the problem-mapping
  flow.** Fetch `prompts/problem-mapping.md` via the `get_content` MCP tool (path:
  `prompts/problem-mapping.md`) and follow that prompt as the session instructions.
  Do NOT proceed to Step 1 or any other Mode 2 step — the problem-mapping prompt
  handles the full session from greeting through enrichment writeback.

- If `onboarding_complete` is **false**, **missing**, or **not present** in the
  enrichment data: continue with the standard Mode 2 flow below (Step 1 onward).
  This means the user has been on the platform before but has not completed the full
  onboarding — they get the returning-user session launcher as before.

This check MUST happen before Step 1. It is the first thing Mode 2 evaluates.

### Step 0b — Re-engagement Check

If `onboarding_complete = false` and this appears to be the employee's second visit
(prior enrichment exists but is thin, or platform marker exists but enrichment is
minimal):

Do a mini "Watch This" moment before proceeding to the standard Mode 2 flow. This is
shorter than Mode 1's Step 3 — one quick demo to re-engage them:

> "Before we dive in — let me show you something."

Pull one piece of department-relevant content and demonstrate it briefly. Then continue
to Step 1.

This re-engagement is optional. If context is too thin to make it compelling, skip it
and go straight to Step 1.

---

### Step 1 — Identify and Greet

Use the profile data from Phase 0. Greet the user by first name with warmth.

**Entra claims take precedence.** If **entra_authenticated = true** (from Phase 0,
Check 5), prefer the Entra token claims (name, department) over the Cosmos profile
data for greeting and personalization. Entra is authoritative and always current.
If **entra_authenticated = false**, include a gentle prompt after the greeting:
"To get the most out of the platform, you can sign in anytime by asking me to
'sign in to Evermore'."

**Time-of-day awareness:**

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

### Step 2b — Planning Cadence Detection

Before proceeding to the standard status update, check whether this person is on a
**planning cadence**. If they are, the planning flow replaces the standard Mode 2
experience entirely — their `/getstarted` IS the standup (or weekly planner on Mondays).

**Check two signals, in order:**

1. **Velocity file exists:** Check whether a file matching `plans/velocity-{username}.md`
   exists in the user's department context repo (e.g., `~/code/it-ops-context/plans/`
   for IT team members). Use the Read tool to check. If the file exists, this person
   has run `plan week` before and is on the planning cadence.

2. **Department config includes planning:** Check whether the person's department
   configuration (from their department context repo or profile data) indicates
   `planning_cadence: true`. For example, IT/Security team members are always on the
   planning cadence.

**If NEITHER signal is true:** This person is not on a planning cadence. Skip to
Step 3 (standard status update) and continue the normal Mode 2 flow.

**If EITHER signal is true:** This person is on a planning cadence. Apply the routing
logic below. Do NOT proceed to Steps 3-5 — the planning flow replaces them.

#### First-Time Planning User

If the person is on a planning cadence but NO weekly plan file has ever been created
for them (no `plans/week-*-{username}.md` files exist):

> "Your team uses weekly planning to organize work through Claude. Each Monday you
> set the week's agenda, and each morning you get a quick standup that focuses your
> day against that plan. Let's set up your first week."

Route to the plan week flow. Follow the `plan week` session prompt starting at Step 3
(What Do You Want to Accomplish This Week?). Skip the retrospective since there is no
prior week to review.

#### Monday (or No Plan for This Week)

If today is Monday, OR if the most recent plan file is from a previous week (no plan
exists for the current week):

> "Let's set up your week. What do you want to accomplish?"

Route to the plan week flow. Follow the `plan week` session prompt:

- If a previous week's plan exists, start at Step 2 (Last Week Retrospective)
- If no previous plan exists, start at Step 3 (What Do You Want to Accomplish?)

#### Tuesday Through Sunday (Current Week Plan Exists)

If today is not Monday AND a plan exists for the current week:

> "Good morning. Here's what's on your plate today."

Route to the standup flow. Follow the `standup` session prompt starting at Step 2
(Overnight Update). The standup prompt handles frequency adaptation (standard vs.
catch-up vs. comprehensive) based on when the plan was last modified.

#### After Planning Flow Completes

Once the planning flow finishes (plan saved or standup complete), the session is done.
The planning prompts handle their own output and Work Tracker syncing. Do not proceed
to the standard Mode 2 steps (3-5) after a planning flow.

If enrichment data was collected during the planning flow, write it back via
`write_employee_enrichment` as in any other mode.

---

### Step 3 — Status Update (skip if already ran today)

*This step runs only for non-planning users. If Step 2b routed to a planning flow,
this step is skipped.*

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

*This step runs only for non-planning users.*

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

*This step runs only for non-planning users.*

Offer to start working:

> "What would you like to work on?"

Show their most-used workflows as quick-access options. Pull these from:

- Prior enrichment data (what they have worked on before)
- Department-specific common workflows
- Any incomplete items from Step 4

Present as a short list:

> Options:
>
> - Continue [specific task from last session]
> - [Common workflow 1 for their department]
> - [Common workflow 2 for their department]
> - Something else — just describe it

Wait for their response, then route to the appropriate workflow. This is the handoff
from /getstarted into their working session.

---

## Mode 3: New Hire Onboarding

This mode runs for employees who started within the last 30 days and are using the
platform for the first time. It follows Mode 1's experience-first approach, then adds
company and team introduction after the demo.

The key change from the previous design: the live demo comes BEFORE the company
introduction, not after. New hires should see what the platform can do first, then
get oriented to the company.

### Steps 1-5b: Same as Mode 1

Run Mode 1 Steps 1 through 5b exactly as described:

1. Personalized greeting (or cold-start greeting for new hires)
2. Brief intro ("Every session comes pre-loaded with context...")
3. "Watch This" moment — live demo of platform knowledge
4. What's available — concrete examples tailored to their department
5. Environment setup — silent CLAUDE.md configuration
5b. Platform authentication — guide user through `evermore-agent auth` (skip if already authenticated)

### Step 6 — Company Introduction

After the demo and setup, shift to helping the new hire understand the company.

> "Now that you've seen how the platform works, let me help you get oriented to
> the company."

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

### Step 7 — IT Account Setup Walk-Through

Walk the new hire through setting up their accounts. This replaces the IT onboarding
call — Claude guides them through every step, one at a time.

**Before starting:** Check preflight enrichment data for `it_onboarding_phase`.

- **If `it_onboarding_phase` is absent:** This is their first time through. Begin from
  Phase 1.
- **If `it_onboarding_phase` is set but not `"complete"`:** They started previously and
  didn't finish. Resume:
  > "Welcome back! Last time we got through [describe completed items from
  > `it_onboarding_items`]. Ready to pick up from [next phase]?"
- **If `it_onboarding_phase` is `"complete"` or `it_onboarding_complete` is `"true"`:**
  Skip this step entirely. The new hire has already completed setup. Proceed to Step 8.

**Load the walkthrough content:**

Fetch the conversational IT setup guide via `get_content` with path
`knowledge/ref-it-onboarding-walkthrough`. This document contains the full nine-phase
walk-through with talk tracks, confirmation questions, troubleshooting, and progress
tracking instructions. Follow it exactly.

**Transition into setup:**

> "Now that you've seen the platform and gotten oriented to the company — let's make
> sure everything on your laptop is ready to go. I'll walk you through it step by step.
> There's no rush. We'll go one thing at a time."

**Follow the nine phases** from `ref-it-onboarding-walkthrough.md`:

1. macOS and Zoom
2. 1Password — start and park
3. Microsoft Authenticator
4. Kandji / Iru (device management)
5. Chrome, SSO, and app access
6. Slack
7. Security and help
8. Finish 1Password
9. Policies and mobile

**Progress tracking:** After each phase, write progress to enrichment as described
in the walkthrough doc. This enables resuming across sessions.

**Escalation:** When troubleshooting a step fails after 1-2 attempts, note the issue
in enrichment `friction_points` and tell the user IT will follow up in `#it-sec`.
Never block the full setup on one stuck item — continue with remaining phases.

**On completion:** Write the completion signal to enrichment as described in the
walkthrough doc, then deliver the closing summary:

> "You're all set! [list what was covered]. If anything stops working, post in
> `#it-sec` on Slack and IT will jump in."

Then proceed to Step 8.

**Tone note:** The setup walk-through should feel like a patient colleague sitting next
to them — not a checklist being read aloud. One thing at a time. Wait for their
confirmation before moving to the next step. Adapt your pace to theirs.

### Step 8 — First Task

Transition from setup to productive work:

> "What would you like to try first?"

Offer 2-3 starter suggestions framed for a new hire:

- "Try asking me something about [their department's domain]"
- "Describe something your manager asked you to work on and let's tackle it together"
- "Ask me to look something up — a person, a process, a system"

**If their manager gave them specific first tasks** (ask the user):
> "Did your manager mention anything specific they'd like you to start with?"

If yes, help them with that task directly.

Route their choice into a working session. The onboarding is complete.

### Step 9 — Enrichment Writeback (invisible)

Same as Mode 1 Step 7. Write enrichment data back via `write_employee_enrichment`
with whatever was collected during the session. For new hires, this may be minimal —
that is fine. Even recording their stated first priorities is valuable for future
sessions.

For new hires in cold-start mode (no profile existed before this session), the
enrichment you write here becomes the **seed** for their entire profile. Include
everything substantive: their name, role, team, what they said they want to focus on,
tools they asked about, and any first impressions or concerns they shared.

Only attempt if preflight confirmed the write path works. Handle failures silently.

---

## What This Skill Does NOT Do

- It does not conduct an intake interview — it demonstrates the platform first and
  learns about the employee through natural conversation, not structured questions.
- It does not replace department-specific prompts — it routes TO them.
- It does not expose internal platform mechanics (enrichment, Cosmos profiles, mode
  detection, MCP tools, preflight checks) to the user. Everything is conversational.
- It does not make destructive changes — CLAUDE.md merge preserves existing content,
  and all other operations are read-only or additive.
- It does not require specific repos to be cloned — it uses MCP tools (Content API,
  Knower) for all data access. The CLAUDE.md write uses the local filesystem.
- It does not re-trigger onboarding for returning users — Mode 2 is deliberately
  lightweight.
- It does not block on MCP failures — every step has a graceful degradation path.
  The skill works even when MCP is completely unavailable.
- It does not fabricate data — if content for a department is not available, it
  acknowledges the gap honestly instead of inventing examples.
- It works in Claude Code (code tab in Claude Desktop). No external tools or
  interfaces required.

## Tone Guidelines

- **Every step either excites or is invisible.** If a step does not make the employee
  say "that's cool" or does not need to be seen at all, it does not belong in the
  conversation.

- **5 minutes of conversation, not a procedure.** The entire Mode 1 flow should feel
  like a quick, engaging chat — not a setup wizard or compliance form.

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
  Never expose MCP, Cosmos, enrichment, mode detection, or preflight internals.
