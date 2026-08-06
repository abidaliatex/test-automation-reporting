# Build 163 — Root Cause Analysis

**Source Report:** [build-163.md](../../reports/build-failures/automationrunCAI-RIALTOB2A-IntegrationTesting-Internal-trunk/build-163.md)

---

## Build Summary

| Field | Value |
|---|---|
| Build | 163 |
| Total Tests | 514 |
| Passed | 456 |
| Failed | 58 |
| Pass Rate | 88.7% |

---

## Root Cause Groups

---

## 1. Discount Not Applied — Rialto Discount Propagation Failure (Magazine Orders)

**Affected Features:**
- rialtoB2A(CASS TC26 Basic order for magazines)
- rialtoB2A(CASS TC27 Magazine (change date))
- rialtoB2A(CASS TC28 Magazine (change size))
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
- MEDIAHOUSE - Verify updated MediaHouse basket state (TC27)
- RIALTO - Verify Rialto reflects the reverted full-page state (TC27)
- MEDIAHOUSE - Verify updated MediaHouse basket state (TC28)
- RIALTO - Verify Rialto reflects the reverted full-page state (TC28)
- RIALTO - Verify Rialto reflects the reverted full-page state (TC29)
- RIALTO - Verify Rialto reflects the reverted full-page state (TC30)
- MEDIAHOUSE - Verify original full-page order state in MediaHouse (TC31)
- MEDIAHOUSE - Verify updated MediaHouse basket state (TC31)
- RIALTO - Verify Rialto reflects the reverted full-page state (TC31)
- MEDIAHOUSE - Verify updated magazine order state in MediaHouse (TC32)
- MEDIAHOUSE - Verify updated magazine order state in MediaHouse (TC33)
- MEDIAHOUSE - Verify updated magazine order state in MediaHouse (TC34)
- MEDIAHOUSE - Verify original magazine order state in MediaHouse (TC35)
- RIALTO - Verify updated Agency order after Rialto change (TC35)
- MEDIAHOUSE - Verify updated magazine order state in MediaHouse (TC36)
- MEDIAHOUSE - Verify original magazine order state in MediaHouse (TC36)
- MEDIAHOUSE - Verify original order state in MediaHouse (TC37)
- MEDIAHOUSE - Verify updated MediaHouse basket state (TC37)
- RIALTO - Verify Rialto reflects the updated state (TC37)

**Failure Pattern:**
- `orderDiscount` expected `[0.00]` but found `[3600.00]` / `[4000.00]` / `[8800.00]`
- `discountAmount` expected `[0.0]` but found `[3600.0]` / `[4000.0]` / `[8800.0]`
- `discountType` expected `[RIALTO]` but found `[NONE]` (TC27)
- `priceNet` significantly lower than expected (discount being applied when it should not be, or discount not cleared on revert)

**Evidence:**
- TC26: `orderDiscount expected [0.00] but found [3600.00], sumDiscount expected [0.00] but found [3600.00]`
- TC27: `discountType expected [RIALTO] but found [NONE]`, `priceNet expected [5814.0] but found [2325.6]`
- TC28: `priceNet expected [4845.0] but found [969.0]; discountAmount expected [0.0] but found [4000.0]`
- TC32–TC34: orderDiscount values consistently non-zero when expecting zero after a Rialto-side change

**Impact:** ~22 failures

**Confidence:** High

---

## 2. Unexpected discountAmount on Newspaper Orders (TC1, TC3, TC5, TC6 — CASS POST)

**Affected Features:**
- rialtoB2A(CASS TC1 and TC2)
- rialtoB2A(CASS TC3 change Size)
- rialtoB2A(CASS TC5 change to Uppslag/Spread/Panorama)
- rialtoB2A(CASS TC6 change to changes the date and the size on the order line.)
- rialtoB2A(CASS TC4 Change Placement)
- rialtoB2A(CASS TC7 Change Date, Size & Placement)
- rialtoB2A(CASS TC9 change size from Rialto)

