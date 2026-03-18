---
title: "Implementation Patterns"
summary: "Real customer onboarding data from Osprey -- 27 customers, 2,229 tasks mapping implementation workflows to sponsor domain concepts with confidence-scored defaults"
topics: [implementation, onboarding, osprey, kestrel, wizard, defaults, patterns]
systems: [Harmony, Osprey, OnRamp, SFTP]
people: []
content_type: reference
departments: [engineering]
roles: [all]
classification: internal
last_verified: "2026-03-18"
review_cycle_days: 90
---

# Implementation Patterns -- Real Customer Onboarding Data

**Source:** Osprey data -- 27 customers, 2,229 tasks, 3,564 task steps, 3,259 responses
**Mined:** 2026-02-22
**Purpose:** Ground truth for what Kestrel needs to automate. Maps real customer
workflows to sponsor domain concepts with confidence-scored defaults.

---

## Data Summary

- **22 real health plans** + 5 test/internal accounts
- **14 real implementation projects**, all 2026 plan year
- **286 modules** (26 canonical types after normalization)
- **278 unique task names**, **273 unique step names**
- **Average project completion: 84%** (range 7%-99%)
- **65% of tasks are milestone/checklist** (workflow tracking, not data collection)
- **35% of tasks have actual form steps** (784 tasks -- the real automation targets)

---

## Module -> Sponsor Domain Mapping

### 1. Kick-Off & Core Program Design (100% of projects)
**Domain:** Sponsor/brand creation
**Key tasks:**
- Define Brands: Program ID, Brand shortcode, Brand Marketing Name, differentiator
- IM Confirms Brand Shortcode & Program Details
- Provide Points of Contact (6-12 contacts with roles)

**Brands per customer:** 1 (most) to 9 (AmeriHealth). Prominence: 4, Gold Kidney/SCAN: 2.

### 2. Benefit Design (93% of projects, 176 tasks)
**Domain:** Benefit configuration
**Key workflow:** Download DRAFT BIG -> Submit DRAFT -> IM Review -> Customer Approval
-> Schedule Call -> Submit FINAL -> Multi-approver chain -> Configuration

**Multi-approver chain:** Customer Approver 1 -> 2 -> 3 -> IM Review & Approval

### 3. Program Configuration Decisions (100% of projects)
**Domain:** Sponsor config
**7 key decisions:** Rewards? EGWP? Qualified benefits? Reimbursement? Grace period?
Disenrollment behavior? Supplemental benefit differentiation?

### 4. New Client: Funding Account (79% of projects, 120 tasks)
**Domain:** Funding setup
**Workflow:** Create Account -> Create Memo -> Send test funds -> Confirm test ->
Send full funding -> Confirm full -> Milestone

### 5. Bank Due Diligence / KYB (79% of projects, 117 tasks)
**Domain:** Compliance/onboarding prerequisite
**Steps:** Entity info -> Controller/Manager info -> UBOs -> Litigation attestation ->
Letter of Authorization -> Compliance review

### 6. Eligibility Setup (93% of projects, 142 tasks)
**Domain:** Eligibility file processing
**Key sub-tasks:** File data mapping, SFTP credentials (SSH key, login, connection),
test file exchange, production readiness sign-off

### 7. Member Experience (93% of projects, one module PER BRAND)
**Domain:** Member materials/cards
**Bottleneck:** 25-50 form fields per brand instance. Contains 4-stage material
review chain (5 material types x 4 stages = 20 milestones per brand).
**Key insight:** 69% of brands differ only in "Logo" -- most values repeat.

### 8. Rewards (71% of projects)
**Domain:** Rewards configuration
**Conditional:** Only if customer offers rewards (10 of 14 do)

---

## Typical Implementation Ordering

Based on average earliest-completion rank across all projects:

