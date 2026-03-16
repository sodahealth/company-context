---
title: BigQuery Schema Reference
description: Complete schema metadata for all datasets and tables in soda-health-production BigQuery project. Use this to write accurate SQL queries.
classification: internal
departments: [all]
last_verified: "2026-03-16"
review_cycle_days: 90
---

# BigQuery Schema Reference — soda-health-production

Auto-generated on 2026-03-16. Metadata only — no PHI/PII data.

## Dataset: `cpg_analysis`

### `cpg_analysis.CPG_OTC_SIF_Transactions`

```json
[
    {
        "name": "member_id",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "transaction_id",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "merchant_id",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "merchant_name",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "merchant_name_rollup",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "harmony_customer_id",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "harmony_customer_name",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "harmony_brand_sponsor_id",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "harmony_brand_sponsor_name",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "date",
        "type": "DATE",
        "mode": "NULLABLE"
    },
    {
        "name": "time",
        "type": "TIMESTAMP",
        "mode": "NULLABLE"
    },
    {
        "name": "item_code",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "item_code_type",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "item_desc",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "item_desc_source",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "manufacturer",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "brand",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "L1",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "L2",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "L3",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "L4",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "L5",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "L1_name",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "L2_name",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "L3_name",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "L4_name",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "L5_name",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "units",
        "type": "FLOAT",
        "mode": "NULLABLE"
    },
    {
        "name": "amt_requested",
        "type": "FLOAT",
        "mode": "NULLABLE"
    },
    {
        "name": "rn",
        "type": "INTEGER",
        "mode": "NULLABLE"
    }
]
```

### `cpg_analysis.KenvueCategories`

```json
[
    {
        "name": "Category",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "Kenvue_Brand",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "Item_Info",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "UPC",
        "type": "INTEGER",
        "mode": "NULLABLE"
    },
    {
        "name": "Description",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "Size",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "GTIN",
        "type": "INTEGER",
        "mode": "NULLABLE"
    }
]
```

### `cpg_analysis.all_purchase_attempts`

```json
[
    {
        "name": "member_id",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "transaction_id",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "transaction_state",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "merchant_id",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "merchant_name",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "merchant_name_rollup",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "basket_source",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "data_source",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "harmony_customer_id",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "harmony_customer_name",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "harmony_brand_sponsor_id",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "harmony_brand_sponsor_name",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "date",
        "type": "DATE",
        "mode": "NULLABLE"
    },
    {
        "name": "time",
        "type": "TIMESTAMP",
        "mode": "NULLABLE"
    },
    {
        "name": "item_code",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "item_code_type",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "item_desc",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "item_desc_source",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "manufacturer",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "brand",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "categories",
        "type": "RECORD",
        "mode": "REPEATED",
        "fields": [
            {
                "name": "L1",
                "type": "STRING",
                "mode": "NULLABLE"
            },
            {
                "name": "L2",
                "type": "STRING",
                "mode": "NULLABLE"
            },
            {
                "name": "L3",
                "type": "STRING",
                "mode": "NULLABLE"
            },
            {
                "name": "L4",
                "type": "STRING",
                "mode": "NULLABLE"
            },
            {
                "name": "L5",
                "type": "STRING",
                "mode": "NULLABLE"
            },
            {
                "name": "L1_name",
                "type": "STRING",
                "mode": "NULLABLE"
            },
            {
                "name": "L2_name",
                "type": "STRING",
                "mode": "NULLABLE"
            },
            {
                "name": "L3_name",
                "type": "STRING",
                "mode": "NULLABLE"
            },
            {
                "name": "L4_name",
                "type": "STRING",
                "mode": "NULLABLE"
            },
            {
                "name": "L5_name",
                "type": "STRING",
                "mode": "NULLABLE"
            }
        ]
    },
    {
        "name": "units",
        "type": "FLOAT",
        "mode": "NULLABLE"
    },
    {
        "name": "amt_requested",
        "type": "FLOAT",
        "mode": "NULLABLE"
    }
]
```

### `cpg_analysis.brandinfo`

```json
[
    {
        "name": "category",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "segment",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "brand",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "item",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "item_code",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "unknown",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "unknown2",
        "type": "STRING",
        "mode": "NULLABLE"
    }
]
```

### `cpg_analysis.cpg-KenvueUPCs-withMedline-NOSIFS`

```json
[
    {
        "name": "member_id",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "transaction_id",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "merchant_id",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "merchant_name",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "merchant_name_rollup",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "harmony_customer_id",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "harmony_customer_name",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "harmony_brand_sponsor_id",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "harmony_brand_sponsor_name",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "date",
        "type": "DATE",
        "mode": "NULLABLE"
    },
    {
        "name": "time",
        "type": "TIMESTAMP",
        "mode": "NULLABLE"
    },
    {
        "name": "item_code",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "item_code_type",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "item_desc",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "item_desc_source",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "manufacturer",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "brand",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "units",
        "type": "FLOAT",
        "mode": "NULLABLE"
    },
    {
        "name": "amt_requested",
        "type": "FLOAT",
        "mode": "NULLABLE"
    }
]
```

### `cpg_analysis.cpg-topical-pain-12-9`

```json
[
    {
        "name": "member_id",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "transaction_id",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "merchant_id",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "merchant_name",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "merchant_name_rollup",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "harmony_customer_id",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "harmony_customer_name",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "harmony_brand_sponsor_id",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "harmony_brand_sponsor_name",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "date",
        "type": "DATE",
        "mode": "NULLABLE"
    },
    {
        "name": "time",
        "type": "TIMESTAMP",
        "mode": "NULLABLE"
    },
    {
        "name": "item_code",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "item_code_type",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "item_desc",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "item_desc_source",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "manufacturer",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "brand",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "units",
        "type": "FLOAT",
        "mode": "NULLABLE"
    },
    {
        "name": "amt_requested",
        "type": "FLOAT",
        "mode": "NULLABLE"
    },
    {
        "name": "pf_digits",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "brand_1",
        "type": "STRING",
        "mode": "NULLABLE"
    }
]
```

### `cpg_analysis.kenvue_categories_3-16`

```json
[
    {
        "name": "Category",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "Kenvue_Brand",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "Item_Info",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "UPC",
        "type": "INTEGER",
        "mode": "NULLABLE"
    },
    {
        "name": "Description",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "Size",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "member_id",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "transaction_id",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "merchant_id",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "merchant_name",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "merchant_name_rollup",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "harmony_customer_id",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "harmony_customer_name",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "harmony_brand_sponsor_id",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "harmony_brand_sponsor_name",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "date",
        "type": "DATE",
        "mode": "NULLABLE"
    },
    {
        "name": "time",
        "type": "TIMESTAMP",
        "mode": "NULLABLE"
    },
    {
        "name": "item_code",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "item_code_type",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "item_desc",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "item_desc_source",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "manufacturer",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "brand",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "units",
        "type": "FLOAT",
        "mode": "NULLABLE"
    },
    {
        "name": "amt_requested",
        "type": "FLOAT",
        "mode": "NULLABLE"
    }
]
```

### `cpg_analysis.purchase_attempts`

```json
[
    {
        "name": "member_id",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "transaction_id",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "transaction_state",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "merchant_id",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "merchant_name",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "merchant_name_rollup",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "basket_source",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "harmony_customer_id",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "harmony_customer_name",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "harmony_brand_sponsor_id",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "harmony_brand_sponsor_name",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "date",
        "type": "DATE",
        "mode": "NULLABLE"
    },
    {
        "name": "time",
        "type": "TIMESTAMP",
        "mode": "NULLABLE"
    },
    {
        "name": "item_code",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "item_code_type",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "item_desc",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "item_desc_source",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "manufacturer",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "brand",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "categories",
        "type": "RECORD",
        "mode": "REPEATED",
        "fields": [
            {
                "name": "L1",
                "type": "STRING",
                "mode": "NULLABLE"
            },
            {
                "name": "L2",
                "type": "STRING",
                "mode": "NULLABLE"
            },
            {
                "name": "L3",
                "type": "STRING",
                "mode": "NULLABLE"
            },
            {
                "name": "L4",
                "type": "STRING",
                "mode": "NULLABLE"
            },
            {
                "name": "L5",
                "type": "STRING",
                "mode": "NULLABLE"
            },
            {
                "name": "L1_name",
                "type": "STRING",
                "mode": "NULLABLE"
            },
            {
                "name": "L2_name",
                "type": "STRING",
                "mode": "NULLABLE"
            },
            {
                "name": "L3_name",
                "type": "STRING",
                "mode": "NULLABLE"
            },
            {
                "name": "L4_name",
                "type": "STRING",
                "mode": "NULLABLE"
            },
            {
                "name": "L5_name",
                "type": "STRING",
                "mode": "NULLABLE"
            }
        ]
    },
    {
        "name": "units",
        "type": "FLOAT",
        "mode": "NULLABLE"
    },
    {
        "name": "amt_requested",
        "type": "FLOAT",
        "mode": "NULLABLE"
    }
]
```

### `cpg_analysis.purchase_attempts_settled`

```json
[
    {
        "name": "member_id",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "transaction_id",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "transaction_state",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "merchant_id",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "merchant_name",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "merchant_name_rollup",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "basket_source",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "harmony_customer_id",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "harmony_customer_name",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "harmony_brand_sponsor_id",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "harmony_brand_sponsor_name",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "date",
        "type": "DATE",
        "mode": "NULLABLE"
    },
    {
        "name": "time",
        "type": "TIMESTAMP",
        "mode": "NULLABLE"
    },
    {
        "name": "item_code",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "item_code_type",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "item_desc",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "item_desc_source",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "manufacturer",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "brand",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "categories",
        "type": "RECORD",
        "mode": "REPEATED",
        "fields": [
            {
                "name": "L1",
                "type": "STRING",
                "mode": "NULLABLE"
            },
            {
                "name": "L2",
                "type": "STRING",
                "mode": "NULLABLE"
            },
            {
                "name": "L3",
                "type": "STRING",
                "mode": "NULLABLE"
            },
            {
                "name": "L4",
                "type": "STRING",
                "mode": "NULLABLE"
            },
            {
                "name": "L5",
                "type": "STRING",
                "mode": "NULLABLE"
            },
            {
                "name": "L1_name",
                "type": "STRING",
                "mode": "NULLABLE"
            },
            {
                "name": "L2_name",
                "type": "STRING",
                "mode": "NULLABLE"
            },
            {
                "name": "L3_name",
                "type": "STRING",
                "mode": "NULLABLE"
            },
            {
                "name": "L4_name",
                "type": "STRING",
                "mode": "NULLABLE"
            },
            {
                "name": "L5_name",
                "type": "STRING",
                "mode": "NULLABLE"
            }
        ]
    },
    {
        "name": "units",
        "type": "FLOAT",
        "mode": "NULLABLE"
    },
    {
        "name": "amt_requested",
        "type": "FLOAT",
        "mode": "NULLABLE"
    }
]
```

### `cpg_analysis.sydney_allpurchases_WITH_SIFS`

```json
[
    {
        "name": "member_id",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "transaction_id",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "merchant_id",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "merchant_name",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "merchant_name_rollup",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "harmony_customer_id",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "harmony_customer_name",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "harmony_brand_sponsor_id",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "harmony_brand_sponsor_name",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "date",
        "type": "DATE",
        "mode": "NULLABLE"
    },
    {
        "name": "time",
        "type": "TIMESTAMP",
        "mode": "NULLABLE"
    },
    {
        "name": "item_code",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "item_code_type",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "item_desc",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "item_desc_source",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "manufacturer",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "brand",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "L1",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "L2",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "L3",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "L4",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "L5",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "L1_name",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "L2_name",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "L3_name",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "L4_name",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "L5_name",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "units",
        "type": "FLOAT",
        "mode": "NULLABLE"
    },
    {
        "name": "amt_requested",
        "type": "FLOAT",
        "mode": "NULLABLE"
    }
]
```

### `cpg_analysis.sydney_new_categories`

```json
[
    {
        "name": "id",
        "type": "INTEGER",
        "mode": "NULLABLE"
    },
    {
        "name": "upc",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "name",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "brand",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "sub_brand",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "units_per_pack",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "new_categories",
        "type": "RECORD",
        "mode": "REPEATED",
        "fields": [
            {
                "name": "provider_name",
                "type": "STRING",
                "mode": "NULLABLE"
            },
            {
                "name": "h1",
                "type": "STRING",
                "mode": "NULLABLE"
            },
            {
                "name": "h2",
                "type": "STRING",
                "mode": "NULLABLE"
            },
            {
                "name": "h3",
                "type": "STRING",
                "mode": "NULLABLE"
            },
            {
                "name": "h4",
                "type": "STRING",
                "mode": "NULLABLE"
            },
            {
                "name": "h5",
                "type": "STRING",
                "mode": "NULLABLE"
            }
        ]
    }
]
```

### `cpg_analysis.sydney_test_table`

```json
[
    {
        "name": "member_id",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "transaction_id",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "merchant_id",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "merchant_name",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "merchant_name_rollup",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "harmony_customer_id",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "harmony_customer_name",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "harmony_brand_sponsor_id",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "harmony_brand_sponsor_name",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "date",
        "type": "DATE",
        "mode": "NULLABLE"
    },
    {
        "name": "time",
        "type": "TIMESTAMP",
        "mode": "NULLABLE"
    },
    {
        "name": "item_code",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "item_code_type",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "item_desc",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "item_desc_source",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "manufacturer",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "brand",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "units",
        "type": "FLOAT",
        "mode": "NULLABLE"
    },
    {
        "name": "amt_requested",
        "type": "FLOAT",
        "mode": "NULLABLE"
    }
]
```

## Dataset: `encounter_reporting_dataset_jul_23`

### `encounter_reporting_dataset_jul_23.FIS_non_prelim_query_jul_23`

```json
[
    {
        "name": "transaction_id",
        "type": "INTEGER",
        "mode": "NULLABLE"
    },
    {
        "name": "id",
        "type": "INTEGER",
        "mode": "NULLABLE"
    },
    {
        "name": "type",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "amount",
        "type": "NUMERIC",
        "mode": "NULLABLE"
    },
    {
        "name": "book_id",
        "type": "INTEGER",
        "mode": "NULLABLE"
    },
    {
        "name": "benefit_id",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "approval_profile_id",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "sponsor_id",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "member_id",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "effective_date",
        "type": "TIMESTAMP",
        "mode": "NULLABLE"
    }
]
```

### `encounter_reporting_dataset_jul_23.OCCO_FIS_non_prelim_aug_26`

```json
[
    {
        "name": "transaction_id",
        "type": "INTEGER",
        "mode": "NULLABLE"
    },
    {
        "name": "id",
        "type": "INTEGER",
        "mode": "NULLABLE"
    },
    {
        "name": "type",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "amount",
        "type": "NUMERIC",
        "mode": "NULLABLE"
    },
    {
        "name": "book_id",
        "type": "INTEGER",
        "mode": "NULLABLE"
    },
    {
        "name": "benefit_id",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "approval_profile_id",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "sponsor_id",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "member_id",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "effective_date",
        "type": "TIMESTAMP",
        "mode": "NULLABLE"
    }
]
```

### `encounter_reporting_dataset_jul_23.OCCO_prelim_aug_26`

```json
[
    {
        "name": "effective_date",
        "type": "TIMESTAMP",
        "mode": "NULLABLE"
    },
    {
        "name": "transaction_id",
        "type": "INTEGER",
        "mode": "NULLABLE"
    },
    {
        "name": "sponsor_id",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "member_id",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "benefit_id",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "approval_profile_id",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "amount",
        "type": "NUMERIC",
        "mode": "NULLABLE"
    }
]
```

### `encounter_reporting_dataset_jul_23.jul_23_query_run`

```json
[
    {
        "name": "effective_date",
        "type": "TIMESTAMP",
        "mode": "NULLABLE"
    },
    {
        "name": "transaction_id",
        "type": "INTEGER",
        "mode": "NULLABLE"
    },
    {
        "name": "sponsor_id",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "member_id",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "benefit_id",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "approval_profile_id",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "amount",
        "type": "NUMERIC",
        "mode": "NULLABLE"
    }
]
```

## Dataset: `external_reporting_metabase`

### `external_reporting_metabase.benefit_active_members`

```json
[
    {
        "name": "snapshot_date",
        "type": "DATE"
    },
    {
        "name": "sponsor_id",
        "type": "STRING"
    },
    {
        "name": "benefit_id",
        "type": "STRING"
    },
    {
        "name": "benefit_name",
        "type": "STRING"
    },
    {
        "name": "benefit_type",
        "type": "STRING"
    },
    {
        "name": "sponsor_identifier",
        "type": "STRING"
    },
    {
        "name": "duration",
        "type": "STRING"
    },
    {
        "name": "active_members",
        "type": "INTEGER"
    },
    {
        "name": "brand_id",
        "type": "STRING"
    },
    {
        "name": "brand_name",
        "type": "STRING"
    },
    {
        "name": "customer_id",
        "type": "STRING"
    },
    {
        "name": "sponsor_name",
        "type": "STRING"
    },
    {
        "name": "benefit_name_specific",
        "type": "STRING"
    }
]
```

### `external_reporting_metabase.benefit_daily_lifecycle`

```json
[
    {
        "name": "date",
        "type": "DATE"
    },
    {
        "name": "sponsor_id",
        "type": "STRING"
    },
    {
        "name": "benefit_id",
        "type": "STRING"
    },
    {
        "name": "benefit_type",
        "type": "STRING"
    },
    {
        "name": "benefit_name",
        "type": "STRING"
    },
    {
        "name": "created_count",
        "type": "INTEGER"
    },
    {
        "name": "deleted_count",
        "type": "INTEGER"
    },
    {
        "name": "brand_id",
        "type": "STRING"
    },
    {
        "name": "brand_name",
        "type": "STRING"
    },
    {
        "name": "customer_id",
        "type": "STRING"
    },
    {
        "name": "sponsor_name",
        "type": "STRING"
    }
]
```

### `external_reporting_metabase.benefit_merchant_spend`

```json
[
    {
        "name": "spend_date",
        "type": "DATE"
    },
    {
        "name": "sponsor_id",
        "type": "STRING"
    },
    {
        "name": "member_sponsor_identifier",
        "type": "STRING"
    },
    {
        "name": "benefit_name",
        "type": "STRING"
    },
    {
        "name": "benefit_id",
        "type": "STRING"
    },
    {
        "name": "benefit_type",
        "type": "STRING"
    },
    {
        "name": "sponsor_identifier",
        "type": "STRING"
    },
    {
        "name": "merchant_grouped",
        "type": "STRING"
    },
    {
        "name": "merchant_mcc",
        "type": "STRING"
    },
    {
        "name": "total_spent",
        "type": "FLOAT"
    },
    {
        "name": "transaction_count",
        "type": "INTEGER"
    },
    {
        "name": "brand_id",
        "type": "STRING"
    },
    {
        "name": "brand_name",
        "type": "STRING"
    },
    {
        "name": "customer_id",
        "type": "STRING"
    },
    {
        "name": "sponsor_name",
        "type": "STRING"
    }
]
```

### `external_reporting_metabase.benefit_reference`

```json
[
    {
        "name": "benefit_id",
        "type": "STRING"
    },
    {
        "name": "benefit_name",
        "type": "STRING"
    },
    {
        "name": "benefit_type",
        "type": "STRING"
    },
    {
        "name": "sponsor_id",
        "type": "STRING"
    },
    {
        "name": "sponsor_identifier",
        "type": "STRING"
    }
]
```

### `external_reporting_metabase.benefit_spend_daily`

```json
[
    {
        "name": "spend_date",
        "type": "DATE"
    },
    {
        "name": "sponsor_id",
        "type": "STRING"
    },
    {
        "name": "benefit_id",
        "type": "STRING"
    },
    {
        "name": "benefit_name",
        "type": "STRING"
    },
    {
        "name": "benefit_type",
        "type": "STRING"
    },
    {
        "name": "sponsor_identifier",
        "type": "STRING"
    },
    {
        "name": "total_spent",
        "type": "FLOAT"
    },
    {
        "name": "transaction_count",
        "type": "INTEGER"
    },
    {
        "name": "unique_members",
        "type": "INTEGER"
    },
    {
        "name": "brand_id",
        "type": "STRING"
    },
    {
        "name": "brand_name",
        "type": "STRING"
    },
    {
        "name": "customer_id",
        "type": "STRING"
    },
    {
        "name": "sponsor_name",
        "type": "STRING"
    }
]
```

### `external_reporting_metabase.benefit_utilization_daily`

```json
[
    {
        "name": "spend_date",
        "type": "DATE"
    },
    {
        "name": "sponsor_id",
        "type": "STRING"
    },
    {
        "name": "benefit_id",
        "type": "STRING"
    },
    {
        "name": "benefit_name",
        "type": "STRING"
    },
    {
        "name": "benefit_type",
        "type": "STRING"
    },
    {
        "name": "sponsor_identifier",
        "type": "STRING"
    },
    {
        "name": "period_start",
        "type": "DATE"
    },
    {
        "name": "period_end",
        "type": "DATE"
    },
    {
        "name": "daily_spent",
        "type": "FLOAT"
    },
    {
        "name": "cumulative_spent",
        "type": "FLOAT"
    },
    {
        "name": "total_funded",
        "type": "FLOAT"
    },
    {
        "name": "utilization_rate",
        "type": "FLOAT"
    },
    {
        "name": "days_into_period",
        "type": "INTEGER"
    },
    {
        "name": "brand_id",
        "type": "STRING"
    },
    {
        "name": "brand_name",
        "type": "STRING"
    },
    {
        "name": "customer_id",
        "type": "STRING"
    },
    {
        "name": "sponsor_name",
        "type": "STRING"
    }
]
```

### `external_reporting_metabase.benefit_utilization_quarterly`

```json
[
    {
        "name": "quarter",
        "type": "STRING"
    },
    {
        "name": "quarter_start",
        "type": "DATE"
    },
    {
        "name": "quarter_end",
        "type": "DATE"
    },
    {
        "name": "sponsor_id",
        "type": "STRING"
    },
    {
        "name": "benefit_id",
        "type": "STRING"
    },
    {
        "name": "benefit_name",
        "type": "STRING"
    },
    {
        "name": "benefit_type",
        "type": "STRING"
    },
    {
        "name": "sponsor_identifier",
        "type": "STRING"
    },
    {
        "name": "category",
        "type": "STRING"
    },
    {
        "name": "total_funded",
        "type": "FLOAT"
    },
    {
        "name": "total_spent",
        "type": "FLOAT"
    },
    {
        "name": "utilization_rate",
        "type": "FLOAT"
    },
    {
        "name": "active_enrollments",
        "type": "INTEGER"
    },
    {
        "name": "brand_id",
        "type": "STRING"
    },
    {
        "name": "brand_name",
        "type": "STRING"
    },
    {
        "name": "customer_id",
        "type": "STRING"
    },
    {
        "name": "sponsor_name",
        "type": "STRING"
    }
]
```

### `external_reporting_metabase.card_daily_snapshot`

```json
[
    {
        "name": "date",
        "type": "DATE",
        "mode": "NULLABLE"
    },
    {
        "name": "sponsor_id",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "contract_id",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "plan_id",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "segment_id",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "program_id",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "language",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "activation_count",
        "type": "INTEGER",
        "mode": "NULLABLE"
    },
    {
        "name": "brand_id",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "brand_name",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "customer_id",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "sponsor_name",
        "type": "STRING",
        "mode": "NULLABLE"
    }
]
```

### `external_reporting_metabase.card_metrics`

```json
[
    {
        "name": "customer_id",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "brand_id",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "brand_name",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "sponsor_id",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "contract_id",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "plan_id",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "segment_id",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "program_id",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "language",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "sum_age_inactive_cards",
        "type": "INTEGER",
        "mode": "NULLABLE"
    },
    {
        "name": "total_inactive_cards",
        "type": "INTEGER",
        "mode": "NULLABLE"
    },
    {
        "name": "sum_days_creation_to_activation",
        "type": "INTEGER",
        "mode": "NULLABLE"
    },
    {
        "name": "total_cards_activated",
        "type": "INTEGER",
        "mode": "NULLABLE"
    }
]
```

### `external_reporting_metabase.card_summary`

```json
[
    {
        "name": "person_id",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "member_id",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "card_id",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "sponsor_id",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "program_id",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "language",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "card_type",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "processor",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "processor_status",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "status",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "display_status",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "is_replacement",
        "type": "BOOLEAN",
        "mode": "NULLABLE"
    },
    {
        "name": "replacement_reason",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "last_four",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "created_at",
        "type": "TIMESTAMP",
        "mode": "NULLABLE"
    },
    {
        "name": "shipped_at",
        "type": "TIMESTAMP",
        "mode": "NULLABLE"
    },
    {
        "name": "activated_at",
        "type": "TIMESTAMP",
        "mode": "NULLABLE"
    },
    {
        "name": "issued_at",
        "type": "TIMESTAMP",
        "mode": "NULLABLE"
    },
    {
        "name": "brand_id",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "brand_name",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "customer_id",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "sponsor_name",
        "type": "STRING",
        "mode": "NULLABLE"
    }
]
```

### `external_reporting_metabase.care_call_stats_aggregated`

```json
[
    {
        "name": "time_period",
        "type": "STRING"
    },
    {
        "name": "period_type",
        "type": "STRING"
    },
    {
        "name": "call_date",
        "type": "DATE"
    },
    {
        "name": "language",
        "type": "STRING"
    },
    {
        "name": "offered",
        "type": "INTEGER"
    },
    {
        "name": "handled",
        "type": "INTEGER"
    },
    {
        "name": "abandoned",
        "type": "INTEGER"
    },
    {
        "name": "short_abandon",
        "type": "INTEGER"
    },
    {
        "name": "abandon_pct",
        "type": "FLOAT"
    },
    {
        "name": "aht_seconds",
        "type": "FLOAT"
    },
    {
        "name": "att_seconds",
        "type": "FLOAT"
    },
    {
        "name": "ahdt_seconds",
        "type": "FLOAT"
    },
    {
        "name": "acw_seconds",
        "type": "FLOAT"
    },
    {
        "name": "asa_seconds",
        "type": "FLOAT"
    },
    {
        "name": "record_count",
        "type": "INTEGER"
    },
    {
        "name": "sponsor_id",
        "type": "STRING"
    },
    {
        "name": "sponsor_name",
        "type": "STRING"
    },
    {
        "name": "customer_id",
        "type": "STRING"
    },
    {
        "name": "brand_id",
        "type": "STRING"
    },
    {
        "name": "brand_name",
        "type": "STRING"
    }
]
```

### `external_reporting_metabase.care_call_summary`

```json
[
    {
        "name": "call_id",
        "type": "STRING"
    },
    {
        "name": "call_guid",
        "type": "STRING"
    },
    {
        "name": "member_id",
        "type": "STRING"
    },
    {
        "name": "sponsor",
        "type": "STRING"
    },
    {
        "name": "plan_id",
        "type": "STRING"
    },
    {
        "name": "contract_id",
        "type": "STRING"
    },
    {
        "name": "queue_name",
        "type": "STRING"
    },
    {
        "name": "language",
        "type": "STRING"
    },
    {
        "name": "skills_list",
        "type": "STRING"
    },
    {
        "name": "call_start_time",
        "type": "TIMESTAMP"
    },
    {
        "name": "call_end_time",
        "type": "TIMESTAMP"
    },
    {
        "name": "call_date",
        "type": "DATE"
    },
    {
        "name": "local_date",
        "type": "STRING"
    },
    {
        "name": "local_hour",
        "type": "STRING"
    },
    {
        "name": "interaction_type_raw",
        "type": "STRING"
    },
    {
        "name": "call_direction",
        "type": "STRING"
    },
    {
        "name": "call_status",
        "type": "STRING"
    },
    {
        "name": "call_outcome",
        "type": "STRING"
    },
    {
        "name": "reached_agent",
        "type": "BOOLEAN"
    },
    {
        "name": "abandoned",
        "type": "BOOLEAN"
    },
    {
        "name": "handled",
        "type": "BOOLEAN"
    },
    {
        "name": "total_duration_minutes",
        "type": "FLOAT"
    },
    {
        "name": "handle_time_minutes",
        "type": "FLOAT"
    },
    {
        "name": "queue_wait_minutes",
        "type": "FLOAT"
    },
    {
        "name": "ivr_only_minutes",
        "type": "FLOAT"
    },
    {
        "name": "total_duration_seconds",
        "type": "FLOAT"
    },
    {
        "name": "handle_time_seconds",
        "type": "FLOAT"
    },
    {
        "name": "agent_talk_time_seconds",
        "type": "FLOAT"
    },
    {
        "name": "queue_duration_seconds",
        "type": "FLOAT"
    },
    {
        "name": "after_call_work_time_seconds",
        "type": "FLOAT"
    },
    {
        "name": "consult_time_seconds",
        "type": "FLOAT"
    },
    {
        "name": "meets_service_level",
        "type": "BOOLEAN"
    },
    {
        "name": "call_met_service_level",
        "type": "BOOLEAN"
    },
    {
        "name": "short_abandon",
        "type": "BOOLEAN"
    },
    {
        "name": "true_abandon",
        "type": "BOOLEAN"
    },
    {
        "name": "contact_reason",
        "type": "STRING"
    },
    {
        "name": "contact_sub_reason",
        "type": "STRING"
    },
    {
        "name": "display_to_agent",
        "type": "STRING"
    },
    {
        "name": "ivr_only",
        "type": "BOOLEAN"
    },
    {
        "name": "offered",
        "type": "BOOLEAN"
    },
    {
        "name": "event_timestamp",
        "type": "STRING"
    },
    {
        "name": "is_anonymous",
        "type": "BOOLEAN"
    },
    {
        "name": "sponsor_id",
        "type": "STRING"
    },
    {
        "name": "sponsor_identifier",
        "type": "STRING"
    },
    {
        "name": "segment_id",
        "type": "STRING"
    },
    {
        "name": "program_id",
        "type": "STRING"
    },
    {
        "name": "call_year",
        "type": "INTEGER"
    },
    {
        "name": "call_month",
        "type": "INTEGER"
    },
    {
        "name": "call_week",
        "type": "INTEGER"
    },
    {
        "name": "call_day_of_week",
        "type": "INTEGER"
    },
    {
        "name": "call_year_month",
        "type": "STRING"
    },
    {
        "name": "call_year_week",
        "type": "STRING"
    },
    {
        "name": "total_duration_minutes_filled",
        "type": "FLOAT"
    },
    {
        "name": "handle_time_minutes_filled",
        "type": "FLOAT"
    },
    {
        "name": "met_30_second_sla",
        "type": "BOOLEAN"
    },
    {
        "name": "brand_id",
        "type": "STRING"
    },
    {
        "name": "brand_name",
        "type": "STRING"
    },
    {
        "name": "customer_id",
        "type": "STRING"
    },
    {
        "name": "sponsor_name",
        "type": "STRING"
    }
]
```

### `external_reporting_metabase.care_daily_metrics`

```json
[
    {
        "name": "date",
        "type": "DATE"
    },
    {
        "name": "sponsor_id",
        "type": "STRING"
    },
    {
        "name": "sponsor",
        "type": "STRING"
    },
    {
        "name": "queue_name",
        "type": "STRING"
    },
    {
        "name": "language",
        "type": "STRING"
    },
    {
        "name": "call_direction",
        "type": "STRING"
    },
    {
        "name": "segment_id",
        "type": "STRING"
    },
    {
        "name": "program_id",
        "type": "STRING"
    },
    {
        "name": "total_calls",
        "type": "INTEGER"
    },
    {
        "name": "inbound_calls",
        "type": "INTEGER"
    },
    {
        "name": "outbound_calls",
        "type": "INTEGER"
    },
    {
        "name": "offered_calls",
        "type": "INTEGER"
    },
    {
        "name": "handled_calls",
        "type": "INTEGER"
    },
    {
        "name": "abandoned_calls",
        "type": "INTEGER"
    },
    {
        "name": "reached_agent_calls",
        "type": "INTEGER"
    },
    {
        "name": "ivr_only_calls",
        "type": "INTEGER"
    },
    {
        "name": "short_abandon_calls",
        "type": "INTEGER"
    },
    {
        "name": "true_abandon_calls",
        "type": "INTEGER"
    },
    {
        "name": "calls_met_service_level",
        "type": "INTEGER"
    },
    {
        "name": "calls_met_30s_sla",
        "type": "INTEGER"
    },
    {
        "name": "total_duration_minutes",
        "type": "FLOAT"
    },
    {
        "name": "handle_time_minutes",
        "type": "FLOAT"
    },
    {
        "name": "queue_wait_minutes",
        "type": "FLOAT"
    },
    {
        "name": "ivr_only_minutes",
        "type": "FLOAT"
    },
    {
        "name": "total_agent_talk_time_seconds",
        "type": "FLOAT"
    },
    {
        "name": "total_queue_duration_seconds",
        "type": "FLOAT"
    },
    {
        "name": "total_after_call_work_seconds",
        "type": "FLOAT"
    },
    {
        "name": "avg_handle_time_seconds",
        "type": "FLOAT"
    },
    {
        "name": "avg_agent_talk_time_seconds",
        "type": "FLOAT"
    },
    {
        "name": "avg_queue_duration_seconds",
        "type": "FLOAT"
    },
    {
        "name": "avg_after_call_work_seconds",
        "type": "FLOAT"
    },
    {
        "name": "avg_speed_of_answer_seconds",
        "type": "FLOAT"
    },
    {
        "name": "handled_pct",
        "type": "FLOAT"
    },
    {
        "name": "abandoned_pct",
        "type": "FLOAT"
    },
    {
        "name": "service_level_pct",
        "type": "FLOAT"
    },
    {
        "name": "sla_30s_pct",
        "type": "FLOAT"
    },
    {
        "name": "brand_id",
        "type": "STRING"
    },
    {
        "name": "brand_name",
        "type": "STRING"
    },
    {
        "name": "customer_id",
        "type": "STRING"
    },
    {
        "name": "sponsor_name",
        "type": "STRING"
    }
]
```

### `external_reporting_metabase.member_card_combined`

```json
[
    {
        "name": "person_id",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "member_id",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "sponsor_id",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "sponsor_identifier",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "birth_year",
        "type": "INTEGER",
        "mode": "NULLABLE"
    },
    {
        "name": "language",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "state",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "contract_id",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "plan_id",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "segment_id",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "program_id",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "member_state",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "created_at",
        "type": "TIMESTAMP",
        "mode": "NULLABLE"
    },
    {
        "name": "activated_at",
        "type": "TIMESTAMP",
        "mode": "NULLABLE"
    },
    {
        "name": "deactivated_at",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "status",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "brand_id",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "brand_name",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "customer_id",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "sponsor_name",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "card_count",
        "type": "INTEGER",
        "mode": "NULLABLE"
    },
    {
        "name": "active_card_count",
        "type": "INTEGER",
        "mode": "NULLABLE"
    },
    {
        "name": "shipped_card_count",
        "type": "INTEGER",
        "mode": "NULLABLE"
    },
    {
        "name": "created_card_count",
        "type": "INTEGER",
        "mode": "NULLABLE"
    },
    {
        "name": "cancelled_card_count",
        "type": "INTEGER",
        "mode": "NULLABLE"
    },
    {
        "name": "inactive_cards_shipped_over_60_days",
        "type": "INTEGER",
        "mode": "NULLABLE"
    },
    {
        "name": "has_inactive_card_shipped_over_60_days",
        "type": "BOOLEAN",
        "mode": "NULLABLE"
    },
    {
        "name": "cards",
        "type": "RECORD",
        "mode": "REPEATED",
        "fields": [
            {
                "name": "card_id",
                "type": "STRING",
                "mode": "NULLABLE"
            },
            {
                "name": "card_type",
                "type": "STRING",
                "mode": "NULLABLE"
            },
            {
                "name": "processor",
                "type": "STRING",
                "mode": "NULLABLE"
            },
            {
                "name": "status",
                "type": "STRING",
                "mode": "NULLABLE"
            },
            {
                "name": "processor_status",
                "type": "STRING",
                "mode": "NULLABLE"
            },
            {
                "name": "is_replacement",
                "type": "BOOLEAN",
                "mode": "NULLABLE"
            },
            {
                "name": "last_four",
                "type": "STRING",
                "mode": "NULLABLE"
            },
            {
                "name": "created_at",
                "type": "TIMESTAMP",
                "mode": "NULLABLE"
            },
            {
                "name": "shipped_at",
                "type": "TIMESTAMP",
                "mode": "NULLABLE"
            },
            {
                "name": "activated_at",
                "type": "TIMESTAMP",
                "mode": "NULLABLE"
            }
        ]
    }
]
```

### `external_reporting_metabase.member_card_status`

```json
[
    {
        "name": "member_id",
        "type": "STRING"
    },
    {
        "name": "sponsor_id",
        "type": "STRING"
    },
    {
        "name": "status",
        "type": "STRING"
    },
    {
        "name": "card_count",
        "type": "INTEGER"
    },
    {
        "name": "active_card_count",
        "type": "INTEGER"
    },
    {
        "name": "has_card",
        "type": "BOOLEAN"
    },
    {
        "name": "brand_id",
        "type": "STRING"
    },
    {
        "name": "brand_name",
        "type": "STRING"
    },
    {
        "name": "customer_id",
        "type": "STRING"
    },
    {
        "name": "sponsor_name",
        "type": "STRING"
    }
]
```

### `external_reporting_metabase.member_daily_creation`

```json
[
    {
        "name": "date",
        "type": "DATE"
    },
    {
        "name": "sponsor_id",
        "type": "STRING"
    },
    {
        "name": "contract_id",
        "type": "STRING"
    },
    {
        "name": "plan_id",
        "type": "STRING"
    },
    {
        "name": "segment_id",
        "type": "STRING"
    },
    {
        "name": "program_id",
        "type": "STRING"
    },
    {
        "name": "plan_name",
        "type": "STRING"
    },
    {
        "name": "language",
        "type": "STRING"
    },
    {
        "name": "member_count",
        "type": "INTEGER"
    },
    {
        "name": "card_count",
        "type": "INTEGER"
    },
    {
        "name": "brand_id",
        "type": "STRING"
    },
    {
        "name": "brand_name",
        "type": "STRING"
    },
    {
        "name": "customer_id",
        "type": "STRING"
    },
    {
        "name": "sponsor_name",
        "type": "STRING"
    }
]
```

### `external_reporting_metabase.member_daily_deactivation`

```json
[
    {
        "name": "date",
        "type": "DATE"
    },
    {
        "name": "sponsor_id",
        "type": "STRING"
    },
    {
        "name": "sponsor_name",
        "type": "STRING"
    },
    {
        "name": "contract_id",
        "type": "STRING"
    },
    {
        "name": "plan_id",
        "type": "STRING"
    },
    {
        "name": "segment_id",
        "type": "STRING"
    },
    {
        "name": "program_id",
        "type": "STRING"
    },
    {
        "name": "deactivation_count",
        "type": "INTEGER"
    },
    {
        "name": "brand_id",
        "type": "STRING"
    },
    {
        "name": "brand_name",
        "type": "STRING"
    },
    {
        "name": "customer_id",
        "type": "STRING"
    }
]
```

### `external_reporting_metabase.member_daily_snapshot`

```json
[
    {
        "name": "date",
        "type": "DATE",
        "mode": "NULLABLE"
    },
    {
        "name": "sponsor_id",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "contract_id",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "plan_id",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "segment_id",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "program_id",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "language",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "status",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "member_count",
        "type": "INTEGER",
        "mode": "NULLABLE"
    },
    {
        "name": "brand_id",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "brand_name",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "customer_id",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "sponsor_name",
        "type": "STRING",
        "mode": "NULLABLE"
    }
]
```

### `external_reporting_metabase.member_deactivation_scheduled`

```json
[
    {
        "name": "member_id",
        "type": "STRING"
    },
    {
        "name": "sponsor_id",
        "type": "STRING"
    },
    {
        "name": "sponsor_identifier",
        "type": "STRING"
    },
    {
        "name": "scheduled_deactivation_at",
        "type": "TIMESTAMP"
    },
    {
        "name": "reason",
        "type": "STRING"
    },
    {
        "name": "scheduled_timestamp",
        "type": "STRING"
    },
    {
        "name": "brand_id",
        "type": "STRING"
    },
    {
        "name": "brand_name",
        "type": "STRING"
    },
    {
        "name": "customer_id",
        "type": "STRING"
    },
    {
        "name": "sponsor_name",
        "type": "STRING"
    }
]
```

### `external_reporting_metabase.member_detail_view`

```json
[
    {
        "name": "member_id",
        "type": "STRING"
    },
    {
        "name": "sponsor_id",
        "type": "STRING"
    },
    {
        "name": "sponsor_identifier",
        "type": "STRING"
    },
    {
        "name": "status",
        "type": "STRING"
    },
    {
        "name": "created_at",
        "type": "STRING"
    },
    {
        "name": "deactivated_at",
        "type": "STRING"
    },
    {
        "name": "birth_year",
        "type": "INTEGER"
    },
    {
        "name": "language",
        "type": "STRING"
    },
    {
        "name": "state",
        "type": "STRING"
    },
    {
        "name": "contract_id",
        "type": "STRING"
    },
    {
        "name": "plan_id",
        "type": "STRING"
    },
    {
        "name": "segment_id",
        "type": "STRING"
    },
    {
        "name": "program_id",
        "type": "STRING"
    },
    {
        "name": "benefit_count",
        "type": "INTEGER"
    },
    {
        "name": "card_id",
        "type": "STRING"
    },
    {
        "name": "card_status",
        "type": "STRING"
    },
    {
        "name": "card_created_at",
        "type": "TIMESTAMP"
    },
    {
        "name": "card_activated_at",
        "type": "TIMESTAMP"
    },
    {
        "name": "card_shipped_at",
        "type": "TIMESTAMP"
    },
    {
        "name": "card_last_four",
        "type": "STRING"
    },
    {
        "name": "brand_id",
        "type": "STRING"
    },
    {
        "name": "brand_name",
        "type": "STRING"
    },
    {
        "name": "customer_id",
        "type": "STRING"
    },
    {
        "name": "sponsor_name",
        "type": "STRING"
    }
]
```

### `external_reporting_metabase.member_eligibility_summary`

```json
[
    {
        "name": "person_id",
        "type": "STRING"
    },
    {
        "name": "member_id",
        "type": "STRING"
    },
    {
        "name": "sponsor_id",
        "type": "STRING"
    },
    {
        "name": "sponsor_identifier",
        "type": "STRING"
    },
    {
        "name": "birth_year",
        "type": "INTEGER"
    },
    {
        "name": "language",
        "type": "STRING"
    },
    {
        "name": "state",
        "type": "STRING"
    },
    {
        "name": "contract_id",
        "type": "STRING"
    },
    {
        "name": "plan_id",
        "type": "STRING"
    },
    {
        "name": "segment_id",
        "type": "STRING"
    },
    {
        "name": "program_id",
        "type": "STRING"
    },
    {
        "name": "created_at",
        "type": "STRING"
    },
    {
        "name": "deactivated_at",
        "type": "STRING"
    },
    {
        "name": "enrollment_id",
        "type": "STRING"
    },
    {
        "name": "benefit_id",
        "type": "STRING"
    },
    {
        "name": "benefit_type",
        "type": "STRING"
    },
    {
        "name": "benefit_name",
        "type": "STRING"
    },
    {
        "name": "benefit_active_at",
        "type": "TIMESTAMP"
    },
    {
        "name": "benefit_expires_at",
        "type": "TIMESTAMP"
    },
    {
        "name": "status",
        "type": "STRING"
    },
    {
        "name": "brand_id",
        "type": "STRING"
    },
    {
        "name": "brand_name",
        "type": "STRING"
    },
    {
        "name": "customer_id",
        "type": "STRING"
    },
    {
        "name": "sponsor_name",
        "type": "STRING"
    }
]
```

### `external_reporting_metabase.member_multi_plan`

```json
[
    {
        "name": "member_id",
        "type": "STRING"
    },
    {
        "name": "sponsor_id",
        "type": "STRING"
    },
    {
        "name": "sponsor_name",
        "type": "STRING"
    },
    {
        "name": "contract_id",
        "type": "STRING"
    },
    {
        "name": "plan_id",
        "type": "STRING"
    },
    {
        "name": "segment_id",
        "type": "STRING"
    },
    {
        "name": "program_id",
        "type": "STRING"
    },
    {
        "name": "plan_count",
        "type": "INTEGER"
    },
    {
        "name": "plan_ids",
        "type": "STRING"
    },
    {
        "name": "benefits",
        "type": "STRING"
    },
    {
        "name": "brand_id",
        "type": "STRING"
    },
    {
        "name": "brand_name",
        "type": "STRING"
    },
    {
        "name": "customer_id",
        "type": "STRING"
    }
]
```

### `external_reporting_metabase.member_summary`

```json
[
    {
        "name": "person_id",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "member_id",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "sponsor_id",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "sponsor_identifier",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "birth_year",
        "type": "INTEGER",
        "mode": "NULLABLE"
    },
    {
        "name": "language",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "state",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "contract_id",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "plan_id",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "segment_id",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "program_id",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "member_state",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "created_at",
        "type": "TIMESTAMP",
        "mode": "NULLABLE"
    },
    {
        "name": "activated_at",
        "type": "TIMESTAMP",
        "mode": "NULLABLE"
    },
    {
        "name": "deactivated_at",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "status",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "brand_id",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "brand_name",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "customer_id",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "sponsor_name",
        "type": "STRING",
        "mode": "NULLABLE"
    }
]
```

### `external_reporting_metabase.reason_code_mapping`

```json
[
    {
        "name": "reason_code",
        "type": "STRING"
    },
    {
        "name": "outcome_category",
        "type": "STRING"
    },
    {
        "name": "description",
        "type": "STRING"
    }
]
```

### `external_reporting_metabase.supplemental_invoicing_aggregated`

```json
[
    {
        "name": "contract_id",
        "type": "STRING"
    },
    {
        "name": "plan_id",
        "type": "STRING"
    },
    {
        "name": "segment_id",
        "type": "STRING"
    },
    {
        "name": "year",
        "type": "INTEGER"
    },
    {
        "name": "month",
        "type": "INTEGER"
    },
    {
        "name": "customer_id",
        "type": "STRING"
    },
    {
        "name": "brand_id",
        "type": "STRING"
    },
    {
        "name": "brand_name",
        "type": "STRING"
    },
    {
        "name": "sponsor_id",
        "type": "STRING"
    },
    {
        "name": "sponsor_name",
        "type": "STRING"
    },
    {
        "name": "program_id",
        "type": "STRING"
    },
    {
        "name": "plan_year",
        "type": "STRING"
    },
    {
        "name": "member_count",
        "type": "INTEGER"
    }
]
```

### `external_reporting_metabase.supplemental_invoicing_members`

```json
[
    {
        "name": "member_id",
        "type": "STRING"
    },
    {
        "name": "sponsor_id",
        "type": "STRING"
    },
    {
        "name": "sponsor_identifier",
        "type": "STRING"
    },
    {
        "name": "sponsor_name",
        "type": "STRING"
    },
    {
        "name": "customer_id",
        "type": "STRING"
    },
    {
        "name": "brand_id",
        "type": "STRING"
    },
    {
        "name": "brand_name",
        "type": "STRING"
    },
    {
        "name": "contract_id",
        "type": "STRING"
    },
    {
        "name": "plan_id",
        "type": "STRING"
    },
    {
        "name": "segment_id",
        "type": "STRING"
    },
    {
        "name": "recorded_at",
        "type": "DATE"
    },
    {
        "name": "year",
        "type": "INTEGER"
    },
    {
        "name": "month",
        "type": "INTEGER"
    },
    {
        "name": "program_id",
        "type": "STRING"
    },
    {
        "name": "plan_year",
        "type": "STRING"
    }
]
```

### `external_reporting_metabase.swipe_reason_daily`

```json
[
    {
        "name": "date",
        "type": "DATE"
    },
    {
        "name": "reason",
        "type": "STRING"
    },
    {
        "name": "swipe_count",
        "type": "INTEGER"
    },
    {
        "name": "sponsor_id",
        "type": "STRING"
    },
    {
        "name": "sponsor_name",
        "type": "STRING"
    },
    {
        "name": "customer_id",
        "type": "STRING"
    },
    {
        "name": "brand_id",
        "type": "STRING"
    },
    {
        "name": "brand_name",
        "type": "STRING"
    }
]
```

### `external_reporting_metabase.swipe_summary`

```json
[
    {
        "name": "transaction_id",
        "type": "STRING"
    },
    {
        "name": "member_id",
        "type": "STRING"
    },
    {
        "name": "sponsor_id",
        "type": "STRING"
    },
    {
        "name": "sponsor_identifier",
        "type": "STRING"
    },
    {
        "name": "merchant_id",
        "type": "STRING"
    },
    {
        "name": "merchant_name",
        "type": "STRING"
    },
    {
        "name": "merchant_name_rollup",
        "type": "STRING"
    },
    {
        "name": "reason",
        "type": "STRING"
    },
    {
        "name": "approved",
        "type": "BOOLEAN"
    },
    {
        "name": "swipe_outcome",
        "type": "STRING"
    },
    {
        "name": "spending",
        "type": "BOOLEAN"
    },
    {
        "name": "state",
        "type": "STRING"
    },
    {
        "name": "amount_requested",
        "type": "FLOAT"
    },
    {
        "name": "amount_approved",
        "type": "FLOAT"
    },
    {
        "name": "occurred_at",
        "type": "TIMESTAMP"
    },
    {
        "name": "settled_at",
        "type": "TIMESTAMP"
    },
    {
        "name": "reversed_at",
        "type": "TIMESTAMP"
    },
    {
        "name": "sources",
        "type": "STRING",
        "mode": "REPEATED"
    },
    {
        "name": "brand_id",
        "type": "STRING"
    },
    {
        "name": "brand_name",
        "type": "STRING"
    },
    {
        "name": "customer_id",
        "type": "STRING"
    },
    {
        "name": "sponsor_name",
        "type": "STRING"
    }
]
```

### `external_reporting_metabase.trip_summary`

```json
[
    {
        "name": "trip_id",
        "type": "STRING"
    },
    {
        "name": "member_id",
        "type": "STRING"
    },
    {
        "name": "sponsor_id",
        "type": "STRING"
    },
    {
        "name": "sponsor_identifier",
        "type": "STRING"
    },
    {
        "name": "merchant_id",
        "type": "STRING"
    },
    {
        "name": "merchant_name",
        "type": "STRING"
    },
    {
        "name": "merchant_name_rollup",
        "type": "STRING"
    },
    {
        "name": "trip_hour",
        "type": "TIMESTAMP"
    },
    {
        "name": "swipe_count",
        "type": "INTEGER"
    },
    {
        "name": "trip_outcome",
        "type": "STRING"
    },
    {
        "name": "trip_reason",
        "type": "STRING"
    },
    {
        "name": "total_requested",
        "type": "FLOAT"
    },
    {
        "name": "total_approved",
        "type": "FLOAT"
    },
    {
        "name": "first_swipe_at",
        "type": "TIMESTAMP"
    },
    {
        "name": "last_swipe_at",
        "type": "TIMESTAMP"
    },
    {
        "name": "brand_id",
        "type": "STRING"
    },
    {
        "name": "brand_name",
        "type": "STRING"
    },
    {
        "name": "customer_id",
        "type": "STRING"
    },
    {
        "name": "sponsor_name",
        "type": "STRING"
    }
]
```

## Dataset: `harmony_export`

### `harmony_export.benefit_factors`

```json
[
    {
        "name": "benefit_id",
        "type": "STRING"
    },
    {
        "name": "factor_id",
        "type": "INTEGER"
    },
    {
        "name": "factor_value_id",
        "type": "INTEGER"
    },
    {
        "name": "created_at",
        "type": "TIMESTAMP"
    },
    {
        "name": "updated_at",
        "type": "TIMESTAMP"
    },
    {
        "name": "deleted_at",
        "type": "TIMESTAMP"
    }
]
```

### `harmony_export.benefits`

```json
[
    {
        "name": "benefit_id",
        "type": "STRING"
    },
    {
        "name": "sponsor_id",
        "type": "STRING"
    },
    {
        "name": "type",
        "type": "STRING"
    },
    {
        "name": "sponsor_identifier",
        "type": "STRING"
    },
    {
        "name": "name",
        "type": "STRING"
    },
    {
        "name": "multiple_enrollment",
        "type": "BOOLEAN"
    },
    {
        "name": "iterations",
        "type": "INTEGER"
    },
    {
        "name": "interval",
        "type": "STRING"
    },
    {
        "name": "duration",
        "type": "STRING"
    },
    {
        "name": "start_date",
        "type": "TIMESTAMP"
    },
    {
        "name": "calculated_end_date",
        "type": "TIMESTAMP"
    },
    {
        "name": "created_at",
        "type": "TIMESTAMP"
    },
    {
        "name": "updated_at",
        "type": "TIMESTAMP"
    },
    {
        "name": "deleted_at",
        "type": "TIMESTAMP"
    },
    {
        "name": "funding_amount",
        "type": "NUMERIC"
    },
    {
        "name": "proration_type",
        "type": "STRING"
    },
    {
        "name": "priority",
        "type": "INTEGER"
    },
    {
        "name": "is_variable_amount",
        "type": "BOOLEAN"
    },
    {
        "name": "amount_on_enrollment",
        "type": "BOOLEAN"
    },
    {
        "name": "otchs_benefit_identifier",
        "type": "STRING"
    },
    {
        "name": "catalog_on_enrollment",
        "type": "BOOLEAN"
    },
    {
        "name": "survey_json",
        "type": "STRING"
    },
    {
        "name": "resource_url",
        "type": "STRING"
    },
    {
        "name": "approval_profiles",
        "type": "RECORD",
        "mode": "REPEATED",
        "fields": [
            {
                "name": "approval_profile_id",
                "type": "STRING"
            },
            {
                "name": "approval_profile_name",
                "type": "STRING"
            },
            {
                "name": "core_categories",
                "type": "RECORD",
                "mode": "REPEATED",
                "fields": [
                    {
                        "name": "id",
                        "type": "STRING"
                    },
                    {
                        "name": "name",
                        "type": "STRING"
                    }
                ]
            }
        ]
    }
]
```

### `harmony_export.call_records`

```json
[
    {
        "name": "call_record_id",
        "type": "STRING"
    },
    {
        "name": "call_start_time",
        "type": "TIMESTAMP"
    },
    {
        "name": "call_end_time",
        "type": "TIMESTAMP"
    },
    {
        "name": "created_at",
        "type": "TIMESTAMP"
    },
    {
        "name": "updated_at",
        "type": "TIMESTAMP"
    },
    {
        "name": "call_type",
        "type": "STRING"
    },
    {
        "name": "member_id",
        "type": "STRING"
    },
    {
        "name": "sponsor_id",
        "type": "STRING"
    },
    {
        "name": "sponsor_name",
        "type": "STRING"
    },
    {
        "name": "member_identifier",
        "type": "STRING"
    },
    {
        "name": "caller_phone",
        "type": "STRING"
    },
    {
        "name": "ivr_member_id",
        "type": "STRING"
    },
    {
        "name": "ivr_sponsor_id",
        "type": "STRING"
    },
    {
        "name": "agent_member_id",
        "type": "STRING"
    },
    {
        "name": "agent_sponsor_id",
        "type": "STRING"
    },
    {
        "name": "call_sid",
        "type": "STRING"
    },
    {
        "name": "called_number",
        "type": "STRING"
    },
    {
        "name": "ivr_start_time",
        "type": "TIMESTAMP"
    },
    {
        "name": "ivr_end_time",
        "type": "TIMESTAMP"
    },
    {
        "name": "ivr_call_duration_seconds",
        "type": "INTEGER"
    },
    {
        "name": "ivr_call_status",
        "type": "STRING"
    },
    {
        "name": "call_outcome",
        "type": "STRING"
    },
    {
        "name": "call_language",
        "type": "STRING"
    },
    {
        "name": "identity_status",
        "type": "STRING"
    },
    {
        "name": "reached_agent",
        "type": "BOOLEAN"
    },
    {
        "name": "call_guid",
        "type": "STRING"
    },
    {
        "name": "call_summary_name",
        "type": "STRING"
    },
    {
        "name": "agent_start_time",
        "type": "TIMESTAMP"
    },
    {
        "name": "agent_end_time",
        "type": "TIMESTAMP"
    },
    {
        "name": "total_call_duration_including_acw_seconds",
        "type": "INTEGER"
    },
    {
        "name": "agent_total_call_duration_seconds",
        "type": "INTEGER"
    },
    {
        "name": "after_call_work_time_seconds",
        "type": "INTEGER"
    },
    {
        "name": "handle_time_seconds",
        "type": "INTEGER"
    },
    {
        "name": "handle_time_over_10_minutes_seconds",
        "type": "INTEGER"
    },
    {
        "name": "agent_talk_time_seconds",
        "type": "INTEGER"
    },
    {
        "name": "agent_consult_time_seconds",
        "type": "INTEGER"
    },
    {
        "name": "hold_time_seconds",
        "type": "INTEGER"
    },
    {
        "name": "external_consult_time_seconds",
        "type": "INTEGER"
    },
    {
        "name": "external_transfer_time_seconds",
        "type": "INTEGER"
    },
    {
        "name": "queue_duration_seconds",
        "type": "INTEGER"
    },
    {
        "name": "meets_service_level",
        "type": "INTEGER"
    },
    {
        "name": "call_met_service_level",
        "type": "INTEGER"
    },
    {
        "name": "call_met_service_level_20_seconds",
        "type": "INTEGER"
    },
    {
        "name": "call_met_service_level_45_seconds",
        "type": "INTEGER"
    },
    {
        "name": "handled",
        "type": "BOOLEAN"
    },
    {
        "name": "abandoned",
        "type": "BOOLEAN"
    },
    {
        "name": "short_abandon",
        "type": "BOOLEAN"
    },
    {
        "name": "true_abandon",
        "type": "BOOLEAN"
    },
    {
        "name": "short_abandon_20_seconds",
        "type": "BOOLEAN"
    },
    {
        "name": "short_abandon_30_seconds",
        "type": "BOOLEAN"
    },
    {
        "name": "short_abandon_45_seconds",
        "type": "BOOLEAN"
    },
    {
        "name": "offered",
        "type": "BOOLEAN"
    },
    {
        "name": "last_state",
        "type": "STRING"
    },
    {
        "name": "skills_list",
        "type": "STRING"
    },
    {
        "name": "interaction_type",
        "type": "STRING"
    },
    {
        "name": "queue_name",
        "type": "STRING"
    },
    {
        "name": "contact_reason",
        "type": "STRING"
    },
    {
        "name": "contact_sub_reason",
        "type": "STRING"
    },
    {
        "name": "display_to_agent",
        "type": "STRING"
    },
    {
        "name": "case_id",
        "type": "STRING"
    },
    {
        "name": "conversation_guid",
        "type": "STRING"
    },
    {
        "name": "utc_date",
        "type": "DATE"
    },
    {
        "name": "local_date",
        "type": "DATE"
    },
    {
        "name": "local_hour",
        "type": "STRING"
    },
    {
        "name": "voice_call_contact_id",
        "type": "STRING"
    },
    {
        "name": "related_sf_account_id",
        "type": "STRING"
    },
    {
        "name": "related_sf_contact_id",
        "type": "STRING"
    },
    {
        "name": "call_direction",
        "type": "STRING"
    },
    {
        "name": "call_status",
        "type": "STRING"
    },
    {
        "name": "language",
        "type": "STRING"
    },
    {
        "name": "is_anonymous",
        "type": "BOOLEAN"
    },
    {
        "name": "data_loaded_at",
        "type": "TIMESTAMP"
    }
]
```

### `harmony_export.catalog_obligation_events`

```json
[
    {
        "name": "enrollment_id",
        "type": "STRING"
    },
    {
        "name": "member_id",
        "type": "STRING"
    },
    {
        "name": "benefit_id",
        "type": "STRING"
    },
    {
        "name": "enrollment_sponsor_identifier",
        "type": "STRING"
    },
    {
        "name": "funding_amount",
        "type": "FLOAT"
    },
    {
        "name": "active_at",
        "type": "TIMESTAMP"
    },
    {
        "name": "expires_at",
        "type": "TIMESTAMP"
    },
    {
        "name": "created_at",
        "type": "TIMESTAMP"
    },
    {
        "name": "sponsor_id",
        "type": "STRING"
    },
    {
        "name": "sponsor_name",
        "type": "STRING"
    },
    {
        "name": "benefit_name",
        "type": "STRING"
    },
    {
        "name": "benefit_type",
        "type": "STRING"
    },
    {
        "name": "otchs_benefit_identifier",
        "type": "STRING"
    },
    {
        "name": "catalog_on_enrollment",
        "type": "BOOLEAN"
    },
    {
        "name": "obligation_type",
        "type": "STRING"
    },
    {
        "name": "obligation_reason",
        "type": "STRING"
    },
    {
        "name": "event_timestamp",
        "type": "TIMESTAMP"
    },
    {
        "name": "catalog_shipment_tracker_id",
        "type": "INTEGER"
    },
    {
        "name": "catalog_kit_id",
        "type": "STRING"
    },
    {
        "name": "data_loaded_at",
        "type": "TIMESTAMP"
    }
]
```

### `harmony_export.catalog_tracking_events`

```json
[
    {
        "name": "member_id",
        "type": "STRING"
    },
    {
        "name": "sponsor_id",
        "type": "STRING"
    },
    {
        "name": "sponsor_identifier",
        "type": "STRING"
    },
    {
        "name": "card_created_at",
        "type": "TIMESTAMP"
    },
    {
        "name": "card_shipped_at",
        "type": "TIMESTAMP"
    },
    {
        "name": "catalog_created_at",
        "type": "TIMESTAMP"
    },
    {
        "name": "catalog_sent_at",
        "type": "TIMESTAMP"
    },
    {
        "name": "replacement_source",
        "type": "STRING"
    },
    {
        "name": "event_type",
        "type": "STRING"
    },
    {
        "name": "data_loaded_at",
        "type": "TIMESTAMP"
    }
]
```

### `harmony_export.core_categories`

```json
[
    {
        "name": "id",
        "type": "STRING"
    },
    {
        "name": "name",
        "type": "STRING"
    },
    {
        "name": "description",
        "type": "STRING"
    },
    {
        "name": "created_at",
        "type": "TIMESTAMP"
    },
    {
        "name": "updated_at",
        "type": "TIMESTAMP"
    },
    {
        "name": "deleted_at",
        "type": "TIMESTAMP"
    }
]
```

### `harmony_export.coupon_enrollments`

```json
[
    {
        "name": "coupon_program_enrollment_id",
        "type": "STRING"
    },
    {
        "name": "coupon_program_id",
        "type": "STRING"
    },
    {
        "name": "member_id",
        "type": "STRING"
    },
    {
        "name": "cpg_sponsor_id",
        "type": "STRING"
    },
    {
        "name": "cpg_name",
        "type": "STRING"
    },
    {
        "name": "clipped_at",
        "type": "TIMESTAMP"
    },
    {
        "name": "expires_at",
        "type": "TIMESTAMP"
    },
    {
        "name": "deleted_at",
        "type": "TIMESTAMP"
    },
    {
        "name": "coupon_enrollment_book_id",
        "type": "INTEGER"
    },
    {
        "name": "coupon_pool_book_id",
        "type": "INTEGER"
    },
    {
        "name": "surrender_date",
        "type": "TIMESTAMP"
    },
    {
        "name": "coupon_brand_name",
        "type": "STRING"
    },
    {
        "name": "dollar_amount",
        "type": "NUMERIC"
    },
    {
        "name": "headline",
        "type": "STRING"
    },
    {
        "name": "details",
        "type": "STRING"
    },
    {
        "name": "legal_disclaimer",
        "type": "STRING"
    },
    {
        "name": "discount_type",
        "type": "STRING"
    },
    {
        "name": "percentage",
        "type": "NUMERIC"
    }
]
```

### `harmony_export.coupons`

```json
[
    {
        "name": "coupon_program_id",
        "type": "STRING"
    },
    {
        "name": "coupon_id",
        "type": "STRING"
    },
    {
        "name": "coupon_brand_name",
        "type": "STRING"
    },
    {
        "name": "dollar_amount",
        "type": "NUMERIC"
    },
    {
        "name": "cpg_sponsor_id",
        "type": "STRING"
    },
    {
        "name": "cpg_name",
        "type": "STRING"
    },
    {
        "name": "program_target_member_id",
        "type": "STRING"
    },
    {
        "name": "program_target_sponsor_id",
        "type": "STRING"
    },
    {
        "name": "created_at",
        "type": "TIMESTAMP"
    },
    {
        "name": "active_at",
        "type": "TIMESTAMP"
    },
    {
        "name": "expires_at",
        "type": "TIMESTAMP"
    },
    {
        "name": "remaining_coupon_quantity",
        "type": "INTEGER"
    },
    {
        "name": "coupon_pool_book_id",
        "type": "INTEGER"
    },
    {
        "name": "funding_account_identifier",
        "type": "STRING"
    },
    {
        "name": "approval_profile_id",
        "type": "STRING"
    },
    {
        "name": "headline",
        "type": "STRING"
    },
    {
        "name": "details",
        "type": "STRING"
    },
    {
        "name": "legal_disclaimer",
        "type": "STRING"
    },
    {
        "name": "discount_type",
        "type": "STRING"
    },
    {
        "name": "percentage",
        "type": "NUMERIC"
    }
]
```

### `harmony_export.enrollments`

```json
[
    {
        "name": "enrollment_id",
        "type": "STRING"
    },
    {
        "name": "member_id",
        "type": "STRING"
    },
    {
        "name": "benefit_id",
        "type": "STRING"
    },
    {
        "name": "sponsor_identifier",
        "type": "STRING"
    },
    {
        "name": "program_enrollment_id",
        "type": "STRING"
    },
    {
        "name": "created_at",
        "type": "TIMESTAMP"
    },
    {
        "name": "deleted_at",
        "type": "TIMESTAMP"
    },
    {
        "name": "active_at",
        "type": "TIMESTAMP"
    },
    {
        "name": "expires_at",
        "type": "TIMESTAMP"
    },
    {
        "name": "funding_amount",
        "type": "NUMERIC"
    }
]
```

### `harmony_export.factor_values`

```json
[
    {
        "name": "factor_value_id",
        "type": "INTEGER"
    },
    {
        "name": "factor_id",
        "type": "INTEGER"
    },
    {
        "name": "value",
        "type": "STRING"
    },
    {
        "name": "description",
        "type": "STRING"
    },
    {
        "name": "created_at",
        "type": "TIMESTAMP"
    },
    {
        "name": "updated_at",
        "type": "TIMESTAMP"
    },
    {
        "name": "deleted_at",
        "type": "TIMESTAMP"
    }
]
```

### `harmony_export.factors`

```json
[
    {
        "name": "factor_id",
        "type": "INTEGER"
    },
    {
        "name": "sponsor_id",
        "type": "STRING"
    },
    {
        "name": "factor_identifier",
        "type": "STRING"
    },
    {
        "name": "name",
        "type": "STRING"
    },
    {
        "name": "description",
        "type": "STRING"
    },
    {
        "name": "created_at",
        "type": "TIMESTAMP"
    },
    {
        "name": "updated_at",
        "type": "TIMESTAMP"
    },
    {
        "name": "deleted_at",
        "type": "TIMESTAMP"
    }
]
```

### `harmony_export.fis_delegated_auth`

```json
[
    {
        "name": "auth_id",
        "type": "STRING"
    },
    {
        "name": "member_id",
        "type": "STRING"
    },
    {
        "name": "sponsor_id",
        "type": "STRING"
    },
    {
        "name": "log_id",
        "type": "INTEGER"
    },
    {
        "name": "retrieval_reference_number",
        "type": "STRING"
    },
    {
        "name": "transaction_id",
        "type": "INTEGER"
    },
    {
        "name": "preliminary_transaction_id",
        "type": "INTEGER"
    },
    {
        "name": "occurred_at",
        "type": "TIMESTAMP"
    },
    {
        "name": "created_at",
        "type": "TIMESTAMP"
    },
    {
        "name": "reason",
        "type": "STRING"
    },
    {
        "name": "card_proxy",
        "type": "INTEGER"
    },
    {
        "name": "subprogram_id",
        "type": "INTEGER"
    },
    {
        "name": "message_type",
        "type": "STRING"
    },
    {
        "name": "processing_code",
        "type": "STRING"
    },
    {
        "name": "network",
        "type": "STRING"
    },
    {
        "name": "amount",
        "type": "NUMERIC"
    },
    {
        "name": "body",
        "type": "STRING"
    },
    {
        "name": "response",
        "type": "STRING"
    }
]
```

### `harmony_export.fis_transaction_basket_items`

```json
[
    {
        "name": "fis_basket_item_id",
        "type": "INTEGER"
    },
    {
        "name": "amount_requested",
        "type": "NUMERIC"
    },
    {
        "name": "product_type",
        "type": "STRING"
    },
    {
        "name": "item_code",
        "type": "STRING"
    },
    {
        "name": "item_code_type",
        "type": "STRING"
    },
    {
        "name": "transaction_id",
        "type": "INTEGER"
    },
    {
        "name": "quantity",
        "type": "INTEGER"
    },
    {
        "name": "eligible",
        "type": "BOOLEAN"
    },
    {
        "name": "merchant_description",
        "type": "STRING"
    },
    {
        "name": "retrieval_reference_number",
        "type": "STRING"
    }
]
```

### `harmony_export.funded_benefit_approval_profile`

```json
[
    {
        "name": "benefit_id",
        "type": "STRING"
    },
    {
        "name": "approval_profile_id",
        "type": "STRING"
    },
    {
        "name": "approval_profile_name",
        "type": "STRING"
    },
    {
        "name": "core_categories",
        "type": "RECORD",
        "mode": "REPEATED",
        "fields": [
            {
                "name": "id",
                "type": "STRING"
            },
            {
                "name": "name",
                "type": "STRING"
            }
        ]
    },
    {
        "name": "factor_value",
        "type": "RECORD",
        "fields": [
            {
                "name": "factor_value_id",
                "type": "INTEGER"
            },
            {
                "name": "factor_id",
                "type": "INTEGER"
            },
            {
                "name": "value",
                "type": "STRING"
            },
            {
                "name": "description",
                "type": "STRING"
            },
            {
                "name": "created_at",
                "type": "TIMESTAMP"
            },
            {
                "name": "updated_at",
                "type": "TIMESTAMP"
            },
            {
                "name": "deleted_at",
                "type": "TIMESTAMP"
            },
            {
                "name": "factor",
                "type": "RECORD",
                "fields": [
                    {
                        "name": "factor_id",
                        "type": "INTEGER"
                    },
                    {
                        "name": "sponsor_id",
                        "type": "STRING"
                    },
                    {
                        "name": "factor_identifier",
                        "type": "STRING"
                    },
                    {
                        "name": "name",
                        "type": "STRING"
                    },
                    {
                        "name": "description",
                        "type": "STRING"
                    },
                    {
                        "name": "created_at",
                        "type": "TIMESTAMP"
                    },
                    {
                        "name": "updated_at",
                        "type": "TIMESTAMP"
                    },
                    {
                        "name": "deleted_at",
                        "type": "TIMESTAMP"
                    }
                ]
            }
        ]
    }
]
```

### `harmony_export.funded_benefit_approval_profiles`

```json
[
    {
        "name": "benefit_id",
        "type": "STRING"
    },
    {
        "name": "approval_profile_id",
        "type": "STRING"
    },
    {
        "name": "approval_profile_name",
        "type": "STRING"
    },
    {
        "name": "core_categories",
        "type": "RECORD",
        "mode": "REPEATED",
        "fields": [
            {
                "name": "id",
                "type": "STRING"
            },
            {
                "name": "name",
                "type": "STRING"
            }
        ]
    }
]
```

### `harmony_export.ingo_events`

```json
[
    {
        "name": "id",
        "type": "STRING"
    },
    {
        "name": "event_type",
        "type": "STRING"
    },
    {
        "name": "event_subtype",
        "type": "STRING"
    },
    {
        "name": "status",
        "type": "STRING"
    },
    {
        "name": "reimbursement_id",
        "type": "STRING"
    },
    {
        "name": "member_id",
        "type": "STRING"
    },
    {
        "name": "occurred_at",
        "type": "TIMESTAMP"
    },
    {
        "name": "created_at",
        "type": "TIMESTAMP"
    },
    {
        "name": "ingo_event_id",
        "type": "STRING"
    },
    {
        "name": "ingo_transaction_id",
        "type": "STRING"
    },
    {
        "name": "ingo_session_id",
        "type": "STRING"
    },
    {
        "name": "ingo_tracer_token",
        "type": "STRING"
    },
    {
        "name": "webhook_body",
        "type": "STRING"
    },
    {
        "name": "event_data",
        "type": "STRING"
    }
]
```

### `harmony_export.ingo_fund_movements`

```json
[
    {
        "name": "id",
        "type": "INTEGER"
    },
    {
        "name": "reimbursement_id",
        "type": "STRING"
    },
    {
        "name": "funding_account_id",
        "type": "STRING"
    },
    {
        "name": "bank_account_id",
        "type": "STRING"
    },
    {
        "name": "amount",
        "type": "NUMERIC"
    },
    {
        "name": "transferred_at",
        "type": "TIMESTAMP"
    },
    {
        "name": "ach_at",
        "type": "TIMESTAMP"
    },
    {
        "name": "ach_id",
        "type": "STRING"
    },
    {
        "name": "disbursed_at",
        "type": "TIMESTAMP"
    },
    {
        "name": "created_at",
        "type": "TIMESTAMP"
    },
    {
        "name": "updated_at",
        "type": "TIMESTAMP"
    }
]
```

### `harmony_export.items`

```json
[
    {
        "name": "item_id",
        "type": "INTEGER"
    },
    {
        "name": "gtin",
        "type": "STRING"
    },
    {
        "name": "name",
        "type": "STRING"
    },
    {
        "name": "brand_name",
        "type": "STRING"
    },
    {
        "name": "manufacturer",
        "type": "STRING"
    },
    {
        "name": "created_at",
        "type": "TIMESTAMP"
    },
    {
        "name": "updated_at",
        "type": "TIMESTAMP"
    },
    {
        "name": "size",
        "type": "FLOAT"
    },
    {
        "name": "unit_of_measure",
        "type": "STRING"
    },
    {
        "name": "plu",
        "type": "INTEGER"
    }
]
```

### `harmony_export.job`

```json
[
    {
        "name": "id",
        "type": "INTEGER"
    },
    {
        "name": "partner_id",
        "type": "STRING"
    },
    {
        "name": "filename",
        "type": "STRING"
    },
    {
        "name": "benthos_stream_configuration_id",
        "type": "INTEGER"
    },
    {
        "name": "ingest_configuration_value_copy",
        "type": "STRING"
    },
    {
        "name": "status",
        "type": "STRING"
    },
    {
        "name": "created_at",
        "type": "TIMESTAMP"
    },
    {
        "name": "updated_at",
        "type": "TIMESTAMP"
    },
    {
        "name": "deleted_at",
        "type": "TIMESTAMP"
    },
    {
        "name": "autorun",
        "type": "BOOLEAN"
    },
    {
        "name": "autodryrun",
        "type": "BOOLEAN"
    },
    {
        "name": "notes",
        "type": "STRING"
    },
    {
        "name": "job_runs",
        "type": "RECORD",
        "mode": "REPEATED",
        "fields": [
            {
                "name": "id",
                "type": "INTEGER"
            },
            {
                "name": "partner_id",
                "type": "STRING"
            },
            {
                "name": "job_id",
                "type": "INTEGER"
            },
            {
                "name": "dry_run",
                "type": "BOOLEAN"
            },
            {
                "name": "status",
                "type": "STRING"
            },
            {
                "name": "created_at",
                "type": "TIMESTAMP"
            },
            {
                "name": "updated_at",
                "type": "TIMESTAMP"
            },
            {
                "name": "total_lines",
                "type": "INTEGER"
            },
            {
                "name": "initiated_by",
                "type": "STRING"
            }
        ]
    },
    {
        "name": "benthos_stream_configuration",
        "type": "RECORD",
        "fields": [
            {
                "name": "id",
                "type": "INTEGER"
            },
            {
                "name": "partner_id",
                "type": "STRING"
            },
            {
                "name": "processing_type",
                "type": "STRING"
            },
            {
                "name": "label",
                "type": "STRING"
            },
            {
                "name": "name_pattern",
                "type": "STRING"
            },
            {
                "name": "configuration_template",
                "type": "STRING"
            },
            {
                "name": "created_at",
                "type": "TIMESTAMP"
            },
            {
                "name": "updated_at",
                "type": "TIMESTAMP"
            },
            {
                "name": "active",
                "type": "BOOLEAN"
            },
            {
                "name": "autorun",
                "type": "BOOLEAN"
            },
            {
                "name": "codec",
                "type": "STRING"
            },
            {
                "name": "autodryrun",
                "type": "BOOLEAN"
            }
        ]
    }
]
```

### `harmony_export.mail_reimbursement_requests`

```json
[
    {
        "name": "id",
        "type": "INTEGER"
    },
    {
        "name": "type",
        "type": "STRING"
    },
    {
        "name": "status",
        "type": "STRING"
    },
    {
        "name": "reimbursement_id",
        "type": "STRING"
    },
    {
        "name": "extend_url",
        "type": "STRING"
    },
    {
        "name": "ocr_run_identifier",
        "type": "STRING"
    },
    {
        "name": "ocr_name",
        "type": "STRING"
    },
    {
        "name": "ocr_address_street1",
        "type": "STRING"
    },
    {
        "name": "ocr_address_street2",
        "type": "STRING"
    },
    {
        "name": "ocr_address_city",
        "type": "STRING"
    },
    {
        "name": "ocr_address_state",
        "type": "STRING"
    },
    {
        "name": "ocr_address_zip",
        "type": "STRING"
    },
    {
        "name": "ocr_phone",
        "type": "STRING"
    },
    {
        "name": "manual_decline_reason",
        "type": "STRING"
    },
    {
        "name": "created_at",
        "type": "TIMESTAMP"
    },
    {
        "name": "updated_at",
        "type": "TIMESTAMP"
    }
]
```

### `harmony_export.member_factors`

```json
[
    {
        "name": "member_id",
        "type": "STRING"
    },
    {
        "name": "factor_id",
        "type": "INTEGER"
    },
    {
        "name": "factor_value_id",
        "type": "INTEGER"
    },
    {
        "name": "created_at",
        "type": "TIMESTAMP"
    },
    {
        "name": "source",
        "type": "STRING"
    },
    {
        "name": "metadata",
        "type": "STRING"
    }
]
```

### `harmony_export.members`

```json
[
    {
        "name": "member_id",
        "type": "STRING"
    },
    {
        "name": "sponsor_id",
        "type": "STRING"
    },
    {
        "name": "sponsor_identifier",
        "type": "STRING"
    },
    {
        "name": "processor_identifier",
        "type": "STRING"
    },
    {
        "name": "fis_identifier",
        "type": "INTEGER"
    },
    {
        "name": "last_login",
        "type": "TIMESTAMP"
    },
    {
        "name": "auth0_user_ids",
        "type": "STRING",
        "mode": "REPEATED"
    },
    {
        "name": "created_at",
        "type": "TIMESTAMP"
    },
    {
        "name": "updated_at",
        "type": "TIMESTAMP"
    },
    {
        "name": "deleted_at",
        "type": "TIMESTAMP"
    },
    {
        "name": "spending_paused",
        "type": "TIMESTAMP"
    },
    {
        "name": "is_test_member",
        "type": "BOOLEAN"
    },
    {
        "name": "pending_deactivation_state",
        "type": "STRING"
    },
    {
        "name": "member_state",
        "type": "STRING"
    },
    {
        "name": "sponsor",
        "type": "RECORD",
        "fields": [
            {
                "name": "sponsor_id",
                "type": "STRING"
            },
            {
                "name": "name",
                "type": "STRING"
            },
            {
                "name": "description",
                "type": "STRING"
            },
            {
                "name": "funding_account_identifier",
                "type": "STRING"
            },
            {
                "name": "galileo_product_identifier",
                "type": "INTEGER"
            },
            {
                "name": "emboss_kit_identifier",
                "type": "INTEGER"
            },
            {
                "name": "uber_org_identifier",
                "type": "STRING"
            },
            {
                "name": "created_at",
                "type": "TIMESTAMP"
            }
        ]
    },
    {
        "name": "year_of_birth",
        "type": "INTEGER"
    },
    {
        "name": "language_tag",
        "type": "STRING"
    },
    {
        "name": "does_email_exist",
        "type": "STRING"
    },
    {
        "name": "cms_reporting_gender",
        "type": "STRING"
    },
    {
        "name": "zip_prefix",
        "type": "STRING"
    },
    {
        "name": "us_state",
        "type": "STRING"
    },
    {
        "name": "cards",
        "type": "RECORD",
        "mode": "REPEATED",
        "fields": [
            {
                "name": "id",
                "type": "BYTES"
            },
            {
                "name": "card_id",
                "type": "STRING"
            },
            {
                "name": "member_id",
                "type": "STRING"
            },
            {
                "name": "fis_identifier",
                "type": "INTEGER"
            },
            {
                "name": "galileo_identifier",
                "type": "INTEGER"
            },
            {
                "name": "bin",
                "type": "STRING"
            },
            {
                "name": "last_four",
                "type": "STRING"
            },
            {
                "name": "expires_at",
                "type": "DATE"
            },
            {
                "name": "processor_status",
                "type": "STRING"
            },
            {
                "name": "created_at",
                "type": "TIMESTAMP"
            },
            {
                "name": "updated_at",
                "type": "TIMESTAMP"
            },
            {
                "name": "activated_at",
                "type": "TIMESTAMP"
            },
            {
                "name": "shipped_at",
                "type": "TIMESTAMP"
            },
            {
                "name": "issued_at",
                "type": "TIMESTAMP"
            },
            {
                "name": "deleted_at",
                "type": "TIMESTAMP"
            },
            {
                "name": "emboss_kit_identifier",
                "type": "STRING"
            },
            {
                "name": "status_events",
                "type": "RECORD",
                "mode": "REPEATED",
                "fields": [
                    {
                        "name": "event_type",
                        "type": "STRING"
                    },
                    {
                        "name": "event_source",
                        "type": "STRING"
                    },
                    {
                        "name": "occurred_at",
                        "type": "TIMESTAMP"
                    },
                    {
                        "name": "metadata",
                        "type": "STRING"
                    }
                ]
            }
        ]
    },
    {
        "name": "enrollments",
        "type": "RECORD",
        "mode": "REPEATED",
        "fields": [
            {
                "name": "enrollment_id",
                "type": "STRING"
            },
            {
                "name": "member_id",
                "type": "STRING"
            },
            {
                "name": "benefit_id",
                "type": "STRING"
            },
            {
                "name": "sponsor_identifier",
                "type": "STRING"
            },
            {
                "name": "funding_amount",
                "type": "NUMERIC"
            },
            {
                "name": "active_at",
                "type": "TIMESTAMP"
            },
            {
                "name": "expires_at",
                "type": "TIMESTAMP"
            },
            {
                "name": "created_at",
                "type": "TIMESTAMP"
            },
            {
                "name": "deleted_at",
                "type": "TIMESTAMP"
            },
            {
                "name": "benefit",
                "type": "RECORD",
                "fields": [
                    {
                        "name": "benefit_id",
                        "type": "STRING"
                    },
                    {
                        "name": "sponsor_id",
                        "type": "STRING"
                    },
                    {
                        "name": "type",
                        "type": "STRING"
                    },
                    {
                        "name": "sponsor_identifier",
                        "type": "STRING"
                    },
                    {
                        "name": "name",
                        "type": "STRING"
                    },
                    {
                        "name": "multiple_enrollment",
                        "type": "BOOLEAN"
                    },
                    {
                        "name": "iterations",
                        "type": "INTEGER"
                    },
                    {
                        "name": "interval",
                        "type": "STRING"
                    },
                    {
                        "name": "duration",
                        "type": "STRING"
                    },
                    {
                        "name": "start_date",
                        "type": "TIMESTAMP"
                    },
                    {
                        "name": "calculated_end_date",
                        "type": "TIMESTAMP"
                    },
                    {
                        "name": "created_at",
                        "type": "TIMESTAMP"
                    },
                    {
                        "name": "updated_at",
                        "type": "TIMESTAMP"
                    },
                    {
                        "name": "deleted_at",
                        "type": "TIMESTAMP"
                    },
                    {
                        "name": "funding_amount",
                        "type": "NUMERIC"
                    },
                    {
                        "name": "proration_type",
                        "type": "STRING"
                    },
                    {
                        "name": "priority",
                        "type": "INTEGER"
                    },
                    {
                        "name": "is_variable_amount",
                        "type": "BOOLEAN"
                    },
                    {
                        "name": "amount_on_enrollment",
                        "type": "BOOLEAN"
                    },
                    {
                        "name": "max_cost_per_ride",
                        "type": "NUMERIC"
                    },
                    {
                        "name": "num_one_way_rides",
                        "type": "INTEGER"
                    },
                    {
                        "name": "otchs_benefit_identifier",
                        "type": "STRING"
                    },
                    {
                        "name": "catalog_on_enrollment",
                        "type": "BOOLEAN"
                    }
                ]
            }
        ]
    },
    {
        "name": "program_enrollments",
        "type": "RECORD",
        "mode": "REPEATED",
        "fields": [
            {
                "name": "enrollment_id",
                "type": "STRING"
            },
            {
                "name": "member_id",
                "type": "STRING"
            },
            {
                "name": "program_id",
                "type": "STRING"
            },
            {
                "name": "active_at",
                "type": "TIMESTAMP"
            },
            {
                "name": "expires_at",
                "type": "TIMESTAMP"
            },
            {
                "name": "created_at",
                "type": "TIMESTAMP"
            },
            {
                "name": "deleted_at",
                "type": "TIMESTAMP"
            },
            {
                "name": "program",
                "type": "RECORD",
                "fields": [
                    {
                        "name": "program_id",
                        "type": "STRING"
                    },
                    {
                        "name": "sponsor_identifier",
                        "type": "STRING"
                    },
                    {
                        "name": "plan_year",
                        "type": "STRING"
                    },
                    {
                        "name": "sponsor_id",
                        "type": "STRING"
                    },
                    {
                        "name": "created_at",
                        "type": "TIMESTAMP"
                    },
                    {
                        "name": "deleted_at",
                        "type": "TIMESTAMP"
                    },
                    {
                        "name": "benefit_ids",
                        "type": "STRING",
                        "mode": "REPEATED"
                    }
                ]
            }
        ]
    },
    {
        "name": "catalogs",
        "type": "RECORD",
        "mode": "REPEATED",
        "fields": [
            {
                "name": "id",
                "type": "INTEGER"
            },
            {
                "name": "benefit_id",
                "type": "STRING"
            },
            {
                "name": "source",
                "type": "STRING"
            },
            {
                "name": "created_at",
                "type": "TIMESTAMP"
            },
            {
                "name": "sent_at",
                "type": "TIMESTAMP"
            },
            {
                "name": "catalog_kit_id",
                "type": "STRING"
            },
            {
                "name": "sponsor_id",
                "type": "BYTES"
            }
        ]
    },
    {
        "name": "coupon_enrollments",
        "type": "RECORD",
        "mode": "REPEATED",
        "fields": [
            {
                "name": "coupon_program_enrollment_id",
                "type": "STRING"
            },
            {
                "name": "coupon_program_id",
                "type": "STRING"
            },
            {
                "name": "active_at",
                "type": "TIMESTAMP"
            },
            {
                "name": "expires_at",
                "type": "TIMESTAMP"
            },
            {
                "name": "deleted_at",
                "type": "TIMESTAMP"
            }
        ]
    },
    {
        "name": "disbursement_accounts",
        "type": "RECORD",
        "mode": "REPEATED",
        "fields": [
            {
                "name": "id",
                "type": "INTEGER"
            },
            {
                "name": "member_id",
                "type": "STRING"
            },
            {
                "name": "account_token",
                "type": "STRING"
            },
            {
                "name": "account_type",
                "type": "STRING"
            },
            {
                "name": "account_payee",
                "type": "STRING"
            },
            {
                "name": "last_four",
                "type": "STRING"
            },
            {
                "name": "created_at",
                "type": "TIMESTAMP"
            },
            {
                "name": "updated_at",
                "type": "TIMESTAMP"
            },
            {
                "name": "expires_at",
                "type": "TIMESTAMP"
            },
            {
                "name": "is_active",
                "type": "BOOLEAN"
            },
            {
                "name": "issuing_network",
                "type": "STRING"
            }
        ]
    },
    {
        "name": "member_gaps",
        "type": "RECORD",
        "mode": "REPEATED",
        "fields": [
            {
                "name": "id",
                "type": "STRING"
            },
            {
                "name": "enrollment_id",
                "type": "STRING"
            },
            {
                "name": "closed_at",
                "type": "TIMESTAMP"
            },
            {
                "name": "metadata",
                "type": "STRING"
            },
            {
                "name": "created_at",
                "type": "TIMESTAMP"
            },
            {
                "name": "updated_at",
                "type": "TIMESTAMP"
            },
            {
                "name": "gap_events",
                "type": "RECORD",
                "mode": "REPEATED",
                "fields": [
                    {
                        "name": "status",
                        "type": "STRING"
                    },
                    {
                        "name": "occurred_at",
                        "type": "TIMESTAMP"
                    },
                    {
                        "name": "source",
                        "type": "STRING"
                    },
                    {
                        "name": "pharmacy_name",
                        "type": "STRING"
                    },
                    {
                        "name": "pharmacy_id",
                        "type": "STRING"
                    },
                    {
                        "name": "results",
                        "type": "STRING"
                    }
                ]
            }
        ]
    },
    {
        "name": "member_plan_data",
        "type": "RECORD",
        "mode": "REPEATED",
        "fields": [
            {
                "name": "member_id",
                "type": "STRING"
            },
            {
                "name": "contract_id",
                "type": "STRING"
            },
            {
                "name": "plan_id",
                "type": "STRING"
            },
            {
                "name": "segment_id",
                "type": "STRING"
            }
        ]
    }
]
```

### `harmony_export.members_old_backup`

```json
[
    {
        "name": "member_id",
        "type": "STRING"
    },
    {
        "name": "sponsor_id",
        "type": "STRING"
    },
    {
        "name": "sponsor_identifier",
        "type": "STRING"
    },
    {
        "name": "processor_identifier",
        "type": "STRING"
    },
    {
        "name": "fis_identifier",
        "type": "INTEGER"
    },
    {
        "name": "last_login",
        "type": "TIMESTAMP"
    },
    {
        "name": "auth0_user_ids",
        "type": "STRING",
        "mode": "REPEATED"
    },
    {
        "name": "created_at",
        "type": "TIMESTAMP"
    },
    {
        "name": "updated_at",
        "type": "TIMESTAMP"
    },
    {
        "name": "deleted_at",
        "type": "TIMESTAMP"
    },
    {
        "name": "spending_paused",
        "type": "TIMESTAMP"
    },
    {
        "name": "is_test_member",
        "type": "BOOLEAN"
    },
    {
        "name": "sponsor",
        "type": "RECORD",
        "fields": [
            {
                "name": "sponsor_id",
                "type": "STRING"
            },
            {
                "name": "name",
                "type": "STRING"
            },
            {
                "name": "description",
                "type": "STRING"
            },
            {
                "name": "funding_account_identifier",
                "type": "STRING"
            },
            {
                "name": "galileo_product_identifier",
                "type": "INTEGER"
            },
            {
                "name": "emboss_kit_identifier",
                "type": "INTEGER"
            },
            {
                "name": "uber_org_identifier",
                "type": "STRING"
            },
            {
                "name": "created_at",
                "type": "TIMESTAMP"
            }
        ]
    },
    {
        "name": "year_of_birth",
        "type": "INTEGER"
    },
    {
        "name": "language_tag",
        "type": "STRING"
    },
    {
        "name": "does_email_exist",
        "type": "STRING"
    },
    {
        "name": "zip_prefix",
        "type": "STRING"
    },
    {
        "name": "us_state",
        "type": "STRING"
    },
    {
        "name": "cards",
        "type": "RECORD",
        "mode": "REPEATED",
        "fields": [
            {
                "name": "id",
                "type": "BYTES"
            },
            {
                "name": "card_id",
                "type": "STRING"
            },
            {
                "name": "member_id",
                "type": "STRING"
            },
            {
                "name": "fis_identifier",
                "type": "INTEGER"
            },
            {
                "name": "galileo_identifier",
                "type": "INTEGER"
            },
            {
                "name": "bin",
                "type": "STRING"
            },
            {
                "name": "last_four",
                "type": "STRING"
            },
            {
                "name": "expires_at",
                "type": "DATE"
            },
            {
                "name": "processor_status",
                "type": "STRING"
            },
            {
                "name": "created_at",
                "type": "TIMESTAMP"
            },
            {
                "name": "updated_at",
                "type": "TIMESTAMP"
            },
            {
                "name": "activated_at",
                "type": "TIMESTAMP"
            },
            {
                "name": "shipped_at",
                "type": "TIMESTAMP"
            },
            {
                "name": "issued_at",
                "type": "TIMESTAMP"
            },
            {
                "name": "deleted_at",
                "type": "TIMESTAMP"
            },
            {
                "name": "status_events",
                "type": "RECORD",
                "mode": "REPEATED",
                "fields": [
                    {
                        "name": "event_type",
                        "type": "STRING"
                    },
                    {
                        "name": "event_source",
                        "type": "STRING"
                    },
                    {
                        "name": "occurred_at",
                        "type": "TIMESTAMP"
                    },
                    {
                        "name": "metadata",
                        "type": "STRING"
                    }
                ]
            }
        ]
    },
    {
        "name": "enrollments",
        "type": "RECORD",
        "mode": "REPEATED",
        "fields": [
            {
                "name": "enrollment_id",
                "type": "STRING"
            },
            {
                "name": "member_id",
                "type": "STRING"
            },
            {
                "name": "benefit_id",
                "type": "STRING"
            },
            {
                "name": "sponsor_identifier",
                "type": "STRING"
            },
            {
                "name": "funding_amount",
                "type": "NUMERIC"
            },
            {
                "name": "active_at",
                "type": "TIMESTAMP"
            },
            {
                "name": "expires_at",
                "type": "TIMESTAMP"
            },
            {
                "name": "created_at",
                "type": "TIMESTAMP"
            },
            {
                "name": "deleted_at",
                "type": "TIMESTAMP"
            },
            {
                "name": "benefit",
                "type": "RECORD",
                "fields": [
                    {
                        "name": "benefit_id",
                        "type": "STRING"
                    },
                    {
                        "name": "sponsor_id",
                        "type": "STRING"
                    },
                    {
                        "name": "type",
                        "type": "STRING"
                    },
                    {
                        "name": "sponsor_identifier",
                        "type": "STRING"
                    },
                    {
                        "name": "name",
                        "type": "STRING"
                    },
                    {
                        "name": "multiple_enrollment",
                        "type": "BOOLEAN"
                    },
                    {
                        "name": "iterations",
                        "type": "INTEGER"
                    },
                    {
                        "name": "interval",
                        "type": "STRING"
                    },
                    {
                        "name": "duration",
                        "type": "STRING"
                    },
                    {
                        "name": "start_date",
                        "type": "TIMESTAMP"
                    },
                    {
                        "name": "calculated_end_date",
                        "type": "TIMESTAMP"
                    },
                    {
                        "name": "created_at",
                        "type": "TIMESTAMP"
                    },
                    {
                        "name": "updated_at",
                        "type": "TIMESTAMP"
                    },
                    {
                        "name": "deleted_at",
                        "type": "TIMESTAMP"
                    },
                    {
                        "name": "funding_amount",
                        "type": "NUMERIC"
                    },
                    {
                        "name": "proration_type",
                        "type": "STRING"
                    },
                    {
                        "name": "priority",
                        "type": "INTEGER"
                    },
                    {
                        "name": "is_variable_amount",
                        "type": "BOOLEAN"
                    },
                    {
                        "name": "amount_on_enrollment",
                        "type": "BOOLEAN"
                    },
                    {
                        "name": "max_cost_per_ride",
                        "type": "NUMERIC"
                    },
                    {
                        "name": "num_one_way_rides",
                        "type": "INTEGER"
                    },
                    {
                        "name": "otchs_benefit_identifier",
                        "type": "STRING"
                    },
                    {
                        "name": "catalog_on_enrollment",
                        "type": "BOOLEAN"
                    }
                ]
            }
        ]
    },
    {
        "name": "catalogs",
        "type": "RECORD",
        "mode": "REPEATED",
        "fields": [
            {
                "name": "id",
                "type": "INTEGER"
            },
            {
                "name": "benefit_id",
                "type": "STRING"
            },
            {
                "name": "source",
                "type": "STRING"
            },
            {
                "name": "created_at",
                "type": "TIMESTAMP"
            },
            {
                "name": "sent_at",
                "type": "TIMESTAMP"
            },
            {
                "name": "catalog_kit_id",
                "type": "STRING"
            },
            {
                "name": "sponsor_id",
                "type": "BYTES"
            }
        ]
    },
    {
        "name": "coupon_enrollments",
        "type": "RECORD",
        "mode": "REPEATED",
        "fields": [
            {
                "name": "coupon_program_enrollment_id",
                "type": "STRING"
            },
            {
                "name": "coupon_program_id",
                "type": "STRING"
            },
            {
                "name": "active_at",
                "type": "TIMESTAMP"
            },
            {
                "name": "expires_at",
                "type": "TIMESTAMP"
            },
            {
                "name": "deleted_at",
                "type": "TIMESTAMP"
            }
        ]
    },
    {
        "name": "member_gaps",
        "type": "RECORD",
        "mode": "REPEATED",
        "fields": [
            {
                "name": "id",
                "type": "STRING"
            },
            {
                "name": "enrollment_id",
                "type": "STRING"
            },
            {
                "name": "closed_at",
                "type": "TIMESTAMP"
            },
            {
                "name": "metadata",
                "type": "STRING"
            },
            {
                "name": "created_at",
                "type": "TIMESTAMP"
            },
            {
                "name": "updated_at",
                "type": "TIMESTAMP"
            },
            {
                "name": "gap_events",
                "type": "RECORD",
                "mode": "REPEATED",
                "fields": [
                    {
                        "name": "status",
                        "type": "STRING"
                    },
                    {
                        "name": "occurred_at",
                        "type": "TIMESTAMP"
                    },
                    {
                        "name": "source",
                        "type": "STRING"
                    },
                    {
                        "name": "pharmacy_name",
                        "type": "STRING"
                    },
                    {
                        "name": "pharmacy_id",
                        "type": "STRING"
                    },
                    {
                        "name": "results",
                        "type": "STRING"
                    }
                ]
            }
        ]
    },
    {
        "name": "member_plan_data",
        "type": "RECORD",
        "mode": "REPEATED",
        "fields": [
            {
                "name": "member_id",
                "type": "STRING"
            },
            {
                "name": "contract_id",
                "type": "STRING"
            },
            {
                "name": "plan_id",
                "type": "STRING"
            },
            {
                "name": "segment_id",
                "type": "STRING"
            }
        ]
    }
]
```

### `harmony_export.merchant_category_codes`

```json
[
    {
        "name": "merchant_category_code",
        "type": "INTEGER"
    },
    {
        "name": "edited_description",
        "type": "STRING"
    }
]
```

### `harmony_export.merchant_items`

```json
[
    {
        "name": "merchant_id",
        "type": "STRING"
    },
    {
        "name": "item_id",
        "type": "INTEGER"
    },
    {
        "name": "merchant_identifier",
        "type": "STRING"
    },
    {
        "name": "short_description",
        "type": "STRING"
    },
    {
        "name": "full_description",
        "type": "STRING"
    },
    {
        "name": "created_at",
        "type": "TIMESTAMP"
    },
    {
        "name": "updated_at",
        "type": "TIMESTAMP"
    },
    {
        "name": "deleted_at",
        "type": "TIMESTAMP"
    },
    {
        "name": "gtin",
        "type": "STRING"
    },
    {
        "name": "brand_name",
        "type": "STRING"
    },
    {
        "name": "manufacturer",
        "type": "STRING"
    },
    {
        "name": "plu",
        "type": "INTEGER"
    },
    {
        "name": "size",
        "type": "FLOAT"
    },
    {
        "name": "unit_of_measure",
        "type": "STRING"
    },
    {
        "name": "sku",
        "type": "STRING"
    },
    {
        "name": "reviewed_at",
        "type": "TIMESTAMP"
    },
    {
        "name": "private_brand",
        "type": "BOOLEAN"
    },
    {
        "name": "raw_code",
        "type": "STRING"
    },
    {
        "name": "inactivated_at",
        "type": "TIMESTAMP"
    },
    {
        "name": "atf",
        "type": "BOOLEAN"
    },
    {
        "name": "merchant_item_group_id",
        "type": "INTEGER"
    },
    {
        "name": "merchant",
        "type": "RECORD",
        "fields": [
            {
                "name": "merchant_id",
                "type": "STRING"
            },
            {
                "name": "name",
                "type": "STRING"
            },
            {
                "name": "created_at",
                "type": "TIMESTAMP"
            },
            {
                "name": "updated_at",
                "type": "TIMESTAMP"
            },
            {
                "name": "deleted_at",
                "type": "TIMESTAMP"
            },
            {
                "name": "description",
                "type": "STRING"
            },
            {
                "name": "aggregate_merchant_identifier",
                "type": "INTEGER"
            },
            {
                "name": "preauth_expiration_duration_seconds",
                "type": "INTEGER"
            },
            {
                "name": "config",
                "type": "STRING"
            },
            {
                "name": "integration_live_at",
                "type": "TIMESTAMP"
            },
            {
                "name": "integration_type",
                "type": "STRING"
            }
        ]
    },
    {
        "name": "item",
        "type": "RECORD",
        "fields": [
            {
                "name": "item_id",
                "type": "INTEGER"
            },
            {
                "name": "gtin",
                "type": "STRING"
            },
            {
                "name": "name",
                "type": "STRING"
            },
            {
                "name": "brand_name",
                "type": "STRING"
            },
            {
                "name": "manufacturer",
                "type": "STRING"
            },
            {
                "name": "created_at",
                "type": "TIMESTAMP"
            },
            {
                "name": "updated_at",
                "type": "TIMESTAMP"
            },
            {
                "name": "size",
                "type": "FLOAT"
            },
            {
                "name": "unit_of_measure",
                "type": "STRING"
            },
            {
                "name": "plu",
                "type": "INTEGER"
            }
        ]
    },
    {
        "name": "merchant_item_group",
        "type": "RECORD",
        "fields": [
            {
                "name": "id",
                "type": "INTEGER"
            },
            {
                "name": "merchant_id",
                "type": "STRING"
            },
            {
                "name": "merchant_group_identifier",
                "type": "STRING"
            },
            {
                "name": "created_at",
                "type": "TIMESTAMP"
            },
            {
                "name": "updated_at",
                "type": "TIMESTAMP"
            },
            {
                "name": "deleted_at",
                "type": "TIMESTAMP"
            },
            {
                "name": "h1",
                "type": "STRING"
            },
            {
                "name": "h2",
                "type": "STRING"
            },
            {
                "name": "h3",
                "type": "STRING"
            },
            {
                "name": "h4",
                "type": "STRING"
            },
            {
                "name": "h5",
                "type": "STRING"
            }
        ]
    }
]
```

### `harmony_export.merchant_preauth_transaction_event`

```json
[
    {
        "name": "id",
        "type": "BYTES"
    },
    {
        "name": "sponsor_id",
        "type": "STRING"
    },
    {
        "name": "member_id",
        "type": "STRING"
    },
    {
        "name": "merchant_id",
        "type": "STRING"
    },
    {
        "name": "merchant_name",
        "type": "STRING"
    },
    {
        "name": "prelim_type",
        "type": "STRING"
    },
    {
        "name": "request",
        "type": "STRING"
    },
    {
        "name": "response",
        "type": "STRING"
    },
    {
        "name": "metadata",
        "type": "STRING"
    },
    {
        "name": "created_at",
        "type": "TIMESTAMP"
    },
    {
        "name": "occurred_at",
        "type": "TIMESTAMP"
    },
    {
        "name": "amount_requested",
        "type": "NUMERIC"
    },
    {
        "name": "amount_approved",
        "type": "NUMERIC"
    },
    {
        "name": "preliminary_transaction_id",
        "type": "INTEGER"
    },
    {
        "name": "merchant_transaction_identifier",
        "type": "STRING"
    },
    {
        "name": "card_id",
        "type": "BYTES"
    },
    {
        "name": "group_key",
        "type": "BYTES"
    },
    {
        "name": "reason",
        "type": "STRING"
    },
    {
        "name": "member",
        "type": "RECORD",
        "fields": [
            {
                "name": "member_id",
                "type": "STRING"
            },
            {
                "name": "sponsor_id",
                "type": "STRING"
            },
            {
                "name": "sponsor_identifier",
                "type": "STRING"
            },
            {
                "name": "processor_identifier",
                "type": "STRING"
            },
            {
                "name": "fis_identifier",
                "type": "INTEGER"
            },
            {
                "name": "e6_customer_number",
                "type": "STRING"
            },
            {
                "name": "last_login",
                "type": "TIMESTAMP"
            },
            {
                "name": "auth0_user_ids",
                "type": "STRING",
                "mode": "REPEATED"
            },
            {
                "name": "created_at",
                "type": "TIMESTAMP"
            },
            {
                "name": "updated_at",
                "type": "TIMESTAMP"
            },
            {
                "name": "deleted_at",
                "type": "TIMESTAMP"
            },
            {
                "name": "spending_paused",
                "type": "TIMESTAMP"
            },
            {
                "name": "is_test_member",
                "type": "BOOLEAN"
            },
            {
                "name": "pending_deactivation_state",
                "type": "STRING"
            }
        ]
    },
    {
        "name": "sponsor",
        "type": "RECORD",
        "fields": [
            {
                "name": "sponsor_id",
                "type": "STRING"
            },
            {
                "name": "name",
                "type": "STRING"
            },
            {
                "name": "description",
                "type": "STRING"
            },
            {
                "name": "config",
                "type": "STRING"
            },
            {
                "name": "funding_account_identifier",
                "type": "STRING"
            },
            {
                "name": "galileo_product_identifier",
                "type": "INTEGER"
            },
            {
                "name": "emboss_kit_identifier",
                "type": "INTEGER"
            },
            {
                "name": "uber_org_identifier",
                "type": "STRING"
            },
            {
                "name": "created_at",
                "type": "TIMESTAMP"
            },
            {
                "name": "variant",
                "type": "STRING"
            },
            {
                "name": "parent_id",
                "type": "STRING"
            }
        ]
    },
    {
        "name": "merchant",
        "type": "RECORD",
        "fields": [
            {
                "name": "merchant_id",
                "type": "STRING"
            },
            {
                "name": "name",
                "type": "STRING"
            },
            {
                "name": "created_at",
                "type": "TIMESTAMP"
            },
            {
                "name": "updated_at",
                "type": "TIMESTAMP"
            },
            {
                "name": "deleted_at",
                "type": "TIMESTAMP"
            },
            {
                "name": "description",
                "type": "STRING"
            },
            {
                "name": "aggregate_merchant_identifier",
                "type": "INTEGER"
            },
            {
                "name": "preauth_expiration_duration_seconds",
                "type": "INTEGER"
            },
            {
                "name": "config",
                "type": "STRING"
            },
            {
                "name": "integration_live_at",
                "type": "TIMESTAMP"
            },
            {
                "name": "integration_type",
                "type": "STRING"
            }
        ]
    }
]
```

### `harmony_export.partners`

```json
[
    {
        "name": "id",
        "type": "STRING"
    },
    {
        "name": "name",
        "type": "STRING"
    },
    {
        "name": "bucket_name",
        "type": "STRING"
    },
    {
        "name": "partner_type",
        "type": "STRING"
    },
    {
        "name": "short_code",
        "type": "STRING"
    },
    {
        "name": "config",
        "type": "STRING"
    },
    {
        "name": "created_at",
        "type": "TIMESTAMP"
    }
]
```

### `harmony_export.preliminary_transactions`

```json
[
    {
        "name": "preliminary_transaction_id",
        "type": "INTEGER"
    },
    {
        "name": "terminal_identifier",
        "type": "STRING"
    },
    {
        "name": "merchant_transaction_identifier",
        "type": "STRING"
    },
    {
        "name": "amount",
        "type": "NUMERIC"
    },
    {
        "name": "effective_date",
        "type": "TIMESTAMP"
    },
    {
        "name": "created_at",
        "type": "TIMESTAMP"
    },
    {
        "name": "metadata",
        "type": "STRING"
    },
    {
        "name": "transaction_id",
        "type": "INTEGER"
    },
    {
        "name": "expires_at",
        "type": "TIMESTAMP"
    },
    {
        "name": "group_key",
        "type": "BYTES"
    },
    {
        "name": "merchant_id",
        "type": "STRING"
    },
    {
        "name": "prelim_type",
        "type": "STRING"
    },
    {
        "name": "member_id",
        "type": "STRING"
    },
    {
        "name": "sponsor_id",
        "type": "STRING"
    },
    {
        "name": "basket_items",
        "type": "RECORD",
        "mode": "REPEATED",
        "fields": [
            {
                "name": "basket_item_id",
                "type": "INTEGER"
            },
            {
                "name": "amount_requested",
                "type": "NUMERIC"
            },
            {
                "name": "matched_core_categories",
                "type": "STRING",
                "mode": "REPEATED"
            },
            {
                "name": "sponsor_id",
                "type": "STRING"
            },
            {
                "name": "item_code",
                "type": "STRING"
            },
            {
                "name": "item_code_type",
                "type": "STRING"
            },
            {
                "name": "preliminary_transaction_id",
                "type": "INTEGER"
            },
            {
                "name": "reference_number",
                "type": "INTEGER"
            },
            {
                "name": "quantity",
                "type": "NUMERIC"
            },
            {
                "name": "eligible",
                "type": "BOOLEAN"
            },
            {
                "name": "merchant_description",
                "type": "STRING"
            },
            {
                "name": "quantity_type",
                "type": "STRING"
            },
            {
                "name": "core_category_sources",
                "type": "STRING"
            }
        ]
    },
    {
        "name": "benefit_items",
        "type": "RECORD",
        "mode": "REPEATED",
        "fields": [
            {
                "name": "benefit_item_id",
                "type": "INTEGER"
            },
            {
                "name": "preliminary_transaction_id",
                "type": "INTEGER"
            },
            {
                "name": "enrollment_book_id",
                "type": "INTEGER"
            },
            {
                "name": "amount_approved",
                "type": "NUMERIC"
            },
            {
                "name": "item_code",
                "type": "STRING"
            },
            {
                "name": "item_code_type",
                "type": "STRING"
            },
            {
                "name": "priority",
                "type": "INTEGER"
            },
            {
                "name": "reference_number",
                "type": "INTEGER"
            },
            {
                "name": "benefit_id",
                "type": "STRING"
            }
        ]
    }
]
```

### `harmony_export.reimbursements`

```json
[
    {
        "name": "reimbursement_id",
        "type": "STRING"
    },
    {
        "name": "type",
        "type": "STRING"
    },
    {
        "name": "current_status",
        "type": "STRING"
    },
    {
        "name": "source",
        "type": "STRING"
    },
    {
        "name": "member_id",
        "type": "STRING"
    },
    {
        "name": "program_id",
        "type": "STRING"
    },
    {
        "name": "lease_id",
        "type": "STRING"
    },
    {
        "name": "transaction_id",
        "type": "INTEGER"
    },
    {
        "name": "preliminary_transaction_id",
        "type": "INTEGER"
    },
    {
        "name": "created_at",
        "type": "TIMESTAMP"
    },
    {
        "name": "updated_at",
        "type": "TIMESTAMP"
    },
    {
        "name": "original_purchase_date",
        "type": "TIMESTAMP"
    },
    {
        "name": "expected_disbursement_date",
        "type": "TIMESTAMP"
    },
    {
        "name": "actual_disbursement_date",
        "type": "TIMESTAMP"
    },
    {
        "name": "manually_reviewed",
        "type": "BOOLEAN"
    },
    {
        "name": "manual_decline_reason",
        "type": "STRING"
    },
    {
        "name": "decline_code",
        "type": "STRING"
    },
    {
        "name": "ocr_run_identifier",
        "type": "STRING"
    },
    {
        "name": "disbursement_payment_token",
        "type": "STRING"
    },
    {
        "name": "disbursement_identifier",
        "type": "STRING"
    },
    {
        "name": "ocr_output",
        "type": "STRING"
    },
    {
        "name": "checks",
        "type": "RECORD",
        "mode": "REPEATED",
        "fields": [
            {
                "name": "check_id",
                "type": "STRING"
            },
            {
                "name": "check_number",
                "type": "STRING"
            },
            {
                "name": "check_amount",
                "type": "NUMERIC"
            },
            {
                "name": "check_status",
                "type": "STRING"
            },
            {
                "name": "check_reason_code",
                "type": "STRING"
            },
            {
                "name": "check_created_at",
                "type": "TIMESTAMP"
            },
            {
                "name": "check_updated_at",
                "type": "TIMESTAMP"
            }
        ]
    },
    {
        "name": "denial_letters",
        "type": "RECORD",
        "mode": "REPEATED",
        "fields": [
            {
                "name": "denial_letter_id",
                "type": "STRING"
            },
            {
                "name": "lob_id",
                "type": "STRING"
            },
            {
                "name": "letter_status",
                "type": "STRING"
            },
            {
                "name": "letter_template_id",
                "type": "STRING"
            },
            {
                "name": "letter_expected_delivery",
                "type": "TIMESTAMP"
            },
            {
                "name": "letter_created_at",
                "type": "TIMESTAMP"
            },
            {
                "name": "letter_updated_at",
                "type": "TIMESTAMP"
            }
        ]
    },
    {
        "name": "status_history",
        "type": "RECORD",
        "mode": "REPEATED",
        "fields": [
            {
                "name": "status",
                "type": "STRING"
            },
            {
                "name": "as_of",
                "type": "TIMESTAMP"
            }
        ]
    },
    {
        "name": "sponsor_info",
        "type": "RECORD",
        "fields": [
            {
                "name": "sponsor_id",
                "type": "STRING"
            },
            {
                "name": "name",
                "type": "STRING"
            },
            {
                "name": "variant",
                "type": "STRING"
            },
            {
                "name": "parent_id",
                "type": "STRING"
            },
            {
                "name": "customer_sponsor_id",
                "type": "STRING"
            },
            {
                "name": "customer_name",
                "type": "STRING"
            },
            {
                "name": "customer_description",
                "type": "STRING"
            }
        ]
    }
]
```

### `harmony_export.rides`

```json
[
    {
        "name": "ride_id",
        "type": "STRING"
    },
    {
        "name": "member_id",
        "type": "STRING"
    },
    {
        "name": "enrollment_id",
        "type": "STRING"
    },
    {
        "name": "type",
        "type": "STRING"
    },
    {
        "name": "occurred_at",
        "type": "TIMESTAMP"
    },
    {
        "name": "trip_request_identifier",
        "type": "STRING"
    },
    {
        "name": "transaction_id",
        "type": "STRING"
    },
    {
        "name": "created_at",
        "type": "TIMESTAMP"
    },
    {
        "name": "etaminutes",
        "type": "INTEGER"
    },
    {
        "name": "fare",
        "type": "STRING"
    },
    {
        "name": "uberproduct",
        "type": "STRING"
    },
    {
        "name": "ridebalanceexpiration",
        "type": "TIMESTAMP"
    },
    {
        "name": "returnridebalanceexpiration",
        "type": "TIMESTAMP"
    },
    {
        "name": "bookedflexiblereturn",
        "type": "BOOLEAN"
    },
    {
        "name": "uberlanguage",
        "type": "STRING"
    },
    {
        "name": "eta",
        "type": "INTEGER"
    },
    {
        "name": "ismobilephone",
        "type": "BOOLEAN"
    },
    {
        "name": "unsubscribedfromsms",
        "type": "BOOLEAN"
    },
    {
        "name": "sponsor_id",
        "type": "STRING"
    },
    {
        "name": "member",
        "type": "RECORD",
        "fields": [
            {
                "name": "member_id",
                "type": "STRING"
            },
            {
                "name": "sponsor_id",
                "type": "STRING"
            },
            {
                "name": "sponsor_identifier",
                "type": "STRING"
            },
            {
                "name": "processor_identifier",
                "type": "STRING"
            },
            {
                "name": "fis_identifier",
                "type": "INTEGER"
            },
            {
                "name": "e6_customer_number",
                "type": "STRING"
            },
            {
                "name": "last_login",
                "type": "TIMESTAMP"
            },
            {
                "name": "auth0_user_ids",
                "type": "STRING",
                "mode": "REPEATED"
            },
            {
                "name": "created_at",
                "type": "TIMESTAMP"
            },
            {
                "name": "updated_at",
                "type": "TIMESTAMP"
            },
            {
                "name": "deleted_at",
                "type": "TIMESTAMP"
            },
            {
                "name": "spending_paused",
                "type": "TIMESTAMP"
            },
            {
                "name": "is_test_member",
                "type": "BOOLEAN"
            },
            {
                "name": "pending_deactivation_state",
                "type": "STRING"
            }
        ]
    },
    {
        "name": "sponsor",
        "type": "RECORD",
        "fields": [
            {
                "name": "sponsor_id",
                "type": "STRING"
            },
            {
                "name": "name",
                "type": "STRING"
            },
            {
                "name": "description",
                "type": "STRING"
            },
            {
                "name": "config",
                "type": "STRING"
            },
            {
                "name": "funding_account_identifier",
                "type": "STRING"
            },
            {
                "name": "galileo_product_identifier",
                "type": "INTEGER"
            },
            {
                "name": "emboss_kit_identifier",
                "type": "INTEGER"
            },
            {
                "name": "uber_org_identifier",
                "type": "STRING"
            },
            {
                "name": "created_at",
                "type": "TIMESTAMP"
            },
            {
                "name": "variant",
                "type": "STRING"
            },
            {
                "name": "parent_id",
                "type": "STRING"
            }
        ]
    },
    {
        "name": "enrollment",
        "type": "RECORD",
        "fields": [
            {
                "name": "enrollment_id",
                "type": "STRING"
            },
            {
                "name": "member_id",
                "type": "STRING"
            },
            {
                "name": "benefit_id",
                "type": "STRING"
            },
            {
                "name": "sponsor_identifier",
                "type": "STRING"
            },
            {
                "name": "funding_amount",
                "type": "NUMERIC"
            },
            {
                "name": "active_at",
                "type": "TIMESTAMP"
            },
            {
                "name": "expires_at",
                "type": "TIMESTAMP"
            },
            {
                "name": "created_at",
                "type": "TIMESTAMP"
            },
            {
                "name": "deleted_at",
                "type": "TIMESTAMP"
            },
            {
                "name": "program_enrollment_id",
                "type": "STRING"
            }
        ]
    },
    {
        "name": "benefit",
        "type": "RECORD",
        "fields": [
            {
                "name": "benefit_id",
                "type": "STRING"
            },
            {
                "name": "sponsor_id",
                "type": "STRING"
            },
            {
                "name": "type",
                "type": "STRING"
            },
            {
                "name": "sponsor_identifier",
                "type": "STRING"
            },
            {
                "name": "name",
                "type": "STRING"
            },
            {
                "name": "multiple_enrollment",
                "type": "BOOLEAN"
            },
            {
                "name": "iterations",
                "type": "INTEGER"
            },
            {
                "name": "interval",
                "type": "STRING"
            },
            {
                "name": "duration",
                "type": "STRING"
            },
            {
                "name": "start_date",
                "type": "TIMESTAMP"
            },
            {
                "name": "calculated_end_date",
                "type": "TIMESTAMP"
            },
            {
                "name": "created_at",
                "type": "TIMESTAMP"
            },
            {
                "name": "updated_at",
                "type": "TIMESTAMP"
            },
            {
                "name": "deleted_at",
                "type": "TIMESTAMP"
            },
            {
                "name": "funding_amount",
                "type": "NUMERIC"
            },
            {
                "name": "proration_type",
                "type": "STRING"
            },
            {
                "name": "priority",
                "type": "INTEGER"
            },
            {
                "name": "is_variable_amount",
                "type": "BOOLEAN"
            },
            {
                "name": "amount_on_enrollment",
                "type": "BOOLEAN"
            },
            {
                "name": "max_cost_per_ride",
                "type": "NUMERIC"
            },
            {
                "name": "num_one_way_rides",
                "type": "INTEGER"
            },
            {
                "name": "otchs_benefit_identifier",
                "type": "STRING"
            },
            {
                "name": "catalog_on_enrollment",
                "type": "BOOLEAN"
            }
        ]
    }
]
```

### `harmony_export.settlement_transfer_summary`

```json
[
    {
        "name": "source_bank_account_identifier",
        "type": "STRING"
    },
    {
        "name": "destination_bank_account_identifier",
        "type": "STRING"
    },
    {
        "name": "transferred_at",
        "type": "TIMESTAMP"
    },
    {
        "name": "number_of_transactions",
        "type": "INTEGER"
    },
    {
        "name": "total_amount",
        "type": "NUMERIC"
    },
    {
        "name": "earliest_created_at",
        "type": "TIMESTAMP"
    },
    {
        "name": "latest_created_at",
        "type": "TIMESTAMP"
    }
]
```

### `harmony_export.sponsor_configs`

```json
[
    {
        "name": "sponsor_id",
        "type": "STRING"
    },
    {
        "name": "name",
        "type": "STRING"
    },
    {
        "name": "description",
        "type": "STRING"
    },
    {
        "name": "created_at",
        "type": "TIMESTAMP"
    },
    {
        "name": "uber_org_identifier",
        "type": "STRING"
    },
    {
        "name": "use_intelligent_kit_assignment",
        "type": "BOOLEAN"
    },
    {
        "name": "fis_subprogram_id",
        "type": "INTEGER"
    },
    {
        "name": "fis_package_id",
        "type": "INTEGER"
    },
    {
        "name": "fis_apl_id",
        "type": "STRING"
    },
    {
        "name": "fis_prin",
        "type": "STRING"
    },
    {
        "name": "fis_account_dan",
        "type": "STRING"
    },
    {
        "name": "fis_waterline",
        "type": "NUMERIC"
    },
    {
        "name": "galileo_funding_account_prn",
        "type": "STRING"
    },
    {
        "name": "galileo_product_identifier",
        "type": "INTEGER"
    },
    {
        "name": "galileo_emboss_kit_identifier",
        "type": "INTEGER"
    },
    {
        "name": "otc_providers",
        "type": "STRING"
    },
    {
        "name": "variant",
        "type": "STRING"
    },
    {
        "name": "parent_id",
        "type": "STRING"
    }
]
```

### `harmony_export.sponsor_funding_account`

```json
[
    {
        "name": "sponsor_id",
        "type": "STRING"
    },
    {
        "name": "name",
        "type": "STRING"
    },
    {
        "name": "processor_identifier",
        "type": "STRING"
    },
    {
        "name": "as_of",
        "type": "TIMESTAMP"
    },
    {
        "name": "balance",
        "type": "NUMERIC"
    },
    {
        "name": "warning_balance",
        "type": "NUMERIC"
    },
    {
        "name": "cutoff_balance",
        "type": "NUMERIC"
    }
]
```

### `harmony_export.sponsor_funding_account-2025-07-23T13_25_23`

```json
[
    {
        "name": "sponsor_id",
        "type": "STRING"
    },
    {
        "name": "name",
        "type": "STRING"
    },
    {
        "name": "processor_identifier",
        "type": "STRING"
    },
    {
        "name": "as_of",
        "type": "TIMESTAMP"
    },
    {
        "name": "balance",
        "type": "NUMERIC"
    },
    {
        "name": "warning_balance",
        "type": "NUMERIC"
    },
    {
        "name": "cutoff_balance",
        "type": "NUMERIC"
    }
]
```

### `harmony_export.sponsors`

```json
[
    {
        "name": "sponsor_id",
        "type": "STRING"
    },
    {
        "name": "name",
        "type": "STRING"
    },
    {
        "name": "description",
        "type": "STRING"
    },
    {
        "name": "variant",
        "type": "STRING"
    },
    {
        "name": "parent_id",
        "type": "STRING"
    },
    {
        "name": "funding_account_identifier",
        "type": "STRING"
    },
    {
        "name": "galileo_product_identifier",
        "type": "INTEGER"
    },
    {
        "name": "emboss_kit_identifier",
        "type": "INTEGER"
    },
    {
        "name": "uber_org_identifier",
        "type": "STRING"
    },
    {
        "name": "created_at",
        "type": "TIMESTAMP"
    },
    {
        "name": "config",
        "type": "JSON"
    },
    {
        "name": "customer_sponsor_id",
        "type": "STRING"
    },
    {
        "name": "customer_name",
        "type": "STRING"
    },
    {
        "name": "customer_description",
        "type": "STRING"
    },
    {
        "name": "resolved_customer_id",
        "type": "STRING"
    },
    {
        "name": "resolved_customer_name",
        "type": "STRING"
    }
]
```

### `harmony_export.standardized_transaction`

```json
[
    {
        "name": "standardized_transaction_id",
        "type": "STRING"
    },
    {
        "name": "sequence_id",
        "type": "STRING"
    },
    {
        "name": "member_id",
        "type": "STRING"
    },
    {
        "name": "sponsor_id",
        "type": "STRING"
    },
    {
        "name": "card_id",
        "type": "STRING"
    },
    {
        "name": "merchant_id",
        "type": "STRING"
    },
    {
        "name": "merchant_description",
        "type": "STRING"
    },
    {
        "name": "reason",
        "type": "STRING"
    },
    {
        "name": "transaction_id",
        "type": "INTEGER"
    },
    {
        "name": "prelim_transaction_id",
        "type": "INTEGER"
    },
    {
        "name": "approved",
        "type": "BOOLEAN"
    },
    {
        "name": "spending",
        "type": "BOOLEAN"
    },
    {
        "name": "state",
        "type": "STRING"
    },
    {
        "name": "amount_requested",
        "type": "NUMERIC"
    },
    {
        "name": "amount_approved",
        "type": "NUMERIC"
    },
    {
        "name": "sources",
        "type": "STRING",
        "mode": "REPEATED"
    },
    {
        "name": "occurred_at",
        "type": "TIMESTAMP"
    },
    {
        "name": "reversed_at",
        "type": "TIMESTAMP"
    },
    {
        "name": "settled_at",
        "type": "TIMESTAMP"
    },
    {
        "name": "created_at",
        "type": "TIMESTAMP"
    },
    {
        "name": "member",
        "type": "RECORD",
        "fields": [
            {
                "name": "member_id",
                "type": "STRING"
            },
            {
                "name": "sponsor_id",
                "type": "STRING"
            },
            {
                "name": "sponsor_identifier",
                "type": "STRING"
            },
            {
                "name": "processor_identifier",
                "type": "STRING"
            },
            {
                "name": "fis_identifier",
                "type": "INTEGER"
            },
            {
                "name": "e6_customer_number",
                "type": "STRING"
            },
            {
                "name": "last_login",
                "type": "TIMESTAMP"
            },
            {
                "name": "auth0_user_ids",
                "type": "STRING",
                "mode": "REPEATED"
            },
            {
                "name": "created_at",
                "type": "TIMESTAMP"
            },
            {
                "name": "updated_at",
                "type": "TIMESTAMP"
            },
            {
                "name": "deleted_at",
                "type": "TIMESTAMP"
            },
            {
                "name": "spending_paused",
                "type": "TIMESTAMP"
            },
            {
                "name": "is_test_member",
                "type": "BOOLEAN"
            },
            {
                "name": "pending_deactivation_state",
                "type": "STRING"
            }
        ]
    },
    {
        "name": "sponsor",
        "type": "RECORD",
        "fields": [
            {
                "name": "sponsor_id",
                "type": "STRING"
            },
            {
                "name": "name",
                "type": "STRING"
            },
            {
                "name": "description",
                "type": "STRING"
            },
            {
                "name": "config",
                "type": "STRING"
            },
            {
                "name": "funding_account_identifier",
                "type": "STRING"
            },
            {
                "name": "galileo_product_identifier",
                "type": "INTEGER"
            },
            {
                "name": "emboss_kit_identifier",
                "type": "INTEGER"
            },
            {
                "name": "uber_org_identifier",
                "type": "STRING"
            },
            {
                "name": "created_at",
                "type": "TIMESTAMP"
            },
            {
                "name": "variant",
                "type": "STRING"
            },
            {
                "name": "parent_id",
                "type": "STRING"
            }
        ]
    },
    {
        "name": "soda_transaction",
        "type": "RECORD",
        "fields": [
            {
                "name": "id",
                "type": "INTEGER"
            },
            {
                "name": "payee",
                "type": "STRING"
            },
            {
                "name": "effective_date",
                "type": "TIMESTAMP"
            },
            {
                "name": "created_at",
                "type": "TIMESTAMP"
            },
            {
                "name": "transaction_type",
                "type": "STRING"
            },
            {
                "name": "mcc",
                "type": "STRING"
            },
            {
                "name": "mid",
                "type": "STRING"
            },
            {
                "name": "transaction_metadata",
                "type": "STRING"
            },
            {
                "name": "transaction_source",
                "type": "STRING"
            },
            {
                "name": "reversal_id",
                "type": "INTEGER"
            }
        ]
    }
]
```

### `harmony_export.standardized_transaction_benefit_spend`

```json
[
    {
        "name": "standardized_transaction_id",
        "type": "STRING"
    },
    {
        "name": "benefit_id",
        "type": "STRING"
    },
    {
        "name": "amount",
        "type": "NUMERIC"
    },
    {
        "name": "created_at",
        "type": "TIMESTAMP"
    },
    {
        "name": "benefit",
        "type": "RECORD",
        "fields": [
            {
                "name": "benefit_id",
                "type": "STRING"
            },
            {
                "name": "sponsor_id",
                "type": "STRING"
            },
            {
                "name": "type",
                "type": "STRING"
            },
            {
                "name": "sponsor_identifier",
                "type": "STRING"
            },
            {
                "name": "name",
                "type": "STRING"
            },
            {
                "name": "multiple_enrollment",
                "type": "BOOLEAN"
            },
            {
                "name": "iterations",
                "type": "INTEGER"
            },
            {
                "name": "interval",
                "type": "STRING"
            },
            {
                "name": "duration",
                "type": "STRING"
            },
            {
                "name": "start_date",
                "type": "TIMESTAMP"
            },
            {
                "name": "calculated_end_date",
                "type": "TIMESTAMP"
            },
            {
                "name": "created_at",
                "type": "TIMESTAMP"
            },
            {
                "name": "updated_at",
                "type": "TIMESTAMP"
            },
            {
                "name": "deleted_at",
                "type": "TIMESTAMP"
            },
            {
                "name": "funding_amount",
                "type": "NUMERIC"
            },
            {
                "name": "proration_type",
                "type": "STRING"
            },
            {
                "name": "priority",
                "type": "INTEGER"
            },
            {
                "name": "is_variable_amount",
                "type": "BOOLEAN"
            },
            {
                "name": "amount_on_enrollment",
                "type": "BOOLEAN"
            },
            {
                "name": "max_cost_per_ride",
                "type": "NUMERIC"
            },
            {
                "name": "num_one_way_rides",
                "type": "INTEGER"
            },
            {
                "name": "otchs_benefit_identifier",
                "type": "STRING"
            },
            {
                "name": "catalog_on_enrollment",
                "type": "BOOLEAN"
            }
        ]
    }
]
```

### `harmony_export.surveys`

```json
[
    {
        "name": "survey_response_id",
        "type": "STRING"
    },
    {
        "name": "enrollment_id",
        "type": "STRING"
    },
    {
        "name": "benefit_id",
        "type": "STRING"
    },
    {
        "name": "member_id",
        "type": "STRING"
    },
    {
        "name": "sponsor_id",
        "type": "STRING"
    },
    {
        "name": "created_at",
        "type": "TIMESTAMP"
    },
    {
        "name": "question_count",
        "type": "INTEGER"
    },
    {
        "name": "response_json",
        "type": "STRING"
    },
    {
        "name": "member",
        "type": "RECORD",
        "fields": [
            {
                "name": "member_id",
                "type": "STRING"
            },
            {
                "name": "sponsor_id",
                "type": "STRING"
            },
            {
                "name": "sponsor_identifier",
                "type": "STRING"
            },
            {
                "name": "processor_identifier",
                "type": "STRING"
            },
            {
                "name": "fis_identifier",
                "type": "INTEGER"
            },
            {
                "name": "e6_customer_number",
                "type": "STRING"
            },
            {
                "name": "last_login",
                "type": "TIMESTAMP"
            },
            {
                "name": "auth0_user_ids",
                "type": "STRING",
                "mode": "REPEATED"
            },
            {
                "name": "created_at",
                "type": "TIMESTAMP"
            },
            {
                "name": "updated_at",
                "type": "TIMESTAMP"
            },
            {
                "name": "deleted_at",
                "type": "TIMESTAMP"
            },
            {
                "name": "spending_paused",
                "type": "TIMESTAMP"
            },
            {
                "name": "is_test_member",
                "type": "BOOLEAN"
            },
            {
                "name": "pending_deactivation_state",
                "type": "STRING"
            }
        ]
    },
    {
        "name": "sponsor",
        "type": "RECORD",
        "fields": [
            {
                "name": "sponsor_id",
                "type": "STRING"
            },
            {
                "name": "name",
                "type": "STRING"
            },
            {
                "name": "description",
                "type": "STRING"
            },
            {
                "name": "config",
                "type": "STRING"
            },
            {
                "name": "funding_account_identifier",
                "type": "STRING"
            },
            {
                "name": "galileo_product_identifier",
                "type": "INTEGER"
            },
            {
                "name": "emboss_kit_identifier",
                "type": "INTEGER"
            },
            {
                "name": "uber_org_identifier",
                "type": "STRING"
            },
            {
                "name": "created_at",
                "type": "TIMESTAMP"
            },
            {
                "name": "variant",
                "type": "STRING"
            },
            {
                "name": "parent_id",
                "type": "STRING"
            }
        ]
    },
    {
        "name": "enrollment",
        "type": "RECORD",
        "fields": [
            {
                "name": "enrollment_id",
                "type": "STRING"
            },
            {
                "name": "member_id",
                "type": "STRING"
            },
            {
                "name": "benefit_id",
                "type": "STRING"
            },
            {
                "name": "sponsor_identifier",
                "type": "STRING"
            },
            {
                "name": "funding_amount",
                "type": "NUMERIC"
            },
            {
                "name": "active_at",
                "type": "TIMESTAMP"
            },
            {
                "name": "expires_at",
                "type": "TIMESTAMP"
            },
            {
                "name": "created_at",
                "type": "TIMESTAMP"
            },
            {
                "name": "deleted_at",
                "type": "TIMESTAMP"
            },
            {
                "name": "program_enrollment_id",
                "type": "STRING"
            }
        ]
    },
    {
        "name": "benefit",
        "type": "RECORD",
        "fields": [
            {
                "name": "benefit_id",
                "type": "STRING"
            },
            {
                "name": "sponsor_id",
                "type": "STRING"
            },
            {
                "name": "type",
                "type": "STRING"
            },
            {
                "name": "sponsor_identifier",
                "type": "STRING"
            },
            {
                "name": "name",
                "type": "STRING"
            },
            {
                "name": "multiple_enrollment",
                "type": "BOOLEAN"
            },
            {
                "name": "iterations",
                "type": "INTEGER"
            },
            {
                "name": "interval",
                "type": "STRING"
            },
            {
                "name": "duration",
                "type": "STRING"
            },
            {
                "name": "start_date",
                "type": "TIMESTAMP"
            },
            {
                "name": "calculated_end_date",
                "type": "TIMESTAMP"
            },
            {
                "name": "created_at",
                "type": "TIMESTAMP"
            },
            {
                "name": "updated_at",
                "type": "TIMESTAMP"
            },
            {
                "name": "deleted_at",
                "type": "TIMESTAMP"
            },
            {
                "name": "funding_amount",
                "type": "NUMERIC"
            },
            {
                "name": "proration_type",
                "type": "STRING"
            },
            {
                "name": "priority",
                "type": "INTEGER"
            },
            {
                "name": "is_variable_amount",
                "type": "BOOLEAN"
            },
            {
                "name": "amount_on_enrollment",
                "type": "BOOLEAN"
            },
            {
                "name": "max_cost_per_ride",
                "type": "NUMERIC"
            },
            {
                "name": "num_one_way_rides",
                "type": "INTEGER"
            },
            {
                "name": "otchs_benefit_identifier",
                "type": "STRING"
            },
            {
                "name": "catalog_on_enrollment",
                "type": "BOOLEAN"
            }
        ]
    }
]
```

### `harmony_export.transaction_events`

```json
[
    {
        "name": "transaction_event_id",
        "type": "STRING"
    },
    {
        "name": "member_id",
        "type": "STRING"
    },
    {
        "name": "sponsor_id",
        "type": "STRING"
    },
    {
        "name": "event_type",
        "type": "STRING"
    },
    {
        "name": "event_subtype",
        "type": "STRING"
    },
    {
        "name": "reason",
        "type": "STRING"
    },
    {
        "name": "transaction_id",
        "type": "INTEGER"
    },
    {
        "name": "auth_id",
        "type": "INTEGER"
    },
    {
        "name": "network",
        "type": "STRING"
    },
    {
        "name": "body",
        "type": "STRING"
    },
    {
        "name": "response",
        "type": "STRING"
    },
    {
        "name": "metadata",
        "type": "STRING"
    },
    {
        "name": "occurred_at",
        "type": "TIMESTAMP"
    },
    {
        "name": "created_at",
        "type": "TIMESTAMP"
    },
    {
        "name": "member",
        "type": "RECORD",
        "fields": [
            {
                "name": "member_id",
                "type": "STRING"
            },
            {
                "name": "sponsor_id",
                "type": "STRING"
            },
            {
                "name": "sponsor_identifier",
                "type": "STRING"
            },
            {
                "name": "processor_identifier",
                "type": "STRING"
            },
            {
                "name": "fis_identifier",
                "type": "INTEGER"
            },
            {
                "name": "e6_customer_number",
                "type": "STRING"
            },
            {
                "name": "last_login",
                "type": "TIMESTAMP"
            },
            {
                "name": "auth0_user_ids",
                "type": "STRING",
                "mode": "REPEATED"
            },
            {
                "name": "created_at",
                "type": "TIMESTAMP"
            },
            {
                "name": "updated_at",
                "type": "TIMESTAMP"
            },
            {
                "name": "deleted_at",
                "type": "TIMESTAMP"
            },
            {
                "name": "spending_paused",
                "type": "TIMESTAMP"
            },
            {
                "name": "is_test_member",
                "type": "BOOLEAN"
            },
            {
                "name": "pending_deactivation_state",
                "type": "STRING"
            }
        ]
    },
    {
        "name": "sponsor",
        "type": "RECORD",
        "fields": [
            {
                "name": "sponsor_id",
                "type": "STRING"
            },
            {
                "name": "name",
                "type": "STRING"
            },
            {
                "name": "description",
                "type": "STRING"
            },
            {
                "name": "config",
                "type": "STRING"
            },
            {
                "name": "funding_account_identifier",
                "type": "STRING"
            },
            {
                "name": "galileo_product_identifier",
                "type": "INTEGER"
            },
            {
                "name": "emboss_kit_identifier",
                "type": "INTEGER"
            },
            {
                "name": "uber_org_identifier",
                "type": "STRING"
            },
            {
                "name": "created_at",
                "type": "TIMESTAMP"
            },
            {
                "name": "variant",
                "type": "STRING"
            },
            {
                "name": "parent_id",
                "type": "STRING"
            }
        ]
    },
    {
        "name": "soda_transaction",
        "type": "RECORD",
        "fields": [
            {
                "name": "id",
                "type": "INTEGER"
            },
            {
                "name": "payee",
                "type": "STRING"
            },
            {
                "name": "effective_date",
                "type": "TIMESTAMP"
            },
            {
                "name": "created_at",
                "type": "TIMESTAMP"
            },
            {
                "name": "transaction_type",
                "type": "STRING"
            },
            {
                "name": "mcc",
                "type": "STRING"
            },
            {
                "name": "mid",
                "type": "STRING"
            },
            {
                "name": "transaction_metadata",
                "type": "STRING"
            },
            {
                "name": "transaction_source",
                "type": "STRING"
            },
            {
                "name": "reversal_id",
                "type": "INTEGER"
            }
        ]
    }
]
```

### `harmony_export.transactions`

```json
[
    {
        "name": "id",
        "type": "INTEGER"
    },
    {
        "name": "payee",
        "type": "STRING"
    },
    {
        "name": "effective_date",
        "type": "TIMESTAMP"
    },
    {
        "name": "created_at",
        "type": "TIMESTAMP"
    },
    {
        "name": "transaction_type",
        "type": "STRING"
    },
    {
        "name": "mcc",
        "type": "STRING"
    },
    {
        "name": "mid",
        "type": "STRING"
    },
    {
        "name": "transaction_metadata",
        "type": "STRING"
    },
    {
        "name": "transaction_source",
        "type": "STRING"
    },
    {
        "name": "reversal_id",
        "type": "INTEGER"
    },
    {
        "name": "entries",
        "type": "RECORD",
        "mode": "REPEATED",
        "fields": [
            {
                "name": "id",
                "type": "INTEGER"
            },
            {
                "name": "transaction_id",
                "type": "INTEGER"
            },
            {
                "name": "book_id",
                "type": "INTEGER"
            },
            {
                "name": "amount",
                "type": "NUMERIC"
            },
            {
                "name": "type",
                "type": "STRING"
            },
            {
                "name": "entry_metadata",
                "type": "STRING"
            },
            {
                "name": "auth_id",
                "type": "INTEGER"
            },
            {
                "name": "network",
                "type": "STRING"
            },
            {
                "name": "processor_message_identifier",
                "type": "STRING"
            },
            {
                "name": "approval_profile_id",
                "type": "STRING"
            },
            {
                "name": "entry_source",
                "type": "STRING"
            },
            {
                "name": "effective_date",
                "type": "TIMESTAMP"
            },
            {
                "name": "created_at",
                "type": "TIMESTAMP"
            },
            {
                "name": "book",
                "type": "RECORD",
                "fields": [
                    {
                        "name": "id",
                        "type": "INTEGER"
                    },
                    {
                        "name": "name",
                        "type": "STRING"
                    },
                    {
                        "name": "type",
                        "type": "STRING"
                    },
                    {
                        "name": "sponsor_id",
                        "type": "STRING"
                    },
                    {
                        "name": "benefit_id",
                        "type": "STRING"
                    },
                    {
                        "name": "member_id",
                        "type": "STRING"
                    },
                    {
                        "name": "surrender_date",
                        "type": "TIMESTAMP"
                    },
                    {
                        "name": "enrollment_id",
                        "type": "STRING"
                    },
                    {
                        "name": "benefit_book_id",
                        "type": "INTEGER"
                    },
                    {
                        "name": "book_metadata",
                        "type": "STRING"
                    },
                    {
                        "name": "idempotence_key",
                        "type": "STRING"
                    },
                    {
                        "name": "funding_account_identifier",
                        "type": "STRING"
                    }
                ]
            },
            {
                "name": "benefit",
                "type": "RECORD",
                "fields": [
                    {
                        "name": "benefit_id",
                        "type": "STRING"
                    },
                    {
                        "name": "sponsor_id",
                        "type": "STRING"
                    },
                    {
                        "name": "type",
                        "type": "STRING"
                    },
                    {
                        "name": "sponsor_identifier",
                        "type": "STRING"
                    },
                    {
                        "name": "name",
                        "type": "STRING"
                    },
                    {
                        "name": "multiple_enrollment",
                        "type": "BOOLEAN"
                    },
                    {
                        "name": "iterations",
                        "type": "INTEGER"
                    },
                    {
                        "name": "interval",
                        "type": "STRING"
                    },
                    {
                        "name": "duration",
                        "type": "STRING"
                    },
                    {
                        "name": "start_date",
                        "type": "TIMESTAMP"
                    },
                    {
                        "name": "calculated_end_date",
                        "type": "TIMESTAMP"
                    },
                    {
                        "name": "created_at",
                        "type": "TIMESTAMP"
                    },
                    {
                        "name": "updated_at",
                        "type": "TIMESTAMP"
                    },
                    {
                        "name": "deleted_at",
                        "type": "TIMESTAMP"
                    },
                    {
                        "name": "funding_amount",
                        "type": "NUMERIC"
                    },
                    {
                        "name": "proration_type",
                        "type": "STRING"
                    },
                    {
                        "name": "priority",
                        "type": "INTEGER"
                    },
                    {
                        "name": "is_variable_amount",
                        "type": "BOOLEAN"
                    },
                    {
                        "name": "amount_on_enrollment",
                        "type": "BOOLEAN"
                    },
                    {
                        "name": "max_cost_per_ride",
                        "type": "NUMERIC"
                    },
                    {
                        "name": "num_one_way_rides",
                        "type": "INTEGER"
                    },
                    {
                        "name": "otchs_benefit_identifier",
                        "type": "STRING"
                    },
                    {
                        "name": "catalog_on_enrollment",
                        "type": "BOOLEAN"
                    }
                ]
            },
            {
                "name": "coupon_enrollment_book",
                "type": "RECORD",
                "fields": [
                    {
                        "name": "coupon_enrollment_book_id",
                        "type": "INTEGER"
                    },
                    {
                        "name": "coupon_program_id",
                        "type": "STRING"
                    },
                    {
                        "name": "coupon_program_enrollment_id",
                        "type": "STRING"
                    }
                ]
            },
            {
                "name": "coupon_pool_book",
                "type": "RECORD",
                "fields": [
                    {
                        "name": "coupon_pool_book_id",
                        "type": "INTEGER"
                    },
                    {
                        "name": "coupon_program_id",
                        "type": "STRING"
                    },
                    {
                        "name": "funding_account_identifier",
                        "type": "STRING"
                    }
                ]
            }
        ]
    },
    {
        "name": "sponsor_id",
        "type": "STRING"
    },
    {
        "name": "member_id",
        "type": "STRING"
    },
    {
        "name": "member",
        "type": "RECORD",
        "fields": [
            {
                "name": "member_id",
                "type": "STRING"
            },
            {
                "name": "sponsor_id",
                "type": "STRING"
            },
            {
                "name": "sponsor_identifier",
                "type": "STRING"
            },
            {
                "name": "processor_identifier",
                "type": "STRING"
            },
            {
                "name": "fis_identifier",
                "type": "INTEGER"
            },
            {
                "name": "e6_customer_number",
                "type": "STRING"
            },
            {
                "name": "last_login",
                "type": "TIMESTAMP"
            },
            {
                "name": "auth0_user_ids",
                "type": "STRING",
                "mode": "REPEATED"
            },
            {
                "name": "created_at",
                "type": "TIMESTAMP"
            },
            {
                "name": "updated_at",
                "type": "TIMESTAMP"
            },
            {
                "name": "deleted_at",
                "type": "TIMESTAMP"
            },
            {
                "name": "spending_paused",
                "type": "TIMESTAMP"
            },
            {
                "name": "is_test_member",
                "type": "BOOLEAN"
            },
            {
                "name": "pending_deactivation_state",
                "type": "STRING"
            }
        ]
    },
    {
        "name": "sponsor",
        "type": "RECORD",
        "fields": [
            {
                "name": "sponsor_id",
                "type": "STRING"
            },
            {
                "name": "name",
                "type": "STRING"
            },
            {
                "name": "description",
                "type": "STRING"
            },
            {
                "name": "config",
                "type": "STRING"
            },
            {
                "name": "funding_account_identifier",
                "type": "STRING"
            },
            {
                "name": "galileo_product_identifier",
                "type": "INTEGER"
            },
            {
                "name": "emboss_kit_identifier",
                "type": "INTEGER"
            },
            {
                "name": "uber_org_identifier",
                "type": "STRING"
            },
            {
                "name": "created_at",
                "type": "TIMESTAMP"
            },
            {
                "name": "variant",
                "type": "STRING"
            },
            {
                "name": "parent_id",
                "type": "STRING"
            }
        ]
    }
]
```

### `harmony_export.transactions_copy`

```json
[
    {
        "name": "id",
        "type": "INTEGER"
    },
    {
        "name": "payee",
        "type": "STRING"
    },
    {
        "name": "effective_date",
        "type": "TIMESTAMP"
    },
    {
        "name": "created_at",
        "type": "TIMESTAMP"
    },
    {
        "name": "transaction_type",
        "type": "STRING"
    },
    {
        "name": "mcc",
        "type": "STRING"
    },
    {
        "name": "mid",
        "type": "STRING"
    },
    {
        "name": "transaction_metadata",
        "type": "STRING"
    },
    {
        "name": "transaction_source",
        "type": "STRING"
    },
    {
        "name": "reversal_id",
        "type": "INTEGER"
    },
    {
        "name": "entries",
        "type": "RECORD",
        "mode": "REPEATED",
        "fields": [
            {
                "name": "id",
                "type": "INTEGER"
            },
            {
                "name": "transaction_id",
                "type": "INTEGER"
            },
            {
                "name": "book_id",
                "type": "INTEGER"
            },
            {
                "name": "amount",
                "type": "NUMERIC"
            },
            {
                "name": "type",
                "type": "STRING"
            },
            {
                "name": "entry_metadata",
                "type": "STRING"
            },
            {
                "name": "auth_id",
                "type": "INTEGER"
            },
            {
                "name": "network",
                "type": "STRING"
            },
            {
                "name": "processor_message_identifier",
                "type": "STRING"
            },
            {
                "name": "approval_profile_id",
                "type": "STRING"
            },
            {
                "name": "entry_source",
                "type": "STRING"
            },
            {
                "name": "effective_date",
                "type": "TIMESTAMP"
            },
            {
                "name": "created_at",
                "type": "TIMESTAMP"
            },
            {
                "name": "book",
                "type": "RECORD",
                "fields": [
                    {
                        "name": "id",
                        "type": "INTEGER"
                    },
                    {
                        "name": "name",
                        "type": "STRING"
                    },
                    {
                        "name": "type",
                        "type": "STRING"
                    },
                    {
                        "name": "sponsor_id",
                        "type": "STRING"
                    },
                    {
                        "name": "benefit_id",
                        "type": "STRING"
                    },
                    {
                        "name": "member_id",
                        "type": "STRING"
                    },
                    {
                        "name": "surrender_date",
                        "type": "TIMESTAMP"
                    },
                    {
                        "name": "enrollment_id",
                        "type": "STRING"
                    },
                    {
                        "name": "benefit_book_id",
                        "type": "INTEGER"
                    },
                    {
                        "name": "book_metadata",
                        "type": "STRING"
                    },
                    {
                        "name": "idempotence_key",
                        "type": "STRING"
                    },
                    {
                        "name": "funding_account_identifier",
                        "type": "STRING"
                    }
                ]
            },
            {
                "name": "benefit",
                "type": "RECORD",
                "fields": [
                    {
                        "name": "benefit_id",
                        "type": "STRING"
                    },
                    {
                        "name": "sponsor_id",
                        "type": "STRING"
                    },
                    {
                        "name": "type",
                        "type": "STRING"
                    },
                    {
                        "name": "sponsor_identifier",
                        "type": "STRING"
                    },
                    {
                        "name": "name",
                        "type": "STRING"
                    },
                    {
                        "name": "multiple_enrollment",
                        "type": "BOOLEAN"
                    },
                    {
                        "name": "iterations",
                        "type": "INTEGER"
                    },
                    {
                        "name": "interval",
                        "type": "STRING"
                    },
                    {
                        "name": "duration",
                        "type": "STRING"
                    },
                    {
                        "name": "start_date",
                        "type": "TIMESTAMP"
                    },
                    {
                        "name": "calculated_end_date",
                        "type": "TIMESTAMP"
                    },
                    {
                        "name": "created_at",
                        "type": "TIMESTAMP"
                    },
                    {
                        "name": "updated_at",
                        "type": "TIMESTAMP"
                    },
                    {
                        "name": "deleted_at",
                        "type": "TIMESTAMP"
                    },
                    {
                        "name": "funding_amount",
                        "type": "NUMERIC"
                    },
                    {
                        "name": "proration_type",
                        "type": "STRING"
                    },
                    {
                        "name": "priority",
                        "type": "INTEGER"
                    },
                    {
                        "name": "is_variable_amount",
                        "type": "BOOLEAN"
                    },
                    {
                        "name": "amount_on_enrollment",
                        "type": "BOOLEAN"
                    },
                    {
                        "name": "max_cost_per_ride",
                        "type": "NUMERIC"
                    },
                    {
                        "name": "num_one_way_rides",
                        "type": "INTEGER"
                    },
                    {
                        "name": "otchs_benefit_identifier",
                        "type": "STRING"
                    },
                    {
                        "name": "catalog_on_enrollment",
                        "type": "BOOLEAN"
                    }
                ]
            },
            {
                "name": "coupon_enrollment_book",
                "type": "RECORD",
                "fields": [
                    {
                        "name": "coupon_enrollment_book_id",
                        "type": "INTEGER"
                    },
                    {
                        "name": "coupon_program_id",
                        "type": "STRING"
                    },
                    {
                        "name": "coupon_program_enrollment_id",
                        "type": "STRING"
                    }
                ]
            },
            {
                "name": "coupon_pool_book",
                "type": "RECORD",
                "fields": [
                    {
                        "name": "coupon_pool_book_id",
                        "type": "INTEGER"
                    },
                    {
                        "name": "coupon_program_id",
                        "type": "STRING"
                    },
                    {
                        "name": "funding_account_identifier",
                        "type": "STRING"
                    }
                ]
            }
        ]
    },
    {
        "name": "sponsor_id",
        "type": "STRING"
    },
    {
        "name": "member_id",
        "type": "STRING"
    },
    {
        "name": "member",
        "type": "RECORD",
        "fields": [
            {
                "name": "member_id",
                "type": "STRING"
            },
            {
                "name": "sponsor_id",
                "type": "STRING"
            },
            {
                "name": "sponsor_identifier",
                "type": "STRING"
            },
            {
                "name": "processor_identifier",
                "type": "STRING"
            },
            {
                "name": "fis_identifier",
                "type": "INTEGER"
            },
            {
                "name": "e6_customer_identifier",
                "type": "STRING"
            },
            {
                "name": "last_login",
                "type": "TIMESTAMP"
            },
            {
                "name": "auth0_user_ids",
                "type": "STRING",
                "mode": "REPEATED"
            },
            {
                "name": "created_at",
                "type": "TIMESTAMP"
            },
            {
                "name": "updated_at",
                "type": "TIMESTAMP"
            },
            {
                "name": "deleted_at",
                "type": "TIMESTAMP"
            },
            {
                "name": "spending_paused",
                "type": "TIMESTAMP"
            },
            {
                "name": "is_test_member",
                "type": "BOOLEAN"
            },
            {
                "name": "pending_deactivation_state",
                "type": "STRING"
            }
        ]
    },
    {
        "name": "sponsor",
        "type": "RECORD",
        "fields": [
            {
                "name": "sponsor_id",
                "type": "STRING"
            },
            {
                "name": "name",
                "type": "STRING"
            },
            {
                "name": "description",
                "type": "STRING"
            },
            {
                "name": "config",
                "type": "STRING"
            },
            {
                "name": "funding_account_identifier",
                "type": "STRING"
            },
            {
                "name": "galileo_product_identifier",
                "type": "INTEGER"
            },
            {
                "name": "emboss_kit_identifier",
                "type": "INTEGER"
            },
            {
                "name": "uber_org_identifier",
                "type": "STRING"
            },
            {
                "name": "created_at",
                "type": "TIMESTAMP"
            },
            {
                "name": "variant",
                "type": "STRING"
            },
            {
                "name": "parent_id",
                "type": "STRING"
            }
        ]
    }
]
```

## Dataset: `harmony_views`

### `harmony_views.CARD-DELIVERY-FUNNEL-SUMMARY-QUERY`

```json
[
    {
        "name": "member_id",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "sponsor_name",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "sponsor_id",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "card_id",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "created_at",
        "type": "TIMESTAMP",
        "mode": "NULLABLE"
    },
    {
        "name": "shipped_at",
        "type": "TIMESTAMP",
        "mode": "NULLABLE"
    },
    {
        "name": "card_status",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "processor_status",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "activated_at",
        "type": "TIMESTAMP",
        "mode": "NULLABLE"
    },
    {
        "name": "deleted_at",
        "type": "TIMESTAMP",
        "mode": "NULLABLE"
    },
    {
        "name": "days_since_activation",
        "type": "INTEGER",
        "mode": "NULLABLE"
    },
    {
        "name": "days_to_activation",
        "type": "INTEGER",
        "mode": "NULLABLE"
    },
    {
        "name": "days_active_before_deletion",
        "type": "INTEGER",
        "mode": "NULLABLE"
    },
    {
        "name": "latest_event_time",
        "type": "TIMESTAMP",
        "mode": "NULLABLE"
    },
    {
        "name": "latest_event_type",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "latest_event_source",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "event_message",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "raw_scan_status",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "raw_metadata",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "location",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "additional_info",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "latest_scan_status",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "is_delivered",
        "type": "BOOLEAN",
        "mode": "NULLABLE"
    },
    {
        "name": "is_return_indicator",
        "type": "BOOLEAN",
        "mode": "NULLABLE"
    },
    {
        "name": "is_out_for_delivery",
        "type": "BOOLEAN",
        "mode": "NULLABLE"
    },
    {
        "name": "scan_date",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "scan_datetime",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "expected_delivery_date",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "scan_date_parsed",
        "type": "DATE",
        "mode": "NULLABLE"
    },
    {
        "name": "scan_datetime_parsed",
        "type": "DATETIME",
        "mode": "NULLABLE"
    },
    {
        "name": "expected_delivery_date_parsed",
        "type": "DATE",
        "mode": "NULLABLE"
    },
    {
        "name": "days_since_shipped",
        "type": "INTEGER",
        "mode": "NULLABLE"
    },
    {
        "name": "days_until_expected_delivery",
        "type": "INTEGER",
        "mode": "NULLABLE"
    },
    {
        "name": "total_days_since_shipped",
        "type": "INTEGER",
        "mode": "NULLABLE"
    },
    {
        "name": "funnel_stage",
        "type": "STRING",
        "mode": "NULLABLE"
    }
]
```

### `harmony_views.GHCE_Median_Transactions_Per_Member_By_Benefit`

```json
[
    {
        "name": "benefit_id",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "benefit_name",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "sponsor_name",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "Median_Transactions_Per_Member",
        "type": "INTEGER",
        "mode": "NULLABLE"
    }
]
```

### `harmony_views.GHCE_Part_C_Report_2024`

```json
[
    {
        "name": "Contract Number",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "Plan Number",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "PBP Category",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "Supplemental Benefit Name",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "Offered Type",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "Unit of Utilization",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "Eligible Enrollees",
        "type": "INTEGER",
        "mode": "NULLABLE"
    },
    {
        "name": "Number of Utilizing Members",
        "type": "INTEGER",
        "mode": "NULLABLE"
    },
    {
        "name": "Instances of Utilization",
        "type": "INTEGER",
        "mode": "NULLABLE"
    },
    {
        "name": "Median Number of Utilizations",
        "type": "INTEGER",
        "mode": "NULLABLE"
    },
    {
        "name": "Net Amount Incurred",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "Type of Payment Arrangement",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "How the Plan accounts for Cost",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "Total out-of-pocket-cost per utilization for enrolees",
        "type": "STRING",
        "mode": "NULLABLE"
    }
]
```

### `harmony_views.IHPC_Median_Transactions_Per_Member_By_Benefit`

```json
[
    {
        "name": "benefit_id",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "benefit_name",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "sponsor_name",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "Median_Transactions_Per_Member",
        "type": "INTEGER",
        "mode": "NULLABLE"
    }
]
```

### `harmony_views.IHPC_Median_Transactions_Per_Member_By_Benefit_2025`

```json
[
    {
        "name": "benefit_id",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "benefit_name",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "sponsor_name",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "Median_Transactions_Per_Member",
        "type": "INTEGER",
        "mode": "NULLABLE"
    }
]
```

### `harmony_views.IHPC_year_of_funding_quarterly_benefits`

```json
[
    {
        "name": "year_of_funding",
        "type": "DATE",
        "mode": "NULLABLE"
    },
    {
        "name": "sponsor_id",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "sponsor_name",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "benefit_id",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "benefit_name",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "amount",
        "type": "NUMERIC",
        "mode": "NULLABLE"
    },
    {
        "name": "Members_In_Plan_At_Some_Point_In_Period",
        "type": "INTEGER",
        "mode": "NULLABLE"
    }
]
```

### `harmony_views.IHPC_yearly_utilization_quarterly_benefits`

```json
[
    {
        "name": "Year",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "Sponsor",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "Benefit",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "Amount_Funded",
        "type": "NUMERIC",
        "mode": "NULLABLE"
    },
    {
        "name": "Amount_Spent",
        "type": "NUMERIC",
        "mode": "NULLABLE"
    },
    {
        "name": "Utilization_Rate",
        "type": "NUMERIC",
        "mode": "NULLABLE"
    },
    {
        "name": "utilizing_members",
        "type": "INTEGER",
        "mode": "NULLABLE"
    },
    {
        "name": "Members_In_Plan_At_Some_Point_In_Period",
        "type": "INTEGER",
        "mode": "NULLABLE"
    },
    {
        "name": "Utilizing_Member_Percentage",
        "type": "FLOAT",
        "mode": "NULLABLE"
    },
    {
        "name": "Transaction_Count",
        "type": "INTEGER",
        "mode": "NULLABLE"
    },
    {
        "name": "Average_Transaction_Amount",
        "type": "NUMERIC",
        "mode": "NULLABLE"
    }
]
```

### `harmony_views.IHPC_yearly_utilization_quarterly_benefits_2025`

```json
[
    {
        "name": "Year",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "Sponsor",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "Benefit",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "Amount_Funded",
        "type": "NUMERIC",
        "mode": "NULLABLE"
    },
    {
        "name": "Amount_Spent",
        "type": "NUMERIC",
        "mode": "NULLABLE"
    },
    {
        "name": "Utilization_Rate",
        "type": "NUMERIC",
        "mode": "NULLABLE"
    },
    {
        "name": "utilizing_members",
        "type": "INTEGER",
        "mode": "NULLABLE"
    },
    {
        "name": "Members_In_Plan_At_Some_Point_In_Period",
        "type": "INTEGER",
        "mode": "NULLABLE"
    },
    {
        "name": "Utilizing_Member_Percentage",
        "type": "FLOAT",
        "mode": "NULLABLE"
    },
    {
        "name": "Transaction_Count",
        "type": "INTEGER",
        "mode": "NULLABLE"
    },
    {
        "name": "Average_Transaction_Amount",
        "type": "NUMERIC",
        "mode": "NULLABLE"
    }
]
```

### `harmony_views.Monthly_EDS_Report_Monthly_Benefits`

```json
[
    {
        "name": "sponsor_id",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "member_id",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "NPI",
        "type": "INTEGER",
        "mode": "NULLABLE"
    },
    {
        "name": "Procedure_Code",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "Diagnosis_Code",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "Revenue_Code",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "From_Date_of_Service",
        "type": "DATE",
        "mode": "NULLABLE"
    },
    {
        "name": "last_day_of_month",
        "type": "DATE",
        "mode": "NULLABLE"
    },
    {
        "name": "PWK06",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "Line_Item_Charge_Amount",
        "type": "NUMERIC",
        "mode": "NULLABLE"
    },
    {
        "name": "Service_Line_Paid_Amount",
        "type": "NUMERIC",
        "mode": "NULLABLE"
    }
]
```

### `harmony_views.Quarterly_EDS_Report_Quarterly_Benefits`

```json
[
    {
        "name": "sponsor_id",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "member_id",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "NPI",
        "type": "INTEGER",
        "mode": "NULLABLE"
    },
    {
        "name": "Procedure_Code",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "Diagnosis_Code",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "Revenue_Code",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "From_Date_of_Service",
        "type": "DATE",
        "mode": "NULLABLE"
    },
    {
        "name": "last_day_of_quarter",
        "type": "DATE",
        "mode": "NULLABLE"
    },
    {
        "name": "PWK06",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "Line_Item_Charge_Amount",
        "type": "NUMERIC",
        "mode": "NULLABLE"
    },
    {
        "name": "Service_Line_Paid_Amount",
        "type": "NUMERIC",
        "mode": "NULLABLE"
    }
]
```

### `harmony_views.Quarterly_EDS_Report_Quarterly_Benefits_BMA`

```json
[
    {
        "name": "sponsor_id",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "member_id",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "NPI",
        "type": "INTEGER",
        "mode": "NULLABLE"
    },
    {
        "name": "Procedure_Code",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "Diagnosis_Code",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "Revenue_Code",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "From_Date_of_Service",
        "type": "DATE",
        "mode": "NULLABLE"
    },
    {
        "name": "last_day_of_quarter",
        "type": "DATE",
        "mode": "NULLABLE"
    },
    {
        "name": "Benefit_Name",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "PWK06",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "Line_Item_Charge_Amount",
        "type": "NUMERIC",
        "mode": "NULLABLE"
    },
    {
        "name": "Service_Line_Paid_Amount",
        "type": "NUMERIC",
        "mode": "NULLABLE"
    }
]
```

### `harmony_views.Year_of_funding_quarterly_benefits`

```json
[
    {
        "name": "year_of_funding",
        "type": "DATE",
        "mode": "NULLABLE"
    },
    {
        "name": "sponsor_id",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "sponsor_name",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "benefit_id",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "benefit_name",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "amount",
        "type": "NUMERIC",
        "mode": "NULLABLE"
    },
    {
        "name": "Members_In_Plan_At_Some_Point_In_Period",
        "type": "INTEGER",
        "mode": "NULLABLE"
    }
]
```

### `harmony_views.active_members_with_only_unsuccessful_trips`

```json
[
    {
        "name": "member_id_new",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "count_of_successful_trips",
        "type": "INTEGER",
        "mode": "NULLABLE"
    },
    {
        "name": "count_of_unsuccessful_trips",
        "type": "INTEGER",
        "mode": "NULLABLE"
    },
    {
        "name": "sponsor_name",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "all_declined_reasons",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "latest_unsuccessful_swipe",
        "type": "TIMESTAMP",
        "mode": "NULLABLE"
    }
]
```

### `harmony_views.daily_spend`

```json
[
    {
        "name": "year_of_spending",
        "type": "TIMESTAMP",
        "mode": "NULLABLE"
    },
    {
        "name": "quarter_of_spending",
        "type": "TIMESTAMP",
        "mode": "NULLABLE"
    },
    {
        "name": "month_of_spending",
        "type": "TIMESTAMP",
        "mode": "NULLABLE"
    },
    {
        "name": "day_of_spending",
        "type": "TIMESTAMP",
        "mode": "NULLABLE"
    },
    {
        "name": "sponsor_id",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "sponsor_name",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "benefit_id",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "benefit_name",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "amount",
        "type": "NUMERIC",
        "mode": "NULLABLE"
    }
]
```

### `harmony_views.daily_spending_of_monthly_benefit`

```json
[
    {
        "name": "day_of_spending",
        "type": "TIMESTAMP",
        "mode": "NULLABLE"
    },
    {
        "name": "month_of_funding",
        "type": "DATE",
        "mode": "NULLABLE"
    },
    {
        "name": "sponsor_id",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "sponsor_name",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "benefit_id",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "benefit_name",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "amount_funded",
        "type": "NUMERIC",
        "mode": "NULLABLE"
    },
    {
        "name": "amount_spent",
        "type": "NUMERIC",
        "mode": "NULLABLE"
    },
    {
        "name": "utilization_rate",
        "type": "NUMERIC",
        "mode": "NULLABLE"
    }
]
```

### `harmony_views.daily_utilization_of_quarterly_benefit`

```json
[
    {
        "name": "day_of_spending",
        "type": "TIMESTAMP",
        "mode": "NULLABLE"
    },
    {
        "name": "quarter_of_funding",
        "type": "DATE",
        "mode": "NULLABLE"
    },
    {
        "name": "sponsor_id",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "sponsor_name",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "benefit_id",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "benefit_name",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "amount_funded",
        "type": "NUMERIC",
        "mode": "NULLABLE"
    },
    {
        "name": "amount_spent",
        "type": "NUMERIC",
        "mode": "NULLABLE"
    },
    {
        "name": "utilization_rate",
        "type": "NUMERIC",
        "mode": "NULLABLE"
    }
]
```

### `harmony_views.daily_utilization_of_yearly_benefits`

```json
[
    {
        "name": "day_of_spending",
        "type": "TIMESTAMP",
        "mode": "NULLABLE"
    },
    {
        "name": "year_of_funding",
        "type": "DATE",
        "mode": "NULLABLE"
    },
    {
        "name": "sponsor_id",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "sponsor_name",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "benefit_id",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "benefit_name",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "amount_funded",
        "type": "NUMERIC",
        "mode": "NULLABLE"
    },
    {
        "name": "amount_spent",
        "type": "NUMERIC",
        "mode": "NULLABLE"
    },
    {
        "name": "utilization_rate",
        "type": "NUMERIC",
        "mode": "NULLABLE"
    }
]
```

### `harmony_views.factors_combined_view`

```json
[
    {
        "name": "member_id",
        "type": "STRING"
    },
    {
        "name": "sponsor_id",
        "type": "STRING"
    },
    {
        "name": "sponsor_name",
        "type": "STRING"
    },
    {
        "name": "sponsor_variant",
        "type": "STRING"
    },
    {
        "name": "customer_name",
        "type": "STRING"
    },
    {
        "name": "resolved_customer_name",
        "type": "STRING"
    },
    {
        "name": "display_customer_name",
        "type": "STRING"
    },
    {
        "name": "factor_id",
        "type": "INTEGER"
    },
    {
        "name": "factor_identifier",
        "type": "STRING"
    },
    {
        "name": "factor_name",
        "type": "STRING"
    },
    {
        "name": "factor_description",
        "type": "STRING"
    },
    {
        "name": "factor_value_id",
        "type": "INTEGER"
    },
    {
        "name": "factor_value",
        "type": "STRING"
    },
    {
        "name": "factor_value_description",
        "type": "STRING"
    },
    {
        "name": "qualification_status",
        "type": "STRING"
    },
    {
        "name": "assignment_source",
        "type": "STRING"
    },
    {
        "name": "assignment_created_at",
        "type": "TIMESTAMP"
    },
    {
        "name": "job_run_id",
        "type": "STRING"
    },
    {
        "name": "job_run_row",
        "type": "STRING"
    },
    {
        "name": "auth0_id",
        "type": "STRING"
    },
    {
        "name": "reason",
        "type": "STRING"
    },
    {
        "name": "factor_created_at",
        "type": "TIMESTAMP"
    },
    {
        "name": "factor_updated_at",
        "type": "TIMESTAMP"
    },
    {
        "name": "factor_value_created_at",
        "type": "TIMESTAMP"
    },
    {
        "name": "assignment_date",
        "type": "DATE"
    },
    {
        "name": "assignment_year",
        "type": "INTEGER"
    },
    {
        "name": "assignment_month",
        "type": "INTEGER"
    },
    {
        "name": "assignment_quarter",
        "type": "INTEGER"
    },
    {
        "name": "assignment_year_month",
        "type": "STRING"
    }
]
```

### `harmony_views.fis_replacement_cards`

```json
[
    {
        "name": "member_id",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "sponsor_identifier",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "card_created_at",
        "type": "TIMESTAMP",
        "mode": "NULLABLE"
    },
    {
        "name": "sponsor_name",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "card_id",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "fis_identifier",
        "type": "INTEGER",
        "mode": "NULLABLE"
    },
    {
        "name": "galileo_identifier",
        "type": "INTEGER",
        "mode": "NULLABLE"
    },
    {
        "name": "card_created_count_for_member",
        "type": "INTEGER",
        "mode": "NULLABLE"
    }
]
```

### `harmony_views.glo_replacement_cards`

```json
[
    {
        "name": "member_id",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "sponsor_identifier",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "card_created_at",
        "type": "TIMESTAMP",
        "mode": "NULLABLE"
    },
    {
        "name": "sponsor_name",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "card_id",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "fis_identifier",
        "type": "INTEGER",
        "mode": "NULLABLE"
    },
    {
        "name": "galileo_identifier",
        "type": "INTEGER",
        "mode": "NULLABLE"
    },
    {
        "name": "card_created_count_for_member",
        "type": "INTEGER",
        "mode": "NULLABLE"
    }
]
```

### `harmony_views.member_enrollment_observability`

```json
[
    {
        "name": "row_type",
        "type": "STRING"
    },
    {
        "name": "rule_name",
        "type": "STRING"
    },
    {
        "name": "severity",
        "type": "STRING"
    },
    {
        "name": "member_id",
        "type": "STRING"
    },
    {
        "name": "sponsor_id",
        "type": "STRING"
    },
    {
        "name": "sponsor_name",
        "type": "STRING"
    },
    {
        "name": "sponsor_identifier",
        "type": "STRING"
    },
    {
        "name": "processor_identifier",
        "type": "STRING"
    },
    {
        "name": "fis_identifier",
        "type": "INTEGER"
    },
    {
        "name": "last_login",
        "type": "TIMESTAMP"
    },
    {
        "name": "member_created_at",
        "type": "TIMESTAMP"
    },
    {
        "name": "member_updated_at",
        "type": "TIMESTAMP"
    },
    {
        "name": "member_deleted_at",
        "type": "TIMESTAMP"
    },
    {
        "name": "spending_paused",
        "type": "TIMESTAMP"
    },
    {
        "name": "is_test_member",
        "type": "BOOLEAN"
    },
    {
        "name": "year_of_birth",
        "type": "INTEGER"
    },
    {
        "name": "language_tag",
        "type": "STRING"
    },
    {
        "name": "does_email_exist",
        "type": "STRING"
    },
    {
        "name": "cms_reporting_gender",
        "type": "STRING"
    },
    {
        "name": "zip_prefix",
        "type": "STRING"
    },
    {
        "name": "us_state",
        "type": "STRING"
    },
    {
        "name": "program_enrollment_id",
        "type": "STRING"
    },
    {
        "name": "program_id",
        "type": "STRING"
    },
    {
        "name": "program_sponsor_identifier",
        "type": "STRING"
    },
    {
        "name": "program_plan_year",
        "type": "INTEGER"
    },
    {
        "name": "program_enrollment_active_at",
        "type": "TIMESTAMP"
    },
    {
        "name": "program_enrollment_expires_at",
        "type": "TIMESTAMP"
    },
    {
        "name": "program_enrollment_created_at",
        "type": "TIMESTAMP"
    },
    {
        "name": "program_enrollment_deleted_at",
        "type": "TIMESTAMP"
    },
    {
        "name": "benefit_enrollment_id",
        "type": "STRING"
    },
    {
        "name": "benefit_id",
        "type": "STRING"
    },
    {
        "name": "benefit_sponsor_identifier",
        "type": "STRING"
    },
    {
        "name": "benefit_name",
        "type": "STRING"
    },
    {
        "name": "benefit_active_at",
        "type": "TIMESTAMP"
    },
    {
        "name": "benefit_expires_at",
        "type": "TIMESTAMP"
    },
    {
        "name": "benefit_created_at",
        "type": "TIMESTAMP"
    },
    {
        "name": "benefit_deleted_at",
        "type": "TIMESTAMP"
    },
    {
        "name": "benefit_start_date",
        "type": "TIMESTAMP"
    },
    {
        "name": "benefit_calculated_end_date",
        "type": "TIMESTAMP"
    },
    {
        "name": "details_json",
        "type": "STRING"
    },
    {
        "name": "is_member_active_by_program_coverage",
        "type": "BOOLEAN"
    },
    {
        "name": "program_enrollments_total",
        "type": "INTEGER"
    },
    {
        "name": "program_enrollments_not_deleted_as_of_observed_ts",
        "type": "INTEGER"
    },
    {
        "name": "program_enrollments_deleted_as_of_observed_ts",
        "type": "INTEGER"
    },
    {
        "name": "benefit_enrollments_total",
        "type": "INTEGER"
    },
    {
        "name": "benefit_enrollments_not_deleted_as_of_observed_ts",
        "type": "INTEGER"
    },
    {
        "name": "benefit_enrollments_deleted_as_of_observed_ts",
        "type": "INTEGER"
    },
    {
        "name": "observed_at",
        "type": "TIMESTAMP"
    }
]
```

### `harmony_views.monthly_benefit_spend`

```json
[
    {
        "name": "month_of_spending",
        "type": "DATE",
        "mode": "NULLABLE"
    },
    {
        "name": "quarter_of_spending",
        "type": "DATE",
        "mode": "NULLABLE"
    },
    {
        "name": "sponsor_id",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "sponsor_name",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "benefit_id",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "benefit_name",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "amount",
        "type": "NUMERIC",
        "mode": "NULLABLE"
    },
    {
        "name": "Utilizing_Members",
        "type": "INTEGER",
        "mode": "NULLABLE"
    },
    {
        "name": "Transaction_Count",
        "type": "INTEGER",
        "mode": "NULLABLE"
    },
    {
        "name": "Average_Transaction_Amount",
        "type": "NUMERIC",
        "mode": "NULLABLE"
    }
]
```

### `harmony_views.monthly_funding`

```json
[
    {
        "name": "month_of_funding",
        "type": "DATE",
        "mode": "NULLABLE"
    },
    {
        "name": "sponsor_id",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "sponsor_name",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "benefit_id",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "benefit_name",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "amount",
        "type": "NUMERIC",
        "mode": "NULLABLE"
    },
    {
        "name": "Members_In_Plan_At_Some_Point_In_Period",
        "type": "INTEGER",
        "mode": "NULLABLE"
    }
]
```

### `harmony_views.monthly_funding_by_member`

```json
[
    {
        "name": "member_id",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "sponsor_identifier",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "month_of_funding",
        "type": "DATE",
        "mode": "NULLABLE"
    },
    {
        "name": "sponsor_id",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "sponsor_name",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "benefit_id",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "benefit_name",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "amount",
        "type": "NUMERIC",
        "mode": "NULLABLE"
    },
    {
        "name": "Members_In_Plan_At_Some_Point_In_Period",
        "type": "INTEGER",
        "mode": "NULLABLE"
    }
]
```

### `harmony_views.monthly_spending_by_member`

```json
[
    {
        "name": "month_of_spending",
        "type": "DATE",
        "mode": "NULLABLE"
    },
    {
        "name": "quarter_of_spending",
        "type": "DATE",
        "mode": "NULLABLE"
    },
    {
        "name": "member_id",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "sponsor_id",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "sponsor_name",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "benefit_id",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "benefit_name",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "amount",
        "type": "NUMERIC",
        "mode": "NULLABLE"
    },
    {
        "name": "Utilizing_Members",
        "type": "INTEGER",
        "mode": "NULLABLE"
    },
    {
        "name": "Transaction_Count",
        "type": "INTEGER",
        "mode": "NULLABLE"
    },
    {
        "name": "Average_Transaction_Amount",
        "type": "NUMERIC",
        "mode": "NULLABLE"
    }
]
```

### `harmony_views.monthly_utilization`

```json
[
    {
        "name": "month_of_spending",
        "type": "TIMESTAMP",
        "mode": "NULLABLE"
    },
    {
        "name": "month_of_funding",
        "type": "TIMESTAMP",
        "mode": "NULLABLE"
    },
    {
        "name": "sponsor_id",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "sponsor_name",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "benefit_id",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "benefit_name",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "amount_funded",
        "type": "NUMERIC",
        "mode": "NULLABLE"
    },
    {
        "name": "amount_spent",
        "type": "NUMERIC",
        "mode": "NULLABLE"
    },
    {
        "name": "utilization_rate",
        "type": "NUMERIC",
        "mode": "NULLABLE"
    }
]
```

### `harmony_views.monthly_utilization_for_report`

```json
[
    {
        "name": "Month",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "Sponsor",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "Benefit",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "Amount_Funded",
        "type": "NUMERIC",
        "mode": "NULLABLE"
    },
    {
        "name": "Amount_Spent",
        "type": "NUMERIC",
        "mode": "NULLABLE"
    },
    {
        "name": "Utilization_Rate",
        "type": "NUMERIC",
        "mode": "NULLABLE"
    },
    {
        "name": "utilizing_members",
        "type": "INTEGER",
        "mode": "NULLABLE"
    },
    {
        "name": "Members_In_Plan_At_Some_Point_In_Period",
        "type": "INTEGER",
        "mode": "NULLABLE"
    },
    {
        "name": "Utilizing_Member_Percentage",
        "type": "FLOAT",
        "mode": "NULLABLE"
    },
    {
        "name": "Transaction_Count",
        "type": "INTEGER",
        "mode": "NULLABLE"
    },
    {
        "name": "Average_Transaction_Amount",
        "type": "NUMERIC",
        "mode": "NULLABLE"
    }
]
```

### `harmony_views.monthly_utilization_of_monthly_benefit_by_member`

```json
[
    {
        "name": "member_id",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "sponsor_identifier",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "month_of_spending",
        "type": "DATE",
        "mode": "NULLABLE"
    },
    {
        "name": "month_of_funding",
        "type": "DATE",
        "mode": "NULLABLE"
    },
    {
        "name": "sponsor_id",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "sponsor_name",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "benefit_id",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "benefit_name",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "amount_funded",
        "type": "NUMERIC",
        "mode": "NULLABLE"
    },
    {
        "name": "amount_spent",
        "type": "NUMERIC",
        "mode": "NULLABLE"
    },
    {
        "name": "utilization_rate",
        "type": "NUMERIC",
        "mode": "NULLABLE"
    }
]
```

### `harmony_views.monthly_utilization_of_quarterly_benefit_by_member`

```json
[
    {
        "name": "member_id",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "month_of_spending",
        "type": "DATE",
        "mode": "NULLABLE"
    },
    {
        "name": "quarter_of_funding",
        "type": "DATE",
        "mode": "NULLABLE"
    },
    {
        "name": "sponsor_id",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "sponsor_name",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "benefit_id",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "benefit_name",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "amount_funded",
        "type": "NUMERIC",
        "mode": "NULLABLE"
    },
    {
        "name": "amount_spent",
        "type": "NUMERIC",
        "mode": "NULLABLE"
    },
    {
        "name": "utilization_rate",
        "type": "NUMERIC",
        "mode": "NULLABLE"
    }
]
```

### `harmony_views.quarterly_funding`

```json
[
    {
        "name": "quarter_of_funding",
        "type": "DATE",
        "mode": "NULLABLE"
    },
    {
        "name": "sponsor_id",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "sponsor_name",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "benefit_id",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "benefit_name",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "amount",
        "type": "NUMERIC",
        "mode": "NULLABLE"
    },
    {
        "name": "Members_In_Plan_At_Some_Point_In_Period",
        "type": "INTEGER",
        "mode": "NULLABLE"
    }
]
```

### `harmony_views.quarterly_funding_by_member`

```json
[
    {
        "name": "member_id",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "sponsor_identifier",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "quarter_of_funding",
        "type": "DATE",
        "mode": "NULLABLE"
    },
    {
        "name": "sponsor_id",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "sponsor_name",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "benefit_id",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "benefit_name",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "amount",
        "type": "NUMERIC",
        "mode": "NULLABLE"
    },
    {
        "name": "Members_In_Plan_At_Some_Point_In_Period",
        "type": "INTEGER",
        "mode": "NULLABLE"
    }
]
```

### `harmony_views.quarterly_spending`

```json
[
    {
        "name": "quarter_of_spending",
        "type": "DATE",
        "mode": "NULLABLE"
    },
    {
        "name": "sponsor_id",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "sponsor_name",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "benefit_id",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "benefit_name",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "amount",
        "type": "NUMERIC",
        "mode": "NULLABLE"
    },
    {
        "name": "Utilizing_Members",
        "type": "INTEGER",
        "mode": "NULLABLE"
    },
    {
        "name": "Transaction_Count",
        "type": "INTEGER",
        "mode": "NULLABLE"
    },
    {
        "name": "Average_Transaction_Amount",
        "type": "NUMERIC",
        "mode": "NULLABLE"
    }
]
```

### `harmony_views.quarterly_spending_by_member`

```json
[
    {
        "name": "quarter_of_spending",
        "type": "DATE",
        "mode": "NULLABLE"
    },
    {
        "name": "member_id",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "sponsor_id",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "sponsor_name",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "benefit_id",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "benefit_name",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "amount",
        "type": "NUMERIC",
        "mode": "NULLABLE"
    },
    {
        "name": "Utilizing_Members",
        "type": "INTEGER",
        "mode": "NULLABLE"
    },
    {
        "name": "Transaction_Count",
        "type": "INTEGER",
        "mode": "NULLABLE"
    },
    {
        "name": "Average_Transaction_Amount",
        "type": "NUMERIC",
        "mode": "NULLABLE"
    }
]
```

### `harmony_views.quarterly_utilization`

```json
[
    {
        "name": "quarter_of_spending",
        "type": "DATE",
        "mode": "NULLABLE"
    },
    {
        "name": "quarter_of_funding",
        "type": "DATE",
        "mode": "NULLABLE"
    },
    {
        "name": "sponsor_name",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "benefit_name",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "amount_funded",
        "type": "NUMERIC",
        "mode": "NULLABLE"
    },
    {
        "name": "amount_spent",
        "type": "NUMERIC",
        "mode": "NULLABLE"
    },
    {
        "name": "utilization_rate",
        "type": "NUMERIC",
        "mode": "NULLABLE"
    },
    {
        "name": "utilizing_members",
        "type": "INTEGER",
        "mode": "NULLABLE"
    },
    {
        "name": "Members_In_Plan_At_Some_Point_In_Period",
        "type": "INTEGER",
        "mode": "NULLABLE"
    },
    {
        "name": "Utilizing_Member_Percentage",
        "type": "FLOAT",
        "mode": "NULLABLE"
    },
    {
        "name": "Transaction_Count",
        "type": "INTEGER",
        "mode": "NULLABLE"
    },
    {
        "name": "Average_Transaction_Amount",
        "type": "NUMERIC",
        "mode": "NULLABLE"
    }
]
```

### `harmony_views.quarterly_utilization_by_member`

```json
[
    {
        "name": "member_id",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "quarter_of_spending",
        "type": "DATE",
        "mode": "NULLABLE"
    },
    {
        "name": "quarter_of_funding",
        "type": "DATE",
        "mode": "NULLABLE"
    },
    {
        "name": "sponsor_name",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "benefit_name",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "amount_funded",
        "type": "NUMERIC",
        "mode": "NULLABLE"
    },
    {
        "name": "amount_spent",
        "type": "NUMERIC",
        "mode": "NULLABLE"
    },
    {
        "name": "utilization_rate",
        "type": "NUMERIC",
        "mode": "NULLABLE"
    },
    {
        "name": "utilizing_members",
        "type": "INTEGER",
        "mode": "NULLABLE"
    },
    {
        "name": "Members_In_Plan_At_Some_Point_In_Period",
        "type": "INTEGER",
        "mode": "NULLABLE"
    },
    {
        "name": "Utilizing_Member_Percentage",
        "type": "FLOAT",
        "mode": "NULLABLE"
    },
    {
        "name": "Transaction_Count",
        "type": "INTEGER",
        "mode": "NULLABLE"
    },
    {
        "name": "Average_Transaction_Amount",
        "type": "NUMERIC",
        "mode": "NULLABLE"
    }
]
```

### `harmony_views.quarterly_utilization_for_report`

```json
[
    {
        "name": "Quarter",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "Sponsor",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "Benefit",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "Amount_Funded",
        "type": "NUMERIC",
        "mode": "NULLABLE"
    },
    {
        "name": "Amount_Spent",
        "type": "NUMERIC",
        "mode": "NULLABLE"
    },
    {
        "name": "Utilization_Rate",
        "type": "NUMERIC",
        "mode": "NULLABLE"
    },
    {
        "name": "utilizing_members",
        "type": "INTEGER",
        "mode": "NULLABLE"
    },
    {
        "name": "Members_In_Plan_At_Some_Point_In_Period",
        "type": "INTEGER",
        "mode": "NULLABLE"
    },
    {
        "name": "Utilizing_Member_Percentage",
        "type": "FLOAT",
        "mode": "NULLABLE"
    },
    {
        "name": "Transaction_Count",
        "type": "INTEGER",
        "mode": "NULLABLE"
    },
    {
        "name": "Average_Transaction_Amount",
        "type": "NUMERIC",
        "mode": "NULLABLE"
    }
]
```

### `harmony_views.quarterly_utilization_of_quarterly_benefit_by_member`

```json
[
    {
        "name": "member_id",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "sponsor_identifier",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "quarter_of_spending",
        "type": "DATE",
        "mode": "NULLABLE"
    },
    {
        "name": "quarter_of_funding",
        "type": "DATE",
        "mode": "NULLABLE"
    },
    {
        "name": "sponsor_id",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "sponsor_name",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "benefit_id",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "benefit_name",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "amount_funded",
        "type": "NUMERIC",
        "mode": "NULLABLE"
    },
    {
        "name": "amount_spent",
        "type": "NUMERIC",
        "mode": "NULLABLE"
    },
    {
        "name": "utilization_rate",
        "type": "NUMERIC",
        "mode": "NULLABLE"
    }
]
```

### `harmony_views.standardized_transaction_one_row_per_tx`

```json
[
    {
        "name": "standardized_transaction_id",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "sequence_id",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "member_id",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "sponsor_id",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "card_id",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "merchant_id",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "merchant_description",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "reason",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "transaction_id",
        "type": "INTEGER",
        "mode": "NULLABLE"
    },
    {
        "name": "prelim_transaction_id",
        "type": "INTEGER",
        "mode": "NULLABLE"
    },
    {
        "name": "approved",
        "type": "BOOLEAN",
        "mode": "NULLABLE"
    },
    {
        "name": "spending",
        "type": "BOOLEAN",
        "mode": "NULLABLE"
    },
    {
        "name": "state",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "amount_requested",
        "type": "NUMERIC",
        "mode": "NULLABLE"
    },
    {
        "name": "amount_approved",
        "type": "NUMERIC",
        "mode": "NULLABLE"
    },
    {
        "name": "sources",
        "type": "STRING",
        "mode": "REPEATED"
    },
    {
        "name": "occurred_at",
        "type": "TIMESTAMP",
        "mode": "NULLABLE"
    },
    {
        "name": "reversed_at",
        "type": "TIMESTAMP",
        "mode": "NULLABLE"
    },
    {
        "name": "settled_at",
        "type": "TIMESTAMP",
        "mode": "NULLABLE"
    },
    {
        "name": "created_at",
        "type": "TIMESTAMP",
        "mode": "NULLABLE"
    },
    {
        "name": "member",
        "type": "RECORD",
        "mode": "NULLABLE",
        "fields": [
            {
                "name": "member_id",
                "type": "STRING",
                "mode": "NULLABLE"
            },
            {
                "name": "sponsor_id",
                "type": "STRING",
                "mode": "NULLABLE"
            },
            {
                "name": "sponsor_identifier",
                "type": "STRING",
                "mode": "NULLABLE"
            },
            {
                "name": "processor_identifier",
                "type": "STRING",
                "mode": "NULLABLE"
            },
            {
                "name": "fis_identifier",
                "type": "INTEGER",
                "mode": "NULLABLE"
            },
            {
                "name": "last_login",
                "type": "TIMESTAMP",
                "mode": "NULLABLE"
            },
            {
                "name": "auth0_user_ids",
                "type": "STRING",
                "mode": "REPEATED"
            },
            {
                "name": "created_at",
                "type": "TIMESTAMP",
                "mode": "NULLABLE"
            },
            {
                "name": "updated_at",
                "type": "TIMESTAMP",
                "mode": "NULLABLE"
            },
            {
                "name": "deleted_at",
                "type": "TIMESTAMP",
                "mode": "NULLABLE"
            }
        ]
    },
    {
        "name": "sponsor",
        "type": "RECORD",
        "mode": "NULLABLE",
        "fields": [
            {
                "name": "sponsor_id",
                "type": "STRING",
                "mode": "NULLABLE"
            },
            {
                "name": "name",
                "type": "STRING",
                "mode": "NULLABLE"
            },
            {
                "name": "description",
                "type": "STRING",
                "mode": "NULLABLE"
            },
            {
                "name": "galileo_funding_account_prn",
                "type": "STRING",
                "mode": "NULLABLE"
            },
            {
                "name": "galileo_product_identifier",
                "type": "INTEGER",
                "mode": "NULLABLE"
            },
            {
                "name": "emboss_kit_identifier",
                "type": "INTEGER",
                "mode": "NULLABLE"
            },
            {
                "name": "uber_org_identifier",
                "type": "STRING",
                "mode": "NULLABLE"
            },
            {
                "name": "created_at",
                "type": "TIMESTAMP",
                "mode": "NULLABLE"
            }
        ]
    },
    {
        "name": "soda_transaction",
        "type": "RECORD",
        "mode": "NULLABLE",
        "fields": [
            {
                "name": "id",
                "type": "INTEGER",
                "mode": "NULLABLE"
            },
            {
                "name": "payee",
                "type": "STRING",
                "mode": "NULLABLE"
            },
            {
                "name": "effective_date",
                "type": "TIMESTAMP",
                "mode": "NULLABLE"
            },
            {
                "name": "created_at",
                "type": "TIMESTAMP",
                "mode": "NULLABLE"
            },
            {
                "name": "transaction_type",
                "type": "STRING",
                "mode": "NULLABLE"
            },
            {
                "name": "mcc",
                "type": "STRING",
                "mode": "NULLABLE"
            },
            {
                "name": "mid",
                "type": "STRING",
                "mode": "NULLABLE"
            },
            {
                "name": "reversal_id",
                "type": "INTEGER",
                "mode": "NULLABLE"
            }
        ]
    },
    {
        "name": "row_number",
        "type": "INTEGER",
        "mode": "NULLABLE"
    },
    {
        "name": "grouped_merchant_description",
        "type": "STRING",
        "mode": "NULLABLE"
    }
]
```

### `harmony_views.successful_trips`

```json
[
    {
        "name": "sponsor_id",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "sponsor_name",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "member_id_new",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "reason",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "merchant_name",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "created_at",
        "type": "TIMESTAMP",
        "mode": "NULLABLE"
    },
    {
        "name": "mcc",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "timekey",
        "type": "TIMESTAMP",
        "mode": "NULLABLE"
    },
    {
        "name": "number_of_swipes_in_trip",
        "type": "INTEGER",
        "mode": "NULLABLE"
    },
    {
        "name": "successful_trip_boolean",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "grouped_merchant_name",
        "type": "STRING",
        "mode": "NULLABLE"
    }
]
```

### `harmony_views.unsuccessful_trips`

```json
[
    {
        "name": "sponsor_id",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "sponsor_name",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "member_id_new",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "member_deleted_at",
        "type": "TIMESTAMP",
        "mode": "NULLABLE"
    },
    {
        "name": "reason",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "merchant_name",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "created_at",
        "type": "TIMESTAMP",
        "mode": "NULLABLE"
    },
    {
        "name": "mcc",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "timekey",
        "type": "TIMESTAMP",
        "mode": "NULLABLE"
    },
    {
        "name": "number_of_swipes_in_trip",
        "type": "INTEGER",
        "mode": "NULLABLE"
    },
    {
        "name": "successful_trip_boolean",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "grouped_merchant_name",
        "type": "STRING",
        "mode": "NULLABLE"
    }
]
```

### `harmony_views.year_of_funding_monthly_benefits`

```json
[
    {
        "name": "year_of_funding",
        "type": "DATE",
        "mode": "NULLABLE"
    },
    {
        "name": "sponsor_id",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "sponsor_name",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "benefit_id",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "benefit_name",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "amount",
        "type": "NUMERIC",
        "mode": "NULLABLE"
    },
    {
        "name": "Members_In_Plan_At_Some_Point_In_Period",
        "type": "INTEGER",
        "mode": "NULLABLE"
    }
]
```

### `harmony_views.year_of_funding_quarterly_benefits`

```json
[
    {
        "name": "year_of_funding",
        "type": "DATE",
        "mode": "NULLABLE"
    },
    {
        "name": "sponsor_id",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "sponsor_name",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "benefit_id",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "benefit_name",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "amount",
        "type": "NUMERIC",
        "mode": "NULLABLE"
    },
    {
        "name": "Members_In_Plan_At_Some_Point_In_Period",
        "type": "INTEGER",
        "mode": "NULLABLE"
    }
]
```

### `harmony_views.year_of_funding_yearly_benefits`

```json
[
    {
        "name": "year_of_funding",
        "type": "DATE",
        "mode": "NULLABLE"
    },
    {
        "name": "sponsor_id",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "sponsor_name",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "benefit_id",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "benefit_name",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "amount",
        "type": "NUMERIC",
        "mode": "NULLABLE"
    },
    {
        "name": "Members_In_Plan_At_Some_Point_In_Period",
        "type": "INTEGER",
        "mode": "NULLABLE"
    }
]
```

### `harmony_views.year_of_spending_monthly_benefits`

```json
[
    {
        "name": "year_of_spending",
        "type": "DATE",
        "mode": "NULLABLE"
    },
    {
        "name": "sponsor_id",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "sponsor_name",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "benefit_id",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "benefit_name",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "amount",
        "type": "NUMERIC",
        "mode": "NULLABLE"
    },
    {
        "name": "Utilizing_Members",
        "type": "INTEGER",
        "mode": "NULLABLE"
    },
    {
        "name": "Transaction_Count",
        "type": "INTEGER",
        "mode": "NULLABLE"
    },
    {
        "name": "Average_Transaction_Amount",
        "type": "NUMERIC",
        "mode": "NULLABLE"
    }
]
```

### `harmony_views.year_of_spending_quarterly_benefits`

```json
[
    {
        "name": "year_of_spending",
        "type": "DATE",
        "mode": "NULLABLE"
    },
    {
        "name": "sponsor_id",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "sponsor_name",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "benefit_id",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "benefit_name",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "amount",
        "type": "NUMERIC",
        "mode": "NULLABLE"
    },
    {
        "name": "Utilizing_Members",
        "type": "INTEGER",
        "mode": "NULLABLE"
    },
    {
        "name": "Transaction_Count",
        "type": "INTEGER",
        "mode": "NULLABLE"
    },
    {
        "name": "Average_Transaction_Amount",
        "type": "NUMERIC",
        "mode": "NULLABLE"
    }
]
```

### `harmony_views.year_of_spending_quarterly_benefits_2025`

```json
[
    {
        "name": "year_of_spending",
        "type": "DATE",
        "mode": "NULLABLE"
    },
    {
        "name": "sponsor_id",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "sponsor_name",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "benefit_id",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "benefit_name",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "amount",
        "type": "NUMERIC",
        "mode": "NULLABLE"
    },
    {
        "name": "Utilizing_Members",
        "type": "INTEGER",
        "mode": "NULLABLE"
    },
    {
        "name": "Transaction_Count",
        "type": "INTEGER",
        "mode": "NULLABLE"
    },
    {
        "name": "Average_Transaction_Amount",
        "type": "NUMERIC",
        "mode": "NULLABLE"
    }
]
```

### `harmony_views.year_of_spending_yearly_benefits`

```json
[
    {
        "name": "year_of_spending",
        "type": "DATE",
        "mode": "NULLABLE"
    },
    {
        "name": "sponsor_id",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "sponsor_name",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "benefit_id",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "benefit_name",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "amount",
        "type": "NUMERIC",
        "mode": "NULLABLE"
    },
    {
        "name": "Utilizing_Members",
        "type": "INTEGER",
        "mode": "NULLABLE"
    },
    {
        "name": "Transaction_Count",
        "type": "INTEGER",
        "mode": "NULLABLE"
    },
    {
        "name": "Average_Transaction_Amount",
        "type": "NUMERIC",
        "mode": "NULLABLE"
    }
]
```

### `harmony_views.yearly_transaction_count_by_member_and_benefit`

```json
[
    {
        "name": "year_of_spending",
        "type": "DATE",
        "mode": "NULLABLE"
    },
    {
        "name": "member_id",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "sponsor_id",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "sponsor_name",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "benefit_id",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "benefit_name",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "amount",
        "type": "NUMERIC",
        "mode": "NULLABLE"
    },
    {
        "name": "Utilizing_Members",
        "type": "INTEGER",
        "mode": "NULLABLE"
    },
    {
        "name": "Transaction_Count",
        "type": "INTEGER",
        "mode": "NULLABLE"
    },
    {
        "name": "Average_Transaction_Amount",
        "type": "NUMERIC",
        "mode": "NULLABLE"
    }
]
```

## Dataset: `ina_event_stream`

### `ina_event_stream.events`

```json
[
    {
        "name": "personRef",
        "type": "RECORD",
        "mode": "NULLABLE",
        "fields": [
            {
                "name": "harmony_member_id",
                "type": "STRING",
                "mode": "NULLABLE"
            },
            {
                "name": "person_id",
                "type": "STRING",
                "mode": "NULLABLE"
            }
        ]
    },
    {
        "name": "type",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "timestamp",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "source",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "details",
        "type": "STRING",
        "mode": "NULLABLE"
    }
]
```

### `ina_event_stream.member_aliases`

```json
[
    {
        "name": "member_id",
        "type": "STRING",
        "mode": "REQUIRED"
    },
    {
        "name": "alias_group",
        "type": "STRING",
        "mode": "REQUIRED"
    }
]
```

### `ina_event_stream.persons`

```json
[
    {
        "name": "person_id",
        "type": "STRING",
        "mode": "REQUIRED",
        "description": "Unique deterministic identifier for this person across all memberships"
    },
    {
        "name": "identifier",
        "type": "RECORD",
        "mode": "REQUIRED",
        "fields": [
            {
                "name": "harmony_fis_identifier",
                "type": "STRING",
                "mode": "REPEATED",
                "description": "List of Harmony FIS identifiers"
            },
            {
                "name": "auth0_user_ids",
                "type": "STRING",
                "mode": "REPEATED",
                "description": "List of Auth0 user IDs"
            },
            {
                "name": "memberships",
                "type": "RECORD",
                "mode": "REPEATED",
                "fields": [
                    {
                        "name": "member_id",
                        "type": "STRING",
                        "mode": "REQUIRED",
                        "description": "Unique identifier for the member in Harmony"
                    },
                    {
                        "name": "sponsor_id",
                        "type": "STRING",
                        "mode": "REQUIRED",
                        "description": "Unique identifier for the sponsor organization"
                    },
                    {
                        "name": "sponsor_identifier",
                        "type": "STRING",
                        "mode": "REQUIRED",
                        "description": "Human-readable identifier for the sponsor"
                    },
                    {
                        "name": "contract_id",
                        "type": "STRING",
                        "mode": "NULLABLE",
                        "description": "Contract identifier from member plan data"
                    },
                    {
                        "name": "plan_id",
                        "type": "STRING",
                        "mode": "NULLABLE",
                        "description": "Plan identifier from member plan data"
                    },
                    {
                        "name": "segment_id",
                        "type": "STRING",
                        "mode": "NULLABLE",
                        "description": "Segment identifier from member plan data"
                    },
                    {
                        "name": "sponsor_program_identifier",
                        "type": "STRING",
                        "mode": "NULLABLE",
                        "description": "Program identifier from program_enrollment.program.sponsor_identifier (e.g., H6743-025)"
                    },
                    {
                        "name": "member_state",
                        "type": "STRING",
                        "mode": "NULLABLE",
                        "description": "Harmony member lifecycle state (Active, Grace Period, Waiting for balance drain, Deleted)"
                    }
                ],
                "description": "List of membership records"
            },
            {
                "name": "salesforce_contact_ids",
                "type": "STRING",
                "mode": "REPEATED",
                "description": "List of Salesforce contact IDs"
            },
            {
                "name": "voice_call_contact_ids",
                "type": "STRING",
                "mode": "REPEATED",
                "description": "List of voice call contact IDs"
            },
            {
                "name": "harmony_ids",
                "type": "STRING",
                "mode": "REPEATED",
                "description": "List of Harmony IDs"
            },
            {
                "name": "phone_numbers",
                "type": "STRING",
                "mode": "REPEATED",
                "description": "List of phone numbers"
            }
        ],
        "description": "All identifiers associated with this person"
    },
    {
        "name": "demographic",
        "type": "RECORD",
        "mode": "REQUIRED",
        "fields": [
            {
                "name": "year_of_birth",
                "type": "INTEGER",
                "mode": "NULLABLE",
                "description": "Year the person was born"
            },
            {
                "name": "language_tag",
                "type": "STRING",
                "mode": "NULLABLE",
                "description": "Preferred language tag (e.g., 'en-US', 'es-MX')"
            },
            {
                "name": "us_state",
                "type": "STRING",
                "mode": "NULLABLE",
                "description": "US state where the person resides"
            }
        ],
        "description": "Demographic information for this person"
    }
]
```

### `ina_event_stream.reason_code_mapping`

```json
[
    {
        "name": "reason_code",
        "type": "STRING"
    },
    {
        "name": "outcome_category",
        "type": "STRING"
    },
    {
        "name": "description",
        "type": "STRING"
    }
]
```

## Dataset: `ina_experiments`

### `ina_experiments.member_aliases`

```json
[
    {
        "name": "member_id",
        "type": "STRING",
        "mode": "REQUIRED"
    },
    {
        "name": "alias_group",
        "type": "STRING",
        "mode": "REQUIRED"
    }
]
```

## Dataset: `ina_gold_vault`

### `ina_gold_vault.partners`

```json
[
    {
        "name": "partner_id",
        "type": "STRING",
        "mode": "NULLABLE",
        "description": "Unique Harmony partner identifier"
    },
    {
        "name": "name",
        "type": "STRING",
        "mode": "NULLABLE",
        "description": "Human-readable partner name"
    },
    {
        "name": "partner_type",
        "type": "STRING",
        "mode": "NULLABLE",
        "description": "Type of partner: 'sponsor', 'merchant', 'processor', or 'internal'"
    },
    {
        "name": "short_code",
        "type": "STRING",
        "mode": "NULLABLE",
        "description": "Short alphanumeric code used to identify this partner in integrations"
    },
    {
        "name": "created_at",
        "type": "TIMESTAMP",
        "mode": "NULLABLE",
        "description": "Timestamp when this partner was created in Harmony"
    }
]
```

### `ina_gold_vault.sponsors`

```json
[
    {
        "name": "sponsor_id",
        "type": "STRING",
        "mode": "NULLABLE",
        "description": "Unique Harmony sponsor identifier (CUID format)"
    },
    {
        "name": "name",
        "type": "STRING",
        "mode": "NULLABLE",
        "description": "Human-readable sponsor name"
    },
    {
        "name": "description",
        "type": "STRING",
        "mode": "NULLABLE",
        "description": "Free-text description of the sponsor, if provided"
    },
    {
        "name": "variant",
        "type": "STRING",
        "mode": "NULLABLE",
        "description": "Sponsor type: 'customer' (health plan) or 'brand' (sub-entity under a customer)"
    },
    {
        "name": "brand_name",
        "type": "STRING",
        "mode": "NULLABLE",
        "description": "Brand name when variant is 'brand'. NULL for customers."
    },
    {
        "name": "parent_id",
        "type": "STRING",
        "mode": "NULLABLE",
        "description": "For brands, the sponsor_id of the parent customer. NULL for customers."
    },
    {
        "name": "resolved_customer_id",
        "type": "STRING",
        "mode": "NULLABLE",
        "description": "The customer-level sponsor_id. For customers, this is their own ID. For brands, this is the parent customer's ID."
    },
    {
        "name": "resolved_customer_name",
        "type": "STRING",
        "mode": "NULLABLE",
        "description": "The customer-level sponsor name. For customers, this is their own name. For brands, this is the parent customer's name."
    },
    {
        "name": "created_at",
        "type": "TIMESTAMP",
        "mode": "NULLABLE",
        "description": "Timestamp when this sponsor was created in Harmony"
    }
]
```

### `ina_gold_vault.support_calls`

```json
[
    {
        "name": "call_record_id",
        "type": "STRING",
        "mode": "NULLABLE",
        "description": "Primary key \u2014 unified call record ID from harmony_export.call_records"
    },
    {
        "name": "agent_call_guid",
        "type": "STRING",
        "mode": "NULLABLE",
        "description": "Agent leg call GUID assigned by the telephony platform (NVMStatsSF__CallGuid__c)"
    },
    {
        "name": "ivr_call_sid",
        "type": "STRING",
        "mode": "NULLABLE",
        "description": "IVR leg session ID (Twilio call SID)"
    },
    {
        "name": "agent_conversation_guid",
        "type": "STRING",
        "mode": "NULLABLE",
        "description": "Agent leg conversation GUID linking related call legs"
    },
    {
        "name": "agent_call_summary_name",
        "type": "STRING",
        "mode": "NULLABLE",
        "description": "Salesforce NVM Call Summary record name (e.g. CS-00123456)"
    },
    {
        "name": "unified_record_type",
        "type": "STRING",
        "mode": "NULLABLE",
        "description": "Call record type: 'ivr_only', 'agent_only', or 'linked' (has both IVR and agent legs)"
    },
    {
        "name": "unified_call_direction",
        "type": "STRING",
        "mode": "NULLABLE",
        "description": "Call direction: 'inbound' or 'outbound'. Derived at silver layer from interaction_type."
    },
    {
        "name": "unified_call_status",
        "type": "STRING",
        "mode": "NULLABLE",
        "description": "Call outcome: 'abandoned', 'completed_with_agent', 'completed_ivr_only', or 'completed'. Derived at silver layer."
    },
    {
        "name": "unified_language",
        "type": "STRING",
        "mode": "NULLABLE",
        "description": "Call language in ISO format (en-US, es-US). IVR call_language preferred, falls back to skills_list."
    },
    {
        "name": "unified_is_anonymous",
        "type": "BOOLEAN",
        "mode": "NULLABLE",
        "description": "TRUE if the call could not be attributed to a specific member (no member_id on either leg)"
    },
    {
        "name": "call_start_time",
        "type": "TIMESTAMP",
        "mode": "NULLABLE",
        "description": "Unified call start timestamp (UTC) from the unified_call_record"
    },
    {
        "name": "call_end_time",
        "type": "TIMESTAMP",
        "mode": "NULLABLE",
        "description": "Unified call end timestamp (UTC) from the unified_call_record. Excludes ACW."
    },
    {
        "name": "call_date",
        "type": "DATE",
        "mode": "NULLABLE",
        "description": "Date of the call (from call_start_time). Partition key."
    },
    {
        "name": "utc_date",
        "type": "DATE",
        "mode": "NULLABLE",
        "description": "Call date in UTC (from agent call record utc_date field)"
    },
    {
        "name": "local_date",
        "type": "STRING",
        "mode": "NULLABLE",
        "description": "Call date in the caller's local timezone (YYYY-MM-DD string)"
    },
    {
        "name": "local_hour",
        "type": "STRING",
        "mode": "NULLABLE",
        "description": "Hour of day in the caller's local timezone"
    },
    {
        "name": "ivr_start_time",
        "type": "TIMESTAMP",
        "mode": "NULLABLE",
        "description": "IVR leg start timestamp (UTC)"
    },
    {
        "name": "ivr_end_time",
        "type": "TIMESTAMP",
        "mode": "NULLABLE",
        "description": "IVR leg end timestamp (UTC)"
    },
    {
        "name": "ivr_duration_seconds",
        "type": "INTEGER",
        "mode": "NULLABLE",
        "description": "IVR leg duration in seconds (ivr_call_record.call_duration_seconds)"
    },
    {
        "name": "ivr_call_status",
        "type": "STRING",
        "mode": "NULLABLE",
        "description": "IVR-specific call status from the IVR call record"
    },
    {
        "name": "ivr_call_outcome",
        "type": "STRING",
        "mode": "NULLABLE",
        "description": "IVR call outcome / last state from the IVR system"
    },
    {
        "name": "ivr_call_language",
        "type": "STRING",
        "mode": "NULLABLE",
        "description": "Language detected or selected during the IVR portion"
    },
    {
        "name": "ivr_identity_status",
        "type": "STRING",
        "mode": "NULLABLE",
        "description": "Member identity verification status from IVR (e.g. verified, unverified)"
    },
    {
        "name": "ivr_reached_agent",
        "type": "BOOLEAN",
        "mode": "NULLABLE",
        "description": "TRUE if the IVR determined the caller should reach a live agent"
    },
    {
        "name": "ivr_member_id",
        "type": "STRING",
        "mode": "NULLABLE",
        "description": "Raw member_id from the IVR leg (for audit / attribution conflict resolution)"
    },
    {
        "name": "ivr_sponsor_id",
        "type": "STRING",
        "mode": "NULLABLE",
        "description": "Raw sponsor_id from the IVR leg (for audit / attribution conflict resolution)"
    },
    {
        "name": "agent_start_time",
        "type": "TIMESTAMP",
        "mode": "NULLABLE",
        "description": "Agent leg start timestamp (UTC)"
    },
    {
        "name": "agent_end_time",
        "type": "TIMESTAMP",
        "mode": "NULLABLE",
        "description": "Agent leg end timestamp (UTC)"
    },
    {
        "name": "agent_total_call_duration_including_acw_seconds",
        "type": "INTEGER",
        "mode": "NULLABLE",
        "description": "SF-authoritative total call duration including after-call work in seconds (Total_Call_Duration_including_ACW__c)"
    },
    {
        "name": "agent_total_call_duration_seconds",
        "type": "INTEGER",
        "mode": "NULLABLE",
        "description": "Agent total call duration in seconds excluding ACW (NVMStatsSF__Total_Call_Duration__c)"
    },
    {
        "name": "agent_after_call_work_time_seconds",
        "type": "INTEGER",
        "mode": "NULLABLE",
        "description": "Time the agent spent on after-call work in seconds"
    },
    {
        "name": "agent_handle_time_seconds",
        "type": "INTEGER",
        "mode": "NULLABLE",
        "description": "Agent handle time in seconds \u2014 talk + hold + ACW (NVMStatsSF__Handle_Time__c)"
    },
    {
        "name": "agent_handle_time_over_10_minutes_seconds",
        "type": "INTEGER",
        "mode": "NULLABLE",
        "description": "Seconds of handle time exceeding 10 minutes (Handle_Time_Over_10_Minutes__c)"
    },
    {
        "name": "agent_talk_time_seconds",
        "type": "INTEGER",
        "mode": "NULLABLE",
        "description": "Time the agent spent actively talking with the caller in seconds"
    },
    {
        "name": "agent_consult_time_seconds",
        "type": "INTEGER",
        "mode": "NULLABLE",
        "description": "Time spent in agent consultation/conference in seconds"
    },
    {
        "name": "agent_hold_time_seconds",
        "type": "INTEGER",
        "mode": "NULLABLE",
        "description": "Time the caller was on hold during agent interaction in seconds"
    },
    {
        "name": "agent_external_consult_time_seconds",
        "type": "INTEGER",
        "mode": "NULLABLE",
        "description": "Time spent consulting an external party in seconds"
    },
    {
        "name": "agent_external_transfer_time_seconds",
        "type": "INTEGER",
        "mode": "NULLABLE",
        "description": "Time spent on external transfer in seconds"
    },
    {
        "name": "agent_queue_duration_seconds",
        "type": "INTEGER",
        "mode": "NULLABLE",
        "description": "Time the caller waited in queue before agent pickup in seconds"
    },
    {
        "name": "agent_meets_service_level",
        "type": "INTEGER",
        "mode": "NULLABLE",
        "description": "TRUE if the call met the default contractual service level (MeetsServiceLevel__c)"
    },
    {
        "name": "agent_call_met_service_level",
        "type": "INTEGER",
        "mode": "NULLABLE",
        "description": "TRUE if the call met the service level target (Call_Met_Service_Level__c)"
    },
    {
        "name": "agent_call_met_service_level_20_seconds",
        "type": "INTEGER",
        "mode": "NULLABLE",
        "description": "TRUE if the call was answered within 20 seconds"
    },
    {
        "name": "agent_call_met_service_level_45_seconds",
        "type": "INTEGER",
        "mode": "NULLABLE",
        "description": "TRUE if the call was answered within 45 seconds"
    },
    {
        "name": "agent_handled",
        "type": "BOOLEAN",
        "mode": "NULLABLE",
        "description": "TRUE if the call was handled by an agent (Handled__c)"
    },
    {
        "name": "agent_abandoned",
        "type": "BOOLEAN",
        "mode": "NULLABLE",
        "description": "TRUE if the call was abandoned before agent pickup (NVMStatsSF__Abandoned__c)"
    },
    {
        "name": "agent_short_abandon",
        "type": "BOOLEAN",
        "mode": "NULLABLE",
        "description": "TRUE if the call was abandoned within the default short-abandon threshold"
    },
    {
        "name": "agent_true_abandon",
        "type": "BOOLEAN",
        "mode": "NULLABLE",
        "description": "TRUE if the call was a true abandon \u2014 abandoned but not a short abandon (True_Abandon_Custom__c)"
    },
    {
        "name": "agent_short_abandon_20_seconds",
        "type": "BOOLEAN",
        "mode": "NULLABLE",
        "description": "TRUE if the call was abandoned within 20 seconds of entering queue"
    },
    {
        "name": "agent_short_abandon_30_seconds",
        "type": "BOOLEAN",
        "mode": "NULLABLE",
        "description": "TRUE if the call was abandoned within 30 seconds of entering queue"
    },
    {
        "name": "agent_short_abandon_45_seconds",
        "type": "BOOLEAN",
        "mode": "NULLABLE",
        "description": "TRUE if the call was abandoned within 45 seconds of entering queue"
    },
    {
        "name": "agent_offered",
        "type": "BOOLEAN",
        "mode": "NULLABLE",
        "description": "TRUE if the call was offered to the agent queue (Offered_Custom__c)"
    },
    {
        "name": "agent_last_state",
        "type": "STRING",
        "mode": "NULLABLE",
        "description": "Last telephony state of the agent leg (NVMStatsSF__Last_State__c)"
    },
    {
        "name": "agent_skills_list",
        "type": "STRING",
        "mode": "NULLABLE",
        "description": "Comma-separated list of agent skills required for this call"
    },
    {
        "name": "agent_queue_name",
        "type": "STRING",
        "mode": "NULLABLE",
        "description": "Name of the agent queue the call was routed to"
    },
    {
        "name": "agent_contact_reason",
        "type": "STRING",
        "mode": "NULLABLE",
        "description": "Primary reason for the call as categorized by the agent"
    },
    {
        "name": "agent_contact_sub_reason",
        "type": "STRING",
        "mode": "NULLABLE",
        "description": "Secondary/sub reason for the call"
    },
    {
        "name": "agent_interaction_type",
        "type": "STRING",
        "mode": "NULLABLE",
        "description": "Raw interaction type from telephony platform (e.g. 'Phone', 'Outbound Call')"
    },
    {
        "name": "agent_display_to_agent",
        "type": "STRING",
        "mode": "NULLABLE",
        "description": "Information displayed to the agent when the call connected"
    },
    {
        "name": "agent_case_id",
        "type": "STRING",
        "mode": "NULLABLE",
        "description": "Salesforce case ID linked to this call"
    },
    {
        "name": "agent_member_id",
        "type": "STRING",
        "mode": "NULLABLE",
        "description": "Raw member_id from the agent leg (for audit / attribution conflict resolution)"
    },
    {
        "name": "agent_sponsor_id",
        "type": "STRING",
        "mode": "NULLABLE",
        "description": "Raw sponsor_id from the agent leg (for audit / attribution conflict resolution)"
    },
    {
        "name": "agent_sponsor_name",
        "type": "STRING",
        "mode": "NULLABLE",
        "description": "Sponsor name from the agent leg (acr.sponsor_name)"
    },
    {
        "name": "agent_member_identifier",
        "type": "STRING",
        "mode": "NULLABLE",
        "description": "External member identifier from the agent leg (e.g. health plan member number)"
    },
    {
        "name": "unified_member_id",
        "type": "STRING",
        "mode": "NULLABLE",
        "description": "Attributed member ID. From event stream personRef when available, otherwise from call_records (agent-first, IVR fallback). NULL for anonymous calls."
    },
    {
        "name": "unified_sponsor_id",
        "type": "STRING",
        "mode": "NULLABLE",
        "description": "Unified sponsor ID \u2014 silver COALESCE(agent, name-resolved, IVR) with gold fallback to member's sponsor"
    },
    {
        "name": "unified_program_id",
        "type": "STRING",
        "mode": "NULLABLE",
        "description": "Program ID for the member's enrollment. Requires join through member enrollment path."
    },
    {
        "name": "calc_telephony_duration_minutes",
        "type": "FLOAT",
        "mode": "NULLABLE",
        "description": "Total telephony duration in minutes. IVR-only: timestamp diff. Linked: timestamp diff + ACW. Agent-only: SF-authoritative total_call_duration_including_acw."
    },
    {
        "name": "calc_agent_handle_minutes",
        "type": "FLOAT",
        "mode": "NULLABLE",
        "description": "Agent handle time in minutes (agent_handle_time_seconds / 60)"
    },
    {
        "name": "calc_agent_talk_minutes",
        "type": "FLOAT",
        "mode": "NULLABLE",
        "description": "Agent talk time in minutes (agent_talk_time_seconds / 60)"
    },
    {
        "name": "calc_queue_wait_minutes",
        "type": "FLOAT",
        "mode": "NULLABLE",
        "description": "Queue wait time in minutes (agent_queue_duration_seconds / 60)"
    },
    {
        "name": "calc_after_call_work_minutes",
        "type": "FLOAT",
        "mode": "NULLABLE",
        "description": "After-call work time in minutes (agent_after_call_work_time_seconds / 60)"
    },
    {
        "name": "calc_ivr_duration_minutes",
        "type": "FLOAT",
        "mode": "NULLABLE",
        "description": "IVR duration in minutes (ivr_duration_seconds / 60)"
    },
    {
        "name": "calc_total_agent_time_minutes",
        "type": "FLOAT",
        "mode": "NULLABLE",
        "description": "Total agent interaction time in minutes (handle time for calls that reached an agent)"
    },
    {
        "name": "calc_billable_telephony_minutes",
        "type": "FLOAT",
        "mode": "NULLABLE",
        "description": "Billable telephony minutes \u2014 CEIL of calc_telephony_duration_minutes to next whole minute"
    },
    {
        "name": "calc_agent_minutes_10min_cap_per_call",
        "type": "FLOAT",
        "mode": "NULLABLE",
        "description": "Agent handle minutes capped at 10 minutes per call for billing"
    },
    {
        "name": "calc_handle_time_cap_correction_minutes",
        "type": "FLOAT",
        "mode": "NULLABLE",
        "description": "Amount of handle time trimmed by the 10-minute cap (excess over 10 min, 0 if under)"
    },
    {
        "name": "call_year_month",
        "type": "STRING",
        "mode": "NULLABLE",
        "description": "Year-month of the call (YYYY-MM format) for monthly aggregation"
    },
    {
        "name": "call_year_week",
        "type": "STRING",
        "mode": "NULLABLE",
        "description": "ISO year-week of the call (GGGG-WVV format, Monday-start) for weekly aggregation"
    },
    {
        "name": "call_day_of_week",
        "type": "INTEGER",
        "mode": "NULLABLE",
        "description": "Day of week (1=Sunday, 7=Saturday) for day-of-week analysis"
    },
    {
        "name": "voice_call_contact_id",
        "type": "STRING",
        "mode": "NULLABLE",
        "description": "Salesforce Voice Call contact record ID"
    },
    {
        "name": "related_sf_account_id",
        "type": "STRING",
        "mode": "NULLABLE",
        "description": "Related Salesforce account ID"
    },
    {
        "name": "related_sf_contact_id",
        "type": "STRING",
        "mode": "NULLABLE",
        "description": "Related Salesforce contact ID"
    },
    {
        "name": "data_loaded_at",
        "type": "TIMESTAMP",
        "mode": "NULLABLE",
        "description": "Timestamp when this record was loaded into the silver call_records table"
    },
    {
        "name": "etl_run_at",
        "type": "TIMESTAMP",
        "mode": "NULLABLE",
        "description": "Timestamp when this gold ETL run produced this record"
    }
]
```

### `ina_playground.benefit_active_members`

```json
[
    {
        "name": "snapshot_date",
        "type": "DATE"
    },
    {
        "name": "sponsor_id",
        "type": "STRING"
    },
    {
        "name": "benefit_id",
        "type": "STRING"
    },
    {
        "name": "benefit_name",
        "type": "STRING"
    },
    {
        "name": "benefit_type",
        "type": "STRING"
    },
    {
        "name": "sponsor_identifier",
        "type": "STRING"
    },
    {
        "name": "duration",
        "type": "STRING"
    },
    {
        "name": "active_members",
        "type": "INTEGER"
    },
    {
        "name": "brand_id",
        "type": "STRING"
    },
    {
        "name": "brand_name",
        "type": "STRING"
    },
    {
        "name": "customer_id",
        "type": "STRING"
    },
    {
        "name": "sponsor_name",
        "type": "STRING"
    },
    {
        "name": "benefit_name_specific",
        "type": "STRING"
    }
]
```

### `ina_playground.benefit_daily_lifecycle`

```json
[
    {
        "name": "date",
        "type": "DATE"
    },
    {
        "name": "sponsor_id",
        "type": "STRING"
    },
    {
        "name": "benefit_id",
        "type": "STRING"
    },
    {
        "name": "benefit_type",
        "type": "STRING"
    },
    {
        "name": "benefit_name",
        "type": "STRING"
    },
    {
        "name": "created_count",
        "type": "INTEGER"
    },
    {
        "name": "deleted_count",
        "type": "INTEGER"
    },
    {
        "name": "brand_id",
        "type": "STRING"
    },
    {
        "name": "brand_name",
        "type": "STRING"
    },
    {
        "name": "customer_id",
        "type": "STRING"
    },
    {
        "name": "sponsor_name",
        "type": "STRING"
    }
]
```

### `ina_playground.benefit_merchant_spend`

```json
[
    {
        "name": "spend_date",
        "type": "DATE"
    },
    {
        "name": "sponsor_id",
        "type": "STRING"
    },
    {
        "name": "member_sponsor_identifier",
        "type": "STRING"
    },
    {
        "name": "benefit_name",
        "type": "STRING"
    },
    {
        "name": "benefit_id",
        "type": "STRING"
    },
    {
        "name": "benefit_type",
        "type": "STRING"
    },
    {
        "name": "sponsor_identifier",
        "type": "STRING"
    },
    {
        "name": "merchant_grouped",
        "type": "STRING"
    },
    {
        "name": "merchant_mcc",
        "type": "STRING"
    },
    {
        "name": "total_spent",
        "type": "FLOAT"
    },
    {
        "name": "transaction_count",
        "type": "INTEGER"
    },
    {
        "name": "brand_id",
        "type": "STRING"
    },
    {
        "name": "brand_name",
        "type": "STRING"
    },
    {
        "name": "customer_id",
        "type": "STRING"
    },
    {
        "name": "sponsor_name",
        "type": "STRING"
    }
]
```

### `ina_playground.benefit_reference`

```json
[
    {
        "name": "benefit_id",
        "type": "STRING"
    },
    {
        "name": "benefit_name",
        "type": "STRING"
    },
    {
        "name": "benefit_type",
        "type": "STRING"
    },
    {
        "name": "sponsor_id",
        "type": "STRING"
    },
    {
        "name": "sponsor_identifier",
        "type": "STRING"
    }
]
```

### `ina_playground.benefit_spend_daily`

```json
[
    {
        "name": "spend_date",
        "type": "DATE"
    },
    {
        "name": "sponsor_id",
        "type": "STRING"
    },
    {
        "name": "benefit_id",
        "type": "STRING"
    },
    {
        "name": "benefit_name",
        "type": "STRING"
    },
    {
        "name": "benefit_type",
        "type": "STRING"
    },
    {
        "name": "sponsor_identifier",
        "type": "STRING"
    },
    {
        "name": "total_spent",
        "type": "FLOAT"
    },
    {
        "name": "transaction_count",
        "type": "INTEGER"
    },
    {
        "name": "unique_members",
        "type": "INTEGER"
    },
    {
        "name": "brand_id",
        "type": "STRING"
    },
    {
        "name": "brand_name",
        "type": "STRING"
    },
    {
        "name": "customer_id",
        "type": "STRING"
    },
    {
        "name": "sponsor_name",
        "type": "STRING"
    }
]
```

### `ina_playground.benefit_utilization_daily`

```json
[
    {
        "name": "spend_date",
        "type": "DATE"
    },
    {
        "name": "sponsor_id",
        "type": "STRING"
    },
    {
        "name": "benefit_id",
        "type": "STRING"
    },
    {
        "name": "benefit_name",
        "type": "STRING"
    },
    {
        "name": "benefit_type",
        "type": "STRING"
    },
    {
        "name": "sponsor_identifier",
        "type": "STRING"
    },
    {
        "name": "period_start",
        "type": "DATE"
    },
    {
        "name": "period_end",
        "type": "DATE"
    },
    {
        "name": "daily_spent",
        "type": "FLOAT"
    },
    {
        "name": "cumulative_spent",
        "type": "FLOAT"
    },
    {
        "name": "total_funded",
        "type": "FLOAT"
    },
    {
        "name": "utilization_rate",
        "type": "FLOAT"
    },
    {
        "name": "days_into_period",
        "type": "INTEGER"
    },
    {
        "name": "brand_id",
        "type": "STRING"
    },
    {
        "name": "brand_name",
        "type": "STRING"
    },
    {
        "name": "customer_id",
        "type": "STRING"
    },
    {
        "name": "sponsor_name",
        "type": "STRING"
    }
]
```

### `ina_playground.benefit_utilization_quarterly`

```json
[
    {
        "name": "quarter",
        "type": "STRING"
    },
    {
        "name": "quarter_start",
        "type": "DATE"
    },
    {
        "name": "quarter_end",
        "type": "DATE"
    },
    {
        "name": "sponsor_id",
        "type": "STRING"
    },
    {
        "name": "benefit_id",
        "type": "STRING"
    },
    {
        "name": "benefit_name",
        "type": "STRING"
    },
    {
        "name": "benefit_type",
        "type": "STRING"
    },
    {
        "name": "sponsor_identifier",
        "type": "STRING"
    },
    {
        "name": "category",
        "type": "STRING"
    },
    {
        "name": "total_funded",
        "type": "FLOAT"
    },
    {
        "name": "total_spent",
        "type": "FLOAT"
    },
    {
        "name": "utilization_rate",
        "type": "FLOAT"
    },
    {
        "name": "active_enrollments",
        "type": "INTEGER"
    },
    {
        "name": "brand_id",
        "type": "STRING"
    },
    {
        "name": "brand_name",
        "type": "STRING"
    },
    {
        "name": "customer_id",
        "type": "STRING"
    },
    {
        "name": "sponsor_name",
        "type": "STRING"
    }
]
```

### `ina_playground.card_daily_snapshot`

```json
[
    {
        "name": "date",
        "type": "DATE",
        "mode": "NULLABLE"
    },
    {
        "name": "sponsor_id",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "contract_id",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "plan_id",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "segment_id",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "program_id",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "language",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "activation_count",
        "type": "INTEGER",
        "mode": "NULLABLE"
    },
    {
        "name": "brand_id",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "brand_name",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "customer_id",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "sponsor_name",
        "type": "STRING",
        "mode": "NULLABLE"
    }
]
```

### `ina_playground.card_metrics`

```json
[
    {
        "name": "customer_id",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "brand_id",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "brand_name",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "sponsor_id",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "contract_id",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "plan_id",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "segment_id",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "program_id",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "language",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "sum_age_inactive_cards",
        "type": "INTEGER",
        "mode": "NULLABLE"
    },
    {
        "name": "total_inactive_cards",
        "type": "INTEGER",
        "mode": "NULLABLE"
    },
    {
        "name": "sum_days_creation_to_activation",
        "type": "INTEGER",
        "mode": "NULLABLE"
    },
    {
        "name": "total_cards_activated",
        "type": "INTEGER",
        "mode": "NULLABLE"
    }
]
```

### `ina_playground.card_summary`

```json
[
    {
        "name": "person_id",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "member_id",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "card_id",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "sponsor_id",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "program_id",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "language",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "card_type",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "processor",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "processor_status",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "status",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "display_status",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "is_replacement",
        "type": "BOOLEAN",
        "mode": "NULLABLE"
    },
    {
        "name": "replacement_reason",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "last_four",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "created_at",
        "type": "TIMESTAMP",
        "mode": "NULLABLE"
    },
    {
        "name": "shipped_at",
        "type": "TIMESTAMP",
        "mode": "NULLABLE"
    },
    {
        "name": "activated_at",
        "type": "TIMESTAMP",
        "mode": "NULLABLE"
    },
    {
        "name": "issued_at",
        "type": "TIMESTAMP",
        "mode": "NULLABLE"
    },
    {
        "name": "brand_id",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "brand_name",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "customer_id",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "sponsor_name",
        "type": "STRING",
        "mode": "NULLABLE"
    }
]
```

### `ina_playground.care_call_stats_aggregated`

```json
[
    {
        "name": "time_period",
        "type": "STRING"
    },
    {
        "name": "period_type",
        "type": "STRING"
    },
    {
        "name": "call_date",
        "type": "DATE"
    },
    {
        "name": "language",
        "type": "STRING"
    },
    {
        "name": "offered",
        "type": "INTEGER"
    },
    {
        "name": "handled",
        "type": "INTEGER"
    },
    {
        "name": "abandoned",
        "type": "INTEGER"
    },
    {
        "name": "short_abandon",
        "type": "INTEGER"
    },
    {
        "name": "abandon_pct",
        "type": "FLOAT"
    },
    {
        "name": "aht_seconds",
        "type": "FLOAT"
    },
    {
        "name": "att_seconds",
        "type": "FLOAT"
    },
    {
        "name": "ahdt_seconds",
        "type": "FLOAT"
    },
    {
        "name": "acw_seconds",
        "type": "FLOAT"
    },
    {
        "name": "asa_seconds",
        "type": "FLOAT"
    },
    {
        "name": "record_count",
        "type": "INTEGER"
    },
    {
        "name": "sponsor_id",
        "type": "STRING"
    },
    {
        "name": "sponsor_name",
        "type": "STRING"
    },
    {
        "name": "customer_id",
        "type": "STRING"
    },
    {
        "name": "brand_id",
        "type": "STRING"
    },
    {
        "name": "brand_name",
        "type": "STRING"
    }
]
```

### `ina_playground.care_call_summary`

```json
[
    {
        "name": "call_id",
        "type": "STRING"
    },
    {
        "name": "call_guid",
        "type": "STRING"
    },
    {
        "name": "member_id",
        "type": "STRING"
    },
    {
        "name": "sponsor",
        "type": "STRING"
    },
    {
        "name": "plan_id",
        "type": "STRING"
    },
    {
        "name": "contract_id",
        "type": "STRING"
    },
    {
        "name": "queue_name",
        "type": "STRING"
    },
    {
        "name": "language",
        "type": "STRING"
    },
    {
        "name": "skills_list",
        "type": "STRING"
    },
    {
        "name": "call_start_time",
        "type": "TIMESTAMP"
    },
    {
        "name": "call_end_time",
        "type": "TIMESTAMP"
    },
    {
        "name": "call_date",
        "type": "DATE"
    },
    {
        "name": "local_date",
        "type": "STRING"
    },
    {
        "name": "local_hour",
        "type": "STRING"
    },
    {
        "name": "interaction_type_raw",
        "type": "STRING"
    },
    {
        "name": "call_direction",
        "type": "STRING"
    },
    {
        "name": "call_status",
        "type": "STRING"
    },
    {
        "name": "call_outcome",
        "type": "STRING"
    },
    {
        "name": "reached_agent",
        "type": "BOOLEAN"
    },
    {
        "name": "abandoned",
        "type": "BOOLEAN"
    },
    {
        "name": "handled",
        "type": "BOOLEAN"
    },
    {
        "name": "total_duration_minutes",
        "type": "FLOAT"
    },
    {
        "name": "handle_time_minutes",
        "type": "FLOAT"
    },
    {
        "name": "queue_wait_minutes",
        "type": "FLOAT"
    },
    {
        "name": "ivr_only_minutes",
        "type": "FLOAT"
    },
    {
        "name": "total_duration_seconds",
        "type": "FLOAT"
    },
    {
        "name": "handle_time_seconds",
        "type": "FLOAT"
    },
    {
        "name": "agent_talk_time_seconds",
        "type": "FLOAT"
    },
    {
        "name": "queue_duration_seconds",
        "type": "FLOAT"
    },
    {
        "name": "after_call_work_time_seconds",
        "type": "FLOAT"
    },
    {
        "name": "meets_service_level",
        "type": "BOOLEAN"
    },
    {
        "name": "call_met_service_level",
        "type": "BOOLEAN"
    },
    {
        "name": "short_abandon",
        "type": "BOOLEAN"
    },
    {
        "name": "true_abandon",
        "type": "BOOLEAN"
    },
    {
        "name": "contact_reason",
        "type": "STRING"
    },
    {
        "name": "contact_sub_reason",
        "type": "STRING"
    },
    {
        "name": "caller_phone",
        "type": "STRING"
    },
    {
        "name": "display_to_agent",
        "type": "STRING"
    },
    {
        "name": "ivr_only",
        "type": "BOOLEAN"
    },
    {
        "name": "offered",
        "type": "BOOLEAN"
    },
    {
        "name": "event_timestamp",
        "type": "STRING"
    },
    {
        "name": "is_anonymous",
        "type": "BOOLEAN"
    },
    {
        "name": "sponsor_id",
        "type": "STRING"
    },
    {
        "name": "sponsor_identifier",
        "type": "STRING"
    },
    {
        "name": "segment_id",
        "type": "STRING"
    },
    {
        "name": "program_id",
        "type": "STRING"
    },
    {
        "name": "call_year",
        "type": "INTEGER"
    },
    {
        "name": "call_month",
        "type": "INTEGER"
    },
    {
        "name": "call_week",
        "type": "INTEGER"
    },
    {
        "name": "call_day_of_week",
        "type": "INTEGER"
    },
    {
        "name": "call_year_month",
        "type": "STRING"
    },
    {
        "name": "call_year_week",
        "type": "STRING"
    },
    {
        "name": "total_duration_minutes_filled",
        "type": "FLOAT"
    },
    {
        "name": "handle_time_minutes_filled",
        "type": "FLOAT"
    },
    {
        "name": "met_30_second_sla",
        "type": "BOOLEAN"
    },
    {
        "name": "brand_id",
        "type": "STRING"
    },
    {
        "name": "brand_name",
        "type": "STRING"
    },
    {
        "name": "customer_id",
        "type": "STRING"
    },
    {
        "name": "sponsor_name",
        "type": "STRING"
    }
]
```

### `ina_playground.care_daily_metrics`

```json
[
    {
        "name": "date",
        "type": "DATE"
    },
    {
        "name": "sponsor_id",
        "type": "STRING"
    },
    {
        "name": "sponsor",
        "type": "STRING"
    },
    {
        "name": "queue_name",
        "type": "STRING"
    },
    {
        "name": "language",
        "type": "STRING"
    },
    {
        "name": "call_direction",
        "type": "STRING"
    },
    {
        "name": "segment_id",
        "type": "STRING"
    },
    {
        "name": "program_id",
        "type": "STRING"
    },
    {
        "name": "total_calls",
        "type": "INTEGER"
    },
    {
        "name": "inbound_calls",
        "type": "INTEGER"
    },
    {
        "name": "outbound_calls",
        "type": "INTEGER"
    },
    {
        "name": "offered_calls",
        "type": "INTEGER"
    },
    {
        "name": "handled_calls",
        "type": "INTEGER"
    },
    {
        "name": "abandoned_calls",
        "type": "INTEGER"
    },
    {
        "name": "reached_agent_calls",
        "type": "INTEGER"
    },
    {
        "name": "ivr_only_calls",
        "type": "INTEGER"
    },
    {
        "name": "short_abandon_calls",
        "type": "INTEGER"
    },
    {
        "name": "true_abandon_calls",
        "type": "INTEGER"
    },
    {
        "name": "calls_met_service_level",
        "type": "INTEGER"
    },
    {
        "name": "calls_met_30s_sla",
        "type": "INTEGER"
    },
    {
        "name": "total_duration_minutes",
        "type": "FLOAT"
    },
    {
        "name": "handle_time_minutes",
        "type": "FLOAT"
    },
    {
        "name": "queue_wait_minutes",
        "type": "FLOAT"
    },
    {
        "name": "ivr_only_minutes",
        "type": "FLOAT"
    },
    {
        "name": "total_agent_talk_time_seconds",
        "type": "FLOAT"
    },
    {
        "name": "total_queue_duration_seconds",
        "type": "FLOAT"
    },
    {
        "name": "total_after_call_work_seconds",
        "type": "FLOAT"
    },
    {
        "name": "avg_handle_time_seconds",
        "type": "FLOAT"
    },
    {
        "name": "avg_agent_talk_time_seconds",
        "type": "FLOAT"
    },
    {
        "name": "avg_queue_duration_seconds",
        "type": "FLOAT"
    },
    {
        "name": "avg_after_call_work_seconds",
        "type": "FLOAT"
    },
    {
        "name": "avg_speed_of_answer_seconds",
        "type": "FLOAT"
    },
    {
        "name": "handled_pct",
        "type": "FLOAT"
    },
    {
        "name": "abandoned_pct",
        "type": "FLOAT"
    },
    {
        "name": "service_level_pct",
        "type": "FLOAT"
    },
    {
        "name": "sla_30s_pct",
        "type": "FLOAT"
    },
    {
        "name": "brand_id",
        "type": "STRING"
    },
    {
        "name": "brand_name",
        "type": "STRING"
    },
    {
        "name": "customer_id",
        "type": "STRING"
    },
    {
        "name": "sponsor_name",
        "type": "STRING"
    }
]
```

### `ina_playground.events`

```json
[
    {
        "name": "personRef",
        "type": "RECORD",
        "mode": "NULLABLE",
        "fields": [
            {
                "name": "harmony_member_id",
                "type": "STRING",
                "mode": "NULLABLE"
            },
            {
                "name": "person_id",
                "type": "STRING",
                "mode": "NULLABLE"
            }
        ]
    },
    {
        "name": "type",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "timestamp",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "source",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "details",
        "type": "STRING",
        "mode": "NULLABLE"
    }
]
```

### `ina_playground.member_card_combined`

```json
[
    {
        "name": "person_id",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "member_id",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "sponsor_id",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "sponsor_identifier",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "birth_year",
        "type": "INTEGER",
        "mode": "NULLABLE"
    },
    {
        "name": "language",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "state",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "contract_id",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "plan_id",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "segment_id",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "program_id",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "created_at",
        "type": "TIMESTAMP",
        "mode": "NULLABLE"
    },
    {
        "name": "activated_at",
        "type": "TIMESTAMP",
        "mode": "NULLABLE"
    },
    {
        "name": "deactivated_at",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "status",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "brand_id",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "brand_name",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "customer_id",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "sponsor_name",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "card_count",
        "type": "INTEGER",
        "mode": "NULLABLE"
    },
    {
        "name": "active_card_count",
        "type": "INTEGER",
        "mode": "NULLABLE"
    },
    {
        "name": "shipped_card_count",
        "type": "INTEGER",
        "mode": "NULLABLE"
    },
    {
        "name": "created_card_count",
        "type": "INTEGER",
        "mode": "NULLABLE"
    },
    {
        "name": "cancelled_card_count",
        "type": "INTEGER",
        "mode": "NULLABLE"
    },
    {
        "name": "inactive_cards_shipped_over_60_days",
        "type": "INTEGER",
        "mode": "NULLABLE"
    },
    {
        "name": "has_inactive_card_shipped_over_60_days",
        "type": "BOOLEAN",
        "mode": "NULLABLE"
    },
    {
        "name": "cards",
        "type": "RECORD",
        "mode": "REPEATED",
        "fields": [
            {
                "name": "card_id",
                "type": "STRING",
                "mode": "NULLABLE"
            },
            {
                "name": "card_type",
                "type": "STRING",
                "mode": "NULLABLE"
            },
            {
                "name": "processor",
                "type": "STRING",
                "mode": "NULLABLE"
            },
            {
                "name": "status",
                "type": "STRING",
                "mode": "NULLABLE"
            },
            {
                "name": "processor_status",
                "type": "STRING",
                "mode": "NULLABLE"
            },
            {
                "name": "is_replacement",
                "type": "BOOLEAN",
                "mode": "NULLABLE"
            },
            {
                "name": "last_four",
                "type": "STRING",
                "mode": "NULLABLE"
            },
            {
                "name": "created_at",
                "type": "TIMESTAMP",
                "mode": "NULLABLE"
            },
            {
                "name": "shipped_at",
                "type": "TIMESTAMP",
                "mode": "NULLABLE"
            },
            {
                "name": "activated_at",
                "type": "TIMESTAMP",
                "mode": "NULLABLE"
            }
        ]
    }
]
```

### `ina_playground.member_card_status`

```json
[
    {
        "name": "member_id",
        "type": "STRING"
    },
    {
        "name": "sponsor_id",
        "type": "STRING"
    },
    {
        "name": "status",
        "type": "STRING"
    },
    {
        "name": "card_count",
        "type": "INTEGER"
    },
    {
        "name": "active_card_count",
        "type": "INTEGER"
    },
    {
        "name": "has_card",
        "type": "BOOLEAN"
    },
    {
        "name": "brand_id",
        "type": "STRING"
    },
    {
        "name": "brand_name",
        "type": "STRING"
    },
    {
        "name": "customer_id",
        "type": "STRING"
    },
    {
        "name": "sponsor_name",
        "type": "STRING"
    }
]
```

### `ina_playground.member_daily_creation`

```json
[
    {
        "name": "date",
        "type": "DATE"
    },
    {
        "name": "sponsor_id",
        "type": "STRING"
    },
    {
        "name": "contract_id",
        "type": "STRING"
    },
    {
        "name": "plan_id",
        "type": "STRING"
    },
    {
        "name": "segment_id",
        "type": "STRING"
    },
    {
        "name": "program_id",
        "type": "STRING"
    },
    {
        "name": "plan_name",
        "type": "STRING"
    },
    {
        "name": "language",
        "type": "STRING"
    },
    {
        "name": "member_count",
        "type": "INTEGER"
    },
    {
        "name": "card_count",
        "type": "INTEGER"
    },
    {
        "name": "brand_id",
        "type": "STRING"
    },
    {
        "name": "brand_name",
        "type": "STRING"
    },
    {
        "name": "customer_id",
        "type": "STRING"
    },
    {
        "name": "sponsor_name",
        "type": "STRING"
    }
]
```

### `ina_playground.member_daily_deactivation`

```json
[
    {
        "name": "date",
        "type": "DATE"
    },
    {
        "name": "sponsor_id",
        "type": "STRING"
    },
    {
        "name": "sponsor_name",
        "type": "STRING"
    },
    {
        "name": "contract_id",
        "type": "STRING"
    },
    {
        "name": "plan_id",
        "type": "STRING"
    },
    {
        "name": "segment_id",
        "type": "STRING"
    },
    {
        "name": "program_id",
        "type": "STRING"
    },
    {
        "name": "deactivation_count",
        "type": "INTEGER"
    },
    {
        "name": "brand_id",
        "type": "STRING"
    },
    {
        "name": "brand_name",
        "type": "STRING"
    },
    {
        "name": "customer_id",
        "type": "STRING"
    }
]
```

### `ina_playground.member_daily_snapshot`

```json
[
    {
        "name": "date",
        "type": "DATE",
        "mode": "NULLABLE"
    },
    {
        "name": "sponsor_id",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "contract_id",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "plan_id",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "segment_id",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "program_id",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "language",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "status",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "member_count",
        "type": "INTEGER",
        "mode": "NULLABLE"
    },
    {
        "name": "brand_id",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "brand_name",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "customer_id",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "sponsor_name",
        "type": "STRING",
        "mode": "NULLABLE"
    }
]
```

### `ina_playground.member_deactivation_scheduled`

```json
[
    {
        "name": "member_id",
        "type": "STRING"
    },
    {
        "name": "sponsor_id",
        "type": "STRING"
    },
    {
        "name": "sponsor_identifier",
        "type": "STRING"
    },
    {
        "name": "scheduled_deactivation_at",
        "type": "TIMESTAMP"
    },
    {
        "name": "reason",
        "type": "STRING"
    },
    {
        "name": "scheduled_timestamp",
        "type": "STRING"
    },
    {
        "name": "brand_id",
        "type": "STRING"
    },
    {
        "name": "brand_name",
        "type": "STRING"
    },
    {
        "name": "customer_id",
        "type": "STRING"
    },
    {
        "name": "sponsor_name",
        "type": "STRING"
    }
]
```

### `ina_playground.member_detail_view`

```json
[
    {
        "name": "member_id",
        "type": "STRING"
    },
    {
        "name": "sponsor_id",
        "type": "STRING"
    },
    {
        "name": "sponsor_identifier",
        "type": "STRING"
    },
    {
        "name": "status",
        "type": "STRING"
    },
    {
        "name": "created_at",
        "type": "STRING"
    },
    {
        "name": "deactivated_at",
        "type": "STRING"
    },
    {
        "name": "birth_year",
        "type": "INTEGER"
    },
    {
        "name": "language",
        "type": "STRING"
    },
    {
        "name": "state",
        "type": "STRING"
    },
    {
        "name": "contract_id",
        "type": "STRING"
    },
    {
        "name": "plan_id",
        "type": "STRING"
    },
    {
        "name": "segment_id",
        "type": "STRING"
    },
    {
        "name": "program_id",
        "type": "STRING"
    },
    {
        "name": "benefit_count",
        "type": "INTEGER"
    },
    {
        "name": "card_id",
        "type": "STRING"
    },
    {
        "name": "card_status",
        "type": "STRING"
    },
    {
        "name": "card_created_at",
        "type": "TIMESTAMP"
    },
    {
        "name": "card_activated_at",
        "type": "TIMESTAMP"
    },
    {
        "name": "card_shipped_at",
        "type": "TIMESTAMP"
    },
    {
        "name": "card_last_four",
        "type": "STRING"
    },
    {
        "name": "brand_id",
        "type": "STRING"
    },
    {
        "name": "brand_name",
        "type": "STRING"
    },
    {
        "name": "customer_id",
        "type": "STRING"
    },
    {
        "name": "sponsor_name",
        "type": "STRING"
    }
]
```

### `ina_playground.member_eligibility_summary`

```json
[
    {
        "name": "person_id",
        "type": "STRING"
    },
    {
        "name": "member_id",
        "type": "STRING"
    },
    {
        "name": "sponsor_id",
        "type": "STRING"
    },
    {
        "name": "sponsor_identifier",
        "type": "STRING"
    },
    {
        "name": "birth_year",
        "type": "INTEGER"
    },
    {
        "name": "language",
        "type": "STRING"
    },
    {
        "name": "state",
        "type": "STRING"
    },
    {
        "name": "contract_id",
        "type": "STRING"
    },
    {
        "name": "plan_id",
        "type": "STRING"
    },
    {
        "name": "segment_id",
        "type": "STRING"
    },
    {
        "name": "program_id",
        "type": "STRING"
    },
    {
        "name": "created_at",
        "type": "STRING"
    },
    {
        "name": "deactivated_at",
        "type": "STRING"
    },
    {
        "name": "enrollment_id",
        "type": "STRING"
    },
    {
        "name": "benefit_id",
        "type": "STRING"
    },
    {
        "name": "benefit_type",
        "type": "STRING"
    },
    {
        "name": "benefit_name",
        "type": "STRING"
    },
    {
        "name": "benefit_active_at",
        "type": "TIMESTAMP"
    },
    {
        "name": "benefit_expires_at",
        "type": "TIMESTAMP"
    },
    {
        "name": "status",
        "type": "STRING"
    },
    {
        "name": "brand_id",
        "type": "STRING"
    },
    {
        "name": "brand_name",
        "type": "STRING"
    },
    {
        "name": "customer_id",
        "type": "STRING"
    },
    {
        "name": "sponsor_name",
        "type": "STRING"
    }
]
```

### `ina_playground.member_multi_plan`

```json
[
    {
        "name": "member_id",
        "type": "STRING"
    },
    {
        "name": "sponsor_id",
        "type": "STRING"
    },
    {
        "name": "sponsor_name",
        "type": "STRING"
    },
    {
        "name": "contract_id",
        "type": "STRING"
    },
    {
        "name": "plan_id",
        "type": "STRING"
    },
    {
        "name": "segment_id",
        "type": "STRING"
    },
    {
        "name": "program_id",
        "type": "STRING"
    },
    {
        "name": "plan_count",
        "type": "INTEGER"
    },
    {
        "name": "plan_ids",
        "type": "STRING"
    },
    {
        "name": "benefits",
        "type": "STRING"
    },
    {
        "name": "brand_id",
        "type": "STRING"
    },
    {
        "name": "brand_name",
        "type": "STRING"
    },
    {
        "name": "customer_id",
        "type": "STRING"
    }
]
```

### `ina_playground.member_summary`

```json
[
    {
        "name": "person_id",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "member_id",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "sponsor_id",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "sponsor_identifier",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "birth_year",
        "type": "INTEGER",
        "mode": "NULLABLE"
    },
    {
        "name": "language",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "state",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "contract_id",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "plan_id",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "segment_id",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "program_id",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "created_at",
        "type": "TIMESTAMP",
        "mode": "NULLABLE"
    },
    {
        "name": "activated_at",
        "type": "TIMESTAMP",
        "mode": "NULLABLE"
    },
    {
        "name": "deactivated_at",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "status",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "brand_id",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "brand_name",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "customer_id",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "sponsor_name",
        "type": "STRING",
        "mode": "NULLABLE"
    }
]
```

### `ina_playground.persons`

```json
[
    {
        "name": "person_id",
        "type": "STRING",
        "mode": "REQUIRED",
        "description": "Unique deterministic identifier for this person across all memberships"
    },
    {
        "name": "identifier",
        "type": "RECORD",
        "mode": "REQUIRED",
        "fields": [
            {
                "name": "harmony_fis_identifier",
                "type": "STRING",
                "mode": "REPEATED",
                "description": "List of Harmony FIS identifiers"
            },
            {
                "name": "auth0_user_ids",
                "type": "STRING",
                "mode": "REPEATED",
                "description": "List of Auth0 user IDs"
            },
            {
                "name": "memberships",
                "type": "RECORD",
                "mode": "REPEATED",
                "fields": [
                    {
                        "name": "member_id",
                        "type": "STRING",
                        "mode": "REQUIRED",
                        "description": "Unique identifier for the member in Harmony"
                    },
                    {
                        "name": "sponsor_id",
                        "type": "STRING",
                        "mode": "REQUIRED",
                        "description": "Unique identifier for the sponsor organization"
                    },
                    {
                        "name": "sponsor_identifier",
                        "type": "STRING",
                        "mode": "REQUIRED",
                        "description": "Human-readable identifier for the sponsor"
                    },
                    {
                        "name": "contract_id",
                        "type": "STRING",
                        "mode": "NULLABLE",
                        "description": "Contract identifier from member plan data"
                    },
                    {
                        "name": "plan_id",
                        "type": "STRING",
                        "mode": "NULLABLE",
                        "description": "Plan identifier from member plan data"
                    },
                    {
                        "name": "segment_id",
                        "type": "STRING",
                        "mode": "NULLABLE",
                        "description": "Segment identifier from member plan data"
                    },
                    {
                        "name": "sponsor_program_identifier",
                        "type": "STRING",
                        "mode": "NULLABLE",
                        "description": "Program identifier from program_enrollment.program.sponsor_identifier (e.g., H6743-025)"
                    }
                ],
                "description": "List of membership records"
            },
            {
                "name": "salesforce_contact_ids",
                "type": "STRING",
                "mode": "REPEATED",
                "description": "List of Salesforce contact IDs"
            },
            {
                "name": "voice_call_contact_ids",
                "type": "STRING",
                "mode": "REPEATED",
                "description": "List of voice call contact IDs"
            },
            {
                "name": "harmony_ids",
                "type": "STRING",
                "mode": "REPEATED",
                "description": "List of Harmony IDs"
            },
            {
                "name": "phone_numbers",
                "type": "STRING",
                "mode": "REPEATED",
                "description": "List of phone numbers"
            }
        ],
        "description": "All identifiers associated with this person"
    },
    {
        "name": "demographic",
        "type": "RECORD",
        "mode": "REQUIRED",
        "fields": [
            {
                "name": "year_of_birth",
                "type": "INTEGER",
                "mode": "NULLABLE",
                "description": "Year the person was born"
            },
            {
                "name": "language_tag",
                "type": "STRING",
                "mode": "NULLABLE",
                "description": "Preferred language tag (e.g., 'en-US', 'es-MX')"
            },
            {
                "name": "us_state",
                "type": "STRING",
                "mode": "NULLABLE",
                "description": "US state where the person resides"
            }
        ],
        "description": "Demographic information for this person"
    }
]
```

### `ina_playground.reason_code_mapping`

```json
[
    {
        "name": "reason_code",
        "type": "STRING"
    },
    {
        "name": "outcome_category",
        "type": "STRING"
    },
    {
        "name": "description",
        "type": "STRING"
    }
]
```

### `ina_playground.supplemental_invoicing_aggregated`

```json
[
    {
        "name": "contract_id",
        "type": "STRING"
    },
    {
        "name": "plan_id",
        "type": "STRING"
    },
    {
        "name": "segment_id",
        "type": "STRING"
    },
    {
        "name": "year",
        "type": "INTEGER"
    },
    {
        "name": "month",
        "type": "INTEGER"
    },
    {
        "name": "customer_id",
        "type": "STRING"
    },
    {
        "name": "brand_id",
        "type": "STRING"
    },
    {
        "name": "brand_name",
        "type": "STRING"
    },
    {
        "name": "sponsor_id",
        "type": "STRING"
    },
    {
        "name": "sponsor_name",
        "type": "STRING"
    },
    {
        "name": "member_count",
        "type": "INTEGER"
    }
]
```

### `ina_playground.supplemental_invoicing_members`

```json
[
    {
        "name": "member_id",
        "type": "STRING"
    },
    {
        "name": "sponsor_id",
        "type": "STRING"
    },
    {
        "name": "sponsor_identifier",
        "type": "STRING"
    },
    {
        "name": "sponsor_name",
        "type": "STRING"
    },
    {
        "name": "customer_id",
        "type": "STRING"
    },
    {
        "name": "brand_id",
        "type": "STRING"
    },
    {
        "name": "brand_name",
        "type": "STRING"
    },
    {
        "name": "contract_id",
        "type": "STRING"
    },
    {
        "name": "plan_id",
        "type": "STRING"
    },
    {
        "name": "segment_id",
        "type": "STRING"
    },
    {
        "name": "recorded_at",
        "type": "DATE"
    },
    {
        "name": "year",
        "type": "INTEGER"
    },
    {
        "name": "month",
        "type": "INTEGER"
    }
]
```

### `ina_playground.swipe_reason_daily`

```json
[
    {
        "name": "date",
        "type": "DATE"
    },
    {
        "name": "reason",
        "type": "STRING"
    },
    {
        "name": "swipe_count",
        "type": "INTEGER"
    },
    {
        "name": "sponsor_id",
        "type": "STRING"
    },
    {
        "name": "sponsor_name",
        "type": "STRING"
    },
    {
        "name": "customer_id",
        "type": "STRING"
    },
    {
        "name": "brand_id",
        "type": "STRING"
    },
    {
        "name": "brand_name",
        "type": "STRING"
    }
]
```

### `ina_playground.swipe_summary`

```json
[
    {
        "name": "transaction_id",
        "type": "STRING"
    },
    {
        "name": "member_id",
        "type": "STRING"
    },
    {
        "name": "sponsor_id",
        "type": "STRING"
    },
    {
        "name": "sponsor_identifier",
        "type": "STRING"
    },
    {
        "name": "merchant_id",
        "type": "STRING"
    },
    {
        "name": "merchant_name",
        "type": "STRING"
    },
    {
        "name": "merchant_name_rollup",
        "type": "STRING"
    },
    {
        "name": "reason",
        "type": "STRING"
    },
    {
        "name": "approved",
        "type": "BOOLEAN"
    },
    {
        "name": "swipe_outcome",
        "type": "STRING"
    },
    {
        "name": "spending",
        "type": "BOOLEAN"
    },
    {
        "name": "state",
        "type": "STRING"
    },
    {
        "name": "amount_requested",
        "type": "FLOAT"
    },
    {
        "name": "amount_approved",
        "type": "FLOAT"
    },
    {
        "name": "occurred_at",
        "type": "TIMESTAMP"
    },
    {
        "name": "settled_at",
        "type": "TIMESTAMP"
    },
    {
        "name": "reversed_at",
        "type": "TIMESTAMP"
    },
    {
        "name": "sources",
        "type": "STRING",
        "mode": "REPEATED"
    },
    {
        "name": "brand_id",
        "type": "STRING"
    },
    {
        "name": "brand_name",
        "type": "STRING"
    },
    {
        "name": "customer_id",
        "type": "STRING"
    },
    {
        "name": "sponsor_name",
        "type": "STRING"
    }
]
```

### `ina_playground.trip_summary`

```json
[
    {
        "name": "trip_id",
        "type": "STRING"
    },
    {
        "name": "member_id",
        "type": "STRING"
    },
    {
        "name": "sponsor_id",
        "type": "STRING"
    },
    {
        "name": "sponsor_identifier",
        "type": "STRING"
    },
    {
        "name": "merchant_id",
        "type": "STRING"
    },
    {
        "name": "merchant_name",
        "type": "STRING"
    },
    {
        "name": "merchant_name_rollup",
        "type": "STRING"
    },
    {
        "name": "trip_hour",
        "type": "TIMESTAMP"
    },
    {
        "name": "swipe_count",
        "type": "INTEGER"
    },
    {
        "name": "trip_outcome",
        "type": "STRING"
    },
    {
        "name": "trip_reason",
        "type": "STRING"
    },
    {
        "name": "total_requested",
        "type": "FLOAT"
    },
    {
        "name": "total_approved",
        "type": "FLOAT"
    },
    {
        "name": "first_swipe_at",
        "type": "TIMESTAMP"
    },
    {
        "name": "last_swipe_at",
        "type": "TIMESTAMP"
    },
    {
        "name": "brand_id",
        "type": "STRING"
    },
    {
        "name": "brand_name",
        "type": "STRING"
    },
    {
        "name": "customer_id",
        "type": "STRING"
    },
    {
        "name": "sponsor_name",
        "type": "STRING"
    }
]
```

## Dataset: `ina_star`

### `ina_star.bridge_product_category`

```json
[
    {
        "name": "upc",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "category_id",
        "type": "STRING",
        "mode": "NULLABLE"
    }
]
```

### `ina_star.dim_category`

```json
[
    {
        "name": "category_id",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "category_name",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "category_description",
        "type": "STRING",
        "mode": "NULLABLE"
    }
]
```

### `ina_star.dim_date`

```json
[
    {
        "name": "date_key",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "full_date",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "year",
        "type": "INTEGER",
        "mode": "NULLABLE"
    },
    {
        "name": "quarter",
        "type": "INTEGER",
        "mode": "NULLABLE"
    },
    {
        "name": "month",
        "type": "INTEGER",
        "mode": "NULLABLE"
    },
    {
        "name": "month_name",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "week_of_year",
        "type": "INTEGER",
        "mode": "NULLABLE"
    },
    {
        "name": "day_of_month",
        "type": "INTEGER",
        "mode": "NULLABLE"
    },
    {
        "name": "day_of_week",
        "type": "INTEGER",
        "mode": "NULLABLE"
    },
    {
        "name": "day_name",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "is_weekend",
        "type": "BOOLEAN",
        "mode": "NULLABLE"
    },
    {
        "name": "fiscal_year",
        "type": "INTEGER",
        "mode": "NULLABLE"
    },
    {
        "name": "fiscal_quarter",
        "type": "INTEGER",
        "mode": "NULLABLE"
    }
]
```

### `ina_star.dim_location`

```json
[
    {
        "name": "location_key",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "merchant_id",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "store_id",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "address_street1",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "address_street2",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "city",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "state",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "zip_code",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "latitude",
        "type": "FLOAT",
        "mode": "NULLABLE"
    },
    {
        "name": "longitude",
        "type": "FLOAT",
        "mode": "NULLABLE"
    },
    {
        "name": "has_pharmacy",
        "type": "INTEGER",
        "mode": "NULLABLE"
    },
    {
        "name": "phone",
        "type": "STRING",
        "mode": "NULLABLE"
    }
]
```

### `ina_star.dim_member`

```json
[
    {
        "name": "member_id",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "sponsor_id",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "person_id",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "year_of_birth",
        "type": "INTEGER",
        "mode": "NULLABLE"
    },
    {
        "name": "language_tag",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "us_state",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "is_active",
        "type": "INTEGER",
        "mode": "NULLABLE"
    }
]
```

### `ina_star.dim_merchant`

```json
[
    {
        "name": "merchant_id",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "merchant_name",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "normalized_name",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "integration_type",
        "type": "STRING",
        "mode": "NULLABLE"
    }
]
```

### `ina_star.dim_product`

```json
[
    {
        "name": "upc",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "brand_name",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "product_name",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "category",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "sub_category",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "is_eligible",
        "type": "INTEGER",
        "mode": "NULLABLE"
    }
]
```

### `ina_star.dim_sponsor`

```json
[
    {
        "name": "sponsor_id",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "sponsor_name",
        "type": "STRING",
        "mode": "NULLABLE"
    }
]
```

### `ina_star.fact_basket_item`

```json
[
    {
        "name": "card_usage_id",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "item_sequence",
        "type": "INTEGER",
        "mode": "NULLABLE"
    },
    {
        "name": "upc",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "member_id",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "merchant_id",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "location_key",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "purchase_date_key",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "quantity",
        "type": "INTEGER",
        "mode": "NULLABLE"
    },
    {
        "name": "unit_price",
        "type": "FLOAT",
        "mode": "NULLABLE"
    }
]
```

### `ina_star.fact_card_purchase`

```json
[
    {
        "name": "card_usage_id",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "member_id",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "sponsor_id",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "merchant_id",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "location_key",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "purchase_date_key",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "amount_requested",
        "type": "FLOAT",
        "mode": "NULLABLE"
    },
    {
        "name": "amount_approved",
        "type": "FLOAT",
        "mode": "NULLABLE"
    },
    {
        "name": "total_items",
        "type": "INTEGER",
        "mode": "NULLABLE"
    },
    {
        "name": "eligible_items",
        "type": "INTEGER",
        "mode": "NULLABLE"
    },
    {
        "name": "unique_upcs",
        "type": "INTEGER",
        "mode": "NULLABLE"
    },
    {
        "name": "integration_type",
        "type": "STRING",
        "mode": "NULLABLE"
    }
]
```

## Dataset: `internal_reporting_metabase`

### `internal_reporting_metabase.partner_raw`

```json
[
    {
        "name": "id",
        "type": "STRING",
        "mode": "REQUIRED",
        "description": "Partner XID"
    },
    {
        "name": "name",
        "type": "STRING",
        "mode": "REQUIRED",
        "description": "Partner name"
    },
    {
        "name": "bucket_name",
        "type": "STRING",
        "mode": "REQUIRED",
        "description": "GCS bucket name"
    },
    {
        "name": "partner_type",
        "type": "STRING",
        "mode": "REQUIRED",
        "description": "Type: sponsor, merchant, or processor"
    },
    {
        "name": "short_code",
        "type": "STRING",
        "mode": "REQUIRED",
        "description": "Partner short code, aka shortcode"
    },
    {
        "name": "config",
        "type": "STRING",
        "mode": "REQUIRED",
        "description": "JSON configuration"
    },
    {
        "name": "created_at",
        "type": "TIMESTAMP",
        "mode": "REQUIRED",
        "description": "Creation timestamp"
    }
]
```

### `internal_reporting_metabase.partner_rls_demo`

```json
[
    {
        "name": "partner_id",
        "type": "STRING",
        "mode": "REQUIRED",
        "description": "Partner XID"
    },
    {
        "name": "sample_restricted_data",
        "type": "STRING",
        "mode": "REQUIRED",
        "description": "Some data that we want to be restricted"
    }
]
```

### `internal_reporting_metabase.partners`

```json
[
    {
        "name": "id",
        "type": "STRING",
        "mode": "REQUIRED",
        "description": "Partner XID"
    },
    {
        "name": "name",
        "type": "STRING",
        "mode": "REQUIRED",
        "description": "Partner name"
    },
    {
        "name": "bucket_name",
        "type": "STRING",
        "mode": "REQUIRED",
        "description": "GCS bucket name"
    },
    {
        "name": "partner_type",
        "type": "STRING",
        "mode": "REQUIRED",
        "description": "Type: sponsor, merchant, or processor"
    },
    {
        "name": "short_code",
        "type": "STRING",
        "mode": "REQUIRED",
        "description": "Partner short code, aka shortcode"
    },
    {
        "name": "created_at",
        "type": "TIMESTAMP",
        "mode": "REQUIRED",
        "description": "Creation timestamp"
    },
    {
        "name": "partner_emoji",
        "type": "STRING",
        "mode": "NULLABLE",
        "description": "Partner emoji from config.partner_emoji"
    },
    {
        "name": "slack_channel_url",
        "type": "STRING",
        "mode": "NULLABLE",
        "description": "Slack channel URL from config.slack_channel_url"
    },
    {
        "name": "file_encryption_key_encrypted",
        "type": "STRING",
        "mode": "NULLABLE",
        "description": "File encryption key encrypted from config.file_encryption_key_encrypted"
    },
    {
        "name": "file_encryption_key_passphrase_encrypted",
        "type": "STRING",
        "mode": "NULLABLE",
        "description": "File encryption key passphrase encrypted from config.file_encryption_key_passphrase_encrypted"
    },
    {
        "name": "file_encryption_method",
        "type": "STRING",
        "mode": "NULLABLE",
        "description": "File encryption method from config.file_encryption_method"
    },
    {
        "name": "sso_config",
        "type": "STRING",
        "mode": "NULLABLE",
        "description": "SSO configuration from config.sso_config"
    },
    {
        "name": "sso_config_callback_url",
        "type": "STRING",
        "mode": "NULLABLE",
        "description": "SSO callback URL from config.sso_config.callback_url"
    },
    {
        "name": "sso_config_entry_point",
        "type": "STRING",
        "mode": "NULLABLE",
        "description": "SSO entry point from config.sso_config.entry_point"
    }
]
```

### `internal_reporting_metabase.user_partner_access`

```json
[
    {
        "name": "user_email",
        "type": "STRING"
    },
    {
        "name": "partner_id",
        "type": "STRING"
    },
    {
        "name": "synced_at",
        "type": "TIMESTAMP"
    }
]
```

## Dataset: `inventory_analysis`

### `inventory_analysis.2026-03-abcorp-wo-cards`

```json
[
    {
        "name": "InputFile",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "WorkOrderID",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "Program",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "ProcessingDate",
        "type": "DATE",
        "mode": "NULLABLE"
    },
    {
        "name": "Status",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "ShipDate",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "Cardholder",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "ProxyNumber",
        "type": "INTEGER",
        "mode": "NULLABLE"
    },
    {
        "name": "PANEnd",
        "type": "INTEGER",
        "mode": "NULLABLE"
    }
]
```

### `inventory_analysis.ABCorp_invoices`

```json
[
    {
        "name": "file_name",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "invoice_number",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "invoice_date",
        "type": "DATE",
        "mode": "NULLABLE"
    },
    {
        "name": "customer_name",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "customer_account",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "invoice_amount",
        "type": "FLOAT",
        "mode": "NULLABLE"
    },
    {
        "name": "due_date",
        "type": "DATE",
        "mode": "NULLABLE"
    },
    {
        "name": "invoice_period",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "page_number",
        "type": "INTEGER",
        "mode": "NULLABLE"
    },
    {
        "name": "line_number",
        "type": "INTEGER",
        "mode": "NULLABLE"
    },
    {
        "name": "line_type",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "part_number",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "description",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "quantity",
        "type": "INTEGER",
        "mode": "NULLABLE"
    },
    {
        "name": "unit_price",
        "type": "FLOAT",
        "mode": "NULLABLE"
    },
    {
        "name": "unit_of_measure",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "amount",
        "type": "FLOAT",
        "mode": "NULLABLE"
    },
    {
        "name": "subtotal",
        "type": "FLOAT",
        "mode": "NULLABLE"
    },
    {
        "name": "total",
        "type": "FLOAT",
        "mode": "NULLABLE"
    }
]
```

### `inventory_analysis.ABCorp_invoices_products_only`

```json
[
    {
        "name": "file_name",
        "type": "STRING"
    },
    {
        "name": "invoice_number",
        "type": "STRING"
    },
    {
        "name": "invoice_date",
        "type": "DATE"
    },
    {
        "name": "customer_name",
        "type": "STRING"
    },
    {
        "name": "customer_account",
        "type": "STRING"
    },
    {
        "name": "invoice_amount",
        "type": "FLOAT"
    },
    {
        "name": "due_date",
        "type": "DATE"
    },
    {
        "name": "invoice_period",
        "type": "STRING"
    },
    {
        "name": "page_number",
        "type": "INTEGER"
    },
    {
        "name": "line_number",
        "type": "INTEGER"
    },
    {
        "name": "line_type",
        "type": "STRING"
    },
    {
        "name": "part_number",
        "type": "STRING"
    },
    {
        "name": "description",
        "type": "STRING"
    },
    {
        "name": "quantity",
        "type": "INTEGER"
    },
    {
        "name": "unit_price",
        "type": "FLOAT"
    },
    {
        "name": "unit_of_measure",
        "type": "STRING"
    },
    {
        "name": "amount",
        "type": "FLOAT"
    },
    {
        "name": "subtotal",
        "type": "FLOAT"
    },
    {
        "name": "total",
        "type": "FLOAT"
    }
]
```

### `inventory_analysis.brand_kit_monthly_invoiced`

```json
[
    {
        "name": "month",
        "type": "STRING"
    },
    {
        "name": "sponsor_name",
        "type": "STRING"
    },
    {
        "name": "brand_shortcode",
        "type": "STRING"
    },
    {
        "name": "kit_id",
        "type": "STRING"
    },
    {
        "name": "program_name",
        "type": "STRING"
    },
    {
        "name": "language_code",
        "type": "STRING"
    },
    {
        "name": "fis_package_id",
        "type": "STRING"
    },
    {
        "name": "abc_fg_number",
        "type": "STRING"
    },
    {
        "name": "kits_invoiced",
        "type": "INTEGER"
    },
    {
        "name": "cards",
        "type": "INTEGER"
    },
    {
        "name": "catalogs",
        "type": "INTEGER"
    },
    {
        "name": "amount_billed",
        "type": "FLOAT"
    }
]
```

### `inventory_analysis.brand_kit_monthly_summary`

```json
[
    {
        "name": "month",
        "type": "STRING"
    },
    {
        "name": "sponsor_name",
        "type": "STRING"
    },
    {
        "name": "brand_shortcode",
        "type": "STRING"
    },
    {
        "name": "kit_id",
        "type": "STRING"
    },
    {
        "name": "program_name",
        "type": "STRING"
    },
    {
        "name": "language_code",
        "type": "STRING"
    },
    {
        "name": "fis_package_id",
        "type": "STRING"
    },
    {
        "name": "abc_fg_number",
        "type": "STRING"
    },
    {
        "name": "kits_created",
        "type": "INTEGER"
    },
    {
        "name": "cards",
        "type": "INTEGER"
    },
    {
        "name": "catalogs",
        "type": "INTEGER"
    }
]
```

### `inventory_analysis.eo_2025_ABCorp_work_orders`

```json
[
    {
        "name": "InputFile",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "WorkOrderID",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "Program",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "ProcessingDate",
        "type": "DATE",
        "mode": "NULLABLE"
    },
    {
        "name": "Status",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "ShipDate",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "ProxyNumber",
        "type": "INTEGER",
        "mode": "NULLABLE"
    }
]
```

### `inventory_analysis.exploded_material_inventory`

```json
[
    {
        "name": "material_id",
        "type": "STRING"
    },
    {
        "name": "sh_part_number",
        "type": "STRING"
    },
    {
        "name": "material_type_code",
        "type": "STRING"
    },
    {
        "name": "material_type_name",
        "type": "STRING"
    },
    {
        "name": "variant",
        "type": "STRING"
    },
    {
        "name": "brand_shortcode",
        "type": "STRING"
    },
    {
        "name": "language_code",
        "type": "STRING"
    },
    {
        "name": "year_introduced",
        "type": "STRING"
    },
    {
        "name": "material_description",
        "type": "STRING"
    },
    {
        "name": "inventory_part_id",
        "type": "STRING"
    },
    {
        "name": "component_role",
        "type": "STRING"
    },
    {
        "name": "component_description",
        "type": "STRING"
    },
    {
        "name": "is_composite_material",
        "type": "BOOLEAN"
    }
]
```

### `inventory_analysis.fis_vs_invoice_monthly_summary`

```json
[
    {
        "name": "month",
        "type": "STRING"
    },
    {
        "name": "kits_matched",
        "type": "INTEGER"
    },
    {
        "name": "kits_mismatched",
        "type": "INTEGER"
    },
    {
        "name": "kits_fis_only",
        "type": "INTEGER"
    },
    {
        "name": "kits_invoiced_only",
        "type": "INTEGER"
    },
    {
        "name": "total_fis_kits",
        "type": "INTEGER"
    },
    {
        "name": "total_invoiced_kits",
        "type": "INTEGER"
    },
    {
        "name": "kit_delta",
        "type": "INTEGER"
    },
    {
        "name": "total_fis_cards",
        "type": "INTEGER"
    },
    {
        "name": "total_invoiced_cards",
        "type": "INTEGER"
    },
    {
        "name": "card_delta",
        "type": "INTEGER"
    },
    {
        "name": "total_fis_catalogs",
        "type": "INTEGER"
    },
    {
        "name": "total_invoiced_catalogs",
        "type": "INTEGER"
    },
    {
        "name": "catalog_delta",
        "type": "INTEGER"
    },
    {
        "name": "total_amount_billed",
        "type": "FLOAT"
    }
]
```

### `inventory_analysis.fis_vs_invoice_reconciliation`

```json
[
    {
        "name": "month",
        "type": "STRING"
    },
    {
        "name": "sponsor_name",
        "type": "STRING"
    },
    {
        "name": "brand_shortcode",
        "type": "STRING"
    },
    {
        "name": "kit_id",
        "type": "STRING"
    },
    {
        "name": "program_name",
        "type": "STRING"
    },
    {
        "name": "language_code",
        "type": "STRING"
    },
    {
        "name": "abc_fg_number",
        "type": "STRING"
    },
    {
        "name": "fis_package_id",
        "type": "STRING"
    },
    {
        "name": "fis_kits",
        "type": "INTEGER"
    },
    {
        "name": "invoiced_kits",
        "type": "INTEGER"
    },
    {
        "name": "kit_delta",
        "type": "INTEGER"
    },
    {
        "name": "fis_cards",
        "type": "INTEGER"
    },
    {
        "name": "invoiced_cards",
        "type": "INTEGER"
    },
    {
        "name": "card_delta",
        "type": "INTEGER"
    },
    {
        "name": "fis_catalogs",
        "type": "INTEGER"
    },
    {
        "name": "invoiced_catalogs",
        "type": "INTEGER"
    },
    {
        "name": "catalog_delta",
        "type": "INTEGER"
    },
    {
        "name": "amount_billed",
        "type": "FLOAT"
    },
    {
        "name": "reconciliation_status",
        "type": "STRING"
    }
]
```

### `inventory_analysis.fis_vs_invoice_timeseries`

```json
[
    {
        "name": "month",
        "type": "STRING"
    },
    {
        "name": "month_date",
        "type": "DATE"
    },
    {
        "name": "fis_kits",
        "type": "INTEGER"
    },
    {
        "name": "invoiced_kits",
        "type": "INTEGER"
    },
    {
        "name": "kit_delta",
        "type": "INTEGER"
    },
    {
        "name": "fis_kits_cumulative",
        "type": "INTEGER"
    },
    {
        "name": "invoiced_kits_cumulative",
        "type": "INTEGER"
    },
    {
        "name": "fis_cards",
        "type": "INTEGER"
    },
    {
        "name": "invoiced_cards",
        "type": "INTEGER"
    },
    {
        "name": "fis_catalogs",
        "type": "INTEGER"
    },
    {
        "name": "invoiced_catalogs",
        "type": "INTEGER"
    },
    {
        "name": "amount_billed",
        "type": "FLOAT"
    }
]
```

### `inventory_analysis.invoiced_kit_summary`

```json
[
    {
        "name": "invoice_month",
        "type": "STRING"
    },
    {
        "name": "invoice_number",
        "type": "STRING"
    },
    {
        "name": "invoice_period",
        "type": "STRING"
    },
    {
        "name": "fg_number",
        "type": "STRING"
    },
    {
        "name": "kit_id",
        "type": "STRING"
    },
    {
        "name": "brand_shortcode",
        "type": "STRING"
    },
    {
        "name": "language_code",
        "type": "STRING"
    },
    {
        "name": "sponsor_name",
        "type": "STRING"
    },
    {
        "name": "program_name",
        "type": "STRING"
    },
    {
        "name": "kit_year",
        "type": "STRING"
    },
    {
        "name": "is_replacement",
        "type": "BOOLEAN"
    },
    {
        "name": "is_catalog_only",
        "type": "BOOLEAN"
    },
    {
        "name": "kits_invoiced",
        "type": "INTEGER"
    },
    {
        "name": "cards_invoiced",
        "type": "INTEGER"
    },
    {
        "name": "catalogs_invoiced",
        "type": "INTEGER"
    },
    {
        "name": "total_materials_in_kit",
        "type": "INTEGER"
    },
    {
        "name": "unit_price",
        "type": "FLOAT"
    },
    {
        "name": "line_amount",
        "type": "FLOAT"
    },
    {
        "name": "invoice_line_description",
        "type": "STRING"
    }
]
```

### `inventory_analysis.kit_component_monthly_drawdown`

```json
[
    {
        "name": "program_name",
        "type": "STRING"
    },
    {
        "name": "brand_shortcode",
        "type": "STRING"
    },
    {
        "name": "kit_year",
        "type": "STRING"
    },
    {
        "name": "is_replacement",
        "type": "BOOLEAN"
    },
    {
        "name": "is_catalog_only",
        "type": "BOOLEAN"
    },
    {
        "name": "fis_package_id",
        "type": "STRING"
    },
    {
        "name": "abc_fg_id",
        "type": "STRING"
    },
    {
        "name": "material_sh_part",
        "type": "STRING"
    },
    {
        "name": "material_type_code",
        "type": "STRING"
    },
    {
        "name": "component_part_id",
        "type": "STRING"
    },
    {
        "name": "component_role",
        "type": "STRING"
    },
    {
        "name": "component_description",
        "type": "STRING"
    },
    {
        "name": "is_sub_component",
        "type": "BOOLEAN"
    },
    {
        "name": "sep_2024",
        "type": "INTEGER"
    },
    {
        "name": "oct_2024",
        "type": "INTEGER"
    },
    {
        "name": "nov_2024",
        "type": "INTEGER"
    },
    {
        "name": "dec_2024",
        "type": "INTEGER"
    },
    {
        "name": "jan_2025",
        "type": "INTEGER"
    },
    {
        "name": "feb_2025",
        "type": "INTEGER"
    },
    {
        "name": "mar_2025",
        "type": "INTEGER"
    },
    {
        "name": "apr_2025",
        "type": "INTEGER"
    },
    {
        "name": "may_2025",
        "type": "INTEGER"
    },
    {
        "name": "jun_2025",
        "type": "INTEGER"
    },
    {
        "name": "jul_2025",
        "type": "INTEGER"
    },
    {
        "name": "aug_2025",
        "type": "INTEGER"
    },
    {
        "name": "sep_2025",
        "type": "INTEGER"
    },
    {
        "name": "oct_2025",
        "type": "INTEGER"
    },
    {
        "name": "nov_2025",
        "type": "INTEGER"
    },
    {
        "name": "dec_2025",
        "type": "INTEGER"
    },
    {
        "name": "jan_2026",
        "type": "INTEGER"
    },
    {
        "name": "feb_2026",
        "type": "INTEGER"
    },
    {
        "name": "total_consumed",
        "type": "INTEGER"
    }
]
```

### `inventory_analysis.kit_drawdown_universal`

```json
[
    {
        "name": "kit_id",
        "type": "STRING"
    },
    {
        "name": "kit_year",
        "type": "STRING"
    },
    {
        "name": "brand_shortcode",
        "type": "STRING"
    },
    {
        "name": "language_code",
        "type": "STRING"
    },
    {
        "name": "sponsor_name",
        "type": "STRING"
    },
    {
        "name": "program_name",
        "type": "STRING"
    },
    {
        "name": "is_replacement",
        "type": "BOOLEAN"
    },
    {
        "name": "is_catalog_only",
        "type": "BOOLEAN"
    },
    {
        "name": "primary_vendor",
        "type": "STRING"
    },
    {
        "name": "fis_package_id",
        "type": "STRING"
    },
    {
        "name": "abc_fg_id",
        "type": "STRING"
    },
    {
        "name": "card_sh_part",
        "type": "STRING"
    },
    {
        "name": "card_vendor_parts",
        "type": "STRING"
    },
    {
        "name": "carrier_sh_part",
        "type": "STRING"
    },
    {
        "name": "carrier_vendor_parts",
        "type": "STRING"
    },
    {
        "name": "catalog_sh_part",
        "type": "STRING"
    },
    {
        "name": "catalog_vendor_parts",
        "type": "STRING"
    },
    {
        "name": "catalog_components",
        "type": "STRING"
    },
    {
        "name": "envelope_sh_part",
        "type": "STRING"
    },
    {
        "name": "envelope_size",
        "type": "STRING"
    },
    {
        "name": "envelope_vendor_parts",
        "type": "STRING"
    },
    {
        "name": "activation_label_sh_part",
        "type": "STRING"
    },
    {
        "name": "activation_label_vendor_parts",
        "type": "STRING"
    },
    {
        "name": "insert_cha_sh_part",
        "type": "STRING"
    },
    {
        "name": "insert_cha_vendor_parts",
        "type": "STRING"
    },
    {
        "name": "insert_mli_sh_part",
        "type": "STRING"
    },
    {
        "name": "insert_mli_vendor_parts",
        "type": "STRING"
    },
    {
        "name": "insert_ndn_sh_part",
        "type": "STRING"
    },
    {
        "name": "insert_ndn_vendor_parts",
        "type": "STRING"
    },
    {
        "name": "insert_welcome_letter_sh_part",
        "type": "STRING"
    },
    {
        "name": "total_materials_in_kit",
        "type": "INTEGER"
    },
    {
        "name": "sep_2024",
        "type": "INTEGER"
    },
    {
        "name": "oct_2024",
        "type": "INTEGER"
    },
    {
        "name": "nov_2024",
        "type": "INTEGER"
    },
    {
        "name": "dec_2024",
        "type": "INTEGER"
    },
    {
        "name": "jan_2025",
        "type": "INTEGER"
    },
    {
        "name": "feb_2025",
        "type": "INTEGER"
    },
    {
        "name": "mar_2025",
        "type": "INTEGER"
    },
    {
        "name": "apr_2025",
        "type": "INTEGER"
    },
    {
        "name": "may_2025",
        "type": "INTEGER"
    },
    {
        "name": "jun_2025",
        "type": "INTEGER"
    },
    {
        "name": "jul_2025",
        "type": "INTEGER"
    },
    {
        "name": "aug_2025",
        "type": "INTEGER"
    },
    {
        "name": "sep_2025",
        "type": "INTEGER"
    },
    {
        "name": "oct_2025",
        "type": "INTEGER"
    },
    {
        "name": "nov_2025",
        "type": "INTEGER"
    },
    {
        "name": "dec_2025",
        "type": "INTEGER"
    },
    {
        "name": "jan_2026",
        "type": "INTEGER"
    },
    {
        "name": "feb_2026",
        "type": "INTEGER"
    },
    {
        "name": "total_fulfilled",
        "type": "INTEGER"
    }
]
```

### `inventory_analysis.kit_material_monthly_drawdown`

```json
[
    {
        "name": "program_name",
        "type": "STRING"
    },
    {
        "name": "brand_shortcode",
        "type": "STRING"
    },
    {
        "name": "kit_year",
        "type": "STRING"
    },
    {
        "name": "is_replacement",
        "type": "BOOLEAN"
    },
    {
        "name": "is_catalog_only",
        "type": "BOOLEAN"
    },
    {
        "name": "fis_package_id",
        "type": "STRING"
    },
    {
        "name": "abc_fg_id",
        "type": "STRING"
    },
    {
        "name": "sh_part_number",
        "type": "STRING"
    },
    {
        "name": "material_type_code",
        "type": "STRING"
    },
    {
        "name": "sep_2024",
        "type": "INTEGER"
    },
    {
        "name": "oct_2024",
        "type": "INTEGER"
    },
    {
        "name": "nov_2024",
        "type": "INTEGER"
    },
    {
        "name": "dec_2024",
        "type": "INTEGER"
    },
    {
        "name": "jan_2025",
        "type": "INTEGER"
    },
    {
        "name": "feb_2025",
        "type": "INTEGER"
    },
    {
        "name": "mar_2025",
        "type": "INTEGER"
    },
    {
        "name": "apr_2025",
        "type": "INTEGER"
    },
    {
        "name": "may_2025",
        "type": "INTEGER"
    },
    {
        "name": "jun_2025",
        "type": "INTEGER"
    },
    {
        "name": "jul_2025",
        "type": "INTEGER"
    },
    {
        "name": "aug_2025",
        "type": "INTEGER"
    },
    {
        "name": "sep_2025",
        "type": "INTEGER"
    },
    {
        "name": "oct_2025",
        "type": "INTEGER"
    },
    {
        "name": "nov_2025",
        "type": "INTEGER"
    },
    {
        "name": "dec_2025",
        "type": "INTEGER"
    },
    {
        "name": "jan_2026",
        "type": "INTEGER"
    },
    {
        "name": "feb_2026",
        "type": "INTEGER"
    },
    {
        "name": "total_consumed",
        "type": "INTEGER"
    }
]
```

### `inventory_analysis.kit_matrix_exploded`

```json
[
    {
        "name": "kit_id",
        "type": "STRING"
    },
    {
        "name": "kit_year",
        "type": "STRING"
    },
    {
        "name": "brand_shortcode",
        "type": "STRING"
    },
    {
        "name": "language_code",
        "type": "STRING"
    },
    {
        "name": "sponsor_name",
        "type": "STRING"
    },
    {
        "name": "program_name",
        "type": "STRING"
    },
    {
        "name": "is_replacement",
        "type": "BOOLEAN"
    },
    {
        "name": "is_catalog_only",
        "type": "BOOLEAN"
    },
    {
        "name": "primary_vendor",
        "type": "STRING"
    },
    {
        "name": "fis_package_id",
        "type": "STRING"
    },
    {
        "name": "abc_fg_id",
        "type": "STRING"
    },
    {
        "name": "arroweye_id",
        "type": "STRING"
    },
    {
        "name": "legacy_2024_id",
        "type": "STRING"
    },
    {
        "name": "catalog_kit_id",
        "type": "STRING"
    },
    {
        "name": "material_id",
        "type": "STRING"
    },
    {
        "name": "material_type_code",
        "type": "STRING"
    },
    {
        "name": "material_type_name",
        "type": "STRING"
    },
    {
        "name": "sh_part_number",
        "type": "STRING"
    },
    {
        "name": "variant",
        "type": "STRING"
    },
    {
        "name": "material_description",
        "type": "STRING"
    },
    {
        "name": "vendor_part_numbers",
        "type": "STRING"
    },
    {
        "name": "inventory_part_id",
        "type": "STRING"
    },
    {
        "name": "component_role",
        "type": "STRING"
    },
    {
        "name": "component_description",
        "type": "STRING"
    },
    {
        "name": "is_composite_material",
        "type": "BOOLEAN"
    }
]
```

### `inventory_analysis.kit_matrix_universal`

```json
[
    {
        "name": "kit_id",
        "type": "STRING"
    },
    {
        "name": "kit_year",
        "type": "STRING"
    },
    {
        "name": "brand_shortcode",
        "type": "STRING"
    },
    {
        "name": "language_code",
        "type": "STRING"
    },
    {
        "name": "sponsor_name",
        "type": "STRING"
    },
    {
        "name": "program_name",
        "type": "STRING"
    },
    {
        "name": "is_replacement",
        "type": "BOOLEAN"
    },
    {
        "name": "is_catalog_only",
        "type": "BOOLEAN"
    },
    {
        "name": "primary_vendor",
        "type": "STRING"
    },
    {
        "name": "fis_package_id",
        "type": "STRING"
    },
    {
        "name": "abc_fg_id",
        "type": "STRING"
    },
    {
        "name": "arroweye_id",
        "type": "STRING"
    },
    {
        "name": "legacy_2024_id",
        "type": "STRING"
    },
    {
        "name": "catalog_kit_id",
        "type": "STRING"
    },
    {
        "name": "card_sh_part",
        "type": "STRING"
    },
    {
        "name": "card_vendor_parts",
        "type": "STRING"
    },
    {
        "name": "carrier_sh_part",
        "type": "STRING"
    },
    {
        "name": "carrier_vendor_parts",
        "type": "STRING"
    },
    {
        "name": "catalog_sh_part",
        "type": "STRING"
    },
    {
        "name": "catalog_vendor_parts",
        "type": "STRING"
    },
    {
        "name": "envelope_sh_part",
        "type": "STRING"
    },
    {
        "name": "envelope_size",
        "type": "STRING"
    },
    {
        "name": "envelope_vendor_parts",
        "type": "STRING"
    },
    {
        "name": "activation_label_sh_part",
        "type": "STRING"
    },
    {
        "name": "activation_label_vendor_parts",
        "type": "STRING"
    },
    {
        "name": "insert_cha_sh_part",
        "type": "STRING"
    },
    {
        "name": "insert_cha_vendor_parts",
        "type": "STRING"
    },
    {
        "name": "insert_mli_sh_part",
        "type": "STRING"
    },
    {
        "name": "insert_mli_vendor_parts",
        "type": "STRING"
    },
    {
        "name": "insert_ndn_sh_part",
        "type": "STRING"
    },
    {
        "name": "insert_ndn_vendor_parts",
        "type": "STRING"
    },
    {
        "name": "insert_welcome_letter_sh_part",
        "type": "STRING"
    },
    {
        "name": "total_materials_in_kit",
        "type": "INTEGER"
    },
    {
        "name": "implementation_status",
        "type": "STRING"
    },
    {
        "name": "live_date",
        "type": "DATE"
    },
    {
        "name": "uat_status",
        "type": "STRING"
    },
    {
        "name": "postage",
        "type": "STRING"
    },
    {
        "name": "notes",
        "type": "STRING"
    },
    {
        "name": "member_scenarios",
        "type": "STRING"
    },
    {
        "name": "pbp",
        "type": "STRING"
    },
    {
        "name": "catalog_upon_enrollment",
        "type": "STRING"
    }
]
```

### `inventory_analysis.kit_monthly_comparison`

```json
[
    {
        "name": "kit_id",
        "type": "STRING"
    },
    {
        "name": "sponsor_name",
        "type": "STRING"
    },
    {
        "name": "brand_shortcode",
        "type": "STRING"
    },
    {
        "name": "language_code",
        "type": "STRING"
    },
    {
        "name": "abc_fg_number",
        "type": "STRING"
    },
    {
        "name": "fis_package_id",
        "type": "STRING"
    },
    {
        "name": "source",
        "type": "STRING"
    },
    {
        "name": "oct_2024",
        "type": "INTEGER"
    },
    {
        "name": "nov_2024",
        "type": "INTEGER"
    },
    {
        "name": "dec_2024",
        "type": "INTEGER"
    },
    {
        "name": "jan_2025",
        "type": "INTEGER"
    },
    {
        "name": "feb_2025",
        "type": "INTEGER"
    },
    {
        "name": "mar_2025",
        "type": "INTEGER"
    },
    {
        "name": "apr_2025",
        "type": "INTEGER"
    },
    {
        "name": "may_2025",
        "type": "INTEGER"
    },
    {
        "name": "jun_2025",
        "type": "INTEGER"
    },
    {
        "name": "jul_2025",
        "type": "INTEGER"
    },
    {
        "name": "aug_2025",
        "type": "INTEGER"
    },
    {
        "name": "sep_2025",
        "type": "INTEGER"
    },
    {
        "name": "oct_2025",
        "type": "INTEGER"
    },
    {
        "name": "nov_2025",
        "type": "INTEGER"
    },
    {
        "name": "dec_2025",
        "type": "INTEGER"
    },
    {
        "name": "jan_2026",
        "type": "INTEGER"
    },
    {
        "name": "feb_2026",
        "type": "INTEGER"
    }
]
```

### `inventory_analysis.monthly_material_consumption`

```json
[
    {
        "name": "event_month",
        "type": "TIMESTAMP"
    },
    {
        "name": "kit_id",
        "type": "STRING"
    },
    {
        "name": "fis_package_id",
        "type": "STRING"
    },
    {
        "name": "abc_fg_id",
        "type": "STRING"
    },
    {
        "name": "material_id",
        "type": "STRING"
    },
    {
        "name": "material_type_code",
        "type": "STRING"
    },
    {
        "name": "material_type_name",
        "type": "STRING"
    },
    {
        "name": "sh_part_number",
        "type": "STRING"
    },
    {
        "name": "variant",
        "type": "STRING"
    },
    {
        "name": "material_description",
        "type": "STRING"
    },
    {
        "name": "brand_shortcode",
        "type": "STRING"
    },
    {
        "name": "language_code",
        "type": "STRING"
    },
    {
        "name": "year_introduced",
        "type": "STRING"
    },
    {
        "name": "abc_part_number",
        "type": "STRING"
    },
    {
        "name": "mele_part_number",
        "type": "STRING"
    },
    {
        "name": "arroweye_part_number",
        "type": "STRING"
    },
    {
        "name": "units_sent",
        "type": "INTEGER"
    }
]
```

### `inventory_analysis.monthly_material_consumption_pivoted`

```json
[
    {
        "name": "event_month",
        "type": "TIMESTAMP"
    },
    {
        "name": "cards",
        "type": "INTEGER"
    },
    {
        "name": "carriers",
        "type": "INTEGER"
    },
    {
        "name": "catalogs",
        "type": "INTEGER"
    },
    {
        "name": "envelopes",
        "type": "INTEGER"
    },
    {
        "name": "inserts",
        "type": "INTEGER"
    },
    {
        "name": "activation_labels",
        "type": "INTEGER"
    },
    {
        "name": "total_kits",
        "type": "INTEGER"
    }
]
```

### `inventory_analysis.monthly_materials_sent`

```json
[
    {
        "name": "month",
        "type": "STRING"
    },
    {
        "name": "brand_shortcode",
        "type": "STRING"
    },
    {
        "name": "language_code",
        "type": "STRING"
    },
    {
        "name": "sponsor_name",
        "type": "STRING"
    },
    {
        "name": "program_name",
        "type": "STRING"
    },
    {
        "name": "kit_id",
        "type": "STRING"
    },
    {
        "name": "kit_year",
        "type": "STRING"
    },
    {
        "name": "is_replacement",
        "type": "BOOLEAN"
    },
    {
        "name": "material_type_code",
        "type": "STRING"
    },
    {
        "name": "material_id",
        "type": "STRING"
    },
    {
        "name": "sh_part_number",
        "type": "STRING"
    },
    {
        "name": "material_description",
        "type": "STRING"
    },
    {
        "name": "material_variant",
        "type": "STRING"
    },
    {
        "name": "cards_sent",
        "type": "INTEGER"
    },
    {
        "name": "material_units_sent",
        "type": "INTEGER"
    }
]
```

### `inventory_analysis.requested_kit_summary`

```json
[
    {
        "name": "event_month",
        "type": "STRING"
    },
    {
        "name": "kit_id",
        "type": "STRING"
    },
    {
        "name": "fis_package_id",
        "type": "STRING"
    },
    {
        "name": "brand_shortcode",
        "type": "STRING"
    },
    {
        "name": "language_code",
        "type": "STRING"
    },
    {
        "name": "sponsor_name",
        "type": "STRING"
    },
    {
        "name": "program_name",
        "type": "STRING"
    },
    {
        "name": "kit_year",
        "type": "STRING"
    },
    {
        "name": "is_replacement",
        "type": "BOOLEAN"
    },
    {
        "name": "is_catalog_only",
        "type": "BOOLEAN"
    },
    {
        "name": "kits_requested",
        "type": "INTEGER"
    },
    {
        "name": "cards_requested",
        "type": "INTEGER"
    },
    {
        "name": "catalogs_requested",
        "type": "INTEGER"
    },
    {
        "name": "total_materials_in_kit",
        "type": "INTEGER"
    }
]
```

## Dataset: `inventory_modeling`

### `inventory_modeling.card_event`

```json
[
    {
        "name": "event_id",
        "type": "STRING",
        "mode": "REQUIRED",
        "description": "Primary key. Unique event identifier (UUID from NONMON field 154). One row per card lifecycle event."
    },
    {
        "name": "vendor_partner",
        "type": "STRING",
        "mode": "REQUIRED",
        "description": "The vendor/partner that reported this event (e.g. FIS). Allows the table to generalize to other partners in the future."
    },
    {
        "name": "card_proxy",
        "type": "STRING",
        "mode": "REQUIRED",
        "description": "The card proxy number \u2014 a 12-14 digit non-PCI identifier uniquely identifying a single physical card (NONMON field 56). Corresponds to member_card.fis_identifier in Harmony. This is the primary key for threading events across the fulfillment chain."
    },
    {
        "name": "member_fis_identifier",
        "type": "STRING",
        "description": "The member/cardholder identifier \u2014 a 10-digit non-PCI number uniquely identifying a single cardholder account (NONMON field 89). Corresponds to member.fis_identifier in Harmony. Stored for future joins to Harmony; not modeled as its own entity here."
    },
    {
        "name": "fis_package_id",
        "type": "STRING",
        "description": "FK to kit_identifier (identifier_type = fis_package_id). The FIS package ID that determines which kit of materials is associated with this card (NONMON field 13). This is the canonical path to resolve what materials should have been sent."
    },
    {
        "name": "event_type",
        "type": "STRING",
        "mode": "REQUIRED",
        "description": "Normalized event type from NONMON field 83. Values include: CARD_CREATED, CARD_REGISTERED, EMBOSS_PENDING, EMBOSS_COMPLETE, ACTIVATED, REPLACEMENT_CREATED, LOST_STOLEN, ADDRESS_CHANGE, PURSE_CREATED, UNSUSPEND, CLOSE. Events that trigger fulfillment: CARD_CREATED, CARD_REGISTERED, EMBOSS_COMPLETE, REPLACEMENT_CREATED."
    },
    {
        "name": "event_timestamp",
        "type": "TIMESTAMP",
        "description": "When the event occurred, from NONMON field 37 (format: MMDDYYYY HH:MM:SS)."
    },
    {
        "name": "file_date",
        "type": "DATE",
        "description": "The date of the source NONMON file, extracted from the filename (e.g. 02152026 from STDNONMON02152026_Soda_Health_Inc.psv). Useful for partitioning and incremental loads."
    },
    {
        "name": "gcs_source_uri",
        "type": "STRING",
        "description": "Full GCS URI of the source file. Enables spot-checking and traceability back to the raw data."
    },
    {
        "name": "source_metadata",
        "type": "RECORD",
        "fields": [
            {
                "name": "product_name",
                "type": "STRING"
            },
            {
                "name": "sponsor_shortcode",
                "type": "STRING"
            },
            {
                "name": "event_description",
                "type": "STRING"
            },
            {
                "name": "card_status",
                "type": "STRING"
            }
        ],
        "description": "Raw source values preserved as-is from the NONMON file. product_name: FIS plan/product name (field 14). sponsor_shortcode: FIS sponsor code (field 9). event_description: raw event detail (field 57). card_status: card status at time of event (field 52)."
    }
]
```

### `inventory_modeling.fulfillment_work_order`

```json
[
    {
        "name": "work_order_id",
        "type": "STRING",
        "description": "The vendor partner batch identifier grouping cards processed together (e.g. WO25034185BS). Each work order maps to exactly one program and one input file. Null for records not yet assigned to a work order."
    },
    {
        "name": "vendor_partner",
        "type": "STRING",
        "mode": "REQUIRED",
        "description": "The vendor/partner that reported this fulfillment action (e.g. ABCorp). Allows the table to generalize to other fulfillment partners in the future."
    },
    {
        "name": "card_proxy",
        "type": "STRING",
        "mode": "REQUIRED",
        "description": "The card proxy number \u2014 a 12-14 digit non-PCI identifier for the physical card. Joins to card_event.card_proxy to thread through the fulfillment chain and resolve the kit/materials via the card event fis_package_id."
    },
    {
        "name": "processing_date",
        "type": "DATE",
        "description": "The date the vendor partner processed this card/work order."
    },
    {
        "name": "status",
        "type": "STRING",
        "description": "The fulfillment status reported by the vendor partner. Known values for ABCorp: Shipped, Perso Completed, Inserting Completed, Cancelled."
    },
    {
        "name": "ship_date",
        "type": "DATE",
        "description": "The date the vendor partner shipped the assembled kit to the member. Null if not yet shipped or if cancelled."
    },
    {
        "name": "gcs_source_uri",
        "type": "STRING",
        "description": "Full GCS URI or source reference for the work order file. Enables spot-checking and traceability back to the raw data."
    },
    {
        "name": "source_metadata",
        "type": "RECORD",
        "fields": [
            {
                "name": "abc_program_name",
                "type": "STRING"
            },
            {
                "name": "input_file",
                "type": "STRING"
            }
        ],
        "description": "Raw source values preserved as-is from the work order file. abc_program_name: the vendor partner label for the kit/program (e.g. SODA-MFG-IHPC-2026-EN). input_file: the FIS embossing file that triggered this work order (e.g. SodaHe-292-NORM-20251101-0.NAF.xml)."
    }
]
```

### `inventory_modeling.kit`

```json
[
    {
        "name": "metadata",
        "type": "RECORD",
        "mode": "NULLABLE",
        "fields": [
            {
                "name": "catalog_upon_enrollment",
                "type": "STRING",
                "mode": "NULLABLE"
            },
            {
                "name": "implementation_status",
                "type": "STRING",
                "mode": "NULLABLE"
            },
            {
                "name": "postage",
                "type": "STRING",
                "mode": "NULLABLE"
            },
            {
                "name": "member_scenarios",
                "type": "STRING",
                "mode": "NULLABLE"
            },
            {
                "name": "live_date",
                "type": "DATE",
                "mode": "NULLABLE"
            },
            {
                "name": "pbp",
                "type": "STRING",
                "mode": "NULLABLE"
            },
            {
                "name": "notes",
                "type": "STRING",
                "mode": "NULLABLE"
            }
        ]
    },
    {
        "name": "is_catalog_only",
        "type": "BOOLEAN",
        "mode": "NULLABLE"
    },
    {
        "name": "is_replacement",
        "type": "BOOLEAN",
        "mode": "NULLABLE"
    },
    {
        "name": "program_name",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "brand_shortcode",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "sponsor_name",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "language_code",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "primary_vendor",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "kit_year",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "kit_id",
        "type": "STRING",
        "mode": "NULLABLE"
    }
]
```

### `inventory_modeling.kit_backup_20260303`

```json
[
    {
        "name": "kit_id",
        "type": "STRING"
    },
    {
        "name": "kit_year",
        "type": "STRING"
    },
    {
        "name": "brand_shortcode",
        "type": "STRING"
    },
    {
        "name": "language_code",
        "type": "STRING"
    },
    {
        "name": "sponsor_name",
        "type": "STRING"
    },
    {
        "name": "program_name",
        "type": "STRING"
    },
    {
        "name": "is_replacement",
        "type": "BOOLEAN"
    },
    {
        "name": "is_catalog_only",
        "type": "BOOLEAN"
    },
    {
        "name": "primary_vendor",
        "type": "STRING"
    },
    {
        "name": "metadata",
        "type": "RECORD",
        "fields": [
            {
                "name": "implementation_status",
                "type": "STRING"
            },
            {
                "name": "live_date",
                "type": "DATE"
            },
            {
                "name": "uat_status",
                "type": "STRING"
            },
            {
                "name": "postage",
                "type": "STRING"
            },
            {
                "name": "notes",
                "type": "STRING"
            },
            {
                "name": "member_scenarios",
                "type": "STRING"
            },
            {
                "name": "pbp",
                "type": "STRING"
            },
            {
                "name": "catalog_upon_enrollment",
                "type": "STRING"
            }
        ]
    }
]
```

### `inventory_modeling.kit_identifier`

```json
[
    {
        "name": "identifier_type",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "identifier_value",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "kit_id",
        "type": "STRING",
        "mode": "NULLABLE"
    }
]
```

### `inventory_modeling.kit_material`

```json
[
    {
        "name": "material_type_code",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "material_id",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "kit_id",
        "type": "STRING",
        "mode": "NULLABLE"
    }
]
```

### `inventory_modeling.material`

```json
[
    {
        "name": "variant",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "sh_part_number",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "brand_shortcode",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "year_introduced",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "description",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "material_type_code",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "language_code",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "material_id",
        "type": "STRING",
        "mode": "NULLABLE"
    }
]
```

### `inventory_modeling.material_component`

```json
[
    {
        "name": "description",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "component_role",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "component_part_id",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "parent_material_id",
        "type": "STRING",
        "mode": "NULLABLE"
    }
]
```

### `inventory_modeling.material_type`

```json
[
    {
        "name": "material_type_code",
        "type": "STRING",
        "mode": "REQUIRED",
        "description": "Primary key. One of: CARD, CARRIER, CATALOG, ENVELOPE, INSERT, ACTIVATION_LABEL"
    },
    {
        "name": "material_type_name",
        "type": "STRING",
        "description": "Human-readable name for the material type (e.g. Card, Carrier, Catalog)"
    },
    {
        "name": "description",
        "type": "STRING",
        "description": "Detailed description of what this material type represents and any variant info"
    }
]
```

### `inventory_modeling.material_vendor_xref`

```json
[
    {
        "name": "vendor_part_number",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "vendor_name",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "material_id",
        "type": "STRING",
        "mode": "NULLABLE"
    }
]
```

## Dataset: `invoicing`

### `invoicing.brand_kit_monthly_summary`

```json
[
    {
        "name": "month",
        "type": "STRING"
    },
    {
        "name": "sponsor_name",
        "type": "STRING"
    },
    {
        "name": "brand_shortcode",
        "type": "STRING"
    },
    {
        "name": "kit_id",
        "type": "STRING"
    },
    {
        "name": "program_name",
        "type": "STRING"
    },
    {
        "name": "language_code",
        "type": "STRING"
    },
    {
        "name": "fis_package_id",
        "type": "STRING"
    },
    {
        "name": "abc_fg_number",
        "type": "STRING"
    },
    {
        "name": "kits_created",
        "type": "INTEGER"
    },
    {
        "name": "cards",
        "type": "INTEGER"
    },
    {
        "name": "catalogs",
        "type": "INTEGER"
    }
]
```

### `invoicing.ivr_calls_unified`

```json
[
    {
        "name": "call_id",
        "type": "STRING"
    },
    {
        "name": "call_date",
        "type": "DATE"
    },
    {
        "name": "call_timestamp",
        "type": "TIMESTAMP"
    },
    {
        "name": "sponsor_id",
        "type": "STRING"
    },
    {
        "name": "sponsor_name",
        "type": "STRING"
    },
    {
        "name": "brand_id",
        "type": "STRING"
    },
    {
        "name": "brand_name",
        "type": "STRING"
    },
    {
        "name": "customer_id",
        "type": "STRING"
    },
    {
        "name": "customer_name",
        "type": "STRING"
    },
    {
        "name": "member_id",
        "type": "STRING"
    },
    {
        "name": "program_id",
        "type": "STRING"
    },
    {
        "name": "call_direction",
        "type": "STRING"
    },
    {
        "name": "data_source",
        "type": "STRING"
    },
    {
        "name": "system_source",
        "type": "STRING"
    },
    {
        "name": "call_outcome",
        "type": "STRING"
    },
    {
        "name": "reached_agent",
        "type": "BOOLEAN"
    },
    {
        "name": "is_ivr_only",
        "type": "BOOLEAN"
    },
    {
        "name": "total_call_duration",
        "type": "INTEGER"
    },
    {
        "name": "ivr_duration",
        "type": "INTEGER"
    },
    {
        "name": "agent_duration",
        "type": "INTEGER"
    },
    {
        "name": "telephony_billable_seconds",
        "type": "INTEGER"
    },
    {
        "name": "agent_billable_seconds",
        "type": "INTEGER"
    },
    {
        "name": "telephony_billable_minutes_rounded",
        "type": "INTEGER"
    },
    {
        "name": "agent_billable_minutes_rounded",
        "type": "INTEGER"
    },
    {
        "name": "handle_time_10_minute_cap",
        "type": "INTEGER"
    },
    {
        "name": "has_complete_data",
        "type": "BOOLEAN"
    },
    {
        "name": "raw_data_source",
        "type": "STRING"
    }
]
```

### `invoicing.ivr_calls_unified_backup_20260204`

```json
[
    {
        "name": "call_id",
        "type": "STRING"
    },
    {
        "name": "call_date",
        "type": "DATE"
    },
    {
        "name": "call_timestamp",
        "type": "TIMESTAMP"
    },
    {
        "name": "sponsor_id",
        "type": "STRING"
    },
    {
        "name": "sponsor_name",
        "type": "STRING"
    },
    {
        "name": "brand_id",
        "type": "STRING"
    },
    {
        "name": "brand_name",
        "type": "STRING"
    },
    {
        "name": "customer_id",
        "type": "STRING"
    },
    {
        "name": "customer_name",
        "type": "STRING"
    },
    {
        "name": "member_id",
        "type": "STRING"
    },
    {
        "name": "program_id",
        "type": "STRING"
    },
    {
        "name": "call_direction",
        "type": "STRING"
    },
    {
        "name": "data_source",
        "type": "STRING"
    },
    {
        "name": "system_source",
        "type": "STRING"
    },
    {
        "name": "call_outcome",
        "type": "STRING"
    },
    {
        "name": "reached_agent",
        "type": "BOOLEAN"
    },
    {
        "name": "is_ivr_only",
        "type": "BOOLEAN"
    },
    {
        "name": "total_call_duration",
        "type": "INTEGER"
    },
    {
        "name": "ivr_duration",
        "type": "INTEGER"
    },
    {
        "name": "agent_duration",
        "type": "INTEGER"
    },
    {
        "name": "telephony_billable_seconds",
        "type": "INTEGER"
    },
    {
        "name": "agent_billable_seconds",
        "type": "INTEGER"
    },
    {
        "name": "telephony_billable_minutes_rounded",
        "type": "INTEGER"
    },
    {
        "name": "agent_billable_minutes_rounded",
        "type": "INTEGER"
    },
    {
        "name": "has_complete_data",
        "type": "BOOLEAN"
    },
    {
        "name": "raw_data_source",
        "type": "STRING"
    }
]
```

### `invoicing.ivr_calls_unified_backup_20260205_pre_offered_fix`

```json
[
    {
        "name": "call_id",
        "type": "STRING"
    },
    {
        "name": "call_date",
        "type": "DATE"
    },
    {
        "name": "call_timestamp",
        "type": "TIMESTAMP"
    },
    {
        "name": "sponsor_id",
        "type": "STRING"
    },
    {
        "name": "sponsor_name",
        "type": "STRING"
    },
    {
        "name": "brand_id",
        "type": "STRING"
    },
    {
        "name": "brand_name",
        "type": "STRING"
    },
    {
        "name": "customer_id",
        "type": "STRING"
    },
    {
        "name": "customer_name",
        "type": "STRING"
    },
    {
        "name": "member_id",
        "type": "STRING"
    },
    {
        "name": "program_id",
        "type": "STRING"
    },
    {
        "name": "call_direction",
        "type": "STRING"
    },
    {
        "name": "data_source",
        "type": "STRING"
    },
    {
        "name": "system_source",
        "type": "STRING"
    },
    {
        "name": "call_outcome",
        "type": "STRING"
    },
    {
        "name": "reached_agent",
        "type": "BOOLEAN"
    },
    {
        "name": "is_ivr_only",
        "type": "BOOLEAN"
    },
    {
        "name": "total_call_duration",
        "type": "INTEGER"
    },
    {
        "name": "ivr_duration",
        "type": "INTEGER"
    },
    {
        "name": "agent_duration",
        "type": "INTEGER"
    },
    {
        "name": "telephony_billable_seconds",
        "type": "INTEGER"
    },
    {
        "name": "agent_billable_seconds",
        "type": "INTEGER"
    },
    {
        "name": "telephony_billable_minutes_rounded",
        "type": "INTEGER"
    },
    {
        "name": "agent_billable_minutes_rounded",
        "type": "INTEGER"
    },
    {
        "name": "has_complete_data",
        "type": "BOOLEAN"
    },
    {
        "name": "raw_data_source",
        "type": "STRING"
    }
]
```

### `invoicing.ivr_modified_invoice`

```json
[
    {
        "name": "invoice_month",
        "type": "STRING"
    },
    {
        "name": "brand_name",
        "type": "STRING"
    },
    {
        "name": "customer_name",
        "type": "STRING"
    },
    {
        "name": "program_id",
        "type": "STRING"
    },
    {
        "name": "call_count",
        "type": "INTEGER"
    },
    {
        "name": "telephony_ivr_minutes",
        "type": "FLOAT"
    },
    {
        "name": "call_center_agent_minutes",
        "type": "FLOAT"
    },
    {
        "name": "telephony_ivr_minutes_rounded",
        "type": "INTEGER"
    },
    {
        "name": "call_center_agent_minutes_rounded",
        "type": "INTEGER"
    },
    {
        "name": "agent_handle_time_10_min_cap",
        "type": "INTEGER"
    }
]
```

### `invoicing.kit_lookup`

```json
[
    {
        "name": "kit_id",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "year",
        "type": "INTEGER",
        "mode": "NULLABLE"
    },
    {
        "name": "has_card",
        "type": "BOOLEAN",
        "mode": "NULLABLE"
    },
    {
        "name": "has_catalog",
        "type": "BOOLEAN",
        "mode": "NULLABLE"
    },
    {
        "name": "language",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "client_program",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "is_evergreen",
        "type": "BOOLEAN",
        "mode": "NULLABLE"
    }
]
```

### `invoicing.member_first_card_count`

```json
[
    {
        "name": "sponsor_name",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "year",
        "type": "INTEGER",
        "mode": "NULLABLE"
    },
    {
        "name": "month",
        "type": "INTEGER",
        "mode": "NULLABLE"
    },
    {
        "name": "members_w_first_card",
        "type": "INTEGER",
        "mode": "NULLABLE"
    }
]
```

### `invoicing.member_invoicing_history`

```json
[
    {
        "name": "recorded_at",
        "type": "DATE"
    },
    {
        "name": "sponsor_id",
        "type": "STRING"
    },
    {
        "name": "member_id",
        "type": "STRING"
    },
    {
        "name": "sponsor_identifier",
        "type": "STRING"
    },
    {
        "name": "non_deleted_cards",
        "type": "INTEGER"
    },
    {
        "name": "non_deleted_enrollments",
        "type": "INTEGER"
    },
    {
        "name": "contract_id",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "plan_id",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "segment_id",
        "type": "STRING",
        "mode": "NULLABLE"
    }
]
```

### `invoicing.member_invoicing_history-2025-01-24T15_47_03`

```json
[
    {
        "name": "recorded_at",
        "type": "DATE"
    },
    {
        "name": "sponsor_id",
        "type": "STRING"
    },
    {
        "name": "member_id",
        "type": "STRING"
    },
    {
        "name": "sponsor_identifier",
        "type": "STRING"
    },
    {
        "name": "non_deleted_cards",
        "type": "INTEGER"
    },
    {
        "name": "non_deleted_enrollments",
        "type": "INTEGER"
    },
    {
        "name": "contract_id",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "plan_id",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "segment_id",
        "type": "STRING",
        "mode": "NULLABLE"
    }
]
```

### `invoicing.member_shipment_timeline`

```json
[
    {
        "name": "member_id",
        "type": "STRING"
    },
    {
        "name": "sponsor_id",
        "type": "STRING"
    },
    {
        "name": "customer_id",
        "type": "STRING"
    },
    {
        "name": "customer_name",
        "type": "STRING"
    },
    {
        "name": "brand_id",
        "type": "STRING"
    },
    {
        "name": "brand_name",
        "type": "STRING"
    },
    {
        "name": "sponsor_program_id",
        "type": "STRING"
    },
    {
        "name": "event_type",
        "type": "STRING"
    },
    {
        "name": "event_date",
        "type": "TIMESTAMP"
    },
    {
        "name": "is_initial",
        "type": "BOOLEAN"
    },
    {
        "name": "kit_id",
        "type": "STRING"
    },
    {
        "name": "item_id",
        "type": "STRING"
    },
    {
        "name": "created_at",
        "type": "TIMESTAMP"
    },
    {
        "name": "processor",
        "type": "STRING"
    },
    {
        "name": "kit_has_card",
        "type": "BOOLEAN"
    },
    {
        "name": "kit_has_catalog",
        "type": "BOOLEAN"
    },
    {
        "name": "kit_language",
        "type": "STRING"
    },
    {
        "name": "kit_client_program",
        "type": "STRING"
    },
    {
        "name": "kit_year",
        "type": "INTEGER"
    }
]
```

### `invoicing.non-deleted_member_count_PMPM_report`

```json
[
    {
        "name": "year",
        "type": "INTEGER",
        "mode": "NULLABLE"
    },
    {
        "name": "month",
        "type": "INTEGER",
        "mode": "NULLABLE"
    },
    {
        "name": "program",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "sponsor_id",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "sponsor_name",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "customer_name",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "total_members",
        "type": "INTEGER",
        "mode": "NULLABLE"
    },
    {
        "name": "billable_members",
        "type": "INTEGER",
        "mode": "NULLABLE"
    },
    {
        "name": "with_current_year_enrollment",
        "type": "INTEGER",
        "mode": "NULLABLE"
    },
    {
        "name": "future_year_only",
        "type": "INTEGER",
        "mode": "NULLABLE"
    },
    {
        "name": "pending_current_year",
        "type": "INTEGER",
        "mode": "NULLABLE"
    },
    {
        "name": "expired_current_year",
        "type": "INTEGER",
        "mode": "NULLABLE"
    },
    {
        "name": "cancelled_current_year",
        "type": "INTEGER",
        "mode": "NULLABLE"
    },
    {
        "name": "prior_year_only",
        "type": "INTEGER",
        "mode": "NULLABLE"
    },
    {
        "name": "never_enrolled",
        "type": "INTEGER",
        "mode": "NULLABLE"
    }
]
```

### `invoicing.program_enrollment_pmpm`

```json
[
    {
        "name": "month",
        "type": "DATE",
        "mode": "NULLABLE"
    },
    {
        "name": "year",
        "type": "INTEGER",
        "mode": "NULLABLE"
    },
    {
        "name": "month_num",
        "type": "INTEGER",
        "mode": "NULLABLE"
    },
    {
        "name": "plan_year",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "program_id",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "sponsor_program_identifier",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "sponsor_id",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "sponsor_name",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "customer_name",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "active_enrollment_member_count",
        "type": "INTEGER",
        "mode": "NULLABLE"
    },
    {
        "name": "total_non_deleted_member_count",
        "type": "INTEGER",
        "mode": "NULLABLE"
    }
]
```

### `invoicing.reimbursement_denial_letters`

```json
[
    {
        "name": "denial_letter_year",
        "type": "INTEGER",
        "mode": "NULLABLE"
    },
    {
        "name": "denial_letter_month",
        "type": "INTEGER",
        "mode": "NULLABLE"
    },
    {
        "name": "customer_name",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "name",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "program_id",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "denial_letter_count",
        "type": "INTEGER",
        "mode": "NULLABLE"
    }
]
```

### `invoicing.reimbursement_disbursement_stats`

## Dataset: `looker_poc`

### `salesforce_data_loader.call_summary`

```json
[
    {
        "name": "Id",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "OwnerId",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "IsDeleted",
        "type": "BOOLEAN",
        "mode": "NULLABLE"
    },
    {
        "name": "Name",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "RecordTypeId",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "CreatedDate",
        "type": "TIMESTAMP",
        "mode": "NULLABLE"
    },
    {
        "name": "CreatedById",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "SystemModstamp",
        "type": "TIMESTAMP",
        "mode": "NULLABLE"
    },
    {
        "name": "LastActivityDate",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "LastViewedDate",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "LastReferencedDate",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "NVMStatsSF__After_Call_Work_Time__c",
        "type": "FLOAT",
        "mode": "NULLABLE"
    },
    {
        "name": "NVMStatsSF__Agent2_ID__c",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "NVMStatsSF__Agent2_Transfer_Time__c",
        "type": "FLOAT",
        "mode": "NULLABLE"
    },
    {
        "name": "NVMStatsSF__Agent2__c",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "NVMStatsSF__AgentChkStr__c",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "NVMStatsSF__Agent_Consult_Time__c",
        "type": "FLOAT",
        "mode": "NULLABLE"
    },
    {
        "name": "NVMStatsSF__Agent_Event_String__c",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "NVMStatsSF__Agent_List__c",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "NVMStatsSF__Agent_Percent__c",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "NVMStatsSF__Agent_Phone_Number__c",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "NVMStatsSF__Agent_Ring_Duration__c",
        "type": "FLOAT",
        "mode": "NULLABLE"
    },
    {
        "name": "NVMStatsSF__Agent_Talk_Time__c",
        "type": "FLOAT",
        "mode": "NULLABLE"
    },
    {
        "name": "NVMStatsSF__Agent__c",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "NVMStatsSF__AutoPhaseStart__c",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "NVMStatsSF__Automation_Segment__c",
        "type": "FLOAT",
        "mode": "NULLABLE"
    },
    {
        "name": "NVMStatsSF__CLID__c",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "NVMStatsSF__CR_Interrupts__c",
        "type": "FLOAT",
        "mode": "NULLABLE"
    },
    {
        "name": "NVMStatsSF__CR_Start_Immediate__c",
        "type": "BOOLEAN",
        "mode": "NULLABLE"
    },
    {
        "name": "NVMStatsSF__CallDisposition__c",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "NVMStatsSF__CallEndTime__c",
        "type": "TIMESTAMP",
        "mode": "NULLABLE"
    },
    {
        "name": "NVMStatsSF__CallGuid__c",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "NVMStatsSF__CallTime__c",
        "type": "TIMESTAMP",
        "mode": "NULLABLE"
    },
    {
        "name": "NVMStatsSF__Call_Diverted__c",
        "type": "BOOLEAN",
        "mode": "NULLABLE"
    },
    {
        "name": "NVMStatsSF__Call_Rating__c",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "NVMStatsSF__Call_Recording__c",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "NVMStatsSF__Call_Transcription__c",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "NVMStatsSF__Categories__c",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "NVMStatsSF__Categorized_At__c",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "NVMStatsSF__Channel__c",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "NVMStatsSF__ChkStr__c",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "NVMStatsSF__Confidence__c",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "NVMStatsSF__Connected__c",
        "type": "BOOLEAN",
        "mode": "NULLABLE"
    },
    {
        "name": "NVMStatsSF__Consult_Time__c",
        "type": "FLOAT",
        "mode": "NULLABLE"
    },
    {
        "name": "NVMStatsSF__ConversationGuid__c",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "NVMStatsSF__Crosstalk_Percent__c",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "NVMStatsSF__Customer_Percent__c",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "NVMStatsSF__Data_Source_Values__c",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "NVMStatsSF__Date__c",
        "type": "DATE",
        "mode": "NULLABLE"
    },
    {
        "name": "NVMStatsSF__EndApplet__c",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "NVMStatsSF__EndReason__c",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "NVMStatsSF__EndRecorded__c",
        "type": "BOOLEAN",
        "mode": "NULLABLE"
    },
    {
        "name": "NVMStatsSF__External_Consult_Time__c",
        "type": "FLOAT",
        "mode": "NULLABLE"
    },
    {
        "name": "NVMStatsSF__External_Transfer_Phone__c",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "NVMStatsSF__External_Transfer_Time__c",
        "type": "FLOAT",
        "mode": "NULLABLE"
    },
    {
        "name": "NVMStatsSF__Interaction_JSON__c",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "NVMStatsSF__Interaction_Type__c",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "NVMStatsSF__Interrupted_Time__c",
        "type": "FLOAT",
        "mode": "NULLABLE"
    },
    {
        "name": "NVMStatsSF__Key_Event_String__c",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "NVMStatsSF__Language__c",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "NVMStatsSF__Last_Agent_Summary__c",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "NVMStatsSF__Last_Queue_Result__c",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "NVMStatsSF__Local_Date__c",
        "type": "DATE",
        "mode": "NULLABLE"
    },
    {
        "name": "NVMStatsSF__Local_Hour__c",
        "type": "INTEGER",
        "mode": "NULLABLE"
    },
    {
        "name": "NVMStatsSF__Local_ISO8601_Week__c",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "NVMStatsSF__MOS__c",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "NVMStatsSF__MessageTaken__c",
        "type": "BOOLEAN",
        "mode": "NULLABLE"
    },
    {
        "name": "NVMStatsSF__Monitored__c",
        "type": "BOOLEAN",
        "mode": "NULLABLE"
    },
    {
        "name": "NVMStatsSF__NVM_AgentID__c",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "NVMStatsSF__NVM_Service_Name__c",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "NVMStatsSF__NVM_Telephone_Number__c",
        "type": "INTEGER",
        "mode": "NULLABLE"
    },
    {
        "name": "NVMStatsSF__New_Events__c",
        "type": "BOOLEAN",
        "mode": "NULLABLE"
    },
    {
        "name": "NVMStatsSF__NextTime__c",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "NVMStatsSF__Notes__c",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "NVMStatsSF__Number_of_Applets__c",
        "type": "FLOAT",
        "mode": "NULLABLE"
    },
    {
        "name": "NVMStatsSF__Number_of_PCI_Transfers__c",
        "type": "FLOAT",
        "mode": "NULLABLE"
    },
    {
        "name": "NVMStatsSF__Number_of_Segments__c",
        "type": "FLOAT",
        "mode": "NULLABLE"
    },
    {
        "name": "NVMStatsSF__Number_of_Transfers__c",
        "type": "FLOAT",
        "mode": "NULLABLE"
    },
    {
        "name": "NVMStatsSF__Number_of_Transfers_to_Applet__c",
        "type": "FLOAT",
        "mode": "NULLABLE"
    },
    {
        "name": "NVMStatsSF__Number_of_Warm_Transfers__c",
        "type": "FLOAT",
        "mode": "NULLABLE"
    },
    {
        "name": "NVMStatsSF__PCI_Time__c",
        "type": "FLOAT",
        "mode": "NULLABLE"
    },
    {
        "name": "NVMStatsSF__Park_Time__c",
        "type": "FLOAT",
        "mode": "NULLABLE"
    },
    {
        "name": "NVMStatsSF__Post_Call_Automation__c",
        "type": "FLOAT",
        "mode": "NULLABLE"
    },
    {
        "name": "NVMStatsSF__Queue_Agent_Queue_List__c",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "NVMStatsSF__Queue_Duration__c",
        "type": "FLOAT",
        "mode": "NULLABLE"
    },
    {
        "name": "NVMStatsSF__Queue_List__c",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "NVMStatsSF__Queue_Name__c",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "NVMStatsSF__Queued_Callback__c",
        "type": "BOOLEAN",
        "mode": "NULLABLE"
    },
    {
        "name": "NVMStatsSF__Recording_Duration__c",
        "type": "FLOAT",
        "mode": "NULLABLE"
    },
    {
        "name": "NVMStatsSF__Related_Account__c",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "NVMStatsSF__Related_Case__c",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "NVMStatsSF__Related_Contact__c",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "NVMStatsSF__Related_Lead__c",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "NVMStatsSF__Related_Opportunity__c",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "NVMStatsSF__Ring_List__c",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "NVMStatsSF__Server__c",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "NVMStatsSF__Silence_Percent__c",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "NVMStatsSF__Skills_List__c",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "NVMStatsSF__StartRecorded__c",
        "type": "BOOLEAN",
        "mode": "NULLABLE"
    },
    {
        "name": "NVMStatsSF__TaskExists__c",
        "type": "BOOLEAN",
        "mode": "NULLABLE"
    },
    {
        "name": "NVMStatsSF__TaskID__c",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "NVMStatsSF__Time_Zone__c",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "NVMStatsSF__Total_Call_Duration__c",
        "type": "FLOAT",
        "mode": "NULLABLE"
    },
    {
        "name": "NVMStatsSF__Trace__c",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "NVMStatsSF__UTC_ISO8601_Week__c",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "NVMStatsSF__Version__c",
        "type": "FLOAT",
        "mode": "NULLABLE"
    },
    {
        "name": "NVMStatsSF__Virtual_Queues__c",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "NVMStatsSF__Warm_Transfer_Time__c",
        "type": "FLOAT",
        "mode": "NULLABLE"
    },
    {
        "name": "NVMStatsSF__dateAgentId__c",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "NVMStatsSF__Abandoned__c",
        "type": "BOOLEAN",
        "mode": "NULLABLE"
    },
    {
        "name": "NVMStatsSF__Day_of_Week__c",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "NVMStatsSF__Delivery_Attempts__c",
        "type": "FLOAT",
        "mode": "NULLABLE"
    },
    {
        "name": "NVMStatsSF__Fiscal_Quarter__c",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "NVMStatsSF__Handle_Time__c",
        "type": "FLOAT",
        "mode": "NULLABLE"
    },
    {
        "name": "NVMStatsSF__Hour__c",
        "type": "INTEGER",
        "mode": "NULLABLE"
    },
    {
        "name": "NVMStatsSF__Last_Ring_Duration__c",
        "type": "FLOAT",
        "mode": "NULLABLE"
    },
    {
        "name": "NVMStatsSF__Last_State__c",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "NVMStatsSF__Local_Day_of_Week__c",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "NVMStatsSF__Month_of_Year__c",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "NVMStatsSF__Numeric_Wk_of_Year__c",
        "type": "FLOAT",
        "mode": "NULLABLE"
    },
    {
        "name": "NVMStatsSF__Related_To__c",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "NVMStatsSF__Short_Abandon__c",
        "type": "BOOLEAN",
        "mode": "NULLABLE"
    },
    {
        "name": "NVMStatsSF__Task_Link__c",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "NVMStatsSF__Week_of_Year__c",
        "type": "INTEGER",
        "mode": "NULLABLE"
    },
    {
        "name": "NVMStatsSF__Yr_Wk_Day_Hr__c",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "UTC_ISO_Week__c",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "IsHandleTimeOver10Mins__c",
        "type": "BOOLEAN",
        "mode": "NULLABLE"
    },
    {
        "name": "Handle_Time_Over_10_Minutes__c",
        "type": "FLOAT",
        "mode": "NULLABLE"
    },
    {
        "name": "Total_Call_Duration_including_ACW__c",
        "type": "FLOAT",
        "mode": "NULLABLE"
    },
    {
        "name": "Offered_Custom__c",
        "type": "BOOLEAN",
        "mode": "NULLABLE"
    },
    {
        "name": "Short_Abandon_Custom__c",
        "type": "BOOLEAN",
        "mode": "NULLABLE"
    },
    {
        "name": "True_Abandon_Custom__c",
        "type": "BOOLEAN",
        "mode": "NULLABLE"
    },
    {
        "name": "Call_Met_Service_Level__c",
        "type": "FLOAT",
        "mode": "NULLABLE"
    },
    {
        "name": "MeetsServiceLevel__c",
        "type": "FLOAT",
        "mode": "NULLABLE"
    },
    {
        "name": "NVMStatsSF__Sentiment__c",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "Voice_Call_Account_Name__c",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "Handled__c",
        "type": "BOOLEAN",
        "mode": "NULLABLE"
    }
]
```

## Dataset: `salesforce_data_transfer`

### `snapshots.daily_sifcounts_snapshot`

```json
Unable to retrieve schema from specified table.
```

