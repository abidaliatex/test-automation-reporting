# Root Cause Analysis — Build 274

**Source Report:** [build-274.md](../../reports/build-failures/automationrunCAI-RIALTOB2A-IntegrationTesting-Internal-trunk-demo/build-274.md)

---

## Summary

Build 274 of `automationrunCAI-RIALTOB2A-IntegrationTesting-Internal-trunk-demo` is UNSTABLE with 3 of 14 tests failing (78.6% pass rate). All three failures are in the `rialtoB2A (CASS TC4 Change Placement)` feature and have persisted since build 246. Failures split into two groups: MediaHouse discount/pricing mismatches and Rialto post-change placement/commission/status mismatches.

---

## Root Cause

### Group 1 — MediaHouse Discount Type and Pricing Mismatch

The MediaHouse API returns `discountType = null` (pre-change) and `discountType = RIALTO` (post-change) where the test fixtures expect `RIALTO` and `NONE` respectively. This indicates the discount type lifecycle is not being updated correctly when the placement is changed via the MH PATCH call. The pricing totals (VAT, totalInclVat, commission) diverge as a downstream consequence of the wrong discount type being applied during price calculation.

### Group 2 — Rialto Commission, Depth, and Status Flag Mismatch

After the MH PATCH triggers a placement change back to Rialto, the Rialto order is not fully updated:
- `commissionAmount` returns `620.0` instead of `7750.00` — commission recalculation is incorrect or not triggered.
- `depth` returns `372` instead of `184` — the placement dimension is not updated.
- `statusFlags` is empty instead of `[PRELIMINARY]` — the order is not being set back to PRELIMINARY status after the change.
- Price fields (`priceGross`, `priceNetExComm`, `priceNet`) show single-decimal precision (`250000.0`) vs the two-decimal format expected by the fixture — possibly a serialization/formatting issue in the API response.

These failures have been continuous since build 246, suggesting an unresolved backend regression in the placement-change workflow.

---

## Affected Components

- **MediaHouse GET API** (`getMHB2A.csv` — `tc_getMHTC03`, `tc_getMHTC03a`)
- **Rialto GET API** (`getRialtoB2A.csv` — `tc_getIntegrationRialto05b`)
- **Placement change flow** — MH PATCH → Rialto sync

---

## Recommended Fix

- Investigate why `discountType` is not propagated correctly after placement creation (`null` instead of `RIALTO`) and after placement change (`RIALTO` instead of `NONE`).
- Check the commission recalculation logic triggered on placement change — `commissionAmount` is `620.0` vs expected `7750.00`.
- Verify that `statusFlags` is set to `[PRELIMINARY]` when a placement change is processed.
- Confirm whether the `depth` field is being overwritten correctly in the Rialto order on change.
- Review API response serialization for numeric fields to ensure consistent two-decimal formatting.

---

## Prevention

- Add contract tests or schema validation on `discountType` and `statusFlags` transitions in the placement-change workflow.
- Ensure commission recalculation is covered by unit tests for the placement-change trigger path.
- Consider adding a regression test guard on price field decimal formatting in Rialto API responses.
