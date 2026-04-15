---
title: "Harmony Core Platform Architecture"
summary: "Engineering reference for the Harmony Go monorepo — architecture, services, authentication, authorization, and code organization"
topics: [harmony, architecture, auth, authz, casbin, monorepo, go, openapi]
systems: [Harmony, Auth0, Entra ID, Casbin, GKE]
people: [Chris Brown]
content_type: reference
departments: [engineering]
roles: [all]
classification: internal
last_verified: "2026-03-18"
review_cycle_days: 90
---

# Harmony — Core Platform Architecture

> **What this is:** Engineering reference for the Harmony monorepo — architecture, services, authentication, authorization, and code organization. This is the canonical reference for AI sessions building features in Harmony.
>
> **Owner:** Engineering (Chris Brown, CTO)
> **Last reviewed:** 2026-02-23
> **Source:** Live authz API, OpenAPI specs, codebase analysis, IT/Security context docs

---

## What Harmony Is

Harmony is Evermore's core Go monorepo — the backend API powering all member-facing and partner-facing products. It is a ~950K LOC Go monorepo with 17 API services, 6 databases, and 2 Angular frontend apps.

| App | Audience | Purpose |
|-----|----------|---------|
| **Member Admin (CSRX)** | Health plan sponsor users (external partners) | View and manage member data — enrollments, benefits, cards, transactions, shopping |
| **Soda Admin** | Internal Evermore staff | Internal operations — broader platform access |

**Production API base URL:** `https://api.mysodahealth.com`

---

## Architecture Overview

### Three-Tier Structure

```text
cmd/soda-api/main.go          <- Service registration (17 API services)
  └── internal/<domain>api/    <- Generated API stubs (oapi-codegen from OpenAPI specs)
        └── pkg/<domain>/      <- Hand-written business logic (packages)
              └── db/<database>/  <- Generated DB code (sqlc from SQL queries)
```

- **Services** are registered in `cmd/soda-api/main.go` — each is a domain-scoped API
- **Internal** (`internal/<domain>api/`) contains generated OpenAPI server stubs — do NOT edit these
- **Packages** (`pkg/<domain>/`) contain hand-written business logic
- **Database** (`db/<database>/`) contains migrations and generated query code — do NOT edit generated files

### Databases (6)

| Database | Domain | Key Entities |
|----------|--------|-------------|
| `sponsor` | Sponsor/client management | Sponsors, brands, programs, eligibility |
| `ledger` | Financial transactions | Transactions, settlements, funding |
| `merchant` | Merchant/retailer | Merchants, stores, catalogs, assortment |
| `partner` | Partner integrations | Partner configs, SFTP, file processing |
| `authz` | Authorization | Roles, policies, domains, role grants |
| `sms` | SMS/communications | Messages, templates, delivery status |

### Frontends (2)

| Frontend | Path | Framework | Audience |
|----------|------|-----------|----------|
| Member Admin | `web/apps/member-admin/` | Angular | External health plan users |
| Soda Admin | `web/apps/soda-admin/` | Angular | Internal Evermore staff |

---

## Authentication Model

### Auth0 → Entra ID

Member Admin authenticates through **Auth0** using an enterprise connection to Entra ID (Azure AD).

**Flow:**

1. Partner user navigates to Member Admin
2. Auth0 redirects to Entra ID login
3. Entra authenticates and returns group memberships
4. Auth0 embeds groups in JWT as custom claim: `https://soda.health/groups`
5. Harmony backend reads this claim; the authz service evaluates permissions

### Two Security Schemes

| Scheme | Use Case | Example |
|--------|----------|---------|
| **M2M (machine-to-machine)** | Service accounts, automation | `carbbot:harmony` token |
| **Auth0 Bearer JWT** | Human users | Carries scopes like `read:roles`, `create:role-grants` |

**Key code location:** `pkg/security/auth0.go` — `Auth0Claims` struct including `Groups` custom claim.

---

## Authorization Model (Casbin + Authz API)

Harmony uses a **database-backed Casbin policy engine** exposed via the `authz` API service. This is a full RBAC system, not a simple group-name parser.

### Core Concepts

| Concept | Description | Example |
|---------|-------------|---------|
| **Role** | Named permission bundle | `member-read-only`, `member-edit` |
| **Policy** | Grants a role the ability to perform `action:object` | `read:members`, `write:cards` |
| **Domain** | Scopes a grant to a specific entity (health plan) | Banner Health, CalOptima Health |
| **Role Grant** | Assigns a role to a subject, scoped to a domain | "give Entra group X `member-edit` on Banner Health" |
| **Subject** | The entity receiving a grant | Entra group ID, Auth0 user sub |

### Domain Hierarchy

Domains are **health plan organizations** with parent/child relationships:

- **Top-level domain** = a health plan (e.g., Banner Health)
- **Child domain** = a brand/product line (e.g., Banner Medicare Advantage)

As of 2026-02-19: **54 top-level customer domains**, **125 child brand domains** = 179 sponsor-type domains. **366 total domains** across all types (sponsor, approval_profile, merchant, processor).

Domain IDs are XID-format strings (e.g., `d05b292c6gb7j3vt49hg`).

### Entra Group → Role Grant Flow

The key provisioning endpoint:

```text
POST /authz/role-grants/actions/create-from-group-name
```

This parses an Entra group name following the `{app}-{domain}-{role}` convention and creates the corresponding role grant.

**Group name format:** `{app}-{shortcode}-{role}`

- `app`: prefix (`csrx`, `hub`) — identifies the application context
- `shortcode`: single alphanumeric segment — maps to a domain by lookup
- `role`: the role name (may contain hyphens)
- Special: `x` as shortcode = global grant (all domains)

