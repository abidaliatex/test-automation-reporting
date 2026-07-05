# Build 267 Root Cause Analysis

Source report: [build-267.md](../../../reports/build-failures/automationrunCAI-RIALTOB2A-IntegrationTesting-Internal-trunk-demo/build-267.md)

## Summary

- Build `automationrunCAI-RIALTOB2A-IntegrationTesting-Internal-trunk-demo` #267 finished `UNSTABLE` with 3 failed checks out of 14.
- All failures belong to `rialtoB2A (CASS TC4 Change Placement)` and occur in post-change retrieval assertions.
- These same 3 tests have been failing continuously since build #246 (age: 22 builds).
- Several previously-failing tests (tc_postRialtoB2A01, tc_postIntegrationRialtoE2E03, tc_patchIntegrationMH03) are now `FIXED` in this build.

## Root Cause

- All three failures assert mismatched pricing, discount, and structural fields in the MH and Rialto GET responses after the CASS TC4 placement-change flow.
- The `failedSince: 246` marker confirms this is a persistent regression, not a flap — the expected test fixtures have not been updated to match the current API behaviour since the v88 API upgrade.
- `tc_getMHTC03`: `discountType` remains `null` instead of `RIALTO`, suggesting the discount is not being applied to the order in MH after initial creation.
- `tc_getMHTC03a`: `discountType` reads `RIALTO` instead of `NONE` after the placement change, and commission/totals diverge — the placement-change event is not resetting the discount type.
- `tc_getIntegrationRialto05b`: `statusFlags` is empty, `depth` is doubled (`372` vs `184`), and commission is drastically lower (`620.0` vs `7750.00`), pointing to a placement-update recalculation defect in the Rialto service.

## Affected Components

- MediaHouse retrieval checks driven by `getMHB2A.csv` (`tc_getMHTC03`, `tc_getMHTC03a`)
- Rialto retrieval checks driven by `getRialtoB2A.csv` (`tc_getIntegrationRialto05b`)
- Shared soft-assert aggregation in `stepDefinition.ApiStepDefinition.tearDown`

## Recommended Fix

- Confirm whether API v88 changed discount/commission semantics for placement updates; if yes, update the test expected values in `getMHB2A.csv` and `getRialtoB2A.csv`.
- If the values reflect a service regression, raise a defect against the Rialto placement-change recalculation logic.

## Prevention

- Enforce expected-value review as part of API version-bump PRs for placement-change-related CSV fixtures.
- Add a post-placement-change smoke assertion for `discountType` and `commissionAmount` to catch similar drift early.
