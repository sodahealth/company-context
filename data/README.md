---
title: "Data Directory — Structured Data Files"
summary: "Machine-readable JSON data files consumed by ever-the-helper at runtime. Not knowledge docs — these are registries and configuration data."
content_type: reference
classification: internal
last_verified: "2026-04-27"
review_cycle_days: 90
topics:
  - data
  - registry
  - automation
  - usage-intelligence
systems:
  - ever-the-helper
---

# Data Directory

This directory contains structured JSON data files consumed by `ever-the-helper`
at runtime. Unlike knowledge docs (markdown for humans), these are machine-readable
registries and configuration data.

## Files

| File | Purpose | Consumer |
|------|---------|----------|
| `onboarded-users.json` | Registry of users who received structured onboarding | Usage Analyst (ADR-e069ca3d) |

## Access Pattern

`ever-the-helper` reads these files via the GitHub Contents API using its GitHub App
credentials. The canonical path is:

```http
GET /repos/{owner}/company-context/contents/data/onboarded-users.json
```

Response is base64-encoded JSON. The helper decodes and parses it at runtime.

These files are **not** served through the Knowledge Gateway (which handles markdown
content with RBAC filtering). They are read directly from the repo by server-side code.

## onboarded-users.json Schema

```json
{
  "$schema": "#onboarded-users",
  "version": 1,
  "description": "string — purpose of this registry",
  "updated_at": "YYYY-MM-DD",
  "users": [
    {
      "upn": "string — user principal name (email)",
      "display_name": "string — human-readable name",
      "department": "string — Entra ID department",
      "onboarded_by": "string — username of person who ran the onboarding",
      "onboarded_date": "YYYY-MM-DD — date onboarding was completed",
      "onboarding_type": "string — engagement_session | it_walkthrough | skill_demo",
      "notes": "string (optional) — context about this user's onboarding"
    }
  ]
}
```

### Field Reference

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `upn` | string | yes | User principal name (Entra ID email). Primary key. |
| `display_name` | string | yes | Human-readable name for reports and queries. |
| `department` | string | yes | Department from Entra ID (Growth, Care, Engineering, etc.). |
| `onboarded_by` | string | yes | Username (before @) of the person who conducted the onboarding. |
| `onboarded_date` | string | yes | ISO date (YYYY-MM-DD) when onboarding was completed. |
| `onboarding_type` | string | yes | Type of onboarding: `engagement_session` (engage sess), `it_walkthrough` (/getstarted), `skill_demo` (targeted skill introduction). |
| `notes` | string | no | Free-text context about this user's adoption patterns or onboarding circumstances. |

### Version History

| Version | Date | Change |
|---------|------|--------|
| 1 | 2026-04-27 | Initial schema. Seeded with 2 onboarded users. |

### Usage in WI-1 (Usage Analyst)

The Usage Analyst (ADR-e069ca3d, WI-1) reads this registry during Pass 1 to classify
each session's user into one of three audiences:

- **Onboarded** — UPN appears in this registry
- **Power user** — High session volume, not in registry
- **General** — Everyone else

Onboarded users get retention tracking, regression detection (WI-11), and proactive
outreach if their usage drops.

### Adding New Users

When a new user completes structured onboarding (via engage session, /getstarted, or
skill demo), add an entry to this file via PR. The Usage Analyst picks up changes on
the next session analysis run (it reads the file fresh each time).

Future: This registry may graduate to Cosmos DB when the number of onboarded users
exceeds what's practical in a flat JSON file (~50+ users).
