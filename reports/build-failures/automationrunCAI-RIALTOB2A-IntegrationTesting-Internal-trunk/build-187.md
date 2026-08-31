# Build Failure Report

## Build Summary

| Field | Value |
|---|---|
| **Build** | [187](https://crossadv.atex.com/jenkins/job/automationrunCAI-RIALTOB2A-IntegrationTesting-Internal-trunk/187/) |
| **Job** | automationrunCAI-RIALTOB2A-IntegrationTesting-Internal-trunk |
| **Date** | 2026-08-31 21:03:11 UTC |
| **Status** | UNSTABLE |
| **Duration** | ~94 min |

**Total Tests:** 514 | **Passed:** 461 | **Failed:** 53 | **Skipped:** 0 | **Pass Rate:** 89.7%

---

## Failing Tests / Steps

### Array ordering mismatch in multi-product order fields — 62 failures across 13 TCs

- **Affected TCs:** TC5, TC14, TC16, TC17, TC18, TC19, TC20, TC21, TC22, TC23, TC24, TC35, TC37
- **Failing steps:** `User perform CASS POST API`, `User perform CASS GET API`, `Verify created Rialto order and capture shared identifiers`, `Verify*MediaHouse*`, `RIALTO*Verify*`
- **Sample evidence:**
  - `Mismatch on field: orderAdDetails.packageId expected [[SVD, AB]] but found [[AB, SVD]]`
  - `Mismatch on field: orders[0].printDetails.paCode expected [[SVDTI, AB]] but found [[AB, SVDTI]]`
  - `Mismatch on field: orderAdDetails.placementId expected [[TEXT, SIDAN3]] but found [[SIDAN3, TEXT]]`

### Transaction rollback on MediaHouse update/revert — 16 failures across 5 TCs

- **Affected TCs:** TC14, TC22, TC23, TC24, TC37
- **Failing steps:** `User perform CASS POST API`, `Update two MediaHouse order lines to uppslag`, `Revert two MediaHouse order lines to full page`, `MEDIAHOUSE - Update MediaHouse order head line to change date`
- **Error:** `Transaction rolled back because it has been marked as rollback-only`

### Pricing / Discount value mismatch — 14 failures across 5 TCs

- **Affected TCs:** TC6, TC9, TC15, TC36, TC37
- **Failing steps:** `User perform CASS POST API`, `User perform CASS GET API`, `MEDIAHOUSE - Verify original order state in MediaHouse`
- **Sample evidence:**
  - `Mismatch on field: discountAmount expected [0.0] but found [38197.97]`
  - `Mismatch on field: orderBasketPriceSummary.orderDiscount expected [3600.00] but found [4800.00]`
  - `Mismatch on field: orders[0].printDetails.netAmount expected [[128531.37, 165799.0]] but found [[128531.37, 158000.0]]`

### Missing statusFlags [PRELIMINARY] — 6 failures across 3 TCs

- **Affected TCs:** TC4, TC28, TC29
- **Failing steps:** `User perform CASS POST API`, `RIALTO - Verify Rialto reflects the reverted full-page state`
- **Error:** `Mismatch on field: orderHeader.statusFlags expected [[PRELIMINARY]] but found [[]]`

### Integration ID mismatch / undefined path parameters — 4 failures across 2 TCs

- **Affected TCs:** TC24, TC35
- **Failing steps:** `Verify Rialto reflects the reverted full-page state`, `MEDIAHOUSE - Verify updated magazine order state in MediaHouse`
- **Error:** `Redundant path parameters are: agencyPrisaId=8392. Undefined path parameters are: uuid` and `INTEGRATION MISMATCH: MH basket ID (orBoxid) [8405] does not match Agency Prisa ID [8406]`

### HTTP response code mismatch — 2 failures across 1 TC

- **Affected TCs:** TC21
- **Failing step:** `User perform CASS POST API`
- **Error:** `expected [N200] but found [N202]`
