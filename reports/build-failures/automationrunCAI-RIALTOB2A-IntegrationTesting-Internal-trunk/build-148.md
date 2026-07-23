# Jenkins Build Failure Report

---

## Build Summary

Build: `automationrunCAI-RIALTOB2A-IntegrationTesting-Internal-trunk` #148  
Date: 2026-07-23 21:03 UTC  
Status: UNSTABLE  
Total Tests: 513  
Passed: 425  
Failed: 88  
Pass Rate: 82.8%

---

## Root Cause Groups

## `discountType` expected `[RIALTO]` but found `[null]`

**Affected Features:**
- `rialtoB2A(CASS)TestCase1.feature`, `rialtoB2A(CASS)TestCase3.feature`, `rialtoB2A(CASS)TestCase4.feature`, `rialtoB2A(CASS)TestCase5.feature`, `rialtoB2A(CASS)TestCase6.feature`, `rialtoB2A(CASS)TestCase7.feature`, `rialtoB2A(CASS)TestCase9.feature`, `rialtoB2A(CASS)TestCase11.feature`
- `rialtoB2A(CASS)TestCase26.feature`–`rialtoB2A(CASS)TestCase36.feature`

**Affected Scenarios:**
- `User perform CASS GET API - #1.1` (TC1 and TC2, TC3, TC4, TC5, TC6, TC7, TC9, TC11)
- `Verify reverted MediaHouse basket state - #1.1` (TC26 Basic order for magazines)
- `MEDIAHOUSE - Verify original full-page order state in MediaHouse - #1.1` (TC27, TC28, TC29, TC30, TC31)
- `MEDIAHOUSE - Verify original magazine order state in MediaHouse - #1.1` (TC32, TC33, TC34, TC35, TC36)
- `MEDIAHOUSE - Verify updated MediaHouse basket state - #1.1` (TC27, TC29, TC31)
- `MEDIAHOUSE - Verify updated magazine order state in MediaHouse - #1.1` (TC32, TC33, TC34, TC36)
- `RIALTO - Verify Rialto reflects the reverted full-page state - #1.1` (TC27)

**Failure Pattern:**
`orders[*].printDetails.discountType` is `null` where the fixtures expect `RIALTO`; the same responses also show missing basket discounts.

**Evidence:**
- `orders[0].printDetails.discountType expected [[RIALTO]] but found [[null]]`
- `orders.printDetails.discountType expected [[RIALTO]] but found [[null]]`
- `orderBasketPriceSummary.orderDiscount expected [0.00] but found [3600.00]`

**Impact:** 24 failures

**Confidence:** High

---

## Financial calculation and state drift after update flows

**Affected Features:**
- `rialtoB2A(CASS)TestCase1.feature`, `rialtoB2A(CASS)TestCase3.feature`, `rialtoB2A(CASS)TestCase4.feature`, `rialtoB2A(CASS)TestCase5.feature`, `rialtoB2A(CASS)TestCase6.feature`, `rialtoB2A(CASS)TestCase9.feature`, `rialtoB2A(CASS)TestCase11.feature`, `rialtoB2A(CASS)TestCase14.feature`, `rialtoB2A(CASS)TestCase15.feature`, `rialtoB2A(CASS)TestCase16.feature`
- `rialtoB2A(CASS)TestCase22.feature`, `rialtoB2A(CASS)TestCase23.feature`, `rialtoB2A(CASS)TestCase27.feature`–`rialtoB2A(CASS)TestCase31.feature`, `rialtoB2A(CASS)TestCase35.feature`, `rialtoB2A(CASS)TestCase37.feature`

**Affected Scenarios:**
- `User perform CASS GET API - #1.1` (TC1 and TC2, TC3, TC4, TC5, TC6, TC9, TC11, TC14, TC15, TC22)
- `User perform CASS POST API - #1.1` (TC1 and TC2, TC3, TC4, TC5, TC6, TC15, TC16)
- `Verify original full-page order state in MediaHouse - #1.1` (TC23)
- `RIALTO - Verify created Rialto order and capture shared identifiers - #1.1` (TC27, TC28)
- `MEDIAHOUSE - Update two MediaHouse order lines to uppslag - #1.1` (TC27)
- `MEDIAHOUSE - Verify updated MediaHouse basket state - #1.1` (TC27, TC28, TC29, TC31)
- `RIALTO - Verify Rialto reflects the reverted full-page state - #1.1` (TC27, TC28, TC30, TC31)
- `RIALTO - Verify updated Agency order after Rialto change - #1.1` (TC35)
- `MEDIAHOUSE - Verify original order state in MediaHouse - #1.1` (TC37)

