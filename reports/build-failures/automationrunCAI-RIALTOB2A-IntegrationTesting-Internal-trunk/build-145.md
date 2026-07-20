# Jenkins Build Failure Report

---

## Build Summary

Build: `automationrunCAI-RIALTOB2A-IntegrationTesting-Internal-trunk` #145  
Date: 2026-07-20 21:03 UTC  
Status: UNSTABLE  
Total Tests: 513  
Passed: 425  
Failed: 88  
Pass Rate: 82.8%

---

## Root Cause Groups

## discountType expected [RIALTO] found [null]

**Affected Features:**
- `rialtoB2A(CASS)TestCase1and2.feature`, `rialtoB2A(CASS)TestCase3.feature`, `rialtoB2A(CASS)TestCase4.feature`, `rialtoB2A(CASS)TestCase5.feature`, `rialtoB2A(CASS)TestCase9.feature`, `rialtoB2A(CASS)TestCase11.feature`, `rialtoB2A(CASS)TestCase14.feature`, `rialtoB2A(CASS)TestCase15.feature`
- `rialtoB2A(CASS)TestCase22.feature`, `rialtoB2A(CASS)TestCase23.feature`, `rialtoB2A(CASS)TestCase24.feature`, `rialtoB2A(CASS)TestCase26.feature`
- `rialtoB2A(CASS)TestCase27.feature`, `rialtoB2A(CASS)TestCase28.feature`, `rialtoB2A(CASS)TestCase30.feature`, `rialtoB2A(CASS)TestCase31.feature`, `rialtoB2A(CASS)TestCase32.feature`, `rialtoB2A(CASS)TestCase33.feature`, `rialtoB2A(CASS)TestCase34.feature`, `rialtoB2A(CASS)TestCase35.feature`, `rialtoB2A(CASS)TestCase36.feature`

**Affected Scenarios:**
- User perform CASS GET API - #1.1 (TC1 and TC2)
- User perform CASS GET API - #1.1 (TC3 change Size) ×2
- User perform CASS GET API - #1.1 (TC4 Change Placement)
- User perform CASS GET API - #1.1 (TC5 change to Uppslag/Spread/Panorama)
- User perform CASS GET API - #1.1 (TC9 change size from Rialto)
- User perform CASS GET API - #1.1 (TC11 change to UPPSLAG from Rialto)
- User perform CASS GET API - #1.1 (TC14 change Product, Size, Placement & Date from Rialto) ×2
- User perform CASS GET API - #1.1 (TC15 2 products change date MH on head order line) ×2
- User perform CASS GET API - #1.1 (TC22 in MH change from Full page to uppslag)
- Verify original full-page order state in MediaHouse - #1.1 (TC23)
- Verify updated MediaHouse basket state - #1.1 (TC23)
- Verify original full-page order state in MediaHouse - #1.1 (TC24)
- Verify reverted MediaHouse basket state - #1.1 (TC26 Basic order for magazines)
- MEDIAHOUSE - Verify original full-page order state in MediaHouse - #1.1 (TC27 Magazine change date)
- MEDIAHOUSE - Verify updated MediaHouse basket state - #1.1 (TC27 Magazine change date)
- MEDIAHOUSE - Verify original full-page order state in MediaHouse - #1.1 (TC28 Magazine change size)
- MEDIAHOUSE - Verify original full-page order state in MediaHouse - #1.1 (TC30 Magazine change Date & Size)
- MEDIAHOUSE - Verify original full-page order state in MediaHouse - #1.1 (TC31 Magazine change Date, Size & Placement)
- MEDIAHOUSE - Verify original magazine order state in MediaHouse - #1.1 (TC32 Magazine change date from Rialto)
- MEDIAHOUSE - Verify updated magazine order state in MediaHouse - #1.1 (TC32)
- MEDIAHOUSE - Verify original magazine order state in MediaHouse - #1.1 (TC33 Magazine change size from Rialto)
- MEDIAHOUSE - Verify updated magazine order state in MediaHouse - #1.1 (TC33)
- MEDIAHOUSE - Verify original magazine order state in MediaHouse - #1.1 (TC34 Magazine change to UPPSLAG from Rialto)
- MEDIAHOUSE - Verify updated magazine order state in MediaHouse - #1.1 (TC34)
- MEDIAHOUSE - Verify original magazine order state in MediaHouse - #1.1 (TC35 Magazine change Date Size & Placement from Rialto)
- MEDIAHOUSE - Verify original magazine order state in MediaHouse - #1.1 (TC36 Magazine change Product Size Placement & Date from Rialto)
- MEDIAHOUSE - Verify updated magazine order state in MediaHouse - #1.1 (TC36)

