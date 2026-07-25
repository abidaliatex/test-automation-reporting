# Jenkins Build Failure Report

---

## Build Summary

Build: `automationrunCAI-RIALTOB2A-IntegrationTesting-Internal-trunk` #150  
Date: 2026-07-25 21:03 UTC  
Status: UNSTABLE  
Total Tests: 513  
Passed: 427  
Failed: 86  
Pass Rate: 83.2%

---

## Root Cause Groups

## `discountType` expected `[RIALTO]` but found `[null]`

**Affected Features:**
- `rialtoB2A(CASS)TestCase1.feature`, `rialtoB2A(CASS)TestCase3.feature`, `rialtoB2A(CASS)TestCase4.feature`, `rialtoB2A(CASS)TestCase5.feature`, `rialtoB2A(CASS)TestCase6.feature`, `rialtoB2A(CASS)TestCase9.feature`, `rialtoB2A(CASS)TestCase11.feature`, `rialtoB2A(CASS)TestCase14.feature`, `rialtoB2A(CASS)TestCase15.feature`
- `rialtoB2A(CASS)TestCase22.feature`, `rialtoB2A(CASS)TestCase23.feature`, `rialtoB2A(CASS)TestCase24.feature`, `rialtoB2A(CASS)TestCase26.feature`
- `rialtoB2A(CASS)TestCase27.feature`–`rialtoB2A(CASS)TestCase36.feature`

**Affected Scenarios:**
- `User perform CASS GET API - #1.1` (TC1 and TC2, TC3, TC4, TC5, TC6, TC9, TC11, TC14, TC15, TC22)
- `Verify original full-page order state in MediaHouse - #1.1` (TC23, TC24)
- `Verify updated MediaHouse basket state - #1.1` (TC23, TC24)
- `Verify reverted MediaHouse basket state - #1.1` (TC23, TC24, TC26)
- `MEDIAHOUSE - Verify original full-page order state in MediaHouse - #1.1` (TC27, TC28, TC29, TC30, TC31)
- `MEDIAHOUSE - Verify updated MediaHouse basket state - #1.1` (TC27)
- `MEDIAHOUSE - Verify original magazine order state in MediaHouse - #1.1` (TC32, TC33, TC34, TC35, TC36)
- `MEDIAHOUSE - Verify updated magazine order state in MediaHouse - #1.1` (TC32, TC33, TC34, TC36)

**Failure Pattern:**
`orders[*].printDetails.discountType` is `null` where fixtures expect `RIALTO`; basket-level discount totals also drift in the same responses.

**Evidence:**
- `orders[0].printDetails.discountType expected [[RIALTO]] but found [[null]]`
- `orderBasketPriceSummary.totalInclVat expected [169660.xx] but found [different]`

**Impact:** 40 failures

**Confidence:** High

---

## Financial and Amount Calculation Mismatch

**Affected Features:**
- `rialtoB2A(CASS)TestCase1.feature`, `rialtoB2A(CASS)TestCase3.feature`, `rialtoB2A(CASS)TestCase4.feature`, `rialtoB2A(CASS)TestCase5.feature`, `rialtoB2A(CASS)TestCase6.feature`, `rialtoB2A(CASS)TestCase9.feature`, `rialtoB2A(CASS)TestCase11.feature`, `rialtoB2A(CASS)TestCase15.feature`
- `rialtoB2A(CASS)TestCase27.feature`, `rialtoB2A(CASS)TestCase28.feature`, `rialtoB2A(CASS)TestCase29.feature`, `rialtoB2A(CASS)TestCase30.feature`, `rialtoB2A(CASS)TestCase31.feature`, `rialtoB2A(CASS)TestCase35.feature`, `rialtoB2A(CASS)TestCase37.feature`

**Affected Scenarios:**
- `User perform CASS GET API - #1.1` (TC1 and TC2, TC3, TC4, TC5, TC6, TC9, TC11, TC15)
- `User perform CASS POST API - #1.1` (TC1 and TC2, TC3, TC4, TC5, TC15)
- `MEDIAHOUSE - Verify updated MediaHouse basket state - #1.1` (TC27, TC28, TC29, TC30, TC31, TC37)
- `RIALTO - Verify Rialto reflects the reverted full-page state - #1.1` (TC29)
- `RIALTO - Verify updated Agency order after Rialto change - #1.1` (TC35)

