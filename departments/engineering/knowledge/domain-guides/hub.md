---
title: "Domain Guide: Hub"
summary: "Sponsor-facing web portal -- SSR-only service for job tracking, reporting dashboards, and account management"
topics: [hub, tier-3, ssr, templ, metabase, sponsor-portal]
systems: [Harmony, Metabase, Redis]
people: []
content_type: reference
departments: [engineering]
roles: [all]
classification: internal
last_verified: "2026-03-18"
review_cycle_days: 90
---

# Domain Guide: Hub

**Tier:** 3 (Web -- stateless, no database)
**Package:** `pkg/hub/` (13 Go files -- 8 impl, 5 test)
**API Spec:** None -- SSR-only portal (no REST API)
**Database:** None -- session state in Redis

---

## What the Hub Domain Owns

Hub is the **sponsor-facing web portal**. Sponsors (customers) log in to:

- Track data processing jobs (eligibility files, benefits, gap closures, merchant uploads)
- View job results and line-item details
- Access reporting dashboards (embedded Metabase)
- Manage their account

## Architecture

Hub is a lightweight SSR portal:
- **Templ templates** for HTML rendering (pages, layouts, components)
- **Chi router** for HTTP handling
- **Redis** for session management
- **Metabase** for embedded analytics dashboards

Service calls:
- **partner** -- job queries and status
- **sponsor** -- sponsor data and configuration
- **GCS** -- file and report storage

## Key Files

| File | Purpose |
|---|---|
| `router.go` | Route definitions and middleware |
| `api_authentication.go` | Sponsor login/logout |
| `api_jobs.go` | Job listing and details |
| `api_reporting.go` | Metabase dashboard integration |
| `authenticator.go` | Auth middleware |
| `metabase.go` | Metabase embed token generation |
| `session/session.go` | Redis-backed session management |
| `pages/` | Templ page templates (home, jobs, reporting, sign-in) |

## Key Relationship to Kestrel

**Hub is the existing sponsor-facing portal.** Kestrel combines Hub's monitoring
capabilities with Admin's configuration capabilities into a unified customer
experience. Hub's job tracking and reporting features will likely be absorbed
into Kestrel.

## Notes for AI Sessions

- Smallest service (13 files) -- SSR only, no REST API
- No OpenAPI spec -- routes defined in `router.go`
- Session state in Redis, not cookies
- Metabase integration for analytics dashboards
