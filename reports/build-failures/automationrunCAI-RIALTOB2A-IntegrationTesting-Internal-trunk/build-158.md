# Jenkins Build Failure Report

---

## Build Summary

Build: `automationrunCAI-RIALTOB2A-IntegrationTesting-Internal-trunk` #158  
Date: 2026-08-01 21:03 UTC  
Status: `UNSTABLE`  
Total Tests: 514  
Passed: 447  
Failed: 67  
Pass Rate: 87.0%

---

## Root Cause Groups

## Floating-point precision drift in monetary fields

**Affected Features:**
- `rialtoB2A(CASS)TestCase1.feature`, `...3.feature`, `...4.feature`, `...5.feature`, `...6.feature`, `...7.feature`, `...9.feature`, `...11.feature`, `...14.feature`, `...15.feature`, `...21.feature`, `...22.feature`, `...23.feature`, `...24.feature`

**Affected Scenarios:**
- User perform CASS POST API - #1.1 (TC1, TC3, TC4, TC5, TC6, TC7, TC9, TC11, TC14, TC15, TC21, TC22)
- User perform CASS GET API - #1.1 (TC22)
- Verify created Rialto order and capture shared identifiers - #1.1 (TC23, TC24)
- Verify original full-page order state in MediaHouse - #1.1 (TC23, TC24)
- Verify updated MediaHouse basket state - #1.1 (TC24)

**Failure Pattern:**
Monetary fields serialised with IEEE-754 residuals instead of rounded decimal values.

**Evidence:**
- `orderAdDetails[0].discountAmount expected [63660.63] but found [63660.630000000005]` (TC1, TC3, TC4, TC5, TC6, TC7, TC9, TC11, TC15)
- `orderAdDetails.priceNet expected [[32131.849999999988, 124546.9]] but found [[32131.850000000002, 124546.9]]` (TC21, TC22, TC23, TC24)
- `orderAdDetails[0].priceNetExComm expected [66451.59999999998] but found [66451.6]` (TC11)
- `orderAdDetails.priceNetExComm expected [[38140.399999999994, ...]] but found [[38140.4, ...]]` (TC14)

**Impact:** 19 failures

**Confidence:** High

---

## Discount-type regression and basket pricing cascade

**Affected Features:**
- `rialtoB2A(CASS)TestCase3.feature`, `...4.feature`, `...5.feature`, `...9.feature`, `...11.feature`, `...15.feature`, `...22.feature`, `...27.feature`, `...37.feature`

**Affected Scenarios:**
- User perform CASS POST API - #1.1 (TC5, TC9)
- User perform CASS GET API - #1.1 (TC3, TC4, TC5, TC9, TC11, TC15, TC22)
- MEDIAHOUSE - Verify original order state in MediaHouse - #1.1 (TC37)
- MEDIAHOUSE - Verify updated MediaHouse basket state - #1.1 (TC27)

**Failure Pattern:**
`discountType` flips between `RIALTO`, `NONE`, and `null`; related commission, VAT, and basket totals diverge materially from expected values.

**Evidence:**
- `orders[0].printDetails.discountType expected [[NONE]] but found [[RIALTO]]` (TC4, TC9)
- `orders[0].printDetails.discountType expected [[null]] but found [[RIALTO]]` (TC11, TC15)
- `orders.printDetails.discountType expected [[RIALTO]] but found [[NONE]]` (TC27)
- `orders.printDetails.discountType expected [[null, null]] but found [[RIALTO, RIALTO]]` (TC37)
- `discountAmount expected [0.0] but found [63660.63]` (TC5)
- `discountAmount expected [0.0] but found [38197.97]` (TC9)
- `orderBasketPriceSummary.commission expected [3574.92] but found [3984.47]` (TC3)

**Impact:** 13 failures

**Confidence:** High

---

## Missing `PRELIMINARY` status flag on POST responses

**Affected Features:**
- `rialtoB2A(CASS)TestCase1.feature`, `rialtoB2A(CASS)TestCase3.feature`
- `rialtoB2A(CASS)TestCase4.feature`, `rialtoB2A(CASS)TestCase6.feature`

**Affected Scenarios:**
- User perform CASS POST API - #1.1 (TC1, TC3, TC4, TC6)

**Failure Pattern:**
`orderHeader.statusFlags` is returned as an empty list where `[PRELIMINARY]` is expected immediately after POST.

**Evidence:**
- `orderHeader.statusFlags expected [[PRELIMINARY]] but found [[]]` (TC1, TC3, TC4, TC6)

**Impact:** 4 failures

**Confidence:** High

---

## Order-line sequencing and stale placement state

