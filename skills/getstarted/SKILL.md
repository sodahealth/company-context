---
name: getstarted
description: First-time onboarding — new employees and platform introduction
---

# /getstarted — Employee Onboarding

This skill is the entry point for employees using Claude for the first time at Evermore.
It identifies the user via the MCP server, loads their rich profile if available, and
runs the appropriate onboarding prompt. After the conversation, it writes enrichment
data back to the employee's profile.

## Step 1: Identify the User

Call the `get_content` MCP tool with path `people/me` to retrieve the caller's basic profile.

### If the tool succeeds:

Note the user's name, role, team, and manager from the returned profile data.

Greet the user by name:

> "Hey [name]! Welcome — I've got your profile loaded. You're [role] on [team].
> Let's get you set up."

### If the tool fails:

The MCP server may be unavailable or the profile may not exist yet. That is fine —
note that the profile is unavailable and proceed. You will ask the user for context
in the fallback flow.

## Step 2: Get Rich Employee Profile

Call the `get_employee_profile` MCP tool to retrieve the caller's full Cosmos-backed
profile. This profile contains richer data than the basic profile from Step 1:

- HR data: department, title, manager, start date
- Entra data: group memberships, app assignments, recent sign-in activity
- Communication patterns: active Slack channels, activity frequency
- Prior enrichment: self-reported data collected from previous sessions

### If the tool succeeds:

Merge the Cosmos profile with the basic profile from Step 1. The Cosmos profile takes
precedence where fields overlap — it is the richer, more current data source. Hold
all of this data for use by the onboarding prompt in Step 3.

Do NOT dump the raw profile to the user. The prompt will use it to personalize the
conversation naturally.

### If the tool fails:

This is expected in several cases:
- The `get_employee_profile` tool may not be available yet on this MCP server
- The employee may be too new to have a Cosmos profile (pipeline hasn't run)
- The Cosmos database may be temporarily unreachable

**Continue with the basic profile from Step 1 only.** Log internally that the Cosmos
profile was not available, but do not surface this to the user. The onboarding
experience works fine without it — there will just be more discovery questions.

## Step 3: Get the Onboarding Prompt

Call the `get_content` MCP tool with path `prompts/onboarding` to get the onboarding
prompt for this user.

### If the tool succeeds:

Follow the returned prompt instructions exactly, passing through all available profile
data (basic profile from Step 1 and Cosmos profile from Step 2, if available). The
prompt contains the full onboarding flow — phases, questions, outputs — and will use
the profile data to personalize the conversation.

### If the tool fails:

Fall back to a basic welcome. Ask the user:

> "I wasn't able to load the onboarding materials automatically. Let me get
> some context from you instead.
>
> What's your name, your role, and what team are you on? Are you new to
> Evermore, or have you been here a while and are getting started with Claude?"

Then provide a basic orientation:
- Explain that Evermore uses Claude across the organization for work automation
- Ask about their focus areas and what they'll primarily be working on
- Suggest they reach out to their manager or IT for the full onboarding experience

## Step 4: Write Enrichment Data Back

After the full onboarding conversation completes (all phases of the prompt have been
followed, the final report has been generated), call the `write_employee_enrichment`
MCP tool with the data collected during the conversation.

### What to write:

Structure the enrichment payload from what the employee shared during the session:

```json
{
  "challenges": ["list of challenges they mentioned"],
  "processes": ["workflows and processes they described"],
  "friction_points": ["pain points and frustrations"],
  "tools_mentioned": ["tools and systems they referenced"],
  "focus_areas": ["their stated priorities"],
  "notes": "free-form summary of key takeaways from the conversation"
}
```

Only include fields where the conversation surfaced meaningful data. Do not fabricate
or pad the enrichment — if a field has nothing substantive, omit it.

### When to skip:

Do NOT call `write_employee_enrichment` if:
- The conversation was too short to collect substantive data
- The user dropped off before engaging meaningfully
- No real challenges, processes, or priorities were discussed

A brief greeting with no substance is not worth writing back.

### If the tool fails:

Handle silently. Do not surface write errors to the user — the enrichment writeback
is a background improvement to their profile, not part of their onboarding experience.
The conversation was still successful even if the writeback fails.

## What This Skill Does NOT Do

- It does not run a full session on its own — it hands off to the prompt from `get_content`.
- It does not read local files or require any repos to be cloned.
- It does not write to any files or make system changes.
- It works in Claude Code with the evermore MCP server configured.
- It does not expose profile data or enrichment mechanics to the user — these are
  internal to the platform.
