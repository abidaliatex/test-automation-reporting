# Build 164 — Root Cause Analysis

**Source Report:** [build-164.md](../../reports/build-failures/automationrunCAI-RIALTOB2A-IntegrationTesting-Internal-trunk/build-164.md)

---

## Build Summary

| Field | Value |
|---|---|
| Build | 164 |
| Total Tests | 514 |
| Passed | 456 |
| Failed | 58 |
| Pass Rate | 88.7% |

---

## Root Cause Groups

---

## 1. Discount Not Applied / Incorrectly Applied — Magazine Order Propagation Failure

**Affected Features:**
- rialtoB2A(CASS TC26 Basic order for magazines)
- rialtoB2A(CASS TC27 Magazine (change date))
- rialtoB2A(CASS TC29 Magazine (change to Uppslag/Spread/Panorama))
- rialtoB2A(CASS TC30 Magazine (change Date & Size))
- rialtoB2A(CASS TC31 Magazine (change Date, Size & Placement))
- rialtoB2A(CASS TC33 Magazine (change size from Rialto))
- rialtoB2A(CASS TC34 Magazine (change to UPPSLAG from Rialto))
- rialtoB2A(CASS TC36 Magazine (change Product Size Placement & Date from Rialto))
- rialtoB2A(CASS TC37 - 2 Products Magazine - changes the size in MH)

**Affected Scenarios:**
- Verify reverted MediaHouse basket state (TC26)
- MEDIAHOUSE - Verify updated MediaHouse basket state (TC27)
- RIALTO - Verify Rialto reflects the reverted full-page state (TC29)
- RIALTO - Verify Rialto reflects the reverted full-page state (TC30)
- MEDIAHOUSE - Verify original full-page order state in MediaHouse (TC31)
- MEDIAHOUSE - Verify updated MediaHouse basket state (TC31)
- RIALTO - Verify Rialto reflects the reverted full-page state (TC31)
- MEDIAHOUSE - Verify updated magazine order state in MediaHouse (TC33)
- MEDIAHOUSE - Verify updated magazine order state in MediaHouse (TC34)
- MEDIAHOUSE - Verify original magazine order state in MediaHouse (TC36)
- MEDIAHOUSE - Verify updated magazine order state in MediaHouse (TC36)
- MEDIAHOUSE - Verify original order state in MediaHouse (TC37)
- MEDIAHOUSE - Verify updated MediaHouse basket state (TC37)
- RIALTO - Verify Rialto reflects the updated state (TC37)

**Failure Pattern:**
`orderDiscount` expected `[0.00]` but found `[3600.00]` / `[4000.00]` / `[8800.00]`
`discountType` expected `[[RIALTO]]` but found `[[NONE]]` (TC27)
`priceNet` lower than expected due to discount not being cleared on revert

**Evidence:**
- TC26: `orderDiscount expected [0.00] but found [3600.00], sumDiscount expected [0.00] but found [3600.00]`
- TC27: `discountType expected [[RIALTO]] but found [[NONE]]`
- TC33: `orderDiscount expected [0.00] but found [4000.00]`
- TC34: `orderDiscount expected [0.00] but found [8800.00]`
- TC37: `priceNet expected [[4969.0, 2325.6]] but found [[4845.0, 5814.0]]`

**Impact:** ~16 failures

**Confidence:** High

---

## 2. Unexpected discountAmount on Newspaper Orders (CASS POST/GET)

**Affected Features:**
- rialtoB2A(CASS TC1 and TC2)
- rialtoB2A(CASS TC5 change to Uppslag/Spread/Panorama)
- rialtoB2A(CASS TC7 Change Date, Size & Placement)
- rialtoB2A(CASS TC9 change size from Rialto)

**Affected Scenarios:**
- User perform CASS POST API - #1.1 (TC1)
- User perform CASS POST API - #1.1 (TC5)
- User perform CASS POST API - #1.1 (TC7)
- User perform CASS POST API - #1.1 (TC9)
- User perform CASS GET API - #1.1 (TC9)

