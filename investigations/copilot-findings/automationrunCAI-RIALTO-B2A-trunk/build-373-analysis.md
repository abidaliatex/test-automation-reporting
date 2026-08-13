# Build 373 — Root Cause Analysis

**Job:** automationrunCAI-RIALTO-B2A-trunk
**Report:** [build-373.md](../../reports/build-failures/automationrunCAI-RIALTO-B2A-trunk/build-373.md)

---

## Build Summary

Build: 373
Total Tests: 17
Passed: 14
Failed: 3
Pass Rate: 82.4%

---

## Root Cause Groups

## Incorrect Pricing / Numeric Value Mismatch

**Affected Features:**
- rialtoB2A(CASS).feature

**Affected Scenarios:**
- Returns StoreStatus of Order (tc_getRialtoB2A05)
- Calculate price for self service (tc_postRialtoB2A03)

**Failure Pattern:**
Response body numeric values do not match expected — actual values differ by approximately 50% or a consistent offset from expected.

**Evidence:**
- `tc_getRialtoB2A05`: `expected [276757.2] but found [369009.6]` (element [3] of response body list)
- `tc_postRialtoB2A03`: `expected [[89392.58, 89392.58]] but found [[44696.29, 44696.29]]` — actual is exactly half the expected value

**Impact:** 2 failures

**Confidence:** High

---

## Unexpected HTTP Status Code on Updated Order Retrieval

**Affected Features:**
- rialtoB2A(CASS).feature

**Affected Scenarios:**
- Returns StoreStatus of Update Order (tc_getRialtoB2A06)

**Failure Pattern:**
GET request for updated order returns HTTP N202 (Accepted/async) instead of expected N200 (OK), suggesting the order update is not yet fully committed when the status check is performed.

**Evidence:**
- `tc_getRialtoB2A06`: `expected [N200] but found [N202]` at status code verification step
- This test depends on `tc_patchRialtoB2A01` (Update ad/Order); the update may be processed asynchronously and the 10-second wait may be insufficient

**Impact:** 1 failure

**Confidence:** Medium

---

## Summary

- All 3 failures have been present since build 231 (143 builds).
- The pricing mismatches (tc_getRialtoB2A05, tc_postRialtoB2A03) suggest a persistent data or calculation regression in the CASS pricing/store-status logic.
- The N202 status (tc_getRialtoB2A06) indicates either an async processing delay or a change in the PATCH endpoint's response contract.
