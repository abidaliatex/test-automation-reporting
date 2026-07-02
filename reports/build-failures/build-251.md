# Build Failure Report — Build #251

| Field | Value |
|---|---|
| **Build ID** | 251 |
| **Date** | 2026-06-26 |
| **Branch** | `main` |
| **Triggered by** | Commit `b7e2d45` — "Bump dependency: commons-httpclient 3.1 → 4.5.14" |
| **Status** | ❌ FAILED |
| **Duration** | 3m 12s |

## Failing Tests

| Test Suite | Test Name | Result |
|---|---|---|
| `HttpClientTests` | `testGetRequest_defaultHeaders` | FAILED |
| `HttpClientTests` | `testPostRequest_withBody` | FAILED |
| `ApiGatewayTests` | `testRouting_legacyEndpoint` | FAILED |

## Error Output

```
[HttpClientTests] testGetRequest_defaultHeaders
  NoSuchMethodError: org.apache.http.client.HttpClient.execute(
    Lorg/apache/http/client/methods/HttpUriRequest;)
  at HttpClientTests.java:55

[HttpClientTests] testPostRequest_withBody
  NoSuchMethodError: org.apache.http.client.HttpClient.execute(
    Lorg/apache/http/client/methods/HttpUriRequest;)
  at HttpClientTests.java:102

[ApiGatewayTests] testRouting_legacyEndpoint
  NullPointerException: httpClient is null — possible initialisation failure
  at ApiGatewayTests.java:34
```

## Environment

- **Runner**: `ubuntu-22.04`
- **Java**: `17.0.10`
- **Build tool**: Maven 3.9.6

## Suggested Next Steps

- Verify API compatibility between `commons-httpclient 3.x` and `4.x` — the method signature changed in the major version bump.
- Update call sites that use the deprecated `HttpClient.execute(HttpUriRequest)` API.
- Check whether `ApiGatewayTests` relies on a bean initialised by the old HTTP client library.
