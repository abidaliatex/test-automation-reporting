# Build 162 — Root Cause Analysis

**Report:** [build-162.md](../../reports/build-failures/automationrunCAI-RIALTOB2A-IntegrationTesting-Internal-trunk/build-162.md)
**Job:** automationrunCAI-RIALTOB2A-IntegrationTesting-Internal-trunk
**Build:** 162 | **Date:** 2026-08-05 | **CAI Version:** 8.8.x-CI.47-r5943e353

---

## Build Summary

Build: 162
Total Tests: 514
Passed: 458
Failed: 56
Pass Rate: 89.1%

---

## Root Cause Groups

---

## RC-1: Unexpected Rialto Discount Applied — Discount Not Being Cleared on B2A Sync

**Affected Features:**
- CASS TC1 and TC2
- CASS TC3 change Size
- CASS TC4 Change Placement
- CASS TC5 change to Uppslag/Spread/Panorama
- CASS TC6 change to date and size on the order line
- CASS TC9 change size from Rialto

**Affected Scenarios:**
- User perform CASS POST API (TC1 and TC2)
- User perform CASS POST API (TC3 change Size)
- User perform CASS GET API (TC4 Change Placement)
- User perform CASS POST API (TC4 Change Placement)
- User perform CASS GET API (TC5 change to Uppslag/Spread/Panorama)
- User perform CASS POST API (TC5 change to Uppslag/Spread/Panorama)
- User perform CASS POST API (TC6 change date and size)
- User perform CASS POST API (TC9 change size from Rialto)
- User perform CASS GET API (TC9 change size from Rialto)

**Failure Pattern:**
```
discountAmount expected [0.0] but found [63660.63]
orderHeader.statusFlags expected [[PRELIMINARY]] but found [[]]
discountType expected [NONE] but found [RIALTO]
```

**Evidence:**
- TC1: `discountAmount expected [0.0] found [63660.63]`, `statusFlags expected [PRELIMINARY] found []`
- TC4 GET: `discountType expected [NONE] found [RIALTO]`, commission expected [7750.00] found [12500.00]
- TC5 POST: `discountAmount expected [0.0] found [63660.63]`, `placementId expected [UPPSLAG] found [TEXT]`
- TC9 GET: `discountType expected [NONE] found [RIALTO]`, `depth expected [184] found [372]`

**Impact:** ~18 failures

**Confidence:** High

---

## RC-2: Magazine Order Discount Not Reset After Revert/Change (B2A Sync)

**Affected Features:**
- CASS TC26 Basic order for magazines
- CASS TC27 Magazine (change date)
- CASS TC28 Magazine (change size)
- CASS TC30 Magazine (change Date & Size)
- CASS TC31 Magazine (change Date, Size & Placement)
- CASS TC32 Magazine (change date from Rialto)
- CASS TC33 Magazine (change size from Rialto)
- CASS TC34 Magazine (change to UPPSLAG from Rialto)
- CASS TC35 Magazine (change Date Size & Placement from Rialto)
- CASS TC36 Magazine (change Product Size Placement & Date from Rialto)
- CASS TC37 - 2 Products Magazine - changes the size in MH

**Affected Scenarios:**
- Verify reverted MediaHouse basket state (TC26)
- MEDIAHOUSE - Verify updated MediaHouse basket state (TC27) — discountType expected [RIALTO] found [NONE]
- MEDIAHOUSE - Verify updated MediaHouse basket state (TC28)
- RIALTO - Verify Rialto reflects the reverted full-page state (TC28, TC30, TC31)
- MEDIAHOUSE - Verify original full-page order state in MediaHouse (TC31)
- MEDIAHOUSE - Verify updated MediaHouse basket state (TC31)
- MEDIAHOUSE - Verify updated magazine order state in MediaHouse (TC32, TC33, TC34, TC35, TC36)
- MEDIAHOUSE - Verify original magazine order state in MediaHouse (TC35, TC36)
- MEDIAHOUSE - Verify original order state in MediaHouse (TC37)
- MEDIAHOUSE - Verify updated MediaHouse basket state (TC37)

**Failure Pattern:**
```
orderBasketPriceSummary.orderDiscount expected [0.00] found [3600.00/4000.00/4800.00/8800.00]
orderBasketPriceSummary.netPrice expected [6000.00] found [2400.00/1200.00/1000.00]
discountType expected [RIALTO] found [NONE]
commission / totalInclVat / orderbasketSum mismatches
```

**Evidence:**
- TC26: `orderDiscount expected [0.00] found [3600.00]`, `netPrice expected [6000.00] found [2400.00]`
- TC27: `discountType expected [RIALTO] found [NONE]`
- TC32: `orderDiscount expected [0.00] found [3600.00]`, `netPrice expected [6000.00] found [2400.00]`
- TC34: `orderDiscount expected [0.00] found [8800.00]`, `netPrice expected [11000.00] found [2200.00]`
- TC37: ordering of paCode/plaCode/prodCode reversed (KOT vs ANA)

**Impact:** ~20 failures

**Confidence:** High

---

## RC-3: Floating-Point Precision Mismatch in Price Fields

**Affected Features:**
- CASS TC11 change to UPPSLAG from Rialto
- CASS TC14 change Product, Size, Placement & Date from Rialto
- CASS TC15 2 products change date MH on head order line
- CASS TC21 2 products change from draft to reserved
- CASS TC23 in MH change from Full page to uppslag
- CASS TC24 in MH change from uppslag to Full page

