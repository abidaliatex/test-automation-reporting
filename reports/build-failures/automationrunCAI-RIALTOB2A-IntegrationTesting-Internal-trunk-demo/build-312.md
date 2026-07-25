# Build Failure Report — automationrunCAI-RIALTOB2A-IntegrationTesting-Internal-trunk-demo #312

## Build Details

| Field | Value |
|---|---|
| **Build ID** | 312 |
| **Date** | 2026-07-25T13:41:07 UTC |
| **Status** | UNSTABLE |
| **Duration** | ~154 s |
| **URL** | https://crossadv.atex.com/jenkins/job/automationrunCAI-RIALTOB2A-IntegrationTesting-Internal-trunk-demo/312/ |

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
| rialtoB2A (CASS TC7 Change Date, Size & Placement) | verify that order arrived in MH from Rialto - Change Date, Size & Placement | tc_getMHTC06 | `orders[0].printDetails.discountType` expected `[RIALTO]` but found `[null]` |

---

## Key Evidence

- Step: `User perform CASS GET API - #1.1` executing `tc_getMHTC06`
- Assertion error: `Mismatch on field: orders[0].printDetails.discountType expected [[RIALTO]] but found [[null]]`
- Stack trace: `SoftAssert.assertAll` → `ApiStepDefinition.tearDown(ApiStepDefinition.java:69)`
- All other 13 steps in the scenario (login, POST order, 70 s wait, GET status, GET MH basket, PATCH MH, 60 s wait, final GET MH, re-auth, GET Rialto order, clear context) passed.
- `failedSince: 312` — new regression introduced in this build.
