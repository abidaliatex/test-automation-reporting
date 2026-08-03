# Build 352 — Root Cause Analysis

**Source Report:** [build-352.md](../../reports/build-failures/automationrunCAI-RIALTO-B2A-trunk/build-352.md)
**Job:** automationrunCAI-RIALTO-B2A-trunk
**Date:** 2026-08-03

---

## Build Summary

Build: 352
Total Tests: 17
Passed: 14
Failed: 3
Pass Rate: 82.4%

---

## Root Cause Groups

---

## Incorrect Pricing / Value Computation in Order Lifecycle

**Affected Features:**
- rialtoB2A(CASS).feature

**Affected Scenarios:**
- Returns StoreStatus of Order (tc_getRialtoB2A05)
- Calculate price for self service (tc_postRialtoB2A03)

**Failure Pattern:**
Numeric values returned by the API differ from expected test data — price/cost fields are off by approximately 33% (`276757.2 vs 369009.6`) or exactly halved (`89392.58 vs 44696.28999...`), suggesting a calculation regression (e.g. wrong discount rate, wrong multiplier, or wrong number of insertions).

**Evidence:**
- `tc_getRialtoB2A05`: `Iterators differ at element [3]: 276757.2 != 369009.6 expected [276757.2] but found [369009.6]`
- `tc_postRialtoB2A03`: `expected [[89392.58, 89392.58]] but found [[44696.28999999999, 44696.28999999999]]`

**Impact:** 2 failures

**Confidence:** High

---

## Unexpected HTTP Status on Updated Order Retrieval

**Affected Features:**
- rialtoB2A(CASS).feature

**Affected Scenarios:**
- Returns StoreStatus of Update Order (tc_getRialtoB2A06)

**Failure Pattern:**
GET request for an updated order returns HTTP `N202` (Accepted / still processing) instead of expected `N200` (OK), suggesting the order update is not fully completed by the time the test queries it — possibly a timing/async issue or a regression in order status transitions.

**Evidence:**
- `tc_getRialtoB2A06`: `expected [N200] but found [N202]`
- Immediately follows a 10-second wait step, implying processing is still not finished within that window.

**Impact:** 1 failure

**Confidence:** Medium

---

## Summary

- All 3 failures have been present since **build 231** (age: 122 builds).
- Failures are isolated to the CASS feature suite (`rialtoB2A(CASS).feature`).
- tc_getRialtoB2A05 and tc_postRialtoB2A03 point to a pricing calculation regression; tc_getRialtoB2A06 points to an async order-state issue.

## Recommended Fix

- Investigate pricing/discount logic changes introduced around build 231.
- For tc_getRialtoB2A06: increase the wait time before querying the updated order, or update the test expectation to accept `N202` if that is the new intended contract.

## Prevention

- Add assertions on intermediate price calculation steps to detect regression earlier.
- Monitor order-status polling intervals when async processing times change.
