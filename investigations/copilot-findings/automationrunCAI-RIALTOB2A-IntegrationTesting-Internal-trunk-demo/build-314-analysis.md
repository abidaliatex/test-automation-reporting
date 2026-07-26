# Root Cause Analysis — Build 314

**Source Report:** [build-314.md](../../../reports/build-failures/automationrunCAI-RIALTOB2A-IntegrationTesting-Internal-trunk-demo/build-314.md)

---

## Build Summary

Build: `automationrunCAI-RIALTOB2A-IntegrationTesting-Internal-trunk-demo` #314  
Total Tests: 15  
Passed: 12  
Failed: 3  
Pass Rate: 80.0%

---

## Root Cause Groups

## `discountType` missing in original MediaHouse order readback

**Affected Features:**
- `rialtoB2A(CASS)TestCase29.feature`

**Affected Scenarios:**
- verify that order arrived in MH from rilato - magzine order original state (`tc_getMHTC_MZN04a`)

**Failure Pattern:**
`orders.printDetails.discountType` expected `[RIALTO]` found `[null]`

**Evidence:**
- `Mismatch on field: orders.printDetails.discountType expected [[RIALTO]] but found [[null]]`
- The checked-out revision message was `updated testcase29 data tc_getMHTC_MZN04a`, so this failure correlates with a recent TC29 data change but does not by itself prove whether the regression is in test data or service output

**Impact:** 1 failure

**Confidence:** Medium

---

## Reverted full-page state was not reflected after the MediaHouse size-change flow

**Affected Features:**
- `rialtoB2A(CASS)TestCase29.feature`

**Affected Scenarios:**
- verify that order arrived in MH from rilato - magzine order after Uppslag/Spread/Panorama change (`tc_getMHTC_MZN04b`)
- confirms order created in Agency for testcase 29 - after size change (`tc_getIntegrationRialtoMZN04b`)

**Failure Pattern:**
Expected reverted full-page values (`HALVLIGG`, original dimensions, and ~5000 pricing), but both MH and Rialto responses still returned `UPPSLAG`/expanded dimensions with ~11000 pricing.

**Evidence:**
- MH verification returned `plaCode` = `UPPSLAG`, width `2`, depth `297`, and `orderBasketPriceSummary.totalGross` = `11000.00` instead of the expected reverted values
- Rialto verification returned `placementId` = `UPPSLAG`, width `460`, depth `297`, and `priceGross` = `11000.0`, matching the same non-reverted state seen in MH

**Impact:** 2 failures

**Confidence:** High

---

## Summary

- Build 314 is UNSTABLE due to 3 failures in the TC29 magazine integration flow.
- One failure is an original-state readback mismatch in MediaHouse (`discountType` returned `null`).
- Two failures show the post-update flow did not return to the expected full-page state; both systems still expose the `UPPSLAG`/higher-price state.

---

## Root Cause

- The first failure may be caused by either missing `discountType` propagation in the MH payload or a TC29 expectation/data change, because the build was run from a revision whose commit message explicitly references `tc_getMHTC_MZN04a`.
- The second and third failures are consistent with one shared integration-state problem: after the MH size-change flow, the reverted values expected by the test were not reflected in either the MH readback or the downstream Rialto readback.

---

## Affected Components

- `rialtoB2A(CASS)TestCase29.feature`
- MediaHouse basket order GET validation for `tc_getMHTC_MZN04a` and `tc_getMHTC_MZN04b`
- Rialto order GET validation for `tc_getIntegrationRialtoMZN04b`
- Potentially the TC29 test data revised in commit `29dc5af001ff347cd07782f72c5d94c34c027394`

---

## Recommended Fix

- Review the TC29 data/expectation change tied to `tc_getMHTC_MZN04a` and confirm whether `discountType` should still be asserted as `RIALTO`.
- Trace the MH update/revert flow for TC29 and verify whether the expected full-page values are actually written back before the follow-up MH and Rialto GET checks run.

---

## Prevention

- Add a focused assertion/log step that records the effective placement, dimensions, and price immediately after the MH update step so state-drift is visible before the final GET validations.
