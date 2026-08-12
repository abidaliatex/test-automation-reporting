# Build 371 — Root Cause Analysis

**Source Report:** [build-371.md](../../reports/build-failures/automationrunCAI-RIALTO-B2A-trunk/build-371.md)
**Job:** automationrunCAI-RIALTO-B2A-trunk
**Date:** 2026-08-12

---

## Build Summary

Build: 371
Total Tests: 17
Passed: 15
Failed: 2
Pass Rate: 88.2%

---

## Root Cause Groups

## Numeric Value Mismatch in Pricing / Financial Fields

**Affected Features:**
- rialtoB2A(CASS).feature

**Affected Scenarios:**
- Returns StoreStatus of Order (tc_getRialtoB2A05)
- Calculate price for self service (tc_postRialtoB2A03)

**Failure Pattern:**
Response body numeric values do not match expected — actual values are either doubled or halved relative to expected:
- `expected [276757.2] but found [369009.6]` (element [3] of response body array)
- `expected [[89392.58, 89392.58]] but found [[44696.29, 44696.29]]` (price fields — actual is ~50% of expected)

**Evidence:**
- tc_getRialtoB2A05: iterator element [3] differs: 276757.2 (expected) vs 369009.6 (actual) — ratio ~1.33×
- tc_postRialtoB2A03: price field [89392.58, 89392.58] expected vs [44696.29, 44696.29] found — actual is exactly 50% of expected, possibly a factor-of-2 calculation regression
- Both failures have `failedSince: 231` and `age: 141`, indicating a persistent regression introduced around build 231

**Impact:** 2 failures

**Confidence:** High

---

## Summary

Both failing tests assert on numeric pricing/financial values returned by the RIALTO B2A API. The consistent ratio discrepancy (50% and ~75%) strongly suggests a pricing calculation change or misconfiguration introduced at or before build 231, and still unresolved. Not a flaky/transient issue.

## Root Cause

Pricing calculation regression in the RIALTO B2A service — possibly a changed multiplier, rate, or formula applied to order cost fields. The failure has persisted for 141 consecutive builds since build 231.

## Affected Components

- `rialtoB2A(CASS).feature` — scenarios `tc_getRialtoB2A05` and `tc_postRialtoB2A03`
- `stepDefinition.ApiStepDefinition` — `user_verify_the_response_body` and `user_verify_the_response_body_fields`
- `utility.JSONManager.compareJSONStrings`
- Endpoint under test: RIALTO B2A order/pricing APIs

## Recommended Fix

- Investigate the pricing/calculation logic change deployed around build 231.
- Update test expected values if the new pricing is intentional, or revert the backend change if it is a regression.

## Prevention

- Add price-field contract tests that alert on ratio changes above a threshold.
- Require explicit sign-off when expected values change in test data files.
