# Investigation — automationrunCAI-RIALTO-B2A-trunk #348

Source report: [build-348.md](../../../reports/build-failures/automationrunCAI-RIALTO-B2A-trunk/build-348.md)

---

## Build Summary

Build: `automationrunCAI-RIALTO-B2A-trunk` #348
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

---

## Price calculation expected-value drift

**Affected Features:**
- `rialtoB2A(CASS).feature`

**Affected Scenarios:**
- Calculate price for self service (`tc_postRialtoB2A03`)

**Failure Pattern:**
Calculated price amounts are exactly half the expected baseline values.

**Evidence:**
- `expected [[89392.58, 89392.58]] but found [[44696.28999999999, 44696.28999999999]]`
- Actual values are ~50% of expected, suggesting a pricing multiplier or split-cost change.

**Impact:** 1 failure

**Confidence:** High

---

## Summary

- Build #348 is unstable with 3 assertion failures in `rialtoB2A(CASS).feature`, all failing since build #231 (`failedSince: 231`, `age: 118`).

## Root Cause

- Expected test baselines do not align with current service output. All three failures are long-running regressions (age 118 builds).
- `tc_getRialtoB2A05`: Response body field at index 3 returns `369009.6` instead of `276757.2` — likely a data or pricing contract change.
- `tc_getRialtoB2A06`: Order status after update returns `N202` instead of `N200` — possibly a workflow state change in the API.
- `tc_postRialtoB2A03`: Price field returns half the expected amount — may indicate a cost-sharing or calculation rule change.

## Affected Components

- `rialtoB2A(CASS).feature`
- `getRialtoB2A.csv` (test data for GET scenarios)
- `postRialtoB2A.csv` (test data for POST scenarios)
- `ApiStepDefinition.user_verify_the_response_body` / `user_verify_the_response_body_fields`

## Recommended Fix

- Rebaseline expected values for `tc_getRialtoB2A05`, `tc_getRialtoB2A06`, and `tc_postRialtoB2A03` against current API contract.

## Prevention

- Add pre-merge contract checks to detect response/status baseline drift before scenario assertions run.
