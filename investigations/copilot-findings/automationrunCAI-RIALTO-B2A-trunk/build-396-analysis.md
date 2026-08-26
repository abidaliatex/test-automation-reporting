# Build 396 — Root Cause Analysis

**Source Report:** [build-396.md](../../reports/build-failures/automationrunCAI-RIALTO-B2A-trunk/build-396.md)

---

## Build Summary

Build: automationrunCAI-RIALTO-B2A-trunk #396
Total Tests: 17
Passed: 14
Failed: 3
Pass Rate: 82.4%

---

## Root Cause Groups

## Numeric Value Mismatch — Pricing / Financial Calculations

**Affected Features:**
- rialtoB2A(CASS).feature

**Affected Scenarios:**
- Returns StoreStatus of Order (tc_getRialtoB2A05)
- Calculate price for self service (tc_postRialtoB2A03)

**Failure Pattern:**
Expected numeric values differ from actuals — amounts appear to be off by a factor (e.g., `44696.29` vs `89392.58`, suggesting a ×2 difference; `276757.2` vs `369009.6` at list element [3]).

**Evidence:**
- `tc_getRialtoB2A05`: `Iterators differ at element [3]: 276757.2 != 369009.6 expected [276757.2] but found [369009.6]`
- `tc_postRialtoB2A03`: `expected [[89392.58, 89392.58]] but found [[44696.29, 44696.29]]`

**Impact:** 2 failures

**Confidence:** High

---

## Wrong HTTP Status Code — Order Update Response

**Affected Features:**
- rialtoB2A(CASS).feature

**Affected Scenarios:**
- Returns StoreStatus of Update Order (tc_getRialtoB2A06)

**Failure Pattern:**
GET request after an order update returns HTTP `N202` (Accepted/async) instead of expected `N200` (OK), possibly indicating the backend processes the update asynchronously and the subsequent GET is issued before the update is committed.

**Evidence:**
- `tc_getRialtoB2A06`: `expected [N200] but found [N202]` at `User verify the status code "Response Code"` (line 111)
- All downstream response-body assertions were skipped as a consequence.

**Impact:** 1 failure

**Confidence:** Medium

---

## Summary

All 3 failures have been ongoing since build 231 and are rooted in backend data discrepancies:
- Pricing/calculation endpoints return values that do not match test expectations (possibly due to a pricing-rule or discount-factor change in the backend).
- The order-update GET endpoint returns an intermediate `202` instead of a final `200`, suggesting a timing or async-processing issue.
