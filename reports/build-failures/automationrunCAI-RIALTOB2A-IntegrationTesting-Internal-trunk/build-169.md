# Build Failure Report

## Build Info

| Field | Value |
|---|---|
| **Build ID** | 169 |
| **Job** | automationrunCAI-RIALTOB2A-IntegrationTesting-Internal-trunk |
| **Date** | 2026-08-12 |
| **Status** | UNSTABLE |
| **URL** | https://crossadv.atex.com/jenkins/job/automationrunCAI-RIALTOB2A-IntegrationTesting-Internal-trunk/169/ |

## Test Results

| Metric | Count |
|---|---:|
| Total Tests | 514 |
| Passed | 483 |
| Failed | 31 |
| Skipped | 0 |
| Pass Rate | 94.0% |

## Failing Tests / Steps

- **Order-line sequencing / mapping drift (9 failures):** TC15, TC19, TC22, TC23, and TC24 reorder `packageId`, `paCode`, `prodCode`, `placementId`, `issueDate`, and related amount fields across multi-line updates.
- **Revert flow / identifier propagation failures (4 failures):** TC23 returns HTTP 500 `rollback-only`, TC24 keeps Uppslag payload values during revert and later misses `uuid`, and TC35 reports a MediaHouse/Agency ID mismatch.
- **Magazine pricing / status drift (12 failures):** TC28, TC29, TC31, TC33, TC34, TC35, TC36, and TC37 keep stale discounts, commissions, placements, dates, or `PRELIMINARY` status after update/revert flows.
- **Single-order placement / pricing drift (6 failures):** TC3, TC4, TC5, TC6, and TC9 return unexpected depth, placement, price, discount, or status values after size/placement changes.

## Key Evidence

- `orderAdDetails.packageId expected [[AB, SVD]] but found [[SVD, AB]]` (TC15 / TC19)
- `500 ... "Transaction rolled back because it has been marked as rollback-only" expected [N200] but found [N400]` (TC23)
- `Path parameters were not correctly defined. Redundant path parameters are: agencyPrisaId=7675. Undefined path parameters are: uuid.` (TC24)
- `orderBasketPriceSummary.orderDiscount expected [0.00] but found [4000.00]` (TC33 / TC36)
- `orderHeader.statusFlags expected [[PRELIMINARY]] but found [[]]` (TC28 / TC29 / TC4)
