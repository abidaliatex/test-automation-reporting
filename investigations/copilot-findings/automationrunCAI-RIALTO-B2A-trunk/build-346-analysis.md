# Investigation — automationrunCAI-RIALTO-B2A-trunk #346

Source report: [build-346.md](../../../reports/build-failures/automationrunCAI-RIALTO-B2A-trunk/build-346.md)

---

## Build Summary

Build: `automationrunCAI-RIALTO-B2A-trunk` #346
Total Tests: 17
Passed: 15
Failed: 2
Pass Rate: 88.2%

---

## Root Cause Groups

## Store status response value mismatch

**Affected Features:**
- `rialtoB2A(CASS).feature`

**Affected Scenarios:**
- Returns StoreStatus of Order (`tc_getRialtoB2A05`)

**Failure Pattern:**
Numeric value at response body element [3] differs from expected baseline: expected 276757.2 but API returned 369009.6.

**Evidence:**
- `Iterators differ at element [3]: 276757.2 != 369009.6 expected [276757.2] but found [369009.6]`
- Stack trace: `JSONManager.compareJSONStrings` → `ApiStepDefinition.user_verify_the_response_body` at `rialtoB2A(CASS).feature:64`
- Failing since build #231 (116 consecutive builds)

**Impact:** 1 failure

**Confidence:** High

---

## Price calculation expected-value drift

**Affected Features:**
- `rialtoB2A(CASS).feature`

**Affected Scenarios:**
- Calculate price for self service (`tc_postRialtoB2A03`)

**Failure Pattern:**
Returned price values are exactly half of the test's expected baseline (44696.29 vs 89392.58), suggesting a pricing calculation or aggregation change in the service.

**Evidence:**
- `expected [[89392.58, 89392.58]] but found [[44696.28999999999, 44696.28999999999]]`
- Stack trace: `ApiStepDefinition.user_verify_the_response_body_fields` at `rialtoB2A(CASS).feature:155`
- Actual values are exactly 50% of expected — possibly a factor or multiplier was changed in the pricing logic
- Failing since build #231 (116 consecutive builds)

**Impact:** 1 failure

**Confidence:** High

---

## Summary

- Build #346 is unstable with 2 assertion mismatches in CASS API validation scenarios.
- Both failures are long-running regressions (failing since build #231).

## Root Cause

- Test baselines for `tc_getRialtoB2A05` and `tc_postRialtoB2A03` do not match current service output.
- The price calculation failure shows actual values at exactly 50% of expected, indicating a persistent change in service behaviour since build #231.

## Affected Components

- `rialtoB2A(CASS).feature`
- Response assertion steps in `ApiStepDefinition` (`user_verify_the_response_body`, `user_verify_the_response_body_fields`)

## Recommended Fix

- Rebaseline expected values for `tc_getRialtoB2A05` and `tc_postRialtoB2A03` against the current contract, or investigate the pricing/store-status service change introduced around build #231.

## Prevention

- Add pre-merge contract checks to detect response value drift before scenario assertions run.
