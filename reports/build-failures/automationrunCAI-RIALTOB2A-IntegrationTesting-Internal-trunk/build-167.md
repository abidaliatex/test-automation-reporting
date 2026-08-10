# Build Failure Report — Build 167

**Build ID:** 167
**Job:** automationrunCAI-RIALTOB2A-IntegrationTesting-Internal-trunk
**Date:** 2026-08-10
**Status:** UNSTABLE
**URL:** https://crossadv.atex.com/jenkins/job/automationrunCAI-RIALTOB2A-IntegrationTesting-Internal-trunk/167/

---

## Test Results

| Metric | Count |
|---|---|
| Total Tests | 514 |
| Passed | 474 |
| Failed | 40 |
| Skipped | 0 |
| Pass Rate | 92.2% |

---

## Failing Tests / Steps

### rialtoB2A(CASS TC15 2 products change date MH on head order line)
- **User perform CASS GET API - #1.1** — Mismatch on printDetails ordering: paCode, prodCode, issueDate, netAmount array order wrong
- **User perform CASS POST API - #1.1** — Mismatch on orderAdDetails ordering: packageId, productId, issueDate arrays in wrong order

### rialtoB2A(CASS TC22 in MH change from Full page to uppslag)
- **User perform CASS GET API - #1.1** (×2) — Mismatch: paCode/plaCode/prodCode array ordering; plaCode expected TEXT but got UPPSLAG; width/moduleCode mismatch
- **User perform CASS POST API - #1.1** — HTTP 500 Transaction rolled back (rollback-only); expected N200 but got N400

### rialtoB2A(CASS TC23 in MH change from Full page to uppslag - two orderlines change)
- **Verify original full-page order state in MediaHouse - #1.1** — netAmount precision mismatch; orderDiscount expected 0.00 but found 588899.49
- **Verify updated MediaHouse basket state - #1.1** — netAmount precision; orderDiscount expected 0.00 but found 323621.09
- **Verify reverted MediaHouse basket state - #1.1** — netAmount mismatch (expected 33159.8, found 158000.0)

### rialtoB2A(CASS TC24 in MH change from uppslag to Full page)
- **Verify created Rialto order and capture shared identifiers - #1.1** — priceNet/priceNetExComm floating-point precision
- **Verify original full-page order state in MediaHouse - #1.1** — netAmount precision; orderDiscount expected 0.00 but found 1467477.60
- **Verify updated MediaHouse basket state - #1.1** — netAmount precision; orderDiscount expected 0.00 but found 1244124.80
- **Revert two MediaHouse order lines to full page - #1.1** — placementId expected TEXT, got UPPSLAG; issueDate mismatch
- **Verify reverted MediaHouse basket state - #1.1** — paCode/plaCode/prodCode array ordering wrong
- **Verify Rialto reflects the reverted full-page state - #1.1** — `IllegalArgumentException`: Redundant path param `agencyPrisaId=7547`, undefined `uuid`

### rialtoB2A(CASS TC26 Basic order for magazines)
- **Verify reverted MediaHouse basket state - #1.1** — orderDiscount expected 0.00 but found 3600.00; netPrice expected 6000.00 but found 2400.00

### rialtoB2A(CASS TC27 Magazine (change date))
- **MEDIAHOUSE - Verify updated MediaHouse basket state - #1.1** — discountType expected RIALTO but found NONE
- **RIALTO - Verify Rialto reflects the reverted full-page state - #1.1** — statusFlags expected [] but found [PRELIMINARY]

### rialtoB2A(CASS TC29 Magazine (change to Uppslag/Spread/Panorama))
- **MEDIAHOUSE - Verify updated MediaHouse basket state - #1.1** — commission expected 550.00 but found 341.00; orderbasketSum/totalInclVat wrong
- **RIALTO - Verify Rialto reflects the reverted full-page state - #1.1** — priceNet expected 10931.8 but found 10659.0; commissionAmount wrong

### rialtoB2A(CASS TC3 change Size)
- **User perform CASS POST API - #1.1** — priceNet expected 115320.00 but found 111745.08; precision mismatch on priceNetExComm/priceGross

