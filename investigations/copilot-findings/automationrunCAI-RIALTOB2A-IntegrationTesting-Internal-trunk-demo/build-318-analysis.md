# Build 318 — Root Cause Analysis

**Source Report:** [build-318.md](../../../reports/build-failures/automationrunCAI-RIALTOB2A-IntegrationTesting-Internal-trunk-demo/build-318.md)
**Job:** automationrunCAI-RIALTOB2A-IntegrationTesting-Internal-trunk-demo
**Date:** 2026-07-27

---

## Summary

- Build 318 is **UNSTABLE** with 2 failures out of 15 tests in `rialtoB2A(CASS)TestCase29.feature`.
- Both failing scenarios show `failedSince: 314`, so this is an ongoing regression rather than a new break in build 318.
- The build ran revision `00c0ddcb05c2b5fc127c1956e5b147790ff4a0f8` (`updated testcase29 data tc_getMHTC_MZN04b`); the updated-state MediaHouse scenario is fixed in this run, leaving two residual failures.

---

## Build Summary

Build: 318  
Total Tests: 15  
Passed: 13  
Failed: 2  
Pass Rate: 86.7%

---

## Root Cause Groups

## Missing `discountType` in MediaHouse original-state order

**Affected Features:**
- `rialtoB2A(CASS)TestCase29.feature`

**Affected Scenarios:**
- MEDIAHOUSE - Verify original full-page order state in MediaHouse - #1.1 (`tc_getMHTC_MZN04a`)

**Failure Pattern:**
`orders.printDetails.discountType expected [RIALTO] found [null]`

**Evidence:**
- JUnit reports a single assertion mismatch on `orders.printDetails.discountType` during `tc_getMHTC_MZN04a`.
- The scenario metadata shows `failedSince: 314`, which matches the long-running pattern seen in earlier builds.

**Impact:** 1 failure

**Confidence:** High

## Reverted full-page values are not restored in Rialto

**Affected Features:**
- `rialtoB2A(CASS)TestCase29.feature`

**Affected Scenarios:**
- RIALTO - Verify Rialto reflects the reverted full-page state - #1.1 (`tc_getIntegrationRialtoMZN04b`)

**Failure Pattern:**
`placementId expected [HALVLIGG] found [UPPSLAG]`; reverted size and pricing fields still return Uppslag values

**Evidence:**
- The failed assertion set includes `placementId`, `columns`, `depth`, `width`, `priceGross`, `priceNet`, and commission mismatches, all showing Uppslag values after the revert flow.
- The scenario metadata shows `failedSince: 314`.
- `tc_getMHTC_MZN04b` is `FIXED` in build 318, which suggests the remaining issue is concentrated in the final reverted-state validation path rather than the prior MediaHouse update step.

**Impact:** 1 failure

**Confidence:** High

---

## Root Cause

- The remaining instability is split across two residual regressions in TC29: a missing `discountType` mapping in the MediaHouse original-state readback, and a revert flow that still leaves Rialto on Uppslag dimensions/pricing.

## Affected Components

- Rialto → MediaHouse field mapping for `orders.printDetails.discountType`
- TC29 revert-state propagation/verification path in Rialto B2A integration
- Pricing and placement fields returned by the final Rialto verification step

## Recommended Fix

- Check why `discountType` is omitted in the MediaHouse original-state payload for `tc_getMHTC_MZN04a`.
- Trace the revert path used before `tc_getIntegrationRialtoMZN04b` and confirm the reverted `HALVLIGG` state is persisted before the final Rialto readback.

## Prevention

- Keep an assertion that validates `discountType` presence in original-state MediaHouse verification.
- Add a focused regression check that confirms revert flows restore pre-Uppslag placement and pricing values before final Rialto verification.
