# Build Analysis — automationrunCAI-RIALTO-B2A-trunk — Build 387

**Report:** [build-387.md](../../reports/build-failures/automationrunCAI-RIALTO-B2A-trunk/build-387.md)

---

## Build Summary

Build: 387
Total Tests: 17
Passed: 15
Failed: 2
Pass Rate: 88.2%

---

## Root Cause Groups

## Incorrect Pricing / Monetary Value Mismatch

**Affected Features:**
- rialtoB2A(CASS).feature

**Affected Scenarios:**
- Returns StoreStatus of Order (tc_getRialtoB2A05)
- Calculate price for self service (tc_postRialtoB2A03)

**Failure Pattern:**
Numeric value mismatch in response body — expected values differ from actual by a consistent factor (~0.5x or ~1.33x), indicating a pricing calculation regression in the back-end service.

**Evidence:**
- `tc_getRialtoB2A05`: `expected [276757.2] but found [369009.6]` — actual is ~1.33× expected
- `tc_postRialtoB2A03`: `expected [[89392.58, 89392.58]] but found [[44696.29, 44696.29]]` — actual is ~0.5× expected
- Both failures trace to response body field verification (`ApiStepDefinition.java:357` and `:609`)
- Both have been failing since build 231 (age: 157 builds)

**Impact:** 2 failures

**Confidence:** High
