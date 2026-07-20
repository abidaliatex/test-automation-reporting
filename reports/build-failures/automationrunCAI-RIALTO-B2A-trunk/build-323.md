# Build Failure Report

## Build ID: 323
**Job:** automationrunCAI-RIALTO-B2A-trunk
**Date:** 2026-07-20 21:02:20 UTC
**Status:** UNSTABLE
**URL:** https://crossadv.atex.com/jenkins/job/automationrunCAI-RIALTO-B2A-trunk/323/

---

## Build Summary

Build: 323
Total Tests: 17
Passed: 7
Failed: 10
Pass Rate: 41.2%

---

## Failing Tests / Steps

| Test Case | Scenario | Error |
|---|---|---|
| tc_postRialtoB2A01 | Attempts to log in a user | HTTP 404 – `/cass/users/login` not found |
| tc_postRialtoB2A02 | Create ad for self service | HTTP 404 – `/cass/orders/orders` not found |
| tc_getRialtoB2A05 | Returns StoreStatus of Order | `Undefined path parameters: uuid` (cascade) |
| tc_patchRialtoB2A01 | Update ad(Order) for self service | `Undefined path parameters: uuid` (cascade) |
| tc_getRialtoB2A06 | Returns StoreStatus of Update Order | `Undefined path parameters: uuid` (cascade) |
| tc_postRialtoB2A03 | Calculate price for self service | HTTP 404 – `/cass/orders/calculatePrice` not found |
| tc_postRialtoB2A04 | Queries space availability | HTTP 404 – `/cass/orders/spaceAvailability` not found |
| tc_getRialtoB2A01 | get order details using order ID | HTTP 404 – `/cass/orders/orders/1620` not found |
| tc_getRialtoB2A02 | Returns package and placement data | HTTP 404 – `/cass/staticData/validPackagesAndPlacements` not found |
| tc_getRialtoB2A04 | Returns OrderHeader objects for orders associated with the user | HTTP 404 – `/cass/orders/orderHeaders` not found |

---

## Feature File

- `rialtoB2A(CASS).feature`

## Base URL

`https://crossadv.atex.com/agency/crossad-integration-ws/api/870/v1/cass/`

## Server

Apache Tomcat/9.0.73
