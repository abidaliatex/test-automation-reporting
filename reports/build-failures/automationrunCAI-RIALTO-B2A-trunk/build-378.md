# Build Failure Report

## Build ID: 378
**Job:** automationrunCAI-RIALTO-B2A-trunk
**Date:** 2026-08-16
**Status:** UNSTABLE
**URL:** https://crossadv.atex.com/jenkins/job/automationrunCAI-RIALTO-B2A-trunk/378/

---

## Test Summary

| Metric | Value |
|---|---|
| Total Tests | 17 |
| Passed | 13 |
| Failed | 4 |
| Skipped | 0 |
| Pass Rate | 76.5% |

---

## Failing Tests

### 1. tc_getRialtoB2A05 — Returns StoreStatus of Order
- **Feature:** `rialtoB2A(CASS).feature` (line 59)
- **Step Failed:** `User verify the status code "Response Code"`
- **Error:** `expected [N200] but found [N202]`
- **Stack Trace (Top):** `stepDefinition.ApiStepDefinition.user_verify_the_status_code(ApiStepDefinition.java:237)`

### 2. tc_patchRialtoB2A01 — Update ad(Order) for self service
- **Feature:** `rialtoB2A(CASS).feature` (line 97)
- **Step Failed:** `User perfrom "post" request with request body "Request Body" and alterd IDs from recent created ad`
- **Error:** `Failed to parse the JSON document`
- **Stack Trace (Top):** `stepDefinition.ApiStepDefinition.user_perfrom_request_with_request_body_and_alterd_IDs_from_recent_created_ad(ApiStepDefinition.java:985)`

### 3. tc_getRialtoB2A06 — Returns StoreStatus of Update Order
- **Feature:** `rialtoB2A(CASS).feature`
- **Step Failed:** `User perfrom "get" request with keys "uuid"`
- **Error:** `Invalid number of path parameters. Expected 1, was 0. Undefined path parameters are: uuid.`
- **Stack Trace (Top):** `stepDefinition.ApiStepDefinition.user_perfrom_request_with_keys(...)`

### 4. tc_postRialtoB2A03 — Calculate price for self service
- **Feature:** `rialtoB2A(CASS).feature`
- **Step Failed:** `User verify the response body fields "Response Body Fields"`
- **Error:** `expected [[89392.58, 89392.58]] but found [[44696.29, 44696.29]]`
- **Stack Trace (Top):** `stepDefinition.ApiStepDefinition.user_verify_the_response_body_fields(ApiStepDefinition.java:609)`
