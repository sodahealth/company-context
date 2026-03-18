---
title: "Kestrel Revised Plan -- Separate Service Architecture"
summary: "Kestrel demo plan using separate Tier 3 service in ever-the-presenter calling Harmony's sponsor API via local docker-compose"
topics: [kestrel, architecture, demo, wizard, hpms, pbp-import, ever-the-presenter]
systems: [Harmony, ever-the-presenter, FastAPI, React, Docker]
people: []
content_type: reference
departments: [engineering]
roles: [all]
classification: internal
last_verified: "2026-03-18"
review_cycle_days: 90
---

# Kestrel Demo -- Revised Plan (Separate Service Architecture)

**Date:** 2026-02-22
**Decision:** Build Kestrel as a separate Tier 3 service in `ever-the-presenter`,
calling Harmony's existing sponsor API via local docker-compose. Do NOT modify
Harmony code.

---

## Architecture

```
Kestrel (ever-the-presenter)          Harmony (bliss docker-compose)
+---------------------------------+  +----------------------------------+
|  React frontend                 |  |  sponsor-api   :8443 (HTTPS)    |
|  - 10-step wizard UI            |  |  admin-api     :8443            |
|  - Derived from Osprey data     |  |  postgres      :5432            |
|  - Confidence-scored defaults   |  |  redis         :6379            |
|                                 |  |  fake-gcs      :4443            |
|  FastAPI backend                |--->  pubsub-emu    :8085            |
|  - Orchestration layer          |M2M|  benthos       :4195            |
|  - Calls sponsor API            |  |  seed data loaded               |
|  - M2M_SECRET=m2m_secret        |  |                                 |
+---------------------------------+  +----------------------------------+
     ever-the-presenter                    bliss local fork
     Port 8080                             No push capability
```

### Why Separate Service

1. **Zero risk to production code** -- Harmony is untouched
2. **Our stack** -- Python/React, we know it cold, fast to build
3. **Architecturally correct** -- Kestrel IS a Tier 3 service (customer-facing,
   stateless, calls lower-tier APIs). Same pattern as Admin, Member, Hub.
4. **90%+ confidence** -- no 950K LOC Go codebase to navigate
5. **The demo proves the approach works** without requiring eng approval to modify Harmony

### Auth

Local Harmony docker-compose uses `M2M_SECRET=m2m_secret` for service-to-service
auth. Kestrel's FastAPI backend includes this as a bearer token when calling
the sponsor API. No cloud auth needed.

---

## Revised Phase 3-4 Plan

### Phase 3A: Start Local Harmony (Bliss)

- `cd ~/code/bliss && make docker-compose-backend` -- start all 28 services
- `make seed` -- load test data (sponsors, members, benefits)
- Verify sponsor API responds: `curl -k https://localhost:8443/sponsors`
- Document the API endpoint map (which port, which service, what auth)

### Phase 3B: Build Kestrel in ever-the-presenter

**Backend (FastAPI):**
- New app directory: `backend/kestrel/`
- Router: `/api/kestrel/` prefix
- Harmony client: calls sponsor API with M2M auth
- Endpoints:
  - `POST /api/kestrel/onboarding/start` -- create customer sponsor
  - `POST /api/kestrel/onboarding/{id}/brands` -- add brand under customer
  - `PATCH /api/kestrel/onboarding/{id}/config` -- apply config with defaults
  - `POST /api/kestrel/onboarding/{id}/benefits` -- add benefit with guided defaults
  - `POST /api/kestrel/onboarding/{id}/programs` -- create program
  - `GET /api/kestrel/onboarding/{id}/status` -- onboarding completion checklist
  - `GET /api/kestrel/defaults` -- confidence-scored defaults from Osprey data
  - `GET /api/kestrel/approval-profiles` -- AP catalog for benefit wizard

**Frontend (React):**
- New route: `/kestrel`
- 10-step wizard derived from Osprey implementation patterns:
  1. Brand Structure (how many brands, Program IDs, shortcodes)
  2. Program Configuration (rewards, EGWP, reimbursement, grace period, disenrollment)
  3. Benefit Design (per-brand, guided by AP catalog)
  4. Rewards Configuration (conditional on step 2)
  5. Eligibility Configuration (file format, SFTP, segments)
  6. Member Materials (languages, reading level, review contacts)
  7. Customer Care (option 1/2, after-hours, admin access)
  8. Finance/Invoicing (payment system, tax exempt)
  9. MFA Configuration (standard/SSO)
  10. Edge Case Policies (benefit extension option)