**Failure Pattern:**
Order totals, commission, issue dates, placement-derived values, and `statusFlags` drift from the fixtures after create/update operations.

**Evidence:**
- `discountAmount expected [0.0] but found [63660.63]`
- `orderHeader.statusFlags expected [[PRELIMINARY]] but found [[]]`
- `body.orderAdDetailUpdates.issueDate expected [[2026-08-19]] but found [[2026-08-26]]`
- `orderAdDetails.priceNet expected [[4845.0]] but found [[4969.0]]`

**Impact:** 32 failures

**Confidence:** High

---

## Two-product MH parser / TestContext cascade

**Affected Features:**
- `rialtoB2A(CASS)TestCase16.feature`, `rialtoB2A(CASS)TestCase17.feature`, `rialtoB2A(CASS)TestCase18.feature`, `rialtoB2A(CASS)TestCase19.feature`, `rialtoB2A(CASS)TestCase20.feature`

**Affected Scenarios:**
- `User perform CASS GET API - #1.1` (TC16, TC17, TC18, TC19, TC20)
- `User perform CASS POST API - #1.1` (TC16, TC17, TC18, TC19, TC20)

**Failure Pattern:**
The MH two-product GET step reads past the available columns, fails to store `odIds`, and downstream POST assertions either cascade or verify the wrong values.

**Evidence:**
- `Index 13 out of bounds for length 13`
- `No MH odIds found in TestContext. Run the MH GET storage step before the patch step.`
- `orderAdDetails.moduleCode expected [[54, 58]] but found [[58, 58]]`

**Impact:** 12 failures

**Confidence:** High

---

## Multi-line MH full-page / uppslag update instability

**Affected Features:**
- `rialtoB2A(CASS)TestCase22.feature`, `rialtoB2A(CASS)TestCase23.feature`, `rialtoB2A(CASS)TestCase24.feature`

**Affected Scenarios:**
- `User perform CASS GET API - #1.1` (TC22)
- `User perform CASS POST API - #1.1` (TC22)
- `Verify original full-page order state in MediaHouse - #1.1` (TC23, TC24)
- `Verify updated MediaHouse basket state - #1.1` (TC23, TC24)
- `Revert two MediaHouse order lines to full page - #1.1` (TC23, TC24)
- `Verify reverted MediaHouse basket state - #1.1` (TC23, TC24)
- `Update two MediaHouse order lines to uppslag - #1.1` (TC24)
- `Verify Rialto reflects the reverted full-page state - #1.1` (TC24)

**Failure Pattern:**
Full-page/uppslag changes on multi-line MH baskets show unstable ordering, rollback-only transactions, and one broken `uuid` path binding in the TC24 Rialto verification step.

**Evidence:**
- `body.orderAdDetailUpdates.packageId expected [[SVDTI, SVDTI, SVDTI, AB, AB, AB]] but found [[SVDTI, AB, SVDTI, AB, AB, SVDTI]]`
- `Transaction rolled back because it has been marked as rollback-only`
- `Path parameters were not correctly defined. Redundant path parameters are: agencyPrisaId=6702. Undefined path parameters are: uuid.`

**Impact:** 15 failures

**Confidence:** High

---

## Basket ID drift after Rialto-side magazine update

**Affected Features:**
- `rialtoB2A(CASS)TestCase35.feature`

**Affected Scenarios:**
- `MEDIAHOUSE - Verify updated magazine order state in MediaHouse - #1.1` (TC35 Magazine change Date Size & Placement from Rialto)

**Failure Pattern:**
The updated MH basket keeps a different basket ID than the Agency Prisa ID captured for the same order.

**Evidence:**
- `INTEGRATION MISMATCH: MH basket ID (orBoxid) [6712] does not match Agency Prisa ID [6713]`

**Impact:** 1 failure

**Confidence:** Medium

---

## Failing Tests / Steps

- 88 Jenkins-reported failures/regressions across 513 tests.
- Build #148 checked out revision `d120278b4bba91939ae718e0f45b6de5827461ac` (`updated testcase29 data`).
