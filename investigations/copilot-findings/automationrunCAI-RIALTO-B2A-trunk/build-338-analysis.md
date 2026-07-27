# Investigation — automationrunCAI-RIALTO-B2A-trunk #338

Source report: [build-338.md](../../../reports/build-failures/automationrunCAI-RIALTO-B2A-trunk/build-338.md)

## Summary
- Build 338 is **UNSTABLE** with 2/17 failures (88.2% pass rate).
- Both failures are persistent numeric assertion mismatches, failing since build 231.
- The third failure seen in build 337 (`tc_getRialtoB2A06` status code mismatch) is now resolved (FIXED).

## Root Cause
- API responses for `tc_getRialtoB2A05` and `tc_postRialtoB2A03` continue to return numeric values that diverge from the expected test baseline.
- For `tc_postRialtoB2A03` the actual value (`44696.29`) is exactly half of the expected value (`89392.58`), possibly indicating a pricing calculation that applies a 50% factor not reflected in test data.
- For `tc_getRialtoB2A05` the actual value (`369009.6`) exceeds the expected value (`276757.2`), possibly due to a data change in the referenced order's stored amounts.

## Affected Components
- `rialtoB2A(CASS).feature`
- Validation steps in:
  - `ApiStepDefinition.user_verify_the_response_body` (line 357)
  - `ApiStepDefinition.user_verify_the_response_body_fields` (line 609)

## Recommended Fix
- Reconcile expected data for `tc_getRialtoB2A05` and `tc_postRialtoB2A03` against the current API contract and live data.
- Investigate whether the price calculation for `tc_postRialtoB2A03` has changed (e.g. halved rate) and update the expected fixture accordingly.

## Prevention
- Version and review expected response fixtures when API business rules or data change.
- Add a contract-level check for critical amount fields to surface discrepancies before full scenario assertions.
