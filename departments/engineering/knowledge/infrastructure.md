---
title: "Infrastructure"
summary: "GKE clusters, Cloud SQL databases, Valkey caching, Pub/Sub messaging, GCS storage, observability stack, and local development environment"
topics: [infrastructure, gke, cloud-sql, valkey, pubsub, gcs, datadog, elastic, terraform, flux, docker]
systems: [GCP, GKE, Cloud SQL, Valkey, Pub/Sub, GCS, Datadog, Elastic, Terraform, Atlantis, FluxCD, Docker]
people: []
content_type: reference
departments: [engineering]
roles: [all]
classification: internal
last_verified: "2026-03-18"
review_cycle_days: 90
---

# Infrastructure

**Last updated:** 2026-02-22
**Sources:** Harmony repo, tf-infra references, Confluence ("Kubernetes Clusters",
HONK meeting notes), Knower search results

---

## Google Cloud Platform

### GKE Clusters

| Cluster | GKE Version | VPC | Purpose |
|---------|-------------|-----|---------|
| **production** | v1.32.x (stable) | production | Production workloads |
| **glo-cv** | v1.32.x (stable) | non-production | Staging/validation with live payment processor connections |
| **pluto** | v1.32.x (stable) | non-production | Testing, pen testing, infra-breaking changes |
| **tooling** | v1.32.x (stable) | tooling | Build nodes (GHA), Atlantis, Elastic synthetics, monitors |

### Cloud SQL (PostgreSQL)

- **Version:** 15.8 (as of Sep 2025; upstream default 16.x)
- **6 databases:** sponsor, ledger, merchant, partner, authz, sms
- **HA:** Hot standby in secondary AZ, warm replica in another region
- **Read replicas:** Implemented for ledger and sponsor services
  - Context-based routing via `X-Soda-Use-Read-Replica` header
  - Env var: `CLOUD_SQL_REPLICA_CONNECTION_NAME`
- **Migrations:** dbmate v2.27.0 with cloud-sql-proxy v2.8.1

### Google Cloud Memorystore (Valkey)

- **What:** HA Redis-compatible cache (Valkey is the open-source Redis fork)
- **Config:** Multi-zone replication, automatic failover, encrypted backups
- **Auth:** TLS + ACLs + IAM token-based authentication
- **Used by:** Tier 2/3 services (caching, distributed locks via distlockutil)
- **Tier 1 services must NOT use cache as source of truth**

### Google Cloud Pub/Sub

- **Topics/subscriptions:** Managed via Terraform in tf-infra
- **Pattern:** Minimal messages (event type + resource ID), exponential backoff retries
- **Rules:** Tier 1 services can publish; Tier 2/3 can subscribe
- **Worker:** `soda-job worker` runs multiplexed subscription handlers
- **Local dev:** Google Pub/Sub Emulator

### Google Cloud Storage (GCS)

- **Multi-region/dual-region buckets** for geo-redundancy
- Used for: file exchange with partners, deployment SHA tracking, report artifacts
- **Local dev:** Fake GCS Server container

### Container Registry

- **Location:** `us-docker.pkg.dev/artifacts-321215/co2-artifacts-docker`
- **Images:** harmony, harmony-migrations, harmony-ivr, harmony-web, galileo-server
- **Service account:** `github-actions-harmony@artifacts-321215.iam.gserviceaccount.com`

---

## Infrastructure as Code

| Tool | Version | Repo | Purpose |
|------|---------|------|---------|
| **Terraform** | 1.3.2 | tf-infra | GCP resource management |
| **Atlantis** | 0.20.1 | tf-infra | Terraform plan/apply via PR comments |
| **FluxCD** | 2.3.0 | k8s-flux | GitOps Kubernetes deployments |
| **Helm** | -- | k8s-flux | Kubernetes package management |

---

## Observability

### Datadog
- **APM:** Orchestrion instrumentation on all soda-api/soda-job builds
- **Metrics:** Tagged metric emission via datadogutil package
- **Logs:** Structured logging with `soda.*`, `fis.*`, `galileo.*` fields
- **Agent:** Sidecar in each pod

### Elastic
- **Version:** 8.15.0 (cluster/console), 8.14.3 (beats)
- **Synthetics:** Playwright-based synthetic monitors in tooling cluster
- **Heartbeat:** Uptime monitoring

### Logging
- Structured via `pkg/logging` (Zap-based)
- Context-preserving with tracing integration
- Log levels: debug/info/warn/error via `LOG_LEVEL` env var

---

## Authentication & Authorization

### Service-to-Service (M2M)
- Custom M2M auth via `pkg/security`
- Services only call lower-tier services (tier 3 -> tier 2 -> tier 1)

### External Auth
- **Auth0:** Member authentication (JWT validation)
- **Azure Entra ID:** Employee/partner SSO
- **Casbin:** RBAC policy engine
  - Local dev: `harmony/conf/development_policy.csv`
  - Cloud: `k8s-flux/apps/common/policy.csv`
  - Groups: Per-environment in `k8s-flux/gke-{env}/apps/common/group.csv`

### Feature Flags
- **LaunchDarkly** via `pkg/featuresutil`
- Sponsor-context-aware flag evaluation

---

## Local Development Stack

```yaml
# docker-compose.yml provides:
- PostgreSQL 17 (all 6 databases)
- Redis (local Valkey substitute)
- Fake GCS Server
- Google Pub/Sub Emulator
- Datadog Agent
- All 16+ API services
- Metabase (BI dashboards)
- Benthos (stream processing)
```

**Key commands:**
```bash
make docker-compose              # Full stack with hot-reload (Air)
make docker-compose-backend      # Backend + pre-built web image
make docker-compose-web          # Backend + local web mount
make docker-compose-functional   # Minimal for functional tests
make docker-compose-debug        # Delve debugger attached
make seed                        # Load test data
```

**Environment files:**
- `.env` -- Local defaults
- `.env-secrets` -- Sensitive values (1Password integration via `op run`)
- `.env-datadog` -- Datadog API key
- `.e6-prod-vars` / `.e6-gcv-vars` -- E6 payment processor configs
- `.fis-prod-vars` / `.fis-uat-vars` -- FIS payment network configs

---

## Key Version Inventory (as of late 2025)

| Component | Version | Notes |
|-----------|---------|-------|
| GKE | v1.32.6 | Stable channel |
| Go | 1.24 | With Orchestrion APM |
| PostgreSQL (Cloud SQL) | 15.8 | HA with replicas |
| FluxCD | 2.3.0 | |
| Terraform | 1.3.2 | |
| Atlantis | 0.20.1 | |
| Elastic | 8.15.0 | Cluster + console |
| dbmate | 2.27.0 | Migration runner |
| Node.js | LTS | Frontend builds |
| Angular | -- | Nx monorepo (web/) |