**Affected Scenarios:**
- User perform CASS POST API (TC11) — priceNetExComm
- User perform CASS POST API (TC14, x2) — priceNet, priceNetExComm
- User perform CASS POST API (TC15) — priceNetExComm
- User perform CASS POST API (TC21, x2) — priceNet, priceNetExComm
- Verify created Rialto order and capture shared identifiers (TC23, TC24)

**Failure Pattern:**
```
priceNetExComm expected [66451.59999999998] found [66451.6]
priceNet expected [36958.049999999996] found [36958.05]
```

**Evidence:**
- TC11 POST: `priceNetExComm expected [66451.59999999998] found [66451.6]`
- TC14 POST: `priceNet expected [36958.049999999996] found [36958.05]`
- TC21 POST: `priceNet expected [32131.849999999988] found [32131.85]`

**Impact:** ~8 failures

**Confidence:** High

---

## RC-4: Transaction Rollback — 500 Internal Server Error on CASS POST

**Affected Features:**
- CASS TC18 2 products change size on not registered as head order line from MH
- CASS TC23 in MH change from Full page to uppslag - two orderlines change

**Affected Scenarios:**
- User perform CASS POST API (TC18)
- Revert two MediaHouse order lines to full page (TC23)

**Failure Pattern:**
```
500: "Transaction rolled back because it has been marked as rollback-only"
expected [N200] but found [N400]
caiVersion: 8.8.x-CI.47-r5943e353
```

**Evidence:**
- TC18: `500 Transaction rolled back because it has been marked as rollback-only` at 2026-08-05 23:28:13
- TC23: Same error at 2026-08-05 23:38:44

**Impact:** 2 failures (plus cascading downstream steps)

**Confidence:** High

---

## RC-5: Order Line Ordering / Sorting Mismatch in MH Basket Response

**Affected Features:**
- CASS TC15 2 products change date MH on head order line
- CASS TC23 in MH change from Full page to uppslag - two orderlines change
- CASS TC24 in MH change from uppslag to Full page
- CASS TC37 - 2 Products Magazine - changes the size in MH

**Affected Scenarios:**
- User perform CASS POST API (TC15) — packageId/productId/issueDate order reversed
- Verify updated MediaHouse basket state (TC23) — paCode/plaCode/prodCode/issueDate ordering mismatch
- Verify reverted MediaHouse basket state (TC23, TC24)
- Revert two MediaHouse order lines to full page (TC24) — placementId TEXT vs UPPSLAG, issueDate wrong
- MEDIAHOUSE - Verify updated MediaHouse basket state (TC37) — paCode/plaCode/prodCode reversed

**Failure Pattern:**
```
paCode expected [[SVDTI, AB, ...]] found [[AB, AB, ...]]
packageId expected [[AB, SVD]] found [[SVD, AB]]
issueDate expected [[2026-07-01, 2026-07-21]] found [[2026-07-01, 2026-07-01]]
```

**Evidence:**
- TC15 POST: `packageId expected [[AB, SVD]] found [[SVD, AB]]`, issueDate mismatch
- TC23: `paCode expected [[SVDTI, SVDTI, AB, ...]] found [[AB, AB, AB, ...]]`
- TC37: `paCode expected [[ANA, KOT]] found [[KOT, ANA]]`

**Impact:** ~6 failures

**Confidence:** Medium

---

## RC-6: Integration ID Mismatch / Path Parameter Error

**Affected Features:**
- CASS TC35 Magazine (change Date Size & Placement from Rialto)
- CASS TC24 in MH change from uppslag to Full page

**Affected Scenarios:**
- MEDIAHOUSE - Verify updated magazine order state in MediaHouse (TC35)
- Verify Rialto reflects the reverted full-page state (TC24)

**Failure Pattern:**
```
INTEGRATION MISMATCH: MH basket ID (orBoxid) [7321] does not match Agency Prisa ID [7322]
Redundant path parameters: agencyPrisaId=7311. Undefined path parameters: uuid
```

**Evidence:**
- TC35: `MH basket ID [7321] does not match Agency Prisa ID [7322]`
- TC24: `Path parameters were not correctly defined. Redundant: agencyPrisaId=7311. Undefined: uuid`

**Impact:** 2 failures

**Confidence:** Medium

---

## Summary

| Root Cause | Impact | Confidence |
|---|---|---|
| RC-1: Rialto discount not cleared on B2A sync | ~18 | High |
| RC-2: Magazine discount not reset after revert/change | ~20 | High |
| RC-3: Floating-point precision mismatch | ~8 | High |
| RC-4: 500 Transaction rollback on CASS POST | 2+ | High |
| RC-5: Order line sorting/ordering mismatch | ~6 | Medium |
| RC-6: Integration ID / path parameter mismatch | 2 | Medium |

## Recommended Fix

- **RC-1/RC-2:** Investigate B2A discount-sync logic for both newspaper and magazine orders — discount fields are not being cleared/reset when order state changes from Rialto back to a neutral state.
- **RC-3:** Test assertions may need rounding tolerance, or the server-side calculation should use consistent rounding.
- **RC-4:** Investigate the rollback-only transaction in caiVersion 8.8.x-CI.47-r5943e353 — possibly a constraint violation or concurrency issue when changing size on non-head order lines.
- **RC-5:** Order-line sort order in MH basket response may have changed — check if API response ordering has been altered or if test data assumptions are stale.
- **RC-6:** Test step for TC24 revert is passing wrong path parameter (`agencyPrisaId` instead of `uuid`); TC35 basket ID not being propagated correctly between steps.

## Prevention

- Add assertion tolerance for floating-point price fields.
- Add integration tests that verify discount fields are cleared after order revert operations.
- Add path-parameter validation in test framework to catch undefined params early.
