# Investigation — automationrunCAI-RIALTO-B2A-trunk #345

Source report: [build-345.md](../../../reports/build-failures/automationrunCAI-RIALTO-B2A-trunk/build-345.md)

---

## Build Summary

Build: `automationrunCAI-RIALTO-B2A-trunk` #345  
Total Tests: 17  
Passed: 14  
Failed: 3  
Pass Rate: 82.4%

---

## Root Cause Groups

## Store status contract/assertion mismatch

**Affected Features:**
- `rialtoB2A(CASS).feature`

**Affected Scenarios:**
- Returns StoreStatus of Order (`tc_getRialtoB2A05`)
- Returns StoreStatus of Update Order (`tc_getRialtoB2A06`)

**Failure Pattern:**
Store-status validation expects older payload/status values than current API response.

**Evidence:**
- `Iterators differ at element [3]: 276757.2 != 369009.6 expected [276757.2] but found [369009.6]`
- `expected [N200] but found [N202]`

**Impact:** 2 failures

**Confidence:** High

## Price calculation expected-value drift

**Affected Features:**
- `rialtoB2A(CASS).feature`

**Affected Scenarios:**
- Calculate price for self service (`tc_postRialtoB2A03`)

**Failure Pattern:**
Calculated amount fields in response are lower than the test's expected baseline.

**Evidence:**
- `expected [[89392.58, 89392.58]] but found [[44696.28999999999, 44696.28999999999]]`
- Stack trace points to `ApiStepDefinition.user_verify_the_response_body_fields`.

**Impact:** 1 failure

**Confidence:** High

---

## Summary

- Build #345 is unstable due to three assertion mismatches in CASS API validation scenarios.

## Root Cause

- Expected test baselines (status and response values) do not align with current service output for the affected scenarios.

## Affected Components

- `rialtoB2A(CASS).feature`
- Response/status assertion steps in `ApiStepDefinition`

## Recommended Fix

- Rebaseline expected values for `tc_getRialtoB2A05`, `tc_getRialtoB2A06`, and `tc_postRialtoB2A03` using the current contract/data.

## Prevention

- Add pre-merge contract checks to detect response/status baseline drift before scenario assertions run.
