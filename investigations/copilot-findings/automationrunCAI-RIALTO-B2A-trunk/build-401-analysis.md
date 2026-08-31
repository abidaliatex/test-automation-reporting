# Build 401 — Root Cause Analysis

**Report:** [build-401.md](../../../reports/build-failures/automationrunCAI-RIALTO-B2A-trunk/build-401.md)
**Job:** automationrunCAI-RIALTO-B2A-trunk
**Date:** 2026-08-31

---

## Build Summary

**Build:** 401
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
Numeric monetary values returned by the API do not match expected values — amounts appear to be halved or differently scaled (e.g. `44696.29` found instead of `89392.58`, `369009.6` found instead of `276757.2`).

**Evidence:**
- `tc_getRialtoB2A05`: `Iterators differ at element [3]: 276757.2 != 369009.6 expected [276757.2] but found [369009.6]`
- `tc_postRialtoB2A03`: `expected [[89392.58, 89392.58]] but found [[44696.29, 44696.29]]` — returned values are exactly half of expected

**Impact:** 2 failures

**Confidence:** High

---

## Summary

| Root Cause | Failures | Confidence |
|---|---|---|
| Incorrect Pricing / Monetary Value Mismatch | 2 | High |

Both failures have been present since build 231, indicating a persistent regression in price calculation or response mapping logic in the CASS B2A integration. The `tc_postRialtoB2A03` values are exactly 50% of expected, suggesting a possible division-by-two bug in price computation. The `tc_getRialtoB2A05` mismatch may be a related rounding or aggregation issue in the StoreStatus response.
