# Build 262 Root Cause Analysis

Source report: [build-262.md](../../../reports/build-failures/automationrunCAI-RIALTOB2A-IntegrationTesting-Internal-trunk-demo/build-262.md)

## Summary

- Build `automationrunCAI-RIALTOB2A-IntegrationTesting-Internal-trunk-demo` #262 finished `UNSTABLE` with 3 failed checks out of 14.
- All failures belong to `rialtoB2A (CASS TC4 Change Placement)` and occur in post-change retrieval assertions.
- The checked-out revision was `4a04ddba1e4e5809017f1f7cf91b06e93e3c19dd` with commit message `updated api version from 87 to 88`.

## Root Cause

- The evidence points to a likely response-contract drift in the placement-change flow after the API version bump.
- Two failures are on MediaHouse GET validation and one is on Rialto GET validation, but all three assert mismatched pricing/discount-related fields after the same scenario flow.
- The repeated mismatches on `discountType`, commission, VAT, totals, status flags, and depth suggest the expected fixtures no longer align with the runtime payloads, or the service is recalculating those fields differently.

## Affected Components

- MediaHouse retrieval checks driven by `getMHB2A.csv`
- Rialto retrieval checks driven by `getRialtoB2A.csv`
- Shared soft-assert aggregation in `stepDefinition.ApiStepDefinition.tearDown`

## Recommended Fix

- Compare the build #262 response payloads with the expected values for `tc_getMHTC03`, `tc_getMHTC03a`, and `tc_getIntegrationRialto05b`.
- Confirm whether API v88 changed discount/commission semantics for placement updates; if yes, update the test expectations, otherwise investigate the service regression.

## Prevention

- Add a focused contract-smoke check for placement-change pricing fields when the API version is bumped.
- Keep a small fixture diff review for `discountType`, commission, VAT, totals, and depth before merging version-upgrade changes.
