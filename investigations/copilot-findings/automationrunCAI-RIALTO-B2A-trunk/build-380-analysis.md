# Build 380 — Root Cause Analysis

**Source Report:** [build-380.md](../../reports/build-failures/automationrunCAI-RIALTO-B2A-trunk/build-380.md)
**Job:** automationrunCAI-RIALTO-B2A-trunk
**Date:** 2026-08-17

---

## Build Summary

Build: 380
Total Tests: 17
Passed: 14
Failed: 3
Pass Rate: 82.4%

---

## Root Cause Groups

## 1. Incorrect Pricing / Numeric Value Mismatch

**Affected Features:**
- rialtoB2A(CASS).feature

**Affected Scenarios:**
- Returns StoreStatus of Order (tc_getRialtoB2A05)
- Calculate price for self service (tc_postRialtoB2A03)

**Failure Pattern:**
Numeric values returned by the API differ from expected test data — likely a price calculation change in the backend.

**Evidence:**
- `tc_getRialtoB2A05`: `expected [276757.2] but found [369009.6]` at response body element [3]
- `tc_postRialtoB2A03`: `expected [[89392.58, 89392.58]] but found [[44696.29, 44696.29]]` in Response Body Fields

**Impact:** 2 failures

**Confidence:** High

---

## 2. Unexpected HTTP Status Code on Updated Order

**Affected Features:**
- rialtoB2A(CASS).feature

**Affected Scenarios:**
- Returns StoreStatus of Update Order (tc_getRialtoB2A06)

**Failure Pattern:**
GET request for an updated order returns HTTP N202 (Accepted/processing) instead of expected N200 (OK) — possibly the order processing is asynchronous and the 20-second wait is insufficient, or the status code mapping changed.

**Evidence:**
- `tc_getRialtoB2A06`: `expected [N200] but found [N202]` at status code verification step

**Impact:** 1 failure

**Confidence:** Medium

---

## Summary

| Section | Details |
|---|---|
| **Root Cause** | Backend pricing logic changes and async order status returning N202 instead of N200 |
| **Affected Components** | Rialto B2A CASS API (StoreStatus, Calculate Price endpoints) |
| **Recommended Fix** | Update expected test data to match new price values; investigate N202 response — may need longer wait or updated expected status code |
| **Prevention** | Synchronize test data CSV files with backend pricing updates; add contract tests for price calculations |

> All three failures have been regressing since build 231, indicating a persistent backend data or logic change that has not been reflected in the test fixtures.
