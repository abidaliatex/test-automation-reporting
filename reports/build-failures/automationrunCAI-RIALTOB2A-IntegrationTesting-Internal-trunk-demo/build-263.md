# Jenkins Build Failure Report

## Build Summary

Build: `automationrunCAI-RIALTOB2A-IntegrationTesting-Internal-trunk-demo` #263  
Date: 2026-07-05 19:49 UTC  
Status: UNSTABLE  
Total Tests: 14  
Passed: 11  
Failed: 3  
Pass Rate: 78.6%

---

## Root Cause Groups

### MediaHouse response contract mismatch after placement-change flow

**Affected Features:**
- `rialtoB2A (CASS TC4 Change Placement)`
- MediaHouse basket/order verification

**Affected Scenarios:**
- verify that order arrived in MH from rilato - placement (`tc_getMHTC03`)
- verify that order arrived in MH from rilato - placement - after change (`tc_getMHTC03a`)

**Failure Pattern:**
Post-change MH GET assertions return pricing/discount values inconsistent with expected fixtures.

**Evidence:**
- `discountType` mismatch in both scenarios (`RIALTO`→`null`, `NONE`→`RIALTO`).
- Commission/totals mismatches: expected `7750.00`/`302812.50`, found `8000.00`/`302500.00`.

**Impact:** 2 failures

**Confidence:** High

### Rialto recalculation mismatch after placement update

**Affected Features:**
- `rialtoB2A (CASS TC4 Change Placement)`
- Rialto order retrieval validation

**Affected Scenarios:**
- get order in rialto using prisa id- check if placement updated (`tc_getIntegrationRialto05b`)

**Failure Pattern:**
Rialto GET validation returns different placement, discount, and pricing values than expected immediately after placement update.

**Evidence:**
- `placementId` expected `SIDAN3`, found `TEXT`; `depth` expected `184`, found `372`.
- `priceGross` expected `250000.00`, found `192192.0`; `discountAmount` expected `0.0`, found `63660.63`.

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
  Mismatch on field: orders[0].printDetails.discountType expected [[NONE]] but found [[RIALTO]]
  Mismatch on field: orderBasketPriceSummary.commission expected [7750.00] but found [8000.00]
  Mismatch on field: orderAdDetails[0].placementId expected [SIDAN3] but found [TEXT]
  Mismatch on field: orderAdDetails[0].depth expected [184] but found [372]
  Mismatch on field: orderAdDetails[0].priceGross expected [250000.00] but found [192192.0]
  Mismatch on field: orderAdDetails[0].discountAmount expected [0.0] but found [63660.63]
  at stepDefinition.ApiStepDefinition.tearDown(ApiStepDefinition.java:69)
```

## Suggested Next Steps

- Confirm whether API v88 intentionally changed placement-change pricing/discount behavior before updating expected values.
- Diff expected rows in `getMHB2A.csv` and `getRialtoB2A.csv` against build #263 runtime payloads.
