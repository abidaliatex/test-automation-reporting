# Root Cause Analysis — Build 313

**Source Report:** [build-313.md](../../../reports/build-failures/automationrunCAI-RIALTOB2A-IntegrationTesting-Internal-trunk-demo/build-313.md)

---

## Build Summary

Build: automationrunCAI-RIALTOB2A-IntegrationTesting-Internal-trunk-demo #313  
Total Tests: 14  
Passed: 13  
Failed: 1  
Pass Rate: 92.9%

---

## Root Cause Groups

## discountType Field Not Propagated in MH Order Readback

**Affected Features:**
- rialtoB2A (CASS TC7 Change Date, Size & Placement)

**Affected Scenarios:**
- verify that order arrived in MH from rilato - Change Date, Size & Placement (tc_getMHTC06)

**Failure Pattern:**
`orders[0].printDetails.discountType` expected `[RIALTO]` found `[null]`

**Evidence:**
- `Mismatch on field: orders[0].printDetails.discountType expected [[RIALTO]] but found [[null]]`
- Stack trace ends at `SoftAssert.assertAll` in `ApiStepDefinition.tearDown(ApiStepDefinition.java:69)`
- Scenario execution reached MH GET verification step and failed only at field assertion

**Impact:** 1 failure

**Confidence:** High

---

## Summary

- Build is UNSTABLE due to one regression in MH order verification.

## Root Cause

- The `discountType` value is missing (`null`) in MH response payload for `orders[0].printDetails.discountType`.

## Affected Components

- Rialto → MediaHouse B2A integration mapping for `printDetails.discountType`
- MH basket order GET validation path (`tc_getMHTC06`)

## Recommended Fix

- Verify `discountType` is present in outbound integration payload and persisted/mapped correctly in MH before GET readback.

## Prevention

- Add targeted contract/assertion checks for `printDetails.discountType` in integration smoke coverage.
