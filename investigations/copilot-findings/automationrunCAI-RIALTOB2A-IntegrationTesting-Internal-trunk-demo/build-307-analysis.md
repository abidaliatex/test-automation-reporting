# Root Cause Analysis — Build 307

**Job:** `automationrunCAI-RIALTOB2A-IntegrationTesting-Internal-trunk-demo`  
**Report:** [build-307.md](../../../reports/build-failures/automationrunCAI-RIALTOB2A-IntegrationTesting-Internal-trunk-demo/build-307.md)

---

## Summary

- Build 307 is `UNSTABLE` with 3 failed tests out of 15 (80.0% pass rate).
- All failures are in the TC29 magazine change flow and have persisted since build 298.
- Failures group into one original-state mismatch and one spread-state pricing/placement mismatch across MediaHouse and Rialto checks.

---

## Root Cause

1. **Original-state check expects discount metadata that is not present in response**
   - MediaHouse original-state validation expects `orders.printDetails.discountType=RIALTO` but response returns `null`.

2. **State-transition expectations for reverted/full-page values do not match returned spread-state data**
   - Both MediaHouse and Rialto validations expect `HALVLIGG`/full-page dimensions and 5000-range amounts.
   - Actual responses return `UPPSLAG`/spread dimensions and 11000-range amounts.

---

## Affected Components

- Feature flow: `rialtoB2A(CASS TC29 Magazine (change to Uppslag/Spread/Panorama)`
- MediaHouse validations: `tc_getMHTC_MZN04a`, `tc_getMHTC_MZN04b`
- Rialto validation: `tc_getIntegrationRialtoMZN04b`

---

## Recommended Fix

- Align TC29 expected assertion data with current response contract for `discountType`, placement, dimensions, and price totals.
- Re-check whether the scenario is expected to revert to full-page values; if not, update reverted-state assertions accordingly.

---

## Prevention

- Add a verification checkpoint immediately after each TC29 state transition to confirm expected placement/price state before downstream assertions.
- Rebaseline TC29 expected datasets whenever pricing/placement rules are updated.
