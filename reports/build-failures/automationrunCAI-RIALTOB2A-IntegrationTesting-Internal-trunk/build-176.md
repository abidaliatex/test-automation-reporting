# Build Failure Report

**Build ID:** 176
**Job:** automationrunCAI-RIALTOB2A-IntegrationTesting-Internal-trunk
**Date:** 2026-08-19 21:03:17 UTC
**Status:** UNSTABLE
**URL:** https://crossadv.atex.com/jenkins/job/automationrunCAI-RIALTOB2A-IntegrationTesting-Internal-trunk/176/

---

## Build Summary

| Metric | Value |
|---|---|
| Total Tests | 514 |
| Passed | 485 |
| Failed | 29 |
| Skipped | 0 |
| Pass Rate | 94.4% |

---

## Failing Tests / Steps

| Test Class | Step | Error (truncated) |
|---|---|---|
| CASS TC4 Change Placement | User perform CASS POST API | `statusFlags expected [[PRELIMINARY]] but found [[]]` |
| CASS TC5 change to Uppslag/Spread/Panorama | User perform CASS POST API | `discountAmount expected [0.0] but found [63660.63]` |
| CASS TC6 change date and size | User perform CASS POST API | `priceNetExComm expected [115320.00] but found [115320.0]` |
| CASS TC9 change size from Rialto | User perform CASS POST API | `discountAmount expected [0.0] but found [38197.97]` |
| CASS TC9 change size from Rialto | User perform CASS GET API | `depth expected [[184]] but found [[372]]` |
| CASS TC14 change Product, Size, Placement & Date from Rialto | User perform CASS POST API | `{"errorCode":1,"message":null} expected [N200] but found [N500]` |
| CASS TC14 change Product, Size, Placement & Date from Rialto | User perform CASS GET API | `paCode expected [[AB, SVDTI, AB, AB]] but found [[AB, SVDTI, SVDTI, AB]]` |
| CASS TC15 2 products change date MH on head order line | User perform CASS GET API | `paCode expected [[SVDTI, AB]] but found [[AB, SVDTI]]` |
| CASS TC19 2 products change placement on head order from MH | User perform CASS POST API | `packageId expected [[AB, SVD]] but found [[SVD, AB]]` |
| CASS TC20 2 products change placement order for non head from MH | User perform CASS POST API | `placementId expected [[TEXT, SIDAN3]] but found [[TEXT, ...]]` |
| CASS TC22 in MH change from Full page to uppslag | User perform CASS GET API (#1) | `paCode expected [[SVDTI, AB, SVDTI, AB, AB, SVD...]]` |
| CASS TC22 in MH change from Full page to uppslag | User perform CASS GET API (#2) | `netAmount expected [[128531.37, 33159.8, ...]]` |
| CASS TC22 in MH change from Full page to uppslag | User perform CASS GET API (#3) | `paCode expected [[SVDTI, AB, SVDTI, AB, AB, SVDTI]]` |
| CASS TC23 in MH change from Full page to uppslag - two orderlines | Verify updated MH basket state | `paCode expected [[SVDTI, SVDTI, AB, AB, AB, SVDTI]]` |
| CASS TC23 in MH change from Full page to uppslag - two orderlines | Verify reverted MH basket state | `paCode expected [[SVDTI, AB, SVDTI, AB, AB, SVDTI]]` |
| CASS TC24 in MH change from uppslag to Full page | Revert two MH order lines to full page | `placementId expected [[TEXT, TEXT, TEXT, TEX...]]` |
| CASS TC24 in MH change from uppslag to Full page | Verify reverted MH basket state | `paCode expected [[SVDTI, AB, SVDTI, AB, AB, SVDTI]]` |
| CASS TC24 in MH change from uppslag to Full page | Verify Rialto reflects reverted full-page state | `Redundant path parameters: agencyPrisaId=7932` |
| CASS TC28 Magazine (change size) | RIALTO - Verify Rialto reflects reverted full-page state | `statusFlags expected [[PRELIMINARY]] but found [[]]` |
| CASS TC29 Magazine (change to Uppslag/Spread/Panorama) | RIALTO - Verify Rialto reflects reverted full-page state | `statusFlags expected [[PRELIMINARY]] but found [[]]` |
| CASS TC31 Magazine (change Date, Size & Placement) | RIALTO - Verify Rialto reflects reverted full-page state | `priceNet expected [[5000.0]] but found [[4845.0]]` |
| CASS TC35 Magazine (change Date Size & Placement from Rialto) | RIALTO - Verify updated Agency order after Rialto change | `placementId expected [[SIDAN2]] but found [[HALVLIGG]]` |
| CASS TC35 Magazine (change Date Size & Placement from Rialto) | MEDIAHOUSE - Verify updated magazine order state in MH | `MH basket ID (orBoxid) [7942] does not match Agency Prisa ID [7943]` |
| CASS TC36 Magazine (change Product Size Placement & Date from Rialto) | MEDIAHOUSE - Verify original magazine order state | `orderDiscount expected [3600.00] but found [4800.xx]` |
| CASS TC36 Magazine (change Product Size Placement & Date from Rialto) | MEDIAHOUSE - Verify updated magazine order state | `orderDiscount expected [0.00] but found [4000.xx]` |
| CASS TC37 - 2 Products Magazine - changes the size in MH | MEDIAHOUSE - Verify original order state | `totalInclVat expected [7368.00] but found [5813.xx]` |
| CASS TC37 - 2 Products Magazine - changes the size in MH | MEDIAHOUSE - Verify updated MH basket state | `commission expected [234.40] but found [229.40]` |
| CASS TC37 - 2 Products Magazine - changes the size in MH | RIALTO - Verify Rialto reflects updated state | `placementId expected [[HALVLIGG, TEXT]] but found [[TEXT, HALVLIGG]]` |