### rialtoB2A(CASS TC30 Magazine (change Date & Size))
- **RIALTO - Verify Rialto reflects the reverted full-page state - #1.1** — priceNet 6000.0 vs 5814.0; commissionAmount 0.0 vs 186.0; statusFlags [] vs [PRELIMINARY]

### rialtoB2A(CASS TC31 Magazine (change Date, Size & Placement))
- **MEDIAHOUSE - Verify original full-page order state in MediaHouse - #1.1** — orderDiscount 3600.00 vs 4800.00; netPrice 2400.00 vs 1200.00
- **MEDIAHOUSE - Verify updated MediaHouse basket state - #1.1** — commission 465.00 vs 155.00; orderbasketSum/totalInclVat wrong
- **RIALTO - Verify Rialto reflects the reverted full-page state - #1.1** — priceNet 5000.0 vs 4845.0; commissionAmount 0.0 vs 155.0

### rialtoB2A(CASS TC32 Magazine (change date from Rialto))
- **MEDIAHOUSE - Verify updated magazine order state in MediaHouse - #1.1** — orderDiscount expected 0.00 but found 3600.00; netPrice expected 6000.00 but found 2400.00

### rialtoB2A(CASS TC33 Magazine (change size from Rialto))
- **MEDIAHOUSE - Verify updated magazine order state in MediaHouse - #1.1** — orderDiscount expected 0.00 but found 4000.00; netPrice expected 5000.00 but found 1000.00

### rialtoB2A(CASS TC34 Magazine (change to UPPSLAG from Rialto))
- **MEDIAHOUSE - Verify updated magazine order state in MediaHouse - #1.1** — orderDiscount expected 0.00 but found 8800.00; netPrice expected 11000.00 but found 2200.00

### rialtoB2A(CASS TC35 Magazine (change Date Size & Placement from Rialto))
- **MEDIAHOUSE - Verify original magazine order state in MediaHouse - #1.1** — orderDiscount 3600.00 vs 4800.00; netPrice 2400.00 vs 1200.00
- **RIALTO - Verify updated Agency order after Rialto change - #1.1** — placementId SIDAN2 vs HALVLIGG; issueDate wrong; depth 297 vs 146
- **MEDIAHOUSE - Verify updated magazine order state in MediaHouse - #1.1** — Integration mismatch: MH basket orBoxid [7557] ≠ Agency Prisa ID [7558]

### rialtoB2A(CASS TC36 Magazine (change Product Size Placement & Date from Rialto))
- **MEDIAHOUSE - Verify original magazine order state in MediaHouse - #1.1** — orderDiscount 3600.00 vs 4800.00; netPrice 2400.00 vs 1200.00
- **MEDIAHOUSE - Verify updated magazine order state in MediaHouse - #1.1** — orderDiscount expected 0.00 but found 4000.00; netPrice 5000.00 vs 1000.00

### rialtoB2A(CASS TC37 - 2 Products Magazine - changes the size in MH)
- **MEDIAHOUSE - Verify original order state in MediaHouse - #1.1** — totalInclVat 7368.00 vs 5814.00; vat/orderTotalInclVat mismatch
- **MEDIAHOUSE - Verify updated MediaHouse basket state - #1.1** — paCode/plaCode/prodCode/issueDate array ordering wrong
- **RIALTO - Verify Rialto reflects the updated state - #1.1** — priceNet/discountAmount/commissionAmount wrong

### rialtoB2A(CASS TC4 Change Placement)
- **User perform CASS POST API - #1.1** — statusFlags expected [PRELIMINARY] but found []; decimal format 250000.00 vs 250000.0

### rialtoB2A(CASS TC5 change to Uppslag/Spread/Panorama)
- **User perform CASS POST API - #1.1** — discountAmount expected 0.0 but found 63660.63; priceGross 250000.00 vs 192192.0; placementId wrong

### rialtoB2A(CASS TC6 change date and size on order line)
- **User perform CASS POST API - #1.1** — priceNet expected 115320.00 but found 111745.08; decimal precision mismatch

### rialtoB2A(CASS TC9 change size from Rialto)
- **User perform CASS POST API - #1.1** — discountAmount expected 0.0 but found 38197.97; priceNetExComm 115320.00 vs 77122.03
- **User perform CASS GET API - #1.1** — depth 184 vs 372; moduleCode 54 vs 58; netAmount 115320.0 vs 128531.37
