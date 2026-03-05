---
title: "HPS Systems and Access"
summary: "Systems, tools, and access groups used by the Health Plan Solutions team"
topics: [access, systems, tools, entra, groups, harmony, onramp, sftp]
systems: [Harmony, OnRamp, SFTP, Smartsheet, Strapi, Hub, MemberAdmin, Salesforce]
people: [Tal Topf, Diane Borton, Megan Guillory, Ariane Grazian, Jordan Savold, Cori Billings]
content_type: reference
departments: [hps]
roles: [all]
classification: internal
last_verified: "2026-03-05"
review_cycle_days: 90
---

# HPS Systems and Access

This document describes the systems, tools, and access groups used by the Health Plan Solutions (HPS) department.

## Team Members

| Name | Title |
|------|-------|
| Ariane Grazian | SVP, Health Plan Solutions |
| Tal Topf | Associate Director, Health Plan Solutions |
| Diane Borton | Senior Manager, Health Plan Solutions |
| Megan Guillory | Senior Manager, Health Plan Solutions |
| Jordan Savold | Associate Director, Health Plan Solutions |
| Cori Billings | Associate Director, Implementations |

## Standard Access (All HPS Members)

All HPS team members are assigned the `department-healthplansolutions` Entra group.

## Common Access (Most HPS Members)

The following groups are assigned to the majority of HPS team members:

| Group Name | Purpose |
|------------|---------|
| `gcp-all-sponsor-bucket-objects-list` | Listing sponsor files in cloud storage |
| `gcp-all-sponsor-buckets-write` | Writing to sponsor file buckets |
| `gcp-sftp-readonly` | Read-only SFTP access |
| `harmony-production-all-sponsors-admin` | Harmony admin access for all sponsors |
| `role-implementation-managers` | Implementation manager role permissions |
| `anthropic-claude-users` | Claude AI standard access |
| `gcp-all-merchants-buckets-write` | Writing to merchant file buckets |
| `memberadmin-production-all-staging-sponsors-admin` | Staging environment admin |
| `lookout-watchers-always` | Alert monitoring |
| `adobe-acrobatpro-users` | Document creation |
| `memberadmin-production-all-sponsors-admin` | Member admin for all sponsors |
| `role-strategy` | Strategy role permissions |

## Key Systems Used by HPS

### OnRamp (Implementation Project Management)

- **URL**: app.onramp.us
- **Purpose**: Customer-facing implementation workflow. Sponsors fill in structured forms during onboarding (benefits, eligibility, contacts, etc.)
- **Usage**: Primary tool for tracking implementation milestones, module submissions, and customer sign-offs
- **Declining**: Usage is dropping as Osprey (the replacement) ramps up

### Harmony (Benefits and Configuration)

- **Purpose**: Evermore's internal authorization and configuration system
- **Used for**: Benefits, rewards, approval profiles, kit configuration, program creation, eligibility processing
- **Access group**: `harmony-production-all-sponsors-admin`
- **Note**: This is the core system that most implementation tasks ultimately configure

### Smartsheet (Project Management)

- **Purpose**: Daily project management tool for tracking implementation timelines and milestones
- **Used for**: Kit matrices, forecasts, inventory tracking, print wave scheduling, timeline management
- **Note**: Tal Topf uses this as her daily PM backbone (20 days active in 90-day window)

### SFTP (File Transfer)

- **Purpose**: Secure file transfer for eligibility files, reports, and rewards files
- **Access groups**: `gcp-sftp-readonly`, `gcp-all-sponsor-buckets-write`
- **Note**: SFTP access setup is gated on contract execution

### Strapi (Content Management)

- **Purpose**: CMS for the online experience (OX) -- member-facing portal content
- **Used for**: Brand pages, benefit descriptions, common questions, shopping categories, disclaimers
- **Note**: Configuration is highly repetitive (per-brand, per-language) and is a top automation target

### Hub (Sponsor Portal)

- **Purpose**: Client-facing portal for managing benefits programs
- **Access group**: `hub-all-sponsors-admin` (2/6 members)

### MemberAdmin (Member Management)

- **Purpose**: Internal tool for managing individual member accounts
- **Access groups**: `memberadmin-production-all-sponsors-admin`, `memberadmin-production-all-staging-sponsors-admin`

### Iterable (Communications)

- **Purpose**: Marketing and communications platform for email and SMS
- **Used for**: Brand setup, email templates, SMS journeys, onboarding sequences

### Salesforce (CRM)

- **Access group**: `salesforce-sales-standard-user` (2/6 members)
- **Purpose**: CRM for customer records and cases

### Other Tools

- **Jira**: `jira-servicedesk-boost-team` and `jira-servicedesk-bpoh-agents` (select members)
- **SharePoint**: External site memberships for customer collaboration (Humana, UCLA, NTC)
- **Ironclad**: Contract request submission (2/6 members)

## Cross-Department Collaboration

HPS works closely with these departments and their systems:

| Department | Collaboration Area |
|-----------|-------------------|
| **Engineering** | Eligibility file processing (Benthos), Harmony configuration, SFTP setup |
| **Member Experience (MX)** | Materials production, Aproove projects, catalog design, OX content |
| **Customer Care** | IVR routing, call center training, complaint handling |
| **Merchants and Payments** | Funding accounts, card operations, FIS coordination |
| **Product** | Kestrel (new admin platform), feature requests, product testing |
| **Finance** | Invoicing, funding account tracking, material cost reconciliation |
| **Legal** | SOW/MSA completion, compliance review |
| **Customer Success** | Post-launch sponsor relationship, account management handoff |
