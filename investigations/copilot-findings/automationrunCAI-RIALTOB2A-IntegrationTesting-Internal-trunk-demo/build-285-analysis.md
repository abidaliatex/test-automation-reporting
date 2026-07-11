# Build 285 Root Cause Analysis

Source report: [build-285.md](../../../reports/build-failures/automationrunCAI-RIALTOB2A-IntegrationTesting-Internal-trunk-demo/build-285.md)

## Summary

- Build `automationrunCAI-RIALTOB2A-IntegrationTesting-Internal-trunk-demo` #285 ended `UNSTABLE`.
- Test result: 11 passed, 3 failed (14 total).
- Failures cluster into two patterns: MH discount/pricing drift and Rialto placement-state/pricing drift.

## Root Cause

- **MH retrieval validation drift (`tc_getMHTC03`, `tc_getMHTC03a`)**: returned `discountType` and financial totals differ from expected fixtures, indicating discount/price calculation mismatch in the current API response.
- **Rialto post-update validation drift (`tc_getIntegrationRialto05b`)**: updated order retrieval returns unexpected `statusFlags`, `depth`, and `commissionAmount`, indicating placement update state/calculation mismatch.

## Affected Components

- `rialtoB2A(CASS)TestCase4.feature`
- Scenario fixtures referenced by:
  - `MediaHouse\getMHB2A.csv` (`tc_getMHTC03`, `tc_getMHTC03a`)
  - `Rialto\RialtoB2A\getRialtoB2A.csv` (`tc_getIntegrationRialto05b`)
- Assertion aggregation point: `stepDefinition.ApiStepDefinition.tearDown(ApiStepDefinition.java:69)`

## Recommended Fix

- Verify discount mapping and downstream basket total/VAT/commission calculation for MH GET flow.
- Verify placement update persistence and order state transition before Rialto GET validation.
- Reconcile expected fixture values with current API contract only after confirming intended business behavior.

## Prevention

- Add contract checks around `discountType`, `statusFlags`, `depth`, `commissionAmount`, and total fields for this integration flow.
- Fail early in pipeline when post-placement-update state is inconsistent before downstream scenario assertions run.
