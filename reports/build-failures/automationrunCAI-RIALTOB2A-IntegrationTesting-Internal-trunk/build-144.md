# Jenkins Build Failure Report

---

## Build Summary

Build: `automationrunCAI-RIALTOB2A-IntegrationTesting-Internal-trunk` #144  
Date: 2026-07-19 21:03 UTC  
Status: UNSTABLE  
Total Tests: 513  
Passed: 425  
Failed: 88  
Pass Rate: 82.8%

---

## Root Cause Groups

## discountType expected [RIALTO] found [null]

**Affected Features:**
- `rialtoB2A(CASS)TestCase3.feature`, `rialtoB2A(CASS)TestCase4.feature`, `rialtoB2A(CASS)TestCase5.feature`, `rialtoB2A(CASS)TestCase9.feature`, `rialtoB2A(CASS)TestCase11.feature`, `rialtoB2A(CASS)TestCase14.feature`, `rialtoB2A(CASS)TestCase15.feature`
- `rialtoB2A(CASS)TestCase22.feature`, `rialtoB2A(CASS)TestCase23.feature`, `rialtoB2A(CASS)TestCase24.feature`, `rialtoB2A(CASS)TestCase26.feature`
- `rialtoB2A(CASS)TestCase27.feature`, `rialtoB2A(CASS)TestCase28.feature`, `rialtoB2A(CASS)TestCase30.feature`, `rialtoB2A(CASS)TestCase31.feature`, `rialtoB2A(CASS)TestCase32.feature`, `rialtoB2A(CASS)TestCase33.feature`, `rialtoB2A(CASS)TestCase34.feature`, `rialtoB2A(CASS)TestCase35.feature`, `rialtoB2A(CASS)TestCase36.feature`, `rialtoB2A(CASS)TestCase37.feature`

**Affected Scenarios:**
- User perform CASS GET API - #1.1 (TC3 change Size)
- User perform CASS GET API - #1.1 (TC4 Change Placement)
- User perform CASS GET API - #1.1 (TC5 change to Uppslag/Spread/Panorama)
- User perform CASS GET API - #1.1 (TC9 change size from Rialto) ×2
- User perform CASS GET API - #1.1 (TC11 change to UPPSLAG from Rialto)
- User perform CASS GET API - #1.1 (TC14 change Product, Size, Placement & Date from Rialto) ×2
- User perform CASS GET API - #1.1 (TC15 2 products change date MH on head order line) ×2
- User perform CASS GET API - #1.1 (TC22 in MH change from Full page to uppslag) ×3
- Verify original full-page order state in MediaHouse - #1.1 (TC23)
- Verify updated MediaHouse basket state - #1.1 (TC23)
- Verify reverted MediaHouse basket state - #1.1 (TC23)
- Verify original full-page order state in MediaHouse - #1.1 (TC24)
- Verify updated MediaHouse basket state - #1.1 (TC24)
- Verify reverted MediaHouse basket state - #1.1 (TC24)
- Verify reverted MediaHouse basket state - #1.1 (TC26 Basic order for magazines)
- MEDIAHOUSE - Verify original full-page order state in MediaHouse - #1.1 (TC27 Magazine change date)
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
- MEDIAHOUSE - Verify updated MediaHouse basket state - #1.1 (TC37 - 2 Products Magazine changes the size in MH)

**Failure Pattern:**
`orders[0].printDetails.discountType` expected `[RIALTO]` but returned `[null]`, with related basket totals drifting on the same responses.

**Evidence:**
- TC11 GET: `orders[0].printDetails.discountType` expected `[[RIALTO]]` found `[[null]]`; `totalInclVat` expected `[169660.46]` found `[171598.78]`
- TC14 GET: `orders[0].printDetails.discountType` expected `[[RIALTO, RIALTO, RIALTO, RIALTO]]` found `[[null, null, null, null]]`

**Impact:** 34 failures

**Confidence:** High

---

## Financial Calculation and Status Flag Drift

**Affected Features:**
- `rialtoB2A(CASS)TestCase1and2.feature`, `rialtoB2A(CASS)TestCase3.feature`, `rialtoB2A(CASS)TestCase4.feature`, `rialtoB2A(CASS)TestCase5.feature`, `rialtoB2A(CASS)TestCase9.feature`, `rialtoB2A(CASS)TestCase11.feature`, `rialtoB2A(CASS)TestCase15.feature`
- `rialtoB2A(CASS)TestCase27.feature`, `rialtoB2A(CASS)TestCase28.feature`, `rialtoB2A(CASS)TestCase30.feature`, `rialtoB2A(CASS)TestCase31.feature`, `rialtoB2A(CASS)TestCase35.feature`, `rialtoB2A(CASS)TestCase37.feature`

