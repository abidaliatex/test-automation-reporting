# Jenkins Build Failure Report

---

## Build Summary

Build: `automationrunCAI-RIALTOB2A-IntegrationTesting-Internal-trunk` #157  
Date: 2026-07-31 21:03 UTC  
Status: `UNSTABLE`  
Total Tests: 514  
Passed: 445  
Failed: 69  
Pass Rate: 86.6%

---

## Root Cause Groups

## Floating-point precision drift in monetary fields

**Affected Features:**
- `rialtoB2A(CASS)TestCase1.feature`, `...3.feature`, `...4.feature`, `...5.feature`, `...6.feature`, `...9.feature`, `...11.feature`, `...14.feature`, `...15.feature`, `...21.feature`, `...22.feature`, `...23.feature`, `...24.feature`

**Affected Scenarios:**
- User perform CASS POST API - #1.1 (TC1, TC2, TC3, TC4, TC5, TC6, TC9, TC11, TC14, TC15, TC21)
- User perform CASS GET API - #1.1 (TC9, TC22)
- Verify created Rialto order and capture shared identifiers - #1.1 (TC23, TC24)
- Verify original full-page order state in MediaHouse - #1.1 (TC23, TC24)
- Verify updated MediaHouse basket state - #1.1 (TC21, TC23, TC24)
- Verify reverted MediaHouse basket state - #1.1 (TC23, TC24)

**Failure Pattern:**
Financial fields serialised with IEEE-754 residuals instead of rounded decimal values.

**Evidence:**
- `orderAdDetails[0].discountAmount expected [63660.63] but found [63660.630000000005]`
- `orderAdDetails[0].priceNetExComm expected [66451.59999999998] but found [66451.6]`
- `orderAdDetails.priceNet expected [[32131.849999999988, 124546.9]] but found [[32131.850000000002, 124546.9]]`
- `orders[0].printDetails.netAmount expected [[33159.79999999999, 128531.37, ...]] but found [[33159.8, 128531.37, ...]]`

**Impact:** 14 failures

**Confidence:** High

---

## Discount-type and pricing-rule regression

**Affected Features:**
- `rialtoB2A(CASS)TestCase4.feature`, `...5.feature`, `...9.feature`, `...11.feature`, `...15.feature`, `...22.feature`, `...26.feature`, `...27.feature`, `...28.feature`, `...30.feature`, `...31.feature`, `...35.feature`, `...36.feature`, `...37.feature`

**Affected Scenarios:**
- User perform CASS POST API - #1.1 (TC5, TC9)
- User perform CASS GET API - #1.1 (TC4, TC11, TC15, TC22)
- MEDIAHOUSE - Verify original full-page/magazine order state in MediaHouse - #1.1 (TC26, TC31, TC35, TC36)
- MEDIAHOUSE - Verify updated MediaHouse basket state - #1.1 (TC28, TC31, TC37)
- MEDIAHOUSE - Verify updated magazine order state in MediaHouse - #1.1 (TC36)
- MEDIAHOUSE - Verify original order state in MediaHouse - #1.1 (TC27, TC37)
- RIALTO - Verify Rialto reflects the reverted full-page state - #1.1 (TC28, TC30, TC31)
- RIALTO - Verify updated Agency order after Rialto change - #1.1 (TC35)

**Failure Pattern:**
`discountType` flips between `RIALTO`, `NONE`, and `null`; related discount, commission, VAT, and basket total fields diverge materially from expected values.

**Evidence:**
- `orders[0].printDetails.discountType expected [[null]] but found [[RIALTO]]` (TC11, TC15)
- `orders.printDetails.discountType expected [[RIALTO]] but found [[NONE]]` (TC27)
- `orderBasketPriceSummary.orderDiscount expected [3600.00] but found [4800.00]` (TC31, TC35, TC36)
- `orderBasketPriceSummary.commission expected [155.00] but found [250.00]` (TC28)
- `orderAdDetails.priceNet expected [[4845.0]] but found [[4969.0]]` (TC28)
- `discountAmount expected [0.0] but found [63660.63]` (TC5, TC9)

