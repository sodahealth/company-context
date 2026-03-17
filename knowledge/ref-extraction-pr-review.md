---
title: "How to Review Extraction PRs"
summary: "One-pager guide for department leads reviewing automated knowledge PRs"
content_type: guide
classification: public
last_verified: "2026-03-17"
---

# How to Review Extraction PRs

**Audience:** Department leads (HPS, Growth, Engineering, and other departments)

**What this is:** The Knower pipeline automatically extracts learnings from Claude sessions and proposes updates to your department's knowledge library. These proposals arrive as GitHub Pull Requests. Your job as a department lead is to confirm the content is accurate before it merges.

You do not need to understand the platform or write any code. You just need to read the proposed content and say yes or no.

---

## How to Access a PR for Review

1. You will receive a GitHub notification when a PR is assigned to you for review.
   - Check your email (GitHub sends a notification to your registered address)
   - Or go directly to: **github.com/sodahealth/company-context/pulls** and look for PRs with your name as a reviewer

2. Click the PR title to open it.

3. In the PR, click the **"Files changed"** tab to see what the pipeline is proposing to add or update.

---

## What to Verify

Review each proposed change against your knowledge of how things actually work:

| Check | What to look for |
|-------|-----------------|
| **Accuracy** | Is the described process, decision, or system behavior correct? Does it match reality as of today? |
| **Completeness** | Is anything important missing from the description? (Minor gaps are okay — perfection is not required) |
| **No sensitive data** | Does the content avoid naming individual customers, health plan sponsor PII, financial details, or anything marked confidential? |
| **Correct department scope** | Is this content actually relevant to your department, or does it belong elsewhere? |

You are **not** expected to review:
- Code or technical implementation details
- Platform configuration
- Whether the formatting is correct (CI handles that)

---

## Approval Process

### To approve a PR

1. Click **"Review changes"** (green button, upper right of the Files changed tab)
2. Select **"Approve"**
3. Click **"Submit review"**

The PR will automatically merge once approved. No further action needed.

### To request corrections

1. Click **"Review changes"**
2. Select **"Request changes"**
3. In the comment box, describe specifically what is wrong or missing:
   - *"Step 3 is incorrect — we now use the new OnRamp API, not the legacy endpoint"*
   - *"This describes SCAN's process, but it should say SummaCare here"*
4. Click **"Submit review"**

The pipeline will be notified and the PR will be revised before coming back to you.

### To reject a PR entirely

If the proposed content is wrong enough that it should not be added at all:

1. Click **"Review changes"**
2. Select **"Request changes"**
3. Write a comment explaining why the content should not be added (e.g., *"This is outdated — we no longer do this process"* or *"This contains customer-specific information that should not be in the shared library"*)
4. Also post a comment on the PR: `@umangkapadia-sodahealth — please close, not suitable for library`

Umang (IT/Security) will close the PR.

---

## Timeline Expectations

- **Target turnaround:** Within 3 business days of receiving the notification
- **If you are out of office:** Delegate to a colleague and notify Umang so temporary reviewer access can be granted
- **If you are unsure** whether something is accurate: ask the person whose session generated the learning (the PR description includes the session date and department)

There is no penalty for requesting changes or rejecting a PR. The goal is accuracy — only accurate content should enter the library.

---

## Escalation Paths

| Situation | Who to contact |
|-----------|---------------|
| Technical issue with GitHub (can't access, can't submit review) | IT Help Desk — `#it-help` on Slack |
| Content dispute (the content is wrong but you're not sure how to describe the correction) | Umang Kapadia — `@umangkapadia-sodahealth` on Slack or GitHub |
| PR about content from another department was routed to you by mistake | Comment on the PR: `@umangkapadia-sodahealth — wrong department, please re-route` |
| You want to add knowledge to the library manually (not from a session) | Open a PR directly on `company-context` or ask IT to do it for you |

---

## Quick Reference

```
Approve  →  Changes are accurate, merge them
Request changes  →  Something specific needs to be corrected
Reject  →  Content should not be added at all (tag @umangkapadia-sodahealth)
Unsure  →  Request changes and explain your uncertainty — do not approve content you cannot verify
```

---

*Questions? Contact Umang Kapadia (IT/Security) via `#it-help` on Slack.*
