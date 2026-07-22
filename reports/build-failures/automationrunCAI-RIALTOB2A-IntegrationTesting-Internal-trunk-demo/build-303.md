# Jenkins Build Failure Report

---

## Build Summary

Build: `automationrunCAI-RIALTOB2A-IntegrationTesting-Internal-trunk-demo` #303  
Date: 2026-07-22 22:36:20 UTC  
Status: `UNSTABLE`  
Total Tests: 15  
Passed: 12  
Failed: 3  
Pass Rate: 80.0%

### Failing Tests / Steps

- MEDIAHOUSE - Verify original full-page order state in MediaHouse (`tc_getMHTC_MZN04a`)
- MEDIAHOUSE - Verify updated MediaHouse basket state (`tc_getMHTC_MZN04b`)
- RIALTO - Verify Rialto reflects the reverted full-page state (`tc_getIntegrationRialtoMZN04b`)

---

## Root Cause Groups

## TC29 placement and pricing assertions do not match the MediaHouse/Rialto order state

**Affected Features:**
- `rialtoB2A(CASS)TestCase29.feature`

**Affected Scenarios:**
- MEDIAHOUSE - Verify original full-page order state in MediaHouse (`tc_getMHTC_MZN04a`)
- MEDIAHOUSE - Verify updated MediaHouse basket state (`tc_getMHTC_MZN04b`)
- RIALTO - Verify Rialto reflects the reverted full-page state (`tc_getIntegrationRialtoMZN04b`)

**Failure Pattern:**
Expected original or reverted full-page values, but MediaHouse and Rialto return discounted or `UPPSLAG`/spread placement and pricing values instead.

**Evidence:**
- `orders.printDetails.discountType` expected `[[RIALTO]]` found `[[null]]`; `orderBasketPriceSummary.totalInclVat` expected `[7267.50]` found `[2907.00]`
- `orders.printDetails.plaCode` expected `[[HALVLIGG]]` found `[[UPPSLAG]]`; `orderBasketPriceSummary.totalInclVat` expected `[6056.25]` found `[13062.50]`
- `orderAdDetails.placementId` expected `[[HALVLIGG]]` found `[[UPPSLAG]]`; `priceGross` expected `[5000.0]` found `[11000.0]`

**Impact:** 3 failures

**Confidence:** High
