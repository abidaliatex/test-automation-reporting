# Build Failure Report

## Build Info

| Field | Value |
|---|---|
| **Build ID** | 168 |
| **Job** | automationrunCAI-RIALTOB2A-IntegrationTesting-Internal-trunk |
| **Date** | 2026-08-11 |
| **Status** | UNSTABLE |
| **URL** | https://crossadv.atex.com/jenkins/job/automationrunCAI-RIALTOB2A-IntegrationTesting-Internal-trunk/168/ |

## Test Results

| Metric | Count |
|---|---:|
| Total Tests | 514 |
| Passed | 477 |
| Failed | 37 |
| Skipped | 0 |
| Pass Rate | 92.8% |

## Failing Tests / Steps

- **Order-line sequencing drift (8 failures):** TC15, TC22, TC23, and TC24 reorder `packageId`, `paCode`, `prodCode`, `plaCode`, `issueDate`, and related price arrays during multi-line updates.
- **Revert / identifier handling failures (4 failures):** TC23 returns HTTP 500 rollback-only during revert, TC24 keeps Uppslag payload values during revert and later misses `uuid`, and TC35 reports `MH basket ID` / `Agency Prisa ID` mismatch.
- **Magazine pricing / discount propagation drift (19 failures):** TC26, TC27, TC29, TC30, TC31, TC32, TC33, TC34, TC35, TC36, and TC37 keep stale discounts, commissions, or `PRELIMINARY` status after updates/reverts.
- **Single-order placement / pricing drift (6 failures):** TC3, TC4, TC5, TC6, and TC9 (POST and GET) return unexpected depth, placement, discount, and net-price values after size/placement changes.

## Key Evidence

- `orderAdDetails.packageId expected [[AB, SVD]] but found [[SVD, AB]]` (TC15)
- `Transaction rolled back because it has been marked as rollback-only` (TC23 revert)
- `Path parameters were not correctly defined. Redundant path parameters are: agencyPrisaId=7613. Undefined path parameters are: uuid.` (TC24)
- `orderBasketPriceSummary.orderDiscount expected [0.00] but found [3600.00]` (TC26)
- `orders.printDetails.discountType expected [[RIALTO]] but found [[NONE]]` (TC27)
- `discountAmount expected [0.0] but found [63660.63]` (TC5)
