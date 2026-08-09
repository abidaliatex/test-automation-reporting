# Build 364 — Root Cause Analysis

**Job:** automationrunCAI-RIALTO-B2A-trunk
**Report:** [build-364.md](../../../reports/build-failures/automationrunCAI-RIALTO-B2A-trunk/build-364.md)
**Date:** 2026-08-09
**Status:** UNSTABLE

---

## Build Summary

Build: 364  
Total Tests: 17  
Passed: 13  
Failed: 4  
Pass Rate: 76.5%

---

## Root Cause Groups

### HTTP Status Contract Mismatch

**Affected Features:**
- rialtoB2A(CASS).feature

**Affected Scenarios:**
- Returns StoreStatus of Order (tc_getRialtoB2A05)

**Failure Pattern:**
`expected [N200] but found [N202]`

**Evidence:**
- Assertion failure in status-code verification step.
- Stack trace starts with `java.lang.AssertionError: expected [N200] but found [N202]`.

**Impact:** 1 failure

**Confidence:** High

---

### Response Parsing Failure (PATCH flow)

**Affected Features:**
- rialtoB2A(CASS).feature

**Affected Scenarios:**
- Update ad(Order) for self service (tc_patchRialtoB2A01)

**Failure Pattern:**
`Failed to parse the JSON document`

**Evidence:**
- RestAssured JSONPath parser throws exception during response validation.
- Stack trace starts with `io.restassured.path.json.exception.JsonPathException: Failed to parse the JSON document`.

**Impact:** 1 failure

**Confidence:** High

---

### Missing Path Parameter (`uuid`)

**Affected Features:**
- rialtoB2A(CASS).feature

**Affected Scenarios:**
- Returns StoreStatus of Update Order (tc_getRialtoB2A06)

**Failure Pattern:**
`Invalid number of path parameters. Expected 1, was 0. Undefined path parameters are: uuid.`

**Evidence:**
- Request execution fails before assertion due to unresolved path placeholder.
- Stack trace starts with `java.lang.IllegalArgumentException: Invalid number of path parameters...`.

**Impact:** 1 failure

**Confidence:** High

---

### Pricing Value Mismatch

**Affected Features:**
- rialtoB2A(CASS).feature

**Affected Scenarios:**
- Calculate price for self service (tc_postRialtoB2A03)

**Failure Pattern:**
`expected [[89392.58, 89392.58]] but found [[44696.29, 44696.29]]`

**Evidence:**
- Response values are exactly half of expected in both compared fields.
- Assertion failure is thrown from response-body field verification step.

**Impact:** 1 failure

**Confidence:** High
