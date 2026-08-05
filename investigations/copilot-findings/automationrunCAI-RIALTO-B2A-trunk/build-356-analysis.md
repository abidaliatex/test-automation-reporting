# Root Cause Analysis — Build 356

**Source Report:** [build-356.md](../../reports/build-failures/automationrunCAI-RIALTO-B2A-trunk/build-356.md)
**Job:** automationrunCAI-RIALTO-B2A-trunk
**Date:** 2026-08-05

---

## Build Summary

Build: 356
Total Tests: 17
Passed: 14
Failed: 3
Pass Rate: 82.4%

---

## Root Cause Groups

## Incorrect Pricing / Financial Value Mismatch

**Affected Features:**
- rialtoB2A(CASS).feature

**Affected Scenarios:**
- Returns StoreStatus of Order (tc_getRialtoB2A05)
- Calculate price for self service (tc_postRialtoB2A03)

**Failure Pattern:**
Response body contains wrong numeric values — amounts returned by the API do not match expected figures (e.g. `276757.2 != 369009.6`; `[44696.29, 44696.29]` vs `[89392.58, 89392.58]`). The discrepancy in `tc_postRialtoB2A03` is exactly 50% of the expected value, suggesting a possible rate or multiplier change in pricing logic.

**Evidence:**
- `tc_getRialtoB2A05`: `Iterators differ at element [3]: 276757.2 != 369009.6 expected [276757.2] but found [369009.6]`
- `tc_postRialtoB2A03`: `expected [[89392.58, 89392.58]] but found [[44696.29, 44696.29]]` — actual is ~50% of expected

**Impact:** 2 failures

**Confidence:** High

---

## Unexpected HTTP Status Code on Update Order

**Affected Features:**
- rialtoB2A(CASS).feature

**Affected Scenarios:**
- Returns StoreStatus of Update Order (tc_getRialtoB2A06)

**Failure Pattern:**
GET request for updated order status returns `N202 (Accepted/Processing)` instead of the expected `N200 (OK)`, suggesting the backend is still processing the update when the test polls for the result.

**Evidence:**
- `tc_getRialtoB2A06`: `expected [N200] but found [N202]` at `User verify the status code "Response Code"` (feature line 111)

**Impact:** 1 failure

**Confidence:** Medium

---

## Summary

| Section | Detail |
|---|---|
| **Root Cause** | API returns incorrect financial values (pricing/rate change) and unexpected processing status |
| **Affected Components** | Rialto B2A CASS API — StoreStatus and price-calculation endpoints |
| **Failing Since** | Build 231 (all 3 failures are persistent, age 126 builds) |
| **Recommended Fix** | Verify pricing multiplier/rate configuration in the B2A service; increase wait time before polling order status in `tc_getRialtoB2A06` |
| **Prevention** | Add contract tests for pricing calculations; use polling with retry instead of fixed wait for async status checks |
