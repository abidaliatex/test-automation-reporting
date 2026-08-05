# Build Failure Report

**Build ID:** 162
**Job:** automationrunCAI-RIALTOB2A-IntegrationTesting-Internal-trunk
**Date:** 2026-08-05
**Status:** UNSTABLE
**Build URL:** https://crossadv.atex.com/jenkins/job/automationrunCAI-RIALTOB2A-IntegrationTesting-Internal-trunk/162/

## Summary

| Metric | Value |
|---|---|
| Total Tests | 514 |
| Passed | 458 |
| Failed | 56 |
| Skipped | 0 |
| Pass Rate | 89.1% |

## Failing Tests / Steps

### CASS TC1 and TC2
- User perform CASS POST API - #1.1 — discountAmount expected [0.0] found [63660.63], statusFlags expected [PRELIMINARY] found [], priceNetExComm mismatch

### CASS TC11 change to UPPSLAG from Rialto
- User perform CASS GET API - #1.1 — totalInclVat, vat, orderTotalInclVat mismatch
- User perform CASS POST API - #1.1 — priceNetExComm floating-point precision mismatch (e.g. expected [66451.59999999998] found [66451.6])
- User perform CASS GET API - #1.1 — totalInclVat/vat mismatch (second scenario)

### CASS TC14 change Product, Size, Placement & Date from Rialto
- User perform CASS POST API - #1.1 (x2) — priceNetExComm / priceNet floating-point precision mismatch

### CASS TC15 2 products change date MH on head order line
- User perform CASS POST API - #1.1 — priceNetExComm precision mismatch
- User perform CASS GET API - #1.1 — netAmount, grossAmount, printGross, totalGross mismatch
- User perform CASS POST API - #1.1 — packageId/productId order mismatch, issueDate mismatch

### CASS TC18 2 products change size on not registered as head order line from MH
- User perform CASS POST API - #1.1 — 500 Transaction rolled back (rollback-only), expected N200 found N400
- User perform CASS POST API - #1.1 — moduleCode expected [58, 54] found [58, 58]

### CASS TC21 2 products change from draft to reserved
- User perform CASS POST API - #1.1 (x2) — priceNet / priceNetExComm floating-point precision mismatch

### CASS TC23 in MH change from Full page to uppslag - two orderlines change
- Verify created Rialto order and capture shared identifiers - #1.1 — priceNet/priceNetExComm precision mismatch
- Verify original full-page order state in MediaHouse - #1.1 — orderDiscount expected [0.00] found [588899.49], netPrice/commission mismatch
- Verify updated MediaHouse basket state - #1.1 — paCode, plaCode, prodCode, issueDate ordering mismatch
- Revert two MediaHouse order lines to full page - #1.1 — 500 Transaction rolled back
- Verify reverted MediaHouse basket state - #1.1 — paCode, plaCode, prodCode, issueDate ordering mismatch

### CASS TC24 in MH change from uppslag to Full page
- Verify created Rialto order and capture shared identifiers - #1.1 — priceNet/priceNetExComm precision mismatch
- Verify original full-page order state in MediaHouse - #1.1 — orderDiscount expected [0.00] found [1467477.60], netPrice mismatch
- Verify updated MediaHouse basket state - #1.1 — orderDiscount mismatch (1244124.80), netPrice mismatch
- Revert two MediaHouse order lines to full page - #1.1 — placementId expected TEXT found UPPSLAG, issueDate mismatch
- Verify reverted MediaHouse basket state - #1.1 — paCode, plaCode, prodCode ordering mismatch
- Verify Rialto reflects the reverted full-page state - #1.1 — Redundant path parameter agencyPrisaId, undefined path param uuid

### CASS TC26 Basic order for magazines
- Verify reverted MediaHouse basket state - #1.1 — orderDiscount expected [0.00] found [3600.00], netPrice expected [6000.00] found [2400.00]

### CASS TC27 Magazine (change date)
- MEDIAHOUSE - Verify updated MediaHouse basket state - #1.1 — discountType expected [RIALTO] found [NONE]

