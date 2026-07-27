# Build Failure Report

**Build ID:** 318
**Job:** automationrunCAI-RIALTOB2A-IntegrationTesting-Internal-trunk-demo
**Date:** 2026-07-27
**Status:** UNSTABLE
**URL:** https://crossadv.atex.com/jenkins/job/automationrunCAI-RIALTOB2A-IntegrationTesting-Internal-trunk-demo/318/

---

## Build Summary

| Metric | Value |
|---|---|
| Total Tests | 15 |
| Passed | 13 |
| Failed | 2 |
| Skipped | 0 |
| Pass Rate | 86.7% |
| Duration | ~3m 25s |

---

## Source Revision

- **Commit:** `00c0ddcb05c2b5fc127c1956e5b147790ff4a0f8`
- **Commit message:** `updated testcase29 data tc_getMHTC_MZN04b`
- **Feature under test:** `src/test/resources/features/rialtoB2A(CASS)TestCase29.feature`

---

## Failing Tests / Steps

### 1. Missing `discountType` in MediaHouse original-state verification

- **Scenario:** `MEDIAHOUSE - Verify original full-page order state in MediaHouse - #1.1`
- **Test Case:** `tc_getMHTC_MZN04a`
- **Failing since:** Build 314
- **Failure pattern:** `orders.printDetails.discountType expected [[RIALTO]] but found [[null]]`
- **Stack trace:** `stepDefinition.ApiStepDefinition.tearDown(ApiStepDefinition.java:69)`

### 2. Reverted full-page values not reflected back in Rialto

- **Scenario:** `RIALTO - Verify Rialto reflects the reverted full-page state - #1.1`
- **Test Case:** `tc_getIntegrationRialtoMZN04b`
- **Failing since:** Build 314
- **Failure pattern:** `placementId expected [[HALVLIGG]] but found [[UPPSLAG]]`, plus width/depth/pricing mismatches
- **Stack trace:** `stepDefinition.ApiStepDefinition.tearDown(ApiStepDefinition.java:69)`

---

## Most Relevant Evidence

- `tc_getMHTC_MZN04a` fails on a single field regression: `orders.printDetails.discountType` is `null` instead of `RIALTO`.
- `tc_getIntegrationRialtoMZN04b` still returns Uppslag values after the revert flow: `placementId=UPPSLAG`, `columns=2`, `depth=297`, `width=460`, `priceGross=11000.0`.
- The related MediaHouse updated-state verification `tc_getMHTC_MZN04b` is marked `FIXED` in this build, so the remaining instability is concentrated in the original-state mapping and final reverted-state verification.
