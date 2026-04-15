---
title: "Data Model: Ledger"
summary: "Schema reference for the ledger database -- double-entry bookkeeping for all financial transactions including settlements, reimbursements, and processor integrations"
topics: [data-model, ledger, transactions, bookkeeping, settlement, reimbursement, fis, e6]
systems: [Harmony, Cloud SQL, PostgreSQL]
people: []
content_type: reference
departments: [engineering]
roles: [all]
classification: internal
last_verified: "2026-03-18"
review_cycle_days: 90
---

# Data Model: ledger

**Database:** ledger
**Migrations:** 188
**Tables:** ~51

The ledger database implements double-entry bookkeeping for all financial
transactions in the Harmony platform. Every fund movement is recorded as
balanced entries across books.

---

## Core Ledger

### book

A named account for tracking a specific type of financial activity.

| Column | Type | Notes |
|--------|------|-------|
| id | bytea (XID) | |
| name | varchar | |
| type | enum | benefit_book, coupon_pool_book, coupon_enrollment_book, enrollment_book, member_overage_book, member_surrender_book, ride_balance, sponsor_overage_book |
| idempotence_key | uuid | Prevents duplicate book creation |
| metadata | jsonb | Flexible attributes |

### transaction

A financial event (debit/credit pair).

| Column | Type | Notes |
|--------|------|-------|
| payee | varchar | |
| merchant_id | bytea | |
| effective_date | date | |
| idempotence_key | uuid | Prevents duplicate transactions |
| metadata | jsonb | |

### entry

The atomic unit -- a single line in a book for a transaction.

| Column | Type | Notes |
|--------|------|-------|
| transaction_id | bytea FK -> transaction | |
| book_id | bytea FK -> book | |
| amount | numeric | Positive or negative |
| effective_date | date | |
| network | varchar | Payment network |
| approval_profile_id | bytea | Links to merchant DB |
| source_type | enum | Origin of the entry |
| processor_message_identifier | varchar | External reference |

---

## Specialized Book Types

| Table | Purpose |
|-------|---------|
| **benefit_book** | Member benefit spending |
| **coupon_enrollment_book** | Coupon spending |
| **coupon_pool_book** | Coupon pool allocation |
| **enrollment_book** | Enrollment transactions |
| **member_overage_book** | Member overage tracking |
| **member_surrender_book** | Surrender transactions |
| **sponsor_overage_book** | Sponsor-level overages |
| **ride_balance** | Available ride balance per member |
| **funding_account_balance** | Available funding per account |
| **funding_account_balance_threshold** | Alert thresholds |
| **funding_account_deposit** | Deposits to funding accounts |

---

## Transaction Events & Processing

### transaction_event

High-level transaction events with metadata.

### preliminary_transaction

Pre-authorization holds before settlement.

| Column | Type | Notes |
|--------|------|-------|
| type | enum | Hold types |
| member_id | bytea | |
| card_id | bytea | |
| amount | numeric | |

Related: **preliminary_transaction_basket_item**, **preliminary_transaction_benefit_item**,
**preliminary_transaction_coupon_item** -- line-item detail for pre-auth.

### standardized_transaction

Normalized transaction format with source tracking.

Related: **standardized_transaction_benefit_spend**, **standardized_transaction_coupon_spend**.

---

## Processor Integration

| Table | Purpose |
|-------|---------|
| **e6_cooperative_auth_event** | E6 auth events |
| **e6_transaction_identifiers** | E6 ID mappings |
| **fis_transaction_identifiers** | FIS ID mappings |
| **fis_transaction_basket_item** | FIS basket items |
| **fis_delegated_auth** | FIS delegated auth tokens |
| **fis_xml_alert** | FIS alert messages |

---

## Reimbursement

### reimbursement

| Column | Type | Notes |
|--------|------|-------|
| type | enum | settlement, mail, debit_adjustment, sponsor_credit |
| amount | numeric | |
| status_history ref | | Links to status tracking |

Related: **reimbursement_check**, **reimbursement_denial_letter**,
**reimbursement_status_history**, **mail_reimbursement_request**.

---

## Other Tables

| Table | Purpose |
|-------|---------|
| **voucher** / **voucher_event** / **voucher_pool** / **voucher_assignment** | Voucher system |
| **ingo_event** / **ingo_fund_movements** / **ingo_fund_return_balance** | Ingo money movement |
| **bank_account_balance** | External bank balance tracking |
| **settlement_transfer** | Settlement transfers |
| **closed_book** | Archive for closed books |
| **verified_transaction** | Transaction verification |
| **transaction_hold** | Transaction holds/blocks |
| **reversal** | Reversal entries |

---

## Key Patterns

1. **Double-entry bookkeeping** -- Every transaction has balanced entries across books.
2. **Idempotence** -- UUID keys on books and transactions prevent duplicates.
3. **Preliminary -> Settled** -- Pre-auth holds (preliminary_transaction) are separate from settled transactions.
4. **Processor-specific tables** -- Each payment processor (E6, FIS, Ingo) has its own mapping tables.
5. **Basket items** -- Multi-line transactions with item-level detail.
6. **Extensive metadata (JSONB)** -- Flexible attributes on books and transactions.