### CASS TC28 Magazine (change size)
- MEDIAHOUSE - Verify updated MediaHouse basket state - #1.1 — commission, orderbasketSum, totalInclVat mismatch
- RIALTO - Verify Rialto reflects the reverted full-page state - #1.1 — priceNet, discountAmount, commissionAmount, priceNetExComm mismatch

### CASS TC3 change Size
- User perform CASS POST API - #1.1 — discountAmount expected [0.0] found [63660.63], statusFlags expected [PRELIMINARY] found []

### CASS TC30 Magazine (change Date & Size)
- RIALTO - Verify Rialto reflects the reverted full-page state - #1.1 — priceNet, discountAmount, commissionAmount mismatch

### CASS TC31 Magazine (change Date, Size & Placement)
- MEDIAHOUSE - Verify original full-page order state in MediaHouse - #1.1 — orderDiscount, sumDiscount, netPrice, commission mismatch
- MEDIAHOUSE - Verify updated MediaHouse basket state - #1.1 — commission expected [465.00] found [250.00]
- RIALTO - Verify Rialto reflects the reverted full-page state - #1.1 — priceNet, discountAmount mismatch

### CASS TC32 Magazine (change date from Rialto)
- MEDIAHOUSE - Verify updated magazine order state in MediaHouse - #1.1 — orderDiscount expected [0.00] found [3600.00], netPrice expected [6000.00] found [2400.00]

### CASS TC33 Magazine (change size from Rialto)
- MEDIAHOUSE - Verify updated magazine order state in MediaHouse - #1.1 — orderDiscount expected [0.00] found [4000.00]

### CASS TC34 Magazine (change to UPPSLAG from Rialto)
- MEDIAHOUSE - Verify updated magazine order state in MediaHouse - #1.1 — orderDiscount expected [0.00] found [8800.00], netPrice expected [11000.00] found [2200.00]

### CASS TC35 Magazine (change Date Size & Placement from Rialto)
- MEDIAHOUSE - Verify original magazine order state in MediaHouse - #1.1 — orderDiscount, netPrice, commission mismatch
- RIALTO - Verify updated Agency order after Rialto change - #1.1 — placementId, issueDate, depth, priceGross mismatch
- MEDIAHOUSE - Verify updated magazine order state in MediaHouse - #1.1 — INTEGRATION MISMATCH: MH basket ID [7321] does not match Agency Prisa ID [7322]

### CASS TC36 Magazine (change Product Size Placement & Date from Rialto)
- MEDIAHOUSE - Verify original magazine order state in MediaHouse - #1.1 — orderDiscount, netPrice mismatch
- MEDIAHOUSE - Verify updated magazine order state in MediaHouse - #1.1 — orderDiscount expected [0.00] found [4000.00]

### CASS TC37 - 2 Products Magazine - changes the size in MH
- MEDIAHOUSE - Verify original order state in MediaHouse - #1.1 — totalInclVat, vat mismatch
- MEDIAHOUSE - Verify updated MediaHouse basket state - #1.1 — paCode, plaCode, prodCode, issueDate, depth ordering mismatch

### CASS TC4 Change Placement
- User perform CASS GET API - #1.1 — discountType expected [NONE] found [RIALTO], commission mismatch
- User perform CASS POST API - #1.1 — discountAmount expected [0.0] found [230000.0], statusFlags expected [PRELIMINARY] found []

### CASS TC5 change to Uppslag/Spread/Panorama
- User perform CASS GET API - #1.1 — commission, orderbasketSum, totalInclVat mismatch
- User perform CASS POST API - #1.1 — discountAmount expected [0.0] found [63660.63], placementId expected [UPPSLAG] found [TEXT]

### CASS TC6 change to date and size on the order line
- User perform CASS POST API - #1.1 — discountAmount expected [0.0] found [63660.63], statusFlags expected [PRELIMINARY] found []

### CASS TC9 change size from Rialto
- User perform CASS POST API - #1.1 — discountAmount expected [0.0] found [38197.97], priceNetExComm mismatch
- User perform CASS GET API - #1.1 — depth expected [184] found [372], discountType expected [NONE] found [RIALTO]