- Pre-filled defaults with confidence indicators
- Real-time validation against sponsor API
- Status dashboard showing onboarding completion

### Phase 3C: HPMS PBP Import -> Auto-Config (NOT a Stretch Goal)

**This is a specced feature with existing infrastructure.**

**What already exists in Harmony:**
- **Benefit Ingestion Job** (shipped mid-2025, KICK-8797): Sponsors upload structured
  CSV via SFTP -> Benthos transforms -> Harmony Benefit Intake API creates benefits.
  No manual Admin entry. Same job infrastructure as eligibility intake.
- **Kestrel Requirements doc** (Confluence, 2026-02-20): Specs the HPMS PBP Import
  Tool -- health plans upload their CMS HPMS PBP Application export, system parses
  it, shows recognized benefits by category, user finalizes.
- **ME-60** (In Testing, Peter Barkey-Bircann): Benefit type templates for Strapi
  content automation.

**What Kestrel adds (the "Step 0"):**
```
HPMS PBP Export (CSV from CMS filing)
  -> AI parses: benefit categories, amounts, periodicity, intended recipients
  -> Maps to Evermore benefit types + approval profiles (using AP catalog from explainers)
  -> Pre-fills wizard steps 3-4 (benefit design + rewards)
  -> Customer reviews, adjusts, confirms
  -> Kestrel calls sponsor API (or generates Benefit Intake CSV for existing job)
```

**Why this is high confidence:**
- The Benefit Ingestion infrastructure already handles CSV -> benefits
- The HPMS PBP export format is structured (CSV, not PDF)
- The mapping from CMS benefit categories to Evermore APs is documented (explainers)
- We only need AI for: parsing the HPMS format + mapping to our categories

**Demo narrative:** "The health plan already told CMS what benefits they offer.
They upload that same filing to Kestrel, the system auto-configures benefits,
and the customer confirms. Zero EZPZs."

**Source:** "Requirements for Kestrel" (Confluence, 2026-02-20):
> "100% of MA clients would have the best experience if they can just drop us
> the HPMS export and that does most of the heavy lifting, then they fill out
> some extra decisions by benefit category."

### Phase 4: Wire Together + Demo

- Kestrel wizard creates real sponsors in local Harmony via API
- Walk through: upload PBP (if available) -> wizard auto-fills -> customer reviews
  -> submit -> sponsors/brands/benefits created in Harmony
- Show traceability: "This default was pre-filled because 93% of 27 customers
  chose this value"
- Show the context layer that made it possible

---

## What's Already Built

| Asset | Location | Status |
|---|---|---|
| Service map (16 services) | `prod-eng-context/knowledge/service-map.yaml` | Done |
| Package graph (75 packages) | `prod-eng-context/knowledge/package-graph.yaml` | Done |
| Data model (6 DBs) | `prod-eng-context/knowledge/data-model/` | Done |
| Sponsor domain guide | `prod-eng-context/knowledge/domain-guides/sponsor.md` | Done |
| Features routing manifest | `prod-eng-context/knowledge/features.yaml` | Done |
| Kestrel context doc | `prod-eng-context/knowledge/ref-kestrel.md` | Done |
| Business context (explainers) | `prod-eng-context/knowledge/ref-business-context.md` | Done |
| Implementation patterns (Osprey) | `prod-eng-context/knowledge/ref-implementation-patterns.md` | Done |
| AI playbook | `prod-eng-context/ai-playbooks/kestrel-sponsor-creation.md` | Done (needs update for separate service approach) |
| Bliss fork | `~/code/bliss` | Done (build passes, tests pass, push disabled) |
| Harmony read-only clone | `~/code/harmony` | Done (push disabled) |
| Go 1.26 + gcloud + Docker | Local machine | Done |

---

## Risk (Revised)

| Risk | Likelihood | Mitigation |
|------|-----------|------------|
| Harmony docker-compose doesn't start | Low (tests already pass) | Debug with eng docs; fall back to mock API |
| M2M auth doesn't work from external service | Low (well-documented) | Test with curl first |
| Wizard scope too ambitious for demo | Medium | Start with steps 1-3 only (brand + config + benefit) |
| PBP processing doesn't exist or isn't ready | Unknown | It's a stretch goal -- wizard works without it |
| 10-step wizard is too many screens | Low | Steps 2-10 have pre-filled defaults; most are confirm-and-continue |
