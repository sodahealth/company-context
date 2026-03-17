---
title: "How to Review Extraction PRs — Department Lead Guide"
content_type: reference
classification: public
last_verified: "2026-03-17"
review_cycle_days: 180
---

# How to Review Extraction PRs

**For:** Department leads assigned as CODEOWNERS in company-context
**Purpose:** Guide department leads through reviewing and approving knowledge extraction pull requests

---

## What Is an Extraction PR?

When the Claude AI platform extracts information from sessions — meeting notes, processes, decisions, people context — it opens a pull request in GitHub to add or update files in your department's folder (`departments/{your-dept}/`).

You will receive an email from GitHub (or a Slack notification if configured) when a PR requires your review.

**Your job:** Confirm that the extracted content is accurate, or request corrections before it's merged into the shared knowledge base.

---

## How to Access and Review a PR

1. **Open the PR link** from your email notification or from [github.com/sodahealth/company-context/pulls](https://github.com/sodahealth/company-context/pulls)
2. Click the **"Files changed"** tab to see what was added or modified
3. Review the content — read through each changed file:
   - Is the information accurate as stated?
   - Does anything contradict what you know to be true?
   - Is anything missing that would make the entry misleading without it?
4. Add a **line comment** on any specific section that needs correction (click the `+` icon that appears when you hover over a line)
5. When finished, click **"Review changes"** and choose one of:
   - **Approve** — content is accurate; safe to merge
   - **Request changes** — content needs correction before merging
   - **Comment** — you have questions but aren't blocking

---

## What to Verify

Focus on factual accuracy, not writing style. Ask yourself:

| Check | What to look for |
|-------|-----------------|
| **Accuracy** | Are names, titles, roles, and responsibilities correct? |
| **Currency** | Is this still true today, or has it changed? |
| **Completeness** | Is anything omitted that would change how this is interpreted? |
| **Sensitivity** | Does this include information that should not be shared widely? |
| **Attribution** | Are people described fairly and in the right context? |

You do **not** need to check technical platform details (file formats, frontmatter fields) — those are handled by the pipeline.

---

## Approval: When to Approve, Request Changes, or Escalate

**Approve when:**
- The content accurately reflects your department's knowledge, people, or processes
- Any minor phrasing differences do not change the meaning

**Request changes when:**
- Facts are incorrect (wrong title, wrong team, outdated process)
- Sensitive information is present that should not be in the shared knowledge base
- The content is missing critical context that makes it misleading

**Escalate when:**
- You are unsure whether certain information is appropriate to publish
- The PR touches multiple departments and you can only speak to your own
- You suspect the extraction captured something from a confidential source

---

## Escalation Paths

| Situation | Who to contact |
|-----------|---------------|
| Technical issue with the PR or GitHub | IT/Security — Umang Kapadia (`#it-security`) |
| Content dispute about another department's data | The other department's lead directly |
| Sensitive or confidential content question | IT/Security — Umang Kapadia (`#it-security`) |
| Platform question (how Claude extracts, what gets stored) | IT/Security — Umang Kapadia (`#it-security`) |

For urgent issues, post in `#it-security` on Slack.

---

## Timeline Expectations

| Stage | Expectation |
|-------|------------|
| Review turnaround | Within **3 business days** of receiving the GitHub notification |
| If you need more time | Comment on the PR explaining the delay — do not leave it unreviewed |
| If you are out of office | Designate a delegate and notify IT so the CODEOWNERS entry can be temporarily updated |

PRs older than 5 business days without a review will be escalated to IT/Security.

---

## Tips

- **GitHub notifications:** Make sure you have email notifications enabled for the `sodahealth/company-context` repository. Go to the repo → Watch → Custom → check "Pull requests"
- **You don't need to understand the code:** The only files you'll review are Markdown documents (`.md`) — plain text with some formatting
- **Drafts don't need review:** PRs marked `[DRAFT]` are not ready for review; you'll only be pinged on ready PRs
- **One approval is enough:** You don't need multiple approvers for your department's folder — your single approval will unblock the merge

---

_Questions? Contact IT/Security: `#it-security` on Slack or `umang@evermore.com`_
