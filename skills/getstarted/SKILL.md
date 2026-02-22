---
name: getstarted
description: First-time onboarding — new employees and platform introduction
---

# /getstarted — Employee Onboarding

This skill is the entry point for employees using Claude for the first time at Evermore.
It identifies the user via the MCP server and loads the appropriate onboarding prompt.

## Step 1: Identify the User

Call the `get_content` MCP tool with path `people/me` to retrieve the caller's profile.

### If the tool succeeds:

Note the user's name, role, team, and manager from the returned profile data.

Greet the user by name:

> "Hey [name]! Welcome — I've got your profile loaded. You're [role] on [team].
> Let's get you set up."

### If the tool fails:

The MCP server may be unavailable or the profile may not exist yet. That is fine —
note that the profile is unavailable and proceed. You will ask the user for context
in Step 2 fallback.

## Step 2: Get the Onboarding Prompt

Call the `get_content` MCP tool with path `prompts/onboarding` to get the onboarding
prompt for this user.

### If the tool succeeds:

Follow the returned prompt instructions exactly, passing through any profile data
from Step 1. The prompt contains the full onboarding flow — phases, questions,
outputs — tailored to the user's department.

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

## What This Skill Does NOT Do

- It does not run a full session on its own — it hands off to the prompt from `get_content`.
- It does not read local files or require any repos to be cloned.
- It does not write to any files or make system changes.
- It works in Claude Code with the evermore MCP server configured.
