# Build Failure Report — automationrunCAI-RIALTOB2A-IntegrationTesting-Internal-trunk-demo #313

## Build Details

| Field | Value |
|---|---|
| **Build ID** | 313 |
| **Date** | 2026-07-25T21:10:06 UTC |
| **Status** | UNSTABLE |
| **Duration** | ~154 s |
| **URL** | https://crossadv.atex.com/jenkins/job/automationrunCAI-RIALTOB2A-IntegrationTesting-Internal-trunk-demo/313/ |

---

## Build Summary

| Metric | Count |
|---|---|
| Total Tests | 14 |
| Passed | 13 |
| Failed | 1 |
| Skipped | 0 |
| Pass Rate | 92.9% |

---

## Failing Tests / Steps

### Group 1 — MH `discountType` field returned null (1 failure)

| Suite | Scenario | Test Case | Error |
|---|---|---|---|
| rialtoB2A (CASS TC7 Change Date, Size & Placement) | verify that order arrived in MH from rilato - Change Date, Size & Placement | tc_getMHTC06 | `orders[0].printDetails.discountType` expected `[RIALTO]` but found `[null]` |

---

## Key Evidence

- Step: `User perform CASS GET API - #1.1` executing `tc_getMHTC06`
- Assertion error: `Mismatch on field: orders[0].printDetails.discountType expected [[RIALTO]] but found [[null]]`
- Stack trace: `SoftAssert.assertAll` → `ApiStepDefinition.tearDown(ApiStepDefinition.java:69)`
- `failedSince: 313` — regression first observed in this build.
