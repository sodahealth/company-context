---
title: "Domain Guide: Member"
summary: "Member-facing API layer -- Tier 3 orchestration service for benefits, cards, transactions, surveys, and shopping"
topics: [member, tier-3, orchestration, benefits, cards, transactions, auth0]
systems: [Harmony, Auth0, FIS, Galileo]
people: []
content_type: reference
departments: [engineering]
roles: [all]
classification: internal
last_verified: "2026-03-18"
review_cycle_days: 90
---

# Domain Guide: Member

**Tier:** 3 (Web -- stateless, no database)
**Package:** `pkg/member/` (65 Go files -- 37 impl, 28 test)
**API Spec:** `internal/memberapi/memberapi.yaml` (35 endpoints)
**Database:** None -- pure orchestration via M2M calls to Tier 1 services

---

## What the Member Domain Owns

The member service is the **member-facing API layer**. Members (end users with
benefit cards) interact with this service to:

- View and manage their benefits and enrollments
- Check card status and request card actions
- View transaction history
- Complete surveys and eligibility intake
- Manage communication preferences
- Browse catalogs and shopping sessions
- Accept agreements

## Architecture

Member is stateless -- it orchestrates calls to lower-tier services:
- **sponsor** -- member data, benefits, enrollments, cards
- **ledger** -- transactions, balances, reimbursements
- **merchant** -- approval profiles, item catalogs
- **partner** -- job status, file processing
- **authz** -- authorization decisions

Additional integrations: Auth0 (identity), FIS/Galileo (card processors),
Datadog, Pub/Sub, Redis (distributed locks, feature flags).

## Key Files

| File | Purpose |
|---|---|
| `api_member.go` | Member profile operations |
| `api_benefits.go` | Benefit listing and details |
| `api_cards.go` | Card operations |
| `api_transaction.go` | Transaction history |
| `workflow.go` | Multi-step workflows |
| `worker.go` | Pub/Sub event handlers |
| `eligibility_intake_*.go` | Eligibility workflow |

## Notes for AI Sessions

- No database to migrate -- changes are purely in API handlers
- All data mutations flow through to Tier 1 services
- Auth: Auth0 JWT for member identity, M2M for service-to-service
- 28 test files -- good coverage for regression testing
