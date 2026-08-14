# Build Failure Report

**Build ID:** 171
**Job:** automationrunCAI-RIALTOB2A-IntegrationTesting-Internal-trunk
**Date:** 2026-08-14 21:03:18 UTC
**Status:** UNSTABLE
**URL:** https://crossadv.atex.com/jenkins/job/automationrunCAI-RIALTOB2A-IntegrationTesting-Internal-trunk/171/

---

## Summary

| Metric | Value |
|--------|-------|
| Total Tests | 514 |
| Passed | 465 |
| Failed | 49 |
| Skipped | 0 |
| Pass Rate | 90.5% |

---

## Failing Tests

| Feature / Class | Test Step | Error |
|---|---|---|
| CASS TC15 2 products change date MH on head order line | User perform CASS GET API - #1.1 | Mismatch: paCode/prodCode/issueDate array order wrong |
| CASS TC15 2 products change date MH on head order line | User perform CASS POST API - #1.1 | Mismatch: packageId/productId array order wrong |
| CASS TC19 2 products change placement on head order from MH | User perform CASS POST API - #1.1 | Mismatch: packageId/productId array order wrong |
| CASS TC22 in MH change from Full page to uppslag | User perform CASS GET API - #1.1 (x3) | Mismatch: paCode array order / netAmount values wrong |
| CASS TC23 in MH change from Full page to uppslag - two orderlines change | Verify updated/reverted MediaHouse basket state - #1.1 | Mismatch: printDetails.netAmount values wrong |
| CASS TC24 in MH change from uppslag to Full page | Revert two MediaHouse order lines to full page - #1.1 | placementId expected TEXT found UPPSLAG |
| CASS TC24 in MH change from uppslag to Full page | Verify reverted MediaHouse basket state - #1.1 | Mismatch: paCode array order wrong |
| CASS TC24 in MH change from uppslag to Full page | Verify Rialto reflects the reverted full-page state - #1.1 | Redundant path param agencyPrisaId; uuid undefined |
| CASS TC28 Magazine (change size) | RIALTO - Verify Rialto reflects the reverted full-page state - #1.1 | statusFlags expected [PRELIMINARY] found [] |
| CASS TC29 Magazine (change to Uppslag/Spread/Panorama) | RIALTO - Verify Rialto reflects the reverted full-page state - #1.1 | statusFlags expected [PRELIMINARY] found [] |
| CASS TC31 Magazine (change Date, Size & Placement) | MEDIAHOUSE - User perform CASS POST API | Basket not found for campaign: TestCase31 |
| CASS TC31 Magazine (change Date, Size & Placement) | MEDIAHOUSE - Verify original full-page order state - #1.1 | Undefined path parameter: mhBasketOrderId |
| CASS TC31 Magazine (change Date, Size & Placement) | MEDIAHOUSE - Update two MediaHouse order lines to uppslag - #1.1 | No MH odIds found in TestContext |
| CASS TC31 Magazine (change Date, Size & Placement) | MEDIAHOUSE - Verify updated MediaHouse basket state - #1.1 | Undefined path parameter: mhBasketOrderId |
| CASS TC31 Magazine (change Date, Size & Placement) | RIALTO - Verify Rialto reflects the reverted full-page state - #1.1 | Mismatch: placementId/issueDate wrong |
| CASS TC32 Magazine (change date from Rialto) | MEDIAHOUSE - User perform CASS POST API | Basket not found for campaign: TestCase32 |
| CASS TC32 Magazine (change date from Rialto) | MEDIAHOUSE - Verify original magazine order state - #1.1 | Undefined path parameter: mhBasketOrderId |
| CASS TC32 Magazine (change date from Rialto) | MEDIAHOUSE - Refresh basket lookup after Rialto update | Basket not found for campaign: TestCase32 |
| CASS TC32 Magazine (change date from Rialto) | MEDIAHOUSE - Verify updated magazine order state - #1.1 | Undefined path parameter: mhBasketOrderId |
| CASS TC33 Magazine (change size from Rialto) | MEDIAHOUSE - Verify updated magazine order state - #1.1 | Mismatch: plaCode expected HALVLIGG found TEXT; depth expected 146 found 297 |
| CASS TC34 Magazine (change to UPPSLAG from Rialto) | MEDIAHOUSE - User perform CASS POST API | Basket not found for campaign: TestCase34 |
| CASS TC34 Magazine (change to UPPSLAG from Rialto) | MEDIAHOUSE - Verify original magazine order state - #1.1 | Undefined path parameter: mhBasketOrderId |
| CASS TC34 Magazine (change to UPPSLAG from Rialto) | MEDIAHOUSE - Refresh basket lookup after Rialto update | Basket not found for campaign: TestCase34 |
| CASS TC34 Magazine (change to UPPSLAG from Rialto) | MEDIAHOUSE - Verify updated magazine order state - #1.1 | Undefined path parameter: mhBasketOrderId |
| CASS TC35 Magazine (change Date Size & Placement from Rialto) | MEDIAHOUSE - User perform CASS POST API | Basket not found for campaign: TestCase35 |
| CASS TC35 Magazine (change Date Size & Placement from Rialto) | MEDIAHOUSE - Verify original magazine order state - #1.1 | Undefined path parameter: mhBasketOrderId |
| CASS TC35 Magazine (change Date Size & Placement from Rialto) | RIALTO - Verify updated Agency order after Rialto change - #1.1 | Mismatch: placementId/issueDate wrong |
| CASS TC35 Magazine (change Date Size & Placement from Rialto) | MEDIAHOUSE - Refresh basket lookup after Rialto update | Basket not found for campaign: TestCase34 |
| CASS TC35 Magazine (change Date Size & Placement from Rialto) | MEDIAHOUSE - Verify updated magazine order state - #1.1 | Undefined path parameter: mhBasketOrderId |
| CASS TC36 Magazine (change Product Size Placement & Date from Rialto) | MEDIAHOUSE - Verify original magazine order state - #1.1 | Mismatch: orderDiscount expected 3600 found 4800 |
| CASS TC36 Magazine (change Product Size Placement & Date from Rialto) | MEDIAHOUSE - Verify updated magazine order state - #1.1 | Mismatch: paCode expected ANA found KOT; plaCode expected HALVLIGG found SIDAN |
| CASS TC37 - 2 Products Magazine - changes the size in MH | MEDIAHOUSE - User connect and authenticate | Basket not found for campaign: TestCase37 |
| CASS TC37 - 2 Products Magazine - changes the size in MH | MEDIAHOUSE - Verify original order state - #1.1 | Undefined path parameter: mhBasketOrderId |
| CASS TC37 - 2 Products Magazine - changes the size in MH | MEDIAHOUSE - Update MediaHouse order head line to change date - #1.1 | No MH odIds found in TestContext |
| CASS TC37 - 2 Products Magazine - changes the size in MH | MEDIAHOUSE - Verify updated MediaHouse basket state - #1.1 | Undefined path parameter: mhBasketOrderId |
| CASS TC37 - 2 Products Magazine - changes the size in MH | RIALTO - Verify Rialto reflects the updated state - #1.1 | Mismatch: placementId expected HALVLIGG/TEXT found TEXT/TEXT |
| CASS TC4 Change Placement | User perform CASS POST API | Basket not found for campaign: TestCase04 |
| CASS TC4 Change Placement | User perform CASS GET API - #1.1 | Undefined path parameter: mhBasketOrderId |
| CASS TC4 Change Placement | User perform CASS POST API - #1.1 | (no error detail) |
| CASS TC4 Change Placement | User perform CASS GET API - #1.1 | Undefined path parameter: mhBasketOrderId |
| CASS TC4 Change Placement | User perform CASS POST API - #1.1 | Mismatch: discountAmount/priceGross/orderHeader values wrong |
| CASS TC5 change to Uppslag/Spread/Panorama | User perform CASS POST API - #1.1 | Mismatch: discountAmount expected 0.0 found 63660.63; priceGross expected 250000 found 192192 |
| CASS TC6 change date and size | User perform CASS POST API - #1.1 | Mismatch: priceNetExComm format 115320.00 vs 115320.0 |
| CASS TC7 Change Date, Size & Placement | User perform CASS POST API - #1.1 | Mismatch: discountAmount expected 0.0 found 63660.63 |
| CASS TC9 change size from Rialto | User perform CASS POST API - #1.1 | Mismatch: discountAmount expected 0.0 found 38197.97 |
| CASS TC9 change size from Rialto | User perform CASS GET API - #1.1 | Mismatch: netAmount/discountAmount wrong |
