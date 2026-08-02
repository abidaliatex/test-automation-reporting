# Jenkins Build Failure Report

---

## Build Summary

Build: `automationrunCAI-RIALTOB2A-IntegrationTesting-Internal-trunk` #159  
Date: 2026-08-02 21:03 UTC  
Status: `UNSTABLE`  
Total Tests: 514  
Passed: 443  
Failed: 71  
Pass Rate: 86.2%

---

## Root Cause Groups

## Floating-point precision drift in monetary fields

**Affected Features:**
- `rialtoB2A(CASS TC1 and TC2).feature`, `...TC3.feature`, `...TC4.feature`, `...TC5.feature`, `...TC6.feature`, `...TC9.feature`, `...TC11.feature`, `...TC14.feature`, `...TC15.feature`, `...TC21.feature`, `...TC23.feature`, `...TC24.feature`

**Affected Scenarios:**
- User perform CASS POST API - #1.1 (TC1, TC3, TC4, TC5, TC6, TC9, TC11, TC14, TC15, TC21)
- Verify created Rialto order and capture shared identifiers - #1.1 (TC23, TC24)

**Failure Pattern:**
Monetary fields serialised with IEEE-754 residuals instead of rounded decimal values.

**Evidence:**
- `orderAdDetails[0].discountAmount expected [63660.63] but found [63660.630000000005]` (TC1, TC3, TC4, TC5, TC6, TC9, TC11, TC15)
- `orderAdDetails.priceNet expected [[74731.25, 32131.849999999988, 124546.9]] but found [[74731.25, 32131.850000000002, 124546.9]]` (TC21 ×2)
- `orderAdDetails.priceNet expected [[32131.849999999988, 124546.9, ...]] but found [[32131.850000000002, ...]]` (TC23)
- `orderAdDetails.priceNet expected [[64391.59999999998, ...]] but found [[64391.6, ...]]` (TC24)
- `orderAdDetails[0].priceNetExComm expected [66451.59999999998] but found [66451.6]` (TC11)
- `orderAdDetails.priceNetExComm expected [[38140.399999999994, ...]] but found [[38140.4, ...]]` (TC14)

**Impact:** ~15 failures

**Confidence:** High

---

## Discount-type misrouting and basket pricing cascade

**Affected Features:**
- `rialtoB2A(CASS TC1 and TC2).feature`, `...TC3.feature`, `...TC4.feature`, `...TC5.feature`, `...TC9.feature`, `...TC11.feature`, `...TC15.feature`, `...TC27.feature`, `...TC37.feature`

**Affected Scenarios:**
- User perform CASS POST API - #1.1 (TC1, TC5, TC9)
- User perform CASS GET API - #1.1 (TC3, TC4, TC5, TC9, TC11, TC15)
- MEDIAHOUSE - Verify updated MediaHouse basket state - #1.1 (TC27, TC37)
- MEDIAHOUSE - Verify original order state in MediaHouse - #1.1 (TC37)

**Failure Pattern:**
`discountType` returns `RIALTO` when `NONE` or `null` expected, or vice versa; cascading mismatches in commission, VAT, and basket totals.

**Evidence:**
- `orders[0].printDetails.discountType expected [[NONE]] but found [[RIALTO]]` (TC4)
- `orders[0].printDetails.discountType expected [[null]] but found [[RIALTO]]` (TC11)
- `orders[0].printDetails.discountType expected [[null, null]] but found [[RIALTO, RIALTO]]` (TC15, TC37)
- `orders.printDetails.discountType expected [[RIALTO]] but found [[NONE]]` (TC27)
- `discountAmount expected [0.0] but found [63660.63]` (TC1, TC5); `found [38197.97]` (TC9)
- `orderBasketPriceSummary.commission expected [3574.92] but found [3984.47]` (TC3)
- `orderBasketPriceSummary.totalInclVat expected [169660.46] but found [155683.63]` (TC11)

**Impact:** ~14 failures

**Confidence:** High

---

## Missing `PRELIMINARY` status flag on POST responses

**Affected Features:**
- `rialtoB2A(CASS TC3 change Size).feature`, `rialtoB2A(CASS TC4 Change Placement).feature`
- `rialtoB2A(CASS TC6 change to changes the date and the size on the order line.).feature`

**Affected Scenarios:**
- User perform CASS POST API - #1.1 (TC3, TC4, TC6)

**Failure Pattern:**
`orderHeader.statusFlags` returned as empty list where `[PRELIMINARY]` is expected immediately after POST.

**Evidence:**
- `orderHeader.statusFlags expected [[PRELIMINARY]] but found [[]]` (TC3, TC4, TC6)
- `orderHeader.priceNetExComm expected [115320.00] but found [115320....]` co-occurs in same response (TC3, TC6)

**Impact:** 3 failures

**Confidence:** High

---

## Order-line sequencing and stale placement state

