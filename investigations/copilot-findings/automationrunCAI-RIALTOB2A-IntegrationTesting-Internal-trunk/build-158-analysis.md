# Root Cause Analysis — Build #158

**Source report:** [build-158.md](../../../reports/build-failures/automationrunCAI-RIALTOB2A-IntegrationTesting-Internal-trunk/build-158.md)

## Summary
- Build #158 (`automationrunCAI-RIALTOB2A-IntegrationTesting-Internal-trunk`) finished **UNSTABLE** on 2026-08-01 21:03 UTC.
- 67 failures out of 514 tests (87.0% pass rate) — 2 more than the prior build (#157, 65 failures; 69 reported; net change negligible).
- 4 newly regressed cases (TC7, TC22 ×2, TC23) alongside 60 previously failing tests now fixed.
- Dominant patterns are monetary precision drift, discount-type misrouting, magazine basket miscalculations, and multi-line sequencing/stale-state issues, all carried forward from build #157 with minor scope changes.

## Root Cause

- **Precision serialisation drift:** POST and verification steps fail because monetary fields (`discountAmount`, `priceNet`, `priceNetExComm`, `netAmount`) are returned with IEEE-754 floating-point residuals. TC7 newly regressed with this pattern. Root cause unchanged from #157.
- **Discount-type misrouting:** `discountType` continues to flip between `RIALTO`, `NONE`, and `null` across GET and MH verification steps. Incorrect discount application drives cascading mismatches in commission, VAT, and basket totals. TC5/TC9 POST steps also confirm discount is applied when the expected value is `0.0`.
- **Missing PRELIMINARY flag:** POST responses for TC1, TC3, TC4, TC6 continue to return an empty `statusFlags` list. Unchanged from #157; no fix has landed.
- **Order-line sequencing and stale state:** Multi-line responses return items in inconsistent order (packageId, paCode, plaCode); update/revert cycles leave stale `moduleCode`, `placementId`, and `issueDate` values. TC22 POST newly regressed with an ordering mismatch in `body.orderAdDetailUpdates.packageId`.
- **Magazine basket miscalculations:** Magazine scenarios (TC26–TC36) show `orderDiscount` applied when it should be zero, or applied at inflated amounts. Commission and `priceNet` diverge after size, date, or placement changes. Two cases (TC33, TC35) additionally show a MH basket ID vs. Agency Prisa ID mismatch, indicating the basket ID capture step fires before the ID is committed.
- **Transactional and routing failures:** TC18 and TC23 produce HTTP 500 rollback-only errors (TC23 is a new regression). TC24 still fails with a path-parameter binding error (`agencyPrisaId` supplied instead of `uuid`).

## Affected Components
- CASS POST/GET response serialisation for monetary fields.
- Discount-type mapping and basket price-summary calculation (Rialto ↔ MediaHouse).
- Order-state initialisation (`PRELIMINARY` flag) on POST.
- Multi-line order update/revert flows: sequencing, state propagation, and `body.orderAdDetailUpdates` construction.
- Magazine basket discount rule and commission rate selection after product/size/date/placement changes.
- MH basket ID capture timing relative to Agency Prisa ID assignment (TC33, TC35).
- Request builder for rollback/revert verification paths (TC24 `uuid` binding).

## Recommended Fix
- Round monetary response fields before serialisation; align the decimal scale used in verification payloads.
- Audit the discount-type routing logic for all CASS scenarios to ensure RIALTO/NONE/null is assigned consistently across POST, GET, and MH basket-summary paths.
- Investigate why `statusFlags` is empty on POST for basic CASS operations; check order-state initialisation.
- Stabilise multi-line ordering: sort response items by a canonical key before assertion, or fix the service to return a deterministic order.
- Review the magazine discount rule applied after size/date/placement changes — confirm that the discount amount is recalculated rather than carried over from a prior state.
- Ensure MH basket ID is captured only after the Agency Prisa ID is committed (TC33, TC35).
- Fix the TC24 verification request builder to pass `uuid` instead of `agencyPrisaId` as the path parameter.

## Prevention
- Add a regression check ensuring serialised monetary fields stay rounded to expected decimal precision.
- Add scenario coverage for `discountType` transitions across Rialto/MH update/revert flows.
- Assert `statusFlags` contains `[PRELIMINARY]` in all basic CASS POST responses.
- Add an ordering-invariant assertion helper for multi-item response arrays to avoid brittle positional checks.
- Validate magazine basket discount and commission after each change operation (size, date, placement, product) in isolation.
