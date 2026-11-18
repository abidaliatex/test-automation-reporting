# Build 162 — Investigation Analysis

**Source report:** [build-162.md](../../../reports/build-failures/automationRunReports-trunk/build-162.md)

## Summary

- Build 162 was **UNSTABLE**: 51 of 53 tests passed (96.2%).
- Two scenarios failed with distinct symptoms; Jenkins did not expose their scenario names or test case IDs.

## Root Cause

- **Offer report:** The generated value differed from the expected value. The assertion identifies a data mismatch, but does not establish why the values differed.
- **Stock Orders filter save:** The test timed out waiting for the dialog's OK button. Jenkins evidence identifies the failed wait, but not why the button was unavailable.

## Affected Components

- `report_offer.feature` — offer report data verification.
- `reports_stockoforders.feature` — saving a created filter as CSV.

## Recommended Fix

- Verify the offer report's expected and generated test data.
- Check the stock-orders dialog state and button readiness when the save action runs.

## Prevention

- Keep report test data deterministic and dialog readiness checks aligned with the UI state.
