# Build 267 Root Cause Analysis

Source report: [build-267.md](../../../reports/build-failures/automationrunCAI-RIALTOB2A-IntegrationTesting-Internal-trunk-demo/build-267.md)

## Summary

- Build `automationrunCAI-RIALTOB2A-IntegrationTesting-Internal-trunk-demo` #267 finished `UNSTABLE` with 3 failed checks out of 14.
- All failures are in `rialtoB2A (CASS TC4 Change Placement)` and occur in post-change retrieval assertions, identical in character to failures first recorded at build #246.
- The failures are persistent across builds 246–267 with no regression fix applied.

## Root Cause

- All three failures stem from the placement-change flow producing pricing, discount, and structural values that no longer match the test fixtures in `getMHB2A.csv` and `getRialtoB2A.csv`.
- `tc_getMHTC03`: `discountType` is `null` where `RIALTO` is expected, and VAT/total values are higher than expected — possibly the service is omitting the discount on the initial GET after the placement flow.
- `tc_getMHTC03a`: `discountType` is `RIALTO` where `NONE` is expected after the change, and commission/sum values differ by ~250 units — the placement-change event may not be resetting the discount type.
- `tc_getIntegrationRialto05b`: `depth` is doubled (372 vs 184), commission is a fraction of expected (620.0 vs 7750.00), and `statusFlags` is empty — the Rialto order-update handler may not be recalculating ad details after placement change.
- All three cases share the same soft-assert aggregation path (`ApiStepDefinition.tearDown`), confirming they are assertion failures rather than connectivity or setup issues.

## Affected Components

- MediaHouse order retrieval (`getMHB2A.csv`) — `tc_getMHTC03`, `tc_getMHTC03a`
- Rialto order retrieval (`getRialtoB2A.csv`) — `tc_getIntegrationRialto05b`
- Shared soft-assert teardown in `stepDefinition.ApiStepDefinition.tearDown`

## Recommended Fix

- Capture actual response payloads for the three failing test cases and compare field-by-field against the CSV fixtures.
- Determine whether the fixture values need to be updated (if service behaviour is intentionally changed) or whether the service has a regression to fix.
- Pay particular attention to `discountType` propagation and `commissionAmount` recalculation logic in the placement-change handler.

## Prevention

- Add a contract-change gate that flags when `discountType`, commission, or pricing fields deviate between API version bumps.
- Introduce a short-lived canary check on placement-change pricing fields so regression is caught in the same build that introduces the change.
