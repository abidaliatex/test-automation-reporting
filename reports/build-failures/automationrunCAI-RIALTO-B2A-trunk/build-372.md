# Build Failure Report — automationrunCAI-RIALTO-B2A-trunk #372

## Build Summary

| Field | Value |
|---|---|
| **Build** | [#372](https://crossadv.atex.com/jenkins/job/automationrunCAI-RIALTO-B2A-trunk/372/) |
| **Date** | 2026-08-13 |
| **Status** | UNSTABLE |
| **Total Tests** | 17 |
| **Passed** | 14 |
| **Failed** | 3 |
| **Pass Rate** | 82.4% |

---

## Failing Tests

### 1. tc_getRialtoB2A05 — Returns StoreStatus of Order
- **Status:** FAILED (age: 142)
- **Feature:** `rialtoB2A(CASS).feature` (line 64)
- **Error:** `Iterators differ at element [3]: 276757.2 != 369009.6 expected [276757.2] but found [369009.6]`
- **Step:** `User verify the response body "Response Body"` — failed

### 2. tc_getRialtoB2A06 — Returns StoreStatus of Update Order
- **Status:** FAILED (age: 142)
- **Feature:** `rialtoB2A(CASS).feature` (line 111)
- **Error:** `expected [N200] but found [N202]`
- **Step:** `User verify the status code "Response Code"` — failed

### 3. tc_postRialtoB2A03 — Calculate price for self service
- **Status:** FAILED (age: 142)
- **Feature:** `rialtoB2A(CASS).feature` (line 155)
- **Error:** `expected [[89392.58, 89392.58]] but found [[44696.29, 44696.29]]`
- **Step:** `User verify the response body fields "Response Body Fields"` — failed
