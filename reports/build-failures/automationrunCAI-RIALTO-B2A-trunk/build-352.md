# Build Failure Report

**Build ID:** 352
**Job:** automationrunCAI-RIALTO-B2A-trunk
**Date:** 2026-08-03
**Status:** UNSTABLE
**Build URL:** https://crossadv.atex.com/jenkins/job/automationrunCAI-RIALTO-B2A-trunk/352/

---

## Build Summary

Build: 352
Total Tests: 17
Passed: 14
Failed: 3
Pass Rate: 82.4%

---

## Failing Tests

### 1. tc_getRialtoB2A05 — Returns StoreStatus of Order
- **Feature:** rialtoB2A(CASS).feature (line 64)
- **Step Failed:** `User verify the response body "Response Body"`
- **Error:** `Iterators differ at element [3]: 276757.2 != 369009.6 expected [276757.2] but found [369009.6]`
- **Age:** 122 builds (failing since build 231)

### 2. tc_getRialtoB2A06 — Returns StoreStatus of Update Order
- **Feature:** rialtoB2A(CASS).feature (line 111)
- **Step Failed:** `User verify the status code "Response Code"`
- **Error:** `expected [N200] but found [N202]`
- **Age:** 122 builds (failing since build 231)

### 3. tc_postRialtoB2A03 — Calculate price for self service
- **Feature:** rialtoB2A(CASS).feature (line 155)
- **Step Failed:** `User verify the response body fields "Response Body Fields"`
- **Error:** `expected [[89392.58, 89392.58]] but found [[44696.28999999999, 44696.28999999999]]`
- **Age:** 122 builds (failing since build 231)
