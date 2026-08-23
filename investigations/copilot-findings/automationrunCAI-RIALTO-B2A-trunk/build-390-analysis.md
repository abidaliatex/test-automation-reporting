# Build Analysis — automationrunCAI-RIALTO-B2A-trunk #390

**Source Report:** [build-390.md](../../../reports/build-failures/automationrunCAI-RIALTO-B2A-trunk/build-390.md)

---

## Build Summary

Build: automationrunCAI-RIALTO-B2A-trunk #390  
Total Tests: 17  
Passed: 15  
Failed: 2  
Pass Rate: 88.2%

---

## Root Cause Groups

## Numeric Value Mismatch in API Response Assertions

**Affected Features:**
- rialtoB2A(CASS).feature

**Affected Scenarios:**
- Returns StoreStatus of Order (tc_getRialtoB2A05)
- Calculate price for self service (tc_postRialtoB2A03)

**Failure Pattern:**
Response numeric assertions are failing because expected financial values do not match actual API response values.

**Evidence:**
- `Iterators differ at element [3]: 276757.2 != 369009.6 expected [276757.2] but found [369009.6]`
- `expected [[89392.58, 89392.58]] but found [[44696.29, 44696.29]]`
- Both failures come from response assertion steps in `ApiStepDefinition`/`JSONManager`.
- Both failures are long-running (`failedSince: 231`, age 160).

**Impact:** 2 failures

**Confidence:** High
