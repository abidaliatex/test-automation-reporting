# Jenkins Build Failure Report

---

## Build Summary

Build: `automationrunCAI-RIALTOB2A-IntegrationTesting-Internal-trunk` #151  
Date: 2026-07-26 21:03 UTC  
Status: UNSTABLE  
Total Tests: 513  
Passed: 425  
Failed: 88  
Pass Rate: 82.8%

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
- `Verify updated MediaHouse basket state - #1.1` (TC23)
- `Verify reverted MediaHouse basket state - #1.1` (TC26)
- `MEDIAHOUSE - Verify original full-page order state in MediaHouse - #1.1` (TC27, TC28, TC29, TC30, TC31)
- `MEDIAHOUSE - Verify updated MediaHouse basket state - #1.1` (TC27)
- `MEDIAHOUSE - Verify original magazine order state in MediaHouse - #1.1` (TC32, TC33, TC34, TC35, TC36)
- `MEDIAHOUSE - Verify updated magazine order state in MediaHouse - #1.1` (TC32, TC33, TC34, TC36)

**Failure Pattern:**
`orders[*].printDetails.discountType` is `null` where fixtures expect `RIALTO`; basket-level discount totals also drift in the same responses.

**Evidence:**
- `orders[0].printDetails.discountType expected [[RIALTO]] but found [[null]]`
- `orderBasketPriceSummary.orderDiscount expected [0.00] but found [3600.00]`
- `orderBasketPriceSummary.netPrice expected [6000.00] but found [2400.00]`

**Impact:** ~40 failures

**Confidence:** High

---

## Financial and Amount Calculation Mismatch

**Affected Features:**
- `rialtoB2A(CASS)TestCase1.feature`, `rialtoB2A(CASS)TestCase3.feature`, `rialtoB2A(CASS)TestCase4.feature`, `rialtoB2A(CASS)TestCase5.feature`, `rialtoB2A(CASS)TestCase6.feature`, `rialtoB2A(CASS)TestCase9.feature`, `rialtoB2A(CASS)TestCase11.feature`, `rialtoB2A(CASS)TestCase15.feature`
- `rialtoB2A(CASS)TestCase22.feature`, `rialtoB2A(CASS)TestCase23.feature`, `rialtoB2A(CASS)TestCase24.feature`
- `rialtoB2A(CASS)TestCase27.feature`, `rialtoB2A(CASS)TestCase28.feature`, `rialtoB2A(CASS)TestCase29.feature`, `rialtoB2A(CASS)TestCase30.feature`, `rialtoB2A(CASS)TestCase31.feature`, `rialtoB2A(CASS)TestCase37.feature`

**Affected Scenarios:**
- `User perform CASS GET API - #1.1` (TC1 and TC2, TC3, TC4, TC5, TC6, TC9, TC11, TC15, TC22)
- `User perform CASS POST API - #1.1` (TC1 and TC2, TC3, TC4, TC5, TC6, TC9, TC15)
- `Verify updated MediaHouse basket state - #1.1` (TC24)
- `RIALTO - Verify created Rialto order and capture shared identifiers - #1.1` (TC27, TC28)
- `MEDIAHOUSE - Verify updated MediaHouse basket state - #1.1` (TC28, TC29, TC31, TC37)
- `RIALTO - Verify Rialto reflects the reverted full-page state - #1.1` (TC28, TC29, TC30, TC31)
- `MEDIAHOUSE - Verify original order state in MediaHouse - #1.1` (TC37)

**Failure Pattern:**
Order totals (`netAmount`, `discountAmount`, `commissionAmount`, `totalInclVat`) and `statusFlags` return wrong or stale values after create/update operations; some mismatches are floating-point precision (e.g. `33159.79999999999` vs `33159.8`), others are large discrepancies.

**Evidence:**
- `discountAmount expected [0.0] but found [63660.63]`
- `orderHeader.statusFlags expected [[PRELIMINARY]] but found [[]]`
- `orderHeader.commissionAmount expected [5957.95] but found [3984.47]`
- `discountAmount expected [[3600.0]] but found [3600.0]` (scalar vs array type mismatch, TC27/TC28)

