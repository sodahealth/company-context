---
title: "People Operations Systems and Access"
summary: "Systems, tools, and access groups used by the People Operations team"
topics: [access, systems, tools, peopleops]
systems: [rippling, office-365, sharepoint, slack, jira, 15five, firstbase, zoom, brex]
people: [Regina Lindsey, Patricia Galvez]
content_type: "reference"
departments: [peopleops]
roles: [all]
classification: "internal"
last_verified: "2026-04-10"
review_cycle_days: 90
---

# People Operations Systems and Access

This document describes the systems, tools, and access groups used by the People Operations department.

## Team Members

| Name | Title |
|------|-------|
| Regina Lindsey | Head of People and Performance |
| Patricia Galvez | Consultant -- People Operations |

## Standard Access (All People Operations Members)

All People Operations team members are assigned the `department-peopleops` Entra group.

## Key Systems Used by People Operations

### Rippling (HRIS Core)

The most critical system for People Operations. Handles employee records, payroll, benefits administration, onboarding workflows, and the applicant tracking system (ATS). Rippling is the source of truth for employee data and syncs to Entra ID for account provisioning.

- **Access**: Direct login (not yet integrated with Entra SSO)
- **Used for**: Employee records, payroll, benefits, hiring/ATS, onboarding workflows, terminations
- **Integration**: Rippling-to-Entra sync for automated account provisioning

### Office 365 (Outlook, SharePoint, Microsoft Forms)

Primary communication and document management platform.

- **Outlook**: Main email and calendar tool (daily use)
- **SharePoint**: Document hub for job descriptions, comp frameworks, workforce planning spreadsheets, recruiting templates, and internal comms
- **Microsoft Forms**: Used for 360 performance reviews, surveys, and the evolve program data collection
- **Access**: Entra SSO

### Slack

Day-to-day team communication and company-wide announcements.

- **Key channel**: `#people-ops`
- **Access**: Entra SSO

### Jira

Project tracking for onboarding and offboarding workflows.

- **HI Project**: New hire tracking -- template-based tickets for each onboarding step
- **OFF Project**: Offboarding tracking -- separation checklist and access revocation
- **Access**: Atlassian Cloud (SSO)

### 15Five

Performance management platform used alongside the evolve program for check-ins, feedback, and goal tracking.

- **Access**: Direct login

### Firstbase

Equipment procurement and shipping for new hires and remote employees. IT-managed but People Operations initiates equipment orders for new hires.

- **Access**: IT-managed; Regina submits requests

### Zoom

External meetings, candidate interviews, and cross-company calls.

- **Access**: SSO

### Brex

Corporate expense and card management. Used for People Operations-related purchases and expense tracking.

- **Access**: Direct login (monthly use)

## Cross-Department Collaboration

| Department | Collaboration Area |
|-----------|-------------------|
| IT/Security | Account provisioning (Rippling-to-Entra sync), device setup, onboarding IT orientation, offboarding access revocation, equipment ordering via Firstbase |
| Finance | Payroll coordination, headcount budgeting, bonus payout processing |
| All departments | Hiring decisions, performance calibration, leveling, workforce planning |
| Office of CEO | Board reporting (headcount and people metrics), executive hiring |
