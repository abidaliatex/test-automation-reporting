# Root Cause Analysis — Build 362

**Source Report:** [build-362.md](../../../reports/build-failures/automationrunCAI-RIALTO-B2A-trunk/build-362.md)
**Job:** automationrunCAI-RIALTO-B2A-trunk
**Date:** 2026-08-08

---

## Build Summary

Build: 362
Total Tests: 17
Passed: 14
Failed: 3
Pass Rate: 82.4%

---

## Root Cause Groups

### Response Value Mismatch in StoreStatus/Pricing Assertions

**Affected Features:**
- rialtoB2A(CASS).feature

**Affected Scenarios:**
- Returns StoreStatus of Order (tc_getRialtoB2A05)
- Calculate price for self service (tc_postRialtoB2A03)

**Failure Pattern:**
expected business values in response do not match actual payload values.

**Evidence:**
- `tc_getRialtoB2A05`: `Iterators differ at element [3]: 276757.2 != 369009.6 expected [276757.2] but found [369009.6]`
- `tc_postRialtoB2A03`: `expected [[89392.58, 89392.58]] but found [[44696.29, 44696.29]]`

**Impact:** 2 failures

**Confidence:** High

### Async Processing Not Completed at Verification Time

**Affected Features:**
- rialtoB2A(CASS).feature

**Affected Scenarios:**
- Returns StoreStatus of Update Order (tc_getRialtoB2A06)

**Failure Pattern:**
status code check expected final state `N200` but received intermediate state `N202`.

**Evidence:**
- `tc_getRialtoB2A06`: `expected [N200] but found [N202]`
- Failure occurs at the status-code assertion step immediately after the GET call.

**Impact:** 1 failure

**Confidence:** Medium

---

## Summary
- Build 362 is unstable with 3 failures grouped into response-value mismatches (2) and async status timing (1).

## Root Cause
- Response contract/value assertions for StoreStatus and pricing outputs are not aligned with returned data.
- Async update verification is checking before processing reaches final status.

## Affected Components
- Rialto B2A CASS API validation flow (`User verify the response body`, `User verify the response body fields`, `User verify the status code`).

## Recommended Fix
- Reconcile expected values for `tc_getRialtoB2A05` and `tc_postRialtoB2A03` with current response contract/test data.
- Add or tune polling/wait criteria before asserting `N200` in `tc_getRialtoB2A06`.

## Prevention
- Separate async-state polling assertions from payload-value assertions in test flow.
- Keep expected dataset/version synchronized with service-side pricing and StoreStatus behavior.
