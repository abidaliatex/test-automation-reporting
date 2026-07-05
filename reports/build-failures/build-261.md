# Build Failure Report — Build #261

| Field | Value |
|---|---|
| **Build ID** | 261 |
| **Date** | 2026-07-05 |
| **Job** | `automationrunCAI-RIALTOB2A-IntegrationTesting-Internal-trunk-demo` |
| **Build URL** | https://crossadv.atex.com/jenkins/job/automationrunCAI-RIALTOB2A-IntegrationTesting-Internal-trunk-demo/261/ |
| **Branch** | `trunk` |
| **Commit** | `4a04ddba` — "updated api version from 87 to 88" |
| **Status** | ⚠️ UNSTABLE |

## Failing Tests / Steps

| Feature | Scenario | Test Case | Result |
|---|---|---|---|
| `rialtoB2A(CASS)TestCase4.feature` | verify that order arrived in MH from Rialto - placement | `tc_getMHTC03` | FAILED |
| `rialtoB2A(CASS)TestCase4.feature` | verify that order arrived in MH from Rialto - placement - after change | `tc_getMHTC03a` | FAILED |
| `rialtoB2A(CASS)TestCase4.feature` | get order in Rialto using prisa id - check if placement updated | `tc_getIntegrationRialto05b` | FAILED |

## Error Output

```text
--- tc_getMHTC03 ---
Mismatch on field: orders[0].printDetails.discountType expected [[RIALTO]] but found [[null]]
Mismatch on field: orderBasketPriceSummary.totalInclVat expected [155683.63] but found [171598.78]
Mismatch on field: orders[0].vat expected [31136.73] but found [47051.88]
Mismatch on field: orders[0].orderTotalInclVat expected [155683.63] but found [171598.78]

--- tc_getMHTC03a ---
Mismatch on field: orders[0].printDetails.discountType expected [[NONE]] but found [[RIALTO]]
Mismatch on field: orderBasketPriceSummary.commission expected [7750.00] but found [8000.00]
Mismatch on field: orderBasketPriceSummary.orderbasketSum expected [242250.00] but found [242000.00]
Mismatch on field: orderBasketPriceSummary.totalInclVat expected [302812.50] but found [302500.00]
Mismatch on field: orders[0].commissions expected [7750.00] but found [8000.00]
Mismatch on field: orders[0].sum expected [242250.00] but found [242000.00]
Mismatch on field: orders[0].vat expected [60562.50] but found [60500.00]
Mismatch on field: orders[0].orderTotalInclVat expected [302812.50] but found [302500.00]

--- tc_getIntegrationRialto05b ---
Mismatch on field: orderHeader.statusFlags expected [[PRELIMINARY]] but found [[]]
Mismatch on field: orderHeader.commissionAmount expected [7750.00] but found [620.0]
Mismatch on field: orderAdDetails[0].depth expected [184] but found [372]
Mismatch on field: orderAdDetails[0].commissionAmount expected [7750.00] but found [620.0]
Mismatch on field: orderAdDetails[0].priceNet expected [250000.00] but found [249380.0]
Mismatch on field: priceGross expected [250000.00] but found [250000.0]
Mismatch on field: orderHeader.priceNetExComm expected [250000.00] but found [250000.0]
Mismatch on field: orderAdDetails[0].priceGross expected [250000.00] but found [250000.0]
Mismatch on field: orderAdDetails[0].priceNetExComm expected [250000.00] but found [250000.0]
```

## Environment

- **API Version**: `880/v1` (bumped from 87 to 88 in latest commit)
- **Build tool**: Maven 3.9.6
- **Runner**: Linux / Jenkins

## Suggested Next Steps

- Investigate discountType mapping changes introduced by API version bump (87→88).
- Review commission rate and pricing recalculation logic in the new API version.
- Check if placement-update sync (MH→Agency) handles depth and statusFlags correctly in v880.
- See investigation: [build-261-analysis.md](../../investigations/copilot-findings/build-261-analysis.md)
