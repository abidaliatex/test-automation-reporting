# Investigation: automationrunCAI-RIALTO-B2A-trunk — Build 392

**Source Report:** [build-392.md](../../reports/build-failures/automationrunCAI-RIALTO-B2A-trunk/build-392.md)

---

## Build Summary

| Field | Value |
|---|---|
| Build | 392 |
| Date | 2026-08-24 |
| Status | UNSTABLE |
| Total Tests | 17 |
| Passed | 15 |
| Failed | 2 |
| Pass Rate | 88.2% |

---

## Root Cause Groups

### Incorrect Numeric Values in Response Body

**Affected Features:**
- rialtoB2A(CASS).feature

**Affected Scenarios:**
- Returns StoreStatus of Order (tc_getRialtoB2A05)
- Calculate price for self service (tc_postRialtoB2A03)

**Failure Pattern:**
Response body numeric fields return values that differ from expected — the actual values appear to be either approximately half or different ratios of expected values, suggesting a pricing/calculation logic change on the backend (e.g. a rate or multiplier changed).

- `tc_getRialtoB2A05`: expected `276757.2` at element [3], found `369009.6` (~1.33× ratio)
- `tc_postRialtoB2A03`: expected `[89392.58, 89392.58]`, found `[44696.29, 44696.29]` (exactly 0.5× ratio — possibly a divisor bug or rate halved)

**Evidence:**
- `Iterators differ at element [3]: 276757.2 != 369009.6 expected [276757.2] but found [369009.6]` — `JSONManager.compareJSONStrings` at `ApiStepDefinition.java:357`
- `expected [[89392.58, 89392.58]] but found [[44696.29, 44696.29]]` — `ApiStepDefinition.user_verify_the_response_body_fields` at `ApiStepDefinition.java:609`
- Both failures have been present since build 231 (age: 162 builds), indicating a persistent regression introduced at that point.

**Impact:** 2 failures

**Confidence:** High

---

## Summary

- **Root Cause:** Backend pricing/calculation values have changed since build 231. Test data expectations no longer match the values returned by the API.
- **Recommended Fix:** Verify whether the backend rate/multiplier change is intentional. If intentional, update the expected values in `getRialtoB2A.csv` (tc_getRialtoB2A05) and `postRialtoB2A.csv` (tc_postRialtoB2A03). If unintentional, revert the backend change.
- **Prevention:** Add tolerance checks or parameterise expected values from a config rather than hardcoding, to catch such regressions earlier.
