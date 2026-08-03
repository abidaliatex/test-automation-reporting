# Build Failure Report

**Build ID:** 160
**Job:** automationrunCAI-RIALTOB2A-IntegrationTesting-Internal-trunk
**Date:** 2026-08-03 21:03:18 UTC
**Status:** UNSTABLE
**URL:** https://crossadv.atex.com/jenkins/job/automationrunCAI-RIALTOB2A-IntegrationTesting-Internal-trunk/160/

---

## Build Summary

- **Total Tests:** 514
- **Passed:** 450
- **Failed:** 64
- **Skipped:** 0
- **Pass Rate:** 87.5%

---

## Failing Tests / Steps

### rialtoB2A(CASS TC1 and TC2)
- User perform CASS POST API - #1.1 — `discountAmount expected [63660.63] found [63660.630000000005]`
- User perform CASS POST API - #1.1 — `orderHeader.statusFlags expected [[PRELIMINARY]] found [[]]`

### rialtoB2A(CASS TC3 change Size)
- User perform CASS POST API - #1.1 — `discountAmount expected [63660.63] found [63660.630000000005]`
- User perform CASS POST API - #1.1 — `statusFlags expected [[PRELIMINARY]] found [[]]`, `priceNetExComm expected [115320.00] found [115320.0]`

### rialtoB2A(CASS TC4 Change Placement)
- User perform CASS POST API - #1.1 — `discountAmount expected [63660.63] found [63660.630000000005]`
- User perform CASS GET API - #1.1 — `discountType expected [[NONE]] found [[RIALTO]]`, commission/total mismatch
- User perform CASS POST API - #1.1 — `discountAmount expected [0.0] found [63660.63]`, `priceGross expected [250000.00] found [192192.0]`

### rialtoB2A(CASS TC5 change to Uppslag/Spread/Panorama)
- User perform CASS POST API - #1.1 — `discountAmount expected [63660.63] found [63660.630000000005]`
- User perform CASS GET API - #1.1 — commission/total mismatch
- User perform CASS POST API - #1.1 — `discountAmount expected [0.0] found [63660.63]`, `priceGross expected [250000.00] found [192192.0]`

### rialtoB2A(CASS TC6 change to changes the date and the size on the order line.)
- User perform CASS POST API - #1.1 — `discountAmount expected [63660.63] found [63660.630000000005]`
- User perform CASS POST API - #1.1 — `statusFlags expected [[PRELIMINARY]] found [[]]`, price formatting mismatches

### rialtoB2A(CASS TC9 change size from Rialto)
- User perform CASS POST API - #1.1 — `discountAmount expected [63660.63] found [63660.630000000005]`
- User perform CASS POST API - #1.1 — `discountAmount expected [0.0] found [38197.97]`
- User perform CASS GET API - #1.1 — `discountType expected [[NONE]] found [[RIALTO]]`, `netAmount` mismatch

### rialtoB2A(CASS TC11 change to UPPSLAG from Rialto)
- User perform CASS POST API - #1.1 — `discountAmount expected [63660.63] found [63660.630000000005]`
- User perform CASS GET API - #1.1 — `totalInclVat`, `vat`, `orderTotalInclVat` mismatches
- User perform CASS POST API - #1.1 — `priceNetExComm`, `priceNet` floating-point mismatches
- User perform CASS GET API - #1.1 — `discountType expected [[null]] found [[RIALTO]]`

### rialtoB2A(CASS TC14 change Product, Size, Placement & Date from Rialto)
- User perform CASS POST API - #1.1 — `priceNetExComm`, `priceNet` floating-point mismatches (multiple steps)

### rialtoB2A(CASS TC15 2 products change date MH on head order line)
- User perform CASS POST API - #1.1 — `discountAmount`, `priceNetExComm` floating-point mismatches
- User perform CASS GET API - #1.1 — `discountType expected [[null, null]] found [[RIALTO, RIALTO]]`
- User perform CASS GET API - #1.1 — `printDetails.netAmount`, `grossAmount`, basket total mismatches
- User perform CASS POST API - #1.1 — `packageId`, `productId`, `issueDate` ordering mismatch

### rialtoB2A(CASS TC18 2 products change size on not registered as head order line from MH)
- User perform CASS POST API - #1.1 — HTTP 500: `Transaction rolled back because it has been marked as rollback-only`
- User perform CASS POST API - #1.1 — `moduleCode expected [[58, 54]] found [[58, 58]]`

### rialtoB2A(CASS TC21 2 products change from draft to reserved)
- User perform CASS POST API - #1.1 — `priceNet`, `discountAmount` floating-point mismatches (two occurrences)

### rialtoB2A(CASS TC22 in MH change from Full page to uppslag)
- User perform CASS POST API - #1.1 — `priceNet`, `discountAmount` floating-point mismatches
- User perform CASS GET API - #1.1 — `printDetails.netAmount` floating-point mismatches, basket total mismatch
- User perform CASS POST API - #1.1 — `packageId`, `placementId` ordering mismatch
- User perform CASS GET API - #1.1 — `printDetails.netAmount`, `grossAmount` mismatches (two occurrences)

