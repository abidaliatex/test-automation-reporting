# QA Triage Report — Build #261

**Source report:** [reports/build-failures/build-261.md](../../reports/build-failures/build-261.md)
**Analysis date:** 2026-07-05
**Analyst:** GitHub Copilot

---

## Build Summary

Build: automationrunCAI-RIALTOB2A-IntegrationTesting-Internal-trunk-demo #261
Total Tests: 14
Passed: 11
Failed: 3
Pass Rate: 78.6%

---

## Root Cause Groups

### discountType Not Propagated / Incorrect in MH After Rialto Order Creation

**Affected Features:**
- rialtoB2A(CASS)TestCase4.feature

**Affected Scenarios:**
- User perform CASS GET API — verify that order arrived in MH from Rialto - placement (tc_getMHTC03)
- User perform CASS GET API — verify that order arrived in MH from Rialto - placement - after change (tc_getMHTC03a)

**Failure Pattern:**
- tc_getMHTC03: `orders[0].printDetails.discountType` expected `[RIALTO]` found `[null]`
- tc_getMHTC03a: `orders[0].printDetails.discountType` expected `[NONE]` found `[RIALTO]`

Discount type is either missing entirely on initial order arrival, or not cleared after the placement update — the two checks produce contradictory actual values (`null` vs `[RIALTO]`), suggesting the field is not being reset correctly when a placement change is applied in MH.

**Evidence:**
- tc_getMHTC03: VAT inflated (`171598.78` vs expected `155683.63`) — a discount-driven recalculation difference
- tc_getMHTC03a: Commission unchanged at `8000.00` (expected `7750.00`) and totals differ by the same delta — consistent with a wrong discount type driving a wrong rate

**Impact:** 2 failures

**Confidence:** High

---

### Commission Rate and Order Financials Wrong in Agency After MH Placement Update

**Affected Features:**
- rialtoB2A(CASS)TestCase4.feature

**Affected Scenarios:**
- User perform CASS POST API — get order in Rialto using prisa id - check if placement updated (tc_getIntegrationRialto05b)

**Failure Pattern:**
`orderHeader.commissionAmount` expected `[7750.00]` found `[620.0]` — commission dropped from expected value to near zero, depth not updated (`372` found, `184` expected), `statusFlags` empty instead of `[PRELIMINARY]`.

**Evidence:**
- `commissionAmount` is `620.0` at both `orderHeader` and `orderAdDetails[0]` levels (consistent, so not a display bug — wrong value from the API)
- `orderAdDetails[0].depth` still `372` (original value), meaning the MH placement-change patch did not propagate back to Agency with the updated dimensions
- `statusFlags = []` — the order has no status in Agency, possibly indicating the sync event was not processed
- Numeric precision mismatches (`250000.00` vs `250000.0`) are formatting-only and not functional failures

**Impact:** 1 failure (9 assertion mismatches within the scenario)

**Confidence:** High

---

## Summary

All 3 failures are in the `rialtoB2A(CASS)TestCase4.feature` E2E flow for the placement-change scenario. The likely root cause is the API version bump from `v870` to `v880` (commit `4a04ddba` — "updated api version from 87 to 88") introducing changed behaviour in:

1. **discountType field** — no longer populated on the initial order in MH, and not cleared on update
2. **Commission / pricing calculations** — rates and totals diverge from test expectations under the new version
3. **Placement update sync** — depth and statusFlags not reflecting in Agency after MH patch
