# Build Failure Report

**Build ID:** 172
**Job:** automationrunCAI-RIALTOB2A-IntegrationTesting-Internal-trunk
**Date:** 2026-08-15 22:43:18 UTC
**Status:** UNSTABLE
**URL:** https://crossadv.atex.com/jenkins/job/automationrunCAI-RIALTOB2A-IntegrationTesting-Internal-trunk/172/

---

## Summary

| Metric | Value |
|--------|-------|
| Total Tests | 514 |
| Passed | 488 |
| Failed | 26 |
| Skipped | 0 |
| Pass Rate | 94.9% |

---

## Failing Tests

| Feature / Class | Test Step | Error |
|---|---|---|
| CASS TC15 2 products change date MH on head order line | User perform CASS GET API - #1.1 | Mismatch: paCode/prodCode/issueDate array order wrong |
| CASS TC15 2 products change date MH on head order line | User perform CASS POST API - #1.1 | Mismatch: packageId/productId array order wrong; issueDate mismatch |
| CASS TC22 in MH change from Full page to uppslag | User perform CASS GET API - #1.1 (x3) | Mismatch: paCode/prodCode array order wrong; netAmount/grossAmount values wrong |
| CASS TC23 in MH change from Full page to uppslag - two orderlines change | Verify updated MediaHouse basket state - #1.1 | Mismatch: netAmount; orderDiscount expected 0.00 found 323621.09 |
| CASS TC23 in MH change from Full page to uppslag - two orderlines change | Verify reverted MediaHouse basket state - #1.1 | Mismatch: netAmount/grossAmount values wrong |
| CASS TC24 in MH change from uppslag to Full page | Revert two MediaHouse order lines to full page - #1.1 | 500 Transaction rolled back; expected N200 found N400 |
| CASS TC24 in MH change from uppslag to Full page | Verify reverted MediaHouse basket state - #1.1 | Mismatch: paCode/plaCode/prodCode array order wrong |
| CASS TC24 in MH change from uppslag to Full page | Verify Rialto reflects the reverted full-page state - #1.1 | Redundant path param agencyPrisaId=7778; uuid undefined |
| CASS TC28 Magazine (change size) | RIALTO - Verify Rialto reflects the reverted full-page state - #1.1 | statusFlags expected [PRELIMINARY] found [] |
| CASS TC29 Magazine (change to Uppslag/Spread/Panorama) | RIALTO - Verify Rialto reflects the reverted full-page state - #1.1 | statusFlags expected [PRELIMINARY] found [] |
| CASS TC31 Magazine (change Date, Size & Placement) | RIALTO - Verify Rialto reflects the reverted full-page state - #1.1 | priceNet expected 5000.0 found 4845.0; commissionAmount expected 0.0 found 155.0 |
| CASS TC35 Magazine (change Date Size & Placement from Rialto) | RIALTO - Verify updated Agency order after Rialto change - #1.1 | placementId expected SIDAN2 found HALVLIGG; issueDate/depth/price wrong |
| CASS TC35 Magazine (change Date Size & Placement from Rialto) | MEDIAHOUSE - Verify updated magazine order state in MediaHouse - #1.1 | MH basket ID mismatch: orBoxid 7788 vs Agency Prisa ID 7789 |
| CASS TC36 Magazine (change Product Size Placement & Date from Rialto) | MEDIAHOUSE - Verify original magazine order state - #1.1 | orderDiscount expected 3600.00 found 4800.00; netPrice/commission wrong |
| CASS TC36 Magazine (change Product Size Placement & Date from Rialto) | MEDIAHOUSE - Verify updated magazine order state - #1.1 | orderDiscount expected 0.00 found 4000.00; netPrice expected 5000 found 1000 |
| CASS TC37 - 2 Products Magazine - changes the size in MH | MEDIAHOUSE - Verify original order state in MediaHouse - #1.1 | totalInclVat expected 7368.00 found 5814.00; vat wrong |
| CASS TC37 - 2 Products Magazine - changes the size in MH | MEDIAHOUSE - Verify updated MediaHouse basket state - #1.1 | commission/totalInclVat/orderbasketSum wrong |
| CASS TC37 - 2 Products Magazine - changes the size in MH | RIALTO - Verify Rialto reflects the updated state - #1.1 | priceNet/commissionAmount/statusFlags wrong |
| CASS TC4 Change Placement | User perform CASS POST API - #1.1 | statusFlags expected [PRELIMINARY] found [] |
| CASS TC5 change to Uppslag/Spread/Panorama | User perform CASS POST API - #1.1 | discountAmount expected 0.0 found 63660.63; priceGross expected 250000 found 192192 |
| CASS TC6 change date and size | User perform CASS POST API - #1.1 | priceNetExComm format 115320.00 vs 115320.0; priceNet expected 115320.00 found 111745.08 |
| CASS TC9 change size from Rialto | User perform CASS POST API - #1.1 | discountAmount expected 0.0 found 38197.97; priceNetExComm expected 115320 found 77122.03 |
| CASS TC9 change size from Rialto | User perform CASS GET API - #1.1 | depth expected 184 found 372; netAmount/grossAmount wrong |
