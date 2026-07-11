# Build 287 Root Cause Analysis

Source report: [build-287.md](../../../reports/build-failures/automationrunCAI-RIALTOB2A-IntegrationTesting-Internal-trunk-demo/build-287.md)

## Summary

- Build `automationrunCAI-RIALTOB2A-IntegrationTesting-Internal-trunk-demo` #287 ended `UNSTABLE`.
- Test result: 11 passed, 3 failed (14 total).
- All 3 failures are persistent (failedSince: build 246, age: 42 builds) — the same test cases have been failing continuously since build 246.
- Failures split into two groups: MediaHouse discount/pricing drift and Rialto post-update state/pricing drift.

## Root Cause

- **MediaHouse retrieval drift (`tc_getMHTC03`, `tc_getMHTC03a`)**: `discountType`, commission, VAT, and basket total values do not match test expectations, indicating the placement change flow produces incorrect downstream pricing/discount data in MediaHouse.
- **Rialto post-update drift (`tc_getIntegrationRialto05b`)**: the follow-up Rialto GET response contains unexpected `statusFlags` (empty instead of `[PRELIMINARY]`), wrong `depth` (`372` vs `184`), and incorrect commission/pricing values, indicating the placement update is not reflected as expected in Rialto.
- The persistent failure age (42 builds since #246) suggests a regression introduced around build 246 that has not been addressed in test fixtures or application behaviour.

## Affected Components

- `rialtoB2A(CASS)TestCase4.feature`
- Scenario fixtures referenced by:
  - `MediaHouse\getMHB2A.csv` (`tc_getMHTC03`, `tc_getMHTC03a`)
  - `Rialto\RialtoB2A\getRialtoB2A.csv` (`tc_getIntegrationRialto05b`)
- Assertion aggregation point: `stepDefinition.ApiStepDefinition.tearDown(ApiStepDefinition.java:69)`

## Recommended Fix

- Investigate the regression introduced around build 246 that caused `discountType`, `statusFlags`, commission, and pricing fields to diverge from expected values.
- Verify whether API or business logic changes since build 246 intentionally altered these fields; if so, update test fixtures accordingly.
- Confirm placement update is fully persisted before the Rialto GET validation step runs.

## Prevention

- Add a focused contract check for `discountType`, `statusFlags`, `depth`, commission, and total fields in the placement-change flow.
- Introduce a build gate to flag tests failing for more than a defined threshold (e.g. 5 consecutive builds) to prevent long-running silent regressions.
