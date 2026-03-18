---
title: "Data Model: Merchant"
summary: "Schema reference for the merchant database -- merchant catalog, product hierarchy, and approval profiles (spending restriction rules engine)"
topics: [data-model, merchant, approval-profiles, catalog, mcc, items, categories]
systems: [Harmony, Cloud SQL, PostgreSQL]
people: []
content_type: reference
departments: [engineering]
roles: [all]
classification: internal
last_verified: "2026-03-18"
review_cycle_days: 90
---

# Data Model: merchant

**Database:** merchant
**Migrations:** 156
**Tables:** ~32

The merchant database manages the merchant catalog, product hierarchy,
and approval profiles (spending restriction rules).

---

## Core Merchant

### merchant
| Column | Type | Notes |
|--------|------|-------|
| id | bytea (XID) | |
| name | varchar | |
| aggregate_merchant_identifier | int | |
| preauth_expiration_duration_seconds | int | |
| config | jsonb | Flexible configuration |
| integration_type | enum (direct, fis) | How we connect |
| integration_live_at | timestamp | |

### merchant_category_codes
MCC codes (integer PK) with name and description. Standard industry codes for merchant classification.

### merchant_group / merchant_merchant_group
Groupings of merchants for approval profile rules.

---

## Product Hierarchy

```
core_category
  +-- fineline (sub-category)
       +-- item -> item_details (metadata, nutrition, attributes)
```

- **core_category** -- Top-level product category
- **fineline** -- Sub-category under core_category
- **item** -- Individual product/item
- **item_details** -- Metadata, nutrition info, attributes
- **item_core_category** -- M2M for cross-categorization

---

## Approval Profiles (Business Rules Engine)

The approval profile system defines what members can spend on. It's the core
business rules engine for benefit restrictions.

### approval_profiles
| Column | Type | Notes |
|--------|------|-------|
| restrictiveness | enum | general, targeted, specific |

### Linked rules (what's approved)
| Table | What it controls |
|-------|-----------------|
| **approval_profiles_merchants** | Whitelist/blacklist merchants |
| **approval_profiles_merchant_groups** | Approved merchant groups |
| **approval_profiles_merchant_category_codes** | Approved MCCs |
| **approval_profiles_core_categories** | Approved product categories |
| **approval_profiles_shopping_categories** | Approved shopping categories |
| **approval_profile_item** | Item-level rules |
| **merchant_matching_profile** | Merchant matching rules |

---

## Location & Geo

- **location** -- Lat/long with geocoding_indicator_type (ADMIN, BLOCK, ROOFTOP, STOREFRONT, etc.)
- **mc_merchant_identifier** / **mc_merchant_location** / **mc_aggregate_merchant** -- MasterCard merchant mappings

---

## Network Matching

- **merchant_item** / **merchant_item_core_category** -- Links merchants to items and categories
- **merchant_core_category_matchers** -- String matching rules for categorization (strict, regex, prefix)

---

## Key Patterns

1. **Hierarchical product classification** -- core_category -> fineline -> item
2. **Approval profiles as rules engine** -- Restrict spending by category, merchant, MCC, or item
3. **Three restrictiveness levels** -- general (broad), targeted (category-level), specific (item-level)
4. **Multiple matching strategies** -- strict, regex, prefix for merchant/item assignment
5. **GS1 standard integration** -- segment, family, class, brick hierarchy
6. **Geocoding** -- Multiple precision levels for merchant location
