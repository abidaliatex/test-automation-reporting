# Build 270 Root Cause Analysis

Source report: [build-270.md](../../../reports/build-failures/automationrunCAI-RIALTOB2A-IntegrationTesting-Internal-trunk-demo/build-270.md)

## Summary

- Build `automationrunCAI-RIALTOB2A-IntegrationTesting-Internal-trunk-demo` #270 ended `UNSTABLE` with 3 failures out of 14 tests.
- All failed checks are in `rialtoB2A (CASS TC4 Change Placement)` and occur during post-placement retrieval validation.
- Jenkins checked out revision `4a04ddba1e4e5809017f1f7cf91b06e93e3c19dd` with commit message `updated api version from 87 to 88`.

## Root Cause

- The failures group into a single likely cause: expected fixture values for placement-change retrieval no longer match service response values after the API version update.
- MediaHouse failures show changed discount/commission/VAT/total values.
- Rialto failure shows changed status flag, depth, and commission/net values.

## Affected Components

- MediaHouse retrieval validation (`MediaHouse\getMHB2A.csv`) for `tc_getMHTC03` and `tc_getMHTC03a`.
- Rialto retrieval validation (`Rialto\RialtoB2A\getRialtoB2A.csv`) for `tc_getIntegrationRialto05b`.
- Shared soft-assert aggregation at `stepDefinition.ApiStepDefinition.tearDown`.

## Recommended Fix

- Validate whether API v88 changed placement recalculation behavior; if expected, update retrieval fixtures for affected test cases.
- If behavior was not intended, treat as regression and restore previous discount/commission/status/depth outputs.

## Prevention

- Gate API-version bumps with focused regression checks for placement-change retrieval fields.
- Keep fixture updates coupled with contract/version changes so expectation drift is caught before merge.
