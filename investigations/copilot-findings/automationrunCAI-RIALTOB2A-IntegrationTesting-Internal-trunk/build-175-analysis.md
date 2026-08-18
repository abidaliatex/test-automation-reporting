# Investigation: Build 175 — Root Cause Analysis

**Source Report:** [build-175.md](../../../reports/build-failures/automationrunCAI-RIALTOB2A-IntegrationTesting-Internal-trunk/build-175.md)  
**Job:** automationrunCAI-RIALTOB2A-IntegrationTesting-Internal-trunk  
**Build:** 175  
**Date:** 2026-08-18  
**Status:** UNSTABLE

## Summary
- Build 175 completed as **UNSTABLE** with 28 failing scenarios.
- Failures are concentrated in data mapping/order consistency and price/discount validation.

---

## Build Summary

Build: 175  
Total Tests: 514  
Passed: 486  
Failed: 28  
Pass Rate: 94.6%

---

## Root Cause
- Primary failure drivers are order-line mapping/sequence defects and pricing-calculation divergence, with smaller regressions in status flags, API response handling, and cross-system ID/path handling.

## Root Cause Groups

### Order mapping and line sequencing mismatches

**Affected Features:**
- TestCase9.feature
- TestCase14.feature
- TestCase15.feature
- TestCase19.feature
- TestCase20.feature
- TestCase22.feature
- TestCase23.feature
- TestCase24.feature
- TestCase35.feature
- TestCase37.feature

**Affected Scenarios:**
- User perform CASS GET API - #1.1 (TC14)
- User perform CASS GET API - #1.1 (TC15)
- User perform CASS POST API - #1.1 (TC19)
- User perform CASS POST API - #1.1 (TC20)
- User perform CASS GET API - #1.1 (TC22) [2 failures]
- Verify updated MediaHouse basket state - #1.1 (TC23)
- Verify reverted MediaHouse basket state - #1.1 (TC23)
- Revert two MediaHouse order lines to full page - #1.1 (TC24)
- Verify reverted MediaHouse basket state - #1.1 (TC24)
- RIALTO - Verify updated Agency order after Rialto change - #1.1 (TC35)
- RIALTO - Verify Rialto reflects the updated state - #1.1 (TC37)
- User perform CASS GET API - #1.1 (TC9)

**Failure Pattern:**
`paCode/prodCode/packageId/productId/placementId/depth/moduleCode` values are mismatched, reordered, or not reverted correctly.

**Evidence:**
- `orders[0].printDetails.paCode expected [[SVDTI, AB]] but found [[AB, SVDTI]]` (TC15)
- `orderAdDetails.packageId expected [[AB, SVD]] but found [[SVD, AB]]` (TC19)

**Impact:** 13 failures

**Confidence:** High

### Pricing and discount calculation mismatches

**Affected Features:**
- TestCase5.feature
- TestCase6.feature
- TestCase22.feature
- TestCase31.feature
- TestCase36.feature
- TestCase37.feature
- TestCase9.feature

**Affected Scenarios:**
- User perform CASS GET API - #1.1 (TC22) [1 failure]
- RIALTO - Verify Rialto reflects the reverted full-page state - #1.1 (TC31)
- MEDIAHOUSE - Verify original magazine order state in MediaHouse - #1.1 (TC36)
- MEDIAHOUSE - Verify updated magazine order state in MediaHouse - #1.1 (TC36)
- MEDIAHOUSE - Verify original order state in MediaHouse - #1.1 (TC37)
- MEDIAHOUSE - Verify updated MediaHouse basket state - #1.1 (TC37)
- User perform CASS POST API - #1.1 (TC5)
- User perform CASS POST API - #1.1 (TC6)
- User perform CASS POST API - #1.1 (TC9)

**Failure Pattern:**
`discountAmount/orderDiscount/sumDiscount/netPrice/commission/totalInclVat/vat` values differ from expected calculated outputs.

**Evidence:**
- `discountAmount expected [0.0] but found [63660.63]` (TC5)
- `orderBasketPriceSummary.orderDiscount expected [3600.00] but found [4800.00]` (TC36)

**Impact:** 9 failures

**Confidence:** High

### Missing PRELIMINARY status flag

**Affected Features:**
- TestCase4.feature
- TestCase28.feature
- TestCase29.feature

**Affected Scenarios:**
- User perform CASS POST API - #1.1 (TC4)
- RIALTO - Verify Rialto reflects the reverted full-page state - #1.1 (TC28)
- RIALTO - Verify Rialto reflects the reverted full-page state - #1.1 (TC29)

**Failure Pattern:**
`orderHeader.statusFlags` expected `[PRELIMINARY]` but returned `[]`.

**Evidence:**
- `orderHeader.statusFlags expected [[PRELIMINARY]] but found [[]]` (TC4/TC28/TC29)

**Impact:** 3 failures

**Confidence:** High

### CASS POST response code regression

**Affected Features:**
- TestCase14.feature

**Affected Scenarios:**
- User perform CASS POST API - #1.1 (TC14)

**Failure Pattern:**
CASS POST returned server error status instead of success status.

**Evidence:**
- `{"errorCode":1,"message":null} expected [N200] but found [N500]`

**Impact:** 1 failure

**Confidence:** Medium

### Revert flow path-parameter contract failure

**Affected Features:**
- TestCase24.feature

**Affected Scenarios:**
- Verify Rialto reflects the reverted full-page state - #1.1 (TC24)

**Failure Pattern:**
Revert verification request is built with invalid path parameters.

**Evidence:**
- `Redundant path parameters are: agencyPrisaId=7892. Undefined path parameters are: uuid.`

**Impact:** 1 failure

**Confidence:** High

### Cross-system order identity mismatch

**Affected Features:**
- TestCase35.feature

**Affected Scenarios:**
- MEDIAHOUSE - Verify updated magazine order state in MediaHouse - #1.1 (TC35)

**Failure Pattern:**
MediaHouse basket identity does not match Agency Prisa order identity.

**Evidence:**
- `MH basket ID (orBoxid) [7902] does not match Agency Prisa ID [7903]`

**Impact:** 1 failure

**Confidence:** High

## Affected Components
- CASS order-line mapping and sequence handling
- Pricing/discount calculation logic across Rialto and MediaHouse views
- Order status propagation (`PRELIMINARY`)
- Revert request path parameter assembly
- Cross-system order identity mapping (Agency Prisa ID vs MH basket ID)

## Recommended Fix
- Stabilize order-line mapping/revert behavior first; this is the highest-impact group.
- Re-validate pricing/discount calculations against the latest expected fixtures.
- Add validation on path-parameter construction and cross-system ID consistency before assertions.

## Prevention
- Add contract checks for ordered array fields (`paCode/prodCode/packageId/productId`).
- Add regression checks for `statusFlags` and CASS POST response code (`N200`).
- Add guard checks to fail early when `orBoxid` and Agency Prisa ID diverge.
