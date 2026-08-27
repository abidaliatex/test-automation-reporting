# Investigation Analysis — Build 397

**Source Report:** [build-397.md](../../../reports/build-failures/automationrunCAI-RIALTO-B2A-trunk/build-397.md)

---

## Build Summary

| Build | Total Tests | Passed | Failed | Pass Rate |
|---|---|---|---|---|
| 397 | 17 | 15 | 2 | 88.2% |

---

## Root Cause Groups

## Numeric Value Mismatch in Response Body Assertions

**Affected Features:**
- rialtoB2A(CASS).feature

**Affected Scenarios:**
- Returns StoreStatus of Order (tc_getRialtoB2A05)
- Calculate price for self service (tc_postRialtoB2A03)

**Failure Pattern:**
Response body numeric fields return values that differ from expected — likely a pricing/calculation logic change on the server side.

**Evidence:**
- `tc_getRialtoB2A05`: `Iterators differ at element [3]: 276757.2 != 369009.6 expected [276757.2] but found [369009.6]`
- `tc_postRialtoB2A03`: `expected [[89392.58, 89392.58]] but found [[44696.29, 44696.29]]` — actual values are approximately half of expected (89392.58 / 2 ≈ 44696.29), suggesting a possible pricing factor or multiplier change

**Impact:** 2 failures

**Confidence:** High

---

## Summary

Both failures are numeric assertion mismatches in calculated/pricing fields. The values returned by the API differ from the hardcoded expected values in the test data files (`getRialtoB2A.csv`, `postRialtoB2A.csv`). Both tests have been failing since build 231, indicating a persistent divergence between the test expectations and the current application behaviour.

## Root Cause

API response returns different numeric values (prices/amounts) than those recorded in the test CSV data. The `tc_postRialtoB2A03` discrepancy (actual ≈ 50% of expected) possibly points to a pricing factor, rate, or multiplier change in the backend.

## Affected Components

- `rialtoB2A(CASS).feature` — test scenarios for B2A CASS API
- `Rialto/RialtoB2A/getRialtoB2A.csv` — expected response data for GET endpoints
- `Rialto/RialtoB2A/postRialtoB2A.csv` — expected response data for POST endpoints
- `stepDefinition.ApiStepDefinition` — response body comparison logic

## Recommended Fix

- Verify whether the pricing/calculation logic changed in the backend since build 231.
- If the new values are correct, update the expected values in the CSV test data files.
- If the old values are correct, investigate backend regression.

## Prevention

- Review test data CSV files whenever pricing or calculation logic changes are deployed.
- Consider parameterising price-sensitive assertions or using tolerance-based comparisons for floating-point values.
