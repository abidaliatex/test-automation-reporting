# Jenkins Build Failure Report

## Build Summary

Build: `automationrunCAI-RIALTOB2A-IntegrationTesting-Internal-trunk` #134  
Date: 2026-07-10 21:03 UTC  
Status: UNSTABLE  
Total Tests: 513  
Passed: 427  
Failed: 86  
Pass Rate: 83.2%

---

## Root Cause Groups

## MediaHouse discountType/pricing assertions drift from current responses

**Affected Features:**
- `rialtoB2A(CASS)TestCase1.feature`, `rialtoB2A(CASS)TestCase2.feature`, `rialtoB2A(CASS)TestCase3.feature`, `rialtoB2A(CASS)TestCase4.feature`, `rialtoB2A(CASS)TestCase5.feature`, `rialtoB2A(CASS)TestCase6.feature`, `rialtoB2A(CASS)TestCase7.feature`, `rialtoB2A(CASS)TestCase9.feature`, `rialtoB2A(CASS)TestCase11.feature`
- `rialtoB2A(CASS)TestCase14.feature`, `rialtoB2A(CASS)TestCase15.feature`, `rialtoB2A(CASS)TestCase22.feature`, `rialtoB2A(CASS)TestCase23.feature`, `rialtoB2A(CASS)TestCase24.feature`
- `rialtoB2A(CASS)TestCase26.feature`, `rialtoB2A(CASS)TestCase27.feature`, `rialtoB2A(CASS)TestCase28.feature`, `rialtoB2A(CASS)TestCase30.feature`, `rialtoB2A(CASS)TestCase31.feature`, `rialtoB2A(CASS)TestCase32.feature`, `rialtoB2A(CASS)TestCase33.feature`, `rialtoB2A(CASS)TestCase34.feature`, `rialtoB2A(CASS)TestCase35.feature`, `rialtoB2A(CASS)TestCase36.feature`

**Affected Scenarios:**
- `tc_getMHTC01` verify order created in Rialto from MH; `tc_getMHTC02` verify order created in Rialto from MH; `tc_getMHTC03` placement; `tc_getMHTC03a` placement after change; `tc_getMHTC04` Uppslag/Spread/Panorama; `tc_getMHTC05` change date and size; `tc_getMHTC06` change date, size and placement; `tc_getMHTC07` size from Rialto; `tc_getMHTC07a` size from Rialto after change
- `tc_getMHTC09` Uppslag from Rialto; `tc_getMHTC12` product/size/placement/date from Rialto; `tc_getMHTC12a` same flow after change; `tc_getMHTC13` two-product MH date change; `tc_getMHTC13a` two-product MH date change after update
- `tc_getMHTC19`, `tc_getMHTC19a`, `tc_getMHTC19b`, `tc_getMHTC20`, `tc_getMHTC20a`, `tc_getMHTC20b`, `tc_getMHTC21`, `tc_getMHTC21a`, `tc_getMHTC21b` full-page/uppslag change validations
- `tc_getMHTC_MZN01`, `tc_getMHTC_MZN02a`, `tc_getMHTC_MZN02b`, `tc_getMHTC_MZN03a`, `tc_getMHTC_MZN05a`, `tc_getMHTC_MZN06a`, `tc_getMHTC_MZN07a`, `tc_getMHTC_MZN07b`, `tc_getMHTC_MZN08a`, `tc_getMHTC_MZN08b`, `tc_getMHTC_MZN09a`, `tc_getMHTC_MZN09b`, `tc_getMHTC_MZN10a`, `tc_getMHTC_MZN11a`, `tc_getMHTC_MZN11b`

**Failure Pattern:**
`orders*.printDetails.discountType` is repeatedly expected as `RIALTO` but returned as `null`, with the same MH basket responses also shifting commission, VAT, net, and total values.

