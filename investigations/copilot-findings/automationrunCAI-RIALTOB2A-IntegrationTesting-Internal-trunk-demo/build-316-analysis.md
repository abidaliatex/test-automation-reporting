# Build 316 — Root Cause Analysis

**Source Report:** [build-316.md](../../reports/build-failures/automationrunCAI-RIALTOB2A-IntegrationTesting-Internal-trunk-demo/build-316.md)
**Job:** automationrunCAI-RIALTOB2A-IntegrationTesting-Internal-trunk-demo
**Date:** 2026-07-26
**Failing Since:** Build 314

---

## Build Summary

Build: 316
Total Tests: 15
Passed: 12
Failed: 3
Pass Rate: 80%

---

## Root Cause Groups

---

## Root Cause 1: discountType Not Propagated from Rialto to MediaHouse

**Affected Features:**
- rialtoB2A — CASS TC29 Magazine (change to Uppslag/Spread/Panorama)

**Affected Scenarios:**
- MEDIAHOUSE - Verify original full-page order state in MediaHouse (TC29 / tc_getMHTC_MZN04a)

**Failure Pattern:**
`orders.printDetails.discountType expected [[RIALTO]] but found [[null]]`

**Evidence:**
- The `discountType` field is absent (null) in the MH order response
- The order was created from Rialto; the expected value `RIALTO` is the source-system discriminator
- Failure started at build 314, suggesting a regression in the Rialto→MH mapping layer

**Impact:** 1 failure

**Confidence:** High

---

## Root Cause 2: Order Revert State Not Applied — Size/Pricing Fields Retain Uppslag Values

**Affected Features:**
- rialtoB2A — CASS TC29 Magazine (change to Uppslag/Spread/Panorama)

**Affected Scenarios:**
- MEDIAHOUSE - Verify updated MediaHouse basket state (TC29 / tc_getMHTC_MZN04b)
- RIALTO - Verify Rialto reflects the reverted full-page state (TC29 / tc_getIntegrationRialtoMZN04b)

**Failure Pattern:**
```
orders.printDetails.plaCode expected [HALVLIGG] but found [UPPSLAG]
orders.printDetails.width expected [1] but found [2]
orders.printDetails.depth expected [146] but found [297]
orders.printDetails.grossAmount expected [5000.0] but found [11000.0]
orderAdDetails.commissionAmount expected [155.0] but found [68.2]
```

**Evidence:**
- Both MH and Rialto return `UPPSLAG` dimensions and pricing (`width=2`, `depth=297`, `grossAmount=11000`) instead of the original `HALVLIGG` values (`width=1`, `depth=146`, `grossAmount=5000`)
- Commission diverges between systems: MH reports 550.00, Rialto reports 68.2; neither matches the expected 155.00
- The revert flow (MH patch → Rialto verification) ran without API errors, indicating the revert request was accepted but possibly not applied or propagated
- Failure started at build 314 across both MH and Rialto verification steps; possibly a shared service or propagation logic regression

**Impact:** 2 failures (18 + 11 field mismatches)

**Confidence:** High

---

## Summary

- **Root Cause 1** — Missing `discountType` field mapping from Rialto to MediaHouse; possibly dropped during a serialization or mapping change introduced around build 314.
- **Root Cause 2** — Order revert after Uppslag format change is not being applied; both Rialto and MediaHouse retain the Uppslag dimensions and pricing post-revert. May indicate a broken revert/update API call or an async propagation failure affecting order state synchronisation.

## Affected Components

- Rialto → Agency (B2A) integration layer
- MediaHouse order basket API (`/getMHB2A`)
- `orders.printDetails` field mapping (discountType, plaCode, width, depth, amounts)
- Commission calculation pipeline

## Recommended Fix

- Investigate changes to the Rialto→MH field mapping introduced at or before build 314, specifically the `discountType` serialisation path.
- Check the revert/undo flow in the MH PATCH endpoint (`tc_patchIntegrationMH_MZN03`) to confirm it returns the original `HALVLIGG` record; trace whether the updated state is propagated back to Rialto.

## Prevention

- Add contract tests for `discountType` and `plaCode` field presence in the Rialto→MH mapping.
- Monitor commission calculation consistency between systems after format-change operations.
