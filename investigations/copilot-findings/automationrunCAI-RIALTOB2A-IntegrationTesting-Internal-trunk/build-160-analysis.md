# Build 160 — Root Cause Analysis

**Source Report:** [build-160.md](../../reports/build-failures/automationrunCAI-RIALTOB2A-IntegrationTesting-Internal-trunk/build-160.md)
**Job:** automationrunCAI-RIALTOB2A-IntegrationTesting-Internal-trunk
**Build:** 160 | **Date:** 2026-08-03 21:03:18 UTC | **Status:** UNSTABLE

---

## Build Summary

| Build | Total Tests | Passed | Failed | Pass Rate |
|-------|-------------|--------|--------|-----------|
| 160   | 514         | 450    | 64     | 87.5%     |

---

## Root Cause Groups

---

## RC-1: Floating-Point Precision — discountAmount / priceNet / priceNetExComm

**Affected Features:**
- rialtoB2A(CASS)TestCase1.feature (TC1, TC2)
- TC3, TC4, TC5, TC6, TC9, TC11, TC14, TC15, TC21, TC22, TC23, TC24

**Affected Scenarios:**
- User perform CASS POST API — TC1 & TC2
- User perform CASS POST API — TC3 (change Size)
- User perform CASS POST API — TC4 (Change Placement)
- User perform CASS POST API — TC5 (change to Uppslag/Spread/Panorama)
- User perform CASS POST API — TC6 (change date and size)
- User perform CASS POST API — TC9 (change size from Rialto)
- User perform CASS POST API — TC11 (change to UPPSLAG from Rialto)
- User perform CASS POST API — TC14 (change Product, Size, Placement & Date from Rialto)
- User perform CASS POST API — TC15 (2 products change date MH on head order line)
- User perform CASS POST API — TC21 (2 products change from draft to reserved)
- User perform CASS POST API — TC22 (in MH change from Full page to uppslag)
- Verify created Rialto order and capture shared identifiers — TC23
- Verify created Rialto order and capture shared identifiers — TC24

**Failure Pattern:**
```
discountAmount expected [63660.63] found [63660.630000000005]
priceNet expected [32131.849999999988] found [32131.850000000002]
priceNetExComm expected [66451.59999999998] found [66451.6]
```

**Evidence:**
- TC1: `orderAdDetails[0].discountAmount expected [63660.63] but found [63660.630000000005]`
- TC14: `priceNet expected [[19380.0, 36958.049999999996, 36958.049999999996, 19380.0]] found [[19380.0, 36958.05, 36958.05, 19380.0]]`
- TC22: `priceNet expected [[32131.849999999988, ...]] found [[32131.850000000002, ...]]`

**Impact:** ~20 failures across 13 test cases

**Confidence:** High

---

## RC-2: Incorrect discountType — RIALTO vs. NONE/null

**Affected Features:**
- TC4, TC5, TC9, TC11, TC15, TC27, TC37

**Affected Scenarios:**
- User perform CASS GET API — TC4 (Change Placement): `discountType expected [[NONE]] found [[RIALTO]]`
- User perform CASS GET API — TC9 (change size from Rialto): `discountType expected [[NONE]] found [[RIALTO]]`
- User perform CASS GET API — TC11 (change to UPPSLAG from Rialto): `discountType expected [[null]] found [[RIALTO]]`
- User perform CASS GET API — TC15 (2 products): `discountType expected [[null, null]] found [[RIALTO, RIALTO]]`
- MEDIAHOUSE - Verify updated MediaHouse basket state — TC27 (Magazine change date): `discountType expected [[RIALTO]] found [[NONE]]`
- MEDIAHOUSE - Verify original order state in MediaHouse — TC37: `discountType expected [[null, null]] found [[RIALTO, RIALTO]]`

**Failure Pattern:**
```
orders[0].printDetails.discountType expected [[NONE/null]] but found [[RIALTO]]
```

