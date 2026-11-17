# Investigation Analysis — Build 191

**Source Report:** [build-191.md](../../../reports/build-failures/automationrunCAI-trunk/build-191.md)

## Summary

Build 191 was UNSTABLE: 15 of 199 scenarios failed or regressed (92.5% passed). Four additional scenarios were marked fixed by Jenkins.

## Root Cause

- Two MC order POST scenarios fail because variant 3 has no adspace.
- Adapter GET scenarios return HTTP 400 and HTTP 500; the latter includes a `NullPointerException`.
- BASE, CUSTOMER, and DWL API responses differ from their expected values.
- An MC order PATCH scenario supplies `ono=0`, which is rejected.
- Three print order POST scenarios fail with a lazy-initialization error for service-fee prices.

The Jenkins results provide these failure patterns but do not establish the underlying configuration, fixture, or implementation cause for the response mismatches.

## Affected Components

- ADAPTERS, BASE, CUSTOMER, DWL, MC ORDER, and PRINT ORDER API suites.
- Jenkins does not report the corresponding `.feature` filenames.

## Recommended Fix

- Verify the affected request data, fixtures, and reference values against the build environment.
- Investigate the reported adapter null dereference and print service-fee session error.

## Prevention

- Keep API test fixtures and expected response values aligned with the test environment.
- Retain these testcase IDs and error patterns when comparing subsequent runs.
