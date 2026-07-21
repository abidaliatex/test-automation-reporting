# Jenkins Build Failure Report

---

## Build Summary

Build: `automationrunCAI-RIALTOB2A-IntegrationTesting-Internal-trunk-demo` #297  
Date: 2026-07-21 21:10:05 UTC  
Status: `UNSTABLE`  
Total Tests: 14  
Passed: 11  
Failed: 3  
Pass Rate: 78.6%

---

## Root Cause Groups

## MediaHouse discount and basket pricing mismatch

**Affected Features:**
- `rialtoB2A(CASS)TestCase4.feature`

**Affected Scenarios:**
- verify that order arrived in MH from rilato - placement (`tc_getMHTC03`)
- verify that order arrived in MH from rilato - placement - after change (`tc_getMHTC03a`)

**Failure Pattern:**
`discountType` expected `[RIALTO]` found `[null]`; MH financial summary fields (`commission`, `vat`, `orderbasketSum`, `totalInclVat`) differ from expected values.

**Evidence:**
- `tc_getMHTC03`: `orders[0].printDetails.discountType` expected `[RIALTO]` found `[null]`
- `tc_getMHTC03a`: `orderBasketPriceSummary.commission` expected `[7750.00]` found `[12500.00]`; `orderBasketPriceSummary.orderbasketSum` expected `[242250.00]` found `[237500.00]`; `orderBasketPriceSummary.totalInclVat` expected `[302812.50]` found `[296875.00]`; `orders[0].vat` expected `[60562.50]` found `[59375.00]`

**Impact:** 2 failures

**Confidence:** High

## Rialto post-update order payload mismatch

**Affected Features:**
- `rialtoB2A(CASS)TestCase4.feature`

**Affected Scenarios:**
- get order in rialto using prisa id- check if placement updated (`tc_getIntegrationRialto05b`)

**Failure Pattern:**
Rialto GET response after placement change returns unexpected order header/detail status and pricing values.

**Evidence:**
- `orderHeader.statusFlags` expected `[PRELIMINARY]` found `[]`; `orderAdDetails[0].depth` expected `[184]` found `[372]`
- `orderHeader.commissionAmount` expected `[7750.00]` found `[620.0]`; `orderAdDetails[0].priceNet` expected `[250000.00]` found `[249380.0]`; `orderAdDetails[0].commissionAmount` expected `[7750.00]` found `[620.0]`

**Impact:** 1 failure

**Confidence:** High