**Code location:** `pkg/authz/group_name_parser.go`

### Roles (31 total, as of 2026-02-17)

#### Partner-Facing Roles

| Role | ID | Permissions |
|------|----|-------------|
| `member-read-only` | 132 | Read members, cards, benefits, enrollments, transactions, reimbursements |
| `member-edit` | 148 | `member-read-only` + write:members, write:reimbursements |
| `member-card-edit` | 163 | `member-read-only` + write:cards, read/list:merchants |
| `member-impersonation` | 235 | Read + create:shopping_sessions, write:identities, write:portal |
| `shopping-impersonate` | 315 | create:shopping_sessions only |
| `catalog-issuer` | 312 | write:catalogs only |
| `read-only` | 207 | Broad read across members, benefits, transactions, merchants, approval profiles |
| `implementation-admins` | 255 | Full CRUD — used during health plan onboarding |

#### Internal / System Roles

| Role | ID | Notes |
|------|----|-------|
| `admins` | 1 | Full access — internal admins |
| `base-user` | 64 | Minimal — list feature flags, partners, sponsors |
| `benefit-admins` | 67 | Benefits/enrollment CRUD |
| `external-activators` | 89 | write:activations only |
| `external-admins` | 91 | External partner admin |
| `factors-admins` | 318 | Full factor management |
| `factors-read` | 316 | Read/list factors |
| `fis-auth-only` | 105 | write:fis-auth — FIS payment integration |
| `member-admins` | 106 | Broad member admin with shopping/portal access |
| `member-ride-read` | 183 | Read ride transactions only |
| `merchant-admins` | 185 | Merchant CRUD |
| `merchant-integration` | 190 | Enrollment read + activations |
| `merchant-preauth-only` | 198 | Pre-authorization only |
| `merchant-read-only` | 195 | Read merchants only |
| `approval-profile-admins` | 201 | Approval profile CRUD |
| `approval-profile-read-only` | 233 | Read approval profiles |
| `assortment-item-viewers` | 230 | Read catalog items |
| `store-finder` | 313 | list:stores only |
| `ping-only` | 314 | read:pings — health check accounts |
| `internal-updates-read` | 324 | read:internal_updates |
| `processor-admins` | 327 | Full access (processor scope) |
| `processors-admins` | 326 | Legacy duplicate of processor-admins |
| `abcorp-admins` | 330 | ABCorp-specific admin |

---

## Authz API — Key Endpoints

**Base URL:** `https://api.mysodahealth.com`

| Endpoint | Method | Use Case |
|----------|--------|----------|
| `/authz/roles` | GET | List all roles |
| `/authz/domains` | GET | List domains + parent/child structure |
| `/authz/role-grants/actions/create-from-group-name` | POST | Provision access from Entra group name |
| `/authz/subjects/{subject}/role-grants` | GET | Audit a user's current access |
| `/authz/actions/decide` | POST | Test whether subject can perform action in domain |
| `/authz/role-grants/{id}` | DELETE | Revoke a role grant |

---

## Build & Dev Commands

| Command | Purpose |
|---------|---------|
| `make docker-compose-backend` | Start local dev environment |
| `make test` | Run test suite |
| `make api` | Regenerate OpenAPI stubs (`oapi-codegen`) |
| `make queries` | Regenerate DB query code (`sqlc`) |
| `make new-migration DATABASE=<db> NAME=<desc>` | Create new SQL migration |

---

## Code Conventions

### Generated vs. Hand-Written

| Pattern | Location | Editable? |
|---------|----------|-----------|
| `gen_` prefix files | Various | NO — regenerate from source |
| `internal/<domain>api/` | API stubs | NO — edit OpenAPI spec, run `make api` |
| `db/<database>/` output dirs | Query code | NO — edit SQL in `db/*/queries/`, run `make queries` |
| `pkg/<domain>/` | Business logic | YES — hand-written |
| `db/<database>/migrations/` | SQL migrations | YES — hand-written |

### Package Structure

```text
pkg/<domain>/           # Business logic for a domain
internal/<domain>api/   # Generated API stubs
db/<database>/queries/  # SQL query sources
db/<database>/migrations/ # SQL migrations
web/apps/<frontend>/    # Angular frontend apps
decisions/              # Architecture Decision Records
```

---

## Key Code Locations

| Location | Purpose |
|----------|---------|
| `cmd/soda-api/main.go` | Service registration — all 17 API services |
| `pkg/security/auth0.go` | Auth0Claims struct — includes `Groups` custom claim |
| `pkg/authz/group_name_parser.go` | Entra group name → authz API call parsing |
| `pkg/entra/types.go` | PIM group sync config for partner groups |
| `web/apps/member-admin/` | Member Admin Angular frontend |
| `web/apps/soda-admin/` | Soda Admin Angular frontend |
| `decisions/` | ADRs — `041`, `075`, `080`, `088`, `089`, `090` cover auth |

---

## Anti-Patterns

- **Do NOT edit generated files.** Files with `gen_` prefix or in `db/*/` output dirs and `internal/<domain>api/` are generated. Edit the source (OpenAPI spec or SQL query) and regenerate.
- **Do NOT bypass the authz API.** All access control goes through the Casbin policy engine via the authz service. Direct database manipulation of permissions will break.
- **Do NOT mix domain short codes with domain IDs.** Short codes (e.g., `bh`) are for Entra group names only. The authz API uses XID-format domain IDs.
- **Do NOT assume Entra group membership equals access.** The group triggers a role grant via the authz API. Both the group AND the role grant must exist.
