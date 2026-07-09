# Jenkins Build Failure Report

## Build Summary

Build: `automationrunCAI-RIALTOB2A-IntegrationTesting-Internal-trunk` #133
Date: 2026-07-09 21:03 UTC
Status: UNSTABLE
Total Tests: 513
Passed: 427
Failed: 86
Pass Rate: 83.2%

---

## Failing Tests

### Root Cause 1 — discountType Not Propagated from Rialto (33 failures)

**Pattern:** `orders[0].printDetails.discountType expected [[RIALTO]] but found [[null]]`

| Test Case | Step |
|---|---|
| CASS TC3 change Size | User perform CASS GET API |
| CASS TC4 Change Placement | User perform CASS GET API |
| CASS TC5 change to Uppslag/Spread/Panorama | User perform CASS GET API |
| CASS TC9 change size from Rialto | User perform CASS GET API (×2) |
| CASS TC11 change to UPPSLAG from Rialto | User perform CASS GET API |
| CASS TC14 change Product, Size, Placement & Date from Rialto | User perform CASS GET API (×2) |
| CASS TC15 2 products change date MH on head order line | User perform CASS GET API (×2) |
| CASS TC22 in MH change from Full page to uppslag | User perform CASS GET API (×3) |
| CASS TC23 in MH change from Full page to uppslag - two orderlines change | Verify original/updated/reverted MH basket state |
| CASS TC24 in MH change from uppslag to Full page | Verify original/updated/reverted MH basket state |
| CASS TC26 Basic order for magazines | Verify reverted MediaHouse basket state |
| CASS TC27 Magazine (change date) | MEDIAHOUSE - Verify original full-page order state |
| CASS TC28 Magazine (change size) | MEDIAHOUSE - Verify original full-page order state |
| CASS TC30 Magazine (change Date & Size) | MEDIAHOUSE - Verify original full-page order state |
| CASS TC31 Magazine (change Date, Size & Placement) | MEDIAHOUSE - Verify original full-page order state |
| CASS TC32 Magazine (change date from Rialto) | MEDIAHOUSE - Verify original/updated magazine order state |
| CASS TC33 Magazine (change size from Rialto) | MEDIAHOUSE - Verify original/updated magazine order state |
| CASS TC34 Magazine (change to UPPSLAG from Rialto) | MEDIAHOUSE - Verify original/updated magazine order state |
| CASS TC35 Magazine (change Date Size & Placement from Rialto) | MEDIAHOUSE - Verify original magazine order state |
| CASS TC36 Magazine (change Product Size Placement & Date from Rialto) | MEDIAHOUSE - Verify original/updated magazine order state |

---

### Root Cause 2 — MediaHouse Order Line Retrieval Failure (11 failures)

**Pattern:** `Index 13 out of bounds for length 13` / `No MH odIds found in TestContext`

| Test Case | Step |
|---|---|
| CASS TC16 2 products change date on non-head order line from MH | CASS GET API / CASS POST API |
| CASS TC17 2 products change size on head order line from MH | CASS GET API / CASS POST API |
| CASS TC18 2 products change size on non-head order line from MH | CASS GET API / CASS POST API |
| CASS TC19 2 products change placement on head order from MH | CASS GET API / CASS POST API |
| CASS TC20 2 products change placement order for non head from MH | CASS GET API / CASS POST API |
| CASS TC29 Magazine (change to Uppslag/Spread/Panorama) | MEDIAHOUSE - Update two MH order lines to uppslag |

---

### Root Cause 3 — Pricing / Financial Calculation Discrepancy (16 failures)

**Pattern:** Mismatches in `totalInclVat`, `commission`, `netAmount`, `discountAmount`, `orderbasketSum`, `vat`

| Test Case | Step |
|---|---|
| CASS TC3 change Size | User perform CASS GET API |
| CASS TC5 change to Uppslag/Spread/Panorama | User perform CASS GET API / CASS POST API |
| CASS TC9 change size from Rialto | User perform CASS POST API |
| CASS TC11 change to UPPSLAG from Rialto | User perform CASS GET API |
| CASS TC15 2 products change date MH on head order line | User perform CASS POST API |
| CASS TC27 Magazine (change date) | RIALTO - Verify created Rialto order |
| CASS TC28 Magazine (change size) | RIALTO - Verify created Rialto order / Verify updated MH state / Verify reverted state |
| CASS TC30 Magazine (change Date & Size) | RIALTO - Verify reverted full-page state |
| CASS TC31 Magazine (change Date, Size & Placement) | MEDIAHOUSE - Verify updated MH state / RIALTO - Verify reverted state |
| CASS TC35 Magazine (change Date Size & Placement from Rialto) | RIALTO - Verify updated Agency order |
| CASS TC37 2 Products Magazine - changes the size in MH | MEDIAHOUSE - Verify original/updated MH state |

---

### Root Cause 4 — statusFlags PRELIMINARY Not Set (5 failures)

**Pattern:** `orderHeader.statusFlags expected [[PRELIMINARY]] but found [[]]`

| Test Case | Step |
|---|---|
| CASS TC1 and TC2 | User perform CASS POST API |
| CASS TC3 change Size | User perform CASS POST API |
| CASS TC4 Change Placement | User perform CASS POST API |
| CASS TC6 change to changes the date and the size on the order line | User perform CASS POST API |
| CASS TC27 Magazine (change date) | RIALTO - Verify reverted full-page state |

---

### Root Cause 5 — Order Detail Field Value / Ordering Mismatch (15 failures)

**Pattern:** Wrong values or order in `packageId`, `placementId`, `moduleCode`, `issueDate`, `paCode`; also integration basket ID mismatch and path parameter errors

| Test Case | Error Summary |
|---|---|
| CASS TC15 2 products change date MH on head order line | discountAmount / commissionAmount ordering wrong |
| CASS TC16–TC20 (×5 POST steps) | packageId / placementId / moduleCode values in wrong order |
| CASS TC22 in MH change from Full page to uppslag | packageId array order mismatch in POST |
| CASS TC24 in MH change from uppslag to Full page | placementId expected TEXT found UPPSLAG; Rialto state mismatch |
| CASS TC27 Magazine (change date) | issueDate expected 2026-08-19 found 2026-08-26 |
| CASS TC29 Magazine (change to Uppslag/Spread/Panorama) | Undefined path param `agencyPrisaId`; cascading null context |
| CASS TC35 Magazine (change Date Size & Placement from Rialto) | INTEGRATION MISMATCH: MH basket orBoxid [6149] ≠ Agency Prisa ID [6150] |