**Failure Pattern:**
`discountAmount expected [0.0] but found [63660.63]`
`priceNetExComm` and `priceGross` significantly lower than expected (discount being applied when none expected)

**Evidence:**
- TC1 POST: `discountAmount expected [0.0] but found [63660.63]; orderHeader.priceNetExComm expected [192192.0] but found [128531.37]`
- TC5 POST: `discountAmount expected [0.0] but found [63660.63]; priceGross expected [250000.00] but found [192192.0]`
- TC7 POST: `discountAmount expected [0.0] but found [63660.63]; priceGross expected [1090.0] but found [192192.0]`
- TC9 POST: `discountAmount expected [0.0] but found [38197.97]; priceNetExComm expected [115320.00] but found [77122.03]`

**Impact:** ~5 failures

**Confidence:** High

---

## 3. Floating-Point Precision Mismatches

**Affected Features:**
- rialtoB2A(CASS TC3 change Size)
- rialtoB2A(CASS TC6 change date and size)
- rialtoB2A(CASS TC11 change to UPPSLAG from Rialto)
- rialtoB2A(CASS TC14 change Product, Size, Placement & Date from Rialto)
- rialtoB2A(CASS TC15 2 products change date MH on head order line)
- rialtoB2A(CASS TC21 2 products change from draft to reserved)
- rialtoB2A(CASS TC23 in MH change from Full page to uppslag)
- rialtoB2A(CASS TC24 in MH change from uppslag to Full page)

**Affected Scenarios:**
- User perform CASS POST API - #1.1 (TC3)
- User perform CASS POST API - #1.1 (TC6)
- User perform CASS POST API - #1.1 (TC11)
- User perform CASS POST API - #1.1 (TC14, x2)
- User perform CASS POST API - #1.1 (TC15)
- User perform CASS POST API - #1.1 (TC21, x2)
- Verify original full-page order state in MediaHouse - #1.1 (TC23)
- Verify updated MediaHouse basket state - #1.1 (TC23)
- Verify created Rialto order and capture shared identifiers - #1.1 (TC24)
- Verify original full-page order state in MediaHouse - #1.1 (TC24)
- Verify updated MediaHouse basket state - #1.1 (TC24)

**Failure Pattern:**
`priceNetExComm expected [115320.00] but found [115320.0]`
`priceNet expected [32131.849999999988] but found [32131.85]`

**Evidence:**
- TC3: `orderHeader.priceNetExComm expected [115320.00] but found [115320.0]`
- TC14: `priceNetExComm expected [[20000.0, 38140.399999999994, ...]] but found [[20000.0, 38140.4, ...]]`
- TC21: `priceNet expected [[74731.25, 32131.849999999988, ...]] but found [[74731.25, 32131.85, ...]]`

**Impact:** ~13 failures

**Confidence:** High — test assertions compare raw floating-point arithmetic results with rounded API outputs; likely a test tolerance/comparison issue.

---

## 4. MH Basket ID / Agency Prisa ID Integration Mismatch

**Affected Features:**
- rialtoB2A(CASS TC32 Magazine (change date from Rialto))
- rialtoB2A(CASS TC35 Magazine (change Date Size & Placement from Rialto))

**Affected Scenarios:**
- MEDIAHOUSE - Verify updated magazine order state in MediaHouse (TC32)
- MEDIAHOUSE - Verify original magazine order state in MediaHouse (TC35)
- MEDIAHOUSE - Verify updated magazine order state in MediaHouse (TC35)

**Failure Pattern:**
`INTEGRATION MISMATCH: MH basket ID (orBoxid) [X] does not match Agency Prisa ID [Y]`

**Evidence:**
- TC32: `MH basket ID (orBoxid) [4745] does not match Agency Prisa ID [7415]`
- TC35: `MH basket ID (orBoxid) [5231] does not match Agency Prisa ID [7418]` (two steps)

**Impact:** 3 failures

**Confidence:** High — the basket identifier returned by MH does not correspond to the Rialto-side agency order ID; possibly a synchronisation or mapping failure between systems.

