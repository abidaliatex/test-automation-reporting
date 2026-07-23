# Root Cause Analysis — Build 304

**Job:** `automationrunCAI-RIALTOB2A-IntegrationTesting-Internal-trunk-demo`  
**Report:** [build-304.md](../../../reports/build-failures/automationrunCAI-RIALTOB2A-IntegrationTesting-Internal-trunk-demo/build-304.md)

---

## Summary

- Build 304 is `UNSTABLE` with 3 failed tests out of 15 (80.0% pass rate).
- All failures are confined to `rialtoB2A(CASS TC29 Magazine (change to Uppslag/Spread/Panorama)`.
- The same failure pattern as builds 301 and 303 persists: MediaHouse and Rialto responses do not match the TC29 expected original-state and reverted full-page values.

---

## Root Cause

1. **TC29 expected original-state dataset does not match returned MediaHouse basket state**
   - `MEDIAHOUSE - Verify original full-page order state in MediaHouse` expects a non-discounted original state (`discountType=RIALTO`, `netPrice=6000.00`), but MediaHouse returns `discountType=null` and discounted totals (`netPrice=2400.00`, `totalInclVat=2907.00`).

2. **Later TC29 assertions still expect reverted full-page values while both systems remain in `UPPSLAG`/spread state**
   - `MEDIAHOUSE - Verify updated MediaHouse basket state` and `RIALTO - Verify Rialto reflects the reverted full-page state` both expect `HALVLIGG`/full-page values (`width=1`, `depth=146`, `priceGross=5000.0`), but responses retain `UPPSLAG` placement, wider dimensions (`width=2`, `depth=297`), and `11000` gross pricing.

This recurring pattern across multiple consecutive builds points to stale TC29 expectation data or an incorrect assumption about the order state transitions rather than a transient environment issue.

---

## Affected Components

- Feature flow: `rialtoB2A(CASS TC29 Magazine (change to Uppslag/Spread/Panorama)`
- MediaHouse validation data: `MediaHouse/getMHB2A.csv` (`tc_getMHTC_MZN04a`, `tc_getMHTC_MZN04b`)
- Rialto validation data: `Rialto/RialtoB2A/getRialtoB2A.csv` (`tc_getIntegrationRialtoMZN04b`)

---

## Recommended Fix

- Reconcile TC29 expected datasets with current service behavior for `discountType`, placement (`HALVLIGG` vs `UPPSLAG`), dimensions, and gross/net totals.
- Confirm whether the flow should revert to the original full-page state after the size change; if not, update the reverted-state assertions to reflect the actual end state.

---

## Prevention

- Add a checkpoint after each TC29 state transition so placement and pricing drift is detected before later validations fail across systems.
- Re-verify TC29 expectation rows whenever test setup or downstream pricing rules change.
