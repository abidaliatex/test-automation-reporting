# Build 383 — Root Cause Analysis

**Source Report:** [build-383.md](../../../reports/build-failures/automationrunCAI-RIALTO-B2A-trunk/build-383.md)

---

## Build Summary

Build: 383  
Total Tests: 17  
Passed: 15  
Failed: 2  
Pass Rate: 88.2%

---

## Root Cause Groups

## Pricing Assertion Mismatch

**Affected Features:**
- rialtoB2A(CASS).feature

**Affected Scenarios:**
- Returns StoreStatus of Order (tc_getRialtoB2A05)
- Calculate price for self service (tc_postRialtoB2A03)

**Failure Pattern:**
Expected pricing values in API assertions do not match actual API response values.

**Evidence:**
- `tc_getRialtoB2A05`: `expected [276757.2] found [369009.6]` in response-body comparison.
- `tc_postRialtoB2A03`: `expected [[89392.58, 89392.58]] found [[44696.29, 44696.29]]` in response-body-fields validation.

**Impact:** 2 failures

**Confidence:** High

## Summary
- Failures are concentrated in pricing value assertions for CASS B2A scenarios.

## Root Cause
- The expected values used by assertions are out of sync with current API outputs for the two failing scenarios.

## Affected Components
- `rialtoB2A(CASS).feature`
- Assertion paths reported by stack traces (`JSONManager.compareJSONStrings`, `ApiStepDefinition.user_verify_the_response_body[_fields]`).

## Recommended Fix
- Revalidate expected pricing values for `tc_getRialtoB2A05` and `tc_postRialtoB2A03`, then align test data or service behavior.

## Prevention
- Add/refresh contract checks for critical pricing fields used by these scenarios.
