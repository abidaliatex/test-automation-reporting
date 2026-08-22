# Build Analysis — automationrunCAI-RIALTO-B2A-trunk #389

**Source Report:** [build-389.md](../../reports/build-failures/automationrunCAI-RIALTO-B2A-trunk/build-389.md)

---

## Build Summary

| Field | Value |
|---|---|
| Build | automationrunCAI-RIALTO-B2A-trunk #389 |
| Total Tests | 17 |
| Passed | 15 |
| Failed | 2 |
| Pass Rate | 88.2% |

---

## Root Cause Groups

## Incorrect Numeric Values in Response Body (Price / Financial Calculations)

**Affected Features:**
- `rialtoB2A(CASS).feature`

**Affected Scenarios:**
- Returns StoreStatus of Order (tc_getRialtoB2A05)
- Calculate price for self service (tc_postRialtoB2A03)

**Failure Pattern:**
Response body fields contain numeric values that differ from expected. The actual values appear to be approximately half (or different multiples) of the expected values, suggesting a pricing/calculation factor change in the backend.

**Evidence:**
- `tc_getRialtoB2A05`: `expected [276757.2] but found [369009.6]` — element [3] of response body iterator differs
- `tc_postRialtoB2A03`: `expected [[89392.58, 89392.58]] but found [[44696.29, 44696.29]]` — actual values are exactly half of expected (44696.29 × 2 = 89392.58)
- Both failures originate from `ApiStepDefinition.java` response body assertion logic
- Both tests have been failing since build 231 (age: 159 builds) — long-standing regression, test data or backend pricing logic may have changed at that point

**Impact:** 2 failures

**Confidence:** High
