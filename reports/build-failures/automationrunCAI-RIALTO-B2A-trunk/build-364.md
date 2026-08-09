# Build Failure Report

**Build ID:** 364
**Job:** automationrunCAI-RIALTO-B2A-trunk
**Date:** 2026-08-09
**Status:** UNSTABLE
**URL:** https://crossadv.atex.com/jenkins/job/automationrunCAI-RIALTO-B2A-trunk/364/

---

## Build Summary

| Metric | Value |
|---|---|
| Total Tests | 17 |
| Passed | 13 |
| Failed | 4 |
| Skipped | 0 |
| Pass Rate | 76.5% |

---

## Failing Tests / Steps

### 1) tc_getRialtoB2A05 — Returns StoreStatus of Order
- **Feature:** rialtoB2A(CASS).feature
- **Step failed:** Status code validation
- **Error:** `expected [N200] but found [N202]`

### 2) tc_patchRialtoB2A01 — Update ad(Order) for self service
- **Feature:** rialtoB2A(CASS).feature
- **Step failed:** Response body parsing/validation
- **Error:** `Failed to parse the JSON document`

### 3) tc_getRialtoB2A06 — Returns StoreStatus of Update Order
- **Feature:** rialtoB2A(CASS).feature
- **Step failed:** Request execution with path parameter
- **Error:** `Invalid number of path parameters. Expected 1, was 0. Undefined path parameters are: uuid.`

### 4) tc_postRialtoB2A03 — Calculate price for self service
- **Feature:** rialtoB2A(CASS).feature
- **Step failed:** Response body field validation
- **Error:** `expected [[89392.58, 89392.58]] but found [[44696.29, 44696.29]]`
