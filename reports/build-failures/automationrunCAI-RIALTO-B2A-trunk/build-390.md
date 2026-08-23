# Build Failure Report

## Build Summary

- **Build:** automationrunCAI-RIALTO-B2A-trunk #390
- **Date:** 2026-08-23
- **Status:** UNSTABLE
- **URL:** https://crossadv.atex.com/jenkins/job/automationrunCAI-RIALTO-B2A-trunk/390/
- **Total Tests:** 17
- **Passed:** 15
- **Failed:** 2
- **Pass Rate:** 88.2%

---

## Failing Tests

### 1. tc_getRialtoB2A05 — Returns StoreStatus of Order
- **Feature:** `rialtoB2A(CASS).feature` (line 64)
- **Step Failed:** `User verify the response body "Response Body"`
- **Error:** `Iterators differ at element [3]: 276757.2 != 369009.6 expected [276757.2] but found [369009.6]`
- **Stack Trace Anchor:** `utility.JSONManager.compareJSONStrings(JSONManager.java:151)`
- **Age:** 160 builds (failing since build 231)

### 2. tc_postRialtoB2A03 — Calculate price for self service
- **Feature:** `rialtoB2A(CASS).feature` (line 155)
- **Step Failed:** `User verify the response body fields "Response Body Fields"`
- **Error:** `expected [[89392.58, 89392.58]] but found [[44696.29, 44696.29]]`
- **Stack Trace Anchor:** `stepDefinition.ApiStepDefinition.user_verify_the_response_body_fields(ApiStepDefinition.java:609)`
- **Age:** 160 builds (failing since build 231)
