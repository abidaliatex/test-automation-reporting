# Root Cause Analysis — Build 361

**Source Report:** [build-361.md](../../../reports/build-failures/automationrunCAI-RIALTO-B2A-trunk/build-361.md)
**Job:** automationrunCAI-RIALTO-B2A-trunk
**Date:** 2026-08-07

---

## Build Summary

Build: 361
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
Response payload values do not match expected monetary amounts in the test data or contract checks.

**Evidence:**
- `tc_getRialtoB2A05`: `Iterators differ at element [3]: 276757.2 != 369009.6 expected [276757.2] but found [369009.6]`
- `tc_postRialtoB2A03`: `expected [[89392.58, 89392.58]] but found [[44696.29, 44696.29]]`

**Impact:** 2 failures

**Confidence:** High

## Async Order Status Still In Progress

**Affected Features:**
- rialtoB2A(CASS).feature

**Affected Scenarios:**
- Returns StoreStatus of Update Order (tc_getRialtoB2A06)

**Failure Pattern:**
Status check expected `N200` but the API still returned `N202`, indicating the updated order was not yet in its final state when polled.

**Evidence:**
- `tc_getRialtoB2A06`: `expected [N200] but found [N202]`
- The failing step is the immediate status-code assertion after the GET request on the stored UUID.

**Impact:** 1 failure

**Confidence:** Medium

---

## Summary

| Section | Detail |
|---|---|
| **Root Cause** | Two failures are value mismatches; one failure is an in-progress async status response |
| **Affected Components** | Rialto B2A CASS API response validation for StoreStatus and pricing flows |
| **Recommended Fix** | Verify expected pricing values/test data for `tc_getRialtoB2A05` and `tc_postRialtoB2A03`; review polling/timing for `tc_getRialtoB2A06` |
| **Prevention** | Separate async-status polling from value assertions and keep expected pricing data aligned with current API behavior |
