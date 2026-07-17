# Jenkins Build Failure Report

---

## Build Summary

Build: `automationrunCAI-RIALTOB2A-IntegrationTesting-Internal-trunk` #142  
Date: 2026-07-17 21:03 UTC  
Status: UNSTABLE  
Total Tests: 513  
Passed: 427  
Failed: 86  
Pass Rate: 83.2%

---

## Root Cause Groups

## discountType expected [RIALTO] found [null]

**Affected Features:**
- `rialtoB2A(CASS)TestCase1and2.feature`, `TestCase3.feature`, `TestCase4.feature`, `TestCase5.feature`, `TestCase6.feature`, `TestCase7.feature`, `TestCase9.feature`, `TestCase11.feature`, `TestCase14.feature`, `TestCase15.feature`, `TestCase22.feature`, `TestCase23.feature`, `TestCase24.feature`, `TestCase26.feature`, `TestCase27.feature`, `TestCase28.feature`, `TestCase30.feature`, `TestCase31.feature`, `TestCase32.feature`, `TestCase33.feature`, `TestCase34.feature`, `TestCase35.feature`, `TestCase36.feature`

**Affected Scenarios:**
- TC1 and TC2 (CASS GET), TC3 (CASS GET), TC4 (CASS GET), TC5 (CASS GET), TC6 (CASS GET), TC7 (CASS GET), TC9 (CASS GET), TC11 (CASS GET), TC14 (CASS GET), TC15 (CASS GET), TC22 (CASS GET)
- TC23 (Verify original/updated/reverted MediaHouse basket), TC24 (Verify original/updated/reverted MediaHouse basket), TC26 (Verify reverted MediaHouse basket)
- TC27 (MEDIAHOUSE verify original full-page), TC28 (MEDIAHOUSE verify original full-page), TC30 (MEDIAHOUSE verify original full-page), TC31 (MEDIAHOUSE verify original full-page)
- TC32 (MEDIAHOUSE verify original/updated magazine order), TC33 (MEDIAHOUSE verify original/updated magazine order), TC34 (MEDIAHOUSE verify original/updated magazine order), TC35 (MEDIAHOUSE verify original magazine order), TC36 (MEDIAHOUSE verify original/updated magazine order)

**Failure Pattern:**
`orders[0].printDetails.discountType` expected `[RIALTO]` found `[null]`.

**Evidence:**
- TC1/TC2 GET: `discountType` expected `[[RIALTO]]` found `[[null]]`; `totalInclVat` expected `155683.63` found `171598.78`
- TC14 GET: `discountType` expected `[[RIALTO, RIALTO, RIALTO, RIALTO]]` found `[[null, null, null, null]]`

**Impact:** 36 failures

**Confidence:** High

## Financial calculation and status flag drift

**Affected Features:**
- `rialtoB2A(CASS)TestCase1and2.feature`, `TestCase3.feature`, `TestCase4.feature`, `TestCase5.feature`, `TestCase6.feature`, `TestCase9.feature`, `TestCase11.feature`, `TestCase15.feature`, `TestCase27.feature`, `TestCase28.feature`, `TestCase30.feature`, `TestCase31.feature`, `TestCase35.feature`, `TestCase37.feature`

**Affected Scenarios:**
- TC1 and TC2 (CASS POST), TC3 (CASS POST + CASS GET), TC4 (CASS POST + CASS GET), TC5 (CASS POST + CASS GET), TC6 (CASS POST), TC9 (CASS POST), TC11 (CASS GET), TC15 (CASS POST)
- TC27 (RIALTO create + MEDIAHOUSE updated basket + RIALTO reverted state), TC28 (RIALTO create + MEDIAHOUSE updated basket + RIALTO reverted state)
- TC30 (RIALTO reverted state), TC31 (MEDIAHOUSE updated basket + RIALTO reverted state), TC35 (RIALTO updated order + MEDIAHOUSE updated magazine order), TC37 (MEDIAHOUSE original + updated order state)

**Failure Pattern:**
`statusFlags`, `discountAmount`, `commissionAmount`, `priceNet`, `totalInclVat` drift from fixtures.

