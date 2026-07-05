## Build Summary

- **Build ID:** `automationrunCAI-RIALTOB2A-IntegrationTesting-Internal-trunk-demo #263`
- **Date:** 2026-07-05 19:49 UTC
- **Status:** UNSTABLE
- **Total Tests:** 14
- **Passed:** 11
- **Failed:** 3
- **Pass Rate:** 78.6%

## Failing Tests / Steps

- `rialtoB2A(CASS)TestCase4.feature`
  - `tc_getMHTC03` — verify that order arrived in MH from rilato - placement
  - `tc_getMHTC03a` — verify that order arrived in MH from rilato - placement - after change
  - `tc_getIntegrationRialto05b` — get order in rialto using prisa id- check if placement updated

## Error Output

```text
tc_getMHTC03
- orders[0].printDetails.discountType expected [RIALTO] but found [null]
- orderBasketPriceSummary.totalInclVat expected [155683.63] but found [171598.78]
- orders[0].vat expected [31136.73] but found [47051.88]

tc_getMHTC03a
- orders[0].printDetails.discountType expected [NONE] but found [RIALTO]
- orderBasketPriceSummary.commission expected [7750.00] but found [8000.00]
- orderBasketPriceSummary.totalInclVat expected [302812.50] but found [302500.00]

tc_getIntegrationRialto05b
- orderAdDetails[0].placementId expected [SIDAN3] but found [TEXT]
- orderAdDetails[0].depth expected [184] but found [372]
- orderAdDetails[0].priceNet expected [250000.00] but found [124546.9]
```

## Suggested Next Steps

- Recheck placement-change handling between Rialto and MediaHouse for `discountType`, placement mapping, and price recalculation.
- Compare expected vs actual order totals after the placement update flow before rerunning the suite.
