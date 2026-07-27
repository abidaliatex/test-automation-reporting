# Build 323 — Root Cause Analysis

**Source Report:** [build-323.md](../../../reports/build-failures/automationrunCAI-RIALTOB2A-IntegrationTesting-Internal-trunk-demo/build-323.md)

---

## Build Summary

Build: 323  
Total Tests: 14  
Passed: 10  
Failed: 4  
Pass Rate: 71.4%

---

## Root Cause Groups

## Pricing/discount state mismatch after MH-to-Rialto order flow

**Affected Features:**
- MediaHouse/getMHB2A.csv
- Rialto/RialtoB2A/getRialtoB2A.csv

**Affected Scenarios:**
- verify order created in Rialto from MH (tc_getMHTC01)
- get order created in Rialto from MH - after change (tc_getMHTC01a)
- get order in rialto using risa id - check if issue date updated (tc_getIntegrationRialto02)

**Failure Pattern:**
`discountType expected [RIALTO/NONE] found [null]` and related totals expected full price found discounted values (`discountAmount=63660.63`, `netPrice=128531.37`).

**Evidence:**
- `tc_getMHTC01`: `orders[0].printDetails.discountType expected [[RIALTO]] but found [[null]]`
- `tc_getMHTC01a`: `orders[0].printDetails.discountType expected [[NONE]] but found [[null]]`, `orderDiscount expected [0.00] but found [63660.63]`
- `tc_getIntegrationRialto02`: `discountAmount expected [0.0] but found [63660.63]`, `priceNetExComm expected [192192.0] but found [128531.37]`

**Impact:** 3 failures

**Confidence:** High

## Issue-date mismatch in patch update response

**Affected Features:**
- MediaHouse/patchMHB2A.csv

**Affected Scenarios:**
- the scenario with one order with only one order line and where the Media house changes the date in the order (tc_patchIntegrationMH01)

**Failure Pattern:**
`issueDate expected [2026-07-21] found [2026-12-21]`

**Evidence:**
- `tc_patchIntegrationMH01`: `body.orderAdDetailUpdates[0].issueDate expected [2026-07-21] but found [2026-12-21]`

**Impact:** 1 failure

**Confidence:** High

## Summary
- Build 323 is unstable due to 4 assertion failures grouped into 2 patterns.
- 3 failures are concentrated on discount/pricing/state fields; 1 failure is isolated to issue-date value drift.

## Root Cause
- Order retrieval/update payloads may be returning inconsistent pricing/discount state and null discount type for MH/Rialto verification paths.
- Patch update flow may be returning an unexpected transformed issue date.

## Affected Components
- MH order retrieval assertions (`orders[0].printDetails.*`, `orderBasketPriceSummary.*`)
- Rialto order retrieval assertions (`orderHeader.*`, `orderAdDetails[0].*`)
- MH patch response field (`body.orderAdDetailUpdates[0].issueDate`)

## Recommended Fix
- Compare response payload values before and after patch/update flow for `discountType`, discount totals, and `issueDate` mapping.
- Validate whether date transformation logic or test data in `patchMHB2A.csv` changed for this build.

## Prevention
- Add contract checks that fail fast on null `discountType` and unexpected date transformations before downstream total-field assertions execute.
