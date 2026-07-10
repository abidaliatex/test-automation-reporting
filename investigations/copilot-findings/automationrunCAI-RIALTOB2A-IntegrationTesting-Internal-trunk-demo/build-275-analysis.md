# Build 275 Root Cause Analysis

Source report: [build-275.md](../../../reports/build-failures/automationrunCAI-RIALTOB2A-IntegrationTesting-Internal-trunk-demo/build-275.md)

## Summary

- Build `automationrunCAI-RIALTOB2A-IntegrationTesting-Internal-trunk-demo` #275 ended `UNSTABLE` with 3 failures out of 14 tests (78.6% pass rate).
- All failed scenarios are in `rialtoB2A(CASS)TestCase4.feature` and occur during retrieval validation after the placement-create / placement-change flow.
- Jenkins checked out revision `4a04ddba1e4e5809017f1f7cf91b06e93e3c19dd` with commit message `updated api version from 87 to 88`.
- The same scenarios report `failedSince: 246`, so this build continues an established expectation drift rather than introducing a brand-new failure set.

## Root Cause

- **MediaHouse retrieval failures (`tc_getMHTC03`, `tc_getMHTC03a`):** The basket-order response does not match the pinned fixture values in `MediaHouse\getMHB2A.csv`. `discountType` is inverted across the before/after checks (`null` instead of `RIALTO`, then `RIALTO` instead of `NONE`), and the downstream commission, VAT, and total fields also differ. This suggests either the service-side pricing/discount calculation changed or the fixture data no longer matches the current API behavior.
- **Rialto retrieval failure (`tc_getIntegrationRialto05b`):** The post-change GET returns a different placement state than expected: `orderHeader.statusFlags` is empty instead of `PRELIMINARY`, `orderAdDetails[0].depth` is `372` instead of `184`, and the commission/net amounts do not match the expected placement outcome. This points to either the placement change not being reflected in the retrieved order state or a pricing/status recalculation change in the current API version.

## Affected Components

- MediaHouse retrieval expectations in `MediaHouse\getMHB2A.csv` for `tc_getMHTC03` and `tc_getMHTC03a`.
- Rialto retrieval expectations in `Rialto\RialtoB2A\getRialtoB2A.csv` for `tc_getIntegrationRialto05b`.
- Shared soft-assert aggregation in `stepDefinition.ApiStepDefinition.tearDown(ApiStepDefinition.java:69)` where the mismatches surface.

## Recommended Fix

- Confirm whether the v88 API behavior for placement change intentionally changed `discountType`, commission, VAT, totals, and placement-derived fields.
- If the responses are correct for the current service version, update `getMHB2A.csv` and `getRialtoB2A.csv` to the current post-placement values.
- If the responses are not expected, investigate why the placement-change flow is returning empty `statusFlags`, `depth=372`, and reduced commission/net values after the update.

## Prevention

- Add a focused contract check around placement-change retrieval that validates `discountType`, `statusFlags`, `depth`, and one representative pricing field before broader regression suites run.
- Keep CSV fixture updates coupled to API version changes so expectation drift is reviewed when the version changes land.
