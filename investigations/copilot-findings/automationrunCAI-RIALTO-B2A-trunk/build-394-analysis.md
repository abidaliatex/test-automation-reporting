# Build 394 — Root Cause Analysis

**Source Report:** [build-394.md](../../../reports/build-failures/automationrunCAI-RIALTO-B2A-trunk/build-394.md)

---

## Build Summary

**Build:** 394
**Total Tests:** 17
**Passed:** 14
**Failed:** 3
**Pass Rate:** 82.4%

---

## Root Cause Groups

---

## Incorrect Numeric Values in Response Body

**Affected Features:**
- rialtoB2A(CASS).feature

**Affected Scenarios:**
- Returns StoreStatus of Order (tc_getRialtoB2A05)
- Calculate price for self service (tc_postRialtoB2A03)

**Failure Pattern:**
Response body fields contain numeric values that differ from expected — values appear to be halved or otherwise miscalculated compared to test expectations.

**Evidence:**
- `tc_getRialtoB2A05`: `Iterators differ at element [3]: 276757.2 != 369009.6 expected [276757.2] but found [369009.6]`
- `tc_postRialtoB2A03`: `expected [[89392.58, 89392.58]] but found [[44696.29, 44696.29]]` — returned values are exactly half of expected

**Impact:** 2 failures

**Confidence:** High

---

## Unexpected HTTP Status Code on Updated Order

**Affected Features:**
- rialtoB2A(CASS).feature

**Affected Scenarios:**
- Returns StoreStatus of Update Order (tc_getRialtoB2A06)

**Failure Pattern:**
GET request for the updated order returns HTTP `N202` (Accepted/async processing) instead of the expected `N200` (OK), suggesting the backend processes the PATCH asynchronously and the order is not fully committed when the GET is issued.

**Evidence:**
- `tc_getRialtoB2A06`: `expected [N200] but found [N202]` at `User verify the status code "Response Code"`
- The preceding wait step is only 10 000 ms; may be insufficient for the update to finalise

**Impact:** 1 failure

**Confidence:** Medium

---

## Summary

| Root Cause | Failures | Failed Since |
|---|---|---|
| Incorrect numeric values in response body | 2 | Build 231 |
| Unexpected HTTP status code (N202 vs N200) after PATCH | 1 | Build 231 |

All three failures have been present since build 231, indicating a persistent regression rather than a new introduction in build 394.
