# Build 357 — Root Cause Analysis

**Source Report:** [build-357.md](../../reports/build-failures/automationrunCAI-RIALTO-B2A-trunk/build-357.md)
**Job:** automationrunCAI-RIALTO-B2A-trunk
**Date:** 2026-08-05

---

## Build Summary

Build: 357
Total Tests: 17
Passed: 15
Failed: 2
Pass Rate: 88.2%

---

## Root Cause Groups

## Pricing / Monetary Value Mismatch

**Affected Features:**
- rialtoB2A(CASS).feature

**Affected Scenarios:**
- Returns StoreStatus of Order (tc_getRialtoB2A05)
- Calculate price for self service (tc_postRialtoB2A03)

**Failure Pattern:**
Numeric monetary values returned by the API do not match expected test data. Actual values are approximately half (or a different ratio) of what is expected.

**Evidence:**
- `tc_getRialtoB2A05`: `expected [276757.2] but found [369009.6]` at response body element [3]
- `tc_postRialtoB2A03`: `expected [[89392.58, 89392.58]] but found [[44696.29, 44696.29]]` — actual values are exactly half of expected

**Impact:** 2 failures

**Confidence:** High

---

## Summary

- Both failures have been failing since **build 231**, indicating a persistent regression rather than a transient flake.
- The `tc_postRialtoB2A03` discrepancy (values exactly halved: 89392.58 → 44696.29) suggests a possible pricing calculation logic change or a tax/discount factor being applied or removed.
- The `tc_getRialtoB2A05` discrepancy (276757.2 vs 369009.6, ratio ≈ 0.75) may indicate a different pricing rule or rounding applied to the stored order status response.
- Test data in `getRialtoB2A.csv` and `postRialtoB2A.csv` may need to be updated to reflect current API behavior, or the API pricing logic requires investigation.
