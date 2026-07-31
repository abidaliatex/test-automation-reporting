# Jenkins Build Failure Report

---

## Build Summary

Build: `automationrunCAI-RIALTOB2A-IntegrationTesting-Internal-trunk` #156  
Date: 2026-07-31 12:22 UTC  
Status: `UNSTABLE`  
Total Tests: 514  
Passed: 449  
Failed: 65  
Pass Rate: 87.4%

---

## Root Cause Groups

## Floating-point precision drift in monetary fields

**Affected Features:**
- `rialtoB2A(CASS)TestCase1.feature`, `...3.feature`, `...4.feature`, `...5.feature`, `...6.feature`, `...9.feature`, `...11.feature`, `...14.feature`, `...15.feature`, `...21.feature`, `...22.feature`, `...23.feature`, `...24.feature`

**Affected Scenarios:**
- User perform CASS POST API - #1.1 (TC1, TC2, TC3, TC4, TC5, TC6, TC9, TC11, TC14, TC15, TC21, TC22)
- User perform CASS GET API - #1.1 (TC22)
- Verify created Rialto order and capture shared identifiers - #1.1 (TC23, TC24)
- Verify original full-page order state in MediaHouse - #1.1 (TC23)

**Failure Pattern:**
Financial fields are serialized with IEEE-754 residuals instead of the expected rounded values.

**Evidence:**
- `orderAdDetails[0].discountAmount expected [63660.63] but found [63660.630000000005]`
- `orderAdDetails[0].priceNetExComm expected [66451.59999999998] but found [66451.6]`
- `orders[0].printDetails.netAmount expected [[33159.79999999999, 128531.37, ...]] but found [[33159.8, 128531.37, ...]]`

**Impact:** 13 failures

**Confidence:** High

---

## Discount-type and pricing-rule regression

**Affected Features:**
- `rialtoB2A(CASS)TestCase4.feature`, `...5.feature`, `...9.feature`, `...11.feature`, `...15.feature`, `...22.feature`, `...26.feature`, `...27.feature`, `...28.feature`, `...30.feature`, `...31.feature`, `...32.feature`, `...33.feature`, `...34.feature`, `...35.feature`, `...36.feature`, `...37.feature`

**Affected Scenarios:**
- User perform CASS POST API - #1.1 (TC5, TC9)
- User perform CASS GET API - #1.1 (TC4, TC11, TC15, TC22)
- MediaHouse basket/order verification - #1.1 (TC26, TC27, TC31, TC32, TC33, TC34, TC35, TC36, TC37)
- Rialto reverted/updated order verification - #1.1 (TC28, TC30, TC31, TC35)

**Failure Pattern:**
`discountType` flips between `RIALTO`, `NONE`, and `null`, and related discount, commission, VAT, and total fields diverge materially from expected values.

**Evidence:**
- `orders[0].printDetails.discountType expected [[null]] but found [[RIALTO]]`
- `orders.printDetails.discountType expected [[RIALTO]] but found [[NONE]]`
- `orderBasketPriceSummary.orderDiscount expected [3600.00] but found [4800.00]`

**Impact:** 25 failures

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
- `rialtoB2A(CASS)TestCase15.feature`, `...18.feature`, `...22.feature`, `...23.feature`, `...24.feature`, `...35.feature`

**Affected Scenarios:**
- User perform CASS POST API - #1.1 (TC15, TC18, TC22)
- Verify updated/reverted MediaHouse basket state - #1.1 (TC23, TC24)
- Revert two MediaHouse order lines to full page - #1.1 (TC24)
- RIALTO - Verify updated Agency order after Rialto change - #1.1 (TC35)
- MEDIAHOUSE - Verify updated magazine order state in MediaHouse - #1.1 (TC35)

**Failure Pattern:**
Multi-line order responses return line items in a different order than expected, retain stale placement/date/module state after updates, or carry a mismatched basket identifier into verification.

**Evidence:**
- `orderAdDetails.packageId expected [[AB, SVD]] but found [[SVD, AB]]`
- `body.orderAdDetailUpdates.packageId expected [[SVDTI, SVDTI, SVDTI, AB, AB, AB]] but found [[SVDTI, AB, SVDTI, AB, AB, SVDTI]]`
- `orderAdDetails.placementId expected [[SIDAN2]] but found [[HALVLIGG]]`
- `INTEGRATION MISMATCH: MH basket ID (orBoxid) [7079] does not match Agency Prisa ID [7080]`

**Impact:** 8 failures

**Confidence:** Medium

---

## Transaction rollback and path-parameter binding failures

**Affected Features:**
- `rialtoB2A(CASS)TestCase18.feature`, `rialtoB2A(CASS)TestCase23.feature`
- `rialtoB2A(CASS)TestCase24.feature`

**Affected Scenarios:**
- User perform CASS POST API - #1.1 (TC18)
- Revert two MediaHouse order lines to full page - #1.1 (TC23)
- Verify Rialto reflects the reverted full-page state - #1.1 (TC24)

**Failure Pattern:**
Backend returns HTTP 500 rollback-only errors, and one verification step fails because `uuid` is missing while an unexpected `agencyPrisaId` path parameter is present.

**Evidence:**
- `Transaction rolled back because it has been marked as rollback-only`
- `Path parameters were not correctly defined. Redundant path parameters are: agencyPrisaId=7069. Undefined path parameters are: uuid`

**Impact:** 3 failures

**Confidence:** High
