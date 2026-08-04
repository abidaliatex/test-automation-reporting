# Build 355 — Root Cause Analysis

**Source Report:** [build-355.md](../../reports/build-failures/automationrunCAI-RIALTO-B2A-trunk/build-355.md)

---

## Build Summary

Build: 355 — automationrunCAI-RIALTO-B2A-trunk
Total Tests: 17
Passed: 15
Failed: 2
Pass Rate: 88.2%

---

## Root Cause Groups

## Incorrect Numeric Values in API Responses

**Affected Features:**
- rialtoB2A(CASS).feature

**Affected Scenarios:**
- Returns StoreStatus of Order (tc_getRialtoB2A05)
- Calculate price for self service (tc_postRialtoB2A03)

**Failure Pattern:**
Response body returns numeric values that do not match expected test data — values appear to be approximately halved or scaled differently than expected.

**Evidence:**
- `tc_getRialtoB2A05`: `expected [276757.2] but found [369009.6]` at element [3] in response body comparison (`JSONManager.compareJSONStrings`)
- `tc_postRialtoB2A03`: `expected [[89392.58, 89392.58]] but found [[44696.29, 44696.29]]` — actual values are exactly half the expected values

**Impact:** 2 failures

**Confidence:** High

---

## Summary

- **Root Cause:** Numeric price/value fields in API responses differ from test expectations. The pattern of values being halved (89392.58 → 44696.29) suggests a possible pricing calculation change or data/configuration mismatch on the server side.
- **Affected Components:** B2A order/pricing endpoints (`getRialtoB2A`, `postRialtoB2A`)
- **Recommended Fix:** Verify whether a pricing calculation rule or rate configuration has changed since build 231 (when failures first appeared). Update test data CSV expectations (`getRialtoB2A.csv`, `postRialtoB2A.csv`) if the new values are intentional.
- **Prevention:** Add change-detection alerts for pricing configuration changes that could affect expected test values.