---

## 5. Order Line Ordering / Placement Mismatch

**Affected Features:**
- rialtoB2A(CASS TC15 2 products change date MH on head order line)
- rialtoB2A(CASS TC23 in MH change from Full page to uppslag)
- rialtoB2A(CASS TC24 in MH change from uppslag to Full page)
- rialtoB2A(CASS TC35 Magazine (change Date Size & Placement from Rialto))

**Affected Scenarios:**
- User perform CASS POST API - #1.1 (TC15)
- Verify reverted MediaHouse basket state - #1.1 (TC23)
- Revert two MediaHouse order lines to full page - #1.1 (TC24)
- Verify reverted MediaHouse basket state - #1.1 (TC24)
- RIALTO - Verify updated Agency order after Rialto change (TC35)

**Failure Pattern:**
`packageId expected [[AB, SVD]] but found [[SVD, AB]]`
`placementId expected [[TEXT,...]] but found [[UPPSLAG,...]]`
`placementId expected [[SIDAN2]] but found [[HALVLIGG]]`

**Evidence:**
- TC15: `orderAdDetails.packageId expected [[AB, SVD]] but found [[SVD, AB]]`
- TC24: `body.orderAdDetailUpdates.placementId expected [[TEXT,...]] but found [[UPPSLAG,...]]`
- TC35: `orderAdDetails.placementId expected [[SIDAN2]] but found [[HALVLIGG]]`

**Impact:** ~6 failures

**Confidence:** Medium — non-deterministic sort order in API response or test data sequence dependency.

---

## 6. statusFlags Unexpected PRELIMINARY State

**Affected Features:**
- rialtoB2A(CASS TC4 Change Placement)
- rialtoB2A(CASS TC27 Magazine (change date))

**Affected Scenarios:**
- User perform CASS POST API - #1.1 (TC4)
- RIALTO - Verify Rialto reflects the reverted full-page state (TC27)

**Failure Pattern:**
`orderHeader.statusFlags expected [[PRELIMINARY]] but found [[]]` (TC4)
`orderHeader.statusFlags expected [[]] but found [[PRELIMINARY]]` (TC27)

**Evidence:**
- TC4: `statusFlags expected [[PRELIMINARY]] but found [[]]`
- TC27: `statusFlags expected [[]] but found [[PRELIMINARY]]`

**Impact:** 2 failures

**Confidence:** Medium — order status not transitioning as expected; may be timing or workflow state machine issue.

---

## 7. Path Parameter Configuration Error

**Affected Features:**
- rialtoB2A(CASS TC1 and TC2)
- rialtoB2A(CASS TC24 in MH change from uppslag to Full page)

**Affected Scenarios:**
- User perform CASS GET API - #1.1 (TC1, x2)
- Verify Rialto reflects the reverted full-page state - #1.1 (TC24)

**Failure Pattern:**
`Invalid number of path parameters. Undefined path parameters are: mhBasketOrderId` (TC1)
`Redundant path parameters are: agencyPrisaId. Undefined path parameters are: uuid` (TC24)

**Evidence:**
- TC1: `Invalid number of path parameters. Expected 1, was 0. Undefined path parameters are: mhBasketOrderId`
- TC24: `Path parameters were not correctly defined. Redundant path parameters are: agencyPrisaId=7407. Undefined path parameters are: uuid`

**Impact:** 3 failures

**Confidence:** High — test steps passing incorrect or missing path parameters; likely a test configuration issue following an API change.

---

## Summary Table

| Root Cause | Failures | Confidence |
|---|---|---|
| Discount propagation failure (magazines) | ~16 | High |
| Unexpected discountAmount on newspaper orders | ~5 | High |
| Floating-point precision mismatches | ~13 | High |
| MH Basket ID / Agency Prisa ID mismatch | 3 | High |
| Order line ordering / placement mismatch | ~6 | Medium |
| statusFlags unexpected state | 2 | Medium |
| Path parameter configuration error | 3 | High |
