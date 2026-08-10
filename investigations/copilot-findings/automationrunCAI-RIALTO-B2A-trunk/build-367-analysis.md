# Build 367 — Root Cause Analysis

**Source Report:** [build-367.md](../../reports/build-failures/automationrunCAI-RIALTO-B2A-trunk/build-367.md)

---

## Build Summary

**Build:** 367
**Total Tests:** 17
**Passed:** 14
**Failed:** 3
**Pass Rate:** 82.4%

---

## Root Cause Groups

---

## Incorrect Numeric Values in API Responses

**Affected Features:**
- rialtoB2A(CASS).feature

**Affected Scenarios:**
- User perform CASS POST API – tc_getRialtoB2A05 "Returns StoreStatus of Order"
- User perform CASS POST API – tc_postRialtoB2A03 "Calculate price for self service"

**Failure Pattern:**
Response body contains numeric values that differ from expected — pricing/value fields return approximately half or a different calculated amount than expected.

**Evidence:**
- `tc_getRialtoB2A05`: `Iterators differ at element [3]: 276757.2 != 369009.6` — expected 276757.2, got 369009.6
- `tc_postRialtoB2A03`: `expected [[89392.58, 89392.58]] but found [[44696.29, 44696.29]]` — returned values are exactly half of expected

**Impact:** 2 failures

**Confidence:** High

---

## Unexpected HTTP Status Code

**Affected Features:**
- rialtoB2A(CASS).feature

**Affected Scenarios:**
- User perform CASS POST API – tc_getRialtoB2A06 "Returns StoreStatus of Update Order"

**Failure Pattern:**
GET request after PATCH/update returns HTTP 202 (Accepted) instead of expected 200 (OK), possibly indicating the update is still being processed asynchronously.

**Evidence:**
- `tc_getRialtoB2A06`: `expected [N200] but found [N202]` — server returned 202 instead of 200 on status check after update

**Impact:** 1 failure

**Confidence:** High

---

## Summary

| Root Cause | Failures | Confidence |
|---|---|---|
| Incorrect numeric values in API responses (price/value calculation) | 2 | High |
| Unexpected HTTP status code (202 instead of 200 after update) | 1 | High |

---

## Affected Components
- `Rialto\RialtoB2A\getRialtoB2A.csv` (tc_getRialtoB2A05, tc_getRialtoB2A06)
- `Rialto\RialtoB2A\postRialtoB2A.csv` (tc_postRialtoB2A03)
- `rialtoB2A(CASS).feature`

## Recommended Fix
- Investigate pricing/calculation logic changes that may have halved returned values (tc_postRialtoB2A03, possibly tc_getRialtoB2A05).
- For tc_getRialtoB2A06: increase wait time before status check, or update test to accept 202 if async processing is expected behaviour.

## Prevention
- Add assertions on numeric precision in pricing-related endpoints.
- Monitor for status code regressions after patch/update operations.