**Evidence:**
- `tc_getMHTC01`: `orders[0].printDetails.discountType` expected `RIALTO` found `null`; `orderBasketPriceSummary.totalInclVat` expected `155683.63` found `171598.78`
- `tc_getMHTC12`: `orders[0].printDetails.discountType` expected `[RIALTO, RIALTO, RIALTO, RIALTO]` found `[null, null, null, null]`
- `tc_getMHTC_MZN01`: `orders.printDetails.discountType` expected `RIALTO` found `null`

**Impact:** 38 failures

**Confidence:** High

## State updates are not persisted or are returned in the wrong order

**Affected Features:**
- `rialtoB2A(CASS)TestCase1.feature`, `rialtoB2A(CASS)TestCase2.feature`, `rialtoB2A(CASS)TestCase3.feature`, `rialtoB2A(CASS)TestCase4.feature`, `rialtoB2A(CASS)TestCase5.feature`, `rialtoB2A(CASS)TestCase6.feature`, `rialtoB2A(CASS)TestCase9.feature`
- `rialtoB2A(CASS)TestCase15.feature`, `rialtoB2A(CASS)TestCase16.feature`, `rialtoB2A(CASS)TestCase17.feature`, `rialtoB2A(CASS)TestCase18.feature`, `rialtoB2A(CASS)TestCase19.feature`, `rialtoB2A(CASS)TestCase20.feature`, `rialtoB2A(CASS)TestCase22.feature`, `rialtoB2A(CASS)TestCase24.feature`
- `rialtoB2A(CASS)TestCase27.feature`, `rialtoB2A(CASS)TestCase28.feature`, `rialtoB2A(CASS)TestCase30.feature`, `rialtoB2A(CASS)TestCase31.feature`, `rialtoB2A(CASS)TestCase35.feature`

**Affected Scenarios:**
- `tc_getIntegrationRialto02` issue-date/state validation; `tc_getIntegrationRialto04` size validation; `tc_getIntegrationRialto05b` placement validation; `tc_getIntegrationRialto06b` Uppslag/Spread/Panorama validation; `tc_getIntegrationRialto07b` date+size validation; `tc_getIntegrationRialto09b` size update validation from Rialto
- `tc_getIntegrationRialto15a`, `tc_getIntegrationRialto15b`, `tc_getIntegrationRialto16b`, `tc_getIntegrationRialto17b`, `tc_getIntegrationRialto18b`, `tc_getIntegrationRialto19b`, `tc_getIntegrationRialto20b` two-product change validations
- `tc_patchIntegrationMH13`, `tc_patchIntegrationMH16a`, `tc_patchIntegrationMH_MZN01`, `tc_getIntegrationRialtoMZN02a`, `tc_getIntegrationRialtoMZN02b`, `tc_getIntegrationRialtoMZN03a`, `tc_getIntegrationRialtoMZN03b`, `tc_getIntegrationRialtoMZN05b`, `tc_getIntegrationRialtoMZN06b`, `tc_getIntegrationRialtoMZN10b`

**Failure Pattern:**
Changed issue dates, placements, module codes, package ordering, and `PRELIMINARY` status flags are either not reflected in downstream GET responses or are returned in a different order than the fixtures expect.

**Evidence:**
- `tc_getIntegrationRialto02`: `orderHeader.statusFlags` expected `PRELIMINARY` found empty
- `tc_getIntegrationRialto19b`: `packageId` expected `[AB, SVD]` found `[SVD, AB]`; `placementId` expected `[TEXT, SIDAN3]` found `[TEXT, TEXT]`
- `tc_patchIntegrationMH13`: patch payload `placementId` and `issueDate` arrays differ from expected ordering/content

**Impact:** 23 failures

**Confidence:** Medium

## Two-product MH flows break before patch steps can reuse stored order-line ids

**Affected Features:**
- `rialtoB2A(CASS)TestCase16.feature`, `rialtoB2A(CASS)TestCase17.feature`, `rialtoB2A(CASS)TestCase18.feature`, `rialtoB2A(CASS)TestCase19.feature`, `rialtoB2A(CASS)TestCase20.feature`, `rialtoB2A(CASS)TestCase29.feature`

