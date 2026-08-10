# Investigation: Build 167 — Root Cause Analysis

**Source Report:** [build-167.md](../../reports/build-failures/automationrunCAI-RIALTOB2A-IntegrationTesting-Internal-trunk/build-167.md)
**Job:** automationrunCAI-RIALTOB2A-IntegrationTesting-Internal-trunk
**Date:** 2026-08-10
**CAI Version:** 8.8.x-CI.56-r14059a2a

---

## Build Summary

| Build | Total Tests | Passed | Failed | Pass Rate |
|---|---|---|---|---|
| 167 | 514 | 474 | 40 | 92.2% |

---

## Root Cause Groups

---

## 1. Unexpected Discount Applied on Magazine Orders

**Affected Features:**
- CASS Magazine scenarios (TC26, TC27, TC29, TC30, TC31, TC32, TC33, TC34, TC35, TC36, TC37)

**Affected Scenarios:**
- Verify reverted MediaHouse basket state (TC26)
- MEDIAHOUSE - Verify updated MediaHouse basket state (TC27)
- RIALTO - Verify Rialto reflects the reverted full-page state (TC27, TC29, TC30, TC31)
- MEDIAHOUSE - Verify updated MediaHouse basket state (TC29, TC31, TC37)
- MEDIAHOUSE - Verify updated magazine order state in MediaHouse (TC32, TC33, TC34, TC35, TC36)
- MEDIAHOUSE - Verify original magazine order state in MediaHouse (TC35, TC36)
- MEDIAHOUSE - Verify original order state in MediaHouse (TC37)
- RIALTO - Verify Rialto reflects the updated state (TC37)

**Failure Pattern:**
`orderDiscount` / `orderBasketPriceSummary.orderDiscount` expected `0.00` but found large positive values (e.g., 3600.00, 4000.00, 8800.00). `netPrice` and `commission` correspondingly deflated. `discountType` expected `[RIALTO]` but found `[NONE]` (TC27).

**Evidence:**
- TC26: `orderDiscount expected [0.00] but found [3600.00]`, `netPrice expected [6000.00] but found [2400.00]`
- TC27: `discountType expected [[RIALTO]] but found [[NONE]]`
- TC32: `orderDiscount expected [0.00] but found [3600.00]`, `netPrice expected [6000.00] but found [2400.00]`
- TC33: `orderDiscount expected [0.00] but found [4000.00]`, `netPrice expected [5000.00] but found [1000.00]`
- TC34: `orderDiscount expected [0.00] but found [8800.00]`, `netPrice expected [11000.00] but found [2200.00]`

**Impact:** 20+ failures across magazine TC26–TC37

**Confidence:** High

---

## 2. Commission Calculation Wrong After Size/Placement Change

**Affected Features:**
- CASS TC3, TC6, TC9, TC29, TC30, TC31, TC35, TC37

**Affected Scenarios:**
- User perform CASS POST API (TC3, TC4, TC5, TC6, TC9)
- MEDIAHOUSE - Verify updated MediaHouse basket state (TC29, TC31)
- RIALTO - Verify Rialto reflects the reverted full-page state (TC29, TC30, TC31)
- RIALTO - Verify Rialto reflects the updated state (TC37)
- RIALTO - Verify updated Agency order after Rialto change (TC35)

**Failure Pattern:**
`commissionAmount` and `priceNet` return wrong values after size/placement changes. `priceNet` is consistently lower than expected while `commissionAmount` is non-zero when zero is expected (or vice versa).

**Evidence:**
- TC3/TC6: `priceNet expected [115320.00] but found [111745.08]`
- TC9: `discountAmount expected [0.0] but found [38197.97]`, `priceNetExComm expected [115320.00] but found [77122.03]`
- TC29: `commissionAmount expected [[68.2]] but found [[341.0]]`, `priceNet expected [[10931.8]] but found [[10659.0]]`
- TC30: `commissionAmount expected [0.0] but found [186.0]`, `priceNet expected [[6000.0]] but found [[5814.0]]`
- TC31: `commissionAmount expected [0.0] but found [155.0]`, `priceNet expected [[5000.0]] but found [[4845.0]]`

**Impact:** ~14 failures

**Confidence:** High

---

## 3. Array/List Ordering Non-Determinism in Multi-Product Scenarios

**Affected Features:**
- CASS TC15, TC22, TC24, TC37