**Affected Features:**
- `rialtoB2A(CASS)TestCase15.feature`, `...18.feature`, `...19.feature`, `...20.feature`, `...22.feature`, `...23.feature`, `...24.feature`, `...35.feature`, `...37.feature`

**Affected Scenarios:**
- User perform CASS POST API - #1.1 (TC15, TC18, TC19, TC20, TC22)
- Verify updated MediaHouse basket state - #1.1 (TC23)
- Verify reverted MediaHouse basket state - #1.1 (TC23, TC24)
- Revert two MediaHouse order lines to full page - #1.1 (TC24)
- RIALTO - Verify updated Agency order after Rialto change - #1.1 (TC35)
- MEDIAHOUSE - Verify updated MediaHouse basket state - #1.1 (TC37)

**Failure Pattern:**
Multi-line order responses return line items in wrong sequence; update/revert cycles retain stale `moduleCode`, `placementId`, or `issueDate` values.

**Evidence:**
- `orderAdDetails.packageId expected [[AB, SVD]] but found [[SVD, AB]]` (TC15, TC19, TC22)
- `orderAdDetails.packageId expected [[SVD, AB]] but found [[AB, SVD]]` (TC20)
- `orderAdDetails.moduleCode expected [[58, 54]] but found [[58, 58]]` (TC18)
- `orders.printDetails.paCode expected [[SVDTI, AB, SVDTI, ...]] but found [[AB, AB, AB, ...]]` (TC23, TC24)
- `body.orderAdDetailUpdates.placementId expected [[TEXT, ...]] but found [[UPPSLAG, ...]]` (TC24)
- `orderAdDetails.placementId expected [[SIDAN2]] but found [[HALVLIGG]]` (TC35)

**Impact:** 11 failures

**Confidence:** Medium

---

## Magazine basket discount and commission miscalculations

**Affected Features:**
- `rialtoB2A(CASS)TestCase26.feature`, `...28.feature`, `...30.feature`, `...31.feature`, `...32.feature`, `...33.feature`, `...34.feature`, `...35.feature`, `...36.feature`

**Affected Scenarios:**
- Verify reverted MediaHouse basket state - #1.1 (TC26)
- MEDIAHOUSE - Verify original full-page order state in MediaHouse - #1.1 (TC31)
- MEDIAHOUSE - Verify original magazine order state in MediaHouse - #1.1 (TC35, TC36)
- MEDIAHOUSE - Verify updated MediaHouse basket state - #1.1 (TC28, TC31)
- MEDIAHOUSE - Verify updated magazine order state in MediaHouse - #1.1 (TC32, TC33, TC34, TC35, TC36)
- RIALTO - Verify Rialto reflects the reverted full-page state - #1.1 (TC28, TC30, TC31)

**Failure Pattern:**
Magazine basket discount is applied when it should be zero, or applied at the wrong amount; commission and `priceNet` diverge from expected values after size/date/placement changes.

**Evidence:**
- `orderBasketPriceSummary.orderDiscount expected [0.00] but found [3600.00]` (TC26, TC32)
- `orderBasketPriceSummary.orderDiscount expected [0.00] but found [8800.00]` (TC34)
- `orderBasketPriceSummary.orderDiscount expected [3600.00] but found [4800.00]` (TC31, TC35, TC36)
- `orderBasketPriceSummary.commission expected [155.00] but found [250.00]` (TC28)
- `orderAdDetails.priceNet expected [[4845.0]] but found [[4969.0]]` (TC28, TC31)
- `INTEGRATION MISMATCH: MH basket ID (orBoxid) [7115] does not match Agency Prisa ID [7152]` (TC33)
- `INTEGRATION MISMATCH: MH basket ID (orBoxid) [7153] does not match Agency Prisa ID [7154]` (TC35)

**Impact:** 15 failures

**Confidence:** High

---

## Transaction rollback and path-parameter binding failures

**Affected Features:**
- `rialtoB2A(CASS)TestCase18.feature`, `rialtoB2A(CASS)TestCase23.feature`, `rialtoB2A(CASS)TestCase24.feature`

**Affected Scenarios:**
- User perform CASS POST API - #1.1 (TC18)
- Revert two MediaHouse order lines to full page - #1.1 (TC23, TC24)
- Verify Rialto reflects the reverted full-page state - #1.1 (TC24)

**Failure Pattern:**
Backend returns HTTP 500 rollback-only errors on multi-line update/revert operations; TC24 verification fails because `uuid` is absent and `agencyPrisaId` is passed as a redundant path parameter.

**Evidence:**
- `Transaction rolled back because it has been marked as rollback-only` (TC18, TC23)
- `Redundant path parameters are: agencyPrisaId=7143. Undefined path parameters are: uuid` (TC24)

**Impact:** 3 failures

**Confidence:** High
