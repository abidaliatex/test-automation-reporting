# Build 370 — Root Cause Analysis

**Source Report:** [build-370.md](../../reports/build-failures/automationrunCAI-RIALTO-B2A-trunk/build-370.md)
**Job:** automationrunCAI-RIALTO-B2A-trunk
**Date:** 2026-08-12

---

## Build Summary

Build: 370
Total Tests: 17
Passed: 14
Failed: 3
Pass Rate: 82.4%

---

## Root Cause Groups

## Incorrect Pricing / Monetary Value Calculations

**Affected Features:**
- rialtoB2A(CASS).feature

**Affected Scenarios:**
- Returns StoreStatus of Order (tc_getRialtoB2A05)
- Calculate price for self service (tc_postRialtoB2A03)

**Failure Pattern:**
Response body numeric values do not match expected — actual values differ by approximately 25–50% from expected, suggesting a pricing multiplier or discount factor is applied differently on the server side.

**Evidence:**
- `tc_getRialtoB2A05`: `expected [276757.2] but found [369009.6]` — actual is ~33% higher than expected (element [3] of response array)
- `tc_postRialtoB2A03`: `expected [[89392.58, 89392.58]] but found [[44696.29, 44696.29]]` — actual is exactly 50% of expected, possibly a discount rate change (e.g., 100% → 50%)

**Impact:** 2 failures

**Confidence:** High

---

## Unexpected HTTP Status Code on Order Update

**Affected Features:**
- rialtoB2A(CASS).feature

**Affected Scenarios:**
- Returns StoreStatus of Update Order (tc_getRialtoB2A06)

**Failure Pattern:**
GET after PATCH returns HTTP `N202` (Accepted / async processing) instead of expected `N200` (OK), indicating the server now processes the update asynchronously and the test does not wait long enough before polling.

**Evidence:**
- `tc_getRialtoB2A06`: `expected [N200] but found [N202]` at step `User verify the status code "Response Code"` (feature line 111)
- All downstream steps (response body checks) are skipped as a result

**Impact:** 1 failure

**Confidence:** High

---

## Summary

| Section | Detail |
|---|---|
| **Root Cause** | Server-side pricing/calculation logic change and async order-update response behaviour |
| **Affected Components** | Rialto B2A CASS API — StoreStatus endpoint, Calculate Price endpoint, Update Order endpoint |
| **Failing Since** | Build 231 (all 3 failures are persistent regressions) |
| **Recommended Fix** | 1. Align test expected values for tc_getRialtoB2A05 and tc_postRialtoB2A03 with the current server computation, or fix the server-side pricing logic if it regressed. 2. For tc_getRialtoB2A06, add a wait/retry step after PATCH before the GET, or update the expected status code to accept `N202`. |
| **Prevention** | Pin expected response values to a versioned contract; add server-side changelog review step to automation pipeline when pricing logic changes. |
