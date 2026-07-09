# Build 273 Root Cause Analysis

Source report: [build-273.md](../../../reports/build-failures/automationrunCAI-RIALTOB2A-IntegrationTesting-Internal-trunk-demo/build-273.md)

## Summary

- Build `automationrunCAI-RIALTOB2A-IntegrationTesting-Internal-trunk-demo` #273 ended `UNSTABLE` with 3 failures out of 14 tests (78.6% pass rate).
- All failures are in `rialtoB2A (CASS TC4 Change Placement)` and occur during post-placement retrieval validation.
- The same 3 scenarios have been failing since build #246 (`failedSince: 246`), indicating persistent fixture drift rather than a newly introduced regression.
- Compared to build #271, `tc_getIntegrationRialto05b` shows a new `statusFlags` failure (`[]` instead of `[PRELIMINARY]`), reduced `commissionAmount` deviation (`620.0` vs `3984.47` previously), and pricing values closer to expected (`priceNet: 249380.0` vs `124546.9` previously) — the service response continues to shift across builds. `tc_getMHTC03a` commission/total mismatches are identical to build #271.

## Root Cause

- **MediaHouse failures (`tc_getMHTC03`, `tc_getMHTC03a`):** The `discountType` field in the MH basket order response does not match the value encoded in `MediaHouse\getMHB2A.csv`. The service returns `null` for the initial placement check and `RIALTO` after the placement change, while fixtures expect `RIALTO` then `NONE` respectively. All downstream pricing (commission, VAT, basket totals) also deviate, likely because recalculation is coupled to the discount type applied. This inversion suggests a discount-application ordering issue in the service.
- **Rialto failure (`tc_getIntegrationRialto05b`):** The placement change is partially applied — `depth` still returns `372` instead of `184`, suggesting placement dimensions are not being updated. `orderHeader.statusFlags` is now empty (not `[PRELIMINARY]`), indicating the order state machine may not be transitioning correctly after the placement update. `commissionAmount` returns `620.0` instead of `7750.00`, and `priceNet` returns `249380.0` instead of `250000.00`. Several fields (`priceGross`, `priceNetExComm`) show only a decimal formatting mismatch (`250000.0` vs `250000.00`), which is a fixture or serialisation issue rather than a logic error.

## Affected Components

- MediaHouse basket order retrieval validation (`MediaHouse\getMHB2A.csv`) — test cases `tc_getMHTC03`, `tc_getMHTC03a`.
- Rialto order retrieval validation (`Rialto\RialtoB2A\getRialtoB2A.csv`) — test case `tc_getIntegrationRialto05b`.
- Shared soft-assert aggregation at `stepDefinition.ApiStepDefinition.tearDown(ApiStepDefinition.java:69)`.

## Recommended Fix

- Investigate why `orderHeader.statusFlags` is empty after the placement update in build #273 (this is a new regression vs #271); check whether the placement-change PATCH step is completing and triggering the correct state transition.
- Confirm whether `commissionAmount: 620.0` reflects an intentional service change or a regression; if intentional, update fixture CSV values accordingly.
- Address decimal serialisation inconsistency: fixture values use `250000.00` while the API returns `250000.0` — align the fixture format or update the assertion to compare numerically.
- If the service `discountType` behaviour is intentional, update `getMHB2A.csv` to reflect the actual post-placement values returned by the current API version.

## Prevention

- Gate placement-change flows with a contract test asserting `statusFlags`, `discountType`, `commissionAmount`, and at least one pricing field before merging API changes.
- Keep fixture CSV values coupled to service contract changes so expectation drift is caught at review time rather than in CI.
- Consider normalising decimal format in the test assertion layer to avoid spurious `250000.00` vs `250000.0` failures.
