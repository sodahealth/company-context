---
title: "Kestrel Discovery Session: Benefits"
summary: "Transcript summary from Kestrel requirements scoring session -- cross-team prioritization of self-service benefit configuration features"
topics: [kestrel, discovery, requirements, prioritization, benefits, ebt, hpms, pbp]
systems: [Harmony, Kestrel, HPMS]
people: [Seth Townsend, Ariane Grazian, Tal Topf, Megan Guillory, Charley Shamaly, Laura de Crescenzo, Peter Barkey-Bircann]
content_type: reference
departments: [engineering]
roles: [all]
classification: internal
last_verified: "2026-03-18"
review_cycle_days: 90
---

# Kestrel Discovery Session: Benefits | Customer Solutions

**Date:** 2026-02-20
**Source:** Granola transcript
**Participants:** Seth Townsend, Ariane Grazian, Tal Topf, Megan Guillory, Charley
Shamaly, Laura de Crescenzo (LDC), Peter Barkey-Bircann, Jaden Wright, Desiree
NeuPhresh, Patrice James

**Format:** Silent reading of 11 requirements -> discussion -> silent voting/scoring
**Tool:** Likely TeamRetro or Miro (numbered rows with scoring)

---

## Key Takeaway

Engineering is still in **discovery and prioritization** -- not building. This
session was about scoring which Kestrel requirements matter most. No estimates,
no sprint assignments, no architecture decisions. They're voting on what to
build first.

---

## Requirements Discussed (by row number)

### Row 11: Self-Service Benefit Configuration (Generic)
- **Scope:** Any program type (MA, EBT, Medicaid, commercial)
- **User:** Customer OR internal -- "anyone who has access to set up a program"
- **Consensus:** High priority, foundational
- **Key quote:** "You can set up any benefit program you want"
- **Voted high across all teams**

### Row 14: Auto-Generate Mirror Extension + Return Benefits
- **What it does:** When you create a primary OTC benefit, extension and return
  benefits auto-generate with inherited config (same AP, etc.)
- **Internal-only automation** -- customer doesn't see this, can't override
- **Reduces manual config time**
- **Returns pain point (Tal):** "The most painful thing was the APs -- figuring
  out the sum of all their APs was not clear between rewards, narrow networks, etc."
- **Seth and Tal spent an hour together asking "what actually is the sum of all their APs?"**
- **Engineering voted this lower** (Charley: "it's got a solution at the moment, just doesn't scale well")

### Row 15: Workflow / Approval / Sign-off + Testing
- **Includes:** Adding additional approvers, sign-off workflow
- **Key addition from discussion:** Customers should see **OX (Online Experience)
  preview** of their benefit config as members would see it, THEN sign off
- **Quote (LDC):** "There's a way to see what you're configuring and make sure
  you understand all the impacts, then sign up for it"
- **BHC tile example:** "Until they saw it in OX, they maybe would have changed
  their filing or their grid once they saw how it was actually working"
- **This is experiential checking** -- not just data review

### Row 16: HPMS PBP Import (MA-Specific)
- **What:** Import from CMS Health Plan Management System instead of creating
  benefit grid manually
- **MA-exclusive** -- "very, very exclusive to MA" (Seth)
- **Tied to Row 11** but dedicated/specialized
- **Key exchange:**
  - Ariane: "Can they do this as soon as bid day [June 2nd]? Even if not final?"
  - Answer: Yes, anytime after bid submission
  - LDC: "Rather than creating the benefit grid and translating all their benefits,
    they just import the same stuff they uploaded to HPMS -- reduces error risk"
- **Confirmed as the approach we're building**

### Row 17: EBT-Specific Benefit Configuration
- **Product + engineering ranked much higher** than other teams
- **LDC caution:** "We'll have 1-2 EBT clients, still learning. Cart before horse."
- **Peter's counter:** "EBT will get complex very soon. Amount of requirements
  building gives me confidence. If we don't solve it, messy implementation in
  old ways -- same problem as this past 1:1."
- **Lower consensus** -- MA is hardened, EBT is emerging

### Row 19: CMS Proposed Rule Impact
- **LDC:** "Nothing that would bother us. Big commentary about returns but no way
  to fix it. Hoping it's a non-event this year."
- **Hard to vote on** -- regulatory uncertainty

### Row 21: Customer/AMs Self-Service Benefit Extensions
- **Care team ranked higher** (tickets get submitted, delays)
- **Josie's team:** Just processed 200 benefit extension tickets
- **Desiree/Patrice:** "Would alleviate delay we've seen"

### Benefit Testing
- **Question raised:** "Is the user us or the customer?"
- **Discussion deferred** -- impacts scoring

### Survey Configurations
- **LDC acknowledged:** "Very, very, very time consuming for a person"
- **But voted lower because:** "Not everyone we sell will have surveys. Everyone
  will have benefits."
- **Higher risk items prioritized** over time-consuming-but-lower-risk items

---

## Scoring Patterns

**Voted highest (cross-team consensus):**
- Row 11: Self-service benefit config (generic)
- Row 16: HPMS PBP import (MA-specific)
- Row 15: Workflow/approval/sign-off + preview

**Voted higher by specific teams:**
- Row 17: EBT config (Product + Engineering higher, others cautious)
- Row 21: Self-service extensions (Care higher, Engineering lower)

**Voted lower:**
- Row 14: Auto-generate extension/return benefits (Engineering: "has a solution")
- Survey config (important but not highest risk)

**Voting principle (LDC):** "I voted for things highest risk for error from
customer input" -- prioritizing correctness over time savings.

---

## Key Decisions Clarified

1. **Grace period and disenrollment** are NOT part of benefit config -- they're
   eligibility processing behaviors. "Should be a behavior we can augment or
   automate in eligibility processing."

2. **Auto-generate extension/return benefits** is internal-only automation.
   Customer doesn't interact with it.

3. **PBP Import timing:** Can happen as soon as bid day (June 2), even before
   final approval. Health plans use HPMS (Health Plan Management System) to
   submit to CMS.

4. **Row 11 is generic, Row 16 is MA-specific.** Both are needed. Row 16 is
   the fast path for MA clients specifically.

5. **Preview/experiential checking** is part of the approval workflow (Row 15),
   not a separate feature. Customers need to see benefits as members would.

---

## Implications for Our Demo

1. **We're building exactly what they voted highest:** Self-service benefit config
   (Row 11) + HPMS PBP import (Row 16) + approval workflow (Row 15)

2. **The approval/preview gap** is something we should address in the wizard --
   Step 10 (Review & Submit) should include a member experience preview

3. **The AP complexity** is a real pain point -- Tal and Seth spent an hour figuring
   out "the sum of all their APs." Our AP catalog (31 profiles) and the mapping
   from Osprey data directly addresses this

4. **200 benefit extension tickets** is a concrete pain metric for the demo narrative

5. **This discovery session was 2 days ago.** They're still voting on priorities.
   We already have a working wireframe.
