---
title: "Kestrel -- Self-Service Sponsor Configuration"
summary: "Kestrel project reference -- customer-facing evolution of Evermore Admin for self-service benefit program setup and management"
topics: [kestrel, self-service, sponsor, configuration, benefits, admin, hub]
systems: [Harmony, Kestrel, Soda Admin, Hub, Galileo, FIS, Iterable, Vonage, Benthos]
people: [Chris Brown, Nick Cruess]
content_type: reference
departments: [engineering]
roles: [all]
classification: internal
last_verified: "2026-03-18"
review_cycle_days: 90
---

# Kestrel -- Self-Service Sponsor Configuration

**What:** Customer-facing evolution of Evermore Admin that lets sponsors set up,
configure, and manage their own benefit programs.
**Why:** Engineering KR -- **zero EZPZs, database updates, or hardcodes** to bring
a typical supplemental benefits client live.
**Status:** PRFAQ written (2026-02-05). AI demo planned as proof-of-concept.

---

## The Problem

Evermore outgrew its internal Admin tooling. Critical capabilities (funding
balances, member experience preview, benefit hot-swaps, real-time utilization
monitoring, eligibility file processing) remain embedded in the Admin portal,
accessible only to Evermore employees.

This creates operational friction:
- Every new sponsor requires engineer involvement (funding accounts, config, kits)
- Every benefit change requires EZPZ tickets
- Complex variable pricing per customer creates invoicing bottlenecks
- 5x CS ticket volume in Jan 2026 vs entire PY25

## The Vision (from PRFAQ)

Kestrel combines Hub's monitoring features with Admin's configuration
capabilities into a unified customer-facing platform:

1. **Configuration wizards** -- Guided setup for Smart Benefits, Rewards, Conditions
2. **Self-serve benefit config** -- Create/modify benefits without engineer intervention
3. **Funding management** -- Balance monitoring, threshold alerting, deposit tracking
4. **Member experience preview** -- See what members see before going live
5. **Add-on features** -- Reimbursement, Make-it-Rights, Benefit Extensions, Returns
6. **Value-added services** -- Card-linked offers, digital promotions
7. **Metabase-powered insights** -- Usage dashboards and invoicing

---

## What Exists Today (Manual Process)

From "How to create a sponsor from scratch" (Confluence, 2025-03-28):

### Step 1: Create Sponsor in Soda Admin
- Enter name and short code -> get Sponsor ID
- This creates the `sponsor` DB record (variant='customer')

### Step 2: Create Funding Account (ENGINEER REQUIRED)
**For Galileo:**
- Engineer creates funding account -> get PRN
- Link to sponsor via API

**For FIS:**
- Engineer creates subprogram via ACC tool -> get subprogram ID, PRIN, APL ID
- Create funding account -> get DAN
- Create package IDs

### Step 3: Configure FIS/Galileo on Sponsor Config
Via Soda Admin config page (JSON Merge Patch):
```json
{
  "galileo_config": {
    "galileo_funding_account_prn": "004",
    "galileo_product_identifier": 30228
  },
  "fis_config": {
    "prin": "005",
    "apl_id": "1234",
    "waterline": 99999,
    "package_id": "PKG-001",
    "subprogram_id": "456789",
    "accounts": { "dan": "9876543210" }
  }
}
```

### Step 4: Configure Emboss and Catalog Kits
- Emboss kits via Soda Admin UI
- Catalog kits: **manual postgres insert** (not in Admin UI)

### Step 5: Create Benefits
Via Soda Admin:
- Funded benefit (minimum): iteration count, interval, duration, approval profiles,
  proration type, funding amount, priority
- Additional: ride benefits, survey benefits, gap closure benefits

### Additional Steps (Not in Checklist)
- **Iterable setup** -- 15-step process for email/notification configuration
- **Vonage IVR setup** -- Phone number, PIN, Strapi script, destination mapping
- **Casbin policies** -- Authorization rules in k8s-flux
- **Benthos streams** -- Data pipeline configuration for partner file intake
- **Content/garnishes** -- Strapi CMS content per sponsor

---

## What Must Change for Self-Service

### HONK-154: Hardcoded Sponsor IDs (Completed)

Nick Cruess documented all instances of sponsor-related hardcoding:
- XID hardcoding in code
- Galileo PRN hardcoding
- FIS subprogram ID hardcoding

These are mostly lookup tables -- they need to become configurable.

### Lower-Touch Implementation Gaps (2025-04-04)

**Covered by existing checklist:**
- Benthos stream configuration
- Returns configuration

**Covered by HONK-154 (hardcodes to remove):**
- Hub Dashboard configuration

**NOT YET COVERED:**
- Custom approval profile creation
- Test file generation
- Promote Benefits Config (stage -> production)
- Promote Content Config (stage -> production)

### Data Model Gaps

For self-service, the sponsor domain needs:
1. **Onboarding status tracking** -- Where is this sponsor in the setup flow?
2. **Customer-visible config** -- Which config fields are customer-editable vs internal?
3. **Validation rules** -- What are the valid ranges/values for each config field?
4. **Default templates** -- Starter configs for common sponsor types (supplemental benefits, etc.)
5. **Approval workflow** -- Who approves sponsor config changes before they go live?

---

## Demo Scope (Kestrel Phase 1 Slice)

The AI demo focuses on the **sponsor creation** feature -- the most impactful
and self-contained piece:

**In scope:**
- New customer-facing API endpoints for sponsor creation
- Guided multi-step flow: create customer -> create brand -> configure -> add benefits
- Validation and defaults for common config patterns
- Basic authorization (new Casbin role for customer admins)

**Out of scope (Phase 1):**
- FIS/Galileo funding account automation (requires external API calls)
- Eligibility file processing
- Benthos configuration
- Frontend UI (API-only for demo)
- Iterable/Vonage setup
- Staging -> production promotion

---

## Key Data Sources

| Source | What It Provides |
|--------|-----------------|
| **Harmony code** | Current sponsor API, config structure, benefit types, DB schema |
| **"How to create a sponsor"** | Complete manual process (what to automate) |
| **Lower-Touch Implementations** | Gap analysis (what's not yet covered) |
| **HONK-154** | Hardcoded IDs to make configurable |
| **Kestrel PRFAQ** | Product vision and customer-facing features |
| **Osprey data** | 2,229 real implementation tasks across 27 customers (ground truth for what Kestrel automates) |
| **Explainer PDFs** | Customer-facing semantics for benefits, approval profiles, funding |
