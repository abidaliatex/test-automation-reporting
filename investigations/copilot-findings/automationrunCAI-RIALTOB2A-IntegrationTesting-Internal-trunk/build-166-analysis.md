# Investigation Analysis — Build 166

**Source Report:** [build-166.md](../../reports/build-failures/automationrunCAI-RIALTOB2A-IntegrationTesting-Internal-trunk/build-166.md)
**Job:** automationrunCAI-RIALTOB2A-IntegrationTesting-Internal-trunk
**Date:** 2026-08-09 21:03:11 UTC

---

## Build Summary

**Build:** 166
**Total Tests:** 514
**Passed:** 457
**Failed:** 57
**Pass Rate:** 88.9%

---

## Root Cause Groups

---

## RC1 — Unexpected Discount / Commission Applied to Magazine Orders

**Affected Features:**
- rialtoB2A(CASS TC26 Basic order for magazines)
- rialtoB2A(CASS TC27 Magazine (change date))
- rialtoB2A(CASS TC29 Magazine (change to Uppslag/Spread/Panorama))
- rialtoB2A(CASS TC30 Magazine (change Date & Size))
- rialtoB2A(CASS TC31 Magazine (change Date, Size & Placement))
- rialtoB2A(CASS TC32 Magazine (change date from Rialto))
- rialtoB2A(CASS TC33 Magazine (change size from Rialto))
- rialtoB2A(CASS TC34 Magazine (change to UPPSLAG from Rialto))
- rialtoB2A(CASS TC35 Magazine (change Date Size & Placement from Rialto))
- rialtoB2A(CASS TC36 Magazine (change Product Size Placement & Date from Rialto))
- rialtoB2A(CASS TC37 - 2 Products Magazine - changes the size in MH)

**Affected Scenarios:**
- Verify reverted MediaHouse basket state (TC26)
- MEDIAHOUSE - Verify updated MediaHouse basket state (TC27, TC29, TC31, TC37)
- RIALTO - Verify Rialto reflects the reverted full-page state (TC29, TC30, TC31)
- RIALTO - Verify Rialto reflects the updated state (TC37)
- MEDIAHOUSE - Verify updated magazine order state in MediaHouse (TC32, TC33, TC34, TC35, TC36)
- MEDIAHOUSE - Verify original full-page order state in MediaHouse (TC31, TC35, TC36)
- MEDIAHOUSE - Verify original order state in MediaHouse (TC37)
- RIALTO - Verify updated Agency order after Rialto change (TC35)

**Failure Pattern:**
- `orderDiscount expected [0.00] but found [3600.00/4000.00/8800.00]`
- `sumDiscount` non-zero when zero expected
- `commission expected [550.00] but found [341.00]`; `priceNet expected [[6000.0]] but found [[5814.0]]`
- `discountType expected [[RIALTO]] but found [[NONE]]` (TC27)

**Evidence:**
- TC26/TC32: `orderDiscount expected [0.00] but found [3600.00]`
- TC31/TC35/TC36: `orderDiscount expected [3600.00] but found [4800.00]`
- TC34: `orderDiscount expected [0.00] but found [8800.00]`
- TC27: `discountType expected [[RIALTO]] but found [[NONE]]` — discount type not propagated from Rialto to MH

**Impact:** 20 failures

**Confidence:** High

---

## RC2 — Pricing/VAT Calculation Errors on Newspaper Orders (Discount Applied Unexpectedly)

**Affected Features:**
- rialtoB2A(CASS TC1 and TC2)
- rialtoB2A(CASS TC5 change to Uppslag/Spread/Panorama)
- rialtoB2A(CASS TC9 change size from Rialto)
- rialtoB2A(CASS TC11 change to UPPSLAG from Rialto)
- rialtoB2A(CASS TC15 2 products change date MH on head order line)
- rialtoB2A(CASS TC23 in MH change from Full page to uppslag - two orderlines change)

**Affected Scenarios:**
- User perform CASS POST API - #1.1 (TC1, TC5, TC9)
- User perform CASS GET API - #1.1 (TC1, TC9, TC11, TC15)
- Verify original full-page order state in MediaHouse - #1.1 (TC23)
- Verify updated MediaHouse basket state - #1.1 (TC23)
- Verify reverted MediaHouse basket state - #1.1 (TC23)

