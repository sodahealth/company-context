---
title: "Growth, Sales & New Markets Systems and Access"
summary: "Systems, tools, and access groups used by Growth, Sales, and New Markets"
topics: [access, systems, tools, growth, sales, new-markets]
systems: [salesforce, hubspot, sharepoint, auth0, office-365, zoom, brex, microsoft-forms, atlassian-cloud, smartsheet]
people: [Jared Childs, Trish Lin, Alex Kochanik, Casey Bartolucci, Jacob Murphy, Reid Smith, Jon Sayer, Sarah Hagan, Julie Nguyen, Lara Lasic, Mason Joyner, Ale Palmer]
content_type: "reference"
departments: [growth]
roles: [all]
classification: "internal"
last_verified: "2026-04-10"
review_cycle_days: 90
authorship: "agent-autonomous"
---

# Growth, Sales & New Markets Systems and Access

Systems, tools, and access groups used across the Growth, Sales, and New Markets teams.

## Team Members

| Name | Title | Sub-function |
|------|-------|-------------|
| Casey Bartolucci | Chief Commercial Officer | Sales (department head) |
| Jared Childs | VP Growth | Growth |
| Trish Lin | Sr. Director, Revenue Operations | Growth |
| Alex Kochanik | Senior Manager, Growth | Growth |
| Jacob Murphy | VP Sales | Sales |
| Reid Smith | Sr. Sales Manager | Sales |
| Becca Cesario | Associate Sales Executive | Sales |
| Jon Sayer | Capture Strategies Consultant (Contractor) | Sales |
| Sarah Hagan | GM, New Markets | New Markets |
| Julie Nguyen | Senior Director | New Markets |
| Lara Lasic | Associate Director | New Markets |
| Mason Joyner | Senior Manager | New Markets |
| Ale Palmer | Associate Manager, SNAP/EBT | New Markets |

## Standard Access (All Growth Members)

All Growth team members are assigned the `department-growth` Entra group.

## Key Systems

### Salesforce CRM

- **Purpose**: Customer relationship management — pipeline tracking, prospect management, deal stages, account records
- **Primary users**: Sales team, Trish Lin (revenue ops), Casey Bartolucci
- **Access**: Via SSO (Entra ID)
- **Notes**: Core system for pipeline analytics and sales forecasting. Trish Lin leads CRM hardening and process standardization.

### HubSpot

- **Purpose**: Marketing automation, lead generation, campaign management
- **Primary users**: Alex Kochanik (marketing), Jared Childs
- **Access**: Via SSO (Entra ID)

### SharePoint Online

- **Purpose**: Document management and collaboration — RFP/RFI responses, proposals, board decks, state implementation documents, OKR tracking
- **Primary users**: All teams, especially Sarah Hagan (New Markets) and Jon Sayer (RFX)
- **Access**: Via Office 365 license
- **Notes**: Heavy usage across New Markets for government proposals, FNS documentation, and state-specific materials. Sarah Hagan's team averages 2,397+ file operations per month.

### Auth0 (Production)

- **Purpose**: Evermore product access — API and application authentication
- **Primary users**: Sarah Hagan, New Markets team
- **Access**: Via SSO
- **Notes**: Used for accessing Evermore's internal product environments for demos and testing.

### Office 365 (Outlook, Teams, Forms)

- **Purpose**: Email, calendar, surveys, and data collection
- **Primary users**: All teams
- **Access**: Standard O365 license
- **Notes**: Microsoft Forms used for surveys and data collection in New Markets.

### Atlassian Cloud (Jira / Confluence)

- **Purpose**: Project tracking (Jira) and strategic planning documentation (Confluence)
- **Primary users**: New Markets (Confluence-heavy), Sales
- **Access**: Via SSO
- **Notes**: New Markets uses Confluence extensively for EBT strategic planning, GTM strategy, and design principles documentation. Sarah Hagan has created 938+ Confluence pages. Jira usage is light — the team operates above ticket-level, using documents and Confluence rather than task trackers.

### Zoom

- **Purpose**: Video meetings — prospect calls, state government meetings, internal coordination
- **Primary users**: All teams
- **Access**: Standard Zoom license

### Brex

- **Purpose**: Corporate card and expense management
- **Primary users**: Sarah Hagan, team leads
- **Access**: Via SSO

### Smartsheet

- **Purpose**: Project tracking and implementation timelines
- **Primary users**: New Markets
- **Access**: Licensed seats
- **Notes**: Used for state implementation tracking and project management.

## Cross-Department Collaboration

| Department | Collaboration Area | Key Systems |
|-----------|-------------------|-------------|
| Health Plan Solutions | Deal handoff, implementation coordination, prospect channels | Salesforce, Slack |
| Member Experience | Marketing collateral, in-store media, brand materials | SharePoint |
| Product | Product roadmap for new market features, EBT capabilities | Confluence, Jira |
| Finance | Deal pricing, proposal budgets, invoicing | SharePoint, Excel |
| IT/Security | Security questionnaire responses for RFPs, access provisioning | Entra ID |
| Merchants & Payments | EBT payment integrations, new payment rails | Slack (#ebt-payments) |
| Legal | Contract review for new deals, regulatory compliance | SharePoint |
