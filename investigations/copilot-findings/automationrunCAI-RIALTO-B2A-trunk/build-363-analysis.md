# Build 363 — Root Cause Analysis

**Job:** automationrunCAI-RIALTO-B2A-trunk
**Report:** [build-363.md](../../reports/build-failures/automationrunCAI-RIALTO-B2A-trunk/build-363.md)
**Date:** 2026-08-08
**Status:** UNSTABLE

---

## Build Summary

Build: 363
Total Tests: 17
Passed: 14
Failed: 3
Pass Rate: 82.4%

---

## Root Cause Groups

## Pricing / Amount Value Mismatch

**Affected Features:**
- rialtoB2A(CASS).feature

**Affected Scenarios:**
- Returns StoreStatus of Order (tc_getRialtoB2A05)
- Calculate price for self service (tc_postRialtoB2A03)

**Failure Pattern:**
Response body contains different numeric values than expected — amounts are either halved or otherwise recalculated differently by the backend.

**Evidence:**
- `tc_getRialtoB2A05`: `expected [276757.2] but found [369009.6]` (element [3] of response body iterator)
- `tc_postRialtoB2A03`: `expected [[89392.58, 89392.58]] but found [[44696.29, 44696.29]]` — returned values are exactly half of expected (44696.29 × 2 = 89392.58)

**Impact:** 2 failures

**Confidence:** High

---

## Status Code Mismatch — PATCH Update Order

**Affected Features:**
- rialtoB2A(CASS).feature

**Affected Scenarios:**
- Returns StoreStatus of Update Order (tc_getRialtoB2A06)

**Failure Pattern:**
GET request after PATCH (update order) returns HTTP status `N202` instead of expected `N200`.

**Evidence:**
- `tc_getRialtoB2A06`: `expected [N200] but found [N202]` at step `User verify the status code "Response Code"` (line 111)
- All subsequent response-body verification steps were skipped due to the status code failure

**Impact:** 1 failure

**Confidence:** High

---

## Summary

- **Root cause:** All 3 failures have been persistent since build 231 (133 builds ago), indicating a long-standing backend data or behaviour change that test expectations have not been updated to reflect.
- Pricing mismatches (tc_getRialtoB2A05, tc_postRialtoB2A03) possibly stem from a pricing-model change (e.g., per-unit vs. total calculation).
- The status code mismatch (tc_getRialtoB2A06) may reflect a deliberate API contract change where PATCH now returns `202 Accepted` instead of `200 OK`.
- No new failures were introduced in this build — the build stability is unchanged from recent runs.
