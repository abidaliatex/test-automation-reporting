# Build 317 — Root Cause Analysis

**Source Report:** [build-317.md](../../../reports/build-failures/automationrunCAI-RIALTOB2A-IntegrationTesting-Internal-trunk-demo/build-317.md)

---

## Summary

- Build 317 is **UNSTABLE** with 4 failures out of 15 tests (73.3% pass rate).
- All failures are in `rialtoB2A(CASS)TestCase29.feature`.
- Three failures are tightly linked to a MediaHouse basket/order correlation mismatch.
- One failure remains in the final Rialto verification, where the order state does not match the expected reverted full-page values.

---

## Root Cause

## MediaHouse basket/order correlation mismatch

**Affected Features:**
- `rialtoB2A(CASS)TestCase29.feature`

**Affected Scenarios:**
- verify that order arrived in MH from rialto - magazine order original state (`tc_getMHTC_MZN04a`)
- for Magazine change to Uppslag/Spread/Panorama in MH (`tc_patchIntegrationMH_MZN03`)
- verify that order arrived in MH from rialto - magazine order after Uppslag/Spread/Panorama change (`tc_getMHTC_MZN04b`)

**Failure Pattern:**
MediaHouse verification fetched basket `6821`, while Agency had already stored Prisa ID `6841`. Because the MH verification failed before persisting order-line IDs, the later MH patch step aborted with missing `odIds`.

**Evidence:**
- `INTEGRATION MISMATCH: MH basket ID (orBoxid) [6821] does not match Agency Prisa ID [6841]`
- `No MH odIds found in TestContext. Run the MH GET storage step before the patch step.`
- Both MH verification scenarios failed on the same `6821` vs `6841` mismatch.

**Impact:** 3 failures

**Confidence:** High

---

## Rialto order state mismatch after the TC29 flow

**Affected Features:**
- `rialtoB2A(CASS)TestCase29.feature`

**Affected Scenarios:**
- confirms order created in Agency for testcase 29 - after size change (`tc_getIntegrationRialtoMZN04b`)

**Failure Pattern:**
The final Rialto GET did not return the expected reverted full-page state. Placement, pricing, discount, and status fields were all different from the asserted baseline.

**Evidence:**
- `orderAdDetails.placementId expected [[HALVLIGG]] but found [[TEXT]]`
- `orderAdDetails.priceGross expected [[5000.0]] but found [[6000.0]]`
- `discountAmount expected [0.0] but found [3600.0]`
- `orderHeader.statusFlags expected [[]] but found [[PRELIMINARY]]`

**Impact:** 1 failure

**Confidence:** Medium

---

## Affected Components

- `rialtoB2A(CASS)TestCase29.feature`
- MediaHouse basket lookup / Prisa ID correlation step
- MH order-line ID capture used by `tc_patchIntegrationMH_MZN03`
- Rialto order readback validation for `tc_getIntegrationRialtoMZN04b`

---

## Recommended Fix

- Verify that the MH basket lookup for campaign text `TestCase29` returns the basket tied to the Agency Prisa ID before running assertions or storing order-line IDs.
- Investigate why the final Rialto order still carries `TEXT` / discounted / `PRELIMINARY` values instead of the expected full-page baseline.
- Review the revision used by this build (`updated testcase29 data tc_getMHTC_MZN04b`) to confirm whether TC29 expectations or lookup data changed.

---

## Prevention

- Fail fast when `orBoxid` and Agency Prisa ID diverge, and log both IDs before any downstream MH patch step.
- Add a guard that skips or clearly marks dependent MH patch steps when order-line IDs were not captured from the preceding GET.
- Log the effective placement, status, and price values immediately before the final Rialto verification to make state drift easier to diagnose.