### rialtoB2A(CASS TC23 in MH change from Full page to uppslag - two orderlines change)
- Verify created Rialto order and capture shared identifiers - #1.1 — `priceNet` floating-point mismatch
- Verify original full-page order state in MediaHouse - #1.1 — `printDetails.netAmount` floating-point mismatch, basket total
- Verify updated MediaHouse basket state - #1.1 — `paCode`, `plaCode` ordering mismatch
- Verify reverted MediaHouse basket state - #1.1 — `paCode`, `plaCode` ordering mismatch

### rialtoB2A(CASS TC24 in MH change in MH change from uppslag to Full page)
- Verify created Rialto order and capture shared identifiers - #1.1 — `priceNet` floating-point mismatch
- Verify original full-page order state in MediaHouse - #1.1 — `printDetails.netAmount` floating-point mismatch, basket total
- Verify updated MediaHouse basket state - #1.1 — `printDetails.netAmount` floating-point mismatch, basket total
- Revert two MediaHouse order lines to full page - #1.1 — `placementId`, `issueDate` ordering mismatch
- Verify reverted MediaHouse basket state - #1.1 — `paCode`, `plaCode` ordering mismatch
- Verify Rialto reflects the reverted full-page state - #1.1 — `Redundant path parameters: agencyPrisaId=7225. Undefined path parameters: uuid`

### rialtoB2A(CASS TC26 Basic order for magazines)
- Verify reverted MediaHouse basket state - #1.1 — `orderDiscount expected [0.00] found [3600.00]`, basket total mismatch

### rialtoB2A(CASS TC27 Magazine (change date))
- MEDIAHOUSE - Verify updated MediaHouse basket state - #1.1 — `discountType expected [[RIALTO]] found [[NONE]]`

### rialtoB2A(CASS TC28 Magazine (change size))
- MEDIAHOUSE - Verify updated MediaHouse basket state - #1.1 — `commission expected [155.00] found [250.00]`, totals mismatch
- RIALTO - Verify Rialto reflects the reverted full-page state - #1.1 — `priceNet expected [[4845.0]] found [[4969.0]]`, commission mismatch

### rialtoB2A(CASS TC30 Magazine (change Date & Size))
- RIALTO - Verify Rialto reflects the reverted full-page state - #1.1 — `priceNet expected [[6000.0]] found [[5962.8]]`, commission mismatch

### rialtoB2A(CASS TC31 Magazine (change Date, Size & Placement))
- MEDIAHOUSE - Verify original full-page order state in MediaHouse - #1.1 — `orderDiscount expected [3600.00] found [4800.00]`, basket total mismatch
- MEDIAHOUSE - Verify updated MediaHouse basket state - #1.1 — `commission expected [465.00] found [250.00]`, totals mismatch
- RIALTO - Verify Rialto reflects the reverted full-page state - #1.1 — `priceNet expected [[5000.0]] found [[4969.0]]`, commission mismatch

### rialtoB2A(CASS TC32 Magazine (change date from Rialto))
- MEDIAHOUSE - Verify updated magazine order state in MediaHouse - #1.1 — `orderDiscount expected [0.00] found [3600.00]`, basket total mismatch

### rialtoB2A(CASS TC33 Magazine (change size from Rialto))
- MEDIAHOUSE - Verify updated magazine order state in MediaHouse - #1.1 — `orderDiscount expected [0.00] found [4000.00]`, basket total mismatch

### rialtoB2A(CASS TC34 Magazine (change to UPPSLAG from Rialto))
- MEDIAHOUSE - Verify updated magazine order state in MediaHouse - #1.1 — `orderDiscount expected [0.00] found [8800.00]`, basket total mismatch

### rialtoB2A(CASS TC35 Magazine (change Date Size & Placement from Rialto))
- MEDIAHOUSE - Verify original magazine order state in MediaHouse - #1.1 — `orderDiscount expected [3600.00] found [4800.00]`
- RIALTO - Verify updated Agency order after Rialto change - #1.1 — `placementId expected [[SIDAN2]] found [[HALVLIGG]]`, date/size/dimension mismatch
- MEDIAHOUSE - Verify updated magazine order state in MediaHouse - #1.1 — `INTEGRATION MISMATCH: MH basket ID [7235] does not match Agency Prisa ID [7236]`

### rialtoB2A(CASS TC36 Magazine (change Product Size Placement & Date from Rialto))
- MEDIAHOUSE - Verify original magazine order state in MediaHouse - #1.1 — `orderDiscount expected [3600.00] found [4800.00]`
- MEDIAHOUSE - Verify updated magazine order state in MediaHouse - #1.1 — `orderDiscount expected [0.00] found [4000.00]`

### rialtoB2A(CASS TC37 - 2 Products Magazine - changes the size in MH)
- MEDIAHOUSE - Verify original order state in MediaHouse - #1.1 — `discountType expected [[null, null]] found [[RIALTO, RIALTO]]`, totalInclVat mismatch
- MEDIAHOUSE - Verify updated MediaHouse basket state - #1.1 — `paCode`, `plaCode`, `prodCode` ordering mismatch
