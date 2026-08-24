# Build Failure Report

## Build Info

| Field | Value |
|---|---|
| **Build ID** | 180 |
| **Job** | automationrunCAI-RIALTOB2A-IntegrationTesting-Internal-trunk |
| **Date** | 2026-08-24 |
| **Status** | UNSTABLE |
| **Duration** | ~94 min |
| **URL** | https://crossadv.atex.com/jenkins/job/automationrunCAI-RIALTOB2A-IntegrationTesting-Internal-trunk/180/ |

## Test Results

| Metric | Count |
|---|---|
| Total Tests | 514 |
| Passed | 467 |
| Failed | 47 |
| Skipped | 0 |
| Pass Rate | 90.9% |

## Failing Tests

| Suite | Test Step | Error Summary |
|---|---|---|
| CASS TC4 Change Placement | User perform CASS POST API | statusFlags expected [PRELIMINARY] but found [] |
| CASS TC5 change to Uppslag/Spread/Panorama | User perform CASS POST API | discountAmount expected [0.0] but found [63660.63]; priceGross mismatch |
| CASS TC6 change date and size | User perform CASS POST API | priceNetExComm / priceGross type mismatch (decimal format) |
| CASS TC9 change size from Rialto | User perform CASS POST API | discountAmount expected [0.0] but found [38197.97]; discountType expected [NONE] |
| CASS TC9 change size from Rialto | User perform CASS GET API | netAmount / discountAmount / discountType mismatch |
| CASS TC14 change Product, Size, Placement & Date from Rialto | User perform CASS GET API (#1) | printDetails.paCode / prodCode ordering mismatch |
| CASS TC14 change Product, Size, Placement & Date from Rialto | User perform CASS POST API | errorCode:1 expected N200 but found N500 |
| CASS TC14 change Product, Size, Placement & Date from Rialto | User perform CASS GET API (#2) | printDetails.paCode / plaCode ordering mismatch |
| CASS TC15 2 products change date MH on head order line | User perform CASS GET API (#1) | paCode / prodCode / netAmount ordering mismatch |
| CASS TC15 2 products change date MH on head order line | User perform CASS GET API (#2) | paCode / plaCode / prodCode array length/ordering mismatch |
| CASS TC19 2 products change placement on head order from MH | User perform CASS POST API | packageId / productId ordering mismatch |
| CASS TC20 2 products change placement order for non head from MH | User perform CASS POST API | placementId ordering mismatch |
| CASS TC22 in MH change from Full page to uppslag | User perform CASS GET API (#1) | paCode / prodCode ordering mismatch |
| CASS TC22 in MH change from Full page to uppslag | User perform CASS POST API (#1) | Transaction rolled back — rollback-only (N400) |
| CASS TC22 in MH change from Full page to uppslag | User perform CASS GET API (#2) | paCode / plaCode ordering mismatch |
| CASS TC22 in MH change from Full page to uppslag | User perform CASS POST API (#2) | Transaction rolled back — rollback-only (N400) |
| CASS TC22 in MH change from Full page to uppslag | User perform CASS GET API (#3) | paCode / prodCode ordering mismatch |
| CASS TC23 two orderlines change | Verify updated MediaHouse basket state | paCode / plaCode ordering mismatch |
| CASS TC23 two orderlines change | Verify reverted MediaHouse basket state | paCode / prodCode ordering mismatch |
| CASS TC24 change from uppslag to Full page | Verify updated MediaHouse basket state | paCode / plaCode ordering mismatch |
| CASS TC24 change from uppslag to Full page | Revert two MediaHouse order lines | Transaction rolled back — rollback-only (N400) |
| CASS TC24 change from uppslag to Full page | Verify reverted MediaHouse basket state | paCode / plaCode mismatch |
| CASS TC24 change from uppslag to Full page | Verify Rialto reflects the reverted state | Path parameter error: agencyPrisaId vs uuid |
| CASS TC28 Magazine (change size) | RIALTO - Verify reverted state | statusFlags expected [PRELIMINARY] but found [] |
| CASS TC29 Magazine (change to Uppslag/Spread/Panorama) | RIALTO - Verify reverted state | statusFlags expected [PRELIMINARY] but found [] |
| CASS TC35 Magazine (change Date Size & Placement from Rialto) | RIALTO - Verify updated Agency order | placementId / issueDate / depth mismatch |
| CASS TC35 Magazine (change Date Size & Placement from Rialto) | MEDIAHOUSE - Verify updated magazine order | orBoxid [8131] != agencyPrisaId [8132] |
| CASS TC36 Magazine (change Product Size Placement & Date from Rialto) | MEDIAHOUSE - Verify original state | orderDiscount / netPrice mismatch |
| CASS TC36 Magazine (change Product Size Placement & Date from Rialto) | MEDIAHOUSE - Verify updated state | orderDiscount expected [0.00] but found [4000.00] |
| CASS TC37 - 2 Products Magazine - changes size in MH | MEDIAHOUSE - Verify original state | totalInclVat / vat mismatch |
| CASS TC37 - 2 Products Magazine - changes size in MH | MEDIAHOUSE - Verify updated basket state | paCode / plaCode / prodCode ordering mismatch |
| CASS TC37 - 2 Products Magazine - changes size in MH | RIALTO - Verify updated state | placementId / depth / materialId mismatch |
