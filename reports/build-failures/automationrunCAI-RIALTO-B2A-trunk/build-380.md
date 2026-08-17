# Build Failure Report

**Build ID:** 380
**Job:** automationrunCAI-RIALTO-B2A-trunk
**Date:** 2026-08-17
**Status:** UNSTABLE
**URL:** https://crossadv.atex.com/jenkins/job/automationrunCAI-RIALTO-B2A-trunk/380/

---

## Summary

| Metric | Value |
|---|---|
| Total Tests | 17 |
| Passed | 14 |
| Failed | 3 |
| Skipped | 0 |
| Pass Rate | 82.4% |

---

## Failing Tests / Steps

### 1. tc_getRialtoB2A05 — Returns StoreStatus of Order
- **Feature:** `rialtoB2A(CASS).feature` (line 64)
- **Step:** `User verify the response body "Response Body"`
- **Error:** `Iterators differ at element [3]: 276757.2 != 369009.6 expected [276757.2] but found [369009.6]`
- **Failed Since:** Build 231

### 2. tc_getRialtoB2A06 — Returns StoreStatus of Update Order
- **Feature:** `rialtoB2A(CASS).feature` (line 111)
- **Step:** `User verify the status code "Response Code"`
- **Error:** `expected [N200] but found [N202]`
- **Failed Since:** Build 231

### 3. tc_postRialtoB2A03 — Calculate price for self service
- **Feature:** `rialtoB2A(CASS).feature` (line 155)
- **Step:** `User verify the response body fields "Response Body Fields"`
- **Error:** `expected [[89392.58, 89392.58]] but found [[44696.29, 44696.29]]`
- **Failed Since:** Build 231
