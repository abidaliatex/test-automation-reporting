# Build Failure Report

## Build Details

- **Build ID:** 355
- **Job:** automationrunCAI-RIALTO-B2A-trunk
- **Date:** 2026-08-04
- **Status:** UNSTABLE
- **URL:** https://crossadv.atex.com/jenkins/job/automationrunCAI-RIALTO-B2A-trunk/355/

## Test Summary

| Metric | Value |
|---|---|
| Total Tests | 17 |
| Passed | 15 |
| Failed | 2 |
| Skipped | 0 |
| Pass Rate | 88.2% |

## Failing Tests

### 1. tc_getRialtoB2A05 — Returns StoreStatus of Order

- **Feature:** rialtoB2A(CASS).feature (line 64)
- **Step:** `User verify the response body "Response Body"`
- **Error:** `Iterators differ at element [3]: 276757.2 != 369009.6 expected [276757.2] but found [369009.6]`
- **Failed Since:** Build 231
- **Age:** 125 builds

### 2. tc_postRialtoB2A03 — Calculate price for self service

- **Feature:** rialtoB2A(CASS).feature (line 155)
- **Step:** `User verify the response body fields "Response Body Fields"`
- **Error:** `expected [[89392.58, 89392.58]] but found [[44696.29, 44696.29]]`
- **Failed Since:** Build 231
- **Age:** 125 builds
