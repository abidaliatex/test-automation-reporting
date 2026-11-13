# Investigation Analysis — Build 190

**Source Report:** [build-190.md](../../../reports/build-failures/automationrunCAI-trunk/build-190.md)

## Summary

Build 190 was UNSTABLE: 15 of 199 tests failed (92.5% passed). Failures span adapter, order, BASE, CUSTOMER, and DWL API tests.

## Root Cause

- Two order POST tests are rejected because variant 3 has no matching adspace.
- Adapter GET tests show an HTTP 400 response and a separate `NullPointerException`.
- BASE, CUSTOMER, and DWL failures are response-versus-expectation mismatches.
- An MC order PATCH request supplies `ono=0`.
- Three print order POST tests hit a lazy-initialization error for service-fee prices.

The Jenkins results establish these failure patterns but do not identify their underlying configuration, data, or code changes.

## Affected Components

- ADAPTERS, BASE, CUSTOMER, DWL, MC ORDER, and PRINT ORDER API test suites.
- Feature filenames are not included in the Jenkins test results.

## Recommended Fix

- Check the failing request inputs and expected fixture data against the build environment.
- Investigate the mapped-adspace null dereference and print service-fee session handling.

## Prevention

- Validate API test fixtures and required reference data before running the suite.
- Retain the testcase IDs and response evidence when comparing subsequent builds.
