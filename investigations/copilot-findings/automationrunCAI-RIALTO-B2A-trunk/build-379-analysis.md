# Build 379 — Root Cause Analysis

**Source Report:** [build-379.md](../../reports/build-failures/automationrunCAI-RIALTO-B2A-trunk/build-379.md)

---

## Build Summary

**Build:** 379
**Total Tests:** 17
**Passed:** 14
**Failed:** 3
**Pass Rate:** 82.4%

---

## Root Cause Groups

## Pricing / Value Calculation Mismatch

**Affected Features:**
- rialtoB2A(CASS).feature

**Affected Scenarios:**
- Returns StoreStatus of Order (tc_getRialtoB2A05)
- Calculate price for self service (tc_postRialtoB2A03)

**Failure Pattern:**
Numeric response body values do not match expected test data — amounts are either doubled or halved relative to expectation.

**Evidence:**
- `tc_getRialtoB2A05`: `expected [276757.2] but found [369009.6]` at element [3] in response body
- `tc_postRialtoB2A03`: `expected [[89392.58, 89392.58]] but found [[44696.29, 44696.29]]` — found values are exactly half the expected amounts

**Impact:** 2 failures

**Confidence:** High

---

## Unexpected HTTP Status Code

**Affected Features:**
- rialtoB2A(CASS).feature

**Affected Scenarios:**
- Returns StoreStatus of Update Order (tc_getRialtoB2A06)

**Failure Pattern:**
GET request after PATCH returns HTTP 202 (Accepted) instead of expected 200 (OK), suggesting the server is still processing the update asynchronously.

**Evidence:**
- `tc_getRialtoB2A06`: `expected [N200] but found [N202]` — status check at line 111 of feature file
- The test waits 10 seconds after the PATCH, but the backend may require more time to finalize the update

**Impact:** 1 failure

**Confidence:** High

---

## Summary

- All 3 failures have persisted since **build 231**, indicating a systemic regression rather than a transient flake.
- Root causes are likely a **pricing/calculation rule change** in the backend (possibly a discount or rate factor applied differently) and a **timing/async processing issue** for the PATCH→GET flow.
