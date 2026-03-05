---
title: "Implementation Cycle"
summary: "End-to-end implementation lifecycle for health plan sponsor onboarding, from kick-off through go-live"
topics: [implementation, lifecycle, onboarding, milestones, process, automation]
systems: [Harmony, OnRamp, Strapi, Iterable, FIS, SFTP, Aproove]
people: [Tal Topf, Diane Borton, Megan Guillory, Ariane Grazian]
content_type: process
departments: [hps]
roles: [all]
classification: internal
last_verified: "2026-03-05"
review_cycle_days: 90
---

# Implementation Cycle

This document describes the end-to-end lifecycle for implementing a new health plan sponsor at Evermore. It synthesizes the implementation process from OnRamp module workflows, the internal task inventory, and operational patterns observed during the 2025-2026 implementation cycle.

## Overview

When Evermore onboards a new health plan sponsor, hundreds of configuration tasks are executed across dozens of systems. The implementation lifecycle typically spans 4-6 months, running from initial kick-off through go-live and the first card mailed to members.

The process involves two parallel tracks:

1. **Customer-facing track** (managed in OnRamp): Structured forms, approvals, and milestones that the health plan completes
2. **Internal operations track** (managed across Harmony, Strapi, Iterable, FIS, etc.): System configuration that the Evermore team executes

## Implementation Phases

### Phase 1: Kick-Off and Core Program Design (Month 1)

**Goal**: Establish the relationship, define program structure, and collect initial requirements.

**Key activities**:

- Kick-off call with the health plan sponsor
- Solutions meetings covering benefits, member experience, eligibility, and add-on products
- Collect points of contact (typically 6+ contacts with roles and titles)
- Define brands (Program ID, Brand name, Brand Marketing Name)
- Eligibility file and reporting decisions (number of files, report separation, SFTP access level)
- Funding structure decisions (single EIN, funding account type)
- Overview of tools access (Hub, Metabase, Iterable, Harmony)

**Owner**: HPS (Implementation Manager)

**OnRamp modules**: Kick Off, Solutions Calls, Points of Contact, Define Brands, Eligibility Files and Reporting, Funding, Tools Overview

### Phase 2: Contracting and Due Diligence (Months 1-3)

**Goal**: Complete legal agreements and bank due diligence.

**Key activities**:

- Draft and finalize MSA / SOW / BAA
- Customer security review (if applicable)
- Bank due diligence: entity information, controller/manager information, ultimate beneficial owners, litigation attestation
- M&P review and submission to bank (Avidia)

**Owner**: HPS + Legal + M&P

**Key risk**: Government entities (like county health plans) can significantly delay contracting. SOW is often the last piece to finalize, but implementation work can begin before the contract is fully signed.

### Phase 3: Benefit and Rewards Design (Months 2-4)

**Goal**: Configure the benefit and rewards structure for the sponsor.

**Key activities**:

- Program configuration decisions: qualified benefits, disenrollment behavior, grace period, reimbursement mode, EGWPs, sub-PBP differentiation, rewards
- Download and submit Benefit Input Grid (DRAFT)
- Customer and IM review and approval of DRAFT
- Schedule call with MX for materials coordination
- Download and submit Benefit Input Grid (FINAL)
- Multi-approver sign-off on FINAL
- Rewards Input Grid follows the same draft-review-final lifecycle
- Reward file data mapping input

**Owner**: HPS + Customer

**Critical artifacts**: The Benefit Input Grid (BIG) and Rewards Input Grid are the primary configuration documents. They drive downstream Harmony configuration.

### Phase 4: Member Experience (Months 3-5)

**Goal**: Configure all member-facing content and materials per brand.

This is the richest data collection phase, with 24 form steps per brand covering:

- Marketing name, threshold languages, plan logo, brand guidelines
- Disclaimers (physical, digital, additional)
- Sample member ID card
- Customer review and compliance review timelines
- Translation review details
- Materials list, IVR scripting, welcome kit contents
- Reward card name, card vendor, languages
- Catalog dimensions, USPS classification

**Owner**: MX + HPS + Customer

### Phase 5: System Configuration (Months 3-5)

**Goal**: Configure all internal systems based on the collected requirements.

This is the largest block of internal work, involving:

**Harmony** (~57 tasks): Benefits, kits, rewards, factors, programs, approval profiles

- Benefits created as test versions, tested, then promoted to final
- Kit configuration including FIS package IDs, bloblang assignment, UAT
- Rewards and surveys configured with factors and qualification rules

**Strapi** (~28 tasks): Online experience configuration

- Brand pages, logo lockups, card art, disclaimers per brand
- Common questions, benefit flavors, shopping categories per language
- OTC catalog components, brand benefits, reward content per language

