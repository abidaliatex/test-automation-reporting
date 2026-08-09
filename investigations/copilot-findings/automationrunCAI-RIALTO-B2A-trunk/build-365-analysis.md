# Build 365 — Root Cause Analysis

**Source Report:** [build-365.md](../../reports/build-failures/automationrunCAI-RIALTO-B2A-trunk/build-365.md)
**Job:** automationrunCAI-RIALTO-B2A-trunk
**Date:** 2026-08-09
**Build Result:** UNSTABLE

---

## Build Summary

Build: 365
Total Tests: 17
Passed: 14
Failed: 3
Pass Rate: 82.4%

---

## Root Cause Groups

---

## Numeric Value Mismatch — Price / Amount Calculations

**Affected Features:**
- rialtoB2A(CASS).feature

**Affected Scenarios:**
- Returns StoreStatus of Order (tc_getRialtoB2A05)
- Calculate price for self service (tc_postRialtoB2A03)

**Failure Pattern:**
Response body numeric fields do not match expected values — actual values differ significantly (roughly ×0.5 or ×1.33 of expected), suggesting a pricing multiplier, currency conversion factor, or discount calculation has changed on the server side.

**Evidence:**
- `tc_getRialtoB2A05`: `expected [276757.2] but found [369009.6]` (element [3] of response array — ratio ≈ 1.33)
- `tc_postRialtoB2A03`: `expected [[89392.58, 89392.58]] but found [[44696.29, 44696.29]]` (exactly half the expected values — ratio = 0.5)

**Impact:** 2 failures

**Confidence:** High

---

## Unexpected HTTP Status Code — Order Update Response

**Affected Features:**
- rialtoB2A(CASS).feature

**Affected Scenarios:**
- Returns StoreStatus of Update Order (tc_getRialtoB2A06)

**Failure Pattern:**
GET request for an updated order returns HTTP `N202` (Accepted / async processing) where `N200` (OK) is expected. Possibly the PATCH update (tc_patchRialtoB2A01) is now processed asynchronously and the subsequent GET is called before the order reaches final state.

**Evidence:**
- `tc_getRialtoB2A06`: `expected [N200] but found [N202]` at `user_verify_the_status_code` (line 111)
- The preceding `tc_patchRialtoB2A01` (Update ad/Order) still passes; only the subsequent status-check GET fails.

**Impact:** 1 failure

**Confidence:** Medium

---

## Summary

All 3 failures have been present since **build 231** (age ≥ 135 builds), indicating a persistent regression introduced at that point rather than a fluke.

**Root Cause:** Server-side behavioural change (pricing logic and/or async order processing) introduced around build 231 that was never corrected in test data or system configuration.

**Recommended Fix:** Update expected test data in `getRialtoB2A.csv` and `postRialtoB2A.csv` to reflect current system output, OR raise a defect against the back-end service if the new values are incorrect business logic.

**Prevention:** Add tolerance/delta assertions for floating-point price fields; add a polling/retry step for order status after PATCH to handle async `N202` responses.
