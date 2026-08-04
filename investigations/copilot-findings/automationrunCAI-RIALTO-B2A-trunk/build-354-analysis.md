# Build 354 — Root Cause Analysis

**Source Report:** [build-354.md](../../reports/build-failures/automationrunCAI-RIALTO-B2A-trunk/build-354.md)

---

## Build Summary

Build: 354
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
Numeric monetary values returned by the API differ from expected test data. The actual values are consistently ~half or ~1.33× of the expected values, suggesting a calculation factor change (e.g. pricing multiplier, tax rate, or currency conversion).

**Evidence:**
- `tc_getRialtoB2A05`: `expected [276757.2] but found [369009.6]` — actual is ~1.33× expected
- `tc_postRialtoB2A03`: `expected [[89392.58, 89392.58]] but found [[44696.29, 44696.29]]` — actual is ~0.5× expected
- Both failures started at **Build 231** and have persisted to this build (age: 124 builds)
- Failures are isolated to price/monetary response body assertions; all other steps (status code, non-null checks, partial string, boolean) pass

**Impact:** 2 failures

**Confidence:** High

---

## Summary

- **Root Cause:** API response values for price/monetary fields diverge from expected test data. This is a long-standing regression since build 231 — possibly caused by a backend pricing calculation change (multiplier, discount factor, or VAT handling) that was never reflected in the test expectations.
- **Root Cause:** Possibly a server-side pricing logic change not synced with test fixture data.
- **Affected Components:** `rialtoB2A(CASS).feature`, `getRialtoB2A.csv` (tc_getRialtoB2A05), `postRialtoB2A.csv` (tc_postRialtoB2A03)
- **Recommended Fix:** Compare the expected values in the CSV test data files against the current API behaviour and update test expectations to reflect the correct pricing logic, or revert the backend change if unintentional.
- **Prevention:** Add alerting for price-related assertion failures so regressions are caught within the same build they are introduced.
