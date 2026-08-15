# Investigation — automationrunCAI-RIALTO-B2A-trunk Build 376

**Source report:** [build-376.md](../../reports/build-failures/automationrunCAI-RIALTO-B2A-trunk/build-376.md)

---

## Build Summary

| Field | Value |
|---|---|
| Build | #376 |
| Total Tests | 17 |
| Passed | 14 |
| Failed | 3 |
| Pass Rate | 82.4% |

---

## Root Cause Groups

## Root Cause 1 — Numeric Price / Calculation Value Mismatch

**Affected Features:**
- rialtoB2A(CASS).feature

**Affected Scenarios:**
- Returns StoreStatus of Order (tc_getRialtoB2A05)
- Calculate price for self service (tc_postRialtoB2A03)

**Failure Pattern:**
Actual numeric values returned by the API differ from the values asserted in the test data CSV.

**Evidence:**
- `tc_getRialtoB2A05`: `expected [276757.2] but found [369009.6]` (element [3] of response body iterator)
- `tc_postRialtoB2A03`: `expected [[89392.58, 89392.58]] but found [[44696.29, 44696.29]]` — actual values are exactly half the expected values, possibly indicating a rate or multiplier change in the pricing calculation

**Impact:** 2 failures

**Confidence:** High

---

## Root Cause 2 — Unexpected HTTP Status Code After Order Update

**Affected Features:**
- rialtoB2A(CASS).feature

**Affected Scenarios:**
- Returns StoreStatus of Update Order (tc_getRialtoB2A06)

**Failure Pattern:**
GET request after a PATCH returns HTTP 202 (Accepted) instead of the expected 200 (OK), suggesting the order update is still processing asynchronously when the status check is made.

**Evidence:**
- `tc_getRialtoB2A06`: `expected [N200] but found [N202]`
- Preceding step `tc_patchRialtoB2A01` (update ad) was followed by a 10 s wait, which may be insufficient for the server to complete the PATCH

**Impact:** 1 failure

**Confidence:** High

---

## Summary

**Root Cause:** Persistent test data / backend value drift (all 3 failures have been present since build 231, age 146). Two failures reflect changed pricing calculation values; one reflects an async processing timing issue with the PATCH → GET flow.

**Affected Components:** Rialto B2A CASS API — order pricing (`postRialtoB2A03`), store-status retrieval (`getRialtoB2A05`/`getRialtoB2A06`).

**Recommended Fix:**
- Update expected values in `getRialtoB2A.csv` and `postRialtoB2A.csv` to match current backend output, or investigate why the backend pricing values changed.
- For tc_getRialtoB2A06: increase the wait time after the PATCH call, or poll until status is 200.

**Prevention:**
- Align test data CSV assertions with each backend deployment; treat persistent age-146+ failures as a test-data drift signal.
