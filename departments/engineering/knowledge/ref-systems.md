---
title: "Engineering Systems and Tools"
summary: "Inventory of core systems, tools, and platforms used by the engineering team including development, deployment, monitoring, and collaboration tools"
topics: [systems, tools, infrastructure, ci-cd, monitoring, payments, collaboration]
systems: [GitHub, Jira, Confluence, GCP, GKE, Cloud SQL, Auth0, Datadog, Metabase, OpsGenie, FIS, Galileo, Slack]
people: [Chris Brown]
content_type: reference
departments: [engineering]
roles: [all]
classification: internal
last_verified: "2026-03-18"
review_cycle_days: 90
---

# Engineering Systems & Tools

> **What this is:** Inventory of the core systems, tools, and platforms used by the engineering team. Covers development, deployment, monitoring, and collaboration tools.
>
> **Owner:** Engineering (Chris Brown, CTO)
> **Last reviewed:** 2026-02-23
> **Sources:** Entra group assignments, CTO discovery profile, infrastructure docs

---

## Core Development

| System | Purpose | Access Group(s) | Notes |
|--------|---------|-----------------|-------|
| **GitHub Enterprise** | Source control, PRs, code review | Org membership (`sodahealth/`) | Most consistently used tool (71/90 days for CTO). Monorepo: `sodahealth/harmony` |
| **Jira** | Sprint planning, issue tracking, backlog | Atlassian SSO | Projects: SOUL, KICK, HONK, IT, EZPZ, SEC, DATA, FRETS, EGGS, PPM, MPOPS |
| **Confluence** | Documentation, ADRs, runbooks, policies | Atlassian SSO | Engineering space, Lookout (incidents), Policy Drafting |
| **Cursor** | AI-assisted code editor | `cursor-ai-users` (11/24 eng) | Adopted Feb 2026 |
| **Claude** | AI assistant (code, analysis) | `anthropic-claude-premium-users` (15/24 eng) | Premium tier for most engineers |

---

## Infrastructure & Cloud

| System | Purpose | Access Group(s) | Notes |
|--------|---------|-----------------|-------|
| **GCP (Google Cloud Platform)** | Primary cloud -- GKE, Cloud SQL, Valkey, GCS | `gcp-team-*` per squad, `gcp-production-admins` | See `infrastructure.md` for topology |
| **GKE (Google Kubernetes Engine)** | Container orchestration | `gcp-production-admins` | Flux for GitOps deployment |
| **Cloud SQL** | Managed PostgreSQL (6 databases) | `gcp-prod-all-database-access` (5 people) | sponsor, ledger, merchant, partner, authz, sms |
| **Valkey** | Caching layer | Infrastructure team | Redis-compatible |
| **GCS (Google Cloud Storage)** | Object storage | `gcp-all-sponsor-bucket-objects-list` | Sponsor files, assets |
| **BigQuery** | Data warehouse, analytics | `gcp-production-bigquery-query`, `gcp-production-bigquery-admin` | Hayden + Matthew are admins |

---

## Authentication & Security

| System | Purpose | Access | Notes |
|--------|---------|--------|-------|
| **Auth0** | Identity provider for Harmony apps | Production + Dev instances | Enterprise connection to Entra ID |
| **Entra ID (Azure AD)** | Corporate identity, SSO, group management | IT+SEC managed | Source of group claims for Auth0 JWT |
| **1Password** | Secrets management (team) | Vaults per team/project | FRETS backlog: align with Entra PIM |

---

## Monitoring & Observability

| System | Purpose | Access | Notes |
|--------|---------|--------|-------|
| **Datadog** | APM, monitoring, observability | Engineering team | CTO uses occasionally |
| **Metabase Internal** | Analytics dashboards, BI | `metabase-internal-admins` (Hayden, Matthew) | Replaced external Metabase mid-Jan 2026. SSO integration in progress |
| **OpsGenie** | Incident alerting, on-call | `role-oncall-engineers` (15 people) | EGGS backlog item to evaluate replacement |
| **Lookout** | Incident tracking (Confluence space) | Engineering team | Post-mortems: INC-54 through INC-75 |

---

## Payment Integrations

| System | Purpose | Access | Notes |
|--------|---------|--------|-------|
| **FIS** | Payment processing | `fis-auth-only`, `FIS Alerts` (5 people) | Primary payment rail |
| **Galileo** | Card issuing, transaction processing | `Galileo Notifications` (3 people) | Integration with The Bancorp |

---

## Collaboration

| System | Purpose | Notes |
|--------|---------|-------|
| **Slack** | Primary communication | Squad channels: #team-soul, #team-honk, #team-lightning, #team-banana-dance. Production: #eng-production |
| **Zoom** | Meetings | Daily driver for CTO (44/90 days) |
| **SharePoint** | Document storage | Engineering2 site, Office of the CEO site |
| **Greenhouse** | Hiring pipeline | CTO actively hiring (GRC role, others) |

---

## CI/CD & Deployment

| Component | Purpose | Notes |
|-----------|---------|-------|
| **GitHub Actions** | CI pipeline | Runs on PR |
| **GCV (Google Cloud Verification)** | Deployment verification | Post-CI, pre-prod |
| **Flux** | GitOps -- K8s deployment | PR -> GHA -> GCV -> Flux -> GKE |
| **Docker** | Container builds | `make docker-compose-backend` for local dev |

See `deployment.md` for the full deployment flow.

---

## Jira Project Map

| Project Key | Squad/Team | Purpose |
|-------------|-----------|---------|
| **SOUL** | Soul | Member experience features |
| **KICK** | Banana Dance / CTO | Payment tech + CTO strategic backlog |
| **HONK** | HONK | Infrastructure, DevOps, SRE |
| **IT** | IT+SEC | IT operations, Metabase rollout |
| **SEC** | IT+SEC / Security | Security findings, pentest remediation |
| **EZPZ** | Support | Support investigations |
| **DATA** | Data Engineering | Data pipeline, analytics tooling |
| **FRETS** | Parking Lot | Long-term strategic items |
| **EGGS** | Parking Lot | CTO strategic debt register |
| **PPM** | Policy | Policy documents and change control |
| **MPOPS** | Merchants & Payments | M&P operations |
| **TR** | Service Requests | IT service request tickets |

---

## Access Provisioning Notes

- **Squad GCP access** is managed via Entra groups (`gcp-team-*`) that map to GCP IAM
- **Production admin** is limited to 8 senior engineers via `gcp-production-admins`
- **Database access** is further restricted -- only 5 engineers have `gcp-prod-all-database-access`
- **AI tooling** is broadly available -- 15/24 engineers have Claude premium, 11/24 have Cursor
- **On-call** covers 15/24 engineers with the `role-oncall-engineers` group
