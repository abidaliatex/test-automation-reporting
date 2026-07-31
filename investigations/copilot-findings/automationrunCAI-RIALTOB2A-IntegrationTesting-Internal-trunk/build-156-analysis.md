# Root Cause Analysis — Build #156

**Source report:** [build-156.md](../../../reports/build-failures/automationrunCAI-RIALTOB2A-IntegrationTesting-Internal-trunk/build-156.md)

## Summary
- Build #156 (`automationrunCAI-RIALTOB2A-IntegrationTesting-Internal-trunk`) finished **UNSTABLE** on 2026-07-31 12:22 UTC.
- 65 failures were reported out of 514 tests (87.4% pass rate).
- The dominant patterns are monetary precision drift, discount/pricing-rule regressions, order-line state mismatches, rollback/path-parameter failures, and one basket ID synchronisation error.

## Root Cause
- **Precision serialisation drift:** Several POST and verification steps fail only because monetary fields such as `discountAmount`, `priceNetExComm`, and `netAmount` are returned with floating-point residuals instead of stable decimal values.
- **Discount/pricing-rule regression:** Multiple GET and MediaHouse verification steps show `discountType` switching between `RIALTO`, `NONE`, and `null`, with matching drift in `orderDiscount`, `commission`, `vat`, and totals. This points to a pricing or discount-mapping regression rather than isolated assertion noise.
- **State propagation / ordering issues:** Multi-line scenarios return order lines in a different sequence than expected, or preserve old placement/date/module values after updates and reverts.
- **Transactional and routing failures:** TC18 and TC23 hit rollback-only HTTP 500 responses, and TC24 fails because `uuid` is missing while `agencyPrisaId` is passed as a redundant path parameter.
- **Cross-system ID mismatch:** TC35 shows the MediaHouse basket ID (`orBoxid`) diverging from the Agency Prisa ID used by the verification step.

## Affected Components
- CASS POST/GET response serialisation for monetary fields.
- Discount-type mapping and basket price-summary calculation between Rialto and MediaHouse.
- Multi-line order update/revert flows and their ordering/state propagation.
- Request construction for rollback/revert verification paths.
- Basket ID handoff between MediaHouse and Agency Prisa.

## Recommended Fix
- Round monetary response fields before serialisation and confirm the same scale is used in verification payloads.
- Review the latest `discountType` and discount-calculation changes for RIALTO/NONE/null handling in basket summaries and order print details.
- Trace ordering/state propagation in TC15/TC22/TC24-style multi-line updates to confirm the expected line order and updated placement/date/module values survive each step.
- Inspect the failing rollback flows and the TC24 verification request builder to confirm `uuid` is preserved after revert operations.
- Recheck the ID capture step used before the TC35 MediaHouse verification.

## Prevention
- Add a regression check that serialised monetary fields stay rounded to the expected decimal precision.
- Add scenario coverage for `discountType` transitions and basket totals across Rialto and MediaHouse update/revert flows.
- Validate required shared identifiers (`uuid`, Agency Prisa ID, MediaHouse basket ID) before dependent verification steps run.
