# Build 386 — Root Cause Analysis

**Source Report:** [build-386.md](../../../reports/build-failures/automationrunCAI-RIALTO-B2A-trunk/build-386.md)

---

## Build Summary

Build: 386  
Total Tests: 17  
Passed: 15  
Failed: 2  
Pass Rate: 88.2%

---

## Root Cause Groups

### Response Payload Price/Value Mismatch

**Affected Features:**
- rialtoB2A(CASS).feature

**Affected Scenarios:**
- Returns StoreStatus of Order (tc_getRialtoB2A05)
- Calculate price for self service (tc_postRialtoB2A03)

**Failure Pattern:**
Response body numeric values do not match expected values in assertions.

**Evidence:**
- `tc_getRialtoB2A05`: `Iterators differ at element [3]: 276757.2 != 369009.6 expected [276757.2] but found [369009.6]`
- `tc_postRialtoB2A03`: `expected [[89392.58, 89392.58]] but found [[44696.29, 44696.29]]`

**Impact:** 2 failures

**Confidence:** High

---

## Summary
- Build is unstable due to 2 assertion failures in CASS B2A validations.
- Both failures are persisted regressions (`failedSince: 231`) and likely tied to response value changes rather than transport failures.

## Root Cause
- Test assertions expect legacy numeric values while API responses return different values for pricing/monetary fields.

## Affected Components
- `rialtoB2A(CASS)` API response validation flow
- JSON comparison and response-body field assertion checks

## Recommended Fix
- Revalidate expected datasets for `tc_getRialtoB2A05` and `tc_postRialtoB2A03` against current API pricing/output contracts.
- If current API values are correct, update test baselines; if not, investigate service-side pricing/value regression.

## Prevention
- Add contract-level checks for critical monetary fields and a controlled baseline update process whenever pricing logic changes.
