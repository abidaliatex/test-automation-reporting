# Jenkins Build Failure Report

---

## Build Summary

Build: `automationrunCAI-RIALTOB2A-IntegrationTesting-Internal-trunk-demo` #300  
Date: 2026-07-22 15:49:37 UTC  
Status: `UNSTABLE`  
Total Tests: 15  
Passed: 11  
Failed: 4  
Pass Rate: 73.3%

---

## Root Cause Groups

## Rialto created-order verification uses mismatched expected value shape

**Affected Features:**
- `rialtoB2A(CASS)TestCase29.feature`

**Affected Scenarios:**
- RIALTO - Verify created Rialto order and capture shared identifiers (`tc_getIntegrationRialtoMZN04a`)

**Failure Pattern:**
Expected numeric fields are list-wrapped in the assertion data while the Rialto GET response returns scalar values with the same numbers.

**Evidence:**
- `discountAmount` expected `[[3600.0]]` found `[3600.0]`
- `priceGross` expected `[[6000.0]]` found `[6000.0]`

**Impact:** 1 failure

**Confidence:** Medium

## TC29 size-change flow returns unexpected placement and pricing state across MediaHouse and Rialto

**Affected Features:**
- `rialtoB2A(CASS)TestCase29.feature`

**Affected Scenarios:**
- MEDIAHOUSE - Verify original full-page order state in MediaHouse (`tc_getMHTC_MZN04a`)
- MEDIAHOUSE - Verify updated MediaHouse basket state (`tc_getMHTC_MZN04b`)
- RIALTO - Verify Rialto reflects the reverted full-page state (`tc_getIntegrationRialtoMZN04b`)

**Failure Pattern:**
Expected full-page / reverted values do not match actual responses; MediaHouse and Rialto return `UPPSLAG`/discounted pricing values where the assertions expect `HALVLIGG` or non-discounted totals.

**Evidence:**
- `orders.printDetails.discountType` expected `[[RIALTO]]` found `[[null]]`; `orderBasketPriceSummary.totalInclVat` expected `[7267.50]` found `[2907.00]`
- `orders.printDetails.plaCode` expected `[[HALVLIGG]]` found `[[UPPSLAG]]`; `orders.totalPrice` expected `[[5000.00]]` found `[[11000.00]]`
- `orderAdDetails.placementId` expected `[[HALVLIGG]]` found `[[UPPSLAG]]`; `priceGross` expected `[[5000.0]]` found `[11000.0]`

**Impact:** 3 failures

**Confidence:** High
