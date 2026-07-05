# Build 263 Root Cause Analysis

Source report: [build-263.md](../../../reports/build-failures/automationrunCAI-RIALTOB2A-IntegrationTesting-Internal-trunk-demo/build-263.md)

## Summary

- Build `automationrunCAI-RIALTOB2A-IntegrationTesting-Internal-trunk-demo` #263 finished `UNSTABLE` with 3 failures out of 14 tests.
- All failed scenarios belong to `rialtoB2A (CASS TC4 Change Placement)` and occur on post-update retrieval assertions.
- Jenkins checked out revision `4a04ddba1e4e5809017f1f7cf91b06e93e3c19dd` with commit message `updated api version from 87 to 88`.

## Root Cause

- Failure signatures indicate response-contract drift in pricing/discount and placement fields after the placement-change flow.
- Two failures hit MediaHouse retrieval checks (`tc_getMHTC03`, `tc_getMHTC03a`) and one hits Rialto retrieval (`tc_getIntegrationRialto05b`), but all three show mismatched expected vs actual monetary/placement values.
- This is likely either a behavior change from API v88 or outdated expected fixtures for the same workflow.

## Affected Components

- MediaHouse retrieval validations sourced by `MediaHouse/getMHB2A.csv`
- Rialto retrieval validations sourced by `Rialto/RialtoB2A/getRialtoB2A.csv`
- Assertion aggregation at `stepDefinition.ApiStepDefinition.tearDown`

## Recommended Fix

- Validate intended API v88 behavior for `discountType`, commission, totalInclVat, placementId, and depth in this placement-change scenario.
- If behavior is intentional, update expected values for `tc_getMHTC03`, `tc_getMHTC03a`, and `tc_getIntegrationRialto05b`; otherwise treat as regression in service recalculation.

## Prevention

- Add a narrow contract check for post-placement-change pricing/placement fields whenever API version is bumped.
- Include fixture-vs-response diff review for these three scenarios in version-upgrade PR validation.
