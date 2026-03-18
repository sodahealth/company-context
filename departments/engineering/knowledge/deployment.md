---
title: "Deployment Flow"
summary: "End-to-end deployment pipeline from PR merge through staging to production via GitHub Actions, GCV, and Flux GitOps"
topics: [deployment, ci-cd, github-actions, flux, gitops, gke, staging, production, canary]
systems: [GitHub Actions, GCV, Flux, GKE, Docker, Slack, Datadog, Elastic]
people: []
content_type: reference
departments: [engineering]
roles: [all]
classification: internal
last_verified: "2026-03-18"
review_cycle_days: 90
---

# Deployment Flow

**Last updated:** 2026-02-22
**Sources:** Harmony repo (.github/workflows/), Confluence ("Automated Deployments",
"Deployments", "Manual Deployments (GHA)", "How to create a new Service/Job")

---

## Overview

Code flows from PR -> main -> container images -> staging -> production on a 2-hour
automated cadence. The pipeline is:

```
PR -> merge to main -> GHA release build -> container images tagged
-> release candidate SHA set -> deploy glo-cv (staging)
-> 1 hour monitoring -> deploy production
```

---

## Pipeline Stages

### 1. Build (on every branch push)
- **Workflow:** `.github/workflows/build.yml`
- **Runner:** `harmony-dind` (Docker-in-Docker, self-hosted)
- **Steps:** Go 1.24 build with race detection, tests with `-p 4` concurrency
- **Auth:** GCP Workload Identity Federation

### 2. Release (on push to main)
- **Workflow:** `.github/workflows/release-main.yml`
- **Docker images built:**
  - `harmony` -- main API binary (distroless, single binary runs all 16 services)
  - `harmony-migrations` -- database migrations (Alpine + dbmate + cloud-sql-proxy)
  - `harmony-ivr` -- IVR service with ONNX Runtime for ML inference
  - `harmony-web` -- Angular frontend
  - `galileo-server` -- Galileo integration server
- **Image tags:** `sha-{12char}`, `edge`, `latest`, `branch-main`
- **Registry:** `us-docker.pkg.dev/artifacts-321215/co2-artifacts-docker`
- **Also:** runs functional tests, publishes `@soda/harmony-client` npm package

### 3. Deploy to Staging (scheduled)
- **Workflow:** `.github/workflows/deploy-glo-cv.yml`
- **Schedule:** 2:15 PM, 4:15 PM, 6:15 PM, 8:15 PM ET, weekdays
- **Mechanism:** Custom `soda-deploy` tool reads next/current SHA from GCS bucket,
  updates `k8s-flux` repo with new image tags
- **Post-deploy:** triggers smoke test workflow (10-min delay), runs BigQuery export

### 4. Monitor (1 hour)
- Synthetics (Playwright) and Datadog monitors run against glo-cv
- If monitors fail, production deployment is automatically blocked
- Monitors can be disabled via `/disable-deploy glo-cv <reason>` Slack command

### 5. Deploy to Production (scheduled)
- **Workflow:** `.github/workflows/deploy-production.yml`
- **Schedule:** Same cadence, ~1 hour after glo-cv
- **Mechanism:** Same `soda-deploy` tool, updates `k8s-flux` for production
- **Notification:** Slack alerts on success/failure

### 6. Flux GitOps Sync
- **FluxCD** watches `k8s-flux` repo for changes
- When image tags are updated, Flux applies the changes to GKE clusters
- Deployment happens within 5-10 seconds of k8s-flux merge

---

## Environments / Clusters

| Cluster | VPC | Purpose |
|---------|-----|---------|
| **glo-cv** | non-production | Global Client Validation -- full workflow with payment processors (FIS, Galileo). Smoke tests run here. |
| **pluto** | non-production | Testing environment for cluster/infra-breaking changes. Also used for pen testing. |
| **production** | production | Production workloads |
| **tooling** | tooling | GHA build nodes, Atlantis, incident bot, Elastic synthetics, pre-auth monitors |

**Staging URLs:** `api-gcv.mysodahealth.dev`, `api-pluto.mysodahealth.dev`
**Production URL:** `api.mysodahealth.com`

---

## Manual / Out-of-Band Deployments

For hotfixes or missed deployment windows:

**Via Slack bot (preferred):**
1. `/update-next-release-sha` (only run ONCE per cycle, requires `#oncall` group)
2. `/deployment-status` to verify
3. `/deploy-cluster glo-cv` -> validate -> `/deploy-cluster pluto` -> `/deploy-cluster production`
4. `/disable-deploy <env> <reason>` to pause automated deploys
5. `/enable-deploy <env>` to resume

**Via GitHub Actions:**
1. Run "Update Next Release" workflow
2. Run "Deploy glo-cv" -> validate -> "Deploy Pluto" -> "Deploy Production"

**Via k8s-flux directly:**
Update `tag` value in `values.yaml` for the target env/app -> merge PR -> Flux syncs in 5-10s.

---

## Canary Deployments
- **Workflow:** `.github/workflows/deploy-canary.yml` (manual dispatch)
- Supports deploying specific SHAs to canary for: `admin-web`, `memberadmin-web`, `microportal-api`

---

## Creating a New Service

1. **In Harmony:** Create OpenAPI spec, Makefile targets, ingress proxy config,
   docker-compose entry, `pkg/` directory, `cmd/` entry point
2. **In k8s-flux:** Create configs for all envs (`/apps`, `/gke-glo-cv`, `/gke-pluto`, `/gke-production`)
3. **In tf-infra:** Create GCP service accounts (`harmonyCore` for DB-using services,
   `harmonyNonCore` otherwise). Add to `ksa_account_map` in `config.auto.tfvars`
4. Deploy to GCV first, validate, then roll to other envs
5. Update the services Miro board

---

## Key Infrastructure Repos

| Repo | What | Tool |
|------|------|------|
| **harmony** | Application code, Dockerfiles, GHA workflows | Go, Docker, GHA |
| **k8s-flux** | Kubernetes manifests, Helm values, image tags | FluxCD, Helm |
| **tf-infra** | GCP infrastructure (GKE, Cloud SQL, IAM, networking) | Terraform, Atlantis |

---

## Test Infrastructure

- **Unit/integration:** `make test` (Go test with `-p 4` parallelism, `-race` flag)
- **Functional:** `make ftest` (docker-compose based)
- **E2E:** Playwright tests in `/harmony/e2e/`, run via GHA ~15 min post-deploy
- **Synthetics:** Elastic Synthetics pods for cloud monitoring
- **CodeQL:** Security scanning via `.github/workflows/codeql-analysis.yml`

**Test concurrency gotcha:** Package parallelism limited to `-p 4` to prevent
"dead shim" container storms in Docker-in-Docker. Peak memory under 14GB.