**Iterable** (~53 tasks): Email and SMS setup

- Email templates for onboarding sequences, per brand, per language
- SMS library configuration, journey creation for reload/reminder/reward/CSAT
- Data requirements for audience segmentation

**Other systems**: FIS (card production), IVR, Salesforce, Metabase dashboards

**Owner**: HPS + Engineering + MX + Product

### Phase 6: Eligibility Setup and Testing (Months 4-5)

**Goal**: Establish the eligibility file pipeline and validate data flows.

**Key activities**:

- Customer provides eligibility data mapping document
- Customer provides SSH public key for SFTP access
- SFTP credentials and connection established
- Customer generates and sends test file
- Benthos configuration for eligibility file processing (test step 1: formatting)
- Benthos tested step 2: commit test data as test members
- Commit test member in every program with benefit enrollment
- Eligibility scenarios signed off with live production member data
- SSBCI file benthos configured and tested (if applicable)
- Production benthos configuration created
- Customer eligibility sign-off

**Owner**: HPS + Engineering

### Phase 7: Materials Production (Months 3-6)

**Goal**: Design, print, and ship physical materials to the card vendor.

**Key activities**:

- Design review with print vendors (carrier, catalog, CHA, NOA)
- Multiple rounds of internal review (HPS, M&P, Legal and Compliance)
- Multiple rounds of customer review
- State review or CMS File and Use (if applicable)
- Bank review
- Print English version, ship to card emboss vendor (ABCorp)
- ABCorp UAT and customer UAT (English)
- Translations, customer translation review
- Print translated versions, ship to emboss vendor
- UAT all languages

**Owner**: MX + HPS + Customer

**Vendor coordination**: ABCorp (card embossing, fulfillment), Mealy (printing, shipping)

### Phase 8: Testing and Validation (Months 5-6)

**Goal**: End-to-end validation before go-live.

**Key activities**:

- Benefit testing started
- VIP swipe UAT (physical card test)
- Internal OX UAT (parts 1 and 2)
- Customer OX / Benefit UAT
- Client UAT card send
- Internal survey UAT and customer survey UAT
- File and benefit testing complete sign-off
- Volume testing

**Owner**: HPS + Engineering + MX

### Phase 9: Go-Live Preparation (Month 6)

**Goal**: Final preparations for member-facing launch.

**Key activities**:

- Call center ready for training
- Fund transfer complete
- First eligibility file committed
- IVR configured
- Digital materials configuration complete (OX, IVR, SMS, Email, App)
- Hub dashboard configured
- Iterable configured and journeys activated
- Reporting launch complete

**Owner**: All departments

### Phase 10: Launch (Month 6-7)

**Goal**: Cards reach members, call center is live.

**Key activities**:

- Cards mailed to members (target: ~November 17 for January 1 delivery)
- Call center takes first call (target: ~December 1)
- Last eligibility files for 1/1 delivery (target: ~December 8)
- Last cards in mail for 1/1 delivery (target: ~December 12)

**Owner**: All departments

## Implementation Timeline (Typical)

For a January 1 go-live date, the typical timeline follows this pattern:

| Month | Phase | Key Milestone |
|-------|-------|---------------|
| June-August | Kick-Off + Contracting | Implementation Kick-Off, Solutions Calls |
| July-August | Due Diligence | Bank diligence submitted |
| August-September | Benefit/Rewards Design | Benefit Input Grid finalized |
| September | System Configuration begins | Benefit Configuration Complete (Sept 30) |
| September-October | Materials Production | Card vendor UAT starts |
| September-November | Eligibility Testing | Testing started (Sept 1), complete (Nov 1) |
| October | Digital Materials | Configuration complete (Oct 15) |
| October | Go-Live Prep | Fund transfer, tool access, training |
| November | Launch | First eligibility file, cards mailed |
| December | Live Operations | Call center live, final cards mailed |

## Current State: Automation and Process Improvement

The implementation process is currently highly manual, with IMs logging into 10+ tools to execute configuration tasks. The "Implementation 2.0" initiative is working to automate the most repetitive elements:

**Highest automation targets**:

1. Strapi OX Configuration (28 repetitive CMS operations)
2. Harmony Configuration (~57 structured, rule-based tasks)
3. Iterable Setup (~53 template and journey tasks)
4. Eligibility Pipeline (16 tasks, already partially automated)

**Vision**: Implementation Managers work through Claude as their primary interface, describing what needs to happen while the platform executes with preview-before-commit, audit trails, and safety controls.

**Osprey**: The OnRamp replacement (currently in test environment) will modernize the customer-facing implementation workflow with self-service eligibility testing, automated timeline tracking, and integrated dashboards.
