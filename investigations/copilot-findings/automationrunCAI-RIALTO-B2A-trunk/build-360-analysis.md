# Root Cause Analysis — Build 360

**Source Report:** [build-360.md](../../../reports/build-failures/automationrunCAI-RIALTO-B2A-trunk/build-360.md)
**Job:** automationrunCAI-RIALTO-B2A-trunk
**Date:** 2026-08-07

---

## Build Summary

Build: 360
Total Tests: 17
Passed: 14
Failed: 3
Pass Rate: 82.4%

---

## Root Cause Groups

## Pricing / Monetary Value Mismatch

**Affected Features:**
- rialtoB2A(CASS).feature

**Affected Scenarios:**
- Returns StoreStatus of Order (tc_getRialtoB2A05)
- Calculate price for self service (tc_postRialtoB2A03)

**Failure Pattern:**
API pricing values do not match the expected response data; one response field is higher than expected and another price pair is exactly half of the expected values.

**Evidence:**
- `tc_getRialtoB2A05`: `Iterators differ at element [3]: 276757.2 != 369009.6 expected [276757.2] but found [369009.6]`
- `tc_postRialtoB2A03`: `expected [[89392.58, 89392.58]] but found [[44696.29, 44696.29]]`

**Impact:** 2 failures

**Confidence:** High

---

## Update Order Still Returning Processing Status

**Affected Features:**
- rialtoB2A(CASS).feature

**Affected Scenarios:**
- Returns StoreStatus of Update Order (tc_getRialtoB2A06)

**Failure Pattern:**
The StoreStatus check for an updated order returns `N202` instead of the expected `N200`, indicating the order is still processing when the test validates it.

**Evidence:**
- `tc_getRialtoB2A06`: `expected [N200] but found [N202]`

**Impact:** 1 failure

**Confidence:** Medium

---

## Summary

- Build 360 matches the same three persistent failures already marked as failing since build 231.
- Jenkins checked out commit `3152fee94ae332b1cf9181d2c7844cfcb85a134c` (`udpated date for testcase23`), but the failing patterns appear long-running rather than newly introduced in this build.

## Root Cause

- Response data is inconsistent with expected pricing values in two scenarios.
- Update-order status remains asynchronous in one scenario.

## Affected Components

- Rialto B2A CASS API pricing responses
- Rialto B2A CASS StoreStatus polling for updated orders

## Recommended Fix

- Verify current pricing/rate data behind `tc_getRialtoB2A05` and `tc_postRialtoB2A03`.
- Recheck whether the update-order status test needs longer polling or whether the backend should return `N200` sooner.

## Prevention

- Keep expected pricing data aligned with approved backend pricing changes.
- Prefer retry/polling for async status validation instead of a single fixed check.
