# Jenkins Build Failure Report

---

## Build Summary

Build: `automationrunCAI-RIALTOB2A-IntegrationTesting-Internal-trunk-demo` #306  
Date: 2026-07-24 11:56:08 UTC  
Status: `UNSTABLE`  
Total Tests: 15  
Passed: 12  
Failed: 3  
Pass Rate: 80.0%

### Failing Tests / Steps

- MEDIAHOUSE - Verify original full-page order state in MediaHouse - #1.1 (`tc_getMHTC_MZN04a`)
- MEDIAHOUSE - Verify updated MediaHouse basket state - #1.1 (`tc_getMHTC_MZN04b`)
- RIALTO - Verify Rialto reflects the reverted full-page state - #1.1 (`tc_getIntegrationRialtoMZN04b`)

---

## Root Cause Groups

## Original-state expectation mismatch in MediaHouse

**Affected Features:**
- `rialtoB2A(CASS TC29 Magazine (change to Uppslag/Spread/Panorama)`

**Affected Scenarios:**
- MEDIAHOUSE - Verify original full-page order state in MediaHouse - #1.1 (`tc_getMHTC_MZN04a`)

**Failure Pattern:**
`orders.printDetails.discountType` expected `[RIALTO]` found `[null]`

**Evidence:**
- `orders.printDetails.discountType` expected `[[RIALTO]]` but found `[[null]]`
- Assertion error raised at `stepDefinition.ApiStepDefinition.tearDown(ApiStepDefinition.java:69)`

**Impact:** 1 failure

**Confidence:** High

## Placement and pricing remain in spread (`UPPSLAG`) state instead of expected reverted/full-page state

**Affected Features:**
- `rialtoB2A(CASS TC29 Magazine (change to Uppslag/Spread/Panorama)`

**Affected Scenarios:**
- MEDIAHOUSE - Verify updated MediaHouse basket state - #1.1 (`tc_getMHTC_MZN04b`)
- RIALTO - Verify Rialto reflects the reverted full-page state - #1.1 (`tc_getIntegrationRialtoMZN04b`)

**Failure Pattern:**
Placement and pricing fields expected full-page values (`HALVLIGG`, 5000-range totals) but returned spread values (`UPPSLAG`, 11000-range totals).

**Evidence:**
- `orders.printDetails.plaCode` expected `[[HALVLIGG]]` but found `[[UPPSLAG]]`; `orderBasketPriceSummary.totalInclVat` expected `[6056.25]` but found `[13062.50]`
- `orderAdDetails.placementId` expected `[[HALVLIGG]]` but found `[[UPPSLAG]]`; `priceGross` expected `[5000.0]` but found `[11000.0]`

**Impact:** 2 failures

**Confidence:** High
