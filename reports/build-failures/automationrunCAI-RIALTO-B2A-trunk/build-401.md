# Build Failure Report

## Build ID: 401
**Job:** automationrunCAI-RIALTO-B2A-trunk
**Date:** 2026-08-31
**Status:** UNSTABLE
**URL:** https://crossadv.atex.com/jenkins/job/automationrunCAI-RIALTO-B2A-trunk/401/

## Test Summary

| Total | Passed | Failed | Skipped |
|-------|--------|--------|---------|
| 17    | 15     | 2      | 0       |

**Pass Rate:** 88.2%

## Failing Tests

### 1. tc_getRialtoB2A05 — Returns StoreStatus of Order
- **Class:** rialtoB2A(CASS)
- **Feature:** rialtoB2A(CASS).feature (line 64)
- **Error:** `Iterators differ at element [3]: 276757.2 != 369009.6 expected [276757.2] but found [369009.6]`
- **Failed Since:** Build 231
- **Step:** `User verify the response body "Response Body"`

### 2. tc_postRialtoB2A03 — Calculate price for self service
- **Class:** rialtoB2A(CASS)
- **Feature:** rialtoB2A(CASS).feature (line 155)
- **Error:** `expected [[89392.58, 89392.58]] but found [[44696.29, 44696.29]]`
- **Failed Since:** Build 231
- **Step:** `User verify the response body fields "Response Body Fields"`
