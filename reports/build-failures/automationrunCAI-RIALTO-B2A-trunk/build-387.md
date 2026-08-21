# Build Failure Report

## Build ID: 387
**Job:** automationrunCAI-RIALTO-B2A-trunk
**Date:** 2026-08-21
**Status:** UNSTABLE
**URL:** https://crossadv.atex.com/jenkins/job/automationrunCAI-RIALTO-B2A-trunk/387/

---

## Test Results

| Total | Passed | Failed | Skipped |
|-------|--------|--------|---------|
| 17    | 15     | 2      | 0       |

---

## Failing Tests

### 1. tc_getRialtoB2A05 — Returns StoreStatus of Order
**Feature:** `rialtoB2A(CASS).feature` (line 64)
**Status:** FAILED (failing since build 231)
**Step:** `User verify the response body "Response Body"`
**Error:**
```
java.lang.AssertionError: Iterators differ at element [3]: 276757.2 != 369009.6
expected [276757.2] but found [369009.6]
```
**Stack Trace:**
```
at utility.JSONManager.compareJSONStrings(JSONManager.java:151)
at stepDefinition.ApiStepDefinition.user_verify_the_response_body(ApiStepDefinition.java:357)
at ✽.User verify the response body "Response Body"(rialtoB2A(CASS).feature:64)
```

---

### 2. tc_postRialtoB2A03 — Calculate price for self service
**Feature:** `rialtoB2A(CASS).feature` (line 155)
**Status:** FAILED (failing since build 231)
**Step:** `User verify the response body fields "Response Body Fields"`
**Error:**
```
java.lang.AssertionError: expected [[89392.58, 89392.58]] but found [[44696.29, 44696.29]]
```
**Stack Trace:**
```
at stepDefinition.ApiStepDefinition.user_verify_the_response_body_fields(ApiStepDefinition.java:609)
at ✽.User verify the response body fields "Response Body Fields"(rialtoB2A(CASS).feature:155)
```