**Affected Scenarios:**
- User perform CASS POST API - #1.1 (TC1 and TC2)
- User perform CASS GET API - #1.1 (TC3 change Size)
- User perform CASS POST API - #1.1 (TC3 change Size)
- User perform CASS GET API - #1.1 (TC4 Change Placement)
- User perform CASS POST API - #1.1 (TC4 Change Placement)
- User perform CASS GET API - #1.1 (TC5 change to Uppslag/Spread/Panorama)
- User perform CASS POST API - #1.1 (TC5 change to Uppslag/Spread/Panorama)
- User perform CASS POST API - #1.1 (TC9 change size from Rialto)
- User perform CASS GET API - #1.1 (TC11 change to UPPSLAG from Rialto)
- User perform CASS POST API - #1.1 (TC15 2 products change date MH on head order line)
- RIALTO - Verify created Rialto order and capture shared identifiers - #1.1 (TC27 Magazine change date)
- MEDIAHOUSE - Verify updated MediaHouse basket state - #1.1 (TC27 Magazine change date)
- RIALTO - Verify created Rialto order and capture shared identifiers - #1.1 (TC28 Magazine change size)
- MEDIAHOUSE - Verify updated MediaHouse basket state - #1.1 (TC28 Magazine change size)
- RIALTO - Verify Rialto reflects the reverted full-page state - #1.1 (TC28 Magazine change size)
- RIALTO - Verify Rialto reflects the reverted full-page state - #1.1 (TC30 Magazine change Date & Size)
- MEDIAHOUSE - Verify updated MediaHouse basket state - #1.1 (TC31 Magazine change Date, Size & Placement)
- RIALTO - Verify updated Agency order after Rialto change - #1.1 (TC35 Magazine change Date Size & Placement from Rialto)
- MEDIAHOUSE - Verify original order state in MediaHouse - #1.1 (TC37 - 2 Products Magazine changes size in MH)

**Failure Pattern:**
`statusFlags`, `discountAmount`, `commissionAmount`, `priceNet`, `vat`, and `totalInclVat` drift from fixture expectations.

**Evidence:**
- TC3 POST: `orderHeader.statusFlags` expected `[[PRELIMINARY]]` found `[[]]`; `priceNetExComm` expected `[127668.75]` found `[115680.28]`
- TC1 and TC2 POST: `discountAmount` expected `[0.0]` found `[63660.63]`; `orderHeader.priceNetExComm` expected `[192192.0]` found `[128531.37]`
- TC27 (Rialto): `discountAmount` expected `[[3600.0]]` found `[3600.0]` (array/scalar type mismatch)

**Impact:** 16 failures (several shared with discountType group)

**Confidence:** High

---

## Two-product MH Index Out-of-Bounds → TestContext Cascade

**Affected Features:**
- `rialtoB2A(CASS)TestCase16.feature`, `rialtoB2A(CASS)TestCase17.feature`, `rialtoB2A(CASS)TestCase18.feature`, `rialtoB2A(CASS)TestCase19.feature`, `rialtoB2A(CASS)TestCase20.feature`, `rialtoB2A(CASS)TestCase29.feature`

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
- MEDIAHOUSE - Update two MediaHouse order lines to uppslag - #1.1 (TC29 Magazine change to Uppslag/Spread/Panorama)

**Failure Pattern:**
`ArrayIndexOutOfBoundsException: Index 13 out of bounds for length 13` in CSV parsing prevents `odIds` from being stored in TestContext; downstream POST steps then fail with `No MH odIds found in TestContext`.

**Evidence:**
- TC16 GET: `java.lang.ArrayIndexOutOfBoundsException: Index 13 out of bounds for length 13` at `CSVRecord.get(CSVRecord.java:87)`
- TC16 POST: `No MH odIds found in TestContext. Run the MH GET storage step before the patch step.`

**Impact:** 11 failures

**Confidence:** High

---

## Array Ordering Non-determinism (packageId/productId)

**Affected Features:**
- `rialtoB2A(CASS)TestCase15.feature`, `rialtoB2A(CASS)TestCase19.feature`

**Affected Scenarios:**
- User perform CASS POST API - #1.1 (TC15 2 products change date MH on head order line)
- User perform CASS POST API - #1.1 (TC19 2 products change placement on head order from MH)

