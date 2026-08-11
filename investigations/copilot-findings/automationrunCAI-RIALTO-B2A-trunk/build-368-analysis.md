# Build 368 — Root Cause Analysis

**Source Report:** [build-368.md](../../../reports/build-failures/automationrunCAI-RIALTO-B2A-trunk/build-368.md)

---

## Build Summary

Build: 368  
Total Tests: 17  
Passed: 15  
Failed: 2  
Pass Rate: 88.2%

---

## Root Cause Groups

## Numeric Value Mismatch in Response Assertions

**Affected Features:**
- rialtoB2A(CASS).feature

**Affected Scenarios:**
- Returns StoreStatus of Order (tc_getRialtoB2A05)
- Calculate price for self service (tc_postRialtoB2A03)

**Failure Pattern:**
Response numeric fields expected in assertions do not match actual values returned by API payloads.

**Evidence:**
- `tc_getRialtoB2A05`: `Iterators differ at element [3]: 276757.2 != 369009.6 expected [276757.2] but found [369009.6]`
- `tc_postRialtoB2A03`: `expected [[89392.58, 89392.58]] but found [[44696.29, 44696.29]]`

**Impact:** 2 failures

**Confidence:** High

---

## Summary
- Both failures are assertion mismatches on response values, suggesting shared data/calculation drift in downstream response content.

## Root Cause
- Expected financial/status values in test data no longer align with current API outputs for the two scenarios above.

## Affected Components
- `Rialto\RialtoB2A\getRialtoB2A.csv` (tc_getRialtoB2A05)
- `Rialto\RialtoB2A\postRialtoB2A.csv` (tc_postRialtoB2A03)
- `rialtoB2A(CASS).feature`

## Recommended Fix
- Reconcile expected values in test datasets with current API pricing/status computation inputs for the two failing test cases.

## Prevention
- Add a lightweight pre-merge validation that flags large numeric deltas in known pricing-related response fields.
