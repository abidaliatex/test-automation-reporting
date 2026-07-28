# Investigation — automationrunCAI-RIALTO-B2A-trunk #341

Source report: [build-341.md](../../../reports/build-failures/automationrunCAI-RIALTO-B2A-trunk/build-341.md)

---

## Build Summary

Build: `automationrunCAI-RIALTO-B2A-trunk` #341  
Total Tests: 17  
Passed: 14  
Failed: 3  
Pass Rate: 82.4%

---

## Root Cause Groups

### Response payload value mismatch in pricing/store-status flows

**Affected Features:**
- `rialtoB2A(CASS).feature`

**Affected Scenarios:**
- Calculate price for self service (`tc_postRialtoB2A03`)
- Returns StoreStatus of Order (`tc_getRialtoB2A05`)

**Failure Pattern:**
Expected numeric values differ from actual API payload values (approximately 2x delta in asserted amounts).

**Evidence:**
- `expected [[89392.58, 89392.58]] but found [[44696.28999999999, 44696.28999999999]]`
- `Iterators differ at element [3]: 276757.2 != 369009.6 expected [276757.2] but found [369009.6]`

**Impact:** 2 failures

**Confidence:** High

### Status code expectation mismatch on update-order status retrieval

**Affected Features:**
- `rialtoB2A(CASS).feature`

**Affected Scenarios:**
- Returns StoreStatus of Update Order (`tc_getRialtoB2A06`)

**Failure Pattern:**
Step expects `N200`, but service responded with `N202`.

**Evidence:**
- `expected [N200] but found [N202]`
- Failure at `rialtoB2A(CASS).feature:111` during `User verify the status code "Response Code"`

**Impact:** 1 failure

**Confidence:** High

---

## Summary

- Build #341 is unstable with 3 failures, concentrated in response validation for CASS price/status flows.

## Root Cause

- Two failures are assertion mismatches on expected numeric response values.
- One failure is an expected status-code mismatch (`N200` vs `N202`) during update-order status retrieval.

## Affected Components

- `rialtoB2A(CASS).feature`
- Assertions in response body and response code validation steps

## Recommended Fix

- Revalidate expected amounts for `tc_postRialtoB2A03` and `tc_getRialtoB2A05` against current service calculation behavior.
- Confirm whether `N202` is now valid for `tc_getRialtoB2A06`; update test expectation or service behavior accordingly.

## Prevention

- Add/maintain contract checks for key numeric fields and status codes before full scenario assertions run.
