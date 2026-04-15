---
title: "Domain Guide: Admin"
summary: "Internal admin portal API -- largest Tier 3 service with 138 endpoints, orchestrating all Tier 1 services for sponsor, benefit, and member management"
topics: [admin, tier-3, orchestration, ssr, templ, chi-router]
systems: [Harmony]
people: []
content_type: reference
departments: [engineering]
roles: [all]
classification: internal
last_verified: "2026-03-18"
review_cycle_days: 90
---

# Domain Guide: Admin

**Tier:** 3 (Web -- stateless, no database)
**Package:** `pkg/admin/` (95 Go files -- 54 impl, 41 test)
**API Spec:** `internal/adminapi/adminapi.yaml` (138 endpoints, 23 top-level paths)
**Database:** None -- orchestration layer
**UI:** REST API + SSR pages (Chi router + Templ templates)

---

## What the Admin Domain Owns

Admin is the **internal operations portal** -- the largest Tier 3 service by
endpoint count. Evermore staff use it to manage every aspect of the platform:

- Sponsor CRUD and configuration
- Benefit creation, versioning, approval profile assignment
- Program management
- Member operations (search, view, edit)
- Merchant catalog management
- Partner integration management
- Emboss file generation
- Activity log viewing
- Feature flag management
- Agreement management
- Shopping category management

## Architecture

Admin is the **widest aggregation layer** -- it calls nearly every Tier 1 service:

- **sponsor** -- sponsor/member/benefit/enrollment data
- **merchant** -- merchant catalog, approval profiles, items
- **ledger** -- financial data, transactions
- **partner** -- partner/job management
- **authz** -- authorization rules and policies
- **txn** -- transaction processing

Additional integrations: GCS (file storage), Strapi CMS (content), Pub/Sub,
feature flags, Datadog.

## SSR Components

Admin includes server-side rendered pages alongside the REST API:

- `ssr/handlers/` -- Templ-based page handlers
- `ssr/ui/views/` -- View templates
- `ssr/ui/layouts/` -- Layout templates

## Key Relationship to Kestrel

**Kestrel is the customer-facing evolution of Admin.** Today, capabilities like
sponsor configuration, benefit setup, and funding management are only accessible
through Admin (internal staff). Kestrel aims to expose a subset of these through
a customer-facing portal with guided wizards and self-service flows.

Understanding Admin's API surface is essential for scoping what Kestrel needs
to expose vs. what stays internal-only.

## Notes for AI Sessions

- 138 endpoints -- largest API surface in the system
- No database -- all mutations flow to Tier 1
- SSR pages use Templ (Go templating) -- not Angular
- 41 test files -- extensive test coverage
