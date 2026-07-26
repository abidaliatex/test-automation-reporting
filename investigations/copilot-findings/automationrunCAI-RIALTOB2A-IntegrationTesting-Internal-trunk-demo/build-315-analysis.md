# Root Cause Analysis — Build 315

**Source Report:** [build-315.md](../../../reports/build-failures/automationrunCAI-RIALTOB2A-IntegrationTesting-Internal-trunk-demo/build-315.md)

---

## Build Summary

Build: automationrunCAI-RIALTOB2A-IntegrationTesting-Internal-trunk-demo #315
Total Tests: 15
Passed: 12
Failed: 3
Pass Rate: 80.0%

---

## Root Cause Groups

## discountType Field Not Propagated in MH Order Readback

**Affected Features:**
- rialtoB2A (CASS TC29 Magazine (change to Uppslag/Spread/Panorama))

**Affected Scenarios:**
- MEDIAHOUSE - Verify original full-page order state in MediaHouse - #1.1 (TC29)

**Failure Pattern:**
`orders.printDetails.discountType` expected `[RIALTO]` found `[null]`

**Evidence:**
- `Mismatch on field: orders.printDetails.discountType expected [[RIALTO]] but found [[null]]`
- Stack trace ends at `SoftAssert.assertAll` in `ApiStepDefinition.tearDown(ApiStepDefinition.java:69)`
- Regression since build 314

**Impact:** 1 failure

**Confidence:** High

---

## Placement/Size/Price Not Reverted — UPPSLAG State Persists Instead of HALVLIGG

**Affected Features:**
- rialtoB2A (CASS TC29 Magazine (change to Uppslag/Spread/Panorama))

**Affected Scenarios:**
- MEDIAHOUSE - Verify updated MediaHouse basket state - #1.1 (TC29)
- RIALTO - Verify Rialto reflects the reverted full-page state - #1.1 (TC29)

**Failure Pattern:**
`plaCode` / `placementId` expected `[HALVLIGG]` found `[UPPSLAG]`; all related dimensions and prices reflect the UPPSLAG (full-page) values instead of the HALVLIGG (half-page) values.

**Evidence:**
- `orders.printDetails.plaCode expected [[HALVLIGG]] but found [[UPPSLAG]]`
- `orders.printDetails.width expected [[1]] but found [[2]]`
- `orders.printDetails.depth expected [[146]] but found [[297]]`
- `orders.printDetails.netAmount expected [[5000.0]] but found [[11000.0]]`
- `orderAdDetails.placementId expected [[HALVLIGG]] but found [[UPPSLAG]]`
- `orderAdDetails.priceGross expected [[5000.0]] but found [[11000.0]]`
- `orderAdDetails.commissionAmount expected [[155.0]] but found [[68.2]]`
- Both MH basket and Rialto order verification see UPPSLAG state — suggests the revert/update to HALVLIGG was not applied in the system before verification
- Regression since build 314

**Impact:** 2 failures

**Confidence:** High

---

## Summary

- Build 315 is UNSTABLE with 3 failures, all in TC29 (Magazine — change to Uppslag/Spread/Panorama).
- Both root causes have been regressing since build 314.

## Root Cause

- **discountType null**: `discountType` is not populated in MH response payload for `orders.printDetails.discountType`; possibly a mapping or persistence gap in the Rialto→MH integration layer.
- **Stale UPPSLAG state**: After TC29 changes the order to Uppslag/Spread/Panorama and then attempts to revert it to HALVLIGG, both MH and Rialto still return UPPSLAG values. The revert API call may have failed silently or the order state was not flushed before the GET verification.

## Affected Components

- Rialto → MediaHouse B2A integration: `printDetails.discountType` mapping
- TC29 revert flow: placement change (UPPSLAG → HALVLIGG), pricing, and commission recalculation
- MH basket order GET validation (`Verify updated MediaHouse basket state`)
- Rialto order GET validation (`Verify Rialto reflects the reverted full-page state`)

## Recommended Fix

- Verify `discountType` is present in outbound integration payload and persisted/mapped correctly in MH.
- Investigate whether the HALVLIGG revert API call in TC29 completes successfully before verification steps; add appropriate wait/polling if the update is asynchronous.

## Prevention

- Add contract assertions for `printDetails.discountType` in integration smoke coverage.
- Add a guard/assertion after the revert API call to confirm the system reflects the updated state before running GET verification steps.
