# Root Cause Analysis — Build 320

**Source Report:** [build-320.md](../../../reports/build-failures/automationrunCAI-RIALTOB2A-IntegrationTesting-Internal-trunk-demo/build-320.md)

---

## Build Summary

Build: 320
Total Tests: 16
Passed: 12
Failed: 4
Pass Rate: 75%

---

## Root Cause Groups

## MediaHouse basket lookup returned a different order than the Agency order

**Affected Features:**
- `rialtoB2A(CASS)TestCase29.feature`

**Affected Scenarios:**
- MEDIAHOUSE - Verify original full-page order state in MediaHouse - #1.1 (`tc_getMHTC_MZN04a`)
- MEDIAHOUSE - Verify updated MediaHouse basket state - #1.1 (`tc_getMHTC_MZN04b`)

**Failure Pattern:**
`MH basket ID (orBoxid) [6863] does not match Agency Prisa ID [6869]`

**Evidence:**
- `INTEGRATION MISMATCH: MH basket ID (orBoxid) [6863] does not match Agency Prisa ID [6869]`
- The same mismatch appears in both MediaHouse verification reads, so the flow is likely bound to the wrong MH basket for this Agency order

**Impact:** 2 failures

**Confidence:** High

---

## Missing MH order-line IDs caused the update flow to abort and left Rialto in the pre-update state

**Affected Features:**
- `rialtoB2A(CASS)TestCase29.feature`

**Affected Scenarios:**
- MEDIAHOUSE - Update two MediaHouse order lines to uppslag - #1.1 (`tc_patchIntegrationMH_MZN03`)
- RIALTO - Verify Rialto reflects the reverted full-page state - #1.1 (`tc_getIntegrationRialtoMZN04b`)

**Failure Pattern:**
`No MH odIds found in TestContext` followed by Rialto returning the original `TEXT` order values instead of the expected `UPPSLAG` values

**Evidence:**
- `No MH odIds found in TestContext. Run the MH GET storage step before the patch step.`
- `orderAdDetails.placementId expected [[UPPSLAG]] but found [[TEXT]]`
- Rialto also kept the original-state dimensions and prices: columns `1`, width `230`, `priceGross` `6000.0`

**Impact:** 2 failures

**Confidence:** High

---

## Summary

- Build `automationrunCAI-RIALTOB2A-IntegrationTesting-Internal-trunk-demo` #320 finished `UNSTABLE` with 4 failed tests out of 16.
- The first failure is a direct cross-system ID mismatch: MediaHouse basket `6863` does not match Agency Prisa ID `6869`.
- The later patch and Rialto verification failures are downstream effects after MH order-line IDs were never stored.

## Root Cause

- Primary issue: the TC29 MediaHouse lookup appears to resolve a basket that does not belong to the Agency order created earlier in the flow.
- Downstream issue: because the first MH verification did not complete the expected storage step, the patch flow had no `odIds`, and the final Rialto readback stayed on the original `TEXT` state.

## Affected Components

- `rialtoB2A(CASS)TestCase29.feature`
- MediaHouse basket lookup / verification steps for `tc_getMHTC_MZN04a` and `tc_getMHTC_MZN04b`
- MediaHouse patch step `tc_patchIntegrationMH_MZN03`
- Rialto verification step `tc_getIntegrationRialtoMZN04b`

## Recommended Fix

- Verify the campaign-text-to-basket lookup returns the MediaHouse basket for the same Agency Prisa ID created earlier in TC29.
- Add a guard immediately after the MH lookup/read step so the scenario stops before patching when the wrong basket or missing `odIds` are detected.

## Prevention

- Add an explicit cross-check that the fetched MH basket ID maps to the Agency Prisa ID before storing order-line IDs.
- Record the stored `odIds` after the first MH verification so missing context is visible before the patch step runs.
