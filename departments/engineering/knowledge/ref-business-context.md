---
title: "Business Context Reference"
summary: "Customer-facing product semantics mapping customer vocabulary and decisions to code concepts -- essential for Kestrel self-service wizard design"
topics: [business-context, sponsor, benefits, approval-profiles, eligibility, funding, ssbci, kestrel]
systems: [Harmony, SFTP, FIS, Galileo, Avidia Bank, The Bancorp Bank]
people: []
content_type: reference
departments: [engineering]
roles: [all]
classification: internal
last_verified: "2026-03-18"
review_cycle_days: 90
---

# Business Context Reference -- Customer-Facing Product Semantics

**Source:** 22 customer-facing explainer PDFs processed 2026-02-22
**Purpose:** Business meaning layer for the sponsor domain. Maps customer vocabulary
and decisions to code concepts. Essential for Kestrel self-service wizard design.

---

## 1. Sponsor Hierarchy and Identity

### Core Terminology

- **Sponsor** (also "Customer" or "Client"): Medicare Advantage plan or health org
  contracting with Evermore to administer supplemental benefits via the &more prepaid card.
- **Program**: A specific benefit card program identified by a **Program Identifier**
  (Contract ID + Plan ID + optional Segment ID, e.g., `H1234-001-01`).
- **Member**: Individual beneficiary (Medicare enrollee) who receives benefits and a card.
- **&more**: Consumer-facing brand. "Evermore" is B2B only -- never appears in member materials.

### Banking / KYB Structure

- Each **legal entity** (unique TIN/EIN) that issues cards needs its own KYB due diligence
  and its own Program Funding Account.
- KYB takes 6-8 weeks, must be approved 4 weeks before launch.
- Required KYB data: entity info, controller/manager info (CEO/CFO), UBO identification
  (25%+ owners for private entities), pending litigation disclosure.
- **Issuing banks:** Avidia Bank (primary, newer programs) and The Bancorp Bank (legacy).

### Maps to Code

- `sponsor` table: `variant` (customer/brand), `parent_id` (hierarchy)
- `sponsor.config` JSONB: `galileo_config`, `fis_config`, `auth0_sso_connection_name`
- `PUT /sponsors/{sponsorID}`: creates/updates the sponsor entity
- `PATCH /sponsors/{sponsorID}/config`: applies configuration via JSON Merge Patch

---

## 2. Benefits Configuration

### The Benefit Input Grid (Central Configuration Artifact)

Each benefit is defined by these fields -- this IS what Kestrel's wizard must collect:

| # | Field | Type | Maps to Code |
|---|-------|------|-------------|
| 1 | Program Identifier | H1234-001-01 | `sponsor_identifier` |
| 2 | Display Name | Text | `benefit.name` |
| 3 | Benefit Identifier | Computed | Auto-generated |
| 4 | Intended Recipients | Enum: all / UF-only / SSBCI-only | Drives qualification logic |
| 5 | SSBCI Qualification Handler | Evermore / Plan handles | Conditional on SSBCI |
| 6 | Benefit Categories | Multi-select (13b OTC, 13i1 Food, etc.) | Maps to approval profiles |
| 7 | Approval Profile(s) | Multi-select from catalog | `funded_benefit_approval_profile` |
| 8 | Start Date | Date | `benefit.startDate` |
| 9 | Frequency | Monthly/quarterly/annually | `benefit.interval` + `benefit.iterations` |
| 10 | Rollover | Boolean | `benefit.duration` config |
| 11 | Amount | Currency | `funded_benefit.funding_amount` |
| 12 | Reimbursement Mode | Boolean | Triggers reimbursement product |
| 13 | PBP Notes | Free text | Critical for CSB expansion |
| 14 | Expansion behavior | 4 options | Expanding Combined benefit config |
| 15 | Expanded Categories | Multi-select (superset of #6) | Expanded AP assignment |
| 16 | Expanded APs | Multi-select | Post-qualification APs |
| 17 | Expansion Amount | Currency (delta, not cumulative) | Additional funding on qualification |

### Benefit Types (Customer Vocabulary -> Code)

| Customer Term | Code `benefit.type` | Key Config |
|---|---|---|
| OTC Benefit | `fundedBenefit` | funding_amount, approval_profiles, otchs_eligible |
| Food/Grocery Benefit | `fundedBenefit` | Different APs (Grocery, Healthy Foods, Produce) |
| Transportation | `rideBenefit` | max_cost_per_ride, num_one_way_rides, max_distance_miles |
| Survey/HRA | `surveyBenefit` | survey_json (dynamic form schema) |
| Rewards | Separate system | Issued via Rewards File to SFTP |
| Reimbursement | Separate flow | Intake -> adjudication -> disbursement |

### Benefit Expansion (SSBCI)

"Expanding Combined" benefit type where base benefit seamlessly expands when
member qualifies for SSBCI. Spending restrictions change without modifying
periodicity, rollover, or remaining balance. Example: $50/mo OTC-only becomes
$50/mo OTC+Food upon qualification.

---

## 3. Approval Profiles (31 for 2026)

### Two Restriction Mechanisms

1. **Item-restricted** (within retail network): Controls WHICH items at SKU/category level
2. **MCC-restricted** (merchant category code): Controls WHERE members spend; no item control

### Complete AP Catalog

**OTC (Item-restricted):**

- OTC Base -- 14 CMS-explicit categories
- OTC Base Plus -- All Base + incremental (herbal supplements, smoking cessation, etc.)
- Home and Bathroom Safety -- Bath mats, grab bars, night lights, non-slip footwear

**Healthcare (MCC-restricted):**

- Acupuncture -- MCC 8041 + name match
- Chiropractic -- MCC 8041 + name match
- Medical Services Base -- MCCs 8011, 8062, 8099
- Medical Services Base Plus -- MCCs 8011, 8031, 8041, 8049, 8050, 8062, 8099
- Dental -- MCCs 8021, 8071
- Vision -- MCCs 8042, 8043
- Hearing -- MCC 5975
- Foot Care Items (item-restricted) / Foot Care Merchants (MCC 8049)

**Food (Item-restricted):**

- Grocery -- Broadest (all food except alcohol/tobacco/cannabis)
- Healthy Foods Base -- CMS-compliant for SSBCI (13 categories)
- Healthy Foods Base Plus -- Base + incremental
- Produce -- Most restrictive (fresh/frozen produce only)
- Meals / Ready to Eat -- Packaged meals, kits, rotisserie

**Fitness:**

- Fitness Equipment (item-restricted) -- Mats, weights, trackers
- Fitness Memberships (MCC 7997 + name match)

**Home/Transport (mixed):**

- Pest Control Items / Merchants
- Pet Supply Items / Merchants
- Structural Home Modification Items / Merchants
- Transportation -- MCCs 4111, 4112, 4121, 4131
- Internet & Phone -- MCCs 4814, 4816, 4899
- Utilities -- MCCs 4900, 5983, 9399
- Rent -- Reimbursement-only

**Rewards:**

- Non-ATFLGC -- Broadest AP (everything except alcohol, tobacco, firearms, lottery, guns, cannabis)

### Maps to Code

- `approval_profiles` table in merchant DB
- `funded_benefit_approval_profile` links AP -> benefit in sponsor DB
- `approval_profiles_merchants`, `approval_profiles_merchant_category_codes`,
  `approval_profiles_core_categories`, `approval_profile_item` -- the rules

---

## 4. Rewards Configuration

### Rewards Input Grid Fields

| Field | Description |
|-------|-------------|
| Program Identifier | Same as benefits |
| Display Name | Member-facing name |
| Start Date | Earliest spendable date |
| Expiration Rules | Duration from issue / Set date / Card expiration (~5 years) |
| Approval Profiles | How reward can be spent |
| Reward Code | Code in Rewards File via SFTP |

### Customer Decisions

- Should rewards expire? (CMS is silent)
- Rewards reinstatement on re-enrollment? (Evermore recommends: yes)
- Disenrollment behavior for rewards? (Continuance vs deactivation)

---

## 5. Eligibility File Processing

### File Spec

- Format: CSV or PSV
- Delivery: SFTP to `sftp.mysodahealth.com:2022`
- Frequency: Daily or weekly recommended
- Encryption: PGP supported

### Eligibility Segment (Core Unit)

Unique combination: `member_identifier` + `program_identifier` + `effective_date` + `termination_date`

### Required Fields

| Column | Required | Notes |
|--------|----------|-------|
| member_identifier | Always | Primary ID |
| member_beneficiary_identifier | MA clients | MBI |
| program_identifier | Yes | Program ID |
| effective_date / termination_date | Yes | Blank term = no end |
| first_name, last_name | Yes | Updates if present |
| biological_sex | Yes | M/F |
| date_of_birth | Yes | |
| address1, city, state, zip | Yes | |
| sms, email | Optional | |
| language | Yes | Default en-us |
| qualification_indicators | Yes | Boolean, for SSBCI |

### Critical Rules

- No conflicting segments (overlapping dates = rejected)
- No term by omission (must explicitly send updated termination date)
- Circuit breakers halt files with significant changes for manual confirmation

### Maps to Code

- `pkg/sponsor/eligibility_intake_processor.go` / `eligibility_intake_workflow.go`
- `pkg/partner/api_job.go` (Benthos stream processing)
- Partner DB: `benthos_stream_configuration`, `job`, `job_run`, `line_item`

---

## 6. Program Funding

### Account Structure

- Program Funding Account = sub-ledgered virtual account within bank's omnibus FBO account
- Funds are NOT payment to Evermore -- beneficial ownership stays with sponsor
- ACH only (no check/wire) to dedicated virtual account number
- Initial funds due 10+ business days before launch (5 for ACH + 5 buffer)
- Separate funding account required per legal entity (unique TIN/EIN)

### Periodic Reloads

- Formula: Required Funding Level - Current Balance = Reload Amount
- Process starts 2-3 weeks before due date
- Evermore monitors daily balance, contacts Finance Lead if below threshold

### Maps to Code

- `funding_account` table in sponsor DB
- `sponsor_funding_account` links sponsor -> funding account
- `POST /sponsors/{sponsorID}/funding-accounts`
- `sponsor.config`: `galileo_config.galileo_funding_account_prn`, `fis_config.accounts.dan`

---

## 7. SSBCI / HRA Qualification

### Three Criteria (42 CFR 422.102(f)(1)(i))

1. One+ comorbid, medically complex chronic condition (from CMS list of 15 groups)
2. High risk of hospitalization or adverse health outcomes
3. Requires intensive care coordination

### 15 CMS Chronic Condition Groups

Chronic alcohol/drug dependence, autoimmune disorders, cancer, cardiovascular,
chronic heart failure, dementia, diabetes mellitus, end-stage liver disease,
ESRD requiring dialysis, severe hematologic disorders, HIV/AIDS, chronic lung
disorders, chronic mental health, neurologic disorders, stroke.

### Evermore's HRA Product

- Digital survey via Member Portal and &more mobile app
- Upon qualification: real-time benefit activation + member notification
- Coexists with plan's own qualification methods

---

## 8. Customer Care / IVR

### Two Models (Customer Decision)

- **Option 1:** IVR -> customer agents first (Tier 1), Evermore handles Tier 2
- **Option 2:** IVR -> Evermore agents first, warm transfer to customer for plan-specific

### IVR System

- Voice-first (no visual menus)
- Auth: last 4 of card + DOB + optional ZIP
- English + Spanish + 300 languages via translation line
- Hours: M-F 8am-8pm, 6 holiday closures

### After-Hours Options (Customer Decision)

Voicemail + callback / Transfer to plan number / Combined

---

## 9. Customer Decisions Required (Kestrel Wizard Inputs)

**The complete list of decisions a sponsor must make during implementation:**

1. **Per Benefit:** Program ID, display name, recipients, SSBCI handler, categories,
   approval profiles, start date, periodicity, rollover, amount, reimbursement mode,
   PBP notes, expansion behavior, expanded categories/profiles/amount
2. **Per Reward:** Program ID, year, display name, expiration rules, APs, reward codes
3. **Eligibility:** File format, field mapping, delivery frequency, SFTP credentials
4. **Disenrollment behavior:** Universal deactivation / Rewards continuance / Leave active
5. **Grace Period:** Yes/No (recommended: Yes)
6. **Rewards Reinstatement:** Yes/No (recommended: Yes)
7. **Benefit Extension policy:** 1 of 4 options
8. **Customer Care option:** Option 1 or 2
9. **After-hours handling:** Voicemail / Transfer / Combined
10. **MFA configuration:** Authenticator / Email / SSO
11. **Membership forecasts:** Per quarterly schedule
12. **Funding account setup:** Virtual account, ACH config, micro-deposit verification
13. **KYB due diligence:** Entity info, controllers, UBOs, litigation
14. **Collateral review:** Reviewers, state review days, translation needs
15. **SSBCI qualification:** Chronic conditions, HRA questions, qualification pathways

---

## 10. Operational Policies (Edge Cases)

| Policy | Customer Decision | Options |
|--------|------------------|---------|
| Benefit Extension | Per-customer | Not permitted / Customer-initiated only / Evermore 1x/year / Evermore multiple |
| Make-It-Right (MIR) | Automatic | 1 per quarter; additional needs customer approval; 60-day expiry |
| Returns | Automatic | Funds go to universal "Returns Benefit" (broadest AP); expires end of plan year |
| Expedited Cards | Criteria-based | Customer request / 2+ failed deliveries / complaint with no other remedy |
| Collateral Review | Via Aproove | Primary reviewer approves, secondary reviews, state review optional |

---

## 11. SFTP Infrastructure

```text
sftp.mysodahealth.com:2022
Username: eligibility-user_[Short code]
Auth: SSH key
PGP encryption: supported

/inbound/eligibility/          (production eligibility files)
/inbound/rewards/              (production rewards files)
/outbound/reports/             (generated reports: txn, funding, declined, card, balance)
/outbound/jobs/                (Line Item Reports: -check and -apply)
```
