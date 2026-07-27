# Root Cause Analysis — Build #152

**Source report:** [build-152.md](../../../reports/build-failures/automationrunCAI-RIALTOB2A-IntegrationTesting-Internal-trunk/build-152.md)

---

## Summary

- Build #152 of `automationrunCAI-RIALTOB2A-IntegrationTesting-Internal-trunk` completed on 2026-07-27 21:03 UTC with status **UNSTABLE**.
- Jenkins reported 84 failures out of 514 tests (83.7% pass rate).
- The dominant pattern remains missing `discountType` propagation in MH/CASS verification steps, with widespread downstream pricing mismatches.
- Additional recurring failures come from the two-product MH parser cascade, date-change propagation drift, and a smaller set of rollback / identifier-wiring errors in TC22, TC24, and TC35.

---

## Root Cause

### 1. `discountType` is still missing for Rialto-managed flows
- MH/CASS verification steps continue to return `orders[*].printDetails.discountType = null` where the fixtures expect `RIALTO`.
- The same responses also show basket discount totals drifting, which suggests the missing field is tied to downstream pricing behaviour rather than being an isolated assertion issue.
- This affects both newspaper-style and magazine-style scenarios, so the defect is likely systemic in the shared integration mapping.

### 2. Financial fields are recalculated incorrectly after create/update flows
- The failing steps show large mismatches in `netAmount`, `discountAmount`, `commissionAmount`, `totalInclVat`, and `statusFlags` after successful API calls.
- Some failures are rounding-only (`66451.59999999998` vs `66451.6`), but many are materially wrong (`192192.0` vs `128531.37`), indicating a real calculation or stale-state problem.
- The breadth of affected scenarios suggests the issue is not isolated to one testcase fixture.

### 3. Two-product MH flows still break at the GET parser stage
- TC16–TC20 fail first with `Index 13 out of bounds for length 13`, which indicates an off-by-one or schema mismatch in the two-product MH response parser.
- Because the GET step never stores `odIds`, the POST step then fails with `No MH odIds found in TestContext`, and some downstream assertions read the wrong line-level values.

### 4. Date-change updates are not propagating consistently
- Date-change flows show `issueDate` remaining on the old value after MH or Rialto updates.
- Evidence appears in TC16, TC27, and TC35, where the updated issue date is asserted in request payload or follow-up verification but the response still carries the previous value.

### 5. TC22 / TC24 / TC35 contain additional flow-control defects
- TC22 and TC24 hit server-side `rollback-only` transaction failures, so the intended update/revert never completes.
- TC24 then follows with a verification step that provides `agencyPrisaId` but leaves `uuid` undefined.
- TC35 ends with a cross-system identifier mismatch: MH basket ID `6904` vs Agency Prisa ID `6905`.

---

## Affected Components

- **Rialto/CASS discount mapping** — `printDetails.discountType` is absent in responses where `RIALTO` is expected.
- **Price and status recalculation** — totals and status fields drift after create/update operations.
- **Two-product MH parser / context storage** — GET-step parsing prevents `odIds` from being captured for later POST checks.
- **Date propagation logic** — updated `issueDate` values are not reflected consistently across verification steps.
- **Flow-control / parameter wiring** — rollback handling and the TC24 `uuid` binding remain unstable.
- **Cross-system identifier sync** — MH and Agency basket/order identifiers diverge in TC35.

---

## Recommended Fix

- Trace where `discountType` is populated for Rialto-originated orders before MH/CASS response assertions run.
- Compare the price-calculation path for failing flows against a passing baseline to determine whether values are stale, rounded incorrectly, or derived from the wrong discount state.
- Fix the two-product MH parser bounds/schema handling so `odIds` are always stored before POST-step assertions execute.
- Re-check date-update propagation for TC16/TC27/TC35 and verify the updated `issueDate` is persisted before follow-up GETs.
- Investigate the TC22/TC24 transaction rollback cause and correct the TC24 verification step to bind `uuid` instead of only `agencyPrisaId`.

---

## Prevention

- Add a contract-level assertion for Rialto-managed orders that rejects `discountType = null` before downstream amount checks run.
- Add a schema/bounds guard for two-product MH GET payload parsing.
- Add a targeted regression for date-change flows that verifies `issueDate` across both the update response and the subsequent GET.
- Add a lightweight step-validation check that fails fast when required path parameters such as `uuid` are missing.
