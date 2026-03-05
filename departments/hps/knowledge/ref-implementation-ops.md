---
title: "Implementation Operations"
summary: "Operational patterns, recurring issues, and cross-cutting themes from health plan implementations"
topics: [implementation, operations, eligibility, benefits, materials, care, sftp, reporting]
systems: [Harmony, OnRamp, Strapi, Iterable, FIS, SFTP]
people: [Tal Topf, Diane Borton, Megan Guillory, Ariane Grazian, Seth Townsend]
content_type: reference
departments: [hps]
roles: [all]
classification: internal
last_verified: "2026-03-05"
review_cycle_days: 90
---

# Implementation Operations

This document captures the operational patterns, recurring issues, and lessons learned from health plan implementations during the 2025-2026 cycle. It is drawn from internal Slack discussions across `#sponsor-implementations`, `#implementation-2dot0`, `#sales-and-implementation`, and customer-specific channels.

## Key Internal Channels

| Channel | Purpose | Key People |
|---------|---------|------------|
| `#sponsor-implementations` | Central coordination for all implementations -- weekly meetings, risk logs, cross-customer status | Tal Topf, Ariane Grazian, Diane Borton |
| `#implementation-2dot0` | Implementation automation and process improvement (OnRamp, Zapier, Harmony) | Seth Townsend, Mac Murphy, Umang Kapadia, Tal Topf |
| `#sales-and-implementation` | Customer Implementation Profile intake (Slack workflow) | Becca Cesario |
| `#internal-<customer>` | Per-customer ops, issues, and implementation tracking | Varies by customer |

## Cross-Cutting Operational Patterns

### Eligibility File Processing

Eligibility file processing is one of the most common sources of issues during implementation.

- **Address field logic**: Multiple customers need mailing-to-primary address fallback logic; benthos update required per customer (SCAN, SFHP)
- **834 EDI not supported**: Evermore only accepts CSV/PDL formats; SFHP requested EDI format which was deferred to 2027
- **Circuit breaker triggers**: CCAH experienced processing issues with address line concatenation
- **File hold/pause coordination**: When material reprints happen, eligibility files must be paused to avoid sending cards with old carriers
- **Timing issues**: Partially-added member data can show up incomplete until a later processing run

### Eligibility File Mapping and Testing

- **SFTP access setup** is gated on contract execution -- credentials are not issued before the contract is signed
- **Data mapping** is the customer's responsibility but often needs hands-on support from the IM
- **Testing sign-off**: Formal sign-off should be documented in OnRamp, not just verbally confirmed
- **Auto-run configuration**: Files drop to the "sponsor files" folder; auto-run can be toggled per brand

### Funding and Banking

- **Funding account explainers**: Customers are often confused about the funding process -- it is not a payment for services and does not trigger a 1099
- **Funds-before-cards policy**: Funds must be in the account before the first card send; not always documented in SOW
- **KYC/UBO complexity**: Government entities have complex beneficial ownership structures; bank diligence can be slow
- **Daily burn tracking**: Tracked for customers with large balances (e.g., NHPRI at ~$32.5K/day)

### Materials and Physical Card Operations

- **Card send timing vs. call center readiness**: Cards must not arrive before the call center is live; IVR covers with a message during the gap period
- **Carrier reprints**: When carrier materials need updating, files must be paused, ABCorp notified, and kits reconfigured
- **Catalog retailer branding**: Standard catalog contains multiple retailer brands; exclusive deals can cause branding conflicts
- **Large print catalogs**: Must be flagged during the MX session
- **Material reorder invoicing**: Additional orders beyond the initial set are billed at the replacement rate in the SOW

### Narrow Network and Retailer Restrictions

- **MX-driven restriction**: The technical backend cannot exclude merchants from approval profiles; restriction is enforced through member experience (materials, app, OX copy)
- **Customer-specific examples**:
  - CTC/Albertsons: Requested Safeway-only network; handled via materials directing to Safeway only
  - PMN: No CVS for any benefits/rewards; Medline catalog-only for some brands
- **Smartsheet AP dashboard**: Narrow network approval profiles must be swapped in on benefits before go-live

### Rewards and Self-Attestation

- **Agent survey completion**: Varies by customer -- must be configured per brand
- **Claims-based vs. self-attest**: Most rewards are self-attest; some also have claims-based rewards via file
- **Reward expiry**: Must confirm with customer whether rewards expire at end of plan year or on disenrollment
- **Incentive bonuses**: Some customers offer extra incentives for specific screenings completed by a deadline

### Care and IVR Operations

- **IVR routing gaps**: Routing configurations should be managed in a proper system, not a transfer sheet
- **Warm transfer protocol**: Standardized globally -- agents hold up to 2 minutes, then offer options
- **Complaint handling**: Varies by customer -- some want agents to resolve on call, others use a complaint log
- **Multi-language IVR**: Chinese, Korean, and Vietnamese are priorities; some plans have significant non-English-speaking populations
- **Call center training**: Customers want script review, proper pronunciation, and KB articles before go-live

### Contracting and SOW Challenges

- **Government entities**: County government processes can significantly slow contracting
- **SOW implementation timeline**: Often the last piece to finalize; implementation can start before contract is fully signed
- **Pricing clarity**: Billing rates for additional materials orders are not always well documented in SOW
- **834 language**: Some SOWs committed to EDI formats that were not feasible; required hybrid language deferring to a future year

### Digital Content and Communications

- **Email approval**: Some customers only approve specific onboarding emails
- **SMS**: Some start transaction-only, may expand mid-year
- **OX/Strapi content**: Must match physical materials; some benefits need specific shopping methods noted
- **Disclaimer variations**: Differ by channel (email vs. OX vs. print) and by customer

### SFTP and Reporting

- **PGP encryption**: Some customers require PGP encryption on outbound reports
- **File naming conventions**: Customers may want date-stamped names that differ from the standard naming
- **SFTP hosting direction**: A roadmap item exists for configurable customer-hosted SFTP
- **EDR reports**: Folder structures must match customer expectations

### Renewals vs. New Implementations

- **OnRamp module gap for renewals**: MX team already has branding and materials from prior year; the module should pre-load past materials
- **Customer memory issues**: Customers may not remember their own decisions from the prior year -- require written approvals in OnRamp
- **Re-carding**: Year-over-year transitions may involve re-carding and higher replacement card volume

## Lessons Learned

1. **Paper trail for customer decisions**: Require written approval clicks in OnRamp, not just verbal confirmation
2. **Funding explainer gaps**: SOW should always clarify that funds must be in account before card send
3. **Material reorder billing**: Replacement rate billing should be communicated clearly upfront
4. **Renewal module**: OnRamp should pre-load prior year materials for returning customers
5. **Narrow network AP timing**: Approval profiles must be swapped before go-live -- add as a checklist item
6. **SFTP file naming**: Configurable naming is needed to meet customer automation requirements
7. **Multi-language priority**: Chinese, Korean, Vietnamese in order; SCAN, CalOptima, SFHP are key customers
8. **IVR routing source of truth**: Needs proper configuration management, not a transfer sheet
9. **Implementation feedback surveys**: Customer feedback (like SCAN's pilot) produces concrete product improvement ideas
10. **Post-implementation after-action reports**: Should become standard practice for all implementations
