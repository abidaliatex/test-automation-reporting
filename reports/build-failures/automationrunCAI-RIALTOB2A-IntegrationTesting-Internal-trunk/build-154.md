# Jenkins Build Failure Report

---

## Build Summary

Build: `automationrunCAI-RIALTOB2A-IntegrationTesting-Internal-trunk` #154  
Total Tests: 514  
Passed: 428  
Failed: 86  
Pass Rate: 83.3%

---

## Root Cause Groups

## Missing `discountType` propagation (`RIALTO` -> `null`)

**Affected Features:**
- `rialtoB2A(CASS)TestCase1.feature`–`rialtoB2A(CASS)TestCase15.feature` (TC1, TC2, TC3, TC4, TC5, TC6, TC7, TC9, TC11, TC14, TC15)
- `rialtoB2A(CASS)TestCase22.feature`–`rialtoB2A(CASS)TestCase24.feature`, `rialtoB2A(CASS)TestCase26.feature`
- `rialtoB2A(CASS)TestCase27.feature`–`rialtoB2A(CASS)TestCase36.feature`

**Affected Scenarios:**
- User perform CASS GET API - #1.1 (TC1, TC2, TC3, TC4, TC5, TC6, TC7, TC9, TC11, TC14, TC15, TC22)
- Verify original full-page order state in MediaHouse - #1.1 (TC23, TC24)
- Verify updated MediaHouse basket state - #1.1 (TC23)
- Verify reverted MediaHouse basket state - #1.1 (TC23, TC26)
- MEDIAHOUSE - Verify original full-page order state in MediaHouse - #1.1 (TC27, TC28, TC29, TC30, TC31)
- MEDIAHOUSE - Verify original magazine order state in MediaHouse - #1.1 (TC32, TC33, TC34, TC35, TC36)
- MEDIAHOUSE - Verify updated magazine order state in MediaHouse - #1.1 (TC32, TC33, TC34, TC36)

**Failure Pattern:**
`orders[*].printDetails.discountType` expected `[RIALTO]` but returned `[null]`.

**Evidence:**
- `orders[0].printDetails.discountType expected [[RIALTO]] but found [[null]]`
- `orders.printDetails.discountType expected [[RIALTO]] but found [[null]]`

**Impact:** 34 failures

**Confidence:** High

## Financial value and status recalculation drift

**Affected Features:**
- `rialtoB2A(CASS)TestCase1.feature`–`rialtoB2A(CASS)TestCase15.feature` (TC1, TC2, TC3, TC4, TC5, TC6, TC7, TC9, TC11, TC14, TC15)
- `rialtoB2A(CASS)TestCase21.feature`–`rialtoB2A(CASS)TestCase24.feature`
- `rialtoB2A(CASS)TestCase27.feature`, `rialtoB2A(CASS)TestCase28.feature`, `rialtoB2A(CASS)TestCase30.feature`, `rialtoB2A(CASS)TestCase31.feature`, `rialtoB2A(CASS)TestCase37.feature`

**Affected Scenarios:**
- User perform CASS POST API - #1.1 (TC1, TC2, TC3, TC4, TC5, TC6, TC7, TC9, TC11, TC14, TC15, TC21, TC22)
- User perform CASS GET API - #1.1 (TC4, TC5, TC11)
- Verify created Rialto order and capture shared identifiers - #1.1 (TC23, TC24)
- RIALTO - Verify created Rialto order and capture shared identifiers - #1.1 (TC27, TC28)
- RIALTO - Verify Rialto reflects the reverted full-page state - #1.1 (TC28, TC30, TC31)
- MEDIAHOUSE - Verify updated MediaHouse basket state - #1.1 (TC28, TC31)
- MEDIAHOUSE - Verify original order state in MediaHouse - #1.1 (TC37)

**Failure Pattern:**
Amounts and status fields (for example `discountAmount`, `netAmount`, `priceNetExComm`, `statusFlags`) diverge from expected values after POST/GET validation.

**Evidence:**
- `discountAmount expected [0.0] but found [63660.63]`
- `orderHeader.statusFlags expected [[PRELIMINARY]] but found [[]]`
- `orderAdDetails[0].discountAmount expected [63660.63] but found [63660.630000000005]`

**Impact:** 34 failures

**Confidence:** High

## Multi-line update ordering and date propagation mismatches

**Affected Features:**
- `rialtoB2A(CASS)TestCase9.feature`, `rialtoB2A(CASS)TestCase15.feature`, `rialtoB2A(CASS)TestCase18.feature`
- `rialtoB2A(CASS)TestCase22.feature`, `rialtoB2A(CASS)TestCase24.feature`, `rialtoB2A(CASS)TestCase27.feature`
- `rialtoB2A(CASS)TestCase35.feature`, `rialtoB2A(CASS)TestCase37.feature`

**Affected Scenarios:**
- User perform CASS POST API - #1.1 (TC15, TC18, TC22)
- User perform CASS GET API - #1.1 (TC9, TC22)
- MEDIAHOUSE - Update two MediaHouse order lines to uppslag - #1.1 (TC27)
- RIALTO - Verify Rialto reflects the reverted full-page state - #1.1 (TC27)
- MEDIAHOUSE - Verify updated MediaHouse basket state - #1.1 (TC27, TC37)
- Verify updated MediaHouse basket state - #1.1 (TC24)
- Verify reverted MediaHouse basket state - #1.1 (TC24)
- RIALTO - Verify updated Agency order after Rialto change - #1.1 (TC35)

**Failure Pattern:**
Order-line ordering and date updates are inconsistent (`packageId/productId/plaCode/issueDate/moduleCode`) after update flows.

**Evidence:**
- `orderAdDetails.packageId expected [[AB, SVD]] but found [[SVD, AB]]`
- `body.orderAdDetailUpdates.issueDate expected [[2026-08-19]] but found [[2026-08-26]]`
- `orderAdDetails.moduleCode expected [[58, 54]] but found [[58, 58]]`

**Impact:** 13 failures

**Confidence:** Medium

## Transaction rollback and identifier binding failures

**Affected Features:**
- `rialtoB2A(CASS)TestCase18.feature`, `rialtoB2A(CASS)TestCase22.feature`, `rialtoB2A(CASS)TestCase24.feature`, `rialtoB2A(CASS)TestCase35.feature`

**Affected Scenarios:**
- User perform CASS POST API - #1.1 (TC18, TC22)
- Revert two MediaHouse order lines to full page - #1.1 (TC24)
- Verify Rialto reflects the reverted full-page state - #1.1 (TC24)
- MEDIAHOUSE - Verify updated magazine order state in MediaHouse - #1.1 (TC35)

**Failure Pattern:**
Update/revert flows fail with rollback-only transaction errors plus identifier wiring mismatches (`uuid` missing and MH basket ID drift).

**Evidence:**
- `Transaction rolled back because it has been marked as rollback-only`
- `Undefined path parameters are: uuid`
- `INTEGRATION MISMATCH: MH basket ID (orBoxid) [6991] does not match Agency Prisa ID [6992]`

**Impact:** 5 failures

**Confidence:** Medium
