# Build 268 Root Cause Analysis

Source report: [build-268.md](../../../reports/build-failures/automationrunCAI-RIALTOB2A-IntegrationTesting-Internal-trunk-demo/build-268.md)

## Summary

- Build `automationrunCAI-RIALTOB2A-IntegrationTesting-Internal-trunk-demo` #268 finished `UNSTABLE` with 3 failed tests out of 14.
- All failures belong to `rialtoB2A (CASS TC4 Change Placement)` and occur in post-placement-change retrieval assertions.
- The same 3 tests have been failing since build #246, indicating a persistent unresolved regression or an intentional service change whose test expectations have not been updated.

## Root Cause

- **MediaHouse pricing/discount drift (2 failures):** `tc_getMHTC03` and `tc_getMHTC03a` assert on `discountType`, commission, VAT, and total fields in the MH order basket after a placement change. Actual values differ from expectations on every numeric and enum pricing field, suggesting the MH service is computing discount and pricing differently from what the CSV fixtures expect.
- **Rialto recalculation mismatch (1 failure):** `tc_getIntegrationRialto05b` asserts that after a placement update the Rialto order reflects a new depth, updated commission, and `PRELIMINARY` status. None of those match: depth is double (372 vs 184), commission is ~8% of expected (620 vs 7750), and `statusFlags` is empty. This may indicate the placement-change PATCH processed but the Rialto recalculation did not propagate correctly.

## Affected Components

- MediaHouse retrieval checks driven by `getMHB2A.csv` (`tc_getMHTC03`, `tc_getMHTC03a`)
- Rialto retrieval checks driven by `getRialtoB2A.csv` (`tc_getIntegrationRialto05b`)
- Shared soft-assert aggregation in `stepDefinition.ApiStepDefinition.tearDown`

## Recommended Fix

- Compare actual API responses from build #268 with the expected values in the CSV fixtures.
- If the service behaviour changed intentionally (e.g. commission rate or depth calculation update), update fixture expected values for `tc_getMHTC03`, `tc_getMHTC03a`, and `tc_getIntegrationRialto05b`.
- If the differences are unintentional, investigate the placement-change recalculation logic in both MH and Rialto services.

## Prevention

- Add a focused contract-smoke check for placement-change pricing fields whenever the placement calculation logic is modified.
- Consider pinning `discountType`, commission, and VAT fields in a lightweight smoke test so regressions are caught before full integration runs.
