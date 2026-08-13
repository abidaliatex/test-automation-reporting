# Investigation — automationrunCAI-RIALTO-B2A-trunk Build 372

**Source Report:** [build-372.md](../../reports/build-failures/automationrunCAI-RIALTO-B2A-trunk/build-372.md)

---

## Build Summary

| Field | Value |
|---|---|
| Build | [#372](https://crossadv.atex.com/jenkins/job/automationrunCAI-RIALTO-B2A-trunk/372/) |
| Total Tests | 17 |
| Passed | 14 |
| Failed | 3 |
| Pass Rate | 82.4% |

---

## Root Cause Groups

---

## Root Cause 1 — Incorrect Computed Monetary / Numerical Values Returned by API

**Affected Features:**
- `rialtoB2A(CASS).feature`

**Affected Scenarios:**
- Returns StoreStatus of Order (tc_getRialtoB2A05)
- Calculate price for self service (tc_postRialtoB2A03)

**Failure Pattern:**
Response body contains different numerical values than expected — amounts differ by approximately a factor of ~0.5 or ~1.33×, suggesting a pricing/calculation regression.

**Evidence:**
- `tc_getRialtoB2A05`: `Iterators differ at element [3]: 276757.2 != 369009.6 expected [276757.2] but found [369009.6]`
- `tc_postRialtoB2A03`: `expected [[89392.58, 89392.58]] but found [[44696.29, 44696.29]]` — returned value is exactly half the expected value, possibly a discount rate or multiplier bug

**Impact:** 2 failures

**Confidence:** High

---

## Root Cause 2 — Order Status Code Mismatch After Update (StoreStatus)

**Affected Features:**
- `rialtoB2A(CASS).feature`

**Affected Scenarios:**
- Returns StoreStatus of Update Order (tc_getRialtoB2A06)

**Failure Pattern:**
HTTP status code mismatch: expected `N200` (200 OK) but received `N202` (202 Accepted). The update order endpoint may have changed its response contract to return 202 instead of 200.

**Evidence:**
- `tc_getRialtoB2A06`: `expected [N200] but found [N202]` at step `User verify the status code "Response Code"` (line 111)
- All subsequent response-body validation steps were skipped due to this failure

**Impact:** 1 failure

**Confidence:** High

---

## Summary

| Root Cause | Failures | Confidence |
|---|---|---|
| Incorrect computed monetary/numerical values | 2 | High |
| Order status code mismatch after update | 1 | High |

All 3 failures have been recurring since build 231 (age: 142 builds), indicating a long-standing regression that was not caught or fixed.
