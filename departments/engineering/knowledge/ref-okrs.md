---
title: "Engineering OKRs"
summary: "Placeholder for engineering OKR tracking -- current state, known structure, and automation opportunity"
topics: [okrs, metrics, automation, spreadsheets, sharepoint]
systems: [SharePoint, Jira, GitHub, Datadog, Greenhouse, Metabase]
people: [Chris Brown]
content_type: reference
departments: [engineering]
roles: [all]
classification: internal
last_verified: "2026-03-18"
review_cycle_days: 90
---

# Engineering OKRs

> **What this is:** Placeholder for engineering OKR tracking. Chris Brown currently tracks OKRs in spreadsheets -- this document captures the known structure and signals for future automation.
>
> **Owner:** Chris Brown (CTO)
> **Last reviewed:** 2026-02-23
> **Status:** Stub -- to be populated when OKR data is formalized
> **Sources:** CTO discovery profile (file access patterns, Jira activity)

---

## Current State

Engineering OKRs are tracked in **Excel spreadsheets on SharePoint**:

| Document | Access Count (90d) | Notes |
|----------|--------------------|-------|
| `2026 evermore OKRs.xlsx` | 564 | CTO's #1 most-accessed document by far |
| `2026 OKRs.pptx` | 63 | Board/exec presentation format |
| `2Q26 OKRs` (planning) | 10 | Q2 planning already started |

Chris accesses the OKR spreadsheet multiple times per day -- likely reviewing and updating manually. This is the strongest signal for automation opportunity in the CTO's workflow.

---

## Known OKR Structure

Based on discovery profile and Jira activity, engineering OKRs likely cover:

### Engineering Execution
- Sprint velocity / completion rate
- PR throughput and review cycle time
- Incident count and MTTR (tracked in `incident-history.xlsx`)

### Platform Reliability
- Uptime / availability targets
- Incident response times
- Infrastructure cost optimization

### Product Delivery
- Feature delivery against roadmap commitments
- Client onboarding velocity (new health plan implementations)
- Payment processing reliability (FIS/Galileo)

### Team Health
- Hiring targets (GRC role, backfills)
- AI tooling adoption (ETS charter goal)
- Engineering culture metrics (demos, documentation)

---

## Automation Opportunity

The OKR spreadsheet is the highest-value automation target identified in the CTO discovery:

| Signal | Value |
|--------|-------|
| File accesses (90d) | 564 -- 6x per day average |
| Format | Excel on SharePoint (manual) |
| Data sources that could auto-populate | Jira (velocity), GitHub (PR metrics), Datadog (uptime), Greenhouse (hiring), Metabase (product metrics) |
| Impact | Reduce daily manual OKR maintenance |

**Recommended approach:** Build a live dashboard or automated data feed that populates metric columns in the OKR tracker. Even partial automation (auto-updating actuals) would save significant CTO time.

---

## Related

- CTO discovery profile: `knowledge/ref-cto-discovery.md` (in it-ops-context)
- Work tracker OKR model: `it-ops-context/` work tracker has a 7-item-type model (objective -> key_result -> project) that could serve as a template
- ETS charter: Engineering Tech Staff virtual team -- owns AI tooling adoption and code quality measurement as charter goals
