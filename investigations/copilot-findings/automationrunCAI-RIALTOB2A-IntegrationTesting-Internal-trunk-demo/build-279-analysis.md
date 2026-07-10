# Build 279 Root Cause Analysis

Source report: [build-279.md](../../../reports/build-failures/automationrunCAI-RIALTOB2A-IntegrationTesting-Internal-trunk-demo/build-279.md)

## Summary

- Build `automationrunCAI-RIALTOB2A-IntegrationTesting-Internal-trunk-demo` #279 ended `UNSTABLE` with 3 failures out of 14 tests (78.6% pass rate).
- All failures are in the `rialtoB2A (CASS TC4 Change Placement)` flow and occur in post-placement retrieval assertions.
- The failed scenarios (`tc_getMHTC03`, `tc_getMHTC03a`, `tc_getIntegrationRialto05b`) show response-vs-fixture mismatches rather than transport/status-code failures.

## Root Cause

- **MediaHouse retrieval assertions (`tc_getMHTC03`, `tc_getMHTC03a`)**: response discount and pricing fields diverge from expected fixture values (`discountType`, commission, VAT, total values), causing grouped soft-assert failures.
- **Rialto retrieval assertion (`tc_getIntegrationRialto05b`)**: order-state and pricing contract fields differ from expected values (`statusFlags`, `depth`, `commissionAmount`, net totals), indicating mismatch between expected post-change state and returned payload.

## Affected Components

- MediaHouse response validation fixture path: `MediaHouse\getMHB2A.csv` (as referenced by failing scenarios).
- Rialto response validation fixture path: `Rialto\RialtoB2A\getRialtoB2A.csv` (as referenced by failing scenario).
- Shared assertion aggregation: `stepDefinition.ApiStepDefinition.tearDown(ApiStepDefinition.java:69)`.

## Recommended Fix

- Verify whether expected fixture values for `discountType`, commission, VAT, and totals still match current API behavior for the placement-change flow.
- Re-check post-change state propagation in the placement workflow before GET validation, especially fields used by `tc_getIntegrationRialto05b` (`statusFlags`, `depth`, pricing totals).
- Align either service response contract or fixture expectations so the same canonical values are used in both MH and Rialto validation stages.

## Prevention

- Add/retain contract checks for key post-placement fields (`discountType`, `statusFlags`, `depth`, commission, VAT, totals) before full scenario assertions execute.
- Review fixture update process whenever API calculation or state-propagation logic changes in placement workflows.
