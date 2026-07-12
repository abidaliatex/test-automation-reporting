# Build 288 Root Cause Analysis

Source report: [build-288.md](../../../reports/build-failures/automationrunCAI-RIALTOB2A-IntegrationTesting-Internal-trunk-demo/build-288.md)

## Summary

- Build `automationrunCAI-RIALTOB2A-IntegrationTesting-Internal-trunk-demo` #288 ended `UNSTABLE`.
- Test result: 11 passed, 3 failed (14 total).
- The same 3 test cases have `failedSince: 246`, so this is a persistent regression rather than a new one introduced only in build 288.

## Root Cause

- **MediaHouse validation drift (`tc_getMHTC03`, `tc_getMHTC03a`)**: MediaHouse GET assertions fail on `discountType`, commission, VAT, and total fields before and after the placement change, which points to incorrect downstream pricing/discount propagation for this flow.
- **Rialto post-update drift (`tc_getIntegrationRialto05b`)**: the follow-up Rialto GET response still shows an unexpected empty `statusFlags`, wrong `depth`, and incorrect commission/net price values after the placement update.
- Jenkins checked out revision `4a04ddba1e4e5809017f1f7cf91b06e93e3c19dd` (`updated api version from 87 to 88`), but the `failedSince: 246` age indicates these failures predate this specific revision.

## Affected Components

- `rialtoB2A(CASS)TestCase4.feature`
- `MediaHouse\getMHB2A.csv` test cases `tc_getMHTC03` and `tc_getMHTC03a`
- `Rialto\RialtoB2A\getRialtoB2A.csv` test case `tc_getIntegrationRialto05b`
- Assertion aggregation in `stepDefinition.ApiStepDefinition.tearDown(ApiStepDefinition.java:69)`

## Recommended Fix

- Check the placement-change flow that feeds MediaHouse and Rialto responses, focusing on `discountType`, commission, VAT, totals, `statusFlags`, and placement `depth`.
- Compare current service output with the fixtures behind `tc_getMHTC03`, `tc_getMHTC03a`, and `tc_getIntegrationRialto05b` to determine whether the application or the expected data regressed around build 246.

## Prevention

- Add a focused regression check for placement-change propagation across both MediaHouse and Rialto response fields.
- Alert on long-running failures so multi-build regressions like this are triaged earlier.
