# Investigation: Build 173 — Root Cause Analysis

**Source Report:** [build-173.md](../../reports/build-failures/automationrunCAI-RIALTOB2A-IntegrationTesting-Internal-trunk/build-173.md)
**Job:** automationrunCAI-RIALTOB2A-IntegrationTesting-Internal-trunk
**Build:** 173 | **Date:** 2026-08-16 | **Status:** UNSTABLE

---

## Build Summary

Build: 173
Total Tests: 514
Passed: 486
Failed: 28
Pass Rate: 94.6%

---

## Root Cause Groups

---

## Root Cause 1 — Array / List Ordering Not Deterministic

**Affected Features:**
- CASS TC15 2 products change date MH on head order line
- CASS TC22 in MH change from Full page to uppslag
- CASS TC23 in MH change from Full page to uppslag – two orderlines change
- CASS TC24 in MH change from uppslag to Full page

**Affected Scenarios:**
- User perform CASS GET API – #1.1 (TC15)
- User perform CASS POST API – #1.1 (TC15)
- User perform CASS GET API – #1.1 (TC22, ×3 occurrences)
- Verify updated MediaHouse basket state – #1.1 (TC23, TC24)
- Verify reverted MediaHouse basket state – #1.1 (TC23, TC24)

**Failure Pattern:**
Fields such as `paCode`, `prodCode`, `packageId`, `productId`, `issueDate`, `netAmount`, `plaCode` contain the correct values but in a different order than expected.
- Expected: `[SVDTI, AB]` → Found: `[AB, SVDTI]`
- Expected: `[SVD, AB]` → Found: `[AB, SVD]`
- Expected: `[2026-12-21, 2026-12-01]` → Found: `[2026-12-01, 2026-12-21]`

**Evidence:**
- TC15 GET: `orders[0].printDetails.paCode expected [[SVDTI, AB]] but found [[AB, SVDTI]]`
- TC15 POST: `orderAdDetails.packageId expected [[AB, SVD]] but found [[SVD, AB]]`
- TC22 GET: `orders[0].printDetails.prodCode expected [[SVD, AB, SVD, AB, AB, SVD]] but found [[AB, SVD, AB, AB, SVD, SVD]]`
- TC24: `orders.printDetails.plaCode expected [[UPPSLAG, UPPSLAG, ...]] but found [[TEXT, UPPSLAG, ...]]`

**Impact:** 11 failures

**Confidence:** High

---

## Root Cause 2 — Missing `PRELIMINARY` Status Flag After Product Change

**Affected Features:**
- CASS TC4 Change Placement
- CASS TC5 change to Uppslag/Spread/Panorama
- CASS TC28 Magazine (change size)
- CASS TC29 Magazine (change to Uppslag/Spread/Panorama)
- CASS TC37 – 2 Products Magazine – changes the size in MH

**Affected Scenarios:**
- User perform CASS POST API – #1.1 (TC4)
- User perform CASS POST API – #1.1 (TC5)
- RIALTO - Verify Rialto reflects the reverted full-page state – #1.1 (TC28)
- RIALTO - Verify Rialto reflects the reverted full-page state – #1.1 (TC29)
- RIALTO - Verify Rialto reflects the updated state – #1.1 (TC37)

**Failure Pattern:**
`orderHeader.statusFlags` expected `[PRELIMINARY]` but found `[]` — the PRELIMINARY flag is absent after product/placement changes.

**Evidence:**
- TC4: `orderHeader.statusFlags expected [[PRELIMINARY]] but found [[]]`
- TC28: `orderHeader.statusFlags expected [[PRELIMINARY]] but found [[]]`
- TC29: `orderHeader.statusFlags expected [[PRELIMINARY]] but found [[]]`
- TC37: `orderHeader.statusFlags expected [[]] but found [[PRELIMINARY]]` (inverted — flag present when not expected)

**Impact:** 5 failures

**Confidence:** High

---

## Root Cause 3 — Incorrect Pricing / Discount Calculation

**Affected Features:**
- CASS TC5 change to Uppslag/Spread/Panorama
- CASS TC6 change date and size
- CASS TC23 – two orderlines change
- CASS TC31 Magazine (change Date, Size & Placement)
- CASS TC36 Magazine (change Product Size Placement & Date from Rialto)
- CASS TC37 – 2 Products Magazine

