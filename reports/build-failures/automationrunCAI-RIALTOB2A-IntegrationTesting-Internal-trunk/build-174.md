# Build Failure Report

**Build ID:** 174  
**Job:** automationrunCAI-RIALTOB2A-IntegrationTesting-Internal-trunk  
**Date:** 2026-08-17  
**Status:** UNSTABLE  
**URL:** https://crossadv.atex.com/jenkins/job/automationrunCAI-RIALTOB2A-IntegrationTesting-Internal-trunk/174/

---

## Build Summary

| Metric | Value |
|---|---|
| Total Tests | 514 |
| Passed | 484 |
| Failed | 30 |
| Skipped | 0 |
| Pass Rate | 94.2% |

---

## Failing Tests / Steps

| Test Class | Step | Error Summary |
|---|---|---|
| CASS TC14 change Product, Size, Placement & Date from Rialto | User perform CASS POST API | `errorCode` expected `N200` found `N500` |
| CASS TC14 change Product, Size, Placement & Date from Rialto | User perform CASS GET API | `paCode/prodCode/plaCode` and amount mismatches |
| CASS TC15 2 products change date MH on head order line | User perform CASS GET API | `paCode/prodCode` ordering mismatch |
| CASS TC18 2 products change size (non-head) from MH | User perform CASS POST API | `moduleCode` expected `[58, 54]` found `[58, 58]` |
| CASS TC19 2 products change placement on head order from MH | User perform CASS POST API | `packageId/productId` ordering mismatch |
| CASS TC20 2 products change placement (non-head) from MH | User perform CASS POST API | `placementId` expected `[TEXT, SIDAN3]` found `[TEXT, TEXT]` |
| CASS TC22 in MH change from Full page to uppslag | User perform CASS GET API (x3) | `paCode/prodCode` ordering and amount mismatches |
| CASS TC23 in MH change from Full page to uppslag (two order lines) | Verify updated/reverted MH basket | `paCode/prodCode` ordering and amount mismatches |
| CASS TC23 in MH change from Full page to uppslag (two order lines) | Revert two MH order lines to full page | HTTP 500 rollback-only transaction |
| CASS TC24 in MH change from uppslag to Full page | Revert/verify reverted state | `placementId/paCode/prodCode` mismatches |
| CASS TC24 in MH change from uppslag to Full page | Verify Rialto reverted state | Path params error (`agencyPrisaId` redundant, `uuid` undefined) |
| CASS TC28 Magazine (change size) | RIALTO verify reverted state | `statusFlags` expected `[PRELIMINARY]` found `[]` |
| CASS TC29 Magazine (change to Uppslag/Spread/Panorama) | RIALTO verify reverted state | `statusFlags` expected `[PRELIMINARY]` found `[]` |
| CASS TC31 Magazine (change Date, Size & Placement) | RIALTO verify reverted state | price/commission mismatch |
| CASS TC35 Magazine (change Date Size & Placement from Rialto) | RIALTO verify updated Agency order | placement/date/depth mismatch |
| CASS TC35 Magazine (change Date Size & Placement from Rialto) | MEDIAHOUSE verify updated state | Basket ID mismatch (`orBoxid` vs Agency Prisa ID) |
| CASS TC36 Magazine (change Product Size Placement & Date from Rialto) | MEDIAHOUSE verify original/updated state | `orderDiscount/sumDiscount/netPrice` mismatches |
| CASS TC37 - 2 Products Magazine - changes the size in MH | MEDIAHOUSE verify original/updated state | commission and totals mismatch |
| CASS TC37 - 2 Products Magazine - changes the size in MH | RIALTO verify updated state | placement/depth/price/status mismatches |
| CASS TC4 Change Placement | User perform CASS POST API | `statusFlags` expected `[PRELIMINARY]` found `[]` |
| CASS TC5 change to Uppslag/Spread/Panorama | User perform CASS POST API | discount and gross-price mismatches |
| CASS TC6 change date and size on order line | User perform CASS POST API | `priceNet/priceGross/commission` mismatches |
| CASS TC9 change size from Rialto | User perform CASS POST API + GET API | discount/net amounts mismatches |