**Affected Scenarios:**
- `tc_getMHTC14`, `tc_getMHTC15`, `tc_getMHTC16`, `tc_getMHTC17`, `tc_getMHTC18` two-product MH GET validations
- `tc_patchIntegrationMH08`, `tc_patchIntegrationMH09`, `tc_patchIntegrationMH10`, `tc_patchIntegrationMH11`, `tc_patchIntegrationMH12` two-product MH patch steps
- `tc_patchIntegrationMH_MZN03` magazine Uppslag/Spread/Panorama patch

**Failure Pattern:**
The initial MH validation step fails with an array-index error, so no `odIds` are stored in `TestContext`; the next patch steps then fail immediately because the required MH order-line ids are missing.

**Evidence:**
- `tc_getMHTC14`/`15`/`16`/`17`/`18`: `Index 13 out of bounds for length 13`
- Follow-on patch steps: `No MH odIds found in TestContext. Run the MH GET storage step before the patch step.`

**Impact:** 11 failures

**Confidence:** High

## Patch and follow-up requests use invalid parameters or hit rollback errors

**Affected Features:**
- `rialtoB2A(CASS)TestCase23.feature`, `rialtoB2A(CASS)TestCase24.feature`, `rialtoB2A(CASS)TestCase29.feature`

**Affected Scenarios:**
- `tc_patchIntegrationMH15a` revert-back patch after two-orderline full-page change
- `tc_getIntegrationRialto24c` Rialto follow-up validation after uppslag-to-full-page change
- `tc_getIntegrationRialtoMZN04b`, `tc_getMHTC_MZN04a`, `tc_getMHTC_MZN04b` magazine Uppslag/Spread/Panorama follow-up validations

**Failure Pattern:**
Some follow-up steps construct requests with missing/redundant path parameters, and one MH patch rolls back server-side, so later validations cannot execute against the intended entity.

**Evidence:**
- `tc_patchIntegrationMH15a`: HTTP 500 `Transaction rolled back because it has been marked as rollback-only`
- `tc_getIntegrationRialto24c`: redundant `agencyPrisaId`, undefined `uuid`
- `tc_getIntegrationRialtoMZN04b`: undefined `agencyPrisaId` / redundant `uuid`

**Impact:** 6 failures

**Confidence:** High

## Residual pricing and identity mismatches remain in a few post-change validations

**Affected Features:**
- `rialtoB2A(CASS)TestCase3.feature`, `rialtoB2A(CASS)TestCase5.feature`, `rialtoB2A(CASS)TestCase11.feature`, `rialtoB2A(CASS)TestCase28.feature`, `rialtoB2A(CASS)TestCase31.feature`, `rialtoB2A(CASS)TestCase35.feature`, `rialtoB2A(CASS)TestCase37.feature`

**Affected Scenarios:**
- `tc_getMHTC02a`, `tc_getMHTC04a`, `tc_getMHTC09a`, `tc_getMHTC_MZN03b`, `tc_getMHTC_MZN06b`, `tc_getMHTC_MZN10b`, `tc_getMHTC_MZN12a`, `tc_getMHTC_MZN12b`

**Failure Pattern:**
These checks do not share the `discountType=null` signature, but still show mismatched basket totals, commission, VAT, or even MH basket ID vs Agency Prisa ID after change flows.

**Evidence:**
- `tc_getMHTC09a`: `totalInclVat` expected `136225.78` found `146941.10`
- `tc_getMHTC_MZN10b`: `MH basket ID (orBoxid) [6198] does not match Agency Prisa ID [6199]`

**Impact:** 8 failures

**Confidence:** Medium

---

## Failing Tests / Steps

- 86 failing validations grouped above across MH GET checks, MH patch steps, and Rialto follow-up GET checks.
