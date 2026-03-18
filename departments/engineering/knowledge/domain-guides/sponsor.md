---
title: "Domain Guide: Sponsor"
summary: "Largest and most complex Harmony domain -- Tier 1 service owning sponsors, members, benefits, enrollments, programs, cards, and funding with 200+ API endpoints"
topics: [sponsor, tier-1, benefits, enrollments, programs, config, casbin, versioning, hierarchy]
systems: [Harmony, Cloud SQL, PostgreSQL, Galileo, FIS, E6]
people: []
content_type: reference
departments: [engineering]
roles: [all]
classification: internal
last_verified: "2026-03-18"
review_cycle_days: 90
---

# Domain Guide: Sponsor

**Tier:** 1 (Core -- database-backed, M2M auth only)
**Database:** sponsor (266 migrations, ~70 tables, 27 query files)
**Package:** `pkg/sponsor/` (110 Go files, 55 test files)
**API Spec:** `internal/sponsorapi/sponsorapi.yaml` (11,765 lines, 200+ endpoints)
**Generated code:** `internal/sponsorapi/chi-server.go`, `client.go`, `types.go`, `spec.go`
**Hand-written helpers:** `internal/sponsorapi/helpers.go` (Bind methods), `benefit_helpers.go`

---

## What the Sponsor Domain Owns

The sponsor service is the **largest and most complex domain** in Harmony. It owns:

- **Sponsors** -- Health plan sponsor entities (customers and brands)
- **Members** -- People enrolled in a sponsor's programs
- **Benefits** -- What members get (funded, ride, survey, resource, voucher, gap closure)
- **Enrollments** -- Member -> benefit relationships with lifecycle
- **Programs** -- Groups of benefits within a plan year
- **Factors** -- Variables used in benefit calculations (income level, family size, etc.)
- **Cards** -- Physical/virtual payment cards issued to members (via Galileo, FIS, E6)
- **Funding accounts** -- Where money comes from (linked to processors)
- **Config** -- Flexible JSONB configuration with hierarchical inheritance
- **Agreements** -- T&C documents members must accept
- **Custom fields** -- Sponsor-defined member attributes
- **Coupons** -- Coupon pools and enrollments
- **Catalogs** -- Product/item catalogs for OTC benefits
- **Call records** -- IVR/agent interaction logs
- **Encounter reporting** -- Healthcare encounter data
- **Scheduled actions** -- Deferred card operations

---

## Core Architectural Patterns

### 1. Sponsor Hierarchy (Customer -> Brand) -- ADR-068

```
Customer (variant='customer', parent_id=NULL)
  +-- config: base settings (FIS, Galileo, Iterable)
  +-- merged_config = config (identity -- no parent to inherit from)
  +-- Brand (variant='brand', parent_id=customer.id)
      +-- config: brand-specific overrides only
      +-- merged_config = customer.config + brand.config (brand wins)
      +-- Members belong to brands, not customers
```

**Rules:**
- Customers have no parent. Brands must have a customer parent.
- Members are always associated with a brand (or a standalone customer).
- Config inheritance is write-time (computed on PATCH, stored in `merged_config`).
- Patching a customer's config recalculates ALL child brands' merged configs.

### 2. Config JSON Structure -- ADR-078

The `config` column is JSONB with flexible schema. Key sections:

```json
{
  "galileo_config": { "galileo_funding_account_prn": "004", "galileo_product_identifier": 296772 },
  "fis_config": { "subprogram_id": "123456", "prin": "005", "accounts": { "dan": "..." } },
  "iterable_api_key": "base64-encoded",
  "otc_config": { "providers": { "OTCHS": true } },
  "auth0_sso_connection_name": "external-sso-conn"
}
```

**Config patching** uses RFC 7386 JSON Merge Patch:
- Snake_case in DB, camelCase in API (conversion in `PatchSponsorConfig`)
- Empty string in PATCH -> field removal (normalized to null)
- `api_config.go` handles the full merge/patch/inheritance flow

### 3. Benefit Versioning -- ADR-067

Benefits are immutable once enrollments exist. Changes create new versions:

