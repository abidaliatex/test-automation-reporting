# Investigation — automationrunCAI-RIALTO-B2A-trunk #339

Source report: [build-339.md](../../../reports/build-failures/automationrunCAI-RIALTO-B2A-trunk/build-339.md)

## Summary
- Build 339 is **UNSTABLE** with 3/17 failures (82.4% pass rate).
- Failures are grouped into:
  - response amount/value assertion mismatches (2)
  - expected status code mismatch `N200` vs `N202` (1)
- All 3 failures have been persisting since build 231 (`failedSince: 231`).

## Root Cause
- API responses for targeted CASS scenarios do not match the expected baseline test data for numeric fields and status values.
- This may indicate business-rule or data changes in downstream response content that have not been reflected in test expectations since build 231.

## Affected Components
- `rialtoB2A(CASS).feature`
- Validation steps in:
  - `ApiStepDefinition.user_verify_the_response_body` (JSONManager.compareJSONStrings)
  - `ApiStepDefinition.user_verify_the_response_body_fields`
  - `ApiStepDefinition.user_verify_the_status_code`

## Recommended Fix
- Reconcile expected data for `tc_getRialtoB2A05` and `tc_postRialtoB2A03` against current API contract/data.
- Confirm whether `tc_getRialtoB2A06` should now expect `N202` instead of `N200`, then update test data or service behavior accordingly.

## Prevention
- Add a lightweight contract check for critical amount/status fields before full scenario assertions.
- Track and version expected response fixtures so intentional API changes are reflected in test data before pipeline runs.
