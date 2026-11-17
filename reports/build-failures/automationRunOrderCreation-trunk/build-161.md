# Build Failure Report

## Build Summary

Build: [161](https://crossadv.atex.com/jenkins/job/automationRunOrderCreation-trunk/161/) | Date: 2026-11-16 19:36:03 UTC | Status: UNSTABLE  
Total Tests: 282 | Passed: 239 | Failed: 43 | Pass Rate: 84.8%

---

## Root Cause Groups

Jenkins provides scenario titles and feature source lines, but no separate TC identifiers.

## Selenium UI controls unavailable or intercepted

**Affected Features:**
- `createorder.feature`, `jobNotes.feature`, `duplicateOrders.feature`
- `onlineJob.feature`, `revisedOrder.feature`, `PrintProductionCode.feature`, `toporder.feature`

**Affected Scenarios:**
- User Creates new print order (`createorder.feature`: 1384, 1432, 1458, 1483, 1531, 1583, 1632, 1726, 1778, 1859, 1886, 1937, 1991)
- User Testing Job Notes (`jobNotes.feature`: 33, 69, 82, 102, 115, 133, 146, 164)
- User Creates Module (`duplicateOrders.feature`: 31); User Creates new order (`duplicateOrders.feature`: 64)
- User verify online jobs (`onlineJob.feature`: 158)
- User Creates new online order (`revisedOrder.feature`: 41, 55)
- User creates new order with production code (`PrintProductionCode.feature`: 45, 68)
- User Creates new order (`toporder.feature`: 38, 39, 63, 64, 65)

**Failure Pattern:** Selenium waits time out on expected controls, or clicks are intercepted by another element.  
**Evidence:** 24 visibility/clickability timeouts (11 waiting for the material-accordion button); 7 intercepted clicks (5 on Save and 2 on Add Production Code).  
**Impact:** 31 failures  
**Confidence:** High for the observed UI failures; underlying cause is not established.

## Online job notes test data unavailable

**Affected Features:**
- `onlineJobNotes.feature`

**Affected Scenarios:**
- User Testing Online Job Notes (`onlineJobNotes.feature`: 32, 52, 70, 85, 99, 113)

**Failure Pattern:** The test cannot access `testdata/onlinejobNotes.csv`.  
**Evidence:** Jenkins reports the CSV path as the failure detail for all six cases.  
**Impact:** 6 failures  
**Confidence:** High

## Sales Forecast orders not found

**Affected Features:**
- `salesForecast.feature`

**Affected Scenarios:**
- Verify order within forecast amount links and saves normally (`salesForecast.feature`: 148)
- Verify cumulative order amounts trigger info message on Sales Forecast (`salesForecast.feature`: 178)

**Failure Pattern:** The expected order is absent from the Recent Orders dialog.  
**Evidence:** `SF_LessAmount` was not found; expected `true`, found `false`.  
**Impact:** 2 failures  
**Confidence:** High

## Undefined Cucumber steps

**Affected Features:**
- `salesForecast.feature`, `minmaxplacementcol.feature`

**Affected Scenarios:**
- Step `User opens Sales Forecast "SF Name"` (`salesForecast.feature`: 189)
- Step `user set column max value "UpdateMaxQuery" through db` (`minmaxplacementcol.feature`: 18)

**Failure Pattern:** Both steps have no matching step definition.  
**Evidence:** Jenkins reports `UndefinedStepException` for each step.  
**Impact:** 2 failures  
**Confidence:** High

## Database result-set access error

**Affected Features:**
- `commissionorders.feature`

**Affected Scenarios:**
- User creates new online order for verifying commision (`commissionorders.feature`: 47)

**Failure Pattern:** Database access attempts to read beyond the last result row.  
**Evidence:** `java.sql.SQLException: Result set after last row`.  
**Impact:** 1 failure  
**Confidence:** High

## Job Notes assertion mismatch

**Affected Features:**
- `jobNotes.feature`

**Affected Scenarios:**
- User Testing Job Notes (`jobNotes.feature`: 48)

**Failure Pattern:** Expected `Automation`, but the actual value was empty.  
**Evidence:** `expected [Automation] but found []`.  
**Impact:** 1 failure  
**Confidence:** High