```
Benefit v1 (is_current=true)
  -> Benefit v2 (superseded_by=v1, is_current=true, v1.is_current=false)
    -> Benefit v3 (superseded_by=v2, is_current=true, v2.is_current=false)
```

- Existing enrollments keep their original benefit version
- New enrollments use the current version
- `sponsor_identifier` + `is_current=true` is unique per sponsor
- Cannot roll back; only forward versioning

### 4. Benefit Types

| Type | DB Table | Key Fields | Purpose |
|------|----------|-----------|---------|
| fundedBenefit | funded_benefit | funding_amount, proration_type, priority, otchs_eligible | OTC/gift card spending |
| rideBenefit | ride_benefit | max_cost_per_ride, num_one_way_rides, max_distance_miles | Transportation |
| surveyBenefit | survey_benefit | survey_json | Enrollment verification forms |
| resourceBenefit | resource_benefit | -- | Non-fundable resources |
| voucherBenefit | voucher_benefit | voucher_pool_id | Multi-use voucher pools |
| gapClosureBenefit | gap_closure_benefit | source, partner_identifier, incentive_benefit_id | Healthcare gap closures |

### 5. Member Multi-Processor Support

A member can have cards across 3 processors simultaneously:

| Processor | Field | Usage |
|-----------|-------|-------|
| Galileo | `processor_identifier` | Primary card issuer |
| FIS | `fis_identifier` | FIS cards, dual issuance |
| E6 | `e6_customer_identifier` | SNAP/WIC (some states) |

### 6. Approval Profiles (Cross-Domain)

Approval profiles live in the **merchant** database but are referenced by sponsor benefits:
- `funded_benefit_approval_profile` links an AP to a funded benefit
- APs restrict what members can buy (by MCC, merchant, category, or item)
- Three restrictiveness levels: general, targeted, specific
- Direct item targeting via `approval_profile_item` (ADR-2026-01-29)

---

## Key API Endpoints (Grouped)

### Sponsor Operations
```
GET    /sponsors                                    # List (filter by variant)
GET    /sponsors/{sponsorID}                        # Get (includes brands for customer)
PUT    /sponsors/{sponsorID}                        # Upsert
GET    /sponsors/{sponsorID}/config                 # Get effective config
PATCH  /sponsors/{sponsorID}/config                 # JSON Merge Patch config
```

### Member Operations
```
POST   /sponsors/{sponsorID}/members                # Create member
GET    /sponsors/{sponsorID}/members                # List (paginated, searchable)
GET    /sponsors/{sponsorID}/members/{memberID}     # Get full member
PATCH  /sponsors/{sponsorID}/members/{memberID}     # Update member
POST   .../members/actions/deactivate-member        # Deactivation
```

### Benefit Operations
```
POST   /sponsors/{sponsorID}/benefits               # Create benefit
GET    /sponsors/{sponsorID}/benefits               # List (filter by type, search)
GET    /sponsors/{sponsorID}/benefits/{benefitID}   # Get
PUT    /sponsors/{sponsorID}/benefits/{benefitID}   # Update
DELETE /sponsors/{sponsorID}/benefits/{benefitID}   # Soft delete
PUT    .../benefits/{benefitID}/supersede           # Create new version
```

### Enrollment Operations
```
POST   .../members/{memberID}/enrollments           # Enroll
GET    .../members/{memberID}/enrollments           # List
DELETE .../members/{memberID}/enrollments/{id}      # Remove
GET    .../members/{memberID}/enrollments/groups    # Grouped by benefit
```

### High-Volume Lookup Actions
```
POST   /sponsors/actions/lookup-member-by-processor-identifier
POST   /sponsors/actions/lookup-member-card-auth-data
POST   /sponsors/actions/lookup-member-by-merchant-preauth
POST   /sponsors/actions/lookup-newest-member-card-by-prn
POST   /sponsors/actions/identify-reimbursement-member
```

---

## Package Structure

### Hand-Written (pkg/sponsor/)

