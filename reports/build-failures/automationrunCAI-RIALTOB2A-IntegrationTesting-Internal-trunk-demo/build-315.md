# Build Failure Report — automationrunCAI-RIALTOB2A-IntegrationTesting-Internal-trunk-demo #315

## Build Details

| Field | Value |
|---|---|
| **Build ID** | 315 |
| **Date** | 2026-07-26T13:01:10 UTC |
| **Status** | UNSTABLE |
| **Duration** | ~204 s |
| **URL** | https://crossadv.atex.com/jenkins/job/automationrunCAI-RIALTOB2A-IntegrationTesting-Internal-trunk-demo/315/ |

---

## Build Summary

| Metric | Count |
|---|---|
| Total Tests | 15 |
| Passed | 12 |
| Failed | 3 |
| Skipped | 0 |
| Pass Rate | 80.0% |

---

## Failing Tests / Steps

All 3 failures are in suite: `rialtoB2A(CASS TC29 Magazine (change to Uppslag/Spread/Panorama)` — regression first observed in build 314.

### Group 1 — `discountType` field returned null (1 failure)

| Scenario | Error |
|---|---|
| MEDIAHOUSE - Verify original full-page order state in MediaHouse - #1.1 | `orders.printDetails.discountType` expected `[RIALTO]` but found `[null]` |

### Group 2 — Placement/Size/Price state not reverted to HALVLIGG (2 failures)

| Scenario | Error |
|---|---|
| MEDIAHOUSE - Verify updated MediaHouse basket state - #1.1 | `orders.printDetails.plaCode` expected `[HALVLIGG]` found `[UPPSLAG]`; width, depth, netAmount, grossAmount, and price summary fields all mismatched |
| RIALTO - Verify Rialto reflects the reverted full-page state - #1.1 | `orderAdDetails.placementId` expected `[HALVLIGG]` found `[UPPSLAG]`; columns, depth, width, priceGross, priceNet, commissionAmount all mismatched |

---

## Key Evidence

### Group 1
- `Mismatch on field: orders.printDetails.discountType expected [[RIALTO]] but found [[null]]`
- Stack: `SoftAssert.assertAll` → `ApiStepDefinition.tearDown(ApiStepDefinition.java:69)`

### Group 2
- `Mismatch on field: orders.printDetails.plaCode expected [[HALVLIGG]] but found [[UPPSLAG]]`
- `Mismatch on field: orders.printDetails.width expected [[1]] but found [[2]]`
- `Mismatch on field: orders.printDetails.depth expected [[146]] but found [[297]]`
- `Mismatch on field: orders.printDetails.netAmount expected [[5000.0]] but found [[11000.0]]`
- `Mismatch on field: orderAdDetails.placementId expected [[HALVLIGG]] but found [[UPPSLAG]]`
- `Mismatch on field: orderAdDetails.priceGross expected [[5000.0]] but found [[11000.0]]`
- `Mismatch on field: orderAdDetails.commissionAmount expected [[155.0]] but found [[68.2]]`
- `failedSince: 314` — regression first observed in build 314.
