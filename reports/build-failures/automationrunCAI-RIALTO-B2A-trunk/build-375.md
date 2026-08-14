# Build Failure Report

## Build ID: 375
**Job:** automationrunCAI-RIALTO-B2A-trunk
**Date:** 2026-08-14
**Status:** UNSTABLE
**URL:** https://crossadv.atex.com/jenkins/job/automationrunCAI-RIALTO-B2A-trunk/375/

---

## Test Summary

| Metric | Value |
|---|---|
| Total Tests | 17 |
| Passed | 14 |
| Failed | 3 |
| Skipped | 0 |
| Pass Rate | 82.4% |

---

## Failing Tests

### 1. tc_getRialtoB2A05 — Returns StoreStatus of Order
- **Feature:** rialtoB2A(CASS).feature (line 64)
- **Step Failed:** `User verify the response body "Response Body"`
- **Error:** `Iterators differ at element [3]: 276757.2 != 369009.6 expected [276757.2] but found [369009.6]`
- **Stack Trace (Top):** `utility.JSONManager.compareJSONStrings(JSONManager.java:151) -> stepDefinition.ApiStepDefinition.user_verify_the_response_body(ApiStepDefinition.java:357)`

### 2. tc_getRialtoB2A06 — Returns StoreStatus of Update Order
- **Feature:** rialtoB2A(CASS).feature (line 111)
- **Step Failed:** `User verify the status code "Response Code"`
- **Error:** `expected [N200] but found [N202]`
- **Stack Trace (Top):** `stepDefinition.ApiStepDefinition.user_verify_the_status_code(ApiStepDefinition.java:237)`

### 3. tc_postRialtoB2A03 — Calculate price for self service
- **Feature:** rialtoB2A(CASS).feature (line 155)
- **Step Failed:** `User verify the response body fields "Response Body Fields"`
- **Error:** `expected [[89392.58, 89392.58]] but found [[44696.29, 44696.29]]`
- **Stack Trace (Top):** `stepDefinition.ApiStepDefinition.user_verify_the_response_body_fields(ApiStepDefinition.java:609)`