**Failure Pattern:**
Order totals (`netAmount`, `discountAmount`, `commissionAmount`, `totalInclVat`) and status flags return wrong or stale values after create/update operations; some mismatches are floating-point precision (e.g. `38140.399999999994` vs `38140.4`).

**Evidence:**
- `discountAmount expected [0.0] but found [63660.63]`
- `orderHeader.statusFlags expected [[PRELIMINARY]] but found [[]]`
- `netAmount expected [[192192.0]] but found [[128531.37]]`
- `orderAdDetails.discountAmount expected [[99479.4, 63660.63]] but found [[132639.2, 63660.63]]`

**Impact:** 23 failures

**Confidence:** High

---

## Two-product MH parser / TestContext cascade

**Affected Features:**
- `rialtoB2A(CASS)TestCase16.feature`, `rialtoB2A(CASS)TestCase17.feature`, `rialtoB2A(CASS)TestCase18.feature`, `rialtoB2A(CASS)TestCase19.feature`, `rialtoB2A(CASS)TestCase20.feature`

**Affected Scenarios:**
- `User perform CASS GET API - #1.1` (TC16, TC17, TC18, TC19, TC20)
- `User perform CASS POST API - #1.1` (TC16, TC17, TC18, TC19, TC20)

**Failure Pattern:**
The MH two-product GET step reads past the available columns, fails to store `odIds`, and the downstream POST step cannot proceed; wrong field values (`moduleCode`, `placementId`) also returned when execution continues.

**Evidence:**
- `Index 13 out of bounds for length 13`
- `No MH odIds found in TestContext. Run the MH GET storage step before the patch step.`
- `orderAdDetails.moduleCode expected [[54, 58]] but found [[58, 58]]`
- `orderAdDetails.placementId expected [[TEXT, SIDAN3]] but found [[TEXT, TEXT]]`

**Impact:** 10 failures

**Confidence:** High

---

## issueDate Not Propagated After Date-Change Operations

**Affected Features:**
- `rialtoB2A(CASS)TestCase15.feature`, `rialtoB2A(CASS)TestCase16.feature`, `rialtoB2A(CASS)TestCase22.feature`, `rialtoB2A(CASS)TestCase24.feature`, `rialtoB2A(CASS)TestCase27.feature`, `rialtoB2A(CASS)TestCase35.feature`

**Affected Scenarios:**
- `User perform CASS POST API - #1.1` (TC16, TC22)
- `User perform CASS GET API - #1.1` (TC15)
- `Revert two MediaHouse order lines to full page - #1.1` (TC24)
- `MEDIAHOUSE - Verify updated MediaHouse basket state - #1.1` (TC27)
- `RIALTO - Verify updated Agency order after Rialto change - #1.1` (TC35)

**Failure Pattern:**
After date-change operations, the returned `issueDate` does not reflect the updated value; one case (TC16) shows a date stuck at the original instead of updated.

**Evidence:**
- `body.orderAdDetailUpdates.issueDate expected [[2026-07-01, 2026-07-21]] but found [[2026-07-01, 2026-07-01]]`

**Impact:** 7 failures

**Confidence:** High

---

## Path Parameter Binding Error and Basket ID Drift

**Affected Features:**
- `rialtoB2A(CASS)TestCase24.feature`, `rialtoB2A(CASS)TestCase35.feature`

**Affected Scenarios:**
- `Verify Rialto reflects the reverted full-page state - #1.1` (TC24 in MH change from uppslag to Full page)
- `MEDIAHOUSE - Verify updated magazine order state in MediaHouse - #1.1` (TC35 Magazine change Date Size & Placement from Rialto)

**Failure Pattern:**
TC24 has a step-definition binding error where `agencyPrisaId` is supplied but `uuid` is left undefined. TC35 ends with a cross-system identifier mismatch between the MH basket and Agency Prisa IDs.

**Evidence:**
- `Path parameters were not correctly defined. Redundant path parameters are: agencyPrisaId=6780. Undefined path parameters are: uuid.`
- `INTEGRATION MISMATCH: MH basket ID (orBoxid) [6790] does not match Agency Prisa ID [6791]`

**Impact:** 2 failures

**Confidence:** Medium

---

## Failing Tests / Steps

- 86 Jenkins-reported failures across 513 tests.
- Failure count matches build #149 (86 failures); no regression or recovery in this run.
- Dominant recurring defect: `discountType` returning `null` for Rialto-originated flows (unchanged from builds #148–#149).
