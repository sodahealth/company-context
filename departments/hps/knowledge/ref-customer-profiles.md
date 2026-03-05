---
title: "Customer Profiles"
summary: "Master reference for all health plan sponsor customers -- brands, shortcodes, product mix, care models, and configuration traits"
topics: [customers, health-plans, brands, products, benefits, rewards, surveys, implementation]
systems: [Harmony, OnRamp, Strapi, Iterable]
people: [Tal Topf, Diane Borton, Megan Guillory, Ariane Grazian]
content_type: reference
departments: [hps]
roles: [all]
classification: internal
last_verified: "2026-03-05"
review_cycle_days: 90
---

# Customer Profiles

Master reference for all health plan sponsor customers. Covers implementation phase, brands, shortcodes, product mix, care model, survey/rewards configuration, digital content customizations, and brand-specific traits.

**Source:** "Customer Profiles.xlsx" (SharePoint: SodaHealthInternal/Internal Docs/Customer Solutions/CSOT/)

## New Implementations (2026)

| Customer | Shortcode | Brand(s) | Brand Shortcode(s) | Launch Date | IM | Secondary |
|----------|-----------|----------|--------------------|-----------|----|-----------|
| Blackhawk | BHWK | Blackhawk Network | BHN | 3/6/2026 | Megan Guillory | Ari |
| Sentara | SEN | Sentara | SHN | 3/27/2026 | Megan Guillory | Ari |
| Health Plan of San Joaquin Medi-Cal | HSJ | HSJMC | HSJMC | 4/20/2026 | Megan Guillory | Tal |
| Regal Med | -- | -- | -- | -- | -- | -- |
| Prominence | -- | PMN Rewards Only | -- | -- | -- | -- |

### Account Managers

- Blackhawk: Genesis Coste
- Sentara: TBD
- HSJMC: Kaity Galanos

### Care Support Model

- Blackhawk: Option 2 (Soda on first) -- "Other" client type
- Sentara: IVR Only -- Pilot-to-Scale
- HSJMC: Option 2 (Soda on first) -- Off Cycle Medicaid

## Product Mix by Customer

| Customer | Supp Benefits | Other Benefits | Rewards Standalone | Rewards Add-On | Reimbursement | Self-Attest | Gap Closure (Surveys) | Gap Closure (HRA+SSBCI) | Gap Closure (Pharmacy) |
|----------|--------------|---------------|-------------------|---------------|--------------|-------------|----------------------|------------------------|----------------------|
| Blackhawk | n/a | n/a | Yes | n/a | n/a | n/a | n/a | -- | -- |
| Sentara | Utilities | n/a | n/a | n/a | n/a | n/a | n/a | -- | -- |
| HSJMC | -- | -- | Yes (Non-ATFLGC) | -- | -- | -- | -- | -- | -- |

## Bank and Diligence Status

| Customer | Bank | Diligence Status | Notes |
|----------|------|-----------------|-------|
| Blackhawk | Avidia | In Progress | Materials in-hand ready for compliance review. Working on compliant funds flow model. |
| Sentara | Avidia | In Progress | Materials received. Memo in progress. |
| HSJMC | Avidia | -- | -- |

## Per-Customer Operational Highlights

### SCAN Health Plan (SCN)

- **Brands**: SCNWA (Washington), SCNCA (California -- R&I only, launched ~1/5/26)
- **Key issues**: Eligibility file address mapping, SFTP encryption/naming, material carrier reprints, multi-language IVR (Chinese priority)
- **IM**: Diane Borton
- **AM**: Kaity Galanos
- **Strategic importance**: Critical for 2027 scaling; multi-language support key to deepening partnership

### SummaCare (SMC)

- **Products**: OTC, Vision, Rewards (Healthy Home, Annual Wellness, Colorectal, Mammogram)
- **Service area**: Ohio; ~30,000 projected cards
- **Key issues**: Eligibility file support, funding account confusion, card timing vs. call center readiness
- **IM**: Diane Borton
- **AM**: Genesis Coste
- **Super purse** with Acupuncture, Chiro, and Naturopathy benefit (MCC + Fuzzy Matching)
- **Rewards and self-attestation**

### San Francisco Health Plan (SFHP/SFOCA)

- **Products**: OTC (all beneficiaries), SSBCI-qualified Food/Produce, Rent/Utilities (with reimbursement)
- **Key issues**: 834 format not supported (deferred to 2027), rent reimbursement process, 75-day state/compliance review
- **IM**: Megan Guillory

### Contra Costa Health Plan (CTC/CCHP)

- **Products**: OTC Base + SSBCI expanding grocery; $25 total budget; Medicare; Care Option 2
- **Key issues**: Albertsons-exclusive retail network (MX-driven restriction only), contracting delays (county government), narrow network AP swap caught late
- **Membership**: ~800 members
- **Tri-party relationship**: Evermore + Albertsons + CCHP

### Imperial Health Plan (IHP/IHPC)

- **Renewal customer** (not new 2026 implementation)
- **Key issues**: Proration dispute, employee program re-carding during Bancorp wind-down, catalog overages invoicing
- **IM**: Megan Guillory
- **AM**: Rachel McMillan

