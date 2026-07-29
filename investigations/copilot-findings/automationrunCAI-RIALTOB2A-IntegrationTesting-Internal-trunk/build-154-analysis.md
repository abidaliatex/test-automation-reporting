# Root Cause Analysis — Build #154

**Source report:** [build-154.md](../../../reports/build-failures/automationrunCAI-RIALTOB2A-IntegrationTesting-Internal-trunk/build-154.md)

## Summary
- Build #154 (`automationrunCAI-RIALTOB2A-IntegrationTesting-Internal-trunk`) finished **UNSTABLE** on 2026-07-29 21:03 UTC.
- Jenkins test report shows 86 failures out of 514 tests (83.3% pass rate).
- Failures are concentrated in four clusters: missing `discountType`, recalculation mismatches, multi-line/date update drift, and rollback/identifier failures.

## Root Cause
- **Missing discount propagation:** `orders[*].printDetails.discountType` is repeatedly `null` where `RIALTO` is expected.
- **Calculation drift:** downstream assertions for `discountAmount`, `netAmount`, and related totals/status fields diverge.
- **Multi-line/date drift:** line ordering and `issueDate` assertions show stale or reordered values.
- **Flow-control errors:** rollback-only 500 responses and broken parameter/ID bindings (`uuid`, basket ID mismatch) interrupt end-to-end paths.

## Affected Components
- CASS GET/POST integration validation paths.
- Rialto -> MediaHouse discount/type mapping.
- Price summary and status recalculation logic.
- Multi-line order update and issue-date propagation handling.
- Request parameter binding and cross-system basket identifier synchronization.

## Recommended Fix
- Trace where `discountType` is mapped before GET response validation and ensure non-null propagation for Rialto-managed lines.
- Compare failing recalculation paths with passing baselines for totals and `statusFlags` updates.
- Validate deterministic ordering for multi-line updates and confirm `issueDate` persistence before follow-up GET checks.
- Investigate rollback causes in TC18/TC22/TC24 and enforce required `uuid` path parameter plus basket ID consistency checks.

## Prevention
- Add contract checks to fail fast when `discountType` is null for Rialto flows.
- Add targeted regression coverage for multi-line reorder/date-update scenarios.
- Add guardrails for required path params and cross-system ID parity before verification steps run.
