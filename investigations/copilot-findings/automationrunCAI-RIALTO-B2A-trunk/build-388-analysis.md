# Build 388 — Root Cause Analysis

**Source Report:** [build-388.md](../../reports/build-failures/automationrunCAI-RIALTO-B2A-trunk/build-388.md)
**Job:** automationrunCAI-RIALTO-B2A-trunk
**Date:** 2026-08-22

---

## Build Summary

Build: 388
Total Tests: 17
Passed: 15
Failed: 2
Pass Rate: 88.2%

---

## Root Cause Groups

## Incorrect Numeric Values in API Response Body

**Affected Features:**
- rialtoB2A(CASS).feature

**Affected Scenarios:**
- User perform CASS POST API — Returns StoreStatus of Order (tc_getRialtoB2A05)
- User perform CASS POST API — Calculate price for self service (tc_postRialtoB2A03)

**Failure Pattern:**
Response body numeric field values do not match expected values — actual values differ by approximately a factor of ~0.5x (halved) or differ by a fixed delta, suggesting a pricing/calculation logic change in the backend.

**Evidence:**
- `tc_getRialtoB2A05`: `expected [276757.2] but found [369009.6]` at element [3] of response body array
- `tc_postRialtoB2A03`: `expected [[89392.58, 89392.58]] but found [[44696.29, 44696.29]]` — actual values are ~50% of expected, possibly a rate or multiplier change

**Impact:** 2 failures

**Confidence:** High

---

## Summary

Both failures are numeric assertion mismatches in response body fields, persisting since build 231. The values consistently differ (either by a ratio or delta), pointing to a backend calculation or data change rather than a test infrastructure issue.

## Root Cause

Backend pricing/calculation logic may have changed in the CASS service, returning different numeric values than what the test data expects. Both failures share the same step definition (`ApiStepDefinition`) and have been failing since build 231, indicating a persistent regression.

## Affected Components

- `rialtoB2A(CASS).feature` — scenarios at lines 68 and 163
- `stepDefinition.ApiStepDefinition` — `user_verify_the_response_body` and `user_verify_the_response_body_fields`
- Test data files: `getRialtoB2A.csv` (tc_getRialtoB2A05), `postRialtoB2A.csv` (tc_postRialtoB2A03)

## Recommended Fix

- Verify current expected values in `getRialtoB2A.csv` and `postRialtoB2A.csv` against the current CASS service behaviour.
- If the service change is intentional, update the expected values in the CSV test data files.
- If the service change is a regression, revert the backend change.

## Prevention

- Pin expected response values to a known-good environment snapshot.
- Add a monitoring alert when numeric fields deviate beyond a threshold to catch regressions earlier.
