# Build 381 — Root Cause Analysis

**Source Report:** [build-381.md](../../reports/build-failures/automationrunCAI-RIALTO-B2A-trunk/build-381.md)

---

## Build Summary

Build: 381
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
Numeric monetary values returned by the API differ from expected test data. The actual values appear to be approximately half or 1.33× the expected values, suggesting a pricing calculation change (e.g. rate multiplier, discount factor, or currency/unit change) on the server side.

**Evidence:**
- `tc_getRialtoB2A05`: `expected [276757.2] but found [369009.6]` (index [3] in response body — found is ~1.33× expected)
- `tc_postRialtoB2A03`: `expected [[89392.58, 89392.58]] but found [[44696.29, 44696.29]]` (found is ~0.5× expected — possibly a 50% discount or factor-of-2 divisor introduced)

**Impact:** 2 failures

**Confidence:** High — both failures are pure numeric assertion mismatches on price/cost fields, consistently reproducible (age: 151 builds, failing since build 231). No infrastructure or connectivity errors present.

---

## Summary

- **Root Cause:** API response pricing values do not match test expectations. Both failures point to a backend pricing/calculation change that has been present since build 231.
- **Affected Components:** Rialto B2A CASS pricing and store-status endpoints.
- **Recommended Fix:** Update expected values in `getRialtoB2A.csv` (tc_getRialtoB2A05) and `postRialtoB2A.csv` (tc_postRialtoB2A03) to reflect current backend behaviour, or revert the backend pricing change if it is unintentional.
- **Prevention:** Add contract tests or snapshot tests for pricing fields to catch calculation changes earlier.
