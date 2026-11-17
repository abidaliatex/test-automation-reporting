# Investigation Analysis — Build 161

**Source Report:** [build-161.md](../../../reports/build-failures/automationRunOrderCreation-trunk/build-161.md)

## Summary

Build 161 was UNSTABLE: 43 of 282 tests failed (84.8% passed).

## Root Cause

- Most failures were Selenium UI waits or intercepted clicks across order-entry workflows.
- Six online job notes cases could not access `onlinejobNotes.csv`.
- Two Sales Forecast checks could not find the expected order.
- Two Cucumber steps were undefined; one database case reported `Result set after last row`.
- One Job Notes assertion expected `Automation` but received an empty value.

The Jenkins results establish these failure patterns but do not determine their underlying configuration, data, or code causes.

## Affected Components

- Order-entry UI scenarios, online job notes test data, Sales Forecast scenarios, Cucumber step definitions, and the commission-order database test.
- Scenario titles and feature source lines are available; separate test-case IDs are not reported by Jenkins.

## Recommended Fix

- Check the UI state and overlays at the reported failed controls, verify the online job notes CSV path, and review the missing step definitions and reported data/database results.

## Prevention

- Validate test data and step-definition coverage before execution; retain feature source lines and failure details for comparison across builds.