**Impact:** ~23 failures

**Confidence:** High

---

## Two-product MH Parser / TestContext Cascade

**Affected Features:**
- `rialtoB2A(CASS)TestCase16.feature`, `rialtoB2A(CASS)TestCase17.feature`, `rialtoB2A(CASS)TestCase18.feature`, `rialtoB2A(CASS)TestCase19.feature`, `rialtoB2A(CASS)TestCase20.feature`

**Affected Scenarios:**
- `User perform CASS GET API - #1.1` (TC16, TC17, TC18, TC19, TC20)
- `User perform CASS POST API - #1.1` (TC16, TC17, TC18, TC19, TC20)

**Failure Pattern:**
The MH two-product GET step reads past the available response columns, fails to store `odIds`, and the downstream POST step cannot proceed; wrong field values (`moduleCode`, `placementId`) also returned when execution continues.

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
- `rialtoB2A(CASS)TestCase15.feature`, `rialtoB2A(CASS)TestCase16.feature`, `rialtoB2A(CASS)TestCase19.feature`, `rialtoB2A(CASS)TestCase20.feature`, `rialtoB2A(CASS)TestCase27.feature`, `rialtoB2A(CASS)TestCase35.feature`

**Affected Scenarios:**
- `User perform CASS POST API - #1.1` (TC15, TC16, TC19, TC20)
- `MEDIAHOUSE - Update two MediaHouse order lines to uppslag - #1.1` (TC27)
- `MEDIAHOUSE - Verify updated MediaHouse basket state - #1.1` (TC27)
- `RIALTO - Verify Rialto reflects the reverted full-page state - #1.1` (TC27)
- `RIALTO - Verify updated Agency order after Rialto change - #1.1` (TC35)

**Failure Pattern:**
After date-change operations via MH or Rialto, the returned `issueDate` does not reflect the updated value; order lines remain stuck at original dates.

**Evidence:**
- `orderAdDetails.issueDate expected [[2026-07-01, 2026-07-21]] but found [[2026-07-01, 2026-07-01]]`
- `orders.printDetails.issueDate expected [[2026-08-19]] but found [[2026-08-26]]`

**Impact:** 7 failures

**Confidence:** High

---

## Path Parameter Error, Transaction Rollback, and Basket ID Drift

**Affected Features:**
- `rialtoB2A(CASS)TestCase1.feature`, `rialtoB2A(CASS)TestCase24.feature`, `rialtoB2A(CASS)TestCase35.feature`

**Affected Scenarios:**
- `User perform CASS GET API - #1.1` (TC1 and TC2 — `mhBasketOrderId` undefined)
- `Revert two MediaHouse order lines to full page - #1.1` (TC24 — 500 transaction rollback)
- `Verify Rialto reflects the reverted full-page state - #1.1` (TC24 — `uuid` undefined)
- `MEDIAHOUSE - Verify updated magazine order state in MediaHouse - #1.1` (TC35 — basket ID mismatch)

**Failure Pattern:**
TC1 GET step missing required path parameter `mhBasketOrderId`; TC24 encounters a server-side transaction rollback and a follow-up step where `agencyPrisaId` is supplied but `uuid` is left undefined; TC35 ends with cross-system basket identifier drift.

**Evidence:**
- `Invalid number of path parameters. Expected 1, was 0. Undefined path parameters are: mhBasketOrderId.`
- `Transaction rolled back because it has been marked as rollback-only` → HTTP 500 (expected N200, got N400)
- `Path parameters were not correctly defined. Redundant path parameters are: agencyPrisaId=6817. Undefined path parameters are: uuid.`
- `INTEGRATION MISMATCH: MH basket ID (orBoxid) [6827] does not match Agency Prisa ID [6828]`

**Impact:** 8 failures

**Confidence:** Medium

---

## Failing Tests / Steps

- 88 Jenkins-reported failures across 513 tests.
- Failure count is up 2 from build #150 (86 failures); TC24 transaction rollback is a new failure type not seen in build #150.
- Dominant recurring defect: `discountType` returning `null` for Rialto-originated flows (unchanged from builds #148–#150).
