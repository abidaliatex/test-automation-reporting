# Build 399 — Root Cause Analysis

**Source Report:** [build-399.md](../../../reports/build-failures/automationrunCAI-RIALTO-B2A-trunk/build-399.md)

---

## Build Summary

**Build:** 399
**Total Tests:** 17
**Passed:** 15
**Failed:** 2
**Pass Rate:** 88.2%

---

## Root Cause Groups

## Incorrect Pricing / Monetary Value Mismatch

**Affected Features:**
- rialtoB2A(CASS).feature

**Affected Scenarios:**
- Returns StoreStatus of Order (tc_getRialtoB2A05)
- Calculate price for self service (tc_postRialtoB2A03)

**Failure Pattern:**
Response body contains numeric values (prices/amounts) that differ from expected — actual values are approximately half or a different ratio of expected values.

**Evidence:**
- `tc_getRialtoB2A05`: `expected [276757.2] but found [369009.6]` at element [3] of response body iterator
- `tc_postRialtoB2A03`: `expected [[89392.58, 89392.58]] but found [[44696.29, 44696.29]]` — actual values are exactly half of expected

**Impact:** 2 failures (both failing since build 231)

**Confidence:** High — both failures share the same root pattern (price/amount field mismatch), have been persistent since build 231, and point to a pricing calculation or data discrepancy in the CASS backend.
