# Build 184 — Investigation Analysis

**Source report:** [build-184.md](../../../reports/build-failures/automationrunCAI-RIALTOB2A-IntegrationTesting-Internal-trunk/build-184.md)

---

## Build Summary

Build: 184  
Total Tests: 514  
Passed: 458  
Failed: 56  
Pass Rate: 89.1%

---

## Root Cause Groups

### Order field/state mismatch

**Affected Features:**
- `rialtoB2A(CASS)TestCase4.feature`, `rialtoB2A(CASS)TestCase5.feature`, `rialtoB2A(CASS)TestCase6.feature`, `rialtoB2A(CASS)TestCase9.feature`
- `rialtoB2A(CASS)TestCase14.feature` through `rialtoB2A(CASS)TestCase24.feature`
- `rialtoB2A(CASS)TestCase28.feature`, `rialtoB2A(CASS)TestCase29.feature`, `rialtoB2A(CASS)TestCase35.feature`, `rialtoB2A(CASS)TestCase36.feature`, `rialtoB2A(CASS)TestCase37.feature`

**Affected Scenarios:**
- User perform CASS POST API (TC4, TC5, TC6, TC9, TC14-TC22)
- User perform CASS GET API (TC9, TC14-TC20, TC22)
- Verify created Rialto order and capture shared identifiers (TC23)
- Verify original full-page order state in MediaHouse (TC23, TC24)
- Verify updated MediaHouse basket state (TC23, TC24, TC37)
- Verify reverted MediaHouse basket state (TC23, TC24)
- RIALTO - Verify Rialto reflects the reverted full-page state (TC28, TC29)
- RIALTO - Verify updated Agency order after Rialto change (TC35)
- MEDIAHOUSE - Verify original magazine order state in MediaHouse (TC36)
- MEDIAHOUSE - Verify updated magazine order state in MediaHouse (TC36)
- MEDIAHOUSE - Verify original order state in MediaHouse (TC37)
- RIALTO - Verify Rialto reflects the updated state (TC37)

**Failure Pattern:**
`Mismatch on field: orderAdDetails.packageId expected [[SVD, AB, SVD, AB]] but found [[AB, SVD, AB, SVD]]`

**Evidence:**
- The same ordering drift appears in both write-time and read-back assertions for `packageId`, `productId`, `paCode`, `prodCode`, `placementId`, `issueDate`, and price-summary fields.
- TC15, TC23, TC24, TC36, and TC37 also show collapsed line counts, stale `statusFlags`, or incorrect basket totals, which is consistent with wrong line-to-line mapping after updates.
- Magazine and full-page flows fail with different field combinations but the values are often present in the wrong position or carried from an earlier state.

**Impact:** 45 failures

**Confidence:** High

### Transaction rollback on MediaHouse updates

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
- All affected update calls fail with the same rollback-only payload and return a non-200 response.
- The rollback errors are isolated to MediaHouse update/revert flows, not the initial setup or read-only verification steps.
- The error payload consistently reports CAI version `8.8.x-CI.87-r3a178be8`.

**Impact:** 7 failures

**Confidence:** High

### Internal server error on POST

**Affected Features:**
- `rialtoB2A(CASS)TestCase14.feature`
- `rialtoB2A(CASS)TestCase21.feature`

**Affected Scenarios:**
- User perform CASS POST API (TC14)
- User perform CASS POST API (TC21)

**Failure Pattern:**
`{"errorCode":1,"message":null} expected [N200] but found [N500]`

**Evidence:**
- Both failures occur on the POST step before downstream verification starts.
- The payload has no business error detail, which suggests an unhandled server-side exception.

**Impact:** 2 failures

**Confidence:** Medium

### Path parameter misconfiguration

**Affected Features:**
- `rialtoB2A(CASS)TestCase24.feature`

**Affected Scenarios:**
- Verify Rialto reflects the reverted full-page state (TC24)

**Failure Pattern:**
`Redundant path parameters are: agencyPrisaId=8276. Undefined path parameters are: uuid.`

**Evidence:**
- The failing verification still passes `agencyPrisaId` where the endpoint expects `uuid`.
- The error is isolated to the final Rialto validation call in TC24.

**Impact:** 1 failure

**Confidence:** High

### Integration ID mismatch

**Affected Features:**
- `rialtoB2A(CASS)TestCase35.feature`

**Affected Scenarios:**
- MEDIAHOUSE - Verify updated magazine order state in MediaHouse (TC35)

**Failure Pattern:**
`INTEGRATION MISMATCH: MH basket ID (orBoxid) [8286] does not match Agency Prisa ID [8287]`

**Evidence:**
- The MediaHouse basket ID differs from the Agency Prisa ID by one in the verification step.
- This appears only in the TC35 MediaHouse verification, so it may be a wrong-record lookup or synchronization issue.

**Impact:** 1 failure

**Confidence:** Medium
