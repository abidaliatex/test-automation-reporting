# Build 176 — Root Cause Analysis

**Source Report:** [build-176.md](../../reports/build-failures/automationrunCAI-RIALTOB2A-IntegrationTesting-Internal-trunk/build-176.md)

---

## Build Summary

**Build:** 176
**Total Tests:** 514
**Passed:** 485
**Failed:** 29
**Pass Rate:** 94.4%

---

## Root Cause Groups

---

## 1. Print Detail Field Ordering Mismatch (paCode / plaCode / depth)

**Affected Features:**
- rialtoB2A CASS scenarios (newspaper & magazine GET validations)

**Affected Scenarios:**
- User perform CASS GET API — TC9 (depth mismatch)
- User perform CASS GET API — TC14 (paCode / plaCode mismatch)
- User perform CASS GET API — TC15 (paCode mismatch)
- User perform CASS GET API #1, #2, #3 — TC22 (paCode / netAmount mismatch)
- Verify updated MediaHouse basket state — TC23
- Verify reverted MediaHouse basket state — TC23
- Verify reverted MediaHouse basket state — TC24
- RIALTO - Verify Rialto reflects updated state — TC37 (placementId ordering)

**Failure Pattern:**
```
paCode expected [[AB, SVDTI, AB, AB]] but found [[AB, SVDTI, SVDTI, AB]]
paCode expected [[SVDTI, AB]] but found [[AB, SVDTI]]
placementId expected [[HALVLIGG, TEXT]] but found [[TEXT, HALVLIGG]]
depth expected [[184]] but found [[372]]
```

**Evidence:**
- TC14 GET: `orders[0].printDetails.paCode expected [[AB, SVDTI, AB, AB]] but found [[AB, SVDTI, SVDTI, AB]]`
- TC15 GET: `orders[0].printDetails.paCode expected [[SVDTI, AB]] but found [[AB, SVDTI]]`
- TC37 RIALTO: `orderAdDetails.placementId expected [[HALVLIGG, TEXT]] but found [[TEXT, HALVLIGG]]`
- TC9 GET: `orders[0].printDetails.depth expected [[184]] but found [[372]]`

**Impact:** ~10 failures

**Confidence:** High — consistent list-ordering reversal pattern across multiple TCs suggests a sort-order regression in the CASS GET response assembly or the B2A mapping layer.

---

## 2. Unexpected Non-Zero Discount Amount

**Affected Features:**
- Newspaper CASS POST (TC5, TC9)
- Magazine MEDIAHOUSE order validation (TC36, TC37)

**Affected Scenarios:**
- User perform CASS POST API — TC5 (change to Uppslag/Spread/Panorama)
- User perform CASS POST API — TC9 (change size from Rialto)
- MEDIAHOUSE - Verify original magazine order state — TC36
- MEDIAHOUSE - Verify updated magazine order state — TC36
- MEDIAHOUSE - Verify original order state — TC37
- MEDIAHOUSE - Verify updated MediaHouse basket state — TC37

**Failure Pattern:**
```
discountAmount expected [0.0] but found [63660.63]
discountAmount expected [0.0] but found [38197.97]
orderBasketPriceSummary.orderDiscount expected [3600.00] but found [4800.xx]
orderBasketPriceSummary.commission expected [234.40] but found [229.40]
```

**Evidence:**
- TC5: `discountAmount expected [0.0] but found [63660.63]`
- TC9: `discountAmount expected [0.0] but found [38197.97]`
- TC36: `orderDiscount expected [3600.00] but found [4800.xx]` and `expected [0.00] but found [4000.xx]`
- TC37: `totalInclVat expected [7368.00] but found [5813.xx]`

**Impact:** 6 failures

**Confidence:** High — discount/price values consistently differ, pointing to a pricing calculation regression in either the CASS engine or a discount-rule configuration change.

---

## 3. statusFlags Missing PRELIMINARY

**Affected Features:**
- Newspaper CASS POST (TC4)
- Magazine RIALTO verification (TC28, TC29)

**Affected Scenarios:**
- User perform CASS POST API — TC4 (Change Placement)
- RIALTO - Verify Rialto reflects the reverted full-page state — TC28 (Magazine change size)
- RIALTO - Verify Rialto reflects the reverted full-page state — TC29 (Magazine change to Uppslag/Spread/Panorama)

**Failure Pattern:**
```
orderHeader.statusFlags expected [[PRELIMINARY]] but found [[]]
```

**Evidence:**
- TC4: `orderHeader.statusFlags expected [[PRELIMINARY]] but found [[]]`
- TC28: `orderHeader.statusFlags expected [[PRELIMINARY]] but found [[]]`
- TC29: `orderHeader.statusFlags expected [[PRELIMINARY]] but found [[]]`

**Impact:** 3 failures

