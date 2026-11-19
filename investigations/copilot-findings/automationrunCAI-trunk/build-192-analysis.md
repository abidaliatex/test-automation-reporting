# Build 192 — Investigation Analysis

**Source report:** [build-192.md](../../../reports/build-failures/automationrunCAI-trunk/build-192.md)

## Summary

- Build 192 was **UNSTABLE**: 244 of 260 tests passed (93.85%); 16 failed.
- Failures span adapter/MC APIs, print orders, and response assertions against expected data.

## Root Cause

- Two MC order POST scenarios encountered a missing adspace for variant `3`.
- Three print order POST scenarios returned a service-fee lazy-initialization error (`FChargeses`, no session).
- Seven BASE, CUSTOMER, and DWL scenarios differed from expected test values or records. The report establishes mismatches, but not whether the cause is fixture drift or environment data.
- Other failures were adapter GET errors (including a `NullPointerException`), an MC PATCH request with `ono=0`, and a reversed suggested-services order.

## Affected Components

- `adapters.feature`, `base.feature`, `customerapi.feature`, `getcustomeractivitiesapi.feature`, `dwl.feature`, `mc_orders.feature`, and `print_orders.feature`.

## Recommended Fix

- Verify the build environment’s adspace mapping, service-fee loading, API test inputs, and expected fixtures against the observed failures.
- Investigate the adapter GET N400 separately; Jenkins provides no underlying error for that case.

## Prevention

- Keep test data and expected API responses aligned with the build environment, and retain regression coverage for adspace validation and service-fee loading.
