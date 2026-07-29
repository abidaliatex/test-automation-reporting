# Investigation — automationrunCAI-RIALTO-B2A-trunk #343

Source report: [build-343.md](../../../reports/build-failures/automationrunCAI-RIALTO-B2A-trunk/build-343.md)

---

## Build Summary

Build: `automationrunCAI-RIALTO-B2A-trunk` #343  
Total Tests: 17  
Passed: 15  
Failed: 2  
Pass Rate: 88.2%

---

## Root Cause Groups

## Store status response payload mismatch

**Affected Features:**
- `rialtoB2A(CASS).feature`

**Affected Scenarios:**
- Returns StoreStatus of Order (`tc_getRialtoB2A05`)

**Failure Pattern:**
Response-body value assertion mismatch against current API output.

**Evidence:**
- `Iterators differ at element [3]: 276757.2 != 369009.6 expected [276757.2] but found [369009.6]`
- Stack trace points to `JSONManager.compareJSONStrings` via `ApiStepDefinition.user_verify_the_response_body`.

**Impact:** 1 failure

**Confidence:** High

## Price field expected-value mismatch

**Affected Features:**
- `rialtoB2A(CASS).feature`

**Affected Scenarios:**
- Calculate price for self service (`tc_postRialtoB2A03`)

**Failure Pattern:**
Price-related response-body fields expected outdated values.

**Evidence:**
- `expected [[89392.58, 89392.58]] but found [[44696.28999999999, 44696.28999999999]]`
- Failure occurs on response-body field validation step in `rialtoB2A(CASS).feature:155`.

**Impact:** 1 failure

**Confidence:** High

---

## Summary

- Build #343 is unstable due to two deterministic response-value assertion mismatches in CASS validation scenarios.

## Root Cause

- Both failures are caused by expected response values not matching current API responses.

## Affected Components

- `rialtoB2A(CASS).feature`
- API response body assertion steps in `ApiStepDefinition`

## Recommended Fix

- Rebaseline expected values for `tc_getRialtoB2A05` and `tc_postRialtoB2A03` against current service contract/data.

## Prevention

- Add contract baseline checks to detect expected-value drift before scenario-level assertion execution.
