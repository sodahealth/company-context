---
title: "Engineering Team Structure"
summary: "Engineering org structure, squad assignments, reporting chains, GCP access tiers, and AI tooling adoption"
topics: [team, squads, org-structure, reporting, gcp-access, on-call, ai-tooling]
systems: [GitHub, Jira, GCP, Slack]
people: [Chris Brown, Charley Shamaly, Jon Dowdle, Kevin McHugh, Umang Kapadia]
content_type: reference
departments: [engineering]
roles: [all]
classification: internal
last_verified: "2026-03-18"
review_cycle_days: 90
---

# Engineering Team Structure

> **What this is:** Engineering org structure, squad assignments, and reporting chains. Reference for understanding who works on what and how the team is organized.
>
> **Owner:** Chris Brown (CTO)
> **Last reviewed:** 2026-02-23
> **Sources:** Rippling HR, Confluence eng-directory, IT/Security org structure docs

---

## Leadership

| Name | Title | Reports To |
|------|-------|-----------|
| **Chris Brown** | CTO | Robby Knight (CEO) |
| **Charley Shamaly** | Head of Product Engineering | Chris Brown |
| **Jon Dowdle** | Sr. Manager | Chris Brown |
| **Kevin McHugh** | Sr. Manager | Charley Shamaly |

Chris also has direct IC reports: Nick Cruess (Staff Engineer I), Hayden Salmon (Senior Engineer I), Matthew Kennedy (Data Engineer -- departed).

**IT+SEC** (Umang Kapadia, Head of Security) also reports to Chris, with Brandon NeuPhresh and Olivia Conley.

---

## Engineering Squads

Engineers are organized into **cross-functional squads** for sprint work. Squads do NOT map 1:1 to reporting chains -- membership is based on product area. Jira projects align with squad names.

### Soul

**Mission:** Powers the &more user experience -- online experience, mobile app, SMS, IVR, Strapi, CSRX.

| Member | Level |
|--------|-------|
| Charley Shamaly | Head of Product Engineering |
| Helena Chi | Software Engineer III |
| Alexis Goodfellow | Sr. Software Engineer I |
| Dana Kim | Software Engineer I |
| Christopher Perardi | Sr. Engineer II |
| Brennan Tymrak | Software Engineer II |
| Peter Ung | Senior Engineer II |

**Jira project:** SOUL
**Slack:** #team-soul

### Banana Dance

**Mission:** Payment technology and merchant integrations -- FIS, Galileo, issuing partners.

| Member | Level |
|--------|-------|
| Jon Dowdle | Sr. Manager |
| Grae Abbott | Senior Software Engineer II |
| Thomas Doyle-Engler | Software Engineer III |
| Michielu Menning | Sr. Software Engineer I |
| Sean Rycek | Staff Engineer |
| Dalton Shehan | Senior Engineer I |
| Travis Stacy | Contractor |
| Amo Zeng | Software Engineer II |

**Jira project:** KICK (Banana Dance backlog)
**Slack:** #team-banana-dance

### Lightning

**Mission:** Sponsor experience and tooling -- eligibility, Hub.

| Member | Level |
|--------|-------|
| Kevin McHugh | Sr. Manager |
| Garrett Allen | Sr. Software Engineer I |
| Alex Hill | Software Engineer III |
| Nicholas Hung | Software Engineer III |
| Mac Murphy | Software Engineer II |
| Jacob Vernau | Software Engineer III |

**Jira project:** (Lightning backlog)
**Slack:** #team-lightning

### HONK

**Mission:** Cross-cutting platform -- DevOps, infrastructure, SRE, data engineering.

| Member | Level |
|--------|-------|
| Javier Castillo II | DevSecOps Engineer |
| Nick Cruess | Staff Engineer I |
| Hank Hollenstain | Staff Engineer II |
| Matthew Kennedy | Data Engineer (departed) |
| Hayden Salmon | Senior Engineer I |

**Jira project:** HONK
**Slack:** #team-honk

> "Team Honk" is also the informal name for the infra-focused engineers under Jon Dowdle's reporting chain -- Hank, Javier, Nick, Sean. There is overlap but they are not identical.

