# Root Cause Analysis — Build 301

**Job:** `automationrunCAI-RIALTOB2A-IntegrationTesting-Internal-trunk-demo`  
**Report:** [build-301.md](../../../reports/build-failures/automationrunCAI-RIALTOB2A-IntegrationTesting-Internal-trunk-demo/build-301.md)

---

## Summary

- Build 301 is `UNSTABLE` with 3 failed tests out of 15 (80.0% pass rate).
- All failures are confined to `rialtoB2A(CASS)TestCase29.feature`.
- The initial Rialto created-order check is marked `FIXED` in this run; the remaining failures begin at MediaHouse original-state verification and continue through the later MediaHouse and Rialto readbacks.

---

## Root Cause

1. **The TC29 expected original-state dataset no longer matches the returned MediaHouse basket state**
   - `tc_getMHTC_MZN04a` expects a non-discounted original state, but MediaHouse returns `discountType=null` and discounted totals (`2400.00` net / `2907.00` incl. VAT).

2. **Later TC29 assertions still expect reverted full-page values while both systems remain in `UPPSLAG`/spread state**
   - `tc_getMHTC_MZN04b` and `tc_getIntegrationRialtoMZN04b` both expect `HALVLIGG`/full-page values, but the responses keep `UPPSLAG` placement, wider dimensions, and `11000` gross pricing.

This points to stale TC29 expectation data or an incorrect assumption about the final state transition, rather than the missing-path-parameter/context issue seen in build 299.

---

## Affected Components

- Feature flow: `rialtoB2A(CASS)TestCase29.feature`
- MediaHouse validation data: `MediaHouse/getMHB2A.csv` (`tc_getMHTC_MZN04a`, `tc_getMHTC_MZN04b`)
- Rialto validation data: `Rialto/RialtoB2A/getRialtoB2A.csv` (`tc_getIntegrationRialtoMZN04b`)

---

## Recommended Fix

- Reconcile the TC29 MediaHouse and Rialto expected datasets with current service behavior for `discountType`, placement (`HALVLIGG` vs `UPPSLAG`), dimensions, and gross/net totals.
- Confirm whether the flow should revert to the original full-page state after the size change; if not, update the reverted-state assertions to the intended end state.

---

## Prevention

- Add a checkpoint after each TC29 state transition so placement and pricing drift is detected before later validations fail in multiple systems.
- Re-verify the shared TC29 expectation rows whenever the test setup or downstream pricing rules change.
