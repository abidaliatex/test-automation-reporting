# Build 284 Root Cause Analysis

Source report: [build-284.md](../../../reports/build-failures/automationrunCAI-RIALTOB2A-IntegrationTesting-Internal-trunk-demo/build-284.md)

## Summary

- Build `automationrunCAI-RIALTOB2A-IntegrationTesting-Internal-trunk-demo` #284 ended `UNSTABLE` with 3 failures out of 14 tests (78.6% pass rate).
- All failed checks are in `rialtoB2A (CASS TC4 Change Placement)` and occur during post-placement retrieval validation.
- The same 3 scenarios have been failing since build #246 (`failedSince: 246`), indicating a persistent fixture drift rather than a newly introduced regression.
- Compared to build #271, `tc_getMHTC03` and `tc_getMHTC03a` show identical MH pricing and discountType mismatches. `tc_getIntegrationRialto05b` shows a partially changed pattern: the `placementId` field no longer mismatches, but `depth` (372 vs 184) remains wrong, `statusFlags` is now empty instead of `[PRELIMINARY]`, and `commissionAmount` has shifted from `3984.47` to `620.0` — indicating ongoing drift in the Rialto order state.

## Root Cause

- **MediaHouse failures (`tc_getMHTC03`, `tc_getMHTC03a`):** The `discountType` field in the MH basket order response does not match the value encoded in `MediaHouse\getMHB2A.csv`. The service returns `null` for the initial placement check and `RIALTO` after the placement change, while fixtures expect `RIALTO` then `NONE` respectively. All downstream pricing (commission, VAT, basket totals) also deviates, consistent with prior builds — suggesting discount application ordering in the service remains broken and unfixed since build #246.
- **Rialto failure (`tc_getIntegrationRialto05b`):** The placement change is not being applied correctly — `depth` returned `372` instead of `184`, confirming the placement dimension update is not persisting. `orderHeader.statusFlags` is empty (missing `PRELIMINARY`), indicating the order has not reached the expected workflow state. `commissionAmount` is `620.0` vs the expected `7750.00`, pointing to a commission calculation fault. Decimal precision mismatches (`250000.0` vs `250000.00`) are a minor serialization issue layered on top of the substantive failures.

## Affected Components

- MediaHouse basket order retrieval validation (`MediaHouse\getMHB2A.csv`) — test cases `tc_getMHTC03`, `tc_getMHTC03a`.
- Rialto order retrieval validation (`Rialto\RialtoB2A\getRialtoB2A.csv`) — test case `tc_getIntegrationRialto05b`.
- Shared soft-assert aggregation at `stepDefinition.ApiStepDefinition.tearDown(ApiStepDefinition.java:69)`.

## Recommended Fix

- Investigate why `discountType` is still `null` in `tc_getMHTC03` (pre-change) and incorrectly `RIALTO` in `tc_getMHTC03a` (post-change); this inversion has persisted since build #246 and has not been addressed.
- Confirm the placement-change PATCH in `tc_patchIntegrationMH03` is completing successfully and that `depth` is updated to `184` in Rialto; if not, the placement-change write path is not persisting the updated dimension.
- Investigate why `orderHeader.statusFlags` is empty — the order may be failing to transition to `PRELIMINARY` state after the placement update.
- Verify commission calculation: actual `620.0` vs expected `7750.00` represents a significant discrepancy; check if the commission rate or base amount has changed in the service.

## Prevention

- Gate placement-change flows with a contract test asserting `depth`, `discountType`, `statusFlags`, and `commissionAmount` before merging API version changes.
- Keep fixture CSV values coupled to service contract changes so expectation drift is caught at review time rather than discovered in CI.
- Address the `failedSince: 246` backlog — these scenarios have been failing for 38+ builds without resolution.