**Affected Scenarios:**
- User perform CASS GET API (TC15, TC22)
- User perform CASS POST API (TC15)
- Verify reverted MediaHouse basket state (TC24)
- MEDIAHOUSE - Verify updated MediaHouse basket state (TC37)

**Failure Pattern:**
Multi-product arrays (`paCode`, `prodCode`, `plaCode`, `issueDate`, `packageId`, `productId`) returned in a different order than expected. The elements are correct but sequence is non-deterministic.

**Evidence:**
- TC15: `paCode expected [[SVDTI, AB]] but found [[AB, SVDTI]]`; `issueDate expected [[2026-12-21, 2026-12-01]] but found [[2026-12-01, 2026-12-21]]`
- TC22: `plaCode expected [[TEXT, TEXT, TEXT, TEXT, TEXT, UPPSLAG]] but found [[UPPSLAG, TEXT, TEXT, TEXT, TEXT, TEXT]]`
- TC37: `paCode expected [[ANA, KOT]] but found [[KOT, ANA]]`; `plaCode expected [[TEXT, HALVLIGG]] but found [[HALVLIGG, TEXT]]`

**Impact:** 6 failures

**Confidence:** High

---

## 4. Transaction Rollback / HTTP 500 on Uppslag Change

**Affected Features:**
- CASS TC22

**Affected Scenarios:**
- User perform CASS POST API (TC22)

**Failure Pattern:**
`HTTP 500 — Transaction rolled back because it has been marked as rollback-only`. Expected N200 but got N400.

**Evidence:**
- `"errorMessage":"Transaction rolled back because it has been marked as rollback-only"`, `caiVersion: 8.8.x-CI.56-r14059a2a`, timestamp: 2026-08-10 23:36:53

**Impact:** 1 failure (possible upstream blocker for TC22 cascade)

**Confidence:** High

---

## 5. Incorrect statusFlags / PRELIMINARY Flag Unexpectedly Set or Missing

**Affected Features:**
- CASS TC4, TC27, TC30

**Affected Scenarios:**
- User perform CASS POST API (TC4)
- RIALTO - Verify Rialto reflects the reverted full-page state (TC27, TC30)

**Failure Pattern:**
`orderHeader.statusFlags` expected `[PRELIMINARY]` but found `[]` (TC4), or expected `[]` but found `[PRELIMINARY]` (TC27, TC30). Inconsistent flag setting after order changes.

**Evidence:**
- TC4: `statusFlags expected [[PRELIMINARY]] but found [[]]`
- TC27: `statusFlags expected [[]] but found [[PRELIMINARY]]`
- TC30: `statusFlags expected [[]] but found [[PRELIMINARY]]`

**Impact:** 3 failures

**Confidence:** High

---

## 6. Path Parameter / UUID Missing — API Configuration Issue

**Affected Features:**
- CASS TC24

**Affected Scenarios:**
- Verify Rialto reflects the reverted full-page state (TC24)

**Failure Pattern:**
`IllegalArgumentException: Path parameters were not correctly defined. Redundant path parameters are: agencyPrisaId=7547. Undefined path parameters are: uuid.`

**Evidence:**
- `agencyPrisaId=7547` used as path param but API endpoint now expects `uuid`; possibly a breaking API contract change.

**Impact:** 1 failure

**Confidence:** High

---

## 7. Basket ID Mismatch — MH/Agency Integration Sync Issue

**Affected Features:**
- CASS TC35

**Affected Scenarios:**
- MEDIAHOUSE - Verify updated magazine order state in MediaHouse (TC35)

**Failure Pattern:**
`INTEGRATION MISMATCH: MH basket ID (orBoxid) [7557] does not match Agency Prisa ID [7558]`

**Evidence:**
- MH basket orBoxid 7557 ≠ Agency Prisa ID 7558; IDs off by 1, possibly a race condition or ordering issue during basket creation.

**Impact:** 1 failure

**Confidence:** Medium

---

## Summary

| # | Root Cause | Failures | Confidence |
|---|---|---|---|
| 1 | Unexpected discount on magazine orders | ~20 | High |
| 2 | Wrong commission/priceNet after size/placement change | ~14 | High |
| 3 | Array ordering non-determinism (multi-product) | 6 | High |
| 4 | Transaction rollback HTTP 500 on uppslag change | 1 | High |
| 5 | statusFlags PRELIMINARY flag inconsistency | 3 | High |
| 6 | Path param / UUID missing in API call | 1 | High |
| 7 | Basket ID mismatch (MH vs Agency) | 1 | Medium |
