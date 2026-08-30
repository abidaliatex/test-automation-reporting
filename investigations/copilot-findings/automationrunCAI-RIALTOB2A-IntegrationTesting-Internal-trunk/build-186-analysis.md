# Build 186 — Investigation Analysis

**Source report:** [build-186.md](../../../reports/build-failures/automationrunCAI-RIALTOB2A-IntegrationTesting-Internal-trunk/build-186.md)

---

## Build Summary

Build: 186  
Total Tests: 514  
Passed: 453  
Failed: 61  
Pass Rate: 88.1%

---

## Root Cause Groups

## Order field/state mismatch after update flows

**Affected Features:**
- `rialtoB2A(CASS)TestCase4.feature`, `rialtoB2A(CASS)TestCase5.feature`, `rialtoB2A(CASS)TestCase6.feature`, `rialtoB2A(CASS)TestCase9.feature`
- `rialtoB2A(CASS)TestCase14.feature` through `rialtoB2A(CASS)TestCase24.feature`
- `rialtoB2A(CASS)TestCase28.feature`, `rialtoB2A(CASS)TestCase29.feature`, `rialtoB2A(CASS)TestCase32.feature`, `rialtoB2A(CASS)TestCase33.feature`, `rialtoB2A(CASS)TestCase35.feature`, `rialtoB2A(CASS)TestCase36.feature`, `rialtoB2A(CASS)TestCase37.feature`

**Affected Scenarios:**
- User perform CASS POST API (TC4, TC5, TC6, TC9, TC14, TC15, TC16, TC17, TC18, TC19, TC20, TC21, TC22)
- User perform CASS GET API (TC9, TC14, TC15, TC16, TC17, TC18, TC19, TC20, TC22)
- Verify created Rialto order and capture shared identifiers (TC23)
- Verify original full-page order state in MediaHouse (TC23, TC24)
- Verify updated MediaHouse basket state (TC23, TC24, TC37)
- Verify reverted MediaHouse basket state (TC23, TC24)
- RIALTO - Verify Rialto reflects the reverted full-page state (TC28, TC29)
- MEDIAHOUSE - Verify updated magazine order state in MediaHouse (TC32, TC33, TC36)
- RIALTO - Verify updated Agency order after Rialto change (TC35)
- MEDIAHOUSE - Verify original order state in MediaHouse (TC37)
- RIALTO - Verify Rialto reflects the updated state (TC37)

**Failure Pattern:**
`Mismatch on field: orderAdDetails.packageId expected [RIALTO order] found [reordered/incorrect values]`

**Evidence:**
- `Mismatch on field: orderAdDetails.packageId expected [[SVD, AB]] but found [[AB, SVD]]`
- `Mismatch on field: orders[0].printDetails.paCode expected [[SVDTI, AB]] but found [[AB, SVDTI]]`
- `Mismatch on field: orderHeader.statusFlags expected [[PRELIMINARY]] but found [[]]`

**Impact:** 46 failures

**Confidence:** High

## Transaction rollback on MediaHouse updates

**Affected Features:**
- `rialtoB2A(CASS)TestCase22.feature`
- `rialtoB2A(CASS)TestCase23.feature`
- `rialtoB2A(CASS)TestCase24.feature`
- `rialtoB2A(CASS)TestCase37.feature`

**Affected Scenarios:**
- User perform CASS POST API (TC22)
- Update two MediaHouse order lines to uppslag (TC23, TC24)
- Revert two MediaHouse order lines to full page (TC23, TC24)
- MEDIAHOUSE - Update MediaHouse order head line to change date (TC37)

**Failure Pattern:**
`Transaction rolled back because it has been marked as rollback-only`

**Evidence:**
- Update/revert API calls return HTTP 500 with rollback-only payload.
- Same rollback error appears in TC22, TC23, TC24, and TC37 write steps.

**Impact:** 7 failures

**Confidence:** High

## Internal server error on POST

**Affected Features:**
- `rialtoB2A(CASS)TestCase14.feature`
- `rialtoB2A(CASS)TestCase21.feature`

**Affected Scenarios:**
- User perform CASS POST API (TC14)
- User perform CASS POST API (TC21)

**Failure Pattern:**
`{"errorCode":1,"message":null} expected [N200] but found [N500]`

**Evidence:**
- POST step fails before downstream verification in both TCs.
- Error body has null message, indicating unhandled server-side failure path.

**Impact:** 2 failures

**Confidence:** Medium

## Path parameter / basket ID propagation errors

**Affected Features:**
- `rialtoB2A(CASS)TestCase24.feature`
- `rialtoB2A(CASS)TestCase35.feature`
- `rialtoB2A(CASS)TestCase36.feature`

**Affected Scenarios:**
- Verify Rialto reflects the reverted full-page state (TC24)
- MEDIAHOUSE - Verify original magazine order state in MediaHouse (TC35)
- MEDIAHOUSE - Verify original magazine order state in MediaHouse (TC36)

**Failure Pattern:**
`Undefined path parameters are: uuid / mhBasketOrderId`

**Evidence:**
- `Redundant path parameters are: agencyPrisaId=8346. Undefined path parameters are: uuid.`
- `Invalid number of path parameters. Expected 1, was 0. Undefined path parameters are: mhBasketOrderId.`

**Impact:** 3 failures

**Confidence:** High

## Basket lookup and ID synchronization failures

**Affected Features:**
- `rialtoB2A(CASS)TestCase35.feature`
- `rialtoB2A(CASS)TestCase36.feature`

**Affected Scenarios:**
- MEDIAHOUSE - User perform CASS POST API (TC35)
- MEDIAHOUSE - User perform CASS POST API (TC36)
- MEDIAHOUSE - Verify updated magazine order state in MediaHouse (TC35)

**Failure Pattern:**
`Basket not found for campaign / INTEGRATION MISMATCH`

**Evidence:**
- `Basket not found for campaign: TestCase35 expected [false] but found [true]`
- `Basket not found for campaign: TestCase36 expected [false] but found [true]`
- `INTEGRATION MISMATCH: MH basket ID (orBoxid) [8356] does not match Agency Prisa ID [8357]`

**Impact:** 3 failures

**Confidence:** Medium
