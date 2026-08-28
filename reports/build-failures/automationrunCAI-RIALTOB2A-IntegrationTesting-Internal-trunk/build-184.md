# Build Failure Report

## Build Summary

| Field | Value |
|---|---|
| **Build** | [184](https://crossadv.atex.com/jenkins/job/automationrunCAI-RIALTOB2A-IntegrationTesting-Internal-trunk/184/) |
| **Job** | automationrunCAI-RIALTOB2A-IntegrationTesting-Internal-trunk |
| **Date** | 2026-08-28 21:03:11 UTC |
| **Status** | UNSTABLE |
| **Duration** | ~94 min |
| **Observed CAI Version** | 8.8.x-CI.87-r3a178be8 |

**Total Tests:** 514 | **Passed:** 458 | **Failed:** 56 | **Skipped:** 0 | **Pass Rate:** 89.1%

---

## Failing Tests / Steps

### Order field/state mismatch — 45 failures across 20 TCs

- **Affected TCs:** TC4, TC5, TC6, TC9, TC14-TC24, TC28, TC29, TC35, TC36, TC37
- **Failing steps:** `User perform CASS POST API`, `User perform CASS GET API`, MediaHouse basket-state checks, and Rialto state verification steps
- **Sample evidence:**
  - `Mismatch on field: orderAdDetails.packageId expected [[SVD, AB, SVD, AB]] but found [[AB, SVD, AB, SVD]]`
  - `Mismatch on field: orders[0].printDetails.paCode expected [[SVDTI, SVDTI, AB, AB]] but found [[AB, SVDTI, AB, SVDTI]]`
  - `Mismatch on field: orderHeader.statusFlags expected [[PRELIMINARY]] but found [[]]`

### Transaction rollback on MediaHouse updates — 7 failures across 4 TCs

- **Affected TCs:** TC22, TC23, TC24, TC37
- **Failing steps:** `User perform CASS POST API`, `Update two MediaHouse order lines to uppslag`, `Revert two MediaHouse order lines to full page`, `MEDIAHOUSE - Update MediaHouse order head line to change date`
- **Error:** `Transaction rolled back because it has been marked as rollback-only ... expected [N200] but found [N400]`

### Internal server error on POST — 2 failures across 2 TCs

- **Affected TCs:** TC14, TC21
- **Failing step:** `User perform CASS POST API`
- **Error:** `{"errorCode":1,"message":null} expected [N200] but found [N500]`

### Path parameter misconfiguration — 1 failure

- **Affected TC:** TC24
- **Failing step:** `Verify Rialto reflects the reverted full-page state`
- **Error:** `Redundant path parameters are: agencyPrisaId=8276. Undefined path parameters are: uuid.`

### Integration ID mismatch — 1 failure

- **Affected TC:** TC35
- **Failing step:** `MEDIAHOUSE - Verify updated magazine order state in MediaHouse`
- **Error:** `MH basket ID (orBoxid) [8286] does not match Agency Prisa ID [8287]`
