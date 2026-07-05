# Jenkins Build Failure Report

---

## Build Summary

Build: `automationrunCAI-RIALTOB2A-IntegrationTesting-Internal-trunk-demo` #264  
Total Tests: 14  
Passed: 11  
Failed: 3  
Pass Rate: 78.6%  
Date: 2026-07-05 20:01 UTC  
Status: UNSTABLE

---

## Root Cause Groups

### MediaHouse retrieval values diverge from expected placement-change contract

**Affected Features:**
- `rialtoB2A (CASS TC4 Change Placement)`

**Affected Scenarios:**
- verify that order arrived in MH from rilato - placement (`tc_getMHTC03`)
- verify that order arrived in MH from rilato - placement - after change (`tc_getMHTC03a`)

**Failure Pattern:**
Discount/pricing totals returned by MediaHouse GET do not match expected values after placement-change flow.

**Evidence:**
- `orders[0].printDetails.discountType` expected `RIALTO`, found `null`
- `orderBasketPriceSummary.totalInclVat` expected `155683.63`, found `171598.78`
- `orders[0].printDetails.discountType` expected `NONE`, found `RIALTO`
- `orderBasketPriceSummary.commission` expected `7750.00`, found `8000.00`

**Impact:** 2 failures  
**Confidence:** High

### Rialto retrieval values diverge after placement update

**Affected Features:**
- `rialtoB2A (CASS TC4 Change Placement)`

**Affected Scenarios:**
- get order in rialto using prisa id- check if placement updated (`tc_getIntegrationRialto05b`)

**Failure Pattern:**
Rialto GET payload fields (status, depth, commission) do not align with expected post-update values.

**Evidence:**
- `orderHeader.statusFlags` expected `PRELIMINARY`, found empty
- `orderAdDetails[0].depth` expected `184`, found `372`
- `orderHeader.commissionAmount` expected `7750.00`, found `620.0`

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
  Mismatch on field: orders[0].orderTotalInclVat expected [155683.63] but found [171598.78]
  Mismatch on field: orders[0].printDetails.discountType expected [[NONE]] but found [[RIALTO]]
  Mismatch on field: orderBasketPriceSummary.commission expected [7750.00] but found [8000.00]
  Mismatch on field: orderBasketPriceSummary.orderbasketSum expected [242250.00] but found [242000.00]
  Mismatch on field: orderBasketPriceSummary.totalInclVat expected [302812.50] but found [302500.00]
  Mismatch on field: orderHeader.statusFlags expected [[PRELIMINARY]] but found [[]]
  Mismatch on field: orderAdDetails[0].depth expected [184] but found [372]
  Mismatch on field: orderHeader.commissionAmount expected [7750.00] but found [620.0]
  at stepDefinition.ApiStepDefinition.tearDown(ApiStepDefinition.java:69)
```

## Suggested Next Steps

- Re-check expected fixture values used by `getMHB2A.csv` and `getRialtoB2A.csv` for the placement-change flow.
- Confirm whether API v88 changed discount/commission semantics; align either service output or test expectations.
