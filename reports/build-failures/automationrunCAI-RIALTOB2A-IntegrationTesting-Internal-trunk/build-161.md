# Build Failure Report — Build 161

**Build ID:** 161
**Job:** automationrunCAI-RIALTOB2A-IntegrationTesting-Internal-trunk
**Date:** 2026-08-04 21:03:15 UTC
**Status:** UNSTABLE
**URL:** https://crossadv.atex.com/jenkins/job/automationrunCAI-RIALTOB2A-IntegrationTesting-Internal-trunk/161/

---

## Build Summary

| Metric | Value |
|---|---|
| Total Tests | 514 |
| Passed | 459 |
| Failed | 55 |
| Skipped | 0 |
| Pass Rate | 89.3% |

---

## Failing Tests / Steps

| Feature (Class) | Scenario / Step | Error Summary |
|---|---|---|
| CASS TC1 and TC2 | User perform CASS POST API | orderHeader.statusFlags expected [[PRELIMINARY]] but found [[]] |
| CASS TC11 change to UPPSLAG from Rialto | User perform CASS GET API (#1) | totalInclVat, vat mismatch |
| CASS TC11 change to UPPSLAG from Rialto | User perform CASS POST API | priceNetExComm, priceNet floating-point mismatch |
| CASS TC11 change to UPPSLAG from Rialto | User perform CASS GET API (#2) | discountType expected [[null]] found [[RIALTO]] |
| CASS TC14 change Product, Size, Placement & Date from Rialto | User perform CASS POST API (#1) | priceNetExComm floating-point mismatch |
| CASS TC14 change Product, Size, Placement & Date from Rialto | User perform CASS POST API (#2) | priceNet floating-point mismatch |
| CASS TC15 2 products change date MH on head order line | User perform CASS POST API (#1) | priceNetExComm floating-point mismatch |
| CASS TC15 2 products change date MH on head order line | User perform CASS GET API (#1) | discountType expected [[null, null]] found [[RIALTO, RIALTO]] |
| CASS TC15 2 products change date MH on head order line | User perform CASS GET API (#2) | printDetails.netAmount, grossAmount mismatch |
| CASS TC15 2 products change date MH on head order line | User perform CASS POST API (#2) | packageId/productId ordering mismatch |
| CASS TC18 2 products change size not registered head | User perform CASS POST API (#1) | 500 Transaction rolled back (rollback-only) |
| CASS TC18 2 products change size not registered head | User perform CASS POST API (#2) | moduleCode expected [[58,54]] found [[58,58]] |
| CASS TC21 2 products change from draft to reserved | User perform CASS POST API (#1) | priceNet floating-point mismatch |
| CASS TC21 2 products change from draft to reserved | User perform CASS POST API (#2) | priceNet floating-point mismatch |
| CASS TC22 in MH change from Full page to uppslag | User perform CASS GET API (#1) | totalOrderNetPrice expected [485073.51] found [1073973.00] |
| CASS TC22 in MH change from Full page to uppslag | User perform CASS GET API (#2) | printDetails.netAmount mismatch |
| CASS TC22 in MH change from Full page to uppslag | User perform CASS GET API (#3) | printDetails.netAmount mismatch |
| CASS TC23 in MH change from Full page to uppslag (two orderlines) | Verify created Rialto order | priceNet floating-point mismatch |
| CASS TC23 in MH change from Full page to uppslag (two orderlines) | Verify original full-page order state | printDetails.netAmount mismatch |
| CASS TC23 in MH change from Full page to uppslag (two orderlines) | Verify updated MH basket state | printDetails.paCode ordering mismatch |
| CASS TC23 in MH change from Full page to uppslag (two orderlines) | Revert two MH order lines | 500 Transaction rolled back (rollback-only) |
| CASS TC23 in MH change from Full page to uppslag (two orderlines) | Verify reverted MH basket state | printDetails.paCode ordering mismatch |
| CASS TC24 in MH change from uppslag to Full page | Verify created Rialto order | priceNet floating-point mismatch |
| CASS TC24 in MH change from uppslag to Full page | Verify original full-page order state | printDetails.netAmount mismatch |
| CASS TC24 in MH change from uppslag to Full page | Verify updated MH basket state | printDetails.netAmount mismatch |
| CASS TC24 in MH change from uppslag to Full page | Revert two MH order lines | placementId expected [[TEXT...]] found [[UPPSLAG...]] |
| CASS TC24 in MH change from uppslag to Full page | Verify reverted MH basket state | printDetails.paCode ordering mismatch |
| CASS TC24 in MH change from uppslag to Full page | Verify Rialto reflects reverted state | Redundant/undefined path parameters (agencyPrisaId/uuid) |
| CASS TC26 Basic order for magazines | Verify reverted MH basket state | orderDiscount/sumDiscount expected [0.00] found [3600.00] |
| CASS TC27 Magazine (change date) | MEDIAHOUSE - Verify updated MH basket state | discountType expected [[RIALTO]] found [[NONE]] |
| CASS TC28 Magazine (change size) | MEDIAHOUSE - Verify updated MH basket state | commission/orderbasketSum mismatch |
| CASS TC28 Magazine (change size) | RIALTO - Verify Rialto reflects reverted state | priceNet/commissionAmount mismatch |
| CASS TC3 change Size | User perform CASS POST API | statusFlags expected [[PRELIMINARY]] found [[]], priceNetExComm mismatch |
| CASS TC30 Magazine (change Date & Size) | RIALTO - Verify Rialto reflects reverted state | priceNet/commissionAmount mismatch |
| CASS TC31 Magazine (change Date, Size & Placement) | MEDIAHOUSE - Verify original full-page order state | orderDiscount/sumDiscount mismatch |
| CASS TC31 Magazine (change Date, Size & Placement) | MEDIAHOUSE - Verify updated MH basket state | commission/orderbasketSum mismatch |
| CASS TC31 Magazine (change Date, Size & Placement) | RIALTO - Verify Rialto reflects reverted state | priceNet/commissionAmount mismatch |
| CASS TC32 Magazine (change date from Rialto) | MEDIAHOUSE - Verify updated magazine order state | orderDiscount/sumDiscount expected [0.00] found [3600.00] |
| CASS TC33 Magazine (change size from Rialto) | MEDIAHOUSE - Verify updated magazine order state | orderDiscount/sumDiscount expected [0.00] found [4000.00] |
| CASS TC34 Magazine (change to UPPSLAG from Rialto) | MEDIAHOUSE - Verify updated magazine order state | orderDiscount/sumDiscount expected [0.00] found [8800.00] |
| CASS TC35 Magazine (change Date Size & Placement from Rialto) | MEDIAHOUSE - Verify original magazine order state | orderDiscount/sumDiscount mismatch |
| CASS TC35 Magazine (change Date Size & Placement from Rialto) | RIALTO - Verify updated Agency order | placementId/issueDate mismatch |
| CASS TC35 Magazine (change Date Size & Placement from Rialto) | MEDIAHOUSE - Verify updated magazine order state | INTEGRATION MISMATCH: MH basket ID [7284] ≠ Agency Prisa ID [7285] |
| CASS TC36 Magazine (change Product Size Placement & Date from Rialto) | MEDIAHOUSE - Verify original magazine order state | orderDiscount/sumDiscount mismatch |
| CASS TC36 Magazine (change Product Size Placement & Date from Rialto) | MEDIAHOUSE - Verify updated magazine order state | orderDiscount/sumDiscount expected [0.00] found [4000.00] |
| CASS TC37 - 2 Products Magazine - changes the size in MH | MEDIAHOUSE - Verify original order state | discountType expected [[null, null]] found [[RIALTO, RIALTO]] |
| CASS TC37 - 2 Products Magazine - changes the size in MH | MEDIAHOUSE - Verify updated MH basket state | discountType expected [[null, NONE]] found [[RIALTO, NONE]] |
| CASS TC4 Change Placement | User perform CASS GET API | discountType expected [[NONE]] found [[RIALTO]], commission mismatch |
| CASS TC4 Change Placement | User perform CASS POST API | priceGross, statusFlags, priceNetExComm mismatch |
| CASS TC5 change to Uppslag/Spread/Panorama | User perform CASS GET API | commission/orderbasketSum mismatch |
| CASS TC5 change to Uppslag/Spread/Panorama | User perform CASS POST API | discountAmount, priceGross, statusFlags mismatch |
| CASS TC6 change date and size on order line | User perform CASS POST API | statusFlags expected [[PRELIMINARY]] found [[]] |
| CASS TC9 change size from Rialto | User perform CASS POST API | discountAmount/priceNetExComm mismatch |
| CASS TC9 change size from Rialto | User perform CASS GET API | depth/moduleCode mismatch |
