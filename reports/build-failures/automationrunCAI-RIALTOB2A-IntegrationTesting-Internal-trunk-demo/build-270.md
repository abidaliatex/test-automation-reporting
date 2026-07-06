# Jenkins Build Failure Report

## Build Summary

Build: `automationrunCAI-RIALTOB2A-IntegrationTesting-Internal-trunk-demo` #270  
Date: 2026-07-06 10:01 UTC  
Status: UNSTABLE  
Total Tests: 14  
Passed: 11  
Failed: 3  
Pass Rate: 78.6%

---

## Root Cause Groups

### MediaHouse post-placement pricing assertions drift from actual values

**Affected Features:**
- `rialtoB2A (CASS TC4 Change Placement)`
- MediaHouse retrieval checks

**Affected Scenarios:**
- `tc_getMHTC03` — verify that order arrived in MH from rialto - placement
- `tc_getMHTC03a` — verify that order arrived in MH from rialto - placement - after change

**Failure Pattern:**
MediaHouse GET validations fail after placement change because discount and pricing totals in the response differ from expected CSV fixture values.

**Evidence:**
- `tc_getMHTC03`: `orders[0].printDetails.discountType` expected `RIALTO`, found `null`; `orderBasketPriceSummary.totalInclVat` expected `155683.63`, found `171598.78`; `orders[0].orderTotalInclVat` expected `155683.63`, found `171598.78`.
- `tc_getMHTC03a`: `orders[0].printDetails.discountType` expected `NONE`, found `RIALTO`; `orderBasketPriceSummary.commission` expected `7750.00`, found `8000.00`; `orderBasketPriceSummary.totalInclVat` expected `302812.50`, found `302500.00`.

**Impact:** 2 failures

**Confidence:** High

### Rialto post-placement state/amount assertions drift from expected values

**Affected Features:**
- `rialtoB2A (CASS TC4 Change Placement)`
- Rialto retrieval checks

**Affected Scenarios:**
- `tc_getIntegrationRialto05b` — get order in rialto using prisa id- check if placement updated

**Failure Pattern:**
Rialto GET validation after placement update returns different status/depth/commission fields than expected.

**Evidence:**
- `orderHeader.statusFlags` expected `PRELIMINARY`, found empty.
- `orderHeader.commissionAmount` expected `7750.00`, found `620.0`.
- `orderAdDetails[0].depth` expected `184`, found `372`; `orderAdDetails[0].priceNet` expected `250000.00`, found `249380.0`.

**Impact:** 1 failure

**Confidence:** High

## Failing Tests / Steps

- `tc_getMHTC03` — verify that order arrived in MH from rialto - placement
- `tc_getMHTC03a` — verify that order arrived in MH from rialto - placement - after change
- `tc_getIntegrationRialto05b` — get order in rialto using prisa id- check if placement updated

## Error Output

```text
java.lang.AssertionError: The following asserts failed:
  Mismatch on field: orders[0].printDetails.discountType expected [[RIALTO]] but found [[null]]
  Mismatch on field: orderBasketPriceSummary.totalInclVat expected [155683.63] but found [171598.78]
  Mismatch on field: orders[0].vat expected [31136.73] but found [47051.88]
  Mismatch on field: orders[0].orderTotalInclVat expected [155683.63] but found [171598.78]
  Mismatch on field: orders[0].printDetails.discountType expected [[NONE]] but found [[RIALTO]]
  Mismatch on field: orderBasketPriceSummary.commission expected [7750.00] but found [8000.00]
  Mismatch on field: orderBasketPriceSummary.orderbasketSum expected [242250.00] but found [242000.00]
  Mismatch on field: orderBasketPriceSummary.totalInclVat expected [302812.50] but found [302500.00]
  Mismatch on field: orders[0].commissions expected [7750.00] but found [8000.00]
  Mismatch on field: orders[0].sum expected [242250.00] but found [242000.00]
  Mismatch on field: orders[0].vat expected [60562.50] but found [60500.00]
  Mismatch on field: orders[0].orderTotalInclVat expected [302812.50] but found [302500.00]
  Mismatch on field: orderHeader.statusFlags expected [[PRELIMINARY]] but found [[]]
  Mismatch on field: orderHeader.commissionAmount expected [7750.00] but found [620.0]
  Mismatch on field: orderAdDetails[0].depth expected [184] but found [372]
  Mismatch on field: orderAdDetails[0].priceNet expected [250000.00] but found [249380.0]
  at stepDefinition.ApiStepDefinition.tearDown(ApiStepDefinition.java:69)
```

## Suggested Next Steps

- Reconcile expected values in `MediaHouse\getMHB2A.csv` and `Rialto\RialtoB2A\getRialtoB2A.csv` with the actual post-placement payloads from this build.
- Confirm whether revision `4a04ddba1e4e5809017f1f7cf91b06e93e3c19dd` (`updated api version from 87 to 88`) intentionally changed placement pricing/status calculations.
