# Build Failure Report

**Build ID:** 321
**Job:** automationrunCAI-RIALTOB2A-IntegrationTesting-Internal-trunk-demo
**Date:** 2026-07-27
**Status:** UNSTABLE
**URL:** https://crossadv.atex.com/jenkins/job/automationrunCAI-RIALTOB2A-IntegrationTesting-Internal-trunk-demo/321/

---

## Build Summary

| Metric | Value |
|---|---|
| Total Tests | 16 |
| Passed | 15 |
| Failed | 1 |
| Skipped | 0 |
| Pass Rate | 93.8% |
| Duration | ~4m 10s |

---

## Failing Tests

All failures are in the same test suite:
**Feature:** `rialtoB2A` — CASS TC29 Magazine (change to Uppslag/Spread/Panorama)
**Failing since:** Build 314

---

### Failure 1 — MEDIAHOUSE - Verify original full-page order state in MediaHouse - #1.1

**Test Case:** `tc_getMHTC_MZN04a` — verify that order arrived in MH from Rialto - magazine order original state

**Error:**
```text
The following asserts failed:
  Mismatch on field: orders.printDetails.discountType expected [[RIALTO]] but found [[null]]
```

**Stack Trace:**
```text
java.lang.AssertionError: The following asserts failed:
	Mismatch on field: orders.printDetails.discountType expected [[RIALTO]] but found [[null]]
	at org.testng.asserts.SoftAssert.assertAll(SoftAssert.java:46)
	at org.testng.asserts.SoftAssert.assertAll(SoftAssert.java:30)
	at stepDefinition.ApiStepDefinition.tearDown(ApiStepDefinition.java:69)
```
