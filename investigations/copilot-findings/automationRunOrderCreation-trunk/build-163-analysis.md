# Build 163 — Investigation Analysis

**Source report:** [build-163.md](../../../reports/build-failures/automationRunOrderCreation-trunk/build-163.md)

## Summary

- Build 163 was **UNSTABLE**: 241 of 282 tests passed (85.5%); 41 failed.
- Failures span UI visibility/clickability, missing test data, empty result assertions, and undefined steps.

## Root Cause

- Jenkins directly reports the failed selector waits, intercepted save clicks, missing `onlinejobNotes.csv`, empty assertions/results, and two undefined Cucumber steps.
- The underlying application or environment cause for the UI and empty-data failures is not established by the available logs.

## Affected Components

- Order creation: `createorder.feature`, `toporder.feature`, `duplicateOrders.feature`
- Job notes and online jobs: `jobNotes.feature`, `onlineJobNotes.feature`, `onlineJob.feature`
- Sales Forecast, revised orders, commission orders, and placement codes.

## Recommended Fix

- Verify the failed controls and page state at the recorded UI waits; ensure the Online Job Notes CSV is available to the job.
- Implement the two undefined steps and check the reported empty query/assertion inputs before rerunning affected cases.

## Prevention

- Validate required test data and step definitions before execution.
- Keep UI readiness checks aligned with the controls used by each scenario.
