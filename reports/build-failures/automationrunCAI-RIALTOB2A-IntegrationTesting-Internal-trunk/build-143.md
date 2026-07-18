# Jenkins Build Failure Report

---

## Build Summary

Build: `automationrunCAI-RIALTOB2A-IntegrationTesting-Internal-trunk` #143  
Date: 2026-07-18 21:03 UTC  
Status: UNSTABLE  
Total Tests: 513  
Passed: 427  
Failed: 86  
Pass Rate: 83.2%

---

## Root Cause Groups

## discountType expected [RIALTO] found [null]

**Affected Features:**
- `rialtoB2A(CASS)TestCase1and2.feature`, `rialtoB2A(CASS)TestCase3.feature`, `rialtoB2A(CASS)TestCase5.feature`, `rialtoB2A(CASS)TestCase6.feature`, `rialtoB2A(CASS)TestCase7.feature`, `rialtoB2A(CASS)TestCase9.feature`
- `rialtoB2A(CASS)TestCase11.feature`, `rialtoB2A(CASS)TestCase14.feature`, `rialtoB2A(CASS)TestCase15.feature`, `rialtoB2A(CASS)TestCase22.feature`, `rialtoB2A(CASS)TestCase23.feature`, `rialtoB2A(CASS)TestCase24.feature`, `rialtoB2A(CASS)TestCase26.feature`
- `rialtoB2A(CASS)TestCase27.feature`, `rialtoB2A(CASS)TestCase28.feature`, `rialtoB2A(CASS)TestCase30.feature`, `rialtoB2A(CASS)TestCase31.feature`, `rialtoB2A(CASS)TestCase32.feature`, `rialtoB2A(CASS)TestCase33.feature`, `rialtoB2A(CASS)TestCase34.feature`, `rialtoB2A(CASS)TestCase35.feature`, `rialtoB2A(CASS)TestCase36.feature`, `rialtoB2A(CASS)TestCase37.feature`

**Affected Scenarios:**
- TC1 and TC2, TC3, TC5, TC6, TC7, TC9, TC11, TC14, TC15, TC22 — CASS GET validations
- TC23, TC24, TC26 — MediaHouse original/updated/reverted basket validations
- TC27, TC28, TC30, TC31, TC32, TC33, TC34, TC35, TC36, TC37 — magazine/full-page verification flows

**Failure Pattern:**
`orders[0].printDetails.discountType` expected `[RIALTO]` but returned `[null]`, with related basket totals drifting on the same responses.

**Evidence:**
- TC1 and TC2 GET: `orders[0].printDetails.discountType` expected `[[RIALTO]]` found `[[null]]`
- TC14 GET: `orders[0].printDetails.discountType` expected `[[RIALTO, RIALTO, RIALTO, RIALTO]]` found `[[null, null, null, null]]`

**Impact:** 39 failures

**Confidence:** High

## Financial calculation and status flag drift

**Affected Features:**
- `rialtoB2A(CASS)TestCase1and2.feature`, `rialtoB2A(CASS)TestCase3.feature`, `rialtoB2A(CASS)TestCase4.feature`, `rialtoB2A(CASS)TestCase5.feature`, `rialtoB2A(CASS)TestCase6.feature`, `rialtoB2A(CASS)TestCase9.feature`, `rialtoB2A(CASS)TestCase11.feature`, `rialtoB2A(CASS)TestCase15.feature`
- `rialtoB2A(CASS)TestCase27.feature`, `rialtoB2A(CASS)TestCase28.feature`, `rialtoB2A(CASS)TestCase30.feature`, `rialtoB2A(CASS)TestCase31.feature`, `rialtoB2A(CASS)TestCase35.feature`, `rialtoB2A(CASS)TestCase37.feature`

**Affected Scenarios:**
- TC1 and TC2, TC3, TC4, TC5, TC6, TC9, TC11, TC15 — CASS POST/GET pricing or `statusFlags` checks
- TC27, TC28, TC30, TC31, TC35, TC37 — Rialto/MediaHouse create-update-revert pricing/state validations

**Failure Pattern:**
`statusFlags`, `discountAmount`, `commissionAmount`, `priceNet`, `vat`, and `totalInclVat` drift from fixture expectations.

