# Investigation — automationrunCAI-RIALTO-B2A-trunk #342

Source report: [build-342.md](../../../reports/build-failures/automationrunCAI-RIALTO-B2A-trunk/build-342.md)

---

## Build Summary

Build: `automationrunCAI-RIALTO-B2A-trunk` #342  
Total Tests: 17  
Passed: 14  
Failed: 3  
Pass Rate: 82.4%

---

## Root Cause Groups

## Response payload value mismatch in price/store-status assertions

**Affected Features:**
- `rialtoB2A(CASS).feature`

**Affected Scenarios:**
- Returns StoreStatus of Order (`tc_getRialtoB2A05`)
- Calculate price for self service (`tc_postRialtoB2A03`)

**Failure Pattern:**
Response-body numeric assertions differ from API output values.

**Evidence:**
- `Iterators differ at element [3]: 276757.2 != 369009.6 expected [276757.2] but found [369009.6]`
- `expected [[89392.58, 89392.58]] but found [[44696.28999999999, 44696.28999999999]]`

**Impact:** 2 failures

**Confidence:** High

## Status code expectation mismatch in update-order status retrieval

**Affected Features:**
- `rialtoB2A(CASS).feature`

**Affected Scenarios:**
- Returns StoreStatus of Update Order (`tc_getRialtoB2A06`)

**Failure Pattern:**
Response code expected `N200` but API returned `N202`.

**Evidence:**
- `expected [N200] but found [N202]`
- Failure at `rialtoB2A(CASS).feature:111` on step `User verify the status code "Response Code"`

**Impact:** 1 failure

**Confidence:** High

---

## Summary

- Build #342 is unstable with 3 failures in CASS response validation flows.

## Root Cause

- Two failures are numeric payload assertion mismatches.
- One failure is a status-code expectation mismatch (`N200` vs `N202`).

## Affected Components

- `rialtoB2A(CASS).feature`
- Response body and status-code validation steps in API test flow

## Recommended Fix

- Rebaseline expected numeric values for `tc_getRialtoB2A05` and `tc_postRialtoB2A03` against current service contract.
- Confirm whether `N202` is expected for `tc_getRialtoB2A06`; align test expectation or API behavior.

## Prevention

- Add contract checks for critical numeric and status-code fields before full scenario assertions.