**Impact:** 27 failures

**Confidence:** High

---

## Missing `PRELIMINARY` status flag on POST responses

**Affected Features:**
- `rialtoB2A(CASS)TestCase1.feature`, `rialtoB2A(CASS)TestCase3.feature`
- `rialtoB2A(CASS)TestCase4.feature`, `rialtoB2A(CASS)TestCase6.feature`

**Affected Scenarios:**
- User perform CASS POST API - #1.1 (TC1, TC2, TC3, TC4, TC6)

**Failure Pattern:**
`orderHeader.statusFlags` is returned as an empty list where `[PRELIMINARY]` is expected immediately after POST.

**Evidence:**
- `orderHeader.statusFlags expected [[PRELIMINARY]] but found [[]]`

**Impact:** 4 failures

**Confidence:** High

---

## Order-line sequencing, stale state, and ID handoff mismatches

**Affected Features:**
- `rialtoB2A(CASS)TestCase15.feature`, `...18.feature`, `...20.feature`, `...24.feature`
- `rialtoB2A(CASS)TestCase32.feature`, `...33.feature`, `...34.feature`, `...35.feature`, `...37.feature`

**Affected Scenarios:**
- User perform CASS POST API - #1.1 (TC15, TC18, TC20)
- Verify created Rialto order and capture shared identifiers - #1.1 (TC24)
- MEDIAHOUSE - Verify updated MediaHouse basket state - #1.1 (TC24, TC37)
- MEDIAHOUSE - Verify updated magazine order state in MediaHouse - #1.1 (TC32, TC33, TC34, TC35)
- MEDIAHOUSE - Verify original order state in MediaHouse - #1.1 (TC37)

**Failure Pattern:**
Multi-line order responses return line items in wrong sequence, retain stale placement/module state after updates, or carry a mismatched basket identifier into verification.

**Evidence:**
- `orderAdDetails.packageId expected [[AB, SVD]] but found [[SVD, AB]]` (TC15)
- `orderAdDetails.packageId expected [[SVD, AB]] but found [[AB, SVD]]` (TC20)
- `orderAdDetails.moduleCode expected [[58, 54]] but found [[58, 58]]` (TC18)
- `orders.printDetails.paCode expected [[SVDTI, SVDTI, AB, ...]] but found [[SVDTI, SVDTI, SVDTI, AB, ...]]` (TC24, TC37)
- `INTEGRATION MISMATCH: MH basket ID (orBoxid) [4476] does not match Agency Prisa ID [7114]` (TC32)
- `INTEGRATION MISMATCH: MH basket ID (orBoxid) [6826] does not match Agency Prisa ID [7115]` (TC33)
- `INTEGRATION MISMATCH: MH basket ID (orBoxid) [4956] does not match Agency Prisa ID [7116]` (TC34)
- `INTEGRATION MISMATCH: MH basket ID (orBoxid) [5410] does not match Agency Prisa ID [7117]` (TC35)

**Impact:** 21 failures

**Confidence:** Medium

---

## Transaction rollback and path-parameter binding failures

**Affected Features:**
- `rialtoB2A(CASS)TestCase18.feature`, `rialtoB2A(CASS)TestCase24.feature`

**Affected Scenarios:**
- User perform CASS POST API - #1.1 (TC18)
- Revert two MediaHouse order lines to full page - #1.1 (TC24)
- Verify Rialto reflects the reverted full-page state - #1.1 (TC24)

**Failure Pattern:**
Backend returns HTTP 500 rollback-only errors; one verification step fails because `uuid` is missing while an unexpected `agencyPrisaId` path parameter is present.

**Evidence:**
- `Transaction rolled back because it has been marked as rollback-only` (TC18, TC24)
- `Path parameters were not correctly defined. Redundant path parameters are: agencyPrisaId=7106. Undefined path parameters are: uuid` (TC24)

**Impact:** 3 failures

**Confidence:** High
