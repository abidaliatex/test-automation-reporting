# Build Failure Report

## Build Summary

| Field         | Value |
|---------------|-------|
| **Build**     | [182](https://crossadv.atex.com/jenkins/job/automationrunCAI-RIALTOB2A-IntegrationTesting-Internal-trunk/182/) |
| **Job**       | automationrunCAI-RIALTOB2A-IntegrationTesting-Internal-trunk |
| **Date**      | 2026-08-26 21:03:16 UTC |
| **Status**    | UNSTABLE |
| **Duration**  | ~94 min |
| **CAI Version** | 8.8.x-CI.80-rd84a301f |

**Total Tests:** 514 | **Passed:** 456 | **Failed:** 58 | **Skipped:** 0 | **Pass Rate:** 88.7%

---

## Failing Tests

### Field Value Mismatch — 86 failures across 19 TCs

| TC | Feature | Failing Steps |
|----|---------|---------------|
| TC4  | rialtoB2A(CASS TC4 Change Placement) | User perform CASS POST API - #1.1 |
| TC5  | rialtoB2A(CASS TC5 change to Uppslag/Spread/Panorama) | User perform CASS POST API - #1.1 |
| TC6  | rialtoB2A(CASS TC6 change date and size on order line) | User perform CASS POST API - #1.1 |
| TC9  | rialtoB2A(CASS TC9 change size from Rialto) | POST API #1.1, GET API #1.1 |
| TC14 | rialtoB2A(CASS TC14 change Product, Size, Placement & Date from Rialto) | POST API #1.1, GET API #1.1 |
| TC15 | rialtoB2A(CASS TC15 2 products change date MH on head order line) | POST API #1.1, GET API #1.1 |
| TC16 | rialtoB2A(CASS TC16 2 products change date on non-head order line from MH) | POST API #1.1, GET API #1.1 |
| TC17 | rialtoB2A(CASS TC17 2 products change size on head order line from MH) | POST API #1.1, GET API #1.1 |
| TC18 | rialtoB2A(CASS TC18 2 products change size on non-head order line from MH) | POST API #1.1, GET API #1.1 |
| TC19 | rialtoB2A(CASS TC19 2 products change placement on head order from MH) | POST API #1.1, GET API #1.1 |
| TC20 | rialtoB2A(CASS TC20 2 products change placement order for non head from MH) | POST API #1.1, GET API #1.1 |
| TC22 | rialtoB2A(CASS TC22 in MH change from Full page to uppslag) | POST API #1.1, GET API #1.1 |
| TC23 | rialtoB2A(CASS TC23 in MH change from Full page to uppslag - two orderlines) | Verify original/updated/reverted MH basket - #1.1 |
| TC24 | rialtoB2A(CASS TC24 in MH change from uppslag to Full page) | Verify original/updated/reverted MH basket - #1.1 |
| TC28 | rialtoB2A(CASS TC28 Magazine change size) | RIALTO - Verify Rialto reverted state - #1.1 |
| TC29 | rialtoB2A(CASS TC29 Magazine change to Uppslag/Spread/Panorama) | RIALTO - Verify Rialto reverted state - #1.1 |
| TC35 | rialtoB2A(CASS TC35 Magazine change Date Size & Placement from Rialto) | RIALTO - Verify updated Agency order - #1.1 |
| TC36 | rialtoB2A(CASS TC36 Magazine change Product Size Placement & Date from Rialto) | MEDIAHOUSE - Verify original/updated MH order state - #1.1 |
| TC37 | rialtoB2A(CASS TC37 - 2 Products Magazine - changes size in MH) | MEDIAHOUSE verify original/updated, RIALTO verify updated state - #1.1 |

**Mismatched fields:** `orderAdDetails.packageId`, `orderAdDetails.productId`, `orderAdDetails.placementId`, `orderAdDetails.issueDate`, `orderAdDetails.materialId`, `orderAdDetails.depth`, `orders[0].printDetails.paCode`, `orders[0].printDetails.plaCode`, `orders[0].printDetails.prodCode`, `discountAmount`

**Sample errors:**
```
Mismatch on field: orderAdDetails.packageId expected [[SVD, AB, SVD, AB]] but found [[AB, SVD, AB, SVD]]
Mismatch on field: orderAdDetails.issueDate expected [[2026-12-01, 2026-12-21]] but found [[2026-12-01, 2026-12-01]]
```

---

### Transaction Rollback (N400) — 14 failures across 4 TCs

| TC | Feature | Failing Steps |
|----|---------|---------------|
| TC22 | rialtoB2A(CASS TC22 in MH change from Full page to uppslag) | User perform CASS POST API - #1.1 |
| TC23 | rialtoB2A(CASS TC23 in MH change from Full page to uppslag - two orderlines) | Update two MH order lines to uppslag - #1.1, Revert two MH order lines to full page - #1.1 |
| TC24 | rialtoB2A(CASS TC24 in MH change from uppslag to Full page) | Update two MH order lines - #1.1, Revert two MH order lines - #1.1 |
| TC37 | rialtoB2A(CASS TC37 - 2 Products Magazine - changes size in MH) | MEDIAHOUSE - Update MH order head line to change date - #1.1 |

**Error:**
```
500: Transaction rolled back because it has been marked as rollback-only
expected [N200] but found [N400]
```

---

### 500 Internal Server Error — 2 failures

| TC | Feature | Failing Steps |
|----|---------|---------------|
| TC14 | rialtoB2A(CASS TC14 change Product, Size, Placement & Date from Rialto) | User perform CASS POST API - #1.1 |

**Error:** `{"errorCode":1,"message":null} expected [N200] but found [N500]`

---

### Path Parameter Error — 2 failures

| TC | Feature | Failing Steps |
|----|---------|---------------|
| TC24 | rialtoB2A(CASS TC24 in MH change from uppslag to Full page) | Verify Rialto reflects reverted full-page state - #1.1 |

**Error:** `Path parameters were not correctly defined. Redundant path parameters: agencyPrisaId=8201. Undefined path parameters: uuid.`

---

### Integration ID Mismatch — 2 failures

| TC | Feature | Failing Steps |
|----|---------|---------------|
| TC35 | rialtoB2A(CASS TC35 Magazine change Date Size & Placement from Rialto) | MEDIAHOUSE - Verify updated magazine order state in MediaHouse - #1.1 |

**Error:** `INTEGRATION MISMATCH: MH basket ID (orBoxid) [8211] does not match Agency Prisa ID [8212] expected [8212] but found [8211]`
