---
title: "Data Model: Authz"
summary: "Schema reference for the authz database -- RBAC with hierarchical domains, roles, policies, and role grants"
topics: [data-model, authz, rbac, roles, policies, domains, casbin]
systems: [Harmony, Cloud SQL, PostgreSQL, Casbin]
people: []
content_type: reference
departments: [engineering]
roles: [all]
classification: internal
last_verified: "2026-03-18"
review_cycle_days: 90
---

# Data Model: authz

**Database:** authz
**Migrations:** 7
**Tables:** 5

The authz database implements role-based access control (RBAC) with
hierarchical domains. It's the smallest but most security-critical database.

---

## Tables

### domain
Hierarchical organizational unit for access scoping.

| Column | Type | Notes |
|--------|------|-------|
| id | text | Hierarchical identifier |
| parent_id | text FK -> domain | Self-referential hierarchy |
| domain_type | varchar | |
| name | varchar | |
| metadata | jsonb | |
| deleted_at | timestamp | Soft delete |

### role
Named role definition.

| Column | Type | Notes |
|--------|------|-------|
| id | bigint (auto) | |
| name | varchar | Unique (where deleted_at IS NULL) |
| deleted_at | timestamp | Soft delete |

### role_grant
Assigns a role to a subject within a domain.

| Column | Type | Notes |
|--------|------|-------|
| subject | varchar | Who (user identifier) |
| role | bigint FK -> role | |
| domain | text FK -> domain | Optional scope |
| memo | text | Reason for grant |

**Unique constraint:** (subject, role, domain) WHERE deleted_at IS NULL

### policy
Defines what a role can do.

| Column | Type | Notes |
|--------|------|-------|
| role | bigint FK -> role | |
| object | varchar | What resource |
| action | varchar | What operation |

**Unique constraint:** (role, object, action) WHERE deleted_at IS NULL

---

## Key Patterns

1. **Hierarchical domains** -- Self-referential parent_id for organizational scoping
2. **Soft deletes everywhere** -- deleted_at with partial unique indexes on active records
3. **Subject -> Role -> Policy** -- Classic RBAC: subjects get roles, roles have policies
4. **Domain-scoped grants** -- Role grants can be scoped to a specific domain
5. **Memo field** -- Audit trail for why a grant was created
