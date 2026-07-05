# Jenkins Build Failure Report

## Build Summary

Build: `automationrunCAI-RIALTOB2A-IntegrationTesting-Internal-trunk-demo` #266  
Date: 2026-07-05 20:24 UTC  
Status: UNSTABLE  
Total Tests: 14  
Passed: 11  
Failed: 3  
Pass Rate: 78.6%

---

## Root Cause Groups

### MediaHouse pricing and discount mismatch after placement change

**Affected Features:**
- `rialtoB2A (CASS TC4 Change Placement)`
- MediaHouse order retrieval validation

**Affected Scenarios:**
- verify that order arrived in MH from rilato - placement (`tc_getMHTC03`)
- verify that order arrived in MH from rilato - placement - after change (`tc_getMHTC03a`)

**Failure Pattern:**
MediaHouse GET validations returned unexpected `discountType`, commission, VAT, and total values after the placement-change flow completed.

**Evidence:**
- `tc_getMHTC03`: `orders[0].printDetails.discountType` expected `RIALTO`, found `null`; `orderBasketPriceSummary.totalInclVat` expected `155683.63`, found `171598.78`.
- `tc_getMHTC03a`: `orders[0].printDetails.discountType` expected `NONE`, found `RIALTO`; `orderBasketPriceSummary.commission` expected `7750.00`, found `8000.00`; `orderBasketPriceSummary.totalInclVat` expected `302812.50`, found `302500.00`.

**Impact:** 2 failures

**Confidence:** High

---

### Rialto order detail recalculation mismatch after placement update

**Affected Features:**
- `rialtoB2A (CASS TC4 Change Placement)`
- Rialto order retrieval validation

**Affected Scenarios:**
- get order in rialto using prisa id- check if placement updated (`tc_getIntegrationRialto05b`)

**Failure Pattern:**
Rialto GET validation did not reflect expected placement-derived depth, status flags, and commission values after the update.

**Evidence:**
- `orderHeader.statusFlags` expected `[PRELIMINARY]`, found `[]`.
- `orderAdDetails[0].depth` expected `184`, found `372`.
- `orderHeader.commissionAmount` expected `7750.00`, found `620.0`.

**Impact:** 1 failure

**Confidence:** High

---

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
  Mismatch on field: orders[0].orderTotalInclVat expected [155683.63] but found [171598.78]
  at stepDefinition.ApiStepDefinition.tearDown(ApiStepDefinition.java:69)

java.lang.AssertionError: The following asserts failed:
  Mismatch on field: orders[0].printDetails.discountType expected [[NONE]] but found [[RIALTO]]
  Mismatch on field: orderBasketPriceSummary.commission expected [7750.00] but found [8000.00]
  Mismatch on field: orderBasketPriceSummary.totalInclVat expected [302812.50] but found [302500.00]
  at stepDefinition.ApiStepDefinition.tearDown(ApiStepDefinition.java:69)

java.lang.AssertionError: The following asserts failed:
  Mismatch on field: orderHeader.statusFlags expected [[PRELIMINARY]] but found [[]]
  Mismatch on field: orderAdDetails[0].depth expected [184] but found [372]
  Mismatch on field: orderHeader.commissionAmount expected [7750.00] but found [620.0]
  at stepDefinition.ApiStepDefinition.tearDown(ApiStepDefinition.java:69)
```

## Suggested Next Steps

- Failures have persisted since build #246 without change — confirm whether the service regression is known and tracked.
- Compare `getMHB2A.csv` and `getRialtoB2A.csv` expected values against current API responses.
- Investigate whether placement-change pricing fields (`discountType`, commission, depth) were intentionally changed in the API and update test fixtures accordingly.
