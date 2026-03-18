---
title: "Engineering Processes"
summary: "Engineering workflows including sprint process, PR review, deployment cadence, incident tracking, and decision-making patterns"
topics: [process, sprints, pr-review, deployment, incidents, adrs, jira]
systems: [GitHub, Jira, Confluence, OpsGenie, Slack, Flux]
people: [Chris Brown]
content_type: process
departments: [engineering]
roles: [all]
classification: internal
last_verified: "2026-03-18"
review_cycle_days: 90
---

# Engineering Processes

> **What this is:** Reference for engineering workflows -- sprint process, PR review, deployment cadence, incident tracking, and decision-making. Extracted from CTO discovery profile and Confluence documentation.
>
> **Owner:** Chris Brown (CTO)
> **Last reviewed:** 2026-02-23
> **Sources:** CTO discovery profile, Confluence eng spaces, Jira activity analysis

---

## Sprint Process

### Squad-Based Sprints

Engineering runs sprints organized by squad (Soul, Banana Dance, Lightning, HONK). Each squad has its own Jira project and backlog.

**Key ceremonies (from Confluence):**
- **Sprint Kickoff** -- Chris Brown maintains a Sprint Kickoff Script in Confluence
- **Engineering Furthermore** -- biweekly + monthly product demos
- **Engineering demos** -- squad-level feature showcases

### Jira Workflow

Typical issue lifecycle:

```
Backlog -> To Do -> In Progress -> Done/Resolved
```

Additional statuses observed in CTO's Jira activity:
- **Parking lot** -- long-term strategic items (EGGS, FRETS projects)
- **On Hold** -- blocked or deprioritized
- **Selected for Development** -- pulled into sprint
- **Draft** -- policy documents (PPM project)

### Jira Usage Patterns

Chris Brown creates 100+ tickets per 90 days across 10+ projects. He uses Jira as both a planning tool and a delegation mechanism:

- **KICK** -- CTO strategic backlog (41 reported in 90d). Bulk ticket creator for items like PIM docs, partner-permissions-propagator, Metabase rollout plans
- **HONK** -- Infrastructure backlog (34 reported). Magus proxy, gcloud session duration, Countly, Partner ETL
- **EGGS** -- Strategic debt register (17 items in Parking lot). "Are we in CCPA scope now?", "Incident Management beyond Engineering", "Replace OpsGenie"
- **SEC** -- Security findings from pentests (4 open: Dynamsoft license, Magus RCE, improper SLO, excessive session lifetime)

---

## PR Review Process

### GitHub as Daily Driver

GitHub Enterprise is the most consistently used tool across engineering -- CTO active on 71 of 90 days. The primary workflow:

1. **Feature branch** -- all work on branches, never push directly to main
2. **PR creation** -- with description, linked Jira ticket
3. **Code review** -- required before merge
4. **CI checks** -- GitHub Actions runs on PR
5. **Merge** -- squash-merge to main

### Conventions

- All repos use **feature branches + PRs** -- no direct pushes to main
- Squash-merge is the standard merge strategy
- PRs should reference the Jira ticket
- Generated code (`gen_` prefix, `internal/`, `db/` output) must be regenerated, not hand-edited

---

## Deployment Flow

```
PR merged -> GitHub Actions (CI) -> GCV (verification) -> Flux (GitOps) -> GKE (production)
```

See `deployment.md` for the detailed flow. Key points:

- **Flux** manages GitOps deployments to GKE
- **GCV** (Google Cloud Verification) gates production deployments
- Deployment pauses are tracked as KICK tickets
- Production issues trigger incidents in the Lookout Confluence space

---

## Incident Management

### Current Process

- **Tracking:** Lookout Confluence space -- incident post-mortems (INC-54 through INC-75)
- **Alerting:** OpsGenie for on-call notifications (15 engineers in rotation)
- **History:** `incident-history.xlsx` -- CTO accesses this 96 times per 90 days (manual tracking)
- **Production channel:** #eng-production in Slack

### Incident Post-Mortem Pattern

Incidents are documented in Confluence with:
- Timeline of events
- Root cause analysis
- Action items
- Prevention measures

### Known Gaps

- Incident history tracked in a spreadsheet (high-access, low-automation)
- OpsGenie replacement is on the EGGS strategic backlog
- "Incident Management beyond Engineering" is a parking lot item -- incidents that span non-engineering teams lack a formal process

---

## Decision Making

### Architecture Decision Records (ADRs)

Engineering uses ADRs to capture significant technical decisions. Stored in the Harmony repo under `decisions/`.

Key auth-related ADRs: `041`, `075`, `080`, `088`, `089`, `090`

### Chris Brown's Decision Style

From discovery profile: **States intent -> gives time for objection -> acts.** He calls this "Intentional Decision Making" -- documented in his Confluence personal space.

- Communicates via Slack with clear @-mention ownership
- Delegates through Jira with explicit assignment
- Heavy documentation habit -- 312 Confluence pages created

---

## Engineering Culture & Documentation

Chris maintains several foundational documents in Confluence:

| Document | Space | Purpose |
|----------|-------|---------|
| Engineering Culture & Values | Engineering | Defining document for eng org |
| Engineering Tech Staff (ETS) Charter | Engineering | Virtual team he sponsors -- AI tooling adoption, code quality |
| Sprint Kickoff Script | Engineering | Operational sprint process |
| Engineering Orientation | Engineering | Onboarding pipeline for new engineers |
| SDLC Policy | Engineering | Formal development lifecycle |
| How to do Engineering Furthermore | Personal | Meeting/demo format |
| Working with Chris Brown | Personal | CTO communication preferences |
| Thumbs-Up Talks | Personal | Feedback/recognition format |

---

## Cross-Functional Touchpoints

| Process | Engineering Role | Other Teams |
|---------|-----------------|-------------|
| **Partner onboarding** | Create domains, configure auth | Health Plan Solutions, IT+SEC |
| **Incident response** | Triage, fix, post-mortem | Customer Care (member impact), M&P (payment issues) |
| **Security findings** | Remediate pentest items (SEC project) | IT+SEC (policy, compliance) |
| **Metabase rollout** | Infrastructure, SSO, RLS | IT (SSO integration), Product (dashboards) |
| **AI tooling** | Evaluate and adopt | IT+SEC (licensing, Entra groups) |
| **Hiring** | Interview, evaluate | People Ops (pipeline, onboarding) |

---

## Working Hours

Engineering leadership maintains availability across US business hours with occasional evening sessions for production issues or async catch-up.
