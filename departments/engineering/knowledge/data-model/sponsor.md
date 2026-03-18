---
title: "Data Model: Sponsor"
summary: "Schema reference for the sponsor database -- core entities including sponsors, members, benefits, enrollments, programs, and cards across ~70 tables"
topics: [data-model, sponsor, member, benefit, enrollment, program, card, schema, postgresql]
systems: [Harmony, Cloud SQL, PostgreSQL]
people: []
content_type: reference
departments: [engineering]
roles: [all]
classification: internal
last_verified: "2026-03-18"
review_cycle_days: 90
---

# Data Model: sponsor

**Database:** sponsor
**Migrations:** 266 (largest in the system)
**Tables:** ~70
**Query files:** 22

The sponsor database is the core of the Harmony platform. It owns member identity,
benefit definitions, enrollment lifecycle, program structure, and sponsor configuration.

---

## Core Entities

### sponsor
The root entity. Represents a health plan sponsor (customer or brand).

| Column | Type | Notes |
|--------|------|-------|
| id | bytea (XID) | Public identifier |
| name | varchar | Display name |
| description | text | |
| galileo_prn | varchar | Galileo processor reference |
| emboss_kit_identifier | int (0-9999) | Card embossing kit |
| config | jsonb | Flexible configuration blob |
| variant | enum (customer, brand) | Hierarchy level |
| parent_id | bytea FK -> sponsor | Brand -> customer relationship |
| auth0_sso_connection_name | varchar | SSO integration |
| merged_config | jsonb | Computed merged config (brand inherits from customer) |

**Key constraint:** Customers have no parent. Brands must have a customer parent.

### member
A person enrolled in a sponsor's program.

| Column | Type | Notes |
|--------|------|-------|
| id | bytea (XID) | Public identifier |
| sponsor_id | bytea FK -> sponsor | Isolation boundary |
| sponsor_identifier | varchar | External reference |
| customer_id | varchar | |
| processor fields | various | Galileo/FIS identifiers |
| test | boolean | Test member flag |

### member_personal_info_current / member_personal_info_history
Tracks personal data changes with source attribution.

Fields: date_of_birth, email_address, first_name, last_name, middle_initial,
phone, language_tag, cms_reporting_gender.
Sources: customer_service_agent, eligibility, external, member, soda.

### member_card
Card issuance and status tracking.

| Column | Type | Notes |
|--------|------|-------|
| bin | varchar | Bank identification number |
| last_four | varchar | Last 4 digits |
| processor_status | enum | Status from processor |
| galileo_* / fis_* | various | Processor-specific IDs |
| shipped_at / issued_at | timestamp | Lifecycle timestamps |

Status events tracked in **member_card_status_event** with sources:
soda, galileo, giesecke-devrient, fis, abcorp.

---

## Benefit System

### benefit
Core benefit definition with versioning.

| Column | Type | Notes |
|--------|------|-------|
| type | enum | fundedBenefit, surveyBenefit, rideBenefit, resourceBenefit, voucherBenefit, gapClosureBenefit |
| sponsor_id | bytea FK | |
| iterations / interval / duration | int | Recurrence config |
| version | int | Version tracking |
| is_current | boolean | Active version flag |
| superseded_by | bytea FK -> benefit | Self-referential version chain |

### Benefit subtypes (one table per type)
- **funded_benefit** -- funding_amount, proration_type (none/prorated/full), priority, variable_amount, otchs_eligible
- **gap_closure_benefit** -- source (sponsor/pharmacy), status (pending/completed/rejected/invalid_time)
- **survey_benefit**, **ride_benefit**, **resource_benefit**, **voucher_benefit** -- type-specific fields

### benefit_factor
Links benefits to factors with factor_values for conditional benefit rules.

### funded_benefit_approval_profile
Links approval profiles (from merchant DB) to funded benefits with factor conditions.

---

## Enrollment & Programs