| File Pattern | Purpose |
|---|---|
| `api_sponsors.go` | Sponsor CRUD, hierarchy management |
| `api_config.go` | Config patching with inheritance |
| `api_benefits.go` | Benefit CRUD, versioning |
| `api_enrollments.go` | Enrollment management |
| `api_members.go` | Member CRUD |
| `api_cards.go` | Card operations |
| `api_factors.go` | Factor definitions |
| `api_funding_accounts.go` | Funding account linking |
| `api_programs.go` | Program management |
| `benefit_helper.go` | Date calculations, reload logic |
| `member.go` | Full member assembly |
| `worker.go` | Pub/Sub event handlers |
| `eligibility_intake_*.go` | Eligibility workflow |
| `enrollment_qualification.go` | Auto-enrollment rules |
| `intelligent_kit_assignment.go` | Card kit routing |

### Generated (internal/sponsorapi/)

| File | Size | Generated By |
|---|---|---|
| `chi-server.go` | 424KB | oapi-codegen (from sponsorapi.yaml) |
| `client.go` | 1.4MB | oapi-codegen |
| `types.go` | 195KB | oapi-codegen |
| `spec.go` | 67KB | oapi-codegen |

**Do NOT edit generated files.** Edit `sponsorapi.yaml` and run `make api`.

### Hand-Written Helpers (internal/sponsorapi/)

| File | Purpose |
|---|---|
| `helpers.go` | `Bind()` methods for request validation (required by go-chi/render) |
| `benefit_helpers.go` | Benefit type predicates |
| `constants.go` | Enum constants |

---

## Database Query Files (db/sponsor/queries/)

| File | Key Queries |
|---|---|
| `sponsor.sql` | Search, upsert, config updates, hierarchy |
| `benefit.sql` | Complex benefit queries with full JOIN metadata |
| `member.sql` | Lookups by ID, sponsor ID, processor ID, search |
| `enrollment.sql` | Create, list, delete, conflict detection |
| `factors.sql` | Factor definitions, values, benefit associations |
| `funding_account.sql` | CRUD and sponsor linking |
| `program.sql` | CRUD, benefit associations, auto-enrollment |
| `cards.sql` | Card operations and status |
| `agreement.sql` | Agreements and sponsor exclusions |
| `catalogs.sql` | Item/product catalogs |
| `coupons.sql` | Coupon pools and enrollments |
| `member_gaps.sql` | Gap closure tracking |

---

## Testing Patterns

```go
// Typical test pattern
func TestSponsorCreate(t *testing.T) {
    result := createASponsor(t, "Pool Healthcare")
    assert.Equal(t, "Pool Healthcare", result.Name)
}
```

- **55 test files** -- one per API handler
- Helper functions: `createASponsor()`, `createCustomerWithBrand()`
- `testClient()` -- auto-generated OpenAPI client for integration tests
- Setup -> Action -> Assert pattern
- Tests run with `make test` (Go test, `-p 4` concurrency, `-race` flag)

---

## Key Decisions

| ADR | Topic |
|-----|-------|
| 068 | Customers and Brands hierarchy |
| 078 | Config inheritance (write-time merge, RFC 7386) |
| 067 | Benefit versioning (superseded_by chain) |
| 069 | Approval profile calculated attributes |
| 2026-01-29 | Direct item targeting in approval profiles |
| 004, 011, 020 | Three-tier architecture (sponsor = Tier 1) |
| 025 | Async messaging via Pub/Sub |
| 006 | Code generation (OpenAPI -> types/routes) |

---

## Common Gotchas

1. **Config inheritance is write-time** -- patching a customer recalculates all brands. Can be slow for customers with many brands.
2. **Benefit versioning is forward-only** -- no rollback. Must create new version to "undo."
3. **Generated files are huge** -- `client.go` is 1.4MB. Don't read the whole thing; search for specific types.
4. **Snake_case vs camelCase** -- DB is snake_case, API is camelCase. Conversion in config patching code.
5. **Empty string -> null** -- In config PATCH, empty string means "remove this field" (RFC 7386 normalization).
6. **Members belong to brands** -- Not customers. The customer is the billing/config parent only.
7. **Approval profiles are cross-domain** -- Defined in merchant DB, referenced by sponsor benefits.
8. **XID format** -- All public IDs are bytea (XID). Use conversion functions `xidb_to_xid()` / `xid_to_xidb()`.