**Affected Scenarios:**
- User perform CASS POST API - #1.1 (TC1)
- User perform CASS POST API - #1.1 (TC3)
- User perform CASS GET API - #1.1 (TC4)
- User perform CASS POST API - #1.1 (TC4)
- User perform CASS GET API - #1.1 (TC5)
- User perform CASS POST API - #1.1 (TC5)
- User perform CASS GET API - #1.1 (TC6)
- User perform CASS POST API - #1.1 (TC6)
- User perform CASS POST API - #1.1 (TC7)
- User perform CASS POST API - #1.1 (TC9)
- User perform CASS GET API - #1.1 (TC9)

**Failure Pattern:**
`discountAmount expected [0.0] but found [63660.63]` (repeated across TC1/TC3/TC5/TC6)
`statusFlags expected [[PRELIMINARY]] but found [[]]`
`priceNetExComm` values significantly lower than expected

**Evidence:**
- TC1 POST: `discountAmount expected [0.0] but found [63660.63]; statusFlags expected [PRELIMINARY] but found []`
- TC4 POST: `discountAmount expected [0.0] but found [230000.0]`
- TC5 POST: `discountAmount expected [0.0] but found [63660.63]; priceGross expected [250000.00] but found [192192.0]`
- TC7 POST: `discountAmount expected [0.0] but found [872.0]; priceNetExComm expected [1090.0] but found [218.0]`

**Impact:** ~12 failures

**Confidence:** High

---

## 3. HTTP 500 — Transaction Rollback on Order Update

**Affected Features:**
- rialtoB2A(CASS TC18 2 products change size on not registered as head order line from MH)
- rialtoB2A(CASS TC23 in MH change from Full page to uppslag - two orderlines change)

**Affected Scenarios:**
- User perform CASS POST API - #1.1 (TC18)
- Revert two MediaHouse order lines to full page - #1.1 (TC23)

**Failure Pattern:**
`500: Transaction rolled back because it has been marked as rollback-only`

**Evidence:**
- TC18: `500 errorMessage: "Transaction rolled back because it has been marked as rollback-only"` (caiVersion 8.8.x-CI.47-r5943e353, timestamp 2026-08-06 23:28:06)
- TC23: `500 errorMessage: "Transaction rolled back because it has been marked as rollback-only"` (timestamp 2026-08-06 23:38:34)

**Impact:** 2 failures

**Confidence:** High

---

## 4. Floating-Point Precision Mismatches

**Affected Features:**
- rialtoB2A(CASS TC11 change to UPPSLAG from Rialto)
- rialtoB2A(CASS TC14 change Product, Size, Placement & Date from Rialto)
- rialtoB2A(CASS TC15 2 products change date MH on head order line)
- rialtoB2A(CASS TC21 2 products change from draft to reserved)
- rialtoB2A(CASS TC23 in MH change from Full page to uppslag)
- rialtoB2A(CASS TC24 in MH change from uppslag to Full page)

**Affected Scenarios:**
- User perform CASS POST API - #1.1 (TC11)
- User perform CASS POST API - #1.1 (TC14, x2)
- User perform CASS POST API - #1.1 (TC15)
- User perform CASS POST API - #1.1 (TC21, x2)
- Verify created Rialto order and capture shared identifiers - #1.1 (TC23)
- Verify original full-page order state in MediaHouse - #1.1 (TC23)
- Verify created Rialto order and capture shared identifiers - #1.1 (TC24)
- Verify original full-page order state in MediaHouse - #1.1 (TC24)

**Failure Pattern:**
`priceNet expected [32131.849999999988] but found [32131.85]`
`priceNetExComm expected [64391.59999999998] but found [64391.6]`

**Evidence:**
- TC21: `priceNet expected [[74731.25, 32131.849999999988, 124546.9]] but found [[74731.25, 32131.85, 124546.9]]`
- TC14: `priceNetExComm expected [[20000.0, 38140.399999999994, ...]] but found [[20000.0, 38140.4, ...]]`

**Impact:** ~10 failures

