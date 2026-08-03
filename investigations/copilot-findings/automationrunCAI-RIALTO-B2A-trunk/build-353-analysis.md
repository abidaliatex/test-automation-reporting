# Build 353 — Root Cause Analysis

**Source Report:** [build-353.md](../../reports/build-failures/automationrunCAI-RIALTO-B2A-trunk/build-353.md)
**Job:** automationrunCAI-RIALTO-B2A-trunk
**Date:** 2026-08-03
**Build Result:** UNSTABLE

---

## Build Summary

| Build | Total Tests | Passed | Failed | Pass Rate |
|---|---|---|---|---|
| 353 | 17 | 14 | 3 | 82.4% |

---

## Root Cause Groups

## Incorrect Pricing / Calculation Values

**Affected Features:**
- rialtoB2A(CASS).feature

**Affected Scenarios:**
- Returns StoreStatus of Order (tc_getRialtoB2A05)
- Calculate price for self service (tc_postRialtoB2A03)

**Failure Pattern:**
Numeric response values do not match expected test data — pricing/calculation fields return different amounts than asserted.

**Evidence:**
- `tc_getRialtoB2A05`: `expected [276757.2] but found [369009.6]` at element [3] of response body iterator
- `tc_postRialtoB2A03`: `expected [[89392.58, 89392.58]] but found [[44696.28999999999, 44696.28999999999]]` — actual values are roughly half the expected, possibly a pricing formula or factor change

**Impact:** 2 failures

**Confidence:** High

---

## Unexpected HTTP Status Code on Updated Order

**Affected Features:**
- rialtoB2A(CASS).feature

**Affected Scenarios:**
- Returns StoreStatus of Update Order (tc_getRialtoB2A06)

**Failure Pattern:**
GET request for updated order returns HTTP 202 (Accepted) instead of the expected 200 (OK), suggesting the order update is still being processed asynchronously when the follow-up GET is made.

**Evidence:**
- `tc_getRialtoB2A06`: `expected [N200] but found [N202]` — response code mismatch after patch/update operation
- Preceded by a 10-second wait (`User waits for 10000`) that may be insufficient for the backend to complete processing

**Impact:** 1 failure

**Confidence:** High

---

## Summary

- All 3 failures have been persisting since **build 231**, indicating a long-standing regression.
- Root causes are likely a backend pricing/calculation change and an async processing timing issue, not test infrastructure problems.

## Recommended Fix

- **Pricing failures:** Review recent backend changes to pricing calculation logic or test data in `getRialtoB2A.csv` (tc_getRialtoB2A05) and `postRialtoB2A.csv` (tc_postRialtoB2A03). Update expected values if the new pricing is intentional.
- **Status code failure:** Increase the wait time before `tc_getRialtoB2A06` or poll until the order status is final (200) to handle async processing.

## Prevention

- Add change detection alerts when pricing endpoints return values outside an expected range.
- Use retry/poll logic instead of fixed waits for asynchronous order state transitions.
