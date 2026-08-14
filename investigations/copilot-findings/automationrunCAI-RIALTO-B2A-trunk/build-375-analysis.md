# Build 375 — Root Cause Analysis

**Job:** automationrunCAI-RIALTO-B2A-trunk
**Report:** [build-375.md](../../../reports/build-failures/automationrunCAI-RIALTO-B2A-trunk/build-375.md)

---

## Build Summary

Build: 375
Total Tests: 17
Passed: 14
Failed: 3
Pass Rate: 82.4%

---

## Root Cause Groups

## Response Payload Numeric Mismatch

**Affected Features:**
- rialtoB2A(CASS).feature

**Affected Scenarios:**
- Returns StoreStatus of Order (tc_getRialtoB2A05)
- Calculate price for self service (tc_postRialtoB2A03)

**Failure Pattern:**
Expected numeric values in response payload do not match actual values returned by API.

**Evidence:**
- `tc_getRialtoB2A05`: `Iterators differ at element [3]: 276757.2 != 369009.6 expected [276757.2] but found [369009.6]`
- `tc_postRialtoB2A03`: `expected [[89392.58, 89392.58]] but found [[44696.29, 44696.29]]`

**Impact:** 2 failures

**Confidence:** High

## Status Code Contract/Timing Mismatch

**Affected Features:**
- rialtoB2A(CASS).feature

**Affected Scenarios:**
- Returns StoreStatus of Update Order (tc_getRialtoB2A06)

**Failure Pattern:**
Response code assertion expects `N200`, but API returned `N202` for updated order retrieval.

**Evidence:**
- `tc_getRialtoB2A06`: `expected [N200] but found [N202]`
- Failure occurs at status code verification step before body validation, indicating contract/timing mismatch at endpoint response stage.

**Impact:** 1 failure

**Confidence:** Medium
