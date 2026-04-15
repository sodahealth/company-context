# Engineering Department Context

This directory contains knowledge, prompts, and people profiles for the Product Engineering department at Evermore.

## What's Here

```text
departments/engineering/
├── knowledge/               # Architecture, systems, processes, and project references
│   ├── data-model/          # Per-database schema summaries (6 databases)
│   ├── domain-guides/       # Per-domain guides (admin, hub, member, sponsor)
│   ├── ref-harmony.md       # Core platform architecture reference
│   ├── ref-engineering-team.md  # Team structure, squads, reporting chains
│   ├── ref-systems.md       # Engineering systems and tools inventory
│   ├── ref-engineering-processes.md  # Sprint, PR review, deployment, incidents
│   ├── ref-okrs.md          # Engineering OKRs (stub)
│   ├── ref-business-context.md  # Customer-facing product semantics
│   ├── ref-implementation-patterns.md  # Real customer onboarding data from Osprey
│   ├── ref-kestrel.md       # Kestrel self-service sponsor configuration
│   ├── ref-kestrel-revised-plan.md  # Kestrel demo plan (separate service)
│   ├── ref-kestrel-discovery-session.md  # Kestrel requirements scoring session
│   ├── deployment.md        # Deployment flow (PR -> staging -> production)
│   └── infrastructure.md    # GKE, Cloud SQL, Valkey, observability
├── prompts/                 # AI playbooks and session prompts
│   └── kestrel-sponsor-creation.md  # Step-by-step Kestrel implementation guide
└── people/                  # Engineering team member profiles
    └── chris.brown.md       # CTO profile
```

## Harmony Quick Reference

- **Repo:** `sodahealth/harmony` -- 950K LOC Go monorepo
- **Architecture:** Three-tier (API services -> packages -> database)
- **Services:** 17 API services registered in `cmd/soda-api/main.go`
- **Databases:** 6 (sponsor, ledger, merchant, partner, authz, sms)
- **Frontends:** 2 Angular apps (Member Admin / CSRX, Soda Admin)
- **Auth:** Auth0 -> Entra ID enterprise connection; Casbin RBAC via authz API
- **Build:** `make docker-compose-backend` for local dev
- **Tests:** `make test`
- **Deploy:** PR -> GitHub Actions -> GCV -> Flux -> GKE

## Engineering Team Quick Reference

- **CTO:** Chris Brown -- hands-on, reviews PRs daily
- **Managers:** Charley Shamaly (Head of PE), Jon Dowdle (Sr. Mgr), Kevin McHugh (Sr. Mgr)
- **Squads:** Soul (member UX), Banana Dance (payments), Lightning (sponsor/Hub), HONK (infra/SRE)
- **Headcount:** ~30 (24 Product Eng + 3 Software Eng + 3 IT+SEC FTE)

## Source

This content was migrated from `prod-eng-context/` -- the standalone product engineering context repo. The original repo remains as the working source for engineering-specific AI sessions; this copy in company-context makes the knowledge available through the knowledge gateway for cross-team discovery.

## Classification

All files in this directory are classified `internal` with `departments: [engineering]`. Access is controlled by the Content API at runtime based on frontmatter metadata.
