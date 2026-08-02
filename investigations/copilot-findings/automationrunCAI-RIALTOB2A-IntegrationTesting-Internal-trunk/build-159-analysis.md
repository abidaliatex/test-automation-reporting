# Root Cause Analysis — Build #159

**Source report:** [build-159.md](../../../reports/build-failures/automationrunCAI-RIALTOB2A-IntegrationTesting-Internal-trunk/build-159.md)

## Summary
- Build #159 (`automationrunCAI-RIALTOB2A-IntegrationTesting-Internal-trunk`) finished **UNSTABLE** on 2026-08-02 21:03 UTC.
- 71 failures out of 514 tests (86.2% pass rate) — 4 more than build #158 (67 failures).
- All six failure patterns from #158 persist unchanged; no fixes have landed between builds.
- New regression: TC35 RIALTO step now shows a stale `placementId`/`issueDate` mismatch not present in #158.

## Root Cause

- **Precision serialisation drift:** POST and verification steps continue to fail because monetary fields (`discountAmount`, `priceNet`, `priceNetExComm`, `netAmount`) are serialised with IEEE-754 floating-point residuals. Identical pattern to #158 with the same affected TCs (TC1, TC3–TC6, TC9, TC11, TC14, TC15, TC21, TC23, TC24). Root cause unchanged.
- **Discount-type misrouting:** `discountType` still flips incorrectly between `RIALTO`, `NONE`, and `null` across CASS GET and MH basket-summary responses. Discount is being applied on POST when expected to be zero (TC1, TC5, TC9), confirming the discount calculation runs before the intended skip condition. Commission, VAT, and basket totals cascade accordingly.
- **Missing PRELIMINARY flag:** `orderHeader.statusFlags` returns `[]` on POST for TC3, TC4, TC6. Pattern identical to #158; no fix present.
- **Order-line sequencing and stale state:** Multi-line responses (packageId, paCode, plaCode, netAmount) return in non-deterministic order. Update/revert cycles leave stale values (TC18 moduleCode, TC22–TC24 paCode/netAmount, TC35 placementId/issueDate). TC35 RIALTO step is a new regression versus #158.
- **Magazine basket miscalculations:** `orderDiscount` is applied at wrong amounts or when it should be zero across TC26–TC36. Commission and `priceNet` diverge after size/date/placement changes. TC35 also shows an integration mismatch where MH basket ID does not match Agency Prisa ID, indicating the basket ID is captured before the Agency Prisa ID is committed.
- **Transactional and routing failures:** TC18 POST and TC24 revert step return HTTP 500 rollback-only. TC24 verification still passes `agencyPrisaId` instead of `uuid` as the path parameter.

## Affected Components
- CASS POST/GET response serialisation for monetary fields.
- Discount-type mapping and basket price-summary calculation (Rialto ↔ MediaHouse).
- Order-state initialisation (`PRELIMINARY` flag) on POST.
- Multi-line order update/revert flows: response ordering, state propagation.
- Magazine basket discount rule and commission rate selection after product/size/date/placement changes.
- MH basket ID capture timing relative to Agency Prisa ID assignment (TC35).
- Request builder for rollback/revert verification paths (TC24 `uuid` binding).

## Recommended Fix
- Round monetary response fields to the expected decimal scale before serialisation.
- Audit discount-type routing logic to ensure `RIALTO`/`NONE`/`null` is assigned consistently across POST, GET, and MH basket-summary paths; prevent discount from being applied when the skip condition should hold.
- Investigate why `statusFlags` is empty on basic CASS POST responses (TC3, TC4, TC6).
- Sort multi-line response arrays by a canonical key before returning, or update assertions to be order-invariant.
- Review magazine discount recalculation logic — confirm discount amount is recomputed rather than carried over from prior state after product/size/date/placement changes.
- Ensure MH basket ID is captured only after Agency Prisa ID is committed (TC35).
- Fix TC24 verification request builder to supply `uuid` instead of `agencyPrisaId` as the path parameter.

## Prevention
- Add a regression check ensuring serialised monetary fields stay rounded to expected decimal precision.
- Add scenario coverage for `discountType` transitions across Rialto/MH update/revert flows.
- Assert `statusFlags` contains `[PRELIMINARY]` in all basic CASS POST responses.
- Add an ordering-invariant assertion helper for multi-item response arrays.
- Validate magazine basket discount and commission after each change operation in isolation.
