# Build 382 — Root Cause Analysis

**Source Report:** [build-382.md](../../../reports/build-failures/automationrunCAI-RIALTO-B2A-trunk/build-382.md)

---

## Build Summary

Build: 382
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
Expected monetary values in API assertions do not match actual response values.

**Evidence:**
- `tc_getRialtoB2A05`: `expected [276757.2] found [369009.6]` during response body comparison.
- `tc_postRialtoB2A03`: `expected [[89392.58, 89392.58]] found [[44696.29, 44696.29]]` during response-body-fields validation.

**Impact:** 2 failures

**Confidence:** High

## Summary
- Two failures are concentrated in price/value assertions for CASS B2A flows.

## Root Cause
- Test expected values and/or backend pricing outputs are out of sync for the two impacted scenarios.

## Affected Components
- `rialtoB2A(CASS).feature`
- Assertion handlers in `ApiStepDefinition` and JSON comparison utility paths shown in stack traces.

## Recommended Fix
- Validate current expected values for `tc_getRialtoB2A05` and `tc_postRialtoB2A03` against the intended pricing behavior, then align test data or API logic.

## Prevention
- Add a periodic contract check for critical pricing fields used by these scenarios.
