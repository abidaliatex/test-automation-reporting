# Build 278 Root Cause Analysis

Source report: [build-278.md](../../../reports/build-failures/automationrunCAI-RIALTOB2A-IntegrationTesting-Internal-trunk-demo/build-278.md)

## Summary

- Build `automationrunCAI-RIALTOB2A-IntegrationTesting-Internal-trunk-demo` #278 ended `UNSTABLE` with 3 failures out of 14 tests (78.6% pass rate).
- All failures are in `rialtoB2A (CASS TC4 Change Placement)` and occur during post-placement retrieval validation.
- All 3 scenarios have been failing continuously since build #246 (`failedSince: 246`), indicating a persistent fixture drift rather than a newly introduced regression.
- Compared to build #271, `tc_getIntegrationRialto05b` now shows different failure details: `statusFlags` is empty `[]` instead of `[PRELIMINARY]`, `commissionAmount` dropped further to `620.0` (vs `3984.47` in #271), and the `discountAmount`/`priceGross` mismatch pattern has shifted — suggesting the service state continues to evolve independently of the pinned fixture expectations.

## Root Cause

- **MediaHouse failures (`tc_getMHTC03`, `tc_getMHTC03a`):** The `discountType` field in the MH basket order response does not match the CSV fixture values. The service returns `null` at the initial placement check (expected `RIALTO`) and `RIALTO` after the placement change (expected `NONE`) — an inversion of the intended discount-application sequence. All downstream pricing totals (VAT, commission, basket sum) also deviate, as pricing recalculation is coupled to the applied discount type.
- **Rialto failure (`tc_getIntegrationRialto05b`):** The placement change is not reflected in the Rialto GET response — `depth` remains `372` (expected `184`), confirming the placement-change write has not persisted. `statusFlags` is empty instead of `[PRELIMINARY]`, and `commissionAmount` is `620.0` instead of `7750.00`, indicating the order has not reached the expected booking state. Numeric formatting differences (`250000.0` vs `250000.00`) point to a serialisation inconsistency between the API and fixture format.

## Affected Components

- MediaHouse basket order retrieval validation (`MediaHouse\getMHB2A.csv`) — test cases `tc_getMHTC03`, `tc_getMHTC03a`.
- Rialto order retrieval validation (`Rialto\RialtoB2A\getRialtoB2A.csv`) — test case `tc_getIntegrationRialto05b`.
- Shared soft-assert aggregation at `stepDefinition.ApiStepDefinition.tearDown(ApiStepDefinition.java:69)`.

## Recommended Fix

- Confirm whether the placement-change PATCH (`tc_patchIntegrationMH03`) is completing successfully and that the resulting Rialto state reflects `depth=184` and `statusFlags=[PRELIMINARY]`; if not, the placement-change write path is broken.
- Investigate why `discountType` is inverted across the two MH steps — `null` pre-change and `RIALTO` post-change — and determine whether the discount application logic has regressed or the fixture expectations are stale.
- If service behaviour is intentionally different, update `getMHB2A.csv` and `getRialtoB2A.csv` to match the current API contract, and standardise numeric serialisation to `%.2f` format to eliminate formatting false positives.

## Prevention

- Gate placement-change flows with a contract test asserting `depth`, `statusFlags`, `discountType`, and at least one pricing field before merging API changes.
- Keep fixture CSV values coupled to service contract changes so expectation drift is caught at review time rather than in CI.
- Add a numeric serialisation normaliser to the assertion framework to treat `250000.0` and `250000.00` as equivalent.
