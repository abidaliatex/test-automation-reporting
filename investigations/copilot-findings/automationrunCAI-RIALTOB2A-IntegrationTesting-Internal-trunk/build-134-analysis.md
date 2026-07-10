# Build 134 Root Cause Analysis

Source report: [build-134.md](../../../reports/build-failures/automationrunCAI-RIALTOB2A-IntegrationTesting-Internal-trunk/build-134.md)

## Summary

- Build `automationrunCAI-RIALTOB2A-IntegrationTesting-Internal-trunk` #134 finished `UNSTABLE` with 86 failures out of 513 tests (83.2% pass rate).
- The build checked out revision `4a04ddba1e4e5809017f1f7cf91b06e93e3c19dd` (`updated api version from 87 to 88`) and ran against `.../api/880/v1`.
- Most failures are not new: 75 failures were already failing since build `99`, 4 since `107`, and 3 other failures since `130/133`; only 4 failures are new regressions in build `134`.
- The failures cluster into five repeatable patterns rather than a single outage: MH `discountType`/pricing drift, state-update/order drift, two-product MH indexing/context loss, malformed follow-up requests, and a small residual set of pricing/ID mismatches.

## Root Cause

- **Primary pattern (38 failures):** MediaHouse validation responses no longer match fixture expectations for `discountType`, commission, VAT, and totals. The clearest repeated symptom is `discountType expected [RIALTO] found [null]`.
- **Secondary pattern (23 failures):** After change operations, downstream responses do not reflect the expected issue date, placement, size/module code, package ordering, or `PRELIMINARY` status flag. In several cases the data appears present but in a different order than expected.
- **Cascading execution failures (11 failures):** Two-product MH validations hit `Index 13 out of bounds for length 13`, which prevents storing `odIds`; subsequent patch steps then fail with `No MH odIds found in TestContext`.
- **Request-construction failures (6 failures):** TC23/24/29 contain malformed follow-up requests (`undefined uuid`, `undefined agencyPrisaId`, redundant path params) and one rollback-only server error.
- **Residual mismatches (8 failures):** A smaller set of post-change validations still fail on totals, commission, or identity correlation without the dominant `discountType=null` signature.

## Affected Components

- MediaHouse basket-order GET validations across MH and magazine scenarios
- Rialto follow-up GET validations after date/size/placement changes
- Patch-step payload construction for MH change flows
- Shared test context hand-off for MH `odIds`

## Recommended Fix

- Re-baseline the failing suites in this order:
  - Fix the MH two-product indexing/context issue first, because it creates direct downstream failures.
  - Review contract drift introduced around API v88 for `discountType`, pricing totals, and status flags.
  - Verify whether array ordering in patch payloads and follow-up GET responses is stable or whether the assertions need order-independent matching.
  - Correct the malformed TC23/24/29 follow-up requests before re-running those flows.

## Prevention

- Add a lightweight smoke check that validates one MH basket response and one Rialto follow-up response immediately after API-version changes.
- Fail fast when MH `odIds` are not captured, so later patch validations are marked as blocked instead of producing secondary errors.
- Separate order-sensitive assertions from value assertions so ordering drift is easier to detect and diagnose.
