# Build Failure Report

## Build Info

| Field | Value |
|---|---|
| **Build ID** | 165 |
| **Job** | automationrunCAI-RIALTOB2A-IntegrationTesting-Internal-trunk |
| **Date** | 2026-08-08 |
| **Status** | UNSTABLE |
| **URL** | https://crossadv.atex.com/jenkins/job/automationrunCAI-RIALTOB2A-IntegrationTesting-Internal-trunk/165/ |

## Test Results

| Metric | Count |
|---|---|
| Total Tests | 514 |
| Passed | 457 |
| Failed | 57 |
| Skipped | 0 |
| Pass Rate | 88.9% |

## Key Failure Groups

| Group | Impact | Evidence |
|---|---:|---|
| Discount/price calculation mismatches | 32 | `discountAmount expected [0.0] but found [63660.63]`; `orderBasketPriceSummary.orderDiscount expected [0.00] but found [4000.00]` |
| Order-line mapping / sequencing mismatches | 13 | `packageId expected [[AB, SVD]] but found [[SVD, AB]]`; `moduleCode expected [[58, 54]] but found [[58, 58]]` |
| Basket ID / path parameter propagation failures | 4 | `Basket not found for campaign`; `Undefined path parameters: mhBasketOrderId` |
| Backend transaction rollback (HTTP 500) | 3 | `Transaction rolled back because it has been marked as rollback-only` |
| Order status propagation mismatches | 3 | `statusFlags expected [[]] but found [[PRELIMINARY]]` |
| MH basket ID / Agency ID mismatch | 1 | `MH basket ID (orBoxid) [7454] does not match Agency Prisa ID [7455]` |

## Most Important Failing Steps

- `User perform CASS POST API` (TC1 and TC2) → basket not found and downstream path-param failures.
- `User perform CASS GET API - #1.1` (TC11, TC15) → large total/VAT mismatches.
- `Revert two MediaHouse order lines to full page - #1.1` (TC24) → HTTP 500 rollback.
- `MEDIAHOUSE - Verify updated magazine order state in MediaHouse - #1.1` (TC35) → basket ID mismatch.