**Failure Pattern:**
- `discountAmount expected [0.0] but found [63660.63/38197.97]`
- `orderHeader.priceNetExComm expected [192192.0] but found [128531.37]`
- `totalInclVat` / VAT totals off
- `printDetails.netAmount` incorrect after revert (TC23: `expected [[33159.8,...]] but found [[158000.0,...]]`)

**Evidence:**
- TC5: `discountAmount expected [0.0] but found [63660.63]`; `priceGross expected [250000.00] but found [192192.0]`
- TC9: `discountAmount expected [0.0] but found [38197.97]`
- TC11: `totalInclVat expected [169660.46] but found [155683.63]`
- TC23 revert: price reverts to wrong base value (158000.0 instead of 33159.8)

**Impact:** 10 failures

**Confidence:** High

---

## RC3 — Transaction Rollback (500 Error) on Size/Format Change

**Affected Features:**
- rialtoB2A(CASS TC18 2 products change size on not registered as head order line from MH)
- rialtoB2A(CASS TC22 in MH change from Full page to uppslag)
- rialtoB2A(CASS TC24 in MH change in MH change from uppslag to Full page)

**Affected Scenarios:**
- User perform CASS POST API - #1.1 (TC18, TC22)
- Revert two MediaHouse order lines to full page - #1.1 (TC24)

**Failure Pattern:**
`500: Transaction rolled back because it has been marked as rollback-only`

**Evidence:**
- TC18: POST fails with transaction rollback when changing size on non-head order line
- TC22: POST fails with rollback when changing from Full page to Uppslag
- TC24: Revert operation fails with rollback

**Impact:** 3 failures

**Confidence:** High

---

## RC4 — Array Ordering Inconsistency (packageId / productId / paCode / plaCode)

**Affected Features:**
- rialtoB2A(CASS TC15 2 products change date MH on head order line)
- rialtoB2A(CASS TC19 2 products change placement on head order from MH)
- rialtoB2A(CASS TC20 2 products change placement order for non head from MH)
- rialtoB2A(CASS TC22 in MH change from Full page to uppslag)
- rialtoB2A(CASS TC24 in MH change in MH change from uppslag to Full page)

**Affected Scenarios:**
- User perform CASS POST API - #1.1 (TC15, TC19, TC20)
- User perform CASS GET API - #1.1 (TC22, TC24)
- Verify updated MediaHouse basket state - #1.1 (TC24)
- Verify reverted MediaHouse basket state - #1.1 (TC24)

**Failure Pattern:**
`orderAdDetails.packageId expected [[AB, SVD]] but found [[SVD, AB]]`
`orders.printDetails.paCode expected [[AB, SVDTI, ...]] but found [[SVDTI, AB, ...]]`

**Evidence:**
- TC15/TC19: `packageId expected [[AB, SVD]] but found [[SVD, AB]]`
- TC20: `packageId expected [[SVD, AB]] but found [[AB, SVD]]`
- TC22/TC24: `paCode` and `plaCode` array element order differs from expected

**Impact:** 8 failures

**Confidence:** High

---

## RC5 — Floating-Point Precision Mismatch

**Affected Features:**
- rialtoB2A(CASS TC3 change Size)
- rialtoB2A(CASS TC6 change to changes the date and the size on the order line.)
- rialtoB2A(CASS TC11 change to UPPSLAG from Rialto)
- rialtoB2A(CASS TC14 change Product, Size, Placement & Date from Rialto)
- rialtoB2A(CASS TC21 2 products change from draft to reserved)
- rialtoB2A(CASS TC23 in MH change from Full page to uppslag - two orderlines change)
- rialtoB2A(CASS TC24 in MH change in MH change from uppslag to Full page)

**Affected Scenarios:**
- User perform CASS POST API - #1.1 (TC3, TC6, TC11, TC14, TC21)
- Verify original full-page order state in MediaHouse - #1.1 (TC23)
- Verify created Rialto order and capture shared identifiers - #1.1 (TC24)

**Failure Pattern:**
`priceNetExComm expected [115320.00] but found [115320.0]`
`priceNet expected [[66451.59999999998]] but found [[66451.6]]`

