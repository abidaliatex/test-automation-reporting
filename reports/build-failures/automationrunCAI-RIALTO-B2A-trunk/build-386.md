# Build Failure Report

## Build ID: 386
**Job:** automationrunCAI-RIALTO-B2A-trunk
**Date:** 2026-08-21
**Status:** UNSTABLE
**URL:** https://crossadv.atex.com/jenkins/job/automationrunCAI-RIALTO-B2A-trunk/386/

---

## Test Results

| Metric | Value |
|---|---|
| Total Tests | 17 |
| Passed | 15 |
| Failed | 2 |
| Skipped | 0 |
| Pass Rate | 88.2% |

---

## Failing Tests / Steps

### 1. tc_getRialtoB2A05 — Returns StoreStatus of Order
- **Step:** `User verify the response body "Response Body"`
- **Error:** `Iterators differ at element [3]: 276757.2 != 369009.6 expected [276757.2] but found [369009.6]`
- **Failed Since:** Build 231
- **Stack Trace (top):** `utility.JSONManager.compareJSONStrings(JSONManager.java:151) -> stepDefinition.ApiStepDefinition.user_verify_the_response_body(ApiStepDefinition.java:357)`

### 2. tc_postRialtoB2A03 — Calculate price for self service
- **Step:** `User verify the response body fields "Response Body Fields"`
- **Error:** `expected [[89392.58, 89392.58]] but found [[44696.29, 44696.29]]`
- **Failed Since:** Build 231
- **Stack Trace (top):** `stepDefinition.ApiStepDefinition.user_verify_the_response_body_fields(ApiStepDefinition.java:609)`
