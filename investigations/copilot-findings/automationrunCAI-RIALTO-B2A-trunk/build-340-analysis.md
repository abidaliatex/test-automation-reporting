# Investigation — automationrunCAI-RIALTO-B2A-trunk #340

Source report: [build-340.md](../../../reports/build-failures/automationrunCAI-RIALTO-B2A-trunk/build-340.md)

## Summary
- Build 340 is **UNSTABLE** with 2/17 failures (88.2% pass rate).
- Both failures are numeric/financial field assertion mismatches in the CASS feature.
- All failures have been persisting since build 231 (`failedSince: 231`).

## Root Cause
- API responses for `tc_getRialtoB2A05` and `tc_postRialtoB2A03` return numeric values that differ from expected test data baselines.
- The actual amounts returned are consistently different from expected values, possibly indicating a data or business-rule change in the backend that has not been reflected in test expectations since build 231.

## Affected Components
- `rialtoB2A(CASS).feature`
- Validation steps in:
  - `ApiStepDefinition.user_verify_the_response_body` (JSONManager.compareJSONStrings — line 64)
  - `ApiStepDefinition.user_verify_the_response_body_fields` (line 155)

## Recommended Fix
- Reconcile expected data for `tc_getRialtoB2A05` and `tc_postRialtoB2A03` against the current API contract/data.
- Confirm whether the new values (`369009.6` and `[44696.28999999999, 44696.28999999999]`) represent the correct business output, then update test fixtures accordingly.

## Prevention
- Version and review expected numeric fixtures as part of any API/data contract changes.
- Add a contract-check step for critical financial fields to detect drift before full scenario assertions fail.
