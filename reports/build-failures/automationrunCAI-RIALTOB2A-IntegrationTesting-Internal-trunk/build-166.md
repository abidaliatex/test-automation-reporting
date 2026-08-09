# Build Failure Report

**Build ID:** 166
**Job:** automationrunCAI-RIALTOB2A-IntegrationTesting-Internal-trunk
**Date:** 2026-08-09 21:03:11 UTC
**Status:** UNSTABLE
**URL:** https://crossadv.atex.com/jenkins/job/automationrunCAI-RIALTOB2A-IntegrationTesting-Internal-trunk/166/

---

## Build Summary

| Metric | Value |
|---|---|
| Total Tests | 514 |
| Passed | 457 |
| Failed | 57 |
| Skipped | 0 |
| Pass Rate | 88.9% |

---

## Failing Tests / Steps

### CASS TC1 and TC2
- **User perform CASS POST API** — `Basket not found for campaign: TestCase01 expected [false] but found [true]`
- **User perform CASS GET API - #1.1** — `Invalid number of path parameters. Expected 1, was 0. Undefined path parameters are: mhBasketOrderId.`
- **User perform CASS POST API - #1.1** — Price/discount field mismatches (discountAmount, priceNetExComm, totalInclVat)
- **User perform CASS POST API - #1.1** *(empty error)*

### CASS TC3 / TC6
- **User perform CASS POST API - #1.1** — `priceNetExComm expected [115320.00] but found [115320.0]` (decimal format mismatch)

### CASS TC4 Change Placement
- **User perform CASS POST API - #1.1** — `priceGross expected [250000.00] but found [250000.0]`; `statusFlags expected [[PRELIMINARY]] but found [[]]`

### CASS TC5 change to Uppslag/Spread/Panorama
- **User perform CASS POST API - #1.1** — `discountAmount expected [0.0] but found [63660.63]`; `priceGross expected [250000.00] but found [192192.0]`

### CASS TC9 change size from Rialto
- **User perform CASS POST API - #1.1** — `discountAmount expected [0.0] but found [38197.97]`
- **User perform CASS GET API - #1.1** — `depth expected [[184]] but found [[372]]`; `moduleCode expected [[54]] but found [[58]]`

### CASS TC11 change to UPPSLAG from Rialto
- **User perform CASS GET API - #1.1** — `totalInclVat expected [169660.46] but found [155683.63]`; VAT mismatch
- **User perform CASS POST API - #1.1** — `priceNetExComm expected [66451.59999999998] but found [66451.6]` (floating-point precision)

### CASS TC14 change Product, Size, Placement & Date from Rialto
- **User perform CASS POST API - #1.1** — `priceNetExComm` / `priceNet` floating-point precision mismatches

### CASS TC15 2 products change date MH on head order line
- **User perform CASS POST API - #1.1** — `priceNetExComm` precision; `packageId/productId` order mismatch `[[AB, SVD]] vs [[SVD, AB]]`
- **User perform CASS GET API - #1.1** — `printDetails.netAmount expected [[165799.0, 128531.37]] but found [[158000.0, 128531.37]]`

### CASS TC18 2 products change size on not registered as head order line from MH
- **User perform CASS POST API - #1.1** — 500 Transaction rollback error; `moduleCode expected [[58, 54]] but found [[58, 58]]`

### CASS TC19 / TC20
- **User perform CASS POST API - #1.1** — `packageId/productId` array ordering mismatch

### CASS TC21 2 products change from draft to reserved
- **User perform CASS POST API - #1.1** (×2) — `priceNet` floating-point precision mismatches

### CASS TC22 in MH change from Full page to uppslag
- **User perform CASS POST API - #1.1** — 500 Transaction rollback error
- **User perform CASS GET API - #1.1** — `printDetails.paCode` and `plaCode` ordering/value mismatches

### CASS TC23 in MH change from Full page to uppslag - two orderlines change
- **Verify original full-page order state in MediaHouse - #1.1** — `printDetails.netAmount` floating-point precision mismatch
- **Verify updated MediaHouse basket state - #1.1** — `printDetails.netAmount` value mismatch
- **Verify reverted MediaHouse basket state - #1.1** — `netAmount expected [[33159.8, ...]] but found [[158000.0, ...]]`

