# Jenkins Build Failure Report

## Build Summary

Build: `automationrunCAI-RIALTOB2A-IntegrationTesting-Internal-trunk-demo` #269  
Date: 2026-07-05 21:18 UTC  
Status: UNSTABLE  
Total Tests: 14  
Passed: 11  
Failed: 3  
Pass Rate: 78.6%

---

## Root Cause Groups

### MediaHouse pricing and discount assertions no longer match placement-change output

**Affected Features:**
- `rialtoB2A (CASS TC4 Change Placement)`
- MediaHouse order retrieval validation

**Affected Scenarios:**
- `tc_getMHTC03` — verify that order arrived in MH from rilato - placement
- `tc_getMHTC03a` — verify that order arrived in MH from rilato - placement - after change

**Failure Pattern:**
MediaHouse GET checks fail after the placement-change flow because returned discount and pricing fields do not match the expected fixture values.

**Evidence:**
- `tc_getMHTC03`: `orders[0].printDetails.discountType` expected `RIALTO`, found `null`; `orderBasketPriceSummary.totalInclVat` expected `155683.63`, found `171598.78`; `orders[0].vat` expected `31136.73`, found `47051.88`.
- `tc_getMHTC03a`: `orders[0].printDetails.discountType` expected `NONE`, found `RIALTO`; `orderBasketPriceSummary.commission` expected `7750.00`, found `8000.00`; `orderBasketPriceSummary.totalInclVat` expected `302812.50`, found `302500.00`.

**Impact:** 2 failures

**Confidence:** High

### Rialto placement recalculation assertions no longer match post-update response

**Affected Features:**
- `rialtoB2A (CASS TC4 Change Placement)`
- Rialto order retrieval validation

**Affected Scenarios:**
- `tc_getIntegrationRialto05b` — get order in rialto using prisa id- check if placement updated

**Failure Pattern:**
Rialto GET validation fails after the placement update because the response does not match the expected placement-derived status, depth, and commission values.

**Evidence:**
- `orderHeader.statusFlags` expected `PRELIMINARY`, found empty.
- `orderHeader.commissionAmount` expected `7750.00`, found `620.0`.
- `orderAdDetails[0].depth` expected `184`, found `372`; `orderAdDetails[0].priceNet` expected `250000.00`, found `249380.0`.

**Impact:** 1 failure

**Confidence:** High

## Failing Tests / Steps

- `tc_getMHTC03` — verify that order arrived in MH from rilato - placement
- `tc_getMHTC03a` — verify that order arrived in MH from rilato - placement - after change
- `tc_getIntegrationRialto05b` — get order in rialto using prisa id- check if placement updated

## Error Output

```text
java.lang.AssertionError: The following asserts failed:
  Mismatch on field: orders[0].printDetails.discountType expected [[RIALTO]] but found [[null]]
  Mismatch on field: orderBasketPriceSummary.totalInclVat expected [155683.63] but found [171598.78]
  Mismatch on field: orders[0].vat expected [31136.73] but found [47051.88]
  Mismatch on field: orders[0].printDetails.discountType expected [[NONE]] but found [[RIALTO]]
  Mismatch on field: orderBasketPriceSummary.commission expected [7750.00] but found [8000.00]
  Mismatch on field: orderBasketPriceSummary.totalInclVat expected [302812.50] but found [302500.00]
  Mismatch on field: orderHeader.statusFlags expected [[PRELIMINARY]] but found [[]]
  Mismatch on field: orderHeader.commissionAmount expected [7750.00] but found [620.0]
  Mismatch on field: orderAdDetails[0].depth expected [184] but found [372]
  at stepDefinition.ApiStepDefinition.tearDown(ApiStepDefinition.java:69)
```

## Suggested Next Steps

- Compare the build #269 MediaHouse and Rialto GET payloads with the expected values in `getMHB2A.csv` and `getRialtoB2A.csv`.
- Verify whether the API v88 revision intentionally changed placement-update discount, commission, VAT, or depth calculations before updating test expectations.
