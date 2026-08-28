# Build 398 — Root Cause Analysis

**Source Report:** [build-398.md](../../../reports/build-failures/automationrunCAI-RIALTO-B2A-trunk/build-398.md)

---

## Build Summary

**Build:** 398
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

---

## Summary

- **Root Cause:** Pricing/amount values returned by the CASS API do not match expected values. The `tc_postRialtoB2A03` case shows the actual is exactly 50% of expected (`44696.29` vs `89392.58`), suggesting a possible halving bug (e.g. double-counting a divisor, or a 50% discount applied unexpectedly). `tc_getRialtoB2A05` shows a ~33% inflation of the actual vs expected amount.
- **Affected Components:** CASS pricing/order-value calculation endpoints.
- **Recommended Fix:** Investigate pricing logic changes introduced around build 231. Check for changes to discount, tax, or quantity multiplier logic in the CASS service.
- **Prevention:** Add contract/value-range assertions for pricing fields to catch regressions early.