### Prominence (PMN) -- Complex Multi-Brand

Three brand groups with different product mixes:

**Brand group 1: PMNTX + PMNFL (OTC + Rewards)**
- 12 TX programs + 4 FL programs (excluding H7680-012 and H7239-004)
- Narrow network (no CVS, Medline for online/phone OTC, Walgreens for in-store)
- OTC Base+, Healthy Foods Base+, Utilities (MCC-based), Rewards (Non-ATFLGC)

**Brand group 2: PMNTX + PMNFL + PMNNV (PHRE package -- Rewards only)**
- 3 specific programs across TX, FL, NV
- No OTC, no catalog -- rewards self-attestation only

**Brand group 3: PMNNV (OTC + Rewards)**
- 8 NV programs
- Medline Catalog only for OTC, no CVS

### Other Active Customers

- **Braven Health / Horizon (BHZ)**: B7U/B7W member ID fix, SLA report accuracy, grace period handling. Extra $25 incentive for AWV, BCS, COL screening by 6/30/26.
- **Central California Alliance (CCAH)**: ~500 members, D-SNP. Circuit breaker on eligibility files, address line concatenation issues.
- **Sharp Health Plan (SHP)**: OTC only (not doing R&I in 2027). IVR disconnecting calls.
- **NHPRI**: EDI encounter files (80-byte format), funding tracking ($3.7M balance, $32.5K/day).
- **Gold Kidney (GKI)**: Rollover file processing, healthy foods postcard co-branding.
- **Atrio (ATR)**: Icario vendor integration (daily SFTP rewards file), IVR routing issues. Transaction SMS only, emails 1/2/5 only.
- **HPSJ (SJQ)**: Medi-Cal rewards delegation, API spec for mid-April go-live.
- **AmeriHealth (ACVC)**: 30,000 enrollment. 2025 rewards rollover to 2026 utility reimbursement.

## Surveys and Rewards Configuration

### Survey Overview by Customer

| Customer | Survey Type | Reward Trigger | All Members Eligible? | Agent Can Complete? |
|----------|------------|---------------|----------------------|---------------------|
| Prominence | HRA | Yes (also via elig file) | No (C-SNP/D-SNP only) | No |
| Atrio | Rewards Self-Attestation | Yes (only way to earn) | Yes | Yes |
| SCAN California | Rewards Self-Attestation | Yes (some also via elig file) | No (varies by survey) | Yes |
| BHZ | Rewards Self-Attestation | Yes (some also via elig file) | Yes | Yes |

### BHZ Nuances

- All rewards are self-attest only, except In Home Assessment (received via file)
- Additional reward dollars for certain activities if completed in specific timeframe
- Attestation for BCS/COL and AWV should be completed by 07/31/26

## Brand Traits Legend

| # | Trait | Description |
|---|-------|-------------|
| 1 | Narrow network | Specific retailer restrictions (e.g., no CVS, catalog-only, specific retailer promotion) |
| 2 | Benefit mix | Non-standard product combination (e.g., no OTC, rewards only, no catalog) |
| 3 | AP (Approval Profile) | Approval profile customization (MCC-only vs. store-level) |
| 4 | Regional relevance | Experience should reflect regional retailer/service availability |
| 5 | Unenrolled members | Customer may send unenrolled members in eligibility file |
| 6 | Reinstated members | Reinstatement flow is enabled |
| 7 | Customer Customization Request | Customer has specific content/flow requirements beyond standard |

## Digital Content Customization Patterns

Key patterns that affect OX, Email, and SMS configuration across customers:

- **Disclaimer variations**: Some customers have email-only disclaimers different from OnRamp. Must be tracked per brand and per channel.
- **Email approval**: Some customers only approve specific onboarding emails (e.g., Atrio approved only 1, 2, 5).
- **SMS opt-in**: Some customers start with transaction SMS only, may expand mid-year.
- **Survey completion by agents**: Varies by customer -- must be configured per brand.
- **Rewards-only brands**: Some brands get no catalog, no OTC benefit -- only rewards self-attestation. Requires different OX content and email templates.
- **Narrow network**: Retailer restrictions drive different shopping method copy, catalog content, and benefit flavor descriptions.

## Implementation Milestones -- Cohort Timeline

Implementations are organized into three cohorts representing staggered launch waves. Key milestone owners:

- **HPS**: Kick-off, program requirements, benefit config, eligibility testing, reporting
- **M&P (Marketing and Print)**: Due diligence, approval profiles, fund transfer
- **MX (Member Experience)**: Package IDs, digital materials, materials forecasts, card vendor UAT
- **IT/CS**: Tool access and training
- **Care**: Member forecast for care, call center readiness
- **Legal**: Contracting
- **Engineering**: Volume testing

Critical dates typically follow this pattern:
- Kick-off: June-August (varies by cohort)
- Benefit Configuration Complete: September 30
- Eligibility File Testing: September 1
- File and Benefit Testing Complete: November 1
- First Eligibility File: November 1-10
- Cards Mailed to Members: November 17
- Call Center Takes First Call: December 1
- Last Cards in Mail for 1/1 Delivery: December 12
