---
title: "MX Tools and Integrations"
summary: "Tools and integrations used by the Member Experience and Merchants & Payments teams"
topics: [tools, integrations, mx, payments, member-experience]
systems: [FIS, Galileo, Brex, SharePoint, Smartsheet, Confluence, Figma, Auth0]
people: [Jared Dauman, Julie Fleischer]
content_type: "reference"
departments: [mx]
roles: [all]
classification: "internal"
last_verified: "2026-04-10"
review_cycle_days: 90
authorship: "agent-autonomous"
---

# MX Tools and Integrations

Tools and integrations used by the Member Experience and Merchants & Payments teams. Tool usage is based on SaaS sign-in data from the CPO discovery profile and team activity patterns.

## Primary Tools — Merchants & Payments

| Tool | Purpose | Frequency | Key Users |
|------|---------|-----------|-----------|
| Brex | Corporate card and expense management | Daily | Jared Dauman (primary -- #1 app by usage) |
| SharePoint | Document management, SOWs, RFP materials, merchant catalogs | Daily | Entire M&P team, especially Jared Dauman |
| Confluence | Knowledge base, EBT go-live coordination, transaction reports, company policies | Daily | Jared Dauman (power user -- 2,661 pages all-time) |
| Smartsheet | Project management and tracking | Weekly | Jared Dauman, M&P team |
| Outlook | Email communication (29 emails/day avg for Jared) | Daily | Entire team |
| Zoom | Meetings and video calls | Daily | Entire team |
| Auth0 (Production) | Evermore API authentication for payment operations | Weekly | Jared Dauman, M&P team |
| Atlassian (Jira/Confluence) | Issue tracking and documentation | Weekly | M&P team |
| Microsoft Forms | Surveys and data collection | Weekly | Jared Dauman |
| Greenhouse | Recruiting and applicant tracking | Monthly | Jared Dauman (actively hiring for M&P) |

## Primary Tools — Member Experience

| Tool | Purpose | Frequency | Key Users |
|------|---------|-----------|-----------|
| Figma | Design review and collaboration | As needed | Julie Fleischer, Ann Grafelman |
| Adobe Creative Suite | Design production -- card carriers, catalogs, signage, digital assets | Daily | Ann Grafelman, Jill Blacketer |
| Aproove | Print materials approval workflow | As needed | Nidhi Nayyar, Sarah Rumfelt |
| ABCorp | Print fulfillment for member materials (card carriers, kits, catalogs) | As needed | Nidhi Nayyar |
| SharePoint | Document management, brand assets | Daily | MX team |

## Secondary Tools (Used Occasionally)

| Tool | Purpose | Frequency | Notes |
|------|---------|-----------|-------|
| Datadog | Monitoring | Rare | Jared checks operational monitoring |
| Miro | Whiteboarding and planning | Rare | Strategy sessions |
| TeamRetro | Retrospectives | Rare | Jared runs team retros |
| DocSend | Document sharing with external partners | Rare | Merchant/partner communications |
| Metabase | Internal analytics | Rare | Operational data review |
| Calendly | Meeting scheduling | Rare | External meeting coordination |
| Virtru | Email encryption | Rare | Sensitive communications |
| Microsoft Copilot | AI assistance (exploring) | Rare | Jared has tried but not adopted |

## Integrations

### Payment Processing Pipeline

```text
Evermore API (Harmony) → FIS (transaction auth/clearing/settlement)
                       → Galileo (card issuing/management)
                       → Settlement/reconciliation → Funding accounts
```

The Banana Dance engineering squad builds and maintains the FIS and Galileo integration code. M&P defines the business rules, merchant configurations, and settlement processes that the integrations execute.

### Member Materials Pipeline

```text
Brand design (Figma/Adobe) → Approval (Aproove) → Print (ABCorp) → Member kits
                                                                   → Card carriers
                                                                   → In-store signage
                                                                   → Catalogs
```

Nidhi Nayyar coordinates the materials pipeline with Sarah Rumfelt (Office of CEO). HPS Implementation Managers request materials for new sponsor launches.

### EBT/SNAP Payment Rails

M&P is building out EBT payment capabilities as a new payment rail alongside the existing Mastercard prepaid infrastructure. This involves FNS (Food and Nutrition Service) compliance, item-level restriction enforcement, and state-specific program requirements. The EBT go-live is a major cross-functional initiative coordinated via `#ebt-payments`.