### enrollment
Links a member to a benefit with lifecycle timestamps.

| Column | Type | Notes |
|--------|------|-------|
| member_id | bytea FK -> member | |
| benefit_id | bytea FK -> benefit | |
| active_at / expires_at | timestamp | Lifecycle |
| funding_amount | numeric | Allocated amount |
| program_enrollment_id | bytea FK | Link to program |
| sponsor_identifier | varchar | External ref |

### program
Groups benefits into a plan year.

| Column | Type | Notes |
|--------|------|-------|
| sponsor_identifier | varchar | |
| sponsor_id | bytea FK | Must be 'brand' variant |
| plan_year | int | |

### program_benefit / member_program_enrollment
M2M relationships linking programs -> benefits and members -> program enrollments.

---

## Factors & Variables

### factor
Sponsor-defined variables used in benefit calculations and conditional rules.

| Column | Type | Notes |
|--------|------|-------|
| sponsor_id | bytea FK | |
| factor_identifier | varchar | String key |
| name / description | varchar | |
| version tracking | | |

### factor_value
Key-value pairs for factor instances.

### member_factor
Per-member factor assignments (e.g., a member's plan tier, geographic region).

---

## Supporting Tables

| Table | Purpose |
|-------|---------|
| **agreement** / **member_agreement** | Terms acceptance tracking |
| **coupon** / **coupon_program** | Coupon management with pools |
| **funding_account** | Accounts for funding allocation |
| **member_disbursement_account** | Member-specific disbursement |
| **call_record** / **ivr_call_record** / **agent_call_record** | Call tracking |
| **custom_field_definition** / **member_custom_field_value** | Sponsor-defined custom fields (string, datetime, boolean, numeric) |
| **member_communication_permission** | Opt-in tracking by channel and source |
| **member_plan_data** | Plan information |
| **member_pharmacy** | Pharmacy network assignments |
| **catalog_kit** / **catalog_family** | Product catalogs |
| **emboss_kit** | Card embossing configs |
| **lob_template** | Mail templates with merge variables |
| **scheduled_action** | Card operations (issue/reissue/replace/cancel) with outcomes |
| **encounter_reporting_file_tracker** | Encounter file tracking |
| **priority_definition** | Priority rules for benefits |
| **report** / **sponsor_report** | Reporting tables |

---

## Key Patterns

1. **XID everywhere** -- All public IDs are bytea (XID format). Conversion functions: `xidb_to_xid()`, `xid_to_xidb()`.
2. **JSONB config** -- Sponsors carry a `config` JSONB column with flexible settings. Brands inherit and merge with customer config via `merged_config`.
3. **Sponsor as isolation boundary** -- Nearly every table has `sponsor_id` FK. Data is partitioned by sponsor.
4. **Benefit versioning** -- Benefits track `version`, `is_current`, and `superseded_by` for safe schema evolution.
5. **Temporal tracking** -- `created_at`, `updated_at`, `deleted_at` (soft deletes) throughout.
6. **Enum-heavy** -- PostgreSQL enums for benefit types, card statuses, proration, etc.
7. **Hierarchical sponsors** -- Customer -> Brand hierarchy via `parent_id` self-reference. Config inheritance flows down.

---

## Relationship Diagram (key FKs)

```
sponsor (customer)
  +-- sponsor (brand, parent_id -> customer)
       +-- member -> member_card -> member_card_status_event
       |           -> member_personal_info_current/history
       |           -> member_factor
       |           -> member_communication_permission
       |           -> enrollment -> benefit -> funded_benefit
       |                                    -> benefit_factor -> factor -> factor_value
       +-- program -> program_benefit -> benefit
       |           -> member_program_enrollment
       +-- funding_account
       +-- agreement -> member_agreement
       +-- custom_field_definition -> member_custom_field_value
       +-- emboss_kit, catalog_kit, lob_template, scheduled_action
```
