---
title: "Data Model: Partner"
summary: "Schema reference for the partner database -- data integration orchestration, Benthos stream configs, job processing, and activity audit logs"
topics: [data-model, partner, benthos, jobs, audit-log, sftp, integrations]
systems: [Harmony, Cloud SQL, PostgreSQL, Benthos]
people: []
content_type: reference
departments: [engineering]
roles: [all]
classification: internal
last_verified: "2026-03-18"
review_cycle_days: 90
---

# Data Model: partner

**Database:** partner
**Migrations:** 75
**Tables:** ~10

The partner database manages data integration orchestration, job processing,
and activity audit logs.

---

## Integration Job Management

### benthos_stream_configuration
Declarative data pipeline config for the Benthos streaming framework.

| Column | Type | Notes |
|--------|------|-------|
| job_processing_type | enum (22 values) | What kind of data this pipeline processes |
| label | varchar | |
| name_pattern | varchar | File matching pattern |
| configuration_template | text | Benthos YAML template |
| autorun / autodryrun / autofinalize | boolean | Automation flags |
| codec | varchar | Data codec |
| respect_file_order | boolean | Sequential processing |

**22 job processing types:** intake_member, intake_eligibility, intake_location,
intake_item, intake_merchant, intake_funding, intake_cc_matcher, intake_ride_restriction,
intake_voucher, intake_card_shipping, intake_rdf_customer_master, batch_intake_items,
intake_fineline, batch_intake_fis_transaction_items, intake_member_gap_closure,
intake_sponsor_benefit, intake_benefit, batch_intake_sif_prediction,
batch_intake_item_details_metadata, batch_intake_item_details_attributes,
batch_intake_item_details_nutrition

### job
| Column | Type | Notes |
|--------|------|-------|
| partner_id | FK | |
| processing_type | enum | |
| status | enum | created, deleted, committed, dry_run, error, incomplete, cancelled, finalized |

### job_run
Execution history with status tracking (created, started, success, error, cancelled, incomplete).

### line_item
Individual data records within a job. Status: created, invalid, valid, warning.

---

## Partner Configuration

### partner
| Column | Type | Notes |
|--------|------|-------|
| id | bytea (XID) | |
| name | varchar | |
| bucket_name | varchar | GCS/S3 bucket for file exchange |
| partner_type | enum | sponsor, merchant, processor, internal |
| short_code | varchar(5) | Uppercase, CLI-friendly |
| config | jsonb | |

### partner_key
API keys/credentials for partner authentication.

---

## Activity Audit Trail

### activity_log
Complete audit trail with causality chains.

| Column | Type | Notes |
|--------|------|-------|
| event_id | bytea | |
| event_parent_id | bytea | Causality chain |
| actor / actor_type | varchar | Who did it |
| resource_id / resource_type | varchar | What was affected |
| action | varchar | What happened |
| occurred_at / recorded_at | timestamp | When |
| metadata | jsonb | Additional context |

### activity_log_related
Cross-references for related resources affected by an event.

---

## Key Patterns

1. **Benthos for data pipelines** -- Declarative streaming configs for 22 data intake types
2. **Job lifecycle** -- created -> committed -> dry_run -> finalized (with error/cancel branches)
3. **Activity logging** -- Parent event IDs enable causality chain reconstruction
4. **Partner abstraction** -- Multi-tenant data integration with type-based routing
5. **Short codes** -- 5-char uppercase identifiers for CLI/API use
