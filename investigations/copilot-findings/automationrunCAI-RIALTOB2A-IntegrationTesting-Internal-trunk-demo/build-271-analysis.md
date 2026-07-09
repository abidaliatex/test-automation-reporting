# Build 271 Root Cause Analysis

Source report: [build-271.md](../../../reports/build-failures/automationrunCAI-RIALTOB2A-IntegrationTesting-Internal-trunk-demo/build-271.md)

## Summary

- Build `automationrunCAI-RIALTOB2A-IntegrationTesting-Internal-trunk-demo` #271 ended `UNSTABLE` with 3 failures out of 14 tests (78.6% pass rate).
- All failed checks are in `rialtoB2A (CASS TC4 Change Placement)` and occur during post-placement retrieval validation.
- The same 3 scenarios have been failing since build #246 (`failedSince: 246`), indicating a persistent fixture drift rather than a newly introduced regression.
- Compared to build #270, `tc_getMHTC03a` shows different actual commission/sum/total values (12500.00 vs previously 8000.00), and `tc_getIntegrationRialto05b` now includes additional failures on `placementId` (returned `TEXT` instead of `SIDAN3`), `discountAmount`, `priceGross`, and `priceNetExComm` — suggesting the service response continues to diverge from pinned fixture expectations.

## Root Cause

- **MediaHouse failures (`tc_getMHTC03`, `tc_getMHTC03a`):** The `discountType` field in the MH basket order response does not match the value encoded in `MediaHouse\getMHB2A.csv`. The service is returning `null` for the initial placement check and `RIALTO` after the placement change, while the fixtures expect `RIALTO` then `NONE` respectively. All downstream pricing (commission, VAT, basket totals) also deviate, possibly because recalculation is coupled to the discount type applied.
- **Rialto failure (`tc_getIntegrationRialto05b`):** The placement change is not being applied as expected — `placementId` returned `TEXT` instead of `SIDAN3`, and `depth` returned `372` instead of `184`. This placement ID and dimension mismatch causes the full pricing chain (`priceGross`, `discountAmount`, `commissionAmount`, `priceNetExComm`, `priceNet`) to differ significantly from fixture values. This may indicate the placement-change write path is not persisting the new placement correctly, or the GET is resolving from a different state.

## Affected Components

- MediaHouse basket order retrieval validation (`MediaHouse\getMHB2A.csv`) — test cases `tc_getMHTC03`, `tc_getMHTC03a`.
- Rialto order retrieval validation (`Rialto\RialtoB2A\getRialtoB2A.csv`) — test case `tc_getIntegrationRialto05b`.
- Shared soft-assert aggregation at `stepDefinition.ApiStepDefinition.tearDown(ApiStepDefinition.java:69)`.

## Recommended Fix

- Confirm whether the placement-change PATCH in `tc_patchIntegrationMH03` is completing successfully and that the resulting state in Rialto reflects `placementId=SIDAN3`; if not, the placement-change write path may be broken.
- If the service behavior is intentionally different, update `getMHB2A.csv` and `getRialtoB2A.csv` with the actual post-placement values returned by the current API version.
- Investigate why `discountType` is `null` in `tc_getMHTC03` (pre-change) and incorrectly `RIALTO` in `tc_getMHTC03a` (post-change) — this inversion suggests a discount-application ordering issue in the service.

## Prevention

- Gate placement-change flows with a contract test that asserts `placementId`, `depth`, `discountType`, and at least one pricing field before merging API version bumps.
- Keep fixture CSV values coupled to service contract changes so expectation drift is caught at review time rather than discovered in CI.
