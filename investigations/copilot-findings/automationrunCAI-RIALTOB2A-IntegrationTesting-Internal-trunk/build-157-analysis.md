# Root Cause Analysis — Build #157

**Source report:** [build-157.md](../../../reports/build-failures/automationrunCAI-RIALTOB2A-IntegrationTesting-Internal-trunk/build-157.md)

## Summary
- Build #157 (`automationrunCAI-RIALTOB2A-IntegrationTesting-Internal-trunk`) finished **UNSTABLE** on 2026-07-31 21:03 UTC.
- 69 failures out of 514 tests (86.6% pass rate) — 4 more than the prior build (#156, 65 failures).
- Dominant patterns are monetary precision drift, discount/pricing-rule regressions, order-line state/sequencing mismatches, and rollback/path-parameter failures. The MH basket ID vs. Agency Prisa ID mismatch (TC32–TC35) is newly widespread compared to build-156.

## Root Cause
- **Precision serialisation drift:** POST and verification steps fail because monetary fields (`discountAmount`, `priceNetExComm`, `netAmount`, `priceNet`) are returned with IEEE-754 floating-point residuals instead of stable rounded values.
- **Discount/pricing-rule regression:** Multiple GET and MediaHouse verification steps show `discountType` switching between `RIALTO`, `NONE`, and `null`, with matching drift in `orderDiscount`, `commission`, `vat`, and totals. Incorrect `discountAmount` values (0.0 vs. 63660.63) indicate the discount rule itself is being applied inconsistently.
- **Missing PRELIMINARY flag:** POST responses for basic CASS operations (TC1–TC6) return an empty `statusFlags` list rather than `[PRELIMINARY]`, suggesting an order-state initialisation defect.
- **Order-line sequencing and stale state:** Multi-line scenarios return items in unpredictable order, and stale `moduleCode`/`placementId` values survive update/revert cycles. Four magazine TCs (TC32–TC35) show a systematic MH basket ID vs. Agency Prisa ID mismatch, pointing to a broken ID capture or handoff step.
- **Transactional and routing failures:** TC18 and TC24 produce HTTP 500 rollback-only errors; TC24 also fails because `uuid` is absent while `agencyPrisaId` is passed as a redundant path parameter.

## Affected Components
- CASS POST/GET response serialisation for monetary fields.
- Discount-type mapping and basket price-summary calculation between Rialto and MediaHouse.
- Order-state initialisation (PRELIMINARY flag) on POST.
- Multi-line order update/revert flows and their sequencing/state propagation.
- MediaHouse basket ID capture and handoff to Agency Prisa ID (magazine TC32–TC35).
- Request construction for rollback/revert verification paths (TC24 `uuid` binding).

## Recommended Fix
- Round monetary response fields before serialisation and align the decimal scale used in verification payloads.
- Review the latest `discountType` and discount-calculation logic for RIALTO/NONE/null handling; confirm the discount rule is applied consistently across POST, GET, and MH basket-summary paths.
- Investigate why `statusFlags` is empty on POST; check order-state initialisation logic for basic CASS operations.
- Trace the magazine flow that sets `orBoxid` to verify the MH basket ID is captured before the Agency Prisa ID lookup (TC32–TC35).
- Fix the TC24 verification request builder to pass `uuid` instead of `agencyPrisaId` as the path parameter.

## Prevention
- Add a regression check ensuring serialised monetary fields stay rounded to the expected decimal precision.
- Add scenario coverage for `discountType` transitions and basket totals across Rialto/MH update/revert flows.
- Validate that `statusFlags` contains `[PRELIMINARY]` in all basic CASS POST responses.
- Assert that the captured MH basket ID matches the Agency Prisa ID before dependent magazine verification steps run.
