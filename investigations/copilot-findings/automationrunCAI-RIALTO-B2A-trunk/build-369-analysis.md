# Build 369 — Root Cause Analysis

**Source Report:** [build-369.md](../../../reports/build-failures/automationrunCAI-RIALTO-B2A-trunk/build-369.md)

---

## Build Summary

**Build:** 369
**Total Tests:** 17
**Passed:** 15
**Failed:** 2
**Pass Rate:** 88.2%

---

## Root Cause Groups

## Numeric Value Mismatch — Price / Amount Calculation

**Affected Features:**
- rialtoB2A(CASS).feature

**Affected Scenarios:**
- Returns StoreStatus of Order (tc_getRialtoB2A05)
- Calculate price for self service (tc_postRialtoB2A03)

**Failure Pattern:**
Response body numeric values do not match expected values — actual values differ by a consistent ratio (~0.5× or ~1.33×), suggesting a pricing rule, currency multiplier, or discount factor has changed.

**Evidence:**
- `tc_getRialtoB2A05`: `expected [276757.2] but found [369009.6]` — actual is ~1.334× expected
- `tc_postRialtoB2A03`: `expected [[89392.58, 89392.58]] but found [[44696.29, 44696.29]]` — actual is ~0.5× expected (possibly a halving of price)
- Both failures have been present since **build 231** — persistent regression, not a flake
- Stack traces point to `JSONManager.compareJSONStrings` and `ApiStepDefinition.user_verify_the_response_body` / `user_verify_the_response_body_fields`

**Impact:** 2 failures

**Confidence:** High

---

## Summary

Both failures are numeric assertion mismatches on calculated monetary/price fields. The consistent directional drift (one ~33% higher, one ~50% lower) since build 231 suggests a backend pricing or discount calculation change introduced at that build that altered the values returned by the CASS API. Test data / expected values in the CSV files (`getRialtoB2A.csv`, `postRialtoB2A.csv`) have not been updated to reflect the new values.

## Root Cause

Backend pricing logic change (possibly a discount factor or rounding rule update) introduced around build 231 caused the API to return different numeric values than what the test CSV fixtures expect.

## Affected Components

- `rialto-cai/src/test/resources/features/rialtoB2A(CASS).feature` (lines 64, 155)
- `Rialto/RialtoB2A/getRialtoB2A.csv` — expected values for tc_getRialtoB2A05
- `Rialto/RialtoB2A/postRialtoB2A.csv` — expected values for tc_postRialtoB2A03
- `stepDefinition.ApiStepDefinition` (JSONManager comparison logic)

## Recommended Fix

Update the expected values in `getRialtoB2A.csv` (tc_getRialtoB2A05) and `postRialtoB2A.csv` (tc_postRialtoB2A03) to match the current API responses, after confirming the new values are intentional and correct.

## Prevention

- When backend pricing logic changes, update test fixture CSV files in the same commit/PR to keep them in sync.
- Add a contract test or changelog step that flags when price-calculation endpoints return values outside a tolerance of the stored expected values.
