# Build 395 — Root Cause Analysis

**Source Report:** [build-395.md](../../../reports/build-failures/automationrunCAI-RIALTO-B2A-trunk/build-395.md)

---

## Build Summary

Build: 395  
Total Tests: 17  
Passed: 15  
Failed: 2  
Pass Rate: 88.2%

---

## Root Cause Groups

### Response Value Mismatch in Business Calculations

**Affected Features:**
- rialtoB2A(CASS).feature

**Affected Scenarios:**
- Returns StoreStatus of Order (tc_getRialtoB2A05)
- Calculate price for self service (tc_postRialtoB2A03)

**Failure Pattern:**
Expected numeric response values differ from actual values (`expected [276757.2] found [369009.6]`; `expected [89392.58] found [44696.29]`).

**Evidence:**
- `tc_getRialtoB2A05`: `Iterators differ at element [3]: 276757.2 != 369009.6 expected [276757.2] but found [369009.6]`
- `tc_postRialtoB2A03`: `expected [[89392.58, 89392.58]] but found [[44696.29, 44696.29]]`

**Impact:** 2 failures

**Confidence:** High

---

## Summary
- Both failures are concentrated in numeric response assertions for `rialtoB2A(CASS).feature`.
- Both failures have persisted since build 231, indicating an existing regression rather than a new break in build 395.

## Root Cause
- Backend response values for pricing/order totals are inconsistent with expected test oracle values in two scenarios.

## Affected Components
- API response payload values validated by:
  - `ApiStepDefinition.user_verify_the_response_body`
  - `ApiStepDefinition.user_verify_the_response_body_fields`

## Recommended Fix
- Reconcile expected fixtures vs service-side calculation logic for the impacted response fields.
- Re-run only `tc_getRialtoB2A05` and `tc_postRialtoB2A03` after correction.

## Prevention
- Add a lightweight check in test data maintenance to detect large proportional drifts in expected numeric fields.