**Failure Pattern:**
`orders[*].printDetails.discountType` expected `[RIALTO]` but returned `[null]`; basket totals drift on the same responses.

**Evidence:**
- TC9 GET: `orders[0].printDetails.discountType` expected `[[RIALTO]]` found `[[null]]`
- TC14 GET: `orders[0].printDetails.discountType` expected `[[RIALTO, RIALTO, RIALTO, RIALTO]]` found `[[null, null, null, null]]`; `orderBasketPriceSummary.orderDiscount` expected `[111.00]` found `[725185.xx]`

**Impact:** 31 failures

**Confidence:** High

---

## Financial Calculation and Status Flag Drift

**Affected Features:**
- `rialtoB2A(CASS)TestCase1and2.feature`, `rialtoB2A(CASS)TestCase3.feature`, `rialtoB2A(CASS)TestCase4.feature`, `rialtoB2A(CASS)TestCase5.feature`, `rialtoB2A(CASS)TestCase6.feature`, `rialtoB2A(CASS)TestCase9.feature`, `rialtoB2A(CASS)TestCase11.feature`, `rialtoB2A(CASS)TestCase15.feature`
- `rialtoB2A(CASS)TestCase23.feature`, `rialtoB2A(CASS)TestCase27.feature`, `rialtoB2A(CASS)TestCase28.feature`, `rialtoB2A(CASS)TestCase30.feature`, `rialtoB2A(CASS)TestCase31.feature`, `rialtoB2A(CASS)TestCase37.feature`

**Affected Scenarios:**
- User perform CASS POST API - #1.1 (TC1 and TC2)
- User perform CASS GET API - #1.1 (TC3 change Size) [2nd step]
- User perform CASS POST API - #1.1 (TC3 change Size)
- User perform CASS GET API - #1.1 (TC4 Change Placement) [2nd step]
- User perform CASS POST API - #1.1 (TC4 Change Placement)
- User perform CASS GET API - #1.1 (TC5 change to Uppslag/Spread/Panorama) [2nd step]
- User perform CASS POST API - #1.1 (TC5 change to Uppslag/Spread/Panorama)
- User perform CASS POST API - #1.1 (TC6 change date and size)
- User perform CASS GET API - #1.1 (TC9 change size from Rialto) [2nd step — depth/moduleCode]
- User perform CASS POST API - #1.1 (TC9 change size from Rialto)
- User perform CASS GET API - #1.1 (TC11 change to UPPSLAG from Rialto) [2nd step]
- User perform CASS POST API - #1.1 (TC15 2 products change date MH on head order line)
- Verify reverted MediaHouse basket state - #1.1 (TC23)
- RIALTO - Verify created Rialto order and capture shared identifiers - #1.1 (TC27 Magazine change date)
- RIALTO - Verify Rialto reflects the reverted full-page state - #1.1 (TC27)
- RIALTO - Verify created Rialto order and capture shared identifiers - #1.1 (TC28 Magazine change size)
- MEDIAHOUSE - Verify updated MediaHouse basket state - #1.1 (TC28)
- RIALTO - Verify Rialto reflects the reverted full-page state - #1.1 (TC28)
- RIALTO - Verify Rialto reflects the reverted full-page state - #1.1 (TC30 Magazine change Date & Size)
- MEDIAHOUSE - Verify updated MediaHouse basket state - #1.1 (TC31 Magazine change Date, Size & Placement)
- RIALTO - Verify Rialto reflects the reverted full-page state - #1.1 (TC31)
- MEDIAHOUSE - Verify original order state in MediaHouse - #1.1 (TC37 - 2 Products Magazine changes size in MH)

**Failure Pattern:**
`statusFlags`, `discountAmount`, `commissionAmount`, `priceNet`, `vat`, and `totalInclVat` drift from fixture expectations; TC27/TC28 additionally hit array-vs-scalar serialisation mismatch.

