# Build Failure Report — Build #262

| Field | Value |
|---|---|
| **Build ID** | 262 |
| **Date** | 2026-07-05 |
| **Job** | `automationrunCAI-RIALTOB2A-IntegrationTesting-Internal-trunk-demo` |
| **Build URL** | https://crossadv.atex.com/jenkins/job/automationrunCAI-RIALTOB2A-IntegrationTesting-Internal-trunk-demo/262/ |
| **Branch** | `trunk` |
| **Status** | ⚠️ UNSTABLE |

## Failing Tests / Steps

| Test Suite / Feature | Scenario | Test Case | Result |
|---|---|---|---|
| `CASS TC4 Change Placement` | verify that order arrived in MH from rilato - placement | `tc_getMHTC03` | FAILED |
| `CASS TC4 Change Placement` | verify that order arrived in MH from rilato - placement - after change | `tc_getMHTC03a` | FAILED |
| `CASS TC4 Change Placement` | get order in rialto using prisa id- check if placement updated | `tc_getIntegrationRialto05b` | FAILED |

## Error Output

```text
java.lang.AssertionError: The following asserts failed:
- Mismatch on field: orders[0].printDetails.discountType expected [[RIALTO]] but found [[null]]
- Mismatch on field: orderBasketPriceSummary.totalInclVat expected [155683.63] but found [171598.78]
- Mismatch on field: orders[0].vat expected [31136.73] but found [47051.88]
- Mismatch on field: orders[0].orderTotalInclVat expected [155683.63] but found [171598.78]

java.lang.AssertionError: The following asserts failed:
- Mismatch on field: orders[0].printDetails.discountType expected [[NONE]] but found [[RIALTO]]
- Mismatch on field: orderBasketPriceSummary.commission expected [7750.00] but found [8000.00]
- Mismatch on field: orderBasketPriceSummary.orderbasketSum expected [242250.00] but found [242000.00]
- Mismatch on field: orderBasketPriceSummary.totalInclVat expected [302812.50] but found [302500.00]

java.lang.AssertionError: The following asserts failed:
- Mismatch on field: orderHeader.statusFlags expected [[PRELIMINARY]] but found [[]]
- Mismatch on field: orderHeader.commissionAmount expected [7750.00] but found [620.0]
- Mismatch on field: orderAdDetails[0].depth expected [184] but found [372]
- Mismatch on field: orderAdDetails[0].priceNet expected [250000.00] but found [249380.0]
```

## Suggested Next Steps

- Verify discount/commission mapping rules between Rialto and MediaHouse for placement-change flows.
- Re-run the three failed CASS TC4 assertions after mapping validation.
- See investigation: [build-262-analysis.md](../../investigations/copilot-findings/build-262-analysis.md)