| Rank | Module | When |
|------|--------|------|
| 1 | Kick-Off & Core Program Design | Always first |
| 2 | Bank Due Diligence | Early |
| 3 | Benefit Design | Early |
| 4 | Rewards | Early (if applicable) |
| 5 | Member Forecast | Mid |
| 6 | Member Experience | Mid |
| 7 | Contracting | Mid |
| 8 | Customer Care | Mid |
| 9 | Eligibility Setup | Mid-late |
| 10 | HP Member Materials & Guidance | Late |
| 11 | Finance/Invoicing | Late |
| 12 | Final Approved Card Package | Late |
| 13 | Digital Member Materials | Late |
| 14 | New Client: Funding Account | Late |
| 15 | Edge Case Policies | Late |
| 16 | Reporting | Late |
| 17 | Tools Overview and Access | Late |
| 18 | Final Check-out | Always last |

---

## Common Defaults (Confidence-Scored)

Pre-fill these in the Kestrel wizard. Confidence = % of customers who chose this value.

### High Confidence (>85%) -- Pre-fill, don't ask
| Field | Default | Confidence |
|-------|---------|------------|
| Backend Member Admin access | Yes | 100% |
| Soda support qualification | No | 100% |
| Acknowledge receipt | Yes | 100% |
| Reading level approved | Yes | 93% |
| Payment system (existing) | No | 94% |
| Differentiate below PBP | No | 92% |
| Voicemail/route after hours | Yes | 90% |
| Rewards reinstatement | Yes | 89% |
| Digital materials languages | English + Spanish | 88% |

### Medium Confidence (60-85%) -- Pre-fill, show as default
| Field | Default | Confidence |
|-------|---------|------------|
| State/compliance review needed | Yes | 76% |
| Multi-language insert | Yes | 76% |
| Customer care option | Option 2 (Evermore first) | 75% |
| Grace period | Yes | 71% |
| Rewards offering | Yes | 71% |
| What differs about this brand | Logo | 69% |
| Reimbursement mode | No | 69% |
| MFA configuration | SSO | 60% |

### Low Confidence (<60%) -- Must ask, no default
| Field | Most Common | Confidence |
|-------|-------------|------------|
| Transfer rewards balances | No | 57% |
| Disenrollment behavior | Universal deactivation | 50% |
| Benefit extension | Option 3 | 47% |
| Business days (physical review) | 5 | 35% |
| Business days (digital review) | 10 | 45% |

---

## Kestrel Wizard Steps (Derived from Patterns)

### Step 1: Brand Structure
- How many brands? (1-9, median: 1)
- Per brand: Program ID (validated CMS format), shortcode, marketing name
- What differentiates brands? (Logo [69%], Guidelines, Card)

### Step 2: Program Configuration
- Rewards? (default: Yes, 71%)
- EGWP? (default: No, 77%)
- Qualified benefits? (default: conditional)
- Reimbursement? (default: No, 69%)
- Grace period? (default: Yes, 71%)
- Disenrollment behavior? (no strong default -- must ask)

### Step 3: Benefit Design
- Input grid per brand (18 fields per benefit -- see ref-business-context.md)
- Currently file-based upload, could become structured form

### Step 4: Rewards Configuration (conditional on Step 2)
- Reinstatement? (default: Yes, 89%)
- Balance transfer? (default: No, 57%)
- Expiration rules, APs, reward codes

### Step 5: Eligibility Configuration
- File format mapping
- SFTP setup (SSH key, login, connection)
- Segments and SSBCI qualification config

### Step 6: Member Materials
- Languages (default: English + Spanish, 88%)
- Reading level (default: approved, 93%)
- Multi-language insert (default: Yes, 76%)
- Review contacts and business days
- Material types needed per brand

### Step 7: Customer Care
- Care option (default: Option 2, 75%)
- After-hours routing (default: voicemail, 90%)
- Admin access (default: Yes, 100%)
- Contact details, phone number, hours

### Step 8: Finance/Invoicing
- Payment system (default: new, 94%)
- Invoicing contacts
- Tax exempt status

### Step 9: MFA Configuration
- Standard / SSO (default: SSO, 60%)

