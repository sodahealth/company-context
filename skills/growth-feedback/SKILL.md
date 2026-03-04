---
name: growth-feedback
version: "1.0.0"
description: Submit structured feedback on Growth CRM tools — files a tracked request for the engineering team to review
---

# /growth-feedback — Growth CRM Feedback

This skill helps you submit feedback about the Growth CRM tools (briefing pages, account
views, pipeline, emails, etc.). Your feedback gets filed as a tracked request that the
engineering team will review and prioritize.

You do not need to know anything technical. Just describe what you want changed and this
skill handles the rest.

---

## Step 1: Ask What They Want to Change

Start with a friendly, plain-language prompt:

> What would you like to change about the Growth CRM tools?
>
> Just describe it in your own words — it can be something broken, something confusing,
> or an idea to make things better.

Wait for the user's response. Do NOT proceed until they have described their feedback.

---

## Step 2: Two Clarifying Questions

After the user describes their feedback, ask **exactly two** follow-up questions.
Present them together in a single message so the user can answer both at once.

**Question 1 — Which area?**

> Which tool or page does this relate to?
>
> - Briefing pages
> - Accounts
> - Pipeline
> - Emails
> - Other (just tell me which)

**Question 2 — How important is this to you?**

> How much does this affect your work?
>
> - **It's blocking my work** — I can't do what I need to do
> - **It would improve my workflow** — I can work around it, but it slows me down
> - **Nice to have** — not urgent, just a suggestion

Wait for the user's answers before continuing.

---

## Step 3: Build the Structured Preview

Using the user's responses from Steps 1 and 2, build a GitHub issue and show a preview.

### Title

Generate a short UUID (8 characters) and create the title:

```
FEEDBACK-{uuid8}: {one-line summary of the feedback}
```

The one-line summary should be written in plain language based on what the user described.

### Priority Mapping

Map the user's importance answer to a priority label:

| User said | Priority label |
|-----------|---------------|
| Blocking my work | `priority:high` |
| Would improve my workflow | `priority:routine` |
| Nice to have | `priority:routine` |

### Issue Body

Structure the body as follows (fill in from the user's answers):

```markdown
## Area

{Which tool/page they selected}

## What happens now

{Current behavior or pain point, based on what they described}

## What I'd like instead

{Desired behavior or change, based on what they described}

## Context

- Submitted by: Growth team member
- Importance: {their importance answer}
```

### Show the Preview

Display the preview to the user in a clear, readable format:

> Here's what I'll submit on your behalf:
>
> **Title:** FEEDBACK-{uuid8}: {summary}
>
> **Area:** {area}
>
> **What happens now:** {current behavior}
>
> **What I'd like instead:** {desired behavior}
>
> **Priority:** {high or routine}
>
> Does this look right? I can adjust anything before submitting.

Wait for the user to confirm or request changes. If they want changes, update the
preview and show it again. Do NOT file the issue until the user confirms.

---

## Step 4: File the GitHub Issue

Once the user confirms, file the issue using `gh issue create` on the
`sodahealth/it-ops-context` repository.

Run the following command:

```bash
gh issue create \
  --repo sodahealth/it-ops-context \
  --title "FEEDBACK-{uuid8}: {summary}" \
  --label "from:growth-team" \
  --label "to:solutions-engineer" \
  --label "status:pending" \
  --label "priority:{mapped}" \
  --label "triage:needs-work-plan" \
  --body "{structured body from Step 3}"
```

**Labels explained (you do NOT need to share these details with the user):**

| Label | Purpose |
|-------|---------|
| `from:growth-team` | Identifies this as Growth team feedback |
| `to:solutions-engineer` | Routes to the SE for review |
| `status:pending` | Marks as not yet started |
| `priority:{mapped}` | High or routine, based on importance |
| `triage:needs-work-plan` | Ensures the SE decomposes this into actionable work before anyone starts building |

---

## Step 5: Confirm

After the issue is created successfully, confirm with a simple message:

> Filed as #{number}. The SE will review and you'll get a Slack DM when it's picked up.

If the issue creation fails for any reason, tell the user:

> Something went wrong filing the request. Let me try again.

Then retry once. If it fails again:

> I wasn't able to file this automatically. I've saved your feedback — please let
> Umang know and he'll file it manually.

---

## Tone and Language Rules

- Use plain, conversational language throughout. No technical jargon.
- Never mention repos, APIs, labels, triage, or engineering processes to the user.
- The user should feel like they're talking to a helpful teammate, not filling out a form.
- Keep responses short. Don't over-explain.
- If the user's feedback is vague, it's okay — the SE will clarify during review.
  Do NOT interrogate the user beyond the two clarifying questions.
