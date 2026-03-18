---
title: "AI Playbook: Kestrel Self-Service Sponsor Creation"
summary: "Step-by-step guide for AI-assisted implementation of customer-facing sponsor creation endpoints in Harmony"
topics: [kestrel, sponsor-creation, playbook, openapi, casbin, testing]
systems: [Harmony]
people: []
content_type: prompt
departments: [engineering]
roles: [all]
classification: internal
last_verified: "2026-03-18"
review_cycle_days: 90
---

# AI Playbook: Kestrel Self-Service Sponsor Creation

**Target:** Implement customer-facing API endpoints for self-service sponsor
creation and configuration -- replacing the manual "How to create a sponsor"
process for the most common case.

**Prerequisites:**
- Read `knowledge/domain-guides/sponsor.md` -- understand the domain
- Read `knowledge/ref-kestrel.md` -- understand what Kestrel is solving
- Read `knowledge/data-model/sponsor.md` -- understand the schema

---

## Step 1: Understand the Current API Surface

Read the sponsorapi.yaml spec to understand existing endpoints:
```
internal/sponsorapi/sponsorapi.yaml
```

Key existing endpoints you'll extend:
- `PUT /sponsors/{sponsorID}` -- upsert sponsor
- `PATCH /sponsors/{sponsorID}/config` -- patch config
- `POST /sponsors/{sponsorID}/benefits` -- create benefit
- `POST /sponsors/{sponsorID}/programs` -- create program
- `POST /sponsors/{sponsorID}/funding-accounts` -- link funding account

The goal is NOT to replace these -- it's to add a customer-facing orchestration
layer that calls them in the right order with the right defaults.

---

## Step 2: Design New Endpoints

Add new paths under a `/kestrel/` or `/self-service/` prefix:

```yaml
# Suggested new paths in sponsorapi.yaml:

/sponsors/self-service/create-customer:
  post:
    summary: "Create a new customer sponsor with defaults"
    # Returns: customer ID, default config, next steps

/sponsors/{sponsorID}/self-service/create-brand:
  post:
    summary: "Create a brand under an existing customer"
    # Returns: brand ID, inherited config

/sponsors/{sponsorID}/self-service/configure:
  put:
    summary: "Apply a configuration template to a sponsor"
    # Validates all fields, applies defaults, returns effective config

/sponsors/{sponsorID}/self-service/add-benefit:
  post:
    summary: "Add a benefit with guided defaults"
    # Validates against available approval profiles, suggests proration

/sponsors/{sponsorID}/self-service/status:
  get:
    summary: "Get onboarding completion status"
    # Returns checklist: which steps are done, which remain
```