### IT+SEC

**Mission:** IT projects, helpdesk, security program, infosec compliance.

| Member | Role |
|--------|------|
| Umang Kapadia | Head of Security |
| Brandon NeuPhresh | Software Engineer III (Kandji/MDM) |
| Olivia Conley | Software Engineer II (IT Ops) |

**Jira project:** IT
**Slack:** #it-sec

---

## Reporting Chains (Rippling)

```text
Chris Brown (CTO)
+-- Charley Shamaly (Head of Product Engineering)
|   +-- Kevin McHugh (Sr. Manager)
|   |   +-- Alex Hill
|   |   +-- Garrett Allen
|   |   +-- Jacob Vernau
|   |   +-- Mac Murphy
|   |   +-- Nicholas Hung
|   +-- Alexis Goodfellow
|   +-- Brennan Tymrak
|   +-- Christopher Perardi
|   +-- Dana Kim
|   +-- Helena Chi
|   +-- Justin Antinarella
|   +-- Peter Ung
|   +-- Travis Stacy (contractor)
+-- Jon Dowdle (Sr. Manager)
|   +-- Amo Zeng
|   +-- Dalton Shehan
|   +-- Grae Abbott
|   +-- Hank Hollenstain
|   +-- Javier Castillo II
|   +-- Michielu Menning
|   +-- Sean Rycek
|   +-- Thomas Doyle-Engler
+-- Nick Cruess (Staff Engineer I)
+-- Hayden Salmon (Senior Engineer I)
+-- Matthew Kennedy (Data Engineer) -- departed
+-- Umang Kapadia (Head of Security)
    +-- Brandon NeuPhresh
    +-- Olivia Conley
```

---

## Headcount

| Category | Count |
|----------|-------|
| Product Engineering (Rippling dept) | 24 |
| Software Engineering (Rippling dept) | 3 |
| IT+SEC | 3 FTE + 3 contractors (pending offboard) |
| **Total engineering org** | **~30** |

> **Note:** "Product Engineering" and "Software Engineering" are separate departments in Rippling but report into the same chain under Chris Brown. The split is administrative.

---

## GCP Access Tiers

Engineers have tiered GCP access based on squad and role:

| GCP Group | Members | Access Level |
|-----------|---------|-------------|
| `gcp-production-admins` | Kevin, Hank, Michielu, Nick, Jon, Grae, Garrett, Sean (8) | Production admin |
| `gcp-prod-all-database-access` | Kevin, Hank, Nick, Jon, Sean (5) | All production databases |
| `gcp-organization-admins` | Hank, Jon, Javier (3) | GCP org-level admin |
| `gcp-production-bigquery-query` | Jon, Grae, Thomas (3) | BigQuery read access |
| `gcp-production-bigquery-admin` | Hayden, Matthew (2) | BigQuery admin |
| `gcp-team-soul` | Helena, Dana, Alexis, Peter, Charley (5) | Soul squad GCP resources |
| `gcp-team-banana-dance` | Michielu, Jon, Grae, Amo, Sean, Dalton, Thomas (7) | Banana Dance GCP resources |
| `gcp-team-lightning` | Kevin, Jacob, Garrett, Nicholas, Mac, Charley, Alex (7) | Lightning GCP resources |
| `gcp-team-honk` | Hank, Nick, Jon, Hayden, Javier, Matthew (6) | HONK GCP resources |

---

## On-Call

15 of 24 Product Engineering members are in the `role-oncall-engineers` group. On-call notifications go to `oncall-notified-always` (13 members).

---

## AI Tooling Adoption

| Tool | Entra Group | Coverage |
|------|-------------|---------|
| Claude (premium) | `anthropic-claude-premium-users` | 15/24 Product Eng + 2/3 Software Eng |
| Claude (standard) | `anthropic-claude-users` | 4/24 (Amo, Sean, Dana, Charley) |
| Cursor | `cursor-ai-users` | 11/24 Product Eng |

Chris Brown is actively exploring AI tooling -- tried Claude, Cursor, Copilot Chat, and Office Copilot in Jan-Feb 2026.
