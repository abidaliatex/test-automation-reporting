# Root Cause Analysis — Build 384

**Source Report:** [build-384.md](../../reports/build-failures/automationrunCAI-RIALTO-B2A-trunk/build-384.md)
**Job:** automationrunCAI-RIALTO-B2A-trunk
**Date:** 2026-08-19

---

## Build Summary

Build: 384
Total Tests: 17
Passed: 14
Failed: 3
Pass Rate: 82.4%

---

## Root Cause Groups

## Incorrect / Stale Expected Values in Test Data

**Affected Features:**
- rialtoB2A(CASS).feature

**Affected Scenarios:**
- Returns StoreStatus of Order (tc_getRialtoB2A05)
- Returns StoreStatus of Update Order (tc_getRialtoB2A06)
- Calculate price for self service (tc_postRialtoB2A03)

**Failure Pattern:**
Response body values or status codes returned by the API differ from the expected values hardcoded in the test CSV data files (`getRialtoB2A.csv`, `postRialtoB2A.csv`). Numeric amounts and status codes no longer match.

**Evidence:**
- `tc_getRialtoB2A05`: expected response body value `276757.2` at index [3], API returned `369009.6`
- `tc_getRialtoB2A06`: expected HTTP status `N200`, API returned `N202`
- `tc_postRialtoB2A03`: expected price fields `[89392.58, 89392.58]`, API returned `[44696.29, 44696.29]` (exactly half — possibly a pricing rate or rounding change)
- All three failures have `failedSince: 231`, indicating regression introduced ~153 builds ago and not yet fixed

**Impact:** 3 failures

**Confidence:** High

---

## Summary

All three failures are concentrated in order status retrieval and price calculation endpoints. The pattern of exact half-value differences in `tc_postRialtoB2A03` and mismatched status code in `tc_getRialtoB2A06` strongly suggests a backend data or configuration change (e.g. pricing rule, order processing logic, or status code mapping) that was not reflected in the test data CSV files. The `failedSince: 231` age indicates these have been failing since build 231.

## Root Cause

Stale expected values in test data CSV files (`getRialtoB2A.csv`, `postRialtoB2A.csv`). The backend API behaviour changed at or around build 231 and the test expectations were never updated.

## Affected Components

- `rialtoB2A(CASS).feature` lines 64, 111, 155
- `Rialto/RialtoB2A/getRialtoB2A.csv` — expected response body and status code fields
- `Rialto/RialtoB2A/postRialtoB2A.csv` — expected price fields

## Recommended Fix

- Review and update the expected values in `getRialtoB2A.csv` and `postRialtoB2A.csv` to match current API responses.
- Verify whether the pricing change in `tc_postRialtoB2A03` (half-value) is intentional.

## Prevention

- Add a changelog or version marker to test data CSV files so future API changes are tracked alongside test data updates.