**Design principles:**
- Customer-facing endpoints validate more strictly (no raw config JSON)
- Include defaults and templates (don't require customers to know all config fields)
- Return clear next-step guidance (wizard-style)
- Use same underlying data model (no new tables for Phase 1)

---

## Step 3: Add Endpoints to the OpenAPI Spec

Edit the source spec:
```
internal/sponsorapi/sponsorapi.yaml
```

Add the new paths, request/response schemas, and security requirements.
Use existing type patterns -- look at how `SponsorInfo`, `BenefitInfo`,
`FundedBenefitInfo` are structured.

**Important:**
- Use `M2M` security for internal paths, `Auth0` for customer-facing
- Add a new Auth0 scope like `self-service:sponsors` for Kestrel users
- Reference existing schemas (don't duplicate)

---

## Step 4: Regenerate Code

After editing the YAML:
```bash
make api
```

This regenerates:
- `internal/sponsorapi/chi-server.go` -- new route handlers
- `internal/sponsorapi/client.go` -- new client methods
- `internal/sponsorapi/types.go` -- new request/response types

**Do NOT hand-edit these files.** If the spec is wrong, fix the YAML and regenerate.

---

## Step 5: Add Bind() Methods

For each new request body type, add a `Bind()` method in:
```
internal/sponsorapi/helpers.go
```

Pattern:
```go
func (model *SelfServiceCreateCustomerRequest) Bind(r *http.Request) error {
    if model.Name == "" {
        return errors.New("name is required")
    }
    // Validate fields, apply defaults
    return nil
}
```

---

## Step 6: Implement Handler Logic

Create a new file in `pkg/sponsor/`:
```
pkg/sponsor/api_self_service.go
```

Implement the handlers. Each orchestrates existing service methods:

```go
func (s *APIServer) SelfServiceCreateCustomer(w http.ResponseWriter, r *http.Request) {
    // 1. Parse and validate request
    // 2. Apply default config template
    // 3. Call existing CreateSponsor with variant=customer
    // 4. Apply default config via PatchSponsorConfig
    // 5. Return customer ID + status + next steps
}
```

**Key patterns to follow:**
- Use `activitylog.HandleActivityLoggableChanges()` for audit trail
- Use existing DB queries via the generated querier interface
- Return proper HTTP status codes (201 Created, 400 Bad Request, 409 Conflict)
- Include `idempotence_key` support where applicable

---

## Step 7: Add DB Migration (If Needed)

If you need new columns (e.g., `onboarding_status`, `customer_visible` flag):

```bash
make new-migration DATABASE=sponsor NAME=add_onboarding_status
```

This creates a new migration file in `db/sponsor/migrations/`. Write the SQL:

```sql
-- +goose Up
ALTER TABLE sponsor ADD COLUMN onboarding_status TEXT DEFAULT 'in_progress';
ALTER TABLE sponsor ADD COLUMN customer_visible BOOLEAN DEFAULT false;

-- +goose Down
ALTER TABLE sponsor DROP COLUMN onboarding_status;
ALTER TABLE sponsor DROP COLUMN customer_visible;
```

If you add new queries, add them to `db/sponsor/queries/` and regenerate:
```bash
make queries
```

---

## Step 8: Add Casbin Authorization

For customer-facing endpoints, define a new role:

In `conf/development_policy.csv` (for local dev):
```csv
p, kestrel_admin, /sponsors/*/self-service/*, GET
p, kestrel_admin, /sponsors/*/self-service/*, POST
p, kestrel_admin, /sponsors/*/self-service/*, PUT
```

The production policy lives in `k8s-flux/apps/common/policy.csv` (separate repo).

---

## Step 9: Write Tests

Create test file:
```
pkg/sponsor/api_self_service_test.go
```

Follow existing patterns:
```go
func TestSelfServiceCreateCustomer(t *testing.T) {
    req := sponsorapi.SelfServiceCreateCustomerRequest{
        Name: "Test Health Plan",
    }
    resp, err := testClient().SelfServiceCreateCustomerWithResponse(
        context.Background(), req,
    )
    require.NoError(t, err)
    assert.Equal(t, http.StatusCreated, resp.StatusCode())
    assert.NotEmpty(t, resp.JSON201.SponsorID)
}
```

---

## Step 10: Verify

```bash
# Run sponsor tests
make test PKG=./pkg/sponsor/...

# Run full test suite
make test

# Local verification
make docker-compose-backend
# Wait for services to start, then test via curl or API client
```

---

## Files You'll Touch (Summary)

| File | Action |
|---|---|
| `internal/sponsorapi/sponsorapi.yaml` | Add new endpoint definitions |
| `internal/sponsorapi/helpers.go` | Add Bind() methods for new types |
| `pkg/sponsor/api_self_service.go` | NEW -- handler implementations |
| `pkg/sponsor/api_self_service_test.go` | NEW -- tests |
| `db/sponsor/migrations/NNN_*.sql` | NEW -- if schema changes needed |
| `db/sponsor/queries/*.sql` | Add queries if needed |
| `conf/development_policy.csv` | Add Casbin policy for new role |

**Files you'll regenerate (don't edit):**
- `internal/sponsorapi/chi-server.go`
- `internal/sponsorapi/client.go`
- `internal/sponsorapi/types.go`
- `internal/sponsor/db/*.go` (if queries change)

---

## Common Pitfalls

1. **Don't edit generated files** -- Always edit the source (YAML or SQL) and regenerate
2. **Config inheritance** -- If creating a brand, `merged_config` must be computed from the customer's config
3. **Benefit versioning** -- New benefits start at version 1 with `is_current=true`
4. **XID format** -- All IDs are bytea XID, not UUID or integer
5. **Snake_case in DB, camelCase in API** -- The helpers handle conversion for config
6. **Approval profiles are cross-domain** -- They live in merchant DB, referenced by sponsor
7. **Test concurrency** -- Tests use `-p 4` to avoid resource exhaustion
