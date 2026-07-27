# Jenkins Build Failure Report

---

## Build Summary

Build: `automationrunCAI-RIALTOB2A-IntegrationTesting-Internal-trunk` #152  
Date: 2026-07-27 21:03 UTC  
Status: UNSTABLE  
Total Tests: 514  
Passed: 430  
Failed: 84  
Pass Rate: 83.7%

---

## Root Cause Groups

## `discountType` expected `[RIALTO]` but found `[null]`

**Affected Features:**
- `rialtoB2A(CASS)TestCase1.feature`–`rialtoB2A(CASS)TestCase15.feature` (TC1 and TC2, TC3–TC6, TC9, TC11, TC14, TC15)
- `rialtoB2A(CASS)TestCase22.feature`–`rialtoB2A(CASS)TestCase24.feature`, `rialtoB2A(CASS)TestCase26.feature`
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
`orders[*].printDetails.discountType` returns `null` where the fixtures expect `RIALTO`; basket discount totals drift in the same MH/CASS responses.

**Evidence:**
- `orders[0].printDetails.discountType expected [[RIALTO]] but found [[null]]`
- `orders.printDetails.discountType expected [[RIALTO]] but found [[null]]`
- `orderBasketPriceSummary.orderDiscount expected [0.00] but found [3600.00]`

**Impact:** 36 failures

**Confidence:** High

---

## Financial and amount calculation mismatch

**Affected Features:**
- `rialtoB2A(CASS)TestCase1.feature`–`rialtoB2A(CASS)TestCase15.feature` (TC1 and TC2, TC3–TC6, TC9, TC11, TC14, TC15)
- `rialtoB2A(CASS)TestCase22.feature`–`rialtoB2A(CASS)TestCase24.feature`, `rialtoB2A(CASS)TestCase26.feature`
- `rialtoB2A(CASS)TestCase27.feature`–`rialtoB2A(CASS)TestCase37.feature`

**Affected Scenarios:**
- `User perform CASS GET API - #1.1` (TC1 and TC2, TC3, TC4, TC5, TC6, TC9, TC11, TC14, TC15, TC22)
- `User perform CASS POST API - #1.1` (TC1 and TC2, TC3, TC4, TC5, TC6, TC9, TC15)
- `Verify original full-page order state in MediaHouse - #1.1` (TC23, TC24)
- `Verify updated MediaHouse basket state - #1.1` (TC23, TC24)
- `Verify reverted MediaHouse basket state - #1.1` (TC23, TC24, TC26)
- `RIALTO - Verify created Rialto order and capture shared identifiers - #1.1` (TC27, TC28)
- `MEDIAHOUSE - Verify original full-page order state in MediaHouse - #1.1` (TC27, TC28, TC30, TC31)
- `MEDIAHOUSE - Verify updated MediaHouse basket state - #1.1` (TC27, TC28, TC31, TC37)
- `RIALTO - Verify Rialto reflects the reverted full-page state - #1.1` (TC27, TC28, TC30, TC31)
- `MEDIAHOUSE - Verify original magazine order state in MediaHouse - #1.1` (TC32, TC33, TC34, TC35, TC36)
- `MEDIAHOUSE - Verify updated magazine order state in MediaHouse - #1.1` (TC32, TC33, TC34, TC36)
- `RIALTO - Verify updated Agency order after Rialto change - #1.1` (TC35)
- `MEDIAHOUSE - Verify original order state in MediaHouse - #1.1` (TC37)

**Failure Pattern:**
`netAmount`, `discountAmount`, `commissionAmount`, `totalInclVat`, and `statusFlags` return stale or incorrect values after create/update flows; some failures are minor precision noise, but many are large calculation mismatches.

**Evidence:**
- `orders[0].printDetails.netAmount expected [[192192.0]] but found [[128531.37]]`
- `discountAmount expected [0.0] but found [63660.63]`
- `orderHeader.statusFlags expected [[PRELIMINARY]] but found [[]]`

**Impact:** 54 failures

**Confidence:** High

---

## Two-product MH parser / TestContext cascade

**Affected Features:**
- `rialtoB2A(CASS)TestCase16.feature`–`rialtoB2A(CASS)TestCase20.feature`

**Affected Scenarios:**
- `User perform CASS GET API - #1.1` (TC16, TC17, TC18, TC19, TC20)
- `User perform CASS POST API - #1.1` (TC16, TC17, TC18, TC19, TC20)

**Failure Pattern:**
The two-product MH GET step reads past the available response columns, fails to store `odIds`, and the downstream POST validations then fail or validate the wrong line-level values.

**Evidence:**
- `Index 13 out of bounds for length 13`
- `No MH odIds found in TestContext. Run the MH GET storage step before the patch step.`
- `orderAdDetails.moduleCode expected [[54, 58]] but found [[58, 58]]`

**Impact:** 10 failures

**Confidence:** High

---

## Date-change propagation drift

**Affected Features:**
- `rialtoB2A(CASS)TestCase16.feature`, `rialtoB2A(CASS)TestCase27.feature`, `rialtoB2A(CASS)TestCase35.feature`

**Affected Scenarios:**
- `User perform CASS POST API - #1.1` (TC16)
- `MEDIAHOUSE - Update two MediaHouse order lines to uppslag - #1.1` (TC27)
- `MEDIAHOUSE - Verify updated MediaHouse basket state - #1.1` (TC27)
- `RIALTO - Verify Rialto reflects the reverted full-page state - #1.1` (TC27)
- `RIALTO - Verify updated Agency order after Rialto change - #1.1` (TC35)

**Failure Pattern:**
After date-change operations, the returned `issueDate` remains on the old value or drifts across MH/Rialto verification steps.

**Evidence:**
- `orderAdDetails.issueDate expected [[2026-07-01, 2026-07-21]] but found [[2026-07-01, 2026-07-01]]`
- `body.orderAdDetailUpdates.issueDate expected [[2026-08-19]] but found [[2026-08-26]]`
- `orders.printDetails.issueDate expected [[2026-08-19]] but found [[2026-08-26]]`

**Impact:** 5 failures

**Confidence:** Medium

---

## Transaction rollback, parameter wiring, and basket ID drift

**Affected Features:**
- `rialtoB2A(CASS)TestCase22.feature`, `rialtoB2A(CASS)TestCase24.feature`, `rialtoB2A(CASS)TestCase35.feature`

**Affected Scenarios:**
- `User perform CASS POST API - #1.1` (TC22)
- `Revert two MediaHouse order lines to full page - #1.1` (TC24)
- `Verify Rialto reflects the reverted full-page state - #1.1` (TC24)
- `MEDIAHOUSE - Verify updated magazine order state in MediaHouse - #1.1` (TC35)

**Failure Pattern:**
A server-side rollback aborts update/revert steps, one follow-up verification uses `agencyPrisaId` while leaving `uuid` undefined, and one magazine verification ends with MH/Agency basket IDs out of sync.

**Evidence:**
- `Transaction rolled back because it has been marked as rollback-only`
- `Path parameters were not correctly defined. Redundant path parameters are: agencyPrisaId=6893. Undefined path parameters are: uuid.`
- `INTEGRATION MISMATCH: MH basket ID (orBoxid) [6904] does not match Agency Prisa ID [6905]`

**Impact:** 4 failures

**Confidence:** Medium

---

## Failing Tests / Steps

- 84 Jenkins-reported failures across 514 executed tests.
- Most failures still cluster around missing `discountType` propagation and downstream price recalculation defects.
