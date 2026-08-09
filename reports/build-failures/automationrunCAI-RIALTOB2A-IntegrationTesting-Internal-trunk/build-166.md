# Build Failure Report

## Build Info

| Field | Value |
|---|---|
| **Build ID** | 166 |
| **Job** | automationrunCAI-RIALTOB2A-IntegrationTesting-Internal-trunk |
| **Date** | 2026-08-09 |
| **Status** | UNSTABLE |
| **URL** | https://crossadv.atex.com/jenkins/job/automationrunCAI-RIALTOB2A-IntegrationTesting-Internal-trunk/166/ |

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
| Discount/price calculation mismatches | 21 | `discountAmount expected [0.0] but found [63660.63]`; `orderDiscount expected [0.00] but found [3600.00]` |
| Order-line mapping / sequencing mismatches | 12 | `packageId expected [[AB, SVD]] but found [[SVD, AB]]`; `paCode`, `plaCode` ordering drift |
| Basket ID / path parameter propagation failures | 5 | `Basket not found for campaign: TestCase01`; `Undefined path parameters: mhBasketOrderId`; `Redundant path parameters: agencyPrisaId` |
| Backend transaction rollback (HTTP 500) | 3 | `Transaction rolled back because it has been marked as rollback-only` (TC18, TC22, TC24) |
| Status-flag / discount-type propagation | 5 | `statusFlags expected [[]] but found [[PRELIMINARY]]`; `discountType expected [[RIALTO]] but found [[NONE]]` |
| Magazine commission / price mismatches | 11 | `commission expected [465.00] but found [155.00]`; `priceNet expected [[6000.0]] but found [[5814.0]]` |

## Most Important Failing Steps

- `User perform CASS POST API` (TC1 and TC2) → basket not found and downstream `mhBasketOrderId` path-parameter failures.
- `User perform CASS GET API - #1.1` (TC11) → large `totalInclVat`, `vat`, `netAmount` mismatches.
- `User perform CASS POST API / Revert steps` (TC18, TC22, TC24) → HTTP 500 rollback-only.
- `MEDIAHOUSE - Verify updated magazine order state` (TC26–TC37) → persistent `orderDiscount`, `commission`, and price-net drift.
- `RIALTO - Verify Rialto reflects the reverted full-page state - #1.1` (TC24) → stale path-parameter (`agencyPrisaId` redundant, `uuid` undefined).

## Failing Tests