**Affected Scenarios:**
- User perform CASS POST API – #1.1 (TC5)
- User perform CASS POST API – #1.1 (TC6)
- Verify updated MediaHouse basket state – #1.1 (TC23)
- RIALTO - Verify Rialto reflects the reverted full-page state – #1.1 (TC31)
- MEDIAHOUSE - Verify original magazine order state in MediaHouse – #1.1 (TC36)
- MEDIAHOUSE - Verify updated magazine order state in MediaHouse – #1.1 (TC36)
- MEDIAHOUSE - Verify original order state in MediaHouse – #1.1 (TC37)
- MEDIAHOUSE - Verify updated MediaHouse basket state – #1.1 (TC37)
- RIALTO - Verify Rialto reflects the updated state – #1.1 (TC37)

**Failure Pattern:**
`priceNet`, `priceGross`, `priceNetExComm`, `commissionAmount`, `orderDiscount`, `sumDiscount`, `netPrice`, `totalInclVat`, and `vat` fields return incorrect values, suggesting a pricing/commission calculation regression.
- TC5: `discountAmount expected 0.0 found 63660.63`; `priceGross expected 250000.00 found 192192.0`
- TC23: `orderDiscount expected 0.00 found 323621.09`
- TC36: `orderDiscount expected 3600.00 found 4800.00`; `netPrice expected 2400.00 found 1200.00`
- TC37: `totalInclVat expected 7368.00 found 5814.00`; `vat expected 2913.60 found 1162.80`
- TC31: `priceNet expected 5000.0 found 4845.0`; `commissionAmount expected 0.0 found 155.0`

**Evidence:**
- TC6: `orderAdDetails[0].priceNet expected [115320.00] but found [111745.08]`
- TC36 original: `orderBasketPriceSummary.netPrice expected [2400.00] but found [1200.00]`
- TC37 updated: `commission expected [234.40] but found [229.40]`

**Impact:** 9 failures

**Confidence:** High

---

## Root Cause 4 — HTTP 500 / Transaction Rollback on Revert

**Affected Features:**
- CASS TC24 in MH change from uppslag to Full page

**Affected Scenarios:**
- Revert two MediaHouse order lines to full page – #1.1 (TC24)
- Verify reverted MediaHouse basket state – #1.1 (TC24) *(cascading from above)*
- Verify Rialto reflects the reverted full-page state – #1.1 (TC24) *(cascading — bad path params after revert failed)*

**Failure Pattern:**
The revert API call returns HTTP 500 with `"Transaction rolled back because it has been marked as rollback-only"`. The subsequent steps cascade-fail due to the order not being reverted.

**Evidence:**
- `500 : errorMessage: Transaction rolled back because it has been marked as rollback-only`
- `caiVersion: 8.8.x-CI.63-r1d2e0ed2`
- Next step: `Path parameters were not correctly defined. Redundant path parameters are: agencyPrisaId=7815. Undefined path parameters are: uuid.`

**Impact:** 3 failures (1 root + 2 cascading)

**Confidence:** High

---

## Root Cause 5 — Rialto–MediaHouse Basket ID Mismatch / Wrong Order Applied

**Affected Features:**
- CASS TC35 Magazine (change Date Size & Placement from Rialto)

**Affected Scenarios:**
- RIALTO - Verify updated Agency order after Rialto change – #1.1 (TC35)
- MEDIAHOUSE - Verify updated magazine order state in MediaHouse – #1.1 (TC35)

**Failure Pattern:**
The Rialto change is applied to the wrong basket. MH basket ID `7825` does not match Agency Prisa ID `7826`. The Agency order also reflects wrong placement, date, depth and price — suggesting the update was applied to a different order.

**Evidence:**
- `INTEGRATION MISMATCH: MH basket ID (orBoxid) [7825] does not match Agency Prisa ID [7826]`
- `placementId expected [SIDAN2] but found [HALVLIGG]`
- `issueDate expected [2026-08-05] but found [2026-08-12]`
- `depth expected [297] but found [146]`

**Impact:** 2 failures

**Confidence:** High

---

## Summary

| Root Cause | Failures | Confidence |
|---|---|---|
| Array/list ordering not deterministic | 11 | High |
| Pricing / discount calculation regression | 9 | High |
| Missing / unexpected PRELIMINARY status flag | 5 | High |
| HTTP 500 transaction rollback on revert (TC24) | 3 | High |
| Rialto–MH basket ID mismatch / wrong order applied (TC35) | 2 | High |
| **Total** | **28** | |
