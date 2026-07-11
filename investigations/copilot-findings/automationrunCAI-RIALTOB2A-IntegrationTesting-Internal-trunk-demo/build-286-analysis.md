# Build 286 Root Cause Analysis

Source report: [build-286.md](../../../reports/build-failures/automationrunCAI-RIALTOB2A-IntegrationTesting-Internal-trunk-demo/build-286.md)

## Summary

- Build `automationrunCAI-RIALTOB2A-IntegrationTesting-Internal-trunk-demo` #286 ended `UNSTABLE`.
- Test result: 11 passed, 3 failed (14 total).
- Failures split into two groups: MediaHouse discount/pricing drift and Rialto post-update state/pricing drift.

## Root Cause

- **MediaHouse retrieval drift (`tc_getMHTC03`, `tc_getMHTC03a`)**: the returned `discountType`, commission, VAT, and total values do not match the scenario expectations, indicating the placement change is producing different downstream pricing/discount data in MediaHouse.
- **Rialto post-update drift (`tc_getIntegrationRialto05b`)**: the follow-up Rialto GET response contains unexpected `statusFlags`, `depth`, and pricing values, indicating the placement update is not reflected as expected in Rialto.
- The build ran commit `4a04ddba1e4e5809017f1f7cf91b06e93e3c19dd` (`updated api version from 87 to 88`), which may be related because all failures are value mismatches rather than transport or availability errors.

## Affected Components

- `rialtoB2A(CASS)TestCase4.feature`
- Scenario fixtures referenced by:
  - `MediaHouse\getMHB2A.csv` (`tc_getMHTC03`, `tc_getMHTC03a`)
  - `Rialto\RialtoB2A\getRialtoB2A.csv` (`tc_getIntegrationRialto05b`)
- Assertion aggregation point: `stepDefinition.ApiStepDefinition.tearDown(ApiStepDefinition.java:69)`

## Recommended Fix

- Verify the expected discount mapping and basket total calculation for the MediaHouse GET assertions after a placement change.
- Verify that the placement update is fully persisted before the final Rialto GET validation runs.
- Confirm whether API version 88 intentionally changed these fields before updating test fixtures.

## Prevention

- Add a focused contract check for `discountType`, `statusFlags`, `depth`, commission, and total fields in this placement-change flow.
- Capture and compare the immediate post-update payload before downstream GET assertions to isolate whether the drift starts in Rialto or MediaHouse.
