# Build 366 — Root Cause Analysis

**Source Report:** [build-366.md](../../../reports/build-failures/automationrunCAI-RIALTO-B2A-trunk/build-366.md)

---

## Build Summary

**Build:** 366
**Total Tests:** 17
**Passed:** 15
**Failed:** 2
**Pass Rate:** 88.2%

---

## Root Cause Groups

## Incorrect Pricing / Financial Value Mismatch

**Affected Features:**
- rialtoB2A(CASS).feature

**Affected Scenarios:**
- Returns StoreStatus of Order (tc_getRialtoB2A05)
- Calculate price for self service (tc_postRialtoB2A03)

**Failure Pattern:**
Numerical field values returned by the API do not match expected values — amounts appear to be approximately halved or recalculated with different rates.

**Evidence:**
- `tc_getRialtoB2A05`: `Iterators differ at element [3]: 276757.2 != 369009.6 expected [276757.2] but found [369009.6]`
- `tc_postRialtoB2A03`: `expected [[89392.58, 89392.58]] but found [[44696.29, 44696.29]]` — returned value is exactly half of expected

**Impact:** 2 failures

**Confidence:** High

---

## Summary

- Both failures are **persistent since build 231**, indicating a long-standing data or pricing logic mismatch between the API response and expected test values.
- `tc_postRialtoB2A03` shows the returned value is exactly 50% of expected (`44696.29` vs `89392.58`), possibly pointing to a factor-of-2 error in price calculation (e.g. per-unit vs per-pair pricing).
- `tc_getRialtoB2A05` shows an order status amount discrepancy (~33% higher than expected), possibly due to a tax, fee, or multiplier being applied inconsistently.
- No new failures introduced in build 366 compared to build 365 (`tc_getRialtoB2A06` which failed in 365 is now passing).