**Evidence:**
- TC4: `discountType expected [[NONE]] but found [[RIALTO]]`; commission `expected [7750.00] found [12500.00]`
- TC9: `discountType expected [[NONE]] found [[RIALTO]]`; `netAmount expected [[115320.0]] found [[77122.03]]`
- TC11: `discountType expected [[null]] found [[RIALTO]]`; `totalInclVat expected [136225.78] found [80489.50]`
- TC27: inverse — discount type expected RIALTO but found NONE

**Impact:** ~10 failures across 6 test cases

**Confidence:** High

---

## RC-3: Magazine Discount Calculation — Incorrect orderDiscount / commission Amounts

**Affected Features:**
- TC26, TC28, TC30, TC31, TC32, TC33, TC34, TC35, TC36

**Affected Scenarios:**
- Verify reverted MediaHouse basket state — TC26 (Basic order for magazines)
- MEDIAHOUSE - Verify updated MediaHouse basket state — TC28 (change size)
- RIALTO - Verify Rialto reflects the reverted full-page state — TC28
- RIALTO - Verify Rialto reflects the reverted full-page state — TC30 (change Date & Size)
- MEDIAHOUSE - Verify original full-page order state in MediaHouse — TC31
- MEDIAHOUSE - Verify updated MediaHouse basket state — TC31
- RIALTO - Verify Rialto reflects the reverted full-page state — TC31
- MEDIAHOUSE - Verify updated magazine order state in MediaHouse — TC32 (change date from Rialto)
- MEDIAHOUSE - Verify updated magazine order state in MediaHouse — TC33 (change size from Rialto)
- MEDIAHOUSE - Verify updated magazine order state in MediaHouse — TC34 (change to UPPSLAG from Rialto)
- MEDIAHOUSE - Verify original magazine order state in MediaHouse — TC35
- MEDIAHOUSE - Verify original magazine order state in MediaHouse — TC36
- MEDIAHOUSE - Verify updated magazine order state in MediaHouse — TC36

**Failure Pattern:**
```
orderDiscount expected [0.00] found [3600.00/4000.00/4800.00/8800.00]
commission expected [155.00/465.00] found [250.00]
priceNet expected [[4845.0/5000.0/6000.0]] found [[4969.0/4969.0/5962.8]]
```

**Evidence:**
- TC26: `orderDiscount expected [0.00] found [3600.00]`; `netPrice expected [6000.00] found [2400.00]`
- TC28: `commission expected [155.00] found [250.00]`; Rialto `priceNet expected [[4845.0]] found [[4969.0]]`
- TC31: `orderDiscount expected [3600.00] found [4800.00]`; `commission expected [465.00] found [250.00]`
- TC34: `orderDiscount expected [0.00] found [8800.00]`; `netPrice expected [11000.00] found [2200.00]`

**Impact:** ~18 failures across 9 magazine test cases

**Confidence:** High

---

## RC-4: Array Element Ordering — packageId / paCode / placementId / productId

**Affected Features:**
- TC15, TC22, TC23, TC24, TC35, TC37

**Affected Scenarios:**
- User perform CASS POST API — TC15 (2 products change date MH): `packageId expected [[AB, SVD]] found [[SVD, AB]]`
- User perform CASS POST API — TC22 (Full page to uppslag): `packageId expected [[SVDTI, SVDTI, SVDTI, AB, AB, AB]] found [[SVDTI, AB, SVDTI, AB, AB, SVDTI]]`
- Verify updated MediaHouse basket state — TC23: `paCode expected [[SVDTI, SVDTI, AB, AB, AB, SVDTI]] found [[AB, AB, AB, SVDTI, SVDTI, SVDTI]]`
- Verify reverted MediaHouse basket state — TC23: `paCode` ordering mismatch
- Revert two MediaHouse order lines to full page — TC24: `placementId expected [[TEXT, TEXT...]] found [[UPPSLAG, UPPSLAG...]]`
- Verify reverted MediaHouse basket state — TC24: `paCode`, `plaCode` ordering mismatch
- RIALTO - Verify updated Agency order after Rialto change — TC35: `placementId expected [[SIDAN2]] found [[HALVLIGG]]`; issueDate, depth, width dimension mismatch
- MEDIAHOUSE - Verify updated MediaHouse basket state — TC37: `paCode expected [[ANA, KOT]] found [[KOT, ANA]]`