**Evidence:**
- TC1&2 POST: `discountAmount` expected `[0.0]` found `[63660.63]`; `orderHeader.statusFlags` expected `[[PRELIMINARY]]` found `[[]]`
- TC6 POST: `discountAmount` expected `[0.0]` found `[63660.63]`; `orderHeader.priceNetExComm` expected `[115320.00]` found `[128531.37]`
- TC27 Rialto: `discountAmount` expected `[[3600.0]]` found `[3600.0]` (array/scalar mismatch)
- TC28 Rialto revert: `orderAdDetails.commissionAmount` expected `[[155.0]]` found `[[31.0]]`

**Impact:** 22 failures

**Confidence:** High

---

## Two-product MH Index Out-of-Bounds → TestContext Cascade

**Affected Features:**
- `rialtoB2A(CASS)TestCase16.feature`, `rialtoB2A(CASS)TestCase17.feature`, `rialtoB2A(CASS)TestCase18.feature`, `rialtoB2A(CASS)TestCase19.feature`, `rialtoB2A(CASS)TestCase20.feature`

**Affected Scenarios:**
- User perform CASS GET API - #1.1 (TC16 2 products change date on order line which is not head order line from MH)
- User perform CASS POST API - #1.1 (TC16)
- User perform CASS GET API - #1.1 (TC17 2 products change size on head order line from MH)
- User perform CASS POST API - #1.1 (TC17)
- User perform CASS GET API - #1.1 (TC18 2 products change size on not registered as head order line from MH)
- User perform CASS POST API - #1.1 (TC18)
- User perform CASS GET API - #1.1 (TC19 2 products change placement on head order from MH)
- User perform CASS POST API - #1.1 (TC19)
- User perform CASS GET API - #1.1 (TC20 2 products change placement order for non head from MH)
- User perform CASS POST API - #1.1 (TC20)

**Failure Pattern:**
`ArrayIndexOutOfBoundsException: Index 13 out of bounds for length 13` in CSV parsing prevents `odIds` from being stored in TestContext; downstream POST steps then fail with `No MH odIds found in TestContext`.

**Evidence:**
- TC16 GET: `java.lang.ArrayIndexOutOfBoundsException: Index 13 out of bounds for length 13`
- TC16 POST: `No MH odIds found in TestContext. Run the MH GET storage step before the patch step.`

**Impact:** 10 failures

**Confidence:** High

---

## Array Ordering Non-determinism (packageId / productId / paCode / plaCode)

**Affected Features:**
- `rialtoB2A(CASS)TestCase15.feature`, `rialtoB2A(CASS)TestCase19.feature`, `rialtoB2A(CASS)TestCase22.feature`, `rialtoB2A(CASS)TestCase24.feature`, `rialtoB2A(CASS)TestCase37.feature`

**Affected Scenarios:**
- User perform CASS POST API - #1.1 (TC15 2 products change date MH on head order line)
- User perform CASS POST API - #1.1 (TC19 2 products change placement on head order from MH)
- User perform CASS POST API - #1.1 (TC22 in MH change from Full page to uppslag)
- User perform CASS GET API - #1.1 (TC22) [3rd step — post-revert paCode/plaCode]
- Verify updated MediaHouse basket state - #1.1 (TC24)
- Verify reverted MediaHouse basket state - #1.1 (TC24)
- MEDIAHOUSE - Verify updated MediaHouse basket state - #1.1 (TC37 - 2 Products Magazine changes size in MH)

**Failure Pattern:**
`packageId`, `productId`, `paCode`, `plaCode`, and `prodCode` arrays returned in non-deterministic order; ordered-equality assertions fail.

**Evidence:**
- TC15 POST: `packageId` expected `[[AB, SVD]]` found `[[SVD, AB]]`; `productId` expected `[[AB, SVD]]` found `[[SVD, AB]]`
- TC22 POST: `body.orderAdDetailUpdates.packageId` expected `[[SVDTI, SVDTI, SVDTI, AB, AB, AB]]` found `[[SVDTI, AB, SVDTI, AB, AB, SVDTI]]`

**Impact:** 7 failures

