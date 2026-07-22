# Root Cause Analysis — Build 300

**Job:** `automationrunCAI-RIALTOB2A-IntegrationTesting-Internal-trunk-demo`  
**Report:** [build-300.md](../../../reports/build-failures/automationrunCAI-RIALTOB2A-IntegrationTesting-Internal-trunk-demo/build-300.md)

---

## Summary

- Build 300 is `UNSTABLE` with 4 failed tests out of 15 (73.3% pass rate).
- All failures are confined to `rialtoB2A(CASS)TestCase29.feature`.
- The failures split into one initial Rialto assertion-shape mismatch and a broader placement/pricing mismatch visible in later MediaHouse and Rialto validations.

---

## Root Cause

1. **Initial Rialto verification compares list-wrapped expected values to scalar response fields**
   - `tc_getIntegrationRialtoMZN04a` fails on `discountAmount` and `priceGross` even though the numeric values align (`3600.0`, `6000.0`).
   - The evidence suggests the expected dataset and actual response differ in value shape rather than amount.

2. **TC29 size-change/revert flow is not matching expected full-page state across downstream validations**
   - `tc_getMHTC_MZN04a` fails because MediaHouse returns `discountType=null` and discounted totals where the test expects the original full-page state.
   - `tc_getMHTC_MZN04b` and `tc_getIntegrationRialtoMZN04b` both return `UPPSLAG` placement/dimensions and `11000` pricing where the assertions expect `HALVLIGG` / `5000` reverted values.
   - This indicates the later flow state in MediaHouse and Rialto does not align with the expected TC29 baseline/revert data.

---

## Affected Components

- Feature flow: `rialtoB2A(CASS)TestCase29.feature`
- Rialto GET validation data: `Rialto/RialtoB2A/getRialtoB2A.csv` (`tc_getIntegrationRialtoMZN04a`, `tc_getIntegrationRialtoMZN04b`)
- MediaHouse GET validation data: `MediaHouse/getMHB2A.csv` (`tc_getMHTC_MZN04a`, `tc_getMHTC_MZN04b`)

---

## Recommended Fix

- Normalize the expected-vs-actual comparison for `discountAmount` and `priceGross` in `tc_getIntegrationRialtoMZN04a`, or correct the expected value shape in the test data.
- Re-check the expected TC29 MediaHouse and Rialto datasets for the size-change/revert flow against current service behavior, especially `discountType`, placement (`HALVLIGG` vs `UPPSLAG`), dimensions, and gross/net totals.

---

## Prevention

- Add a targeted checkpoint after the initial Rialto verification to catch value-shape mismatches before the remainder of the flow runs.
- Validate the expected placement/pricing state immediately after each TC29 transition so baseline, updated, and reverted assertions stay aligned with the intended flow.
