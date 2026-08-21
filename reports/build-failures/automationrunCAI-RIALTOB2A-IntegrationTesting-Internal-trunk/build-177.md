# Build Failure Report

**Build ID:** 177
**Job:** automationrunCAI-RIALTOB2A-IntegrationTesting-Internal-trunk
**Date:** 2026-08-21 22:03:09 UTC
**Status:** UNSTABLE
**URL:** https://crossadv.atex.com/jenkins/job/automationrunCAI-RIALTOB2A-IntegrationTesting-Internal-trunk/177/

---

## Build Summary

| Metric | Value |
|---|---|
| Total Tests | 514 |
| Passed | 481 |
| Failed | 33 |
| Skipped | 0 |
| Pass Rate | 93.6% |

---

## Failing Tests / Steps

| Test Class | Step | Error (truncated) |
|---|---|---|
| CASS TC4 Change Placement | User perform CASS POST API | `statusFlags expected [[PRELIMINARY]] but found [[]]` |
| CASS TC5 change to Uppslag/Spread/Panorama | User perform CASS POST API | `discountAmount expected [0.0] but found [63660.63]` |
| CASS TC6 change date and size | User perform CASS POST API | `priceNetExComm expected [115320.00] but found [115320.0]` |
| CASS TC9 change size from Rialto | User waits for the server to complete the process | `discountAmount expected [0.0] but found [38197.97]` |
| CASS TC9 change size from Rialto | User perform CASS GET API | `depth expected [[184]] but found [[372]]` |
| CASS TC14 change Product, Size, Placement & Date from Rialto | User perform CASS POST API | `{"errorCode":1,"message":null} expected [N200] but found [N500]` |
| CASS TC14 change Product, Size, Placement & Date from Rialto | User perform CASS GET API | *(cascade from POST failure)* |
| CASS TC19 2 products change placement on head order from MH | User waits for the server to complete the process | `packageId expected [[AB, SVD]] but found [[SVD, AB]]` |
| CASS TC19 2 products change placement on head order from MH | User perform CASS POST API | `packageId expected [[AB, SVD]] but found [[SVD, AB]]` |
| CASS TC20 2 products change placement order for non head from MH | User waits for the server to complete the process | `placementId expected [[TEXT, SIDAN3]] but found [[TEXT, TEXT]]` |
| CASS TC22 in MH change from Full page to uppslag | User perform CASS GET API | `paCode expected [[SVDTI, AB, SVDTI, AB, AB, SVDTI]] but found [[AB, SVDTI, AB, AB, SVD...]]` |
| CASS TC22 in MH change from Full page to uppslag | Verify updated MH basket state | *(cascade)* |
| CASS TC24 in MH change from uppslag to Full page | Wait before starting MediaHouse revert flow | `placementId expected [[TEXT…TEXT]] but found [[UPPSLAG…UPPSLAG]]` |
| CASS TC24 in MH change from uppslag to Full page | Verify reverted MH basket state | *(cascade)* |
| CASS TC24 in MH change from uppslag to Full page | Verify Rialto reflects reverted full-page state | *(cascade)* |
| CASS TC28 Magazine (change size) | RIALTO - Re-authenticate / verify updated state | `statusFlags expected [[PRELIMINARY]] but found [[]]` |
| CASS TC29 Magazine (change to Uppslag/Spread/Panorama) | RIALTO - Re-authenticate / verify updated state | `statusFlags expected [[PRELIMINARY]] but found [[]]` |
| CASS TC31 Magazine (change Date, Size & Placement) | RIALTO - Re-authenticate / verify updated state | `priceNet expected [[5000.0]] but found [[4845.0]]` |
| CASS TC35 Magazine (change Date Size & Placement from Rialto) | Wait for Rialto update propagation | `placementId expected [[SIDAN2]] but found [[HALVLIGG]]` |
| CASS TC35 Magazine (change Date Size & Placement from Rialto) | MEDIAHOUSE - Refresh basket lookup after Rialto update | `MH basket ID (orBoxid) [8003] does not match Agency Prisa ID [8004]` |
| CASS TC35 Magazine (change Date Size & Placement from Rialto) | MEDIAHOUSE - Verify original magazine order state | *(cascade)* |
| CASS TC35 Magazine (change Date Size & Placement from Rialto) | MEDIAHOUSE - Verify updated magazine order state | *(cascade)* |
| CASS TC36 Magazine (change Product Size Placement & Date from Rialto) | MEDIAHOUSE - Verify updated magazine order state | `orderDiscount expected [0.00] but found [4000.00]` |
| CASS TC37 - 2 Products Magazine - changes the size in MH | Wait before switching to MediaHouse verification | `totalInclVat expected [7368.00] but found [5814.00]` |
| CASS TC37 - 2 Products Magazine - changes the size in MH | MEDIAHOUSE - Update MH order head line to change date | `commission expected [234.40] but found [229.40]` |
| CASS TC37 - 2 Products Magazine - changes the size in MH | RIALTO - Verify Rialto reflects updated state | `placementId expected [[HALVLIGG, TEXT]] but found [[TEXT, TEXT]]` |
