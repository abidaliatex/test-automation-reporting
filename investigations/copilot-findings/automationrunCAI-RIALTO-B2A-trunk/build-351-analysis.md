# Investigation — automationrunCAI-RIALTO-B2A-trunk #351

Source report: [build-351.md](../../../reports/build-failures/automationrunCAI-RIALTO-B2A-trunk/build-351.md)

---

## Build Summary

Build: `automationrunCAI-RIALTO-B2A-trunk` #351  
Total Tests: 17  
Passed: 14  
Failed: 3  
Pass Rate: 82.4%

---

## Root Cause Groups

## Store status and response contract mismatch

**Affected Features:**
- `rialtoB2A(CASS).feature`

**Affected Scenarios:**
- Returns StoreStatus of Order (`tc_getRialtoB2A05`)
- Returns StoreStatus of Update Order (`tc_getRialtoB2A06`)

**Failure Pattern:**
Stored status/body assertions expect older values than current API output.

**Evidence:**
- `Iterators differ at element [3]: 276757.2 != 369009.6 expected [276757.2] but found [369009.6]`
- `expected [N200] but found [N202]`

**Impact:** 2 failures

**Confidence:** High

---

## Price calculation baseline drift

**Affected Features:**
- `rialtoB2A(CASS).feature`

**Affected Scenarios:**
- Calculate price for self service (`tc_postRialtoB2A03`)

**Failure Pattern:**
Price assertion expects a higher baseline than the current calculated response.

**Evidence:**
- `expected [[89392.58, 89392.58]] but found [[44696.28999999999, 44696.28999999999]]`

**Impact:** 1 failure

**Confidence:** High

---

## Summary

- Build #351 is unstable with 3 assertion failures in `rialtoB2A(CASS).feature`.
- Failures cluster into response/status contract mismatch (2) and price baseline mismatch (1).

## Root Cause

- Test expectations for status, response body values, and price fields are not aligned with current service outputs for the affected scenarios.

## Affected Components

- `rialtoB2A(CASS).feature`
- `Rialto\\RialtoB2A\\getRialtoB2A.csv`
- `Rialto\\RialtoB2A\\postRialtoB2A.csv`
- `ApiStepDefinition.user_verify_the_status_code`
- `ApiStepDefinition.user_verify_the_response_body`
- `ApiStepDefinition.user_verify_the_response_body_fields`

## Recommended Fix

- Rebaseline expected values for `tc_getRialtoB2A05`, `tc_getRialtoB2A06`, and `tc_postRialtoB2A03` against current API contract and pricing outputs.

## Prevention

- Add periodic contract/baseline review for these scenario datasets to detect drift before assertion execution.