**Evidence:**
- TC1 and TC2 POST: `orderHeader.statusFlags` expected `[[PRELIMINARY]]` found `[[]]`
- TC15 POST: `discountAmount` expected `[163140.03]` found `[196299.83]`

**Impact:** 21 failures

**Confidence:** High

## Two-product MH index out-of-bounds → TestContext cascade

**Affected Features:**
- `rialtoB2A(CASS)TestCase16.feature`, `rialtoB2A(CASS)TestCase17.feature`, `rialtoB2A(CASS)TestCase18.feature`, `rialtoB2A(CASS)TestCase19.feature`, `rialtoB2A(CASS)TestCase20.feature`, `rialtoB2A(CASS)TestCase29.feature`

**Affected Scenarios:**
- TC16, TC17, TC18, TC19, TC20 — multi-product MediaHouse GET/POST flows
- TC29 — MH update flow after missing shared identifiers

**Failure Pattern:**
`Index 13 out of bounds for length 13` prevents `odIds` from being stored, then downstream steps fail with missing TestContext data.

**Evidence:**
- TC16 GET: `Index 13 out of bounds for length 13`
- TC16 POST: `No MH odIds found in TestContext. Run the MH GET storage step before the patch step.`

**Impact:** 11 failures

**Confidence:** High

## Array ordering non-determinism (packageId/productId)

**Affected Features:**
- `rialtoB2A(CASS)TestCase15.feature`, `rialtoB2A(CASS)TestCase19.feature`, `rialtoB2A(CASS)TestCase22.feature`

**Affected Scenarios:**
- TC15, TC19, TC22 — package/product ordering assertions on POST updates

**Failure Pattern:**
`packageId` and `productId` arrays are returned in an unexpected order.

**Evidence:**
- TC15 POST: `packageId` expected `[[AB, SVD]]` found `[[SVD, AB]]`; `productId` expected `[[AB, SVD]]` found `[[SVD, AB]]`
- TC22 POST: `packageId` expected `[[SVDTI, SVDTI, SVDTI, AB, AB, AB]]` found `[[SVDTI, AB, SVDTI, AB, AB, SVDTI]]`

**Impact:** 3 failures

**Confidence:** High

## Path parameter mapping and TC29 null-pointer cascade

**Affected Features:**
- `rialtoB2A(CASS)TestCase24.feature`, `rialtoB2A(CASS)TestCase29.feature`

**Affected Scenarios:**
- TC24 — reverted full-page Rialto verification
- TC29 — created-order capture, MediaHouse checks, and reverted-state verification

**Failure Pattern:**
`agencyPrisaId` and `uuid` are swapped or missing, and TC29 follow-up validations then hit `NullPointerException`.

**Evidence:**
- TC24: `Redundant path parameters are: agencyPrisaId=6507. Undefined path parameters are: uuid.`
- TC29: `Invalid number of path parameters. Expected 1, was 0. Undefined path parameters are: agencyPrisaId.`

**Impact:** 5 failures

**Confidence:** High

## Post-patch/revert state mismatch (including rollback)

**Affected Features:**
- `rialtoB2A(CASS)TestCase16.feature`, `rialtoB2A(CASS)TestCase17.feature`, `rialtoB2A(CASS)TestCase18.feature`, `rialtoB2A(CASS)TestCase20.feature`, `rialtoB2A(CASS)TestCase23.feature`, `rialtoB2A(CASS)TestCase24.feature`, `rialtoB2A(CASS)TestCase27.feature`

**Affected Scenarios:**
- TC16, TC17, TC18, TC20 — patch/update payload validations after MH changes
- TC23, TC24 — revert/full-page transition checks
- TC27 — reverted Rialto order-state validation

**Failure Pattern:**
Patch/revert steps return unchanged or incorrect `issueDate`, `moduleCode`, or `placementId`; one revert request rolls back server-side.

**Evidence:**
- TC17 POST: `orderAdDetails.moduleCode` expected `[[54, 58]]` found `[[58, 58]]`
- TC23 revert: `Transaction rolled back because it has been marked as rollback-only`

**Impact:** 7 failures

**Confidence:** Medium

---

## Failing Tests / Steps

- 86 failing validations are grouped above by the six recurring root causes.
