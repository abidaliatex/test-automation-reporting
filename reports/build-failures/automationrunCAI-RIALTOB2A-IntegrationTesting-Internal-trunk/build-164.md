# Build Failure Report

## Build Info

| Field | Value |
|---|---|
| **Build ID** | 164 |
| **Job** | automationrunCAI-RIALTOB2A-IntegrationTesting-Internal-trunk |
| **Date** | 2026-08-07 |
| **Status** | UNSTABLE |
| **URL** | https://crossadv.atex.com/jenkins/job/automationrunCAI-RIALTOB2A-IntegrationTesting-Internal-trunk/164/ |

## Test Results

| Metric | Count |
|---|---|
| Total Tests | 514 |
| Passed | 456 |
| Failed | 58 |
| Skipped | 0 |
| Pass Rate | 88.7% |

## Failing Tests

| Feature Class | Scenario | Error Summary |
|---|---|---|
| rialtoB2A(CASS TC1 and TC2) | User perform CASS GET API - #1.1 (x2) | Invalid number of path parameters: mhBasketOrderId undefined |
| rialtoB2A(CASS TC1 and TC2) | User perform CASS POST API - #1.1 | discountAmount expected [0.0] but found [63660.63]; priceNetExComm mismatch |
| rialtoB2A(CASS TC3 change Size) | User perform CASS POST API - #1.1 | priceNetExComm expected [115320.00] but found [115320.0]; priceGross precision mismatch |
| rialtoB2A(CASS TC4 Change Placement) | User perform CASS POST API - #1.1 | statusFlags expected [[PRELIMINARY]] but found [[]]; priceGross precision mismatch |
| rialtoB2A(CASS TC5 change to Uppslag/Spread/Panorama) | User perform CASS POST API - #1.1 | discountAmount expected [0.0] but found [63660.63]; priceGross expected [250000.00] but found [192192.0] |
| rialtoB2A(CASS TC6 change date and size) | User perform CASS POST API - #1.1 | priceNetExComm expected [115320.00] but found [115320.0]; priceGross precision mismatch |
| rialtoB2A(CASS TC7 Change Date, Size & Placement) | User perform CASS POST API - #1.1 | discountAmount expected [0.0] but found [63660.63]; priceGross expected [1090.0] but found [192192.0] |
| rialtoB2A(CASS TC9 change size from Rialto) | User perform CASS POST API - #1.1 | discountAmount expected [0.0] but found [38197.97]; priceNetExComm expected [115320.00] but found [77122.03] |
| rialtoB2A(CASS TC9 change size from Rialto) | User perform CASS GET API - #1.1 | depth expected [[184]] but found [[372]]; moduleCode expected [[54]] but found [[58]] |
| rialtoB2A(CASS TC11 change to UPPSLAG from Rialto) | User perform CASS GET API - #1.1 (x2) | totalInclVat mismatch; vat mismatch |
| rialtoB2A(CASS TC11 change to UPPSLAG from Rialto) | User perform CASS POST API - #1.1 | priceNetExComm floating-point precision mismatch (66451.59999999998 vs 66451.6) |
| rialtoB2A(CASS TC14 change Product, Size, Placement & Date) | User perform CASS POST API - #1.1 (x2) | priceNetExComm/priceNet floating-point precision mismatches |
| rialtoB2A(CASS TC15 2 products change date MH on head order line) | User perform CASS POST API - #1.1 | priceNetExComm precision mismatch (33159.79999999999 vs 33159.8) |
| rialtoB2A(CASS TC15 2 products change date MH on head order line) | User perform CASS GET API - #1.1 | netAmount expected [[165799.0, 128531.37]] but found [[158000.0, 128531.37]] |
| rialtoB2A(CASS TC15 2 products change date MH on head order line) | User perform CASS POST API - #1.1 | packageId/productId ordering: expected [[AB, SVD]] but found [[SVD, AB]] |
| rialtoB2A(CASS TC18 2 products change size) | User perform CASS POST API - #1.1 | HTTP 500 Transaction rolled back |
| rialtoB2A(CASS TC18 2 products change size) | User perform CASS POST API - #1.1 | moduleCode expected [[58, 54]] but found [[58, 58]] |
| rialtoB2A(CASS TC21 2 products change from draft to reserved) | User perform CASS POST API - #1.1 (x2) | priceNet precision mismatch (32131.849999999988 vs 32131.85) |
| rialtoB2A(CASS TC23 MH change Full page to uppslag) | Verify original full-page order state in MediaHouse - #1.1 | netAmount precision mismatch (33159.79999999999 vs 33159.8) |
| rialtoB2A(CASS TC23 MH change Full page to uppslag) | Verify updated MediaHouse basket state - #1.1 | netAmount mismatch |
| rialtoB2A(CASS TC23 MH change Full page to uppslag) | Verify reverted MediaHouse basket state - #1.1 | netAmount expected [[33159.8, ...]] but found [[158000.0, ...]] |
| rialtoB2A(CASS TC24 MH change uppslag to Full page) | Verify created Rialto order - #1.1 | priceNet precision mismatch (64391.59999999998 vs 64391.6) |
| rialtoB2A(CASS TC24 MH change uppslag to Full page) | Verify original full-page order state - #1.1 | netAmount precision mismatch |
| rialtoB2A(CASS TC24 MH change uppslag to Full page) | Verify updated MediaHouse basket state - #1.1 | netAmount mismatch |
| rialtoB2A(CASS TC24 MH change uppslag to Full page) | Revert two MediaHouse order lines - #1.1 | placementId expected [[TEXT,...]] but found [[UPPSLAG,...]] |
| rialtoB2A(CASS TC24 MH change uppslag to Full page) | Verify reverted MediaHouse basket state - #1.1 | paCode ordering mismatch |
| rialtoB2A(CASS TC24 MH change uppslag to Full page) | Verify Rialto reflects the reverted state - #1.1 | Path parameters: agencyPrisaId redundant, uuid undefined |
| rialtoB2A(CASS TC26 Basic order for magazines) | Verify reverted MediaHouse basket state - #1.1 | orderDiscount expected [0.00] but found [3600.00] |
| rialtoB2A(CASS TC27 Magazine (change date)) | MEDIAHOUSE - Verify updated MediaHouse basket state - #1.1 | discountType expected [[RIALTO]] but found [[NONE]] |
| rialtoB2A(CASS TC27 Magazine (change date)) | RIALTO - Verify Rialto reflects the reverted full-page state - #1.1 | statusFlags expected [[]] but found [[PRELIMINARY]] |
| rialtoB2A(CASS TC29 Magazine (change to Uppslag/Spread/Panorama)) | RIALTO - Verify Rialto reflects the reverted full-page state - #1.1 | priceNet expected [[10931.8]] but found [[10659.0]]; commissionAmount mismatch |
| rialtoB2A(CASS TC30 Magazine (change Date & Size)) | RIALTO - Verify Rialto reflects the reverted full-page state - #1.1 | priceNet expected [[6000.0]] but found [[5814.0]]; commissionAmount expected [[0.0]] but found [[186.0]] |
| rialtoB2A(CASS TC31 Magazine (change Date, Size & Placement)) | MEDIAHOUSE - Verify original full-page order state in MediaHouse - #1.1 | orderDiscount expected [3600.00] but found [4800.00] |
| rialtoB2A(CASS TC31 Magazine (change Date, Size & Placement)) | MEDIAHOUSE - Verify updated MediaHouse basket state - #1.1 | commission expected [465.00] but found [155.00]; orderbasketSum mismatch |
| rialtoB2A(CASS TC31 Magazine (change Date, Size & Placement)) | RIALTO - Verify Rialto reflects the reverted full-page state - #1.1 | priceNet expected [[5000.0]] but found [[4845.0]]; commissionAmount expected [[0.0]] but found [[155.0]] |
| rialtoB2A(CASS TC32 Magazine (change date from Rialto)) | MEDIAHOUSE - Verify updated magazine order state in MediaHouse - #1.1 | INTEGRATION MISMATCH: MH basket ID [4745] does not match Agency Prisa ID [7415] |
| rialtoB2A(CASS TC33 Magazine (change size from Rialto)) | MEDIAHOUSE - Verify updated magazine order state in MediaHouse - #1.1 | orderDiscount expected [0.00] but found [4000.00] |
| rialtoB2A(CASS TC34 Magazine (change to UPPSLAG from Rialto)) | MEDIAHOUSE - Verify updated magazine order state in MediaHouse - #1.1 | orderDiscount expected [0.00] but found [8800.00] |
| rialtoB2A(CASS TC35 Magazine (change Date Size & Placement from Rialto)) | MEDIAHOUSE - Verify original magazine order state in MediaHouse - #1.1 | INTEGRATION MISMATCH: MH basket ID [5231] does not match Agency Prisa ID [7418] |
| rialtoB2A(CASS TC35 Magazine (change Date Size & Placement from Rialto)) | RIALTO - Verify updated Agency order after Rialto change - #1.1 | placementId expected [[SIDAN2]] but found [[HALVLIGG]]; issueDate mismatch |
| rialtoB2A(CASS TC35 Magazine (change Date Size & Placement from Rialto)) | MEDIAHOUSE - Verify updated magazine order state in MediaHouse - #1.1 | INTEGRATION MISMATCH: MH basket ID [5231] does not match Agency Prisa ID [7418] |
| rialtoB2A(CASS TC36 Magazine (change Product Size Placement & Date from Rialto)) | MEDIAHOUSE - Verify original magazine order state in MediaHouse - #1.1 | orderDiscount expected [3600.00] but found [4800.00] |
| rialtoB2A(CASS TC36 Magazine (change Product Size Placement & Date from Rialto)) | MEDIAHOUSE - Verify updated magazine order state in MediaHouse - #1.1 | orderDiscount expected [0.00] but found [4000.00] |
| rialtoB2A(CASS TC37 - 2 Products Magazine - changes the size in MH) | MEDIAHOUSE - Verify original order state in MediaHouse - #1.1 | totalInclVat expected [7368.00] but found [5814.00]; vat mismatch |
| rialtoB2A(CASS TC37 - 2 Products Magazine - changes the size in MH) | MEDIAHOUSE - Verify updated MediaHouse basket state - #1.1 | commission expected [234.40] but found [229.40] |
| rialtoB2A(CASS TC37 - 2 Products Magazine - changes the size in MH) | RIALTO - Verify Rialto reflects the updated state - #1.1 | priceNet expected [[4969.0, 2325.6]] but found [[4845.0, 5814.0]]; discountAmount mismatch |