**Evidence:**
- TC1/TC2 POST: `orderHeader.statusFlags` expected `[[PRELIMINARY]]` found `[[]]`
- TC28 revert: `priceNet` expected `4845.0` found `4969.0`; `commissionAmount` expected `155.00` found `250.00`

**Impact:** 24 failures

**Confidence:** High

## Two-product MH index out-of-bounds → TestContext cascade

**Affected Features:**
- `rialtoB2A(CASS)TestCase16.feature`, `TestCase17.feature`, `TestCase18.feature`, `TestCase19.feature`, `TestCase20.feature`, `TestCase29.feature`

**Affected Scenarios:**
- TC16 (CASS GET + CASS POST), TC17 (CASS GET + CASS POST), TC18 (CASS GET + CASS POST), TC19 (CASS GET + CASS POST), TC20 (CASS GET + CASS POST), TC29 (MEDIAHOUSE update two order lines)

**Failure Pattern:**
`Index 13 out of bounds` blocks `odIds` storage, causing `No MH odIds found in TestContext`.

**Evidence:**
- TC16 GET: `Index 13 out of bounds for length 13`
- TC16 POST: `No MH odIds found in TestContext. Run the MH GET storage step before the patch step.`

**Impact:** 11 failures

**Confidence:** High

## Array ordering non-determinism (packageId/productId)

**Affected Features:**
- `rialtoB2A(CASS)TestCase15.feature`, `TestCase19.feature`, `TestCase22.feature`

**Affected Scenarios:**
- TC15 (CASS POST), TC19 (CASS POST), TC22 (CASS POST)

**Failure Pattern:**
`packageId`/`productId` arrays returned in unexpected order.

**Evidence:**
- TC15 POST: `packageId` expected `[[AB, SVD]]` found `[[SVD, AB]]`; `productId` expected `[[AB, SVD]]` found `[[SVD, AB]]`
- TC22 POST: `packageId` expected `[[SVDTI, SVDTI, SVDTI, AB, AB, AB]]` found `[[SVDTI, AB, SVDTI, AB, AB, SVDTI]]`

**Impact:** 3 failures

**Confidence:** High

## Path parameter mapping and TC29 null-pointer cascade

**Affected Features:**
- `rialtoB2A(CASS)TestCase24.feature`, `TestCase29.feature`

**Affected Scenarios:**
- TC24 (RIALTO verify reverted full-page state)
- TC29 (RIALTO create, MEDIAHOUSE verify original state, MEDIAHOUSE verify updated state, RIALTO verify reverted state)

**Failure Pattern:**
`agencyPrisaId`/`uuid` are swapped or missing; TC29 follow-up MediaHouse steps throw `NullPointerException`.

**Evidence:**
- TC24: `Redundant path parameters: agencyPrisaId=6472. Undefined path parameters: uuid`
- TC29 revert: `Invalid number of path parameters. Expected 1, was 0. Undefined path parameters are: agencyPrisaId.`

**Impact:** 5 failures

**Confidence:** High

## Post-patch/revert state mismatch (including rollback)

**Affected Features:**
- `rialtoB2A(CASS)TestCase16.feature`, `TestCase17.feature`, `TestCase18.feature`, `TestCase20.feature`, `TestCase23.feature`, `TestCase24.feature`, `TestCase27.feature`

**Affected Scenarios:**
- TC16 (CASS POST), TC17 (CASS POST), TC18 (CASS POST), TC20 (CASS POST), TC23 (revert two order lines), TC24 (revert two order lines), TC27 (MEDIAHOUSE update two order lines)

**Failure Pattern:**
Patch/revert steps return unchanged or incorrect state; one revert call fails with rollback-only transaction.

**Evidence:**
- TC16 POST: `issueDate` expected `[[2026-07-01, 2026-07-21]]` found `[[2026-07-01, 2026-07-01]]`
- TC23 revert: `Transaction rolled back because it has been marked as rollback-only`

**Impact:** 7 failures

**Confidence:** Medium

---

## Failing Tests / Steps

- 86 failed/regression validations grouped above.
