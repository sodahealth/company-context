---
name: getstarted
description: First-time onboarding for employees new to the Claude platform
disable-model-invocation: true
---

# /getstarted — Employee Onboarding

Welcome to the Claude platform at Evermore. This skill is the entry point for employees
using Claude for the first time.

## Step 1: Identify the User

Call the `get_my_profile` MCP tool to retrieve the caller's profile.

### If the tool succeeds (Mode A — known user with profile):

Greet the user by name using the profile data returned.

> "Hey [name]! Welcome — I've got your profile loaded. You're [role] on [team]. Let's
> get you set up."

Then load the engage prompt and route to the appropriate mode:

```
Read and follow ~/code/company-context/prompts/engage.md
```

Use the profile data to determine which mode applies:
- **New hire** (recent start date, first-time flag) → Mode A
- **Existing employee** (established, exploring Claude) → Mode B
- If unclear, start with Phase 0 (routing) from the engage prompt — it will sort it out.

### If the tool fails (Mode B1 — cold start, no MCP):

The agent MCP server may be unavailable, or the profile may not exist yet. That is fine —
fall back to a manual introduction.

> "Hey — welcome to Claude at Evermore. I wasn't able to pull your profile automatically,
> so let me get a bit of context from you.
>
> What's your name, and what team are you on? And are you new to Evermore, or have you
> been here a while and are just getting started with Claude?"

Once you have their name, role, and situation, load the engage prompt:

```
Read and follow ~/code/company-context/prompts/engage.md
```

Route to the appropriate mode based on their answers. The engage prompt's Phase 0 handles
all routing.

## What This Skill Does NOT Do

- It does not run a full session on its own — it hands off to the engage prompt.
- It does not write to any files or make system changes (Tier 1 — read + plan only).
- It does not require a terminal or Claude Code — it works in the Claude desktop app.