**Failure Pattern:**
```
orderAdDetailUpdates.packageId expected [[AB, SVD]] found [[SVD, AB]]
orders.printDetails.paCode expected [[SVDTI, AB,...]] found [[AB, AB,...]]
```

**Evidence:**
- TC15: `packageId expected [[AB, SVD]] found [[SVD, AB]]`, `issueDate` ordering also swapped
- TC22: placement/package ordering wrong across 6 order lines
- TC23/24: paCode and plaCode arrays returned in different sequence after basket operations

**Impact:** ~8 failures across 6 test cases

**Confidence:** High

---

## RC-5: statusFlags Missing PRELIMINARY Flag

**Affected Features:**
- TC1, TC3, TC6

**Affected Scenarios:**
- User perform CASS POST API — TC1 & TC2: `orderHeader.statusFlags expected [[PRELIMINARY]] found [[]]`
- User perform CASS POST API — TC3 (change Size): `orderHeader.statusFlags expected [[PRELIMINARY]] found [[]]`
- User perform CASS POST API — TC6 (change date and size): `orderHeader.statusFlags expected [[PRELIMINARY]] found [[]]`

**Failure Pattern:**
```
orderHeader.statusFlags expected [[PRELIMINARY]] but found [[]]
```

**Evidence:**
- TC1: `statusFlags expected [[PRELIMINARY]] found [[]]`
- TC3: `statusFlags expected [[PRELIMINARY]] found [[]]`, also `priceNetExComm expected [115320.00] found [115320.0]`
- TC6: Same pattern

**Impact:** 3 failures across 3 test cases

**Confidence:** High

---

## RC-6: HTTP 500 / Transaction Rollback

**Affected Features:**
- TC18

**Affected Scenarios:**
- User perform CASS POST API — TC18 (2 products change size on not registered as head order line from MH): HTTP 500 Transaction rolled back

**Failure Pattern:**
```
500: Transaction rolled back because it has been marked as rollback-only
```

**Evidence:**
- TC18: `errorMessage: "Transaction rolled back because it has been marked as rollback-only"`, caiVersion: `8.8.x-CI.41-rec8094db`, timestamp: `2026-08-03 23:28:10`

**Impact:** 1 failure (TC18), cascades to subsequent step (moduleCode mismatch)

**Confidence:** High

---

## RC-7: Integration Mismatch — Basket ID / Path Parameter Error

**Affected Features:**
- TC24, TC35

**Affected Scenarios:**
- Verify Rialto reflects the reverted full-page state — TC24: `Redundant path parameters: agencyPrisaId=7225. Undefined path parameters: uuid`
- MEDIAHOUSE - Verify updated magazine order state in MediaHouse — TC35: `INTEGRATION MISMATCH: MH basket ID [7235] does not match Agency Prisa ID [7236]`

**Failure Pattern:**
```
INTEGRATION MISMATCH: MH basket ID does not match Agency Prisa ID
Redundant path parameters: agencyPrisaId. Undefined path parameters: uuid
```

**Evidence:**
- TC24: API call built with wrong path parameter (`agencyPrisaId` used instead of `uuid`)
- TC35: Basket ID sync failure between MediaHouse and Agency Prisa during magazine order update

**Impact:** 2 failures across 2 test cases

**Confidence:** Medium

---

## Summary

| # | Root Cause | Failures | Confidence |
|---|-----------|----------|-----------|
| RC-1 | Floating-point precision (discountAmount / priceNet) | ~20 | High |
| RC-2 | Incorrect discountType (RIALTO vs. NONE/null) | ~10 | High |
| RC-3 | Magazine discount/commission calculation errors | ~18 | High |
| RC-4 | Array element ordering (packageId/paCode/placementId) | ~8 | High |
| RC-5 | Missing PRELIMINARY statusFlag | 3 | High |
| RC-6 | HTTP 500 transaction rollback (TC18) | 1–2 | High |
| RC-7 | Integration mismatch / path parameter error | 2 | Medium |
