# Jenkins Build Failure Report

---

## Build Summary

Build: `automationrunCAI-RIALTOB2A-IntegrationTesting-Internal-trunk-demo` #305  
Date: 2026-07-24 10:25:04 UTC  
Status: `UNSTABLE`  
Total Tests: 15  
Passed: 12  
Failed: 3  
Pass Rate: 80.0%

### Failing Tests / Steps

- MEDIAHOUSE - Verify original full-page order state in MediaHouse - #1.1
- MEDIAHOUSE - Verify updated MediaHouse basket state - #1.1
- RIALTO - Verify Rialto reflects the reverted full-page state - #1.1

---

## Root Cause Groups

## TC29 placement and pricing assertions do not match the MediaHouse/Rialto order state

**Affected Features:**
- `rialtoB2A(CASS TC29 Magazine (change to Uppslag/Spread/Panorama)`

**Affected Scenarios:**
- MEDIAHOUSE - Verify original full-page order state in MediaHouse - #1.1
- MEDIAHOUSE - Verify updated MediaHouse basket state - #1.1
- RIALTO - Verify Rialto reflects the reverted full-page state - #1.1

**Failure Pattern:**
Expected original or reverted full-page values, but MediaHouse and Rialto return discounted or `UPPSLAG`/spread placement and pricing values instead.

**Evidence:**
- `orders.printDetails.discountType` expected `[[RIALTO]]` found `[[null]]`; `orderBasketPriceSummary.totalInclVat` expected `[7267.50]` found `[2907.00]`
- `orders.printDetails.plaCode` expected `[[HALVLIGG]]` found `[[UPPSLAG]]`; `orderBasketPriceSummary.totalInclVat` expected `[6056.25]` found `[13062.50]`
- `orderAdDetails.placementId` expected `[[HALVLIGG]]` found `[[UPPSLAG]]`; `priceGross` expected `[5000.0]` found `[11000.0]`

**Impact:** 3 failures

**Confidence:** High