### Step 10: Edge Case Policies
- Benefit extension option (no strong default -- must ask)

---

## Response Fields -> Sponsor API Config Mapping

These Osprey response fields map directly to sponsor/brand configuration in Harmony:

| # | Osprey Field | Sponsor API Field | Type |
|---|---|---|---|
| 1 | Program ID | `brand.program_id` | Validated CMS format |
| 2 | Brand shortcode | `brand.short_code` | String |
| 3 | Brand Marketing Name | `brand.marketing_name` | String |
| 4 | Customer Call Center Number | `brand.customer_care_phone` | Phone |
| 5 | Hours of operations | `brand.customer_care_hours` | Text |
| 6 | Reading Level | `brand.reading_level_approved` | Boolean |
| 7 | Digital Materials Languages | `brand.languages` | Enum |
| 8 | Multi-Language Insert | `brand.multi_language_insert` | Boolean |
| 9 | Translation Review | `brand.needs_translation_review` | Boolean |
| 10 | State/Compliance Review | `brand.needs_compliance_review` | Boolean |
| 11 | Disclaimers | `brand.physical_disclaimer`, `brand.digital_disclaimer` | Text |
| 12 | Business days for review | `brand.physical_review_days`, `brand.digital_review_days` | Number |
| 13 | Grace Period | `program.grace_period_enabled` | Boolean |
| 14 | Disenrollment Behavior | `program.disenrollment_behavior` | Enum (3 options) |
| 15 | Benefit Extension | `program.benefit_extension_option` | Enum (4 options) |
| 16 | Payment System | `sponsor.has_existing_payment_system` | Boolean |
| 17 | Tax Exempt | `sponsor.tax_exempt` | Boolean |
| 18 | MFA Configuration | `sponsor.mfa_type` | Enum (standard/sso) |
| 19 | Customer Care Option | `sponsor.care_option` | Enum (option_1/option_2) |
| 20 | Rewards | `program.rewards_enabled` | Boolean |
| 21 | EGWP | `program.egwp_enabled` | Boolean |
| 22 | Qualified benefits | `program.qualified_benefits` | Boolean |
| 23 | Reimbursement | `program.reimbursement_enabled` | Boolean |
| 24 | Reinstatement | `program.rewards_reinstatement` | Boolean |

**Note:** These fields don't all exist in the current sponsor schema. Many would be
new columns or config JSON fields that Kestrel needs to add. This mapping defines
the minimum data model extension for self-service.

---

## The 65/35 Split -- Workflow vs. Data

- **65% of tasks (1,445)** are milestone/checklist items (status tracking). Kestrel
  models these as workflow states/transitions, not form steps.
- **35% of tasks (784)** have actual form steps that collect data. These are the real
  automation targets -- structured wizard forms with validation, defaults, and
  conditional logic.

---

## The Member Experience Bottleneck

The single most complex implementation module:
- **46 instances** of "Member Experience Details" (one per brand across all projects)
- **25-50 form fields per instance**
- **4-stage review chain** per material type (5 types x 4 stages = 20 milestones/brand)
- Many fields repeat across brands within a customer

**Kestrel opportunity:** Set common values once at sponsor level, only override per-brand
where something differs. Data shows "what differs" is usually just "Logo" (69%).

---

## Response Type Distribution

| Type | Count | % | Kestrel Form Type |
|------|-------|---|---|
| text | 1,921 | 59% | Many should be typed (phone, number, validated) |
| select | 435 | 13% | Dropdown/radio |
| file_upload | 305 | 9% | File upload (BIG, materials, etc.) |
| multi_select | 218 | 7% | Checkbox group |
| email | 163 | 5% | Email input |
| textarea | 110 | 3% | Multi-line text (disclaimers, notes) |
| number | 66 | 2% | Number input |
| yes_no | 23 | 1% | Toggle/checkbox |
| date | 18 | 1% | Date picker |

59% are freeform text but many contain structured data (phone numbers, business day
counts, Program IDs). Kestrel should use typed inputs with validation.
