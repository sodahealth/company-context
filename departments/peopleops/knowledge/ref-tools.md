---
title: "People Operations Tools"
summary: "Tools and integrations used by the People Operations team"
topics: [tools, integrations, peopleops]
systems: [rippling, office-365, sharepoint, slack, jira, 15five, firstbase, zoom, brex, microsoft-forms, m365-copilot]
people: [Regina Lindsey]
content_type: "reference"
departments: [peopleops]
roles: [all]
classification: "internal"
last_verified: "2026-04-10"
review_cycle_days: 90
---

# People Operations Tools

Tools and integrations used by the People Operations department, organized by frequency of use.

## Daily Tools

| Tool | Purpose | Access |
|------|---------|--------|
| Rippling | HRIS core -- employee records, payroll, benefits, ATS, onboarding/offboarding workflows | Direct login |
| Microsoft Outlook | Email and calendar -- primary communication tool (~14 outbound emails/day) | Entra SSO |
| Slack | Real-time team communication, announcements, cross-department coordination | Entra SSO |
| SharePoint | Document management -- job descriptions, comp frameworks, workforce planning, templates | Entra SSO |

## Weekly Tools

| Tool | Purpose | Access |
|------|---------|--------|
| Microsoft Forms | Surveys, 360 performance reviews, evolve program data collection | Entra SSO |
| Zoom | Candidate interviews, external meetings, cross-company calls | SSO |
| M365 Copilot | AI assistant for drafting communications, summarizing documents | Entra SSO |
| Jira | Onboarding (HI project) and offboarding (OFF project) ticket tracking | Atlassian SSO |

## Monthly Tools

| Tool | Purpose | Access |
|------|---------|--------|
| 15Five | Performance management -- check-ins, feedback, goal tracking | Direct login |
| Brex | Corporate expense management and purchase card | Direct login |
| Firstbase | Equipment procurement and shipping for new hires | IT-managed |

## Integrations

### Rippling to Entra ID

Rippling is the source of truth for employee data. When a new hire is added to Rippling, the Rippling-to-Entra sync automatically provisions their Microsoft 365 account, Entra group memberships, and downstream access. Terminations in Rippling trigger access revocation through the same sync.

### Jira Onboarding and Offboarding Projects

People Operations uses two Jira projects for employee lifecycle tracking:

- **HI (Hire)** -- Template-based tickets cloned for each new hire. Tracks all onboarding steps: Rippling enrollment, IT provisioning, equipment ordering, orientation scheduling, and first-week checklist.
- **OFF (Offboarding)** -- Template-based tickets for separations. Tracks Rippling termination, access revocation, equipment return, and knowledge transfer.

### SharePoint Document Library

Centralized storage for People Operations documents including:

- Recruiting forms and templates
- Job descriptions (active and draft)
- Compensation band frameworks
- Workforce planning spreadsheets
- Internal communications drafts
- Board reporting materials
