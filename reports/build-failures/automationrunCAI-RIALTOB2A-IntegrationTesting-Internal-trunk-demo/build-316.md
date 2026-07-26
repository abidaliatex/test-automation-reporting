# Build Failure Report

**Build ID:** 316
**Job:** automationrunCAI-RIALTOB2A-IntegrationTesting-Internal-trunk-demo
**Date:** 2026-07-26
**Status:** UNSTABLE
**URL:** https://crossadv.atex.com/jenkins/job/automationrunCAI-RIALTOB2A-IntegrationTesting-Internal-trunk-demo/316/

---

## Build Summary

| Metric | Value |
|---|---|
| Total Tests | 15 |
| Passed | 12 |
| Failed | 3 |
| Skipped | 0 |
| Pass Rate | 80% |
| Duration | ~3m 41s |

---

## Failing Tests

All 3 failures are in the same test suite:
**Feature:** `rialtoB2A` — CASS TC29 Magazine (change to Uppslag/Spread/Panorama)
**Failing since:** Build 314

---

### Failure 1 — MEDIAHOUSE - Verify original full-page order state in MediaHouse - #1.1

**Test Case:** `tc_getMHTC_MZN04a` — verify that order arrived in MH from rialto - magazine order original state

**Error:**
```
The following asserts failed:
  Mismatch on field: orders.printDetails.discountType expected [[RIALTO]] but found [[null]]
```

**Stack Trace:**
```
java.lang.AssertionError: The following asserts failed:
  Mismatch on field: orders.printDetails.discountType expected [[RIALTO]] but found [[null]]
  at org.testng.asserts.SoftAssert.assertAll(SoftAssert.java:46)
  at stepDefinition.ApiStepDefinition.tearDown(ApiStepDefinition.java:69)
```

---

### Failure 2 — MEDIAHOUSE - Verify updated MediaHouse basket state - #1.1

**Test Case:** `tc_getMHTC_MZN04b` — verify that order arrived in MH from rialto - magazine order after Uppslag/Spread/Panorama change

**Error:**
```
Mismatch on field: orders.printDetails.plaCode expected [[HALVLIGG]] but found [[UPPSLAG]]
Mismatch on field: orders.printDetails.width expected [[1]] but found [[2]]
Mismatch on field: orders.printDetails.depth expected [[146]] but found [[297]]
Mismatch on field: orders.printDetails.netAmount expected [[5000.0]] but found [[11000.0]]
Mismatch on field: orders.printDetails.grossAmount expected [[5000.0]] but found [[11000.0]]
Mismatch on field: orderBasketPriceSummary.printGross expected [5000.00] but found [11000.00]
Mismatch on field: orderBasketPriceSummary.commission expected [155.00] but found [550.00]
Mismatch on field: orderBasketPriceSummary.orderbasketSum expected [4845.00] but found [10450.00]
Mismatch on field: orderBasketPriceSummary.totalInclVat expected [6056.25] but found [13062.50]
... (18 field mismatches total)
```

---

### Failure 3 — RIALTO - Verify Rialto reflects the reverted full-page state - #1.1

**Test Case:** `tc_getIntegrationRialtoMZN04b` — confirms order created in Agency for testcase 29 - after size change

**Error:**
```
Mismatch on field: orderAdDetails.placementId expected [[HALVLIGG]] but found [[UPPSLAG]]
Mismatch on field: orderAdDetails.columns expected [[1]] but found [[2]]
Mismatch on field: orderAdDetails.depth expected [[146]] but found [[297]]
Mismatch on field: orderAdDetails.width expected [[230]] but found [[460]]
Mismatch on field: orderAdDetails.priceGross expected [[5000.0]] but found [[11000.0]]
Mismatch on field: orderAdDetails.commissionAmount expected [[155.0]] but found [[68.2]]
Mismatch on field: priceGross expected [5000.0] but found [11000.0]
... (11 field mismatches total)
```