| Test | Step | Error |
|---|---|---|
| CASS TC1 and TC2 | User perform CASS POST API | `Basket not found for campaign: TestCase01` |
| CASS TC1 and TC2 | User perform CASS GET API - #1.1 | `Undefined path parameters: mhBasketOrderId` |
| CASS TC1 and TC2 | User perform CASS POST API - #1.1 | `discountAmount expected [0.0] but found [63660.63]` |
| CASS TC1 and TC2 | User perform CASS GET API - #1.1 | `Undefined path parameters: mhBasketOrderId` |
| CASS TC3 change Size | User perform CASS POST API - #1.1 | `priceNetExComm expected [115320.00] but found [115320.0]` |
| CASS TC4 Change Placement | User perform CASS POST API - #1.1 | `discountAmount expected [0.0] but found [63660.63]` |
| CASS TC5 change to Uppslag/Spread/Panorama | User perform CASS POST API - #1.1 | `discountAmount expected [0.0] but found [63660.63]` |
| CASS TC6 change date and size | User perform CASS POST API - #1.1 | `priceNetExComm expected [115320.00] but found [115320.0]` |
| CASS TC9 change size from Rialto | User perform CASS POST API - #1.1 | `discountAmount expected [0.0] but found [38197.97]` |
| CASS TC9 change size from Rialto | User perform CASS GET API - #1.1 | `depth expected [[184]] but found [[372]]`; `discountType expected [[NONE]] but found [[RIALTO]]` |
| CASS TC11 change to UPPSLAG from Rialto | User perform CASS GET API - #1.1 | `totalInclVat expected [169660.46] but found [larger value]` |
| CASS TC11 change to UPPSLAG from Rialto | User perform CASS POST API - #1.1 | `priceNetExComm` floating-point mismatch |
| CASS TC11 change to UPPSLAG from Rialto | User perform CASS GET API - #1.1 | `totalInclVat` mismatch (second GET) |
| CASS TC14 | User perform CASS POST API - #1.1 | `priceNetExComm` floating-point mismatch |
| CASS TC14 | User perform CASS POST API - #1.1 | `priceNet` floating-point mismatch |
| CASS TC15 | User perform CASS POST API - #1.1 | `priceNetExComm` mismatch |
| CASS TC15 | User perform CASS GET API - #1.1 | `netAmount`, `grossAmount` mismatch |
| CASS TC15 | User perform CASS POST API - #1.1 | `packageId expected [[AB, SVD]] but found [[SVD, AB]]` |
| CASS TC18 | User perform CASS POST API - #1.1 | HTTP 500 rollback-only |
| CASS TC18 | User perform CASS POST API - #1.1 | `moduleCode expected [[58, 54]] but found [[58, 58]]` |
| CASS TC19 | User perform CASS POST API - #1.1 | `packageId expected [[AB, SVD]] but found [[SVD, AB]]` |
| CASS TC20 | User perform CASS POST API - #1.1 | `packageId expected [[SVD, AB]] but found [[AB, SVD]]` |
| CASS TC21 | User perform CASS POST API - #1.1 | `priceNet` floating-point mismatch |
| CASS TC21 | User perform CASS POST API - #1.1 | `priceNet` floating-point mismatch (second step) |
| CASS TC22 | User perform CASS GET API - #1.1 | `paCode` ordering mismatch |
| CASS TC22 | User perform CASS POST API - #1.1 | HTTP 500 rollback-only |
| CASS TC22 | User perform CASS GET API - #1.1 | `plaCode` ordering mismatch |
| CASS TC23 | Verify original full-page order state in MediaHouse - #1.1 | `netAmount` mismatch |
| CASS TC23 | Verify updated MediaHouse basket state - #1.1 | `netAmount` mismatch |
| CASS TC23 | Verify reverted MediaHouse basket state - #1.1 | `netAmount` mismatch |
| CASS TC24 | Verify created Rialto order - #1.1 | `priceNet` floating-point mismatch |
| CASS TC24 | Verify original full-page order state in MediaHouse - #1.1 | `netAmount` mismatch |
| CASS TC24 | Verify updated MediaHouse basket state - #1.1 | `paCode` ordering mismatch |
| CASS TC24 | Revert two MediaHouse order lines to full page - #1.1 | HTTP 500 rollback-only |
| CASS TC24 | Verify reverted MediaHouse basket state - #1.1 | `paCode` ordering mismatch |
| CASS TC24 | Verify Rialto reflects the reverted full-page state - #1.1 | `Redundant path parameters: agencyPrisaId; Undefined path parameters: uuid` |
| CASS TC26 Basic order for magazines | Verify reverted MediaHouse basket state - #1.1 | `orderDiscount expected [0.00] but found [3600.00]` |
| CASS TC27 Magazine (change date) | MEDIAHOUSE - Verify updated MediaHouse basket state - #1.1 | `discountType expected [[RIALTO]] but found [[NONE]]` |
| CASS TC27 Magazine (change date) | RIALTO - Verify Rialto reflects the reverted full-page state - #1.1 | `statusFlags expected [[]] but found [[PRELIMINARY]]` |
| CASS TC29 Magazine (change to Uppslag) | MEDIAHOUSE - Verify updated MediaHouse basket state - #1.1 | `commission expected [550.00] but found [341.00]` |
| CASS TC29 Magazine (change to Uppslag) | RIALTO - Verify Rialto reflects the reverted full-page state - #1.1 | `priceNet expected [[10931.8]] but found [[10659.0]]` |
| CASS TC30 Magazine (change Date & Size) | RIALTO - Verify Rialto reflects the reverted full-page state - #1.1 | `priceNet expected [[6000.0]] but found [[5814.0]]` |
| CASS TC31 Magazine (change Date, Size & Placement) | MEDIAHOUSE - Verify original full-page order state - #1.1 | `orderDiscount expected [3600.00] but found [4800.00]` |
| CASS TC31 Magazine (change Date, Size & Placement) | MEDIAHOUSE - Verify updated MediaHouse basket state - #1.1 | `commission expected [465.00] but found [155.00]` |
| CASS TC31 Magazine (change Date, Size & Placement) | RIALTO - Verify Rialto reflects the reverted full-page state - #1.1 | `priceNet expected [[5000.0]] but found [[4845.0]]` |
| CASS TC32 Magazine (change date from Rialto) | MEDIAHOUSE - Verify updated magazine order state - #1.1 | `orderDiscount expected [0.00] but found [3600.00]` |
| CASS TC33 Magazine (change size from Rialto) | MEDIAHOUSE - Verify updated magazine order state - #1.1 | `orderDiscount expected [0.00] but found [4000.00]` |
| CASS TC34 Magazine (change to UPPSLAG from Rialto) | MEDIAHOUSE - Verify updated magazine order state - #1.1 | `orderDiscount expected [0.00] but found [8800.00]` |
| CASS TC35 Magazine (change Date Size & Placement) | MEDIAHOUSE - Verify original magazine order state - #1.1 | `orderDiscount expected [3600.00] but found [4800.00]` |
| CASS TC35 Magazine (change Date Size & Placement) | RIALTO - Verify updated Agency order after Rialto change - #1.1 | `placementId expected [[SIDAN2]] but found [[HALVLIGG]]` |
| CASS TC35 Magazine (change Date Size & Placement) | MEDIAHOUSE - Verify updated magazine order state - #1.1 | `MH basket ID [7493] does not match Agency Prisa ID [7494]` |
| CASS TC36 Magazine (change Product Size Placement & Date) | MEDIAHOUSE - Verify original magazine order state - #1.1 | `orderDiscount expected [3600.00] but found [4800.00]` |
| CASS TC36 Magazine (change Product Size Placement & Date) | MEDIAHOUSE - Verify updated magazine order state - #1.1 | `orderDiscount expected [0.00] but found [4000.00]` |
| CASS TC37 - 2 Products Magazine | MEDIAHOUSE - Verify original order state - #1.1 | `totalInclVat expected [7368.00] but found [larger value]` |
| CASS TC37 - 2 Products Magazine | MEDIAHOUSE - Verify updated MediaHouse basket state - #1.1 | `commission expected [234.40] but found [229.40]` |
| CASS TC37 - 2 Products Magazine | RIALTO - Verify Rialto reflects the updated state - #1.1 | `priceNet expected [[4969.0, 2325.6]] but found [[4845.0, ...]]` |

## Root Cause Groups

| Root Cause | Total Failures | Still Active | Confidence |
|---|---:|---|---|
| Discount/price calculation mismatch | 21 | Yes | High |
| Order-line sequencing drift | 12 | Yes | High |
| Basket ID / path-parameter propagation failure | 5 | Yes | High |
| Backend transaction rollback (HTTP 500) | 3 | Yes | High |
| Status-flag / discount-type propagation | 5 | Yes | High |
| Magazine commission/price drift | 11 | Yes | High |
