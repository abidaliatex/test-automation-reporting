# Build 324 — Root Cause Analysis

**Source Report:** [build-324.md](../../../reports/build-failures/automationrunCAI-RIALTOB2A-IntegrationTesting-Internal-trunk-demo/build-324.md)
**Job:** automationrunCAI-RIALTOB2A-IntegrationTesting-Internal-trunk-demo
**Date:** 2026-07-27

---

## Build Summary

Build: 324
Total Tests: 14
Passed: 11
Failed: 3
Pass Rate: 78.6%

---

## Root Cause Groups

## Missing `discountType` in MediaHouse GET response

**Affected Features:**
- MediaHouse order verification flow (`MediaHouse/getMHB2A.csv`)

**Affected Scenarios:**
- verify order created in Rialto from MH (`tc_getMHTC01`)
- get order created in Rialto from MH - after change (`tc_getMHTC01a`)

**Failure Pattern:**
`orders[0].printDetails.discountType expected [[RIALTO/NONE]] but found [[null]]`

**Evidence:**
- `tc_getMHTC01` fails on `orders[0].printDetails.discountType expected [[RIALTO]] but found [[null]]`
- `tc_getMHTC01a` also fails on `orders[0].printDetails.discountType expected [[NONE]] but found [[null]]`
- Both failing since build 322 — persistent regression not yet resolved

**Impact:** 2 failures

**Confidence:** High

## Incorrect pricing/discount totals after order change flow

**Affected Features:**
- MediaHouse post-change basket validation (`MediaHouse/getMHB2A.csv`)
- Rialto order retrieval validation (`Rialto/RialtoB2A/getRialtoB2A.csv`)

**Affected Scenarios:**
- get order created in Rialto from MH - after change (`tc_getMHTC01a`)
- get order in rialto using risa id - check if issue date updated (`tc_getIntegrationRialto02`)

**Failure Pattern:**
`Expected zero-discount/full-price totals but response contains discountAmount=63660.63 and reduced net totals`

**Evidence:**
- `tc_getMHTC01a`: `orderBasketPriceSummary.orderDiscount expected [0.00] but found [63660.63]` and `netPrice expected [192192.00] but found [128531.37]`
- `tc_getIntegrationRialto02`: `discountAmount expected [0.0] but found [63660.63]`, `orderHeader.priceNetExComm expected [192192.0] but found [128531.37]`, and `orderHeader.statusFlags expected [[PRELIMINARY]] but found [[]]`
- Identical delta values across both scenarios (`63660.63`, `128531.37`) confirm a shared pricing-state inconsistency
- Failing since build 322 — 3 consecutive builds affected (322, 323 not in report, 324)

**Impact:** 2 failures

**Confidence:** High

---

## Summary

- Build 324 is unstable due to three assertion failures in MH/Rialto order validation — same failures as build 322.
- Two failures share missing `discountType`; two failures share identical discount/price drift values (`63660.63`, `128531.37`).

## Root Cause

- The MH/Rialto response payloads carry inconsistent discount metadata and recalculated totals after the order-change flow.
- The `discountType` field is returning `null` instead of the expected enum value (`RIALTO`/`NONE`), indicating the field is not being populated in the backend response.
- The recurring numeric deltas across two scenarios point to a single pricing-state inconsistency (possibly an unintended discount being applied in the post-change path).

## Affected Components

- MediaHouse basket order response mapping (`orders[0].printDetails.*`, `orderBasketPriceSummary.*`)
- Rialto order header/detail totals and status flag mapping (`orderHeader.*`, `orderAdDetails[0].*`)

## Recommended Fix

- Compare payload generation for the passing create flow vs failing post-change/get flows for `discountType`, `discountAmount`, and net total fields.
- Validate whether an unintended discount rule is applied in post-change path.
- Restore/verify `orderHeader.statusFlags` population for updated-order retrieval.

## Prevention

- Add guard assertions in API contract checks for non-null `discountType` and consistent price/discount arithmetic across MH and Rialto GET validations.
