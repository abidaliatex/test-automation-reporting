# Build 393 — Root Cause Analysis

**Source Report:** [build-393.md](../../reports/build-failures/automationrunCAI-RIALTO-B2A-trunk/build-393.md)

---

## Build Summary

**Build:** 393
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
Numeric price/cost fields returned by the API do not match expected values. The actual values are consistently lower than expected (roughly 50% or different ratio), suggesting a pricing calculation regression.

**Evidence:**
- `tc_getRialtoB2A05`: `expected [276757.2] but found [369009.6]` — element [3] of response body array differs
- `tc_postRialtoB2A03`: `expected [[89392.58, 89392.58]] but found [[44696.29, 44696.29]]` — returned values are exactly half of expected

**Impact:** 2 failures

**Confidence:** High

---

## Summary

- **Root Cause:** API pricing/calculation logic returning incorrect monetary values. The `tc_postRialtoB2A03` discrepancy (values halved) strongly suggests a divisor or multiplier bug in the price calculation endpoint. The `tc_getRialtoB2A05` mismatch may be a related propagation of a stale or incorrect order total.
- **Affected Components:** Rialto B2A pricing/order endpoints (`postRialtoB2A`, `getRialtoB2A`)
- **Recommended Fix:** Investigate pricing calculation logic changes since build 231 (when failures first appeared). Focus on the `/calculate` endpoint and any order totalling logic.
- **Prevention:** Add contract/snapshot tests for pricing endpoints to detect value regressions early.