**Evidence:**
- TC3/TC6: `priceNetExComm expected [115320.00] but found [115320.0]` — trailing zero format difference
- TC11: `priceNetExComm expected [66451.59999999998] but found [66451.6]` — rounding
- TC14: `priceNetExComm expected [[20000.0, 38140.399999999994,...]] but found [[20000.0, 38140.4,...]]`

**Impact:** 9 failures

**Confidence:** High

---

## RC6 — Path Parameter / API Configuration Errors

**Affected Features:**
- rialtoB2A(CASS TC1 and TC2)
- rialtoB2A(CASS TC24 in MH change in MH change from uppslag to Full page)

**Affected Scenarios:**
- User perform CASS GET API - #1.1 (TC1 ×2)
- Verify Rialto reflects the reverted full-page state - #1.1 (TC24)

**Failure Pattern:**
- `Invalid number of path parameters. Expected 1, was 0. Undefined path parameters are: mhBasketOrderId.`
- `Redundant path parameters are: agencyPrisaId=7481. Undefined path parameters are: uuid.`

**Evidence:**
- TC1: GET call missing `mhBasketOrderId` path parameter — possibly basket ID not captured from prior POST failure
- TC24: API call uses `agencyPrisaId` but endpoint expects `uuid` — possibly wrong ID captured due to upstream TC24 500 error

**Impact:** 3 failures (cascade from RC3)

**Confidence:** Medium

---

## RC7 — Module Code / Size Mismatch After Change

**Affected Features:**
- rialtoB2A(CASS TC9 change size from Rialto)
- rialtoB2A(CASS TC18 2 products change size on not registered as head order line from MH)

**Affected Scenarios:**
- User perform CASS GET API - #1.1 (TC9)
- User perform CASS POST API - #1.1 (TC18)

**Failure Pattern:**
`moduleCode expected [[54]] but found [[58]]`
`depth expected [[184]] but found [[372]]`

**Evidence:**
- TC9: After size change from Rialto, `depth` remains at 372 (original) instead of reverting to 184; `moduleCode` stays at 58 instead of 54
- TC18: `moduleCode expected [[58, 54]] but found [[58, 58]]` — second order line not updated

**Impact:** 2 failures

**Confidence:** High

---

## RC8 — Status Flags / Integration ID Mismatch

**Affected Features:**
- rialtoB2A(CASS TC4 Change Placement)
- rialtoB2A(CASS TC27 Magazine (change date))
- rialtoB2A(CASS TC35 Magazine (change Date Size & Placement from Rialto))

**Affected Scenarios:**
- User perform CASS POST API - #1.1 (TC4)
- RIALTO - Verify Rialto reflects the reverted full-page state - #1.1 (TC27)
- MEDIAHOUSE - Verify updated magazine order state in MediaHouse - #1.1 (TC35)
- RIALTO - Verify updated Agency order after Rialto change - #1.1 (TC35)

**Failure Pattern:**
- `statusFlags expected [[PRELIMINARY]] but found [[]]` / `expected [[]] but found [[PRELIMINARY]]`
- `INTEGRATION MISMATCH: MH basket ID (orBoxid) [7493] does not match Agency Prisa ID [7494]`
- `placementId expected [[SIDAN2]] but found [[HALVLIGG]]`

**Evidence:**
- TC4/TC27: `PRELIMINARY` flag present/absent unexpectedly — order state not transitioning as expected
- TC35: MH basket orBoxid and Agency Prisa ID off by 1 — ID synchronisation issue between systems

**Impact:** 4 failures

**Confidence:** Medium

---

## Summary

| Root Cause | Impact | Confidence |
|---|---|---|
| RC1 — Unexpected discount/commission on magazines | 20 | High |
| RC2 — Pricing/VAT errors (unexpected discount on newspaper) | 10 | High |
| RC3 — 500 Transaction rollback on format/size change | 3 | High |
| RC4 — Array ordering inconsistency | 8 | High |
| RC5 — Floating-point precision mismatch | 9 | High |
| RC6 — Path parameter / API config errors (cascade) | 3 | Medium |
| RC7 — Module code / size not updated after change | 2 | High |
| RC8 — Status flags / integration ID mismatch | 4 | Medium |