### CASS TC24 in MH change from uppslag to Full page
- **Revert two MediaHouse order lines to full page - #1.1** — 500 Transaction rollback error
- **Verify created Rialto order and capture shared identifiers - #1.1** — `priceNet` floating-point precision
- **Verify original full-page order state in MediaHouse - #1.1** — `printDetails.netAmount` mismatch
- **Verify updated MediaHouse basket state - #1.1** — `paCode/plaCode` ordering mismatch
- **Verify reverted MediaHouse basket state - #1.1** — `paCode/plaCode` array size and ordering mismatch
- **Verify Rialto reflects the reverted full-page state - #1.1** — `Redundant path parameters: agencyPrisaId=7481. Undefined path parameters: uuid`

### CASS TC26 Basic order for magazines / TC32 Magazine (change date from Rialto)
- **Verify reverted MediaHouse basket state - #1.1** — `orderDiscount expected [0.00] but found [3600.00]`

### CASS TC27 Magazine (change date)
- **MEDIAHOUSE - Verify updated MediaHouse basket state - #1.1** — `discountType expected [[RIALTO]] but found [[NONE]]`
- **RIALTO - Verify Rialto reflects the reverted full-page state - #1.1** — `statusFlags expected [[]] but found [[PRELIMINARY]]`

### CASS TC29 Magazine (change to Uppslag/Spread/Panorama)
- **MEDIAHOUSE - Verify updated MediaHouse basket state - #1.1** — `commission expected [550.00] but found [341.00]`
- **RIALTO - Verify Rialto reflects the reverted full-page state - #1.1** — `priceNet expected [[10931.8]] but found [[10659.0]]`

### CASS TC30 Magazine (change Date & Size)
- **RIALTO - Verify Rialto reflects the reverted full-page state - #1.1** — `priceNet expected [[6000.0]] but found [[5814.0]]`; unexpected `commissionAmount`

### CASS TC31 Magazine (change Date, Size & Placement)
- **MEDIAHOUSE - Verify original full-page order state** — `orderDiscount expected [3600.00] but found [4800.00]`
- **MEDIAHOUSE - Verify updated MediaHouse basket state** — `commission expected [465.00] but found [155.00]`
- **RIALTO - Verify Rialto reflects the reverted full-page state** — `priceNet expected [[5000.0]] but found [[4845.0]]`

### CASS TC33 / TC36 Magazine (change size/product from Rialto)
- **MEDIAHOUSE - Verify updated magazine order state** — `orderDiscount expected [0.00] but found [4000.00]` / `[8800.00]`

### CASS TC34 Magazine (change to UPPSLAG from Rialto)
- **MEDIAHOUSE - Verify updated magazine order state** — `orderDiscount expected [0.00] but found [8800.00]`

### CASS TC35 Magazine (change Date Size & Placement from Rialto)
- **RIALTO - Verify updated Agency order after Rialto change** — `placementId expected [[SIDAN2]] but found [[HALVLIGG]]`; `issueDate` mismatch
- **MEDIAHOUSE - Verify updated magazine order state** — `INTEGRATION MISMATCH: MH basket ID (orBoxid) [7493] does not match Agency Prisa ID [7494]`
- **MEDIAHOUSE - Verify original magazine order state** — `orderDiscount expected [3600.00] but found [4800.00]`

### CASS TC36 Magazine (change Product Size Placement & Date from Rialto)
- **MEDIAHOUSE - Verify original magazine order state** — `orderDiscount expected [3600.00] but found [4800.00]`
- **MEDIAHOUSE - Verify updated magazine order state** — `orderDiscount expected [0.00] but found [4000.00]`

### CASS TC37 - 2 Products Magazine - changes the size in MH
- **MEDIAHOUSE - Verify original order state** — `totalInclVat expected [7368.00] but found [5814.00]`; VAT mismatch
- **MEDIAHOUSE - Verify updated MediaHouse basket state** — `commission expected [234.40] but found [229.40]`
- **RIALTO - Verify Rialto reflects the updated state** — `priceNet expected [[4969.0, 2325.6]] but found [[4845.0, 5814.0]]`
