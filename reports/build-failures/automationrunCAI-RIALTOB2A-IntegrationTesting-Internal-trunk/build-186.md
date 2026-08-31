# Build Failure Report

## Build Summary

| Field | Value |
|---|---|
| **Build** | [186](https://crossadv.atex.com/jenkins/job/automationrunCAI-RIALTOB2A-IntegrationTesting-Internal-trunk/186/) |
| **Job** | automationrunCAI-RIALTOB2A-IntegrationTesting-Internal-trunk |
| **Date** | 2026-08-30 21:03:10 UTC |
| **Status** | UNSTABLE |
| **Duration** | ~94 min |

**Total Tests:** 514 | **Passed:** 453 | **Failed:** 61 | **Skipped:** 0 | **Pass Rate:** 88.1%

---

## Failing Tests / Steps

### Order field/state mismatch after update flows — 46 failures across 22 TCs

- **Affected TCs:** TC4, TC5, TC6, TC9, TC14-TC24, TC28, TC29, TC32, TC33, TC35, TC36, TC37
- **Failing steps:** `User perform CASS POST API`, `User perform CASS GET API`, `Verify*MediaHouse*`, `RIALTO*Verify*`
- **Sample evidence:**
  - `Mismatch on field: orderAdDetails.packageId expected [[SVD, AB]] but found [[AB, SVD]]`
  - `Mismatch on field: orders[0].printDetails.paCode expected [[SVDTI, AB]] but found [[AB, SVDTI]]`
  - `Mismatch on field: orderHeader.statusFlags expected [[PRELIMINARY]] but found [[]]`

### Transaction rollback on MediaHouse updates — 7 failures across 4 TCs

- **Affected TCs:** TC22, TC23, TC24, TC37
- **Failing steps:** `User perform CASS POST API`, `Update two MediaHouse order lines to uppslag`, `Revert two MediaHouse order lines to full page`, `MEDIAHOUSE - Update MediaHouse order head line to change date`
- **Error:** `Transaction rolled back because it has been marked as rollback-only`

### Internal server error on POST — 2 failures across 2 TCs

- **Affected TCs:** TC14, TC21
- **Failing step:** `User perform CASS POST API`
- **Error:** `{"errorCode":1,"message":null} expected [N200] but found [N500]`

### Path parameter / basket ID propagation errors — 3 failures across 3 TCs

- **Affected TCs:** TC24, TC35, TC36
- **Failing steps:** `Verify Rialto reflects the reverted full-page state`, `MEDIAHOUSE - Verify original magazine order state in MediaHouse`
- **Error:** `Undefined path parameters are: uuid` and `Undefined path parameters are: mhBasketOrderId`

### Basket lookup and ID synchronization failures — 3 failures across 2 TCs

- **Affected TCs:** TC35, TC36
- **Failing steps:** `MEDIAHOUSE - User perform CASS POST API`, `MEDIAHOUSE - Verify updated magazine order state in MediaHouse`
- **Error:** `Basket not found for campaign` and `INTEGRATION MISMATCH: MH basket ID ... does not match Agency Prisa ID`
