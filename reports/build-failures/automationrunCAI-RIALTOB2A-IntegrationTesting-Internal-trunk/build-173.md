# Build Failure Report

**Build ID:** 173
**Job:** automationrunCAI-RIALTOB2A-IntegrationTesting-Internal-trunk
**Date:** 2026-08-16
**Status:** UNSTABLE
**URL:** https://crossadv.atex.com/jenkins/job/automationrunCAI-RIALTOB2A-IntegrationTesting-Internal-trunk/173/

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
| CASS TC4 Change Placement | User perform CASS POST API | `orderHeader.statusFlags` expected `[PRELIMINARY]` but found `[]` |
| CASS TC5 change to Uppslag/Spread/Panorama | User perform CASS POST API | `discountAmount` expected `0.0` found `63660.63`; `priceGross` expected `250000.00` found `192192.0`; `placementId` mismatch |
| CASS TC6 change date and size on order line | User perform CASS POST API | `priceNet` expected `115320.00` found `111745.08`; commission amount mismatch |
| CASS TC15 2 products change date MH | CASS GET API | `paCode`/`prodCode`/`issueDate`/`netAmount` ordering wrong |
| CASS TC15 2 products change date MH | CASS POST API | `packageId`/`productId` ordering mismatch; `issueDate` wrong |
| CASS TC22 in MH change Full page to uppslag | CASS GET API (×3) | `paCode`/`prodCode` ordering wrong; `netAmount`/`grossAmount` mismatch |
| CASS TC23 in MH change Full page to uppslag (two lines) | Verify updated MH basket | `netAmount` rounding `33159.79999999999` vs `33159.8`; `orderDiscount` expected `0.00` found `323621.09` |
| CASS TC23 in MH change Full page to uppslag (two lines) | Verify reverted MH basket | `netAmount` expected `33159.8` found `158000.0` |
| CASS TC24 in MH change uppslag to Full page | Verify updated MH basket | `paCode`/`plaCode`/`prodCode` ordering mismatch |
| CASS TC24 in MH change uppslag to Full page | Revert two MH order lines | HTTP 500 – Transaction rolled back (rollback-only) |
| CASS TC24 in MH change uppslag to Full page | Verify reverted MH basket | `plaCode` all `UPPSLAG` instead of `TEXT` |
| CASS TC24 in MH change uppslag to Full page | Verify Rialto reflects reverted state | Path params error: `agencyPrisaId=7815` redundant, `uuid` undefined |
| CASS TC28 Magazine change size | RIALTO - Verify reverted state | `statusFlags` expected `[PRELIMINARY]` found `[]` |
| CASS TC29 Magazine change to Uppslag | RIALTO - Verify reverted state | `statusFlags` expected `[PRELIMINARY]` found `[]` |
| CASS TC31 Magazine change Date/Size/Placement | RIALTO - Verify reverted state | `priceNet` expected `5000.0` found `4845.0`; commission `0.0` vs `155.0` |
| CASS TC35 Magazine change Date/Size/Placement from Rialto | RIALTO - Verify updated Agency order | `placementId` `SIDAN2` vs `HALVLIGG`; wrong date/depth/price |
| CASS TC35 Magazine change Date/Size/Placement from Rialto | MEDIAHOUSE - Verify updated state | MH basket ID `7825` ≠ Agency Prisa ID `7826` |
| CASS TC36 Magazine change Product/Size/Placement/Date from Rialto | MEDIAHOUSE - Verify original state | `orderDiscount` `3600.00` vs `4800.00`; `netPrice` `2400.00` vs `1200.00` |
| CASS TC36 Magazine change Product/Size/Placement/Date from Rialto | MEDIAHOUSE - Verify updated state | `orderDiscount` `0.00` vs `4000.00`; `netPrice` `5000.00` vs `1000.00` |
| CASS TC37 2 Products Magazine size change in MH | MEDIAHOUSE - Verify original state | `totalInclVat` `7368.00` vs `5814.00`; `vat` `2913.60` vs `1162.80` |
| CASS TC37 2 Products Magazine size change in MH | MEDIAHOUSE - Verify updated MH basket | `commission` `234.40` vs `229.40`; `totalInclVat` `9734.00` vs `8963.25` |
| CASS TC37 2 Products Magazine size change in MH | RIALTO - Verify updated state | `priceNet` `4969.0` vs `4845.0`; commission/statusFlags mismatch |