**Confidence:** High

---

## Path Parameter Mapping Error (TC24 / TC29)

**Affected Features:**
- `rialtoB2A(CASS)TestCase24.feature`, `rialtoB2A(CASS)TestCase29.feature`

**Affected Scenarios:**
- Verify Rialto reflects the reverted full-page state - #1.1 (TC24)
- RIALTO - Verify created Rialto order and capture shared identifiers - #1.1 (TC29 Magazine change to Uppslag/Spread/Panorama)
- MEDIAHOUSE - Verify original full-page order state in MediaHouse - #1.1 (TC29)
- MEDIAHOUSE - Update two MediaHouse order lines to uppslag - #1.1 (TC29)
- MEDIAHOUSE - Verify updated MediaHouse basket state - #1.1 (TC29)
- RIALTO - Verify Rialto reflects the reverted full-page state - #1.1 (TC29)

**Failure Pattern:**
`agencyPrisaId` and `uuid` path parameters are swapped or absent; TC29 cascades into null downstream steps.

**Evidence:**
- TC24: `Redundant path parameters are: agencyPrisaId=6580. Undefined path parameters are: uuid.`
- TC29: `Redundant path parameters are: uuid=3b6c5519-e445-4404-be9d-ce24ade05abd. Undefined path parameters are: agencyPrisaId.`

**Impact:** 6 failures

**Confidence:** High

---

## Post-Patch / Revert State Mismatch and Transaction Rollback

**Affected Features:**
- `rialtoB2A(CASS)TestCase16.feature`, `rialtoB2A(CASS)TestCase17.feature`, `rialtoB2A(CASS)TestCase18.feature`, `rialtoB2A(CASS)TestCase20.feature`, `rialtoB2A(CASS)TestCase22.feature`, `rialtoB2A(CASS)TestCase24.feature`, `rialtoB2A(CASS)TestCase27.feature`, `rialtoB2A(CASS)TestCase35.feature`

**Affected Scenarios:**
- User perform CASS POST API - #1.1 (TC16 — `issueDate` expected `[[2026-07-01, 2026-07-21]]` found `[[2026-07-01, 2026-07-01]]`)
- User perform CASS POST API - #1.1 (TC17 — `moduleCode` expected `[[54, 58]]` found `[[58, 58]]`)
- User perform CASS POST API - #1.1 (TC18 — `moduleCode` expected `[[58, 54]]` found `[[58, 58]]`)
- User perform CASS POST API - #1.1 (TC20 — `placementId` expected `[[TEXT, SIDAN3]]` found `[[TEXT, TEXT]]`)
- User perform CASS POST API - #1.1 (TC22 — Transaction rolled back 500)
- User perform CASS GET API - #1.1 (TC22 — post-revert `plaCode`/`width` not fully restored)
- Revert two MediaHouse order lines to full page - #1.1 (TC24 — Transaction rolled back 500)
- MEDIAHOUSE - Update two MediaHouse order lines to uppslag - #1.1 (TC27 — `issueDate` expected `[[2026-08-19]]` found `[[2026-08-26]]`)
- RIALTO - Verify updated Agency order after Rialto change - #1.1 (TC35 — `placementId` expected `[[SIDAN2]]` found `[[HALVLIGG]]`; `issueDate` mismatch)
- MEDIAHOUSE - Verify updated magazine order state in MediaHouse - #1.1 (TC35 — basket ID mismatch `[6590]` vs `[6591]`)

**Failure Pattern:**
Patch/update steps leave `issueDate`, `moduleCode`, or `placementId` unchanged; two tests (TC22, TC24) hit a `Transaction rolled back` 500 error; TC35 hits a basket-ID synchronisation drift.

**Evidence:**
- TC22 POST: `500: "Transaction rolled back because it has been marked as rollback-only"` expected `[N200]` found `[N400]`
- TC35 MH: `INTEGRATION MISMATCH: MH basket ID (orBoxid) [6590] does not match Agency Prisa ID [6591]`

**Impact:** 10 failures

**Confidence:** Medium

---

## Failing Tests / Steps

- 88 failing validations grouped above by six recurring root causes.
- Identical failure count to build #144 (88 failures) — no improvement; all six root cause clusters remain unresolved.
