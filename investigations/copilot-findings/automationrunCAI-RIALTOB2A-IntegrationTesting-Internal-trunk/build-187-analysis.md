# Build 187 — Investigation Analysis

**Source report:** [build-187.md](../../../reports/build-failures/automationrunCAI-RIALTOB2A-IntegrationTesting-Internal-trunk/build-187.md)

---

## Build Summary

Build: 187
Total Tests: 514
Passed: 461
Failed: 53
Pass Rate: 89.7%

---

## Root Cause Groups

### Array ordering mismatch in multi-product order fields

**Affected Features:**
- `rialtoB2A(CASS)TestCase5.feature`
- `rialtoB2A(CASS)TestCase14.feature`
- `rialtoB2A(CASS)TestCase16.feature`
- `rialtoB2A(CASS)TestCase17.feature`
- `rialtoB2A(CASS)TestCase18.feature`
- `rialtoB2A(CASS)TestCase19.feature`
- `rialtoB2A(CASS)TestCase20.feature`
- `rialtoB2A(CASS)TestCase21.feature`
- `rialtoB2A(CASS)TestCase22.feature`
- `rialtoB2A(CASS)TestCase23.feature`
- `rialtoB2A(CASS)TestCase24.feature`
- `rialtoB2A(CASS)TestCase35.feature`
- `rialtoB2A(CASS)TestCase37.feature`

**Affected Scenarios:**
- User perform CASS POST API (TC5, TC14, TC16, TC17, TC18, TC19, TC20, TC21)
- User perform CASS GET API (TC14, TC16, TC17, TC18, TC19, TC20, TC22)
- Verify created Rialto order and capture shared identifiers (TC23)
- Verify original full-page order state in MediaHouse (TC23, TC24)
- Verify updated MediaHouse basket state (TC23, TC24, TC37)
- Verify reverted MediaHouse basket state (TC23, TC24)
- RIALTO - Verify updated Agency order after Rialto change (TC35)
- MEDIAHOUSE - Verify updated MediaHouse basket state (TC37)
- RIALTO - Verify Rialto reflects the updated state (TC37)

**Failure Pattern:**
`Mismatch on field: orderAdDetails.packageId expected [[SVD, AB]] but found [[AB, SVD]]`

**Evidence:**
- `Mismatch on field: orderAdDetails.packageId expected [[SVD, AB, SVD, AB]] but found [[AB, SVD, AB, SVD]]`
- `Mismatch on field: orders[0].printDetails.paCode expected [[SVDTI, AB]] but found [[AB, SVDTI]]`
- `Mismatch on field: orderAdDetails.placementId expected [[TEXT, SIDAN3]] but found [[SIDAN3, TEXT]]`

**Impact:** 62 failures

**Confidence:** High

---

### Transaction rollback on MediaHouse update/revert

**Affected Features:**
- `rialtoB2A(CASS)TestCase14.feature`
- `rialtoB2A(CASS)TestCase22.feature`
- `rialtoB2A(CASS)TestCase23.feature`
- `rialtoB2A(CASS)TestCase24.feature`
- `rialtoB2A(CASS)TestCase37.feature`

**Affected Scenarios:**
- User perform CASS POST API (TC14, TC22)
- Update two MediaHouse order lines to uppslag (TC23, TC24)
- Revert two MediaHouse order lines to full page (TC23, TC24)
- MEDIAHOUSE - Update MediaHouse order head line to change date (TC37)

**Failure Pattern:**
`500 Transaction rolled back because it has been marked as rollback-only`

**Evidence:**
- `500 : {"errorCode":null,"errorMessage":"Transaction rolled back because it has been marked as rollback-only","detailErrorMessage":"Transaction rolled back because it has been marked as rollback-only"}`
- Affects both update and revert steps — possibly shared transactional boundary or dirty state left from prior step.

**Impact:** 16 failures

**Confidence:** High

---

### Pricing / Discount value mismatch

**Affected Features:**
- `rialtoB2A(CASS)TestCase6.feature`
- `rialtoB2A(CASS)TestCase9.feature`
- `rialtoB2A(CASS)TestCase15.feature`
- `rialtoB2A(CASS)TestCase36.feature`
- `rialtoB2A(CASS)TestCase37.feature`

**Affected Scenarios:**
- User perform CASS POST API (TC6, TC9)
- User perform CASS GET API (TC9, TC15)
- MEDIAHOUSE - Verify original magazine order state in MediaHouse (TC36)
- MEDIAHOUSE - Verify original order state in MediaHouse (TC37)

**Failure Pattern:**
`Mismatch on field: discountAmount expected [0.0] but found [38197.97]`

**Evidence:**
- `Mismatch on field: discountAmount expected [0.0] but found [38197.97]` (TC9)
- `Mismatch on field: orderBasketPriceSummary.orderDiscount expected [3600.00] but found [4800.00]` (TC36)
- `Mismatch on field: orders[0].printDetails.netAmount expected [[128531.37, 165799.0]] but found [[128531.37, 158000.0]]` (TC15)
- `Mismatch on field: orderBasketPriceSummary.totalInclVat expected [7368.00] but found [5814.00]` (TC37)

**Impact:** 14 failures

**Confidence:** High

---

### Missing statusFlags [PRELIMINARY]

**Affected Features:**
- `rialtoB2A(CASS)TestCase4.feature`
- `rialtoB2A(CASS)TestCase28.feature`
- `rialtoB2A(CASS)TestCase29.feature`

**Affected Scenarios:**
- User perform CASS POST API (TC4)
- RIALTO - Verify Rialto reflects the reverted full-page state (TC28, TC29)

**Failure Pattern:**
`Mismatch on field: orderHeader.statusFlags expected [[PRELIMINARY]] but found [[]]`

**Evidence:**
- `orderHeader.statusFlags expected [[PRELIMINARY]] but found [[]]` across all three TCs.
- Possibly a Rialto order status propagation regression — PRELIMINARY flag not being set or returned after change.

**Impact:** 6 failures

**Confidence:** High

---

### Integration ID mismatch / undefined path parameters

**Affected Features:**
- `rialtoB2A(CASS)TestCase24.feature`
- `rialtoB2A(CASS)TestCase35.feature`

**Affected Scenarios:**
- Verify Rialto reflects the reverted full-page state (TC24)
- MEDIAHOUSE - Verify updated magazine order state in MediaHouse (TC35)

**Failure Pattern:**
`Redundant path parameters are: agencyPrisaId=8392. Undefined path parameters are: uuid`

**Evidence:**
- `Path parameters were not correctly defined. Redundant path parameters are: agencyPrisaId=8392. Undefined path parameters are: uuid.` (TC24)
- `INTEGRATION MISMATCH: MH basket ID (orBoxid) [8405] does not match Agency Prisa ID [8406]` (TC35)

**Impact:** 4 failures

**Confidence:** High

---

### HTTP response code mismatch (N200 vs N202)

**Affected Features:**
- `rialtoB2A(CASS)TestCase21.feature`

**Affected Scenarios:**
- User perform CASS POST API (TC21)

**Failure Pattern:**
`expected [N200] but found [N202]`

**Evidence:**
- `expected [N200] but found [N202]` — server is returning HTTP 202 Accepted instead of 200 OK for a reservation step.

**Impact:** 2 failures

**Confidence:** Medium
