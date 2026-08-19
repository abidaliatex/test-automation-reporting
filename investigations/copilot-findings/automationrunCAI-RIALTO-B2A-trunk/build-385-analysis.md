# Build 385 — Root Cause Analysis

**Source Report:** [build-385.md](../../reports/build-failures/automationrunCAI-RIALTO-B2A-trunk/build-385.md)

---

## Build Summary

**Build:** 385
**Total Tests:** 17
**Passed:** 14
**Failed:** 3
**Pass Rate:** 82.4%

---

## Root Cause Groups

---

## Incorrect Pricing / Monetary Value Calculations

**Affected Features:**
- rialtoB2A(CASS).feature

**Affected Scenarios:**
- Returns StoreStatus of Order (tc_getRialtoB2A05)
- Calculate price for self service (tc_postRialtoB2A03)

**Failure Pattern:**
Response body fields contain numeric values that differ from expected — prices or totals returned by the API are approximately half or differ from expected amounts.

**Evidence:**
- `tc_getRialtoB2A05`: `Iterators differ at element [3]: 276757.2 != 369009.6 expected [276757.2] but found [369009.6]`
- `tc_postRialtoB2A03`: `expected [[89392.58, 89392.58]] but found [[44696.29, 44696.29]]` — returned values are exactly half of expected (44696.29 × 2 = 89392.58)

**Impact:** 2 failures

**Confidence:** High

---

## Wrong HTTP Status Code on Order Update

**Affected Features:**
- rialtoB2A(CASS).feature

**Affected Scenarios:**
- Returns StoreStatus of Update Order (tc_getRialtoB2A06)

**Failure Pattern:**
GET request for updated order status returns HTTP `N202` (Accepted/async) instead of expected `N200` (OK), possibly indicating asynchronous processing is not completing before the assertion is made.

**Evidence:**
- `tc_getRialtoB2A06`: `expected [N200] but found [N202]` at step `User verify the status code "Response Code"`

**Impact:** 1 failure

**Confidence:** High

---

## Summary

- **Root Cause:** All 3 failures have been persistent since build 231, indicating a regression introduced at or before that build that has not been resolved.
- **Affected Components:** B2A CASS API — order status retrieval and price calculation endpoints.
- **Recommended Fix:** Investigate the pricing calculation logic change introduced around build 231 (possibly a discount factor, currency conversion, or quantity multiplier change). For tc_getRialtoB2A06, verify whether the PATCH order endpoint now processes asynchronously and introduce a wait/poll step before the GET status check.
- **Prevention:** Add contract tests for pricing fields to detect calculation regressions early.