**Confidence:** High — all three scenarios expect PRELIMINARY flag after a change operation; empty array suggests the status transition logic is not firing for certain change types.

---

## 4. HTTP 500 on CASS POST (TC14)

**Affected Features:**
- rialtoB2A CASS TC14 — change Product, Size, Placement & Date from Rialto

**Affected Scenarios:**
- User perform CASS POST API — TC14

**Failure Pattern:**
```
{"errorCode":1,"message":null} expected [N200] but found [N500]
```

**Evidence:**
- TC14 POST: `{"errorCode":1,"message":null} expected [N200] but found [N500]`
- The downstream CASS GET for TC14 also fails with paCode mismatch, possibly caused by this POST failure leaving corrupted state.

**Impact:** 1 failure (plus cascading TC14 GET failure)

**Confidence:** High — server-side error; possibly a null-pointer or unhandled exception in the combined product+placement+date change code path.

---

## 5. Placement / Basket Sync Mismatches

**Affected Features:**
- Newspaper CASS POST ordering (TC19, TC20)
- Magazine Rialto–MH sync (TC24, TC31, TC35)

**Affected Scenarios:**
- User perform CASS POST API — TC19 (2 products change placement on head order from MH)
- User perform CASS POST API — TC20 (2 products change placement non-head from MH)
- Revert two MediaHouse order lines to full page — TC24
- Verify Rialto reflects the reverted full-page state — TC24 (redundant path param `agencyPrisaId`)
- RIALTO - Verify Rialto reflects the reverted full-page state — TC31 (`priceNet` mismatch)
- RIALTO - Verify updated Agency order after Rialto change — TC35 (`placementId` mismatch)
- MEDIAHOUSE - Verify updated magazine order state — TC35 (basket ID mismatch)

**Failure Pattern:**
```
orderAdDetails.packageId expected [[AB, SVD]] but found [[SVD, AB]]
orderAdDetails.placementId expected [[TEXT, SIDAN3]] but found [...]
Redundant path parameters: agencyPrisaId=7932
MH basket ID (orBoxid) [7942] does not match Agency Prisa ID [7943]
orderAdDetails.priceNet expected [[5000.0]] but found [[4845.0]]
```

**Evidence:**
- TC19: `packageId expected [[AB, SVD]] but found [[SVD, AB]]`
- TC35: `MH basket ID (orBoxid) [7942] does not match Agency Prisa ID [7943]`
- TC24: `Redundant path parameters: agencyPrisaId=7932`
- TC31: `priceNet expected [[5000.0]] but found [[4845.0]]`

**Impact:** 7 failures

**Confidence:** Medium — mix of ordering issues (possibly same root cause as Group 1), an off-by-one basket ID sync problem, and a stale/redundant parameter in the B2A request builder.

---

## 6. Price Format Mismatch (TC6)

**Affected Features:**
- Newspaper CASS TC6 — change date and size

**Affected Scenarios:**
- User perform CASS POST API — TC6

**Failure Pattern:**
```
orderHeader.priceNetExComm expected [115320.00] but found [115320.0]
```

**Evidence:**
- TC6: decimal scale difference — `115320.00` vs `115320.0`

**Impact:** 1 failure

**Confidence:** High — trivial serialisation/decimal-scale regression; value is numerically correct but formatted differently.

---

## Summary Table

| Group | Root Cause | Failures | Confidence |
|---|---|---|---|
| 1 | Print detail field ordering mismatch (paCode/plaCode/depth) | ~10 | High |
| 2 | Unexpected non-zero discount / price | 6 | High |
| 3 | statusFlags missing PRELIMINARY | 3 | High |
| 4 | HTTP 500 on CASS POST (TC14) | 1 | High |
| 5 | Placement / basket sync mismatches | 7 | Medium |
| 6 | Price decimal format mismatch (TC6) | 1 | High |

---

## Recommended Fix

- **Group 1:** Investigate sort order of collections returned by CASS GET / B2A mapping; check if a recent change altered the ordering of `printDetails` lists.
- **Group 2:** Review discount-rule configuration or pricing calculation changes deployed before this build; compare discount logic between passing and failing TCs.
- **Group 3:** Check the status-flag transition logic for change-type operations (placement, size, magazine uppslag); possibly a condition was added that skips the PRELIMINARY assignment.
- **Group 4:** Investigate the combined product+placement+date change endpoint for null-handling; the `errorCode:1, message:null` suggests an unhandled exception.
- **Group 5:** Review the B2A request-builder for redundant parameter injection; investigate basket-ID allocation for magazine orders around TC35.
- **Group 6:** Fix decimal serialisation — enforce two-decimal scale for `priceNetExComm`.

## Prevention

- Add contract tests for collection ordering in CASS GET responses.
- Add regression tests for discount=0 scenarios after pricing changes.
- Add status-flag assertion to smoke suite so PRELIMINARY regression is caught early.