**Affected Features:**
- `rialtoB2A(CASS TC15 2 products...).feature`, `...TC18.feature`, `...TC19.feature`, `...TC20.feature`
- `rialtoB2A(CASS TC22...).feature`, `...TC23.feature`, `...TC24.feature`, `...TC35.feature`

**Affected Scenarios:**
- User perform CASS POST API - #1.1 (TC15, TC18, TC19, TC20)
- User perform CASS GET API - #1.1 (TC22)
- Verify original full-page order state in MediaHouse - #1.1 (TC22, TC23, TC24)
- Verify updated MediaHouse basket state - #1.1 (TC22, TC23, TC24)
- Verify reverted MediaHouse basket state - #1.1 (TC23, TC24)
- RIALTO - Verify updated Agency order after Rialto change - #1.1 (TC35)

**Failure Pattern:**
Multi-line response arrays returned in non-deterministic order; update/revert cycles leave stale `moduleCode`, `placementId`, `paCode`, or `netAmount`.

**Evidence:**
- `orderAdDetails.packageId expected [[AB, SVD]] but found [[SVD, AB]]` (TC15, TC19)
- `orderAdDetails.packageId expected [[SVD, AB]] but found [[AB, SVD]]` (TC20)
- `orderAdDetails.moduleCode expected [[58, 54]] but found [[58, 58]]` (TC18)
- `orders.printDetails.paCode expected [[AB, SVDTI, ...]] but found [[SVDTI, AB, ...]]` (TC22, TC23, TC24)
- `orders.printDetails.plaCode expected [[TEXT, TEXT, ...]] but found [[UPPSLAG, TEXT, ...]]` (TC22)
- `orders.printDetails.netAmount expected [[33159.79999999999, ...]] but found [[33159.8, ...]] / found [[158000.0, ...]]` (TC22, TC23, TC24)
- `orderAdDetails.placementId expected [[SIDAN2]] but found [[HALVLIGG]]` (TC35)

**Impact:** ~14 failures

**Confidence:** Medium

---

## Magazine basket discount and commission miscalculations

**Affected Features:**
- `rialtoB2A(CASS TC26...).feature`, `...TC27.feature`, `...TC28.feature`, `...TC30.feature`
- `rialtoB2A(CASS TC31...).feature`, `...TC32.feature`, `...TC33.feature`, `...TC34.feature`
- `rialtoB2A(CASS TC35...).feature`, `...TC36.feature`

**Affected Scenarios:**
- Verify reverted MediaHouse basket state - #1.1 (TC26)
- MEDIAHOUSE - Verify original full-page order state in MediaHouse - #1.1 (TC31)
- MEDIAHOUSE - Verify original magazine order state in MediaHouse - #1.1 (TC35, TC36)
- MEDIAHOUSE - Verify updated MediaHouse basket state - #1.1 (TC28, TC31)
- MEDIAHOUSE - Verify updated magazine order state in MediaHouse - #1.1 (TC32, TC33, TC34, TC35, TC36)
- RIALTO - Verify Rialto reflects the reverted full-page state - #1.1 (TC28, TC30, TC31)

**Failure Pattern:**
Magazine basket discount applied when zero expected, or wrong amount; commission and `priceNet` diverge after size/date/placement changes.

**Evidence:**
- `orderBasketPriceSummary.orderDiscount expected [0.00] but found [3600.00]` (TC26, TC32)
- `orderBasketPriceSummary.orderDiscount expected [0.00] but found [4000.00]` (TC33, TC36)
- `orderBasketPriceSummary.orderDiscount expected [0.00] but found [8800.00]` (TC34)
- `orderBasketPriceSummary.orderDiscount expected [3600.00] but found [4800.00]` (TC31, TC35, TC36)
- `orderBasketPriceSummary.commission expected [155.00] but found [250.00]` (TC28)
- `orderAdDetails.priceNet expected [[4845.0]] but found [[4969.0]]` (TC28, TC31)
- `INTEGRATION MISMATCH: MH basket ID (orBoxid) [7190] does not match Agency Prisa ID [7191]` (TC35)

**Impact:** ~15 failures

**Confidence:** High

---

## Transaction rollback and path-parameter binding failures

**Affected Features:**
- `rialtoB2A(CASS TC18...).feature`, `rialtoB2A(CASS TC24...).feature`

**Affected Scenarios:**
- User perform CASS POST API - #1.1 (TC18)
- Revert two MediaHouse order lines to full page - #1.1 (TC24)
- Verify Rialto reflects the reverted full-page state - #1.1 (TC24)

**Failure Pattern:**
HTTP 500 rollback-only on multi-line update operations; TC24 verification step uses `agencyPrisaId` as path parameter where `uuid` is required.

**Evidence:**
- `500: Transaction rolled back because it has been marked as rollback-only` (TC18, TC24)
- `Redundant path parameters are: agencyPrisaId=7180. Undefined path parameters are: uuid` (TC24)

**Impact:** 3 failures

**Confidence:** High
