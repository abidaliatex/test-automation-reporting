# Build 377 — Root Cause Analysis

**Job:** automationrunCAI-RIALTO-B2A-trunk
**Report:** [build-377.md](../../../reports/build-failures/automationrunCAI-RIALTO-B2A-trunk/build-377.md)

---

## Build Summary

Build: 377
Total Tests: 17
Passed: 14
Failed: 3
Pass Rate: 82.4%

---

## Root Cause Groups

### Response Payload Numeric Mismatch

**Affected Features:**
- rialtoB2A(CASS).feature

**Affected Scenarios:**
- Returns StoreStatus of Order (tc_getRialtoB2A05)
- Calculate price for self service (tc_postRialtoB2A03)

**Failure Pattern:**
Response numeric values differ from expected payload values.

**Evidence:**
- `tc_getRialtoB2A05`: `Iterators differ at element [3]: 276757.2 != 369009.6 expected [276757.2] but found [369009.6]`
- `tc_postRialtoB2A03`: `expected [[89392.58, 89392.58]] but found [[44696.29, 44696.29]]`

**Impact:** 2 failures

**Confidence:** High

### Status Code Contract/Timing Mismatch

**Affected Features:**
- rialtoB2A(CASS).feature

**Affected Scenarios:**
- Returns StoreStatus of Update Order (tc_getRialtoB2A06)

**Failure Pattern:**
Status code expected [N200] but found [N202]

**Evidence:**
- `tc_getRialtoB2A06`: `expected [N200] but found [N202]`
- Failure occurs at the status-code validation step before response-body checks.

**Impact:** 1 failure

**Confidence:** Medium
