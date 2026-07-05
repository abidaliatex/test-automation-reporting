# Build 269 Root Cause Analysis

Source report: [build-269.md](../../../reports/build-failures/automationrunCAI-RIALTOB2A-IntegrationTesting-Internal-trunk-demo/build-269.md)

## Summary

- Build `automationrunCAI-RIALTOB2A-IntegrationTesting-Internal-trunk-demo` #269 finished `UNSTABLE` with 3 failed checks out of 14.
- All failures belong to `rialtoB2A (CASS TC4 Change Placement)` and occur only in the retrieval assertions after the placement-change flow.
- Jenkins checked out revision `4a04ddba1e4e5809017f1f7cf91b06e93e3c19dd` with commit message `updated api version from 87 to 88`.

## Root Cause

- The failures group into one likely issue: post-update response values no longer match the expected test fixtures after the API v88 change.
- MediaHouse assertions fail on `discountType`, VAT, commission, and total fields, while Rialto assertions fail on `statusFlags`, commission, depth, and derived net values.
- The same three scenario failures and the same checked-out revision were already observed in build #262, which suggests a recurring contract or business-rule drift rather than a one-off infrastructure problem.

## Affected Components

- MediaHouse retrieval checks driven by `MediaHouse\getMHB2A.csv`
- Rialto retrieval checks driven by `Rialto\RialtoB2A\getRialtoB2A.csv`
- Shared soft-assert aggregation in `stepDefinition.ApiStepDefinition.tearDown`

## Recommended Fix

- Reconcile the expected values for `tc_getMHTC03`, `tc_getMHTC03a`, and `tc_getIntegrationRialto05b` against the actual build #269 responses.
- Confirm with the API v88 change whether placement updates are now recalculating discount, commission, VAT, totals, and depth differently; if not, treat this as a service regression.

## Prevention

- Add a focused regression check for placement-change retrieval fields whenever the API version is bumped.
- Review and refresh the placement-change fixture set together with version-upgrade changes so contract drift is caught before merge.
