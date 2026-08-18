# Build Failure Report

**Build ID:** 175  
**Job:** automationrunCAI-RIALTOB2A-IntegrationTesting-Internal-trunk  
**Date:** 2026-08-18  
**Status:** UNSTABLE  
**URL:** https://crossadv.atex.com/jenkins/job/automationrunCAI-RIALTOB2A-IntegrationTesting-Internal-trunk/175/

---

## Build Summary

| Metric | Value |
|---|---|
| Total Tests | 514 |
| Passed | 486 |
| Failed | 28 |
| Skipped | 0 |
| Pass Rate | 94.6% |

---

## Failing Tests / Steps

| Test Class | Step | Error Summary |
|---|---|---|
| CASS TC14 change Product, Size, Placement & Date from Rialto | User perform CASS POST API | `errorCode` expected `N200` found `N500` |
| CASS TC14 change Product, Size, Placement & Date from Rialto | User perform CASS GET API | `paCode/printDetails` mismatch |
| CASS TC15 2 products change date MH on head order line | User perform CASS GET API | `paCode/prodCode` order mismatch |
| CASS TC19 2 products change placement on head order from MH | User perform CASS POST API | `packageId/productId` order mismatch |
| CASS TC20 2 products change placement order for non head from MH | User perform CASS POST API | `placementId` mismatch (`TEXT,SIDAN3` vs `TEXT,TEXT`) |
| CASS TC22 in MH change from Full page to uppslag | User perform CASS GET API (3 failures) | `paCode/prodCode/netAmount` mismatches |
| CASS TC23 in MH change from Full page to uppslag (two orderlines change) | Verify updated MediaHouse basket state | `netAmount` mismatch |
| CASS TC23 in MH change from Full page to uppslag (two orderlines change) | Verify reverted MediaHouse basket state | `netAmount` mismatch |
| CASS TC24 in MH change from uppslag to Full page | Revert two MediaHouse order lines to full page | `placementId` not reverted (still `UPPSLAG`) |
| CASS TC24 in MH change from uppslag to Full page | Verify reverted MediaHouse basket state | `paCode/prodCode` mapping mismatch |
| CASS TC24 in MH change from uppslag to Full page | Verify Rialto reflects reverted state | Path params invalid (`agencyPrisaId` redundant, `uuid` undefined) |
| CASS TC28 Magazine (change size) | RIALTO verify reverted full-page state | `statusFlags` expected `[PRELIMINARY]` found `[]` |
| CASS TC29 Magazine (change to Uppslag/Spread/Panorama) | RIALTO verify reverted full-page state | `statusFlags` expected `[PRELIMINARY]` found `[]` |
| CASS TC31 Magazine (change Date, Size & Placement) | RIALTO verify reverted full-page state | `priceNet/commission` mismatch |
| CASS TC35 Magazine (change Date Size & Placement from Rialto) | RIALTO verify updated Agency order | `placementId/issueDate/depth` mismatch |
| CASS TC35 Magazine (change Date Size & Placement from Rialto) | MEDIAHOUSE verify updated order state | `orBoxid` mismatch vs Agency Prisa ID |
| CASS TC36 Magazine (change Product Size Placement & Date from Rialto) | MEDIAHOUSE verify original order state | `orderDiscount/sumDiscount/netPrice` mismatch |
| CASS TC36 Magazine (change Product Size Placement & Date from Rialto) | MEDIAHOUSE verify updated order state | `orderDiscount/sumDiscount/netPrice` mismatch |
| CASS TC37 - 2 Products Magazine - changes the size in MH | MEDIAHOUSE verify original order state | `totalInclVat/vat` mismatch |
| CASS TC37 - 2 Products Magazine - changes the size in MH | MEDIAHOUSE verify updated basket state | `commission/orderbasketSummary` mismatch |
| CASS TC37 - 2 Products Magazine - changes the size in MH | RIALTO verify updated state | `placementId/depth/statusFlags` mismatch |
| CASS TC4 Change Placement | User perform CASS POST API | `statusFlags` expected `[PRELIMINARY]` found `[]` |
| CASS TC5 change to Uppslag/Spread/Panorama | User perform CASS POST API | `discountAmount/priceGross` mismatch |
| CASS TC6 changes date and size on order line | User perform CASS POST API | `priceGross/commission/priceNetExComm` mismatch |
| CASS TC9 change size from Rialto | User perform CASS POST API | `discountAmount/priceNetExComm` mismatch |
| CASS TC9 change size from Rialto | User perform CASS GET API | `depth/moduleCode` mismatch |