**Failure Pattern:**
`packageId` and `productId` arrays returned in non-deterministic order, failing ordered-equality assertions.

**Evidence:**
- TC15 POST: `packageId` expected `[[AB, SVD]]` found `[[SVD, AB]]`; `productId` expected `[[AB, SVD]]` found `[[SVD, AB]]`
- TC19 POST: same ordering inversion on `packageId`/`productId`

**Impact:** 2 failures

**Confidence:** High

---

## Path Parameter Mapping and TC29 Null-Pointer Cascade

**Affected Features:**
- `rialtoB2A(CASS)TestCase24.feature`, `rialtoB2A(CASS)TestCase29.feature`

**Affected Scenarios:**
- Revert two MediaHouse order lines to full page - #1.1 (TC24)
- Verify Rialto reflects the reverted full-page state - #1.1 (TC24)
- RIALTO - Verify created Rialto order and capture shared identifiers - #1.1 (TC29 Magazine change to Uppslag/Spread/Panorama)
- MEDIAHOUSE - Verify original full-page order state in MediaHouse - #1.1 (TC29)
- MEDIAHOUSE - Verify updated MediaHouse basket state - #1.1 (TC29)
- RIALTO - Verify Rialto reflects the reverted full-page state - #1.1 (TC29)

**Failure Pattern:**
`agencyPrisaId` and `uuid` path parameters are swapped or absent; TC29 cascades into `NullPointerException` on follow-up steps.

**Evidence:**
- TC24: `Redundant path parameters are: agencyPrisaId=6542. Undefined path parameters are: uuid.`
- TC29: `Invalid number of path parameters. Expected 1, was 0. Undefined path parameters are: agencyPrisaId.`

**Impact:** 6 failures

**Confidence:** High

---

## Post-Patch/Revert State Mismatch

**Affected Features:**
- `rialtoB2A(CASS)TestCase16.feature`, `rialtoB2A(CASS)TestCase17.feature`, `rialtoB2A(CASS)TestCase18.feature`, `rialtoB2A(CASS)TestCase20.feature`, `rialtoB2A(CASS)TestCase27.feature`, `rialtoB2A(CASS)TestCase35.feature`

**Affected Scenarios:**
- User perform CASS POST API - #1.1 (TC16 date not updated: `issueDate` expected `[[2026-07-01, 2026-07-21]]` found `[[2026-07-01, 2026-07-01]]`)
- User perform CASS POST API - #1.1 (TC17 moduleCode: expected `[[54, 58]]` found `[[58, 58]]`)
- User perform CASS POST API - #1.1 (TC18 moduleCode: expected `[[58, 54]]` found `[[58, 58]]`)
- User perform CASS POST API - #1.1 (TC20 placementId: expected `[[TEXT, SIDAN3]]` found `[[TEXT, TEXT]]`)
- MEDIAHOUSE - Update two MediaHouse order lines to uppslag - #1.1 (TC27: `issueDate` expected `[[2026-08-19]]` found `[[2026-08-26]]`)
- RIALTO - Verify Rialto reflects the reverted full-page state - #1.1 (TC27: `issueDate` expected `[[2026-08-19]]` found `[[2026-08-26]]`; `statusFlags` expected `[[PRELIMINARY]]` found `[[]]`)
- RIALTO - Verify updated Agency order after Rialto change - #1.1 (TC35: `placementId` expected `[[SIDAN2]]` found `[[HALVLIGG]]`; `issueDate` mismatch)
- MEDIAHOUSE - Verify updated magazine order state in MediaHouse - #1.1 (TC35: basket ID mismatch `[6552]` vs `[6553]`)

**Failure Pattern:**
Patch/update steps leave `issueDate`, `moduleCode`, or `placementId` unchanged; one test hits a transaction rollback; one test hits a basket-ID mismatch.

**Evidence:**
- TC17 POST: `orderAdDetails.moduleCode` expected `[[54, 58]]` found `[[58, 58]]`
- TC35 MH: `INTEGRATION MISMATCH: MH basket ID (orBoxid) [6552] does not match Agency Prisa ID [6553]`

**Impact:** 8 failures

**Confidence:** Medium

---

## Failing Tests / Steps

- 88 failing validations grouped above by six recurring root causes.
- Persistent failures vs. build #143 (86 failures): discountType null (+0 net), financial drift continues, index-out-of-bounds cluster unchanged.
