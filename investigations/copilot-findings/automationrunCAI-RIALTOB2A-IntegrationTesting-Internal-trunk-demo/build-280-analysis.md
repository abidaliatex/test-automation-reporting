# Build 280 Root Cause Analysis

Source report: [build-280.md](../../../reports/build-failures/automationrunCAI-RIALTOB2A-IntegrationTesting-Internal-trunk-demo/build-280.md)

## Summary

- Build `automationrunCAI-RIALTOB2A-IntegrationTesting-Internal-trunk-demo` #280 ended `UNSTABLE` with 3 failures out of 14 tests (78.6% pass rate).
- All failures are in `rialtoB2A (CASS TC4 Change Placement)` and occur during post-placement retrieval validation.
- The same 3 scenarios have been failing since build #246 (`failedSince: 246`), indicating a persistent, ongoing regression.
- Compared to build #271, `tc_getMHTC03` and `tc_getMHTC03a` show identical failure patterns. `tc_getIntegrationRialto05b` shows a changed failure signature: `placementId` and large price/discount mismatches from build #271 are no longer present, but `statusFlags` is now empty (`[]` instead of `[PRELIMINARY]`), `commissionAmount` has dropped to `620.0` (from `3984.47`), and `depth` remains `372` vs expected `184`.

## Root Cause

- **MediaHouse failures (`tc_getMHTC03`, `tc_getMHTC03a`):** The `discountType` field in the MH basket order response does not match the value encoded in `MediaHouse\getMHB2A.csv`. The service returns `null` for the initial placement check and `RIALTO` after the placement change, while the fixtures expect `RIALTO` then `NONE` respectively. All downstream pricing (commission, VAT, basket totals) also deviates, likely because the pricing recalculation is coupled to the discount type being applied. This pattern is unchanged from prior builds.
- **Rialto failure (`tc_getIntegrationRialto05b`):** The order returned by the Rialto GET does not have `statusFlags` set to `PRELIMINARY` after the placement-change PATCH, suggesting the order lifecycle state transition is not completing. Commission calculation is drastically wrong (`620.0` vs `7750.00`), which is consistent with the `depth` still being `372` instead of the expected `184` — indicating the placement-change write is not persisting the new placement dimensions, causing an incorrect size-based pricing calculation.

## Affected Components

- MediaHouse basket order retrieval validation (`MediaHouse\getMHB2A.csv`) — test cases `tc_getMHTC03`, `tc_getMHTC03a`.
- Rialto order retrieval validation (`Rialto\RialtoB2A\getRialtoB2A.csv`) — test case `tc_getIntegrationRialto05b`.
- Shared soft-assert aggregation at `stepDefinition.ApiStepDefinition.tearDown(ApiStepDefinition.java:69)`.

## Recommended Fix

- Investigate why `statusFlags` is empty after the placement-change PATCH — the order state machine may not be transitioning to `PRELIMINARY` when a placement change is applied.
- Confirm whether `depth` is correctly written during the placement-change PATCH; `372` (the original depth) persisting after the change to a new placement suggests the update is silently failing or targeting the wrong record.
- With `depth` incorrect, commission recalculation produces `620.0` instead of `7750.00`; once `depth` is corrected, verify commission and pricing align with fixture expectations.
- The `discountType` inversion in MH (null before change, RIALTO after) is a pre-existing issue — investigate the discount application order in the B2A integration layer.

## Prevention

- Add a post-PATCH assertion on `orderAdDetails[0].depth` and `orderHeader.statusFlags` before proceeding to the GET validation steps to catch placement-write failures earlier in the scenario.
- Gate placement-change flows with a contract test that asserts `depth`, `discountType`, `statusFlags`, and at least one pricing field before merging API version changes.
- Keep fixture CSV values coupled to service contract changes so expectation drift is caught at review time rather than discovered in CI.
