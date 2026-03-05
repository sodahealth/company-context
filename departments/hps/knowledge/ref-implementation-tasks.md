---
title: "Implementation Task Inventory"
summary: "Complete inventory of ~350+ implementation tasks organized by category with automation potential ratings"
topics: [implementation, tasks, automation, configuration, testing, milestones]
systems: [Harmony, Strapi, Iterable, FIS, OnRamp, SFTP]
people: [Tal Topf]
content_type: reference
departments: [hps]
roles: [all]
classification: internal
last_verified: "2026-03-05"
review_cycle_days: 90
---

# Implementation Task Inventory

This document inventories the ~350+ tasks involved in implementing a new health plan sponsor. These tasks cover system-level configuration, vendor coordination, and operational steps that go beyond what appears in OnRamp.

**Source:** "All Implementation Tasks - Operation Automation!.xlsx" (Tal Topf's OneDrive)

**Relationship to OnRamp:** OnRamp tracks the customer-facing implementation workflow (sponsor forms, approvals, milestones). This inventory tracks the internal operational work that happens alongside and downstream of OnRamp -- system configuration in Harmony, Strapi, Iterable, FIS, and other systems. Some tasks map one-to-one to OnRamp tasks; many are internal-only.

## Task Categories Overview

| Category | Task Count | Description |
|----------|-----------|-------------|
| Benefits | 26 | Benefit configuration in Harmony -- creation, testing, approval, finalization |
| Physical Materials | 27+ | Print material lifecycle -- design, review, print, ship, UAT across all languages |
| OX Configuration (Strapi) | 28 | Online experience configuration -- per-brand, per-language CMS operations |
| Milestones | 24 | High-level implementation gates tracking major phase completion |
| Kits | 19 | Physical material kit configuration and management (cards, catalogs, carriers) |
| Eligibility | 16 | Eligibility file processing -- SFTP setup, Benthos configuration, testing, production |
| Digital Materials | 14 | OX, SMS, and Email content at the high level |
| Email (all sub-categories) | 26 | Email content, templates, journeys, data requirements, review and testing |
| SMS (all sub-categories) | 27 | SMS content, templates, journeys, data requirements, review and testing |
| Rewards and Surveys | 19 | Reward and survey configuration, factors, testing |
| Rewards | 7 | Rewards configuration and file processing |
| OnRamp Module Submissions | 12+ | Customer-facing module submission milestones |
| Surveys | 5 | Survey configuration and testing |
| SFTP | 4 | SFTP connectivity and user provisioning |
| Funding | 3 | Funding account setup and deposit tracking |
| Factors | 3 | Factor configuration for eligibility/benefit qualification |
| Customers and Brands | 2 | Customer and brand entity creation in Harmony |
| Contracting | 2 | Contract and SOW completion |
| IVR | 2 | IVR configuration |
| Programs | 2 | Program creation and configuration in Harmony |
| Access | 2 | Tool access provisioning for customer users |
| Reimbursement | 2 | Reimbursement configuration and testing |
| OTC Provider | 1 | OTC provider configuration in Harmony |
| Iterable | 1 | Iterable configuration |
| Reporting | 1 | Hub dashboard configuration |

## Key Task Categories in Detail

### Benefits (26 tasks)

Benefit configuration in Harmony is one of the most critical and complex areas. Tasks include:

1. Benefits Grid QA
2. Final Benefit Sign-off
3. Cross-check Benefit Program Map with Benefit Grids
4. Configuring Approval Profile Shell and Details in Harmony
5. Adding APL (Approval Profile List) in Harmony
6. Benefits Created as Test Versions
7. Program Benefit Mapping
8. Confirm Narrow Network APs Implemented on Benefits
9. Benefit Test Version cleanup
10. Add client funding accounts to benefits
11. Benefit Customer UAT
12. Benefits Created as Final Versions
13. Customer configs for eligibility and benefits (disenrollment behavior, grace period)
14. Extension Benefits, Make-it-Rights, Returns, Reinstatement configured
15. Benefit Name Automation to Strapi

### Eligibility (16 tasks)

1. Eligibility file mapping doc QA with customer
2. Sponsor drops eligibility file for testing
3. Eligibility Benthos Test Step 1 (file formatting)
4. Eligibility Benthos Configured
5. Eligibility Benthos Tested Step 2 (commit some test data)
6. Commit test member in every program with benefit enrollment
7. Eligibility scenarios signed off on with live production member data
8. Received first production file
9. SSBCI file benthos configured and tested
10. Commit first eligibility file
11. Create production benthos configuration
12. Customer Eligibility Sign-Off

### Online Experience -- Configuration (28 tasks)

The most repetitive category, involving per-brand and per-language CMS operations in Strapi:

- Create brand logo lockup and card art for the online experience
- Upload logo lockup, card art, and disclaimers to garnish pages in Strapi (per brand)
- Create registration pages per brand
- Create brand pages in Strapi 5 (need brand name and soda ID from Harmony)
- Create common question entries for each language
- Create benefit flavors (shopping categories) with English and Spanish copy
- Create OTC catalog benefit components per language
- Create brand benefits in Strapi 5 per language
- Add OTC catalog links, rewards content, and friendly identifiers
- Add benefit overrides for customer-specific content
- Registration page configuration and validation

### Kits (19 tasks)

Kit configuration covers physical material kits including cards, catalogs, and carriers:

1. Define packages (languages, renewals, catalog only, etc.)
2. Submit ticket for FIS package IDs
3. FIS Card and Catalog Kits Configured in Harmony
4. Kit Assignment bloblang configured
5. Internal Kit Testing
6. Card UAT (VIP test cards)
7. Kit Assignment tested with test member file
8. ABCorp UAT Complete
9. Kit Assignment validated with first card send file

### Milestones (24 key gates)

These track whether major implementation phases are complete:

1. Solutions Calls Complete
2. Contracting Complete
3. Due Diligence Complete
4. Physical Materials Ready for Card Send
5. Benefit Configuration Complete
6. Rewards Configuration Complete
7. Client Tool Access and Training
8. Eligibility File Testing Started
9. File and Benefit Testing Complete
10. Digital Materials Configuration Complete (OX, IVR, SMS, Email, App)
11. Call Center Ready for Training
12. Fund Transfer Complete
13. First Eligibility File
14. Cards Mailed to Members
15. Call Center Takes First Call
16. Reporting Launch Complete

## Automation Potential

The task inventory has been assessed for automation potential. The highest-value clusters are:

### Very High Automation Value

1. **Strapi OX Configuration (28 tasks)** -- Most repetitive, per-brand/per-language CMS operations. Strapi has APIs. Every task is copy/paste or select-and-configure.

2. **Harmony Configuration (Benefits + Kits + Rewards + Factors + Programs, ~57 tasks)** -- Core benefit/reward system. Configuration is structured and rule-based.

3. **Iterable Setup (Email + SMS templates + journeys, ~53 tasks)** -- Template creation, journey configuration, data requirements. Iterable has APIs.

### High Automation Value

1. **Eligibility Pipeline (16 tasks)** -- Benthos configuration, SFTP setup, file processing. Already partially automated; pipeline is code-driven.

2. **FIS/Kit Configuration (19 tasks)** -- Package IDs, APLs, subprogram configuration. FIS integration plus Harmony API.

3. **SFTP, Access, Programs, Customers/Brands** -- Small task sets that can be fully automated via APIs.

### Medium Automation Value

1. **Physical Materials (27+ tasks)** -- Vendor coordination and approval workflows limit full automation.
2. **Digital Materials (14 tasks)** -- Content creation is manual, but distribution can be automated.

### Low Automation Value

1. **Contracting (2 tasks)** -- Legal and human process.
2. **Milestones (24 tasks)** -- Status tracking only; value is in auto-updating from downstream task completion.