**Confidence:** High — test expectations use raw floating-point arithmetic results; likely a test data or comparison tolerance issue rather than a backend regression.

---

## 5. Order Line Ordering / Sorting Mismatch

**Affected Features:**
- rialtoB2A(CASS TC15 2 products change date MH on head order line)
- rialtoB2A(CASS TC23 in MH change from Full page to uppslag)
- rialtoB2A(CASS TC24 in MH change from uppslag to Full page)

**Affected Scenarios:**
- User perform CASS POST API - #1.1 (TC15)
- Verify updated MediaHouse basket state - #1.1 (TC23)
- Verify reverted MediaHouse basket state - #1.1 (TC23)
- Verify updated MediaHouse basket state - #1.1 (TC24) — `placementId expected [TEXT] but found [UPPSLAG]`
- Verify reverted MediaHouse basket state - #1.1 (TC24)

**Failure Pattern:**
`packageId expected [[AB, SVD]] but found [[SVD, AB]]`
`paCode expected [[SVDTI, SVDTI, AB, AB, AB, SVDTI]] but found [[AB, AB, AB, SVDTI, SVDTI, SVDTI]]`

**Evidence:**
- TC15: `orderAdDetails.packageId expected [[AB, SVD]] but found [[SVD, AB]]`
- TC23: `orders.printDetails.paCode expected [[SVDTI, SVDTI, AB, AB, AB, SVDTI]] but found [[AB, AB, AB, SVDTI, SVDTI, SVDTI]]`
- TC24: `body.orderAdDetailUpdates.placementId expected [[TEXT, TEXT, TEXT, TEXT, TEXT, TEXT]] but found [[UPPSLAG, UPPSLAG, UPPSLAG, UPPSLAG, UPPSLAG, UPPSLAG]]`

**Impact:** ~5 failures

**Confidence:** Medium — may be a non-deterministic sort order in the API response or a test data sequence dependency.

---

## 6. Path Parameter Error (agencyPrisaId / uuid)

**Affected Features:**
- rialtoB2A(CASS TC24 in MH change from uppslag to Full page)

**Affected Scenarios:**
- Verify Rialto reflects the reverted full-page state - #1.1 (TC24)

**Failure Pattern:**
`Path parameters were not correctly defined. Redundant path parameters are: agencyPrisaId=7368. Undefined path parameters are: uuid.`

**Evidence:**
- TC24: `java.lang.IllegalArgumentException: Path parameters were not correctly defined. Redundant path parameters are: agencyPrisaId=7368. Undefined path parameters are: uuid.`

**Impact:** 1 failure

**Confidence:** High — test step is passing `agencyPrisaId` as a path parameter instead of `uuid`; likely a test configuration issue following an API change.

---

## 7. Module Code / Size Mismatch (TC9, TC18)

**Affected Features:**
- rialtoB2A(CASS TC9 change size from Rialto)
- rialtoB2A(CASS TC18 2 products change size on not registered as head order line from MH)

**Affected Scenarios:**
- User perform CASS GET API - #1.1 (TC9)
- User perform CASS POST API - #1.1 (TC18, second step)

**Failure Pattern:**
`moduleCode expected [54] but found [58]`
`depth expected [184] but found [372]`

**Evidence:**
- TC9 GET: `depth expected [[184]] but found [[372]]; moduleCode expected [[54]] but found [[58]]`
- TC18 POST: `moduleCode expected [[58, 54]] but found [[58, 58]]`

**Impact:** 2 failures

**Confidence:** Medium — size/module change not being persisted or reflected correctly after a Rialto-side size change.

---

## Summary Table

| Root Cause | Failures | Confidence |
|---|---|---|
| Discount propagation failure (magazines) | ~22 | High |
| Unexpected discountAmount on newspaper orders | ~12 | High |
| HTTP 500 transaction rollback | 2 | High |
| Floating-point precision mismatches | ~10 | High |
| Order line ordering/sorting | ~5 | Medium |
| Path parameter configuration error | 1 | High |
| Module code / size mismatch | 2 | Medium |
