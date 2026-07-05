# Jenkins Build Failure Report

## Build Summary

Build: `automationrunCAI-RIALTOB2A-IntegrationTesting-Internal-trunk-demo` #265  
Date: 2026-07-05 20:15 UTC  
Status: UNSTABLE  
Total Tests: 14  
Passed: 11  
Failed: 3  
Pass Rate: 78.6%

---

## Root Cause Groups

### MediaHouse pricing totals and discountType drift after placement change

**Affected Features:**
- `rialtoB2A (CASS TC4 Change Placement)`
- MediaHouse basket retrieval validation

**Affected Scenarios:**
- verify that order arrived in MH from rilato - placement (`tc_getMHTC03`)
- verify that order arrived in MH from rilato - placement - after change (`tc_getMHTC03a`)

**Failure Pattern:**
Placement-change retrieval in MediaHouse returned financial and discount fields that differ from expected values (`discountType`, commission, VAT, totals).

**Evidence:**
- `tc_getMHTC03`: `orders[0].printDetails.discountType` expected `RIALTO`, found `null`; `orderBasketPriceSummary.totalInclVat` expected `155683.63`, found `171598.78`.
- `tc_getMHTC03a`: `orders[0].printDetails.discountType` expected `NONE`, found `RIALTO`; `orderBasketPriceSummary.commission` expected `7750.00`, found `8000.00`; `orderBasketPriceSummary.totalInclVat` expected `302812.50`, found `302500.00`.

**Impact:** 2 failures

**Confidence:** High

### Rialto post-update order detail values inconsistent with expected placement output

**Affected Features:**
- `rialtoB2A (CASS TC4 Change Placement)`
- Rialto order retrieval validation

**Affected Scenarios:**
- get order in rialto using prisa id- check if placement updated (`tc_getIntegrationRialto05b`)

**Failure Pattern:**
Post-update Rialto order retrieval returned mismatches across status and monetary/detail fields (status flag, depth, commission, net values).

**Evidence:**
- `orderHeader.statusFlags` expected `PRELIMINARY`, found empty.
- `orderHeader.commissionAmount` expected `7750.00`, found `620.0`; `orderAdDetails[0].depth` expected `184`, found `372`.

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
  Mismatch on field: orderHeader.statusFlags expected [[PRELIMINARY]] but found [[]]
  Mismatch on field: orderAdDetails[0].depth expected [184] but found [372]
  at stepDefinition.ApiStepDefinition.tearDown(ApiStepDefinition.java:69)
```

## Suggested Next Steps

- Validate whether API v88 intentionally changed placement-change pricing/status field semantics.
- Reconcile expected values in `MediaHouse\\getMHB2A.csv` and `Rialto\\RialtoB2A\\getRialtoB2A.csv` for the failing scenarios.
