---
title: Settings API - Failure detection parameters schema table
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/settings/schemas/builtin-failure-detection-environment-parameters
---

# Settings API - Failure detection parameters schema table

# Settings API - Failure detection parameters schema table

* Published Dec 05, 2023

### Failure detection parameters (`builtin:failure-detection.environment.parameters)`

Failure detection parameters that determine whether a service call is considered successful or failed. Use failure detection rules (`<your-dynatrace-url>//ui/settings/builtin:failure-detection.environment.rules`) to configure which services these parameters apply to.

These settings are not applied to [Unified services﻿](https://dt-url.net/gy03cmt).

To programmatically manage these settings, see [API Reference﻿](https://docs.dynatrace.com/docs/shortlink/service-failure-detection#settings-api).

| Schema ID | Schema groups | Scope |
| --- | --- | --- |
| `builtin:failure-detection.environment.parameters` | * `group:service-monitoring` * `group:failure-detection` | `environment` |

Retrieve schema via Settings API

|  |  |  |
| --- | --- | --- |
| GET | Managed | `https://{your-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:failure-detection.environment.parameters` |
| GET | SaaS | `https://{your-environment-id}.live.dynatrace.com/api/v2/settings/schemas/builtin:failure-detection.environment.parameters` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:failure-detection.environment.parameters` |

## Authentication

To execute this request, you need an access token with **Read settings** (`settings.read`) scope. To learn how to obtain and use it, see [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Parameters

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| Name `name` | text | The display name of this failure detection parameter set. | Required |
| Description `description` | text | A short description of this failure detection parameter set. | Optional |
| HTTP response codes `httpResponseCodes` | [httpResponseCodes](#httpResponseCodes) | HTTP response code settings that control which response codes are treated as server-side or client-side errors. | Required |
| HTTP 404 (broken links) `brokenLinks` | [brokenLinks](#brokenLinks) | HTTP 404 response codes are thrown when a web server can't find a certain page. 404s are classified as broken links on the client side and therefore aren't considered to be service failures. By enabling this setting, you can have 404s treated as server-side service failures. | Required |
| Customize failure detection for specific exceptions and errors `exceptionRules` | [exceptionRules](#exceptionRules) | Exception and custom error rules that determine how specific exceptions, handled errors, and request-attribute-based conditions affect failure detection. | Required |

##### The `httpResponseCodes` object

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| HTTP response codes which indicate an error on the server side `serverSideErrors` | text | A list of HTTP response code ranges and individual values that are treated as server-side errors. The format is a comma-separated list of ranges and values (e.g., `500-599, 402, 405-499`). Default: `500-599`. | Required |
| Treat missing HTTP response code as server side errors `failOnMissingResponseCodeServerSide` | boolean | If `true`, a missing HTTP response code on the server side is treated as a failure. Missing response codes can indicate a fire-and-forget call, a timeout, or an error. Default: `false`. | Required |
| HTTP response codes which indicate client side errors `clientSideErrors` | text | A list of HTTP response code ranges and individual values that are treated as client-side errors. The format is a comma-separated list of ranges and values (e.g., `400-499, 503, 510-599`). Default: `400-599`. | Required |
| Treat missing HTTP response code as client side error `failOnMissingResponseCodeClientSide` | boolean | If `true`, a missing HTTP response code on the client side is treated as a failure. Missing response codes can indicate a fire-and-forget call, a timeout, or an error. Default: `false`. | Required |

##### The `brokenLinks` object

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| Consider 404 HTTP response codes as failures `http404NotFoundFailures` | boolean | If `true`, HTTP 404 response codes are treated as server-side service failures. Only applicable when 404 is not already in the list of failing server-side HTTP response codes. Default: `false`. | Required |
| Rules for broken links to related domains `brokenLinkDomains` | set | If your application relies on other hosts at other domains, add the associated domain names here. Once configured, Dynatrace will consider 404s thrown by hosts at these domains to be service failures related to your application. | Required |

##### The `exceptionRules` object

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| Ignore all exceptions `ignoreAllExceptions` | boolean | If `true`, all exceptions are ignored for failure detection. Success forcing exceptions, ignored exceptions, and custom handled exceptions have no effect. Exceptions are still tracked and appear in distributed traces, but requests are not labeled as failed. Default: `false`. | Required |
| Success forcing exceptions `successForcingExceptions` | Set<[exception](#exception)> | Define exceptions which indicate that an entire service call should not be considered as failed. E.g. an exception indicating that the client aborted the operation. If an exception matching any of the defined patterns occurs on the **entry node** of the service, it will be considered successful. Compared to ignored exceptions, the request will be considered successful even if other exceptions occur in the same request. | Required |
| Ignored exceptions `ignoredExceptions` | Set<[exception](#exception)> | Some exceptions that are thrown by legacy or 3rd-party code indicate a specific response, not an error. Use this setting to instruct Dynatrace to treat such exceptions as non-failed requests. If an exception matching any of the defined patterns occurs on the **entry node** of the service, it will not be considered as a failure. Other exceptions occurring at the same request might still mark the request as failed. | Required |
| Custom handled exceptions `customHandledExceptions` | Set<[exception](#exception)> | There may be situations where your application code handles exceptions gracefully in a manner that these failures aren't detected by Dynatrace. Use this setting to define specific gracefully-handled exceptions that should be treated as service failures. | Required |
| Custom error rules `customErrorRules` | Set<[customErrorRule](#customErrorRule)> | Some custom error situations are only detectable via a return value or other means. To support such cases, [define a request attribute﻿](https://dt-url.net/ys5k0p4y) that captures the required data. Then define a custom error rule that determines if the request has failed based on the value of the request attribute. | Required |
| Ignore span failure detection `ignoreSpanFailureDetection` | boolean | If `true`, span failure detection is ignored. This is specific to OpenTelemetry. Default: `false`. | Required |

##### The `exception` object

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| Class pattern `classPattern` | text | The pattern will match if it is contained within the actual class name. | Optional |
| Exception message pattern `messagePattern` | text | Optionally, define an exception message pattern. The pattern will match if the actual exception message contains the pattern. | Optional |

##### The `customErrorRule` object

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| Request attribute `requestAttribute` | text | The ID of the request attribute to check. The request attribute must already be defined. | Required |
| Request attribute condition `condition` | [compareOperation](#compareOperation) | The condition that determines whether the request attribute value indicates a failure. | Required |

##### The `compareOperation` object

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| Apply this comparison `compareOperationType` | text | The type of comparison to apply. Available types depend on the data type of the request attribute:  * String types support `STRING_EXISTS`, `STRING_EQUALS`, `NOT_STRING_EQUALS`, `STARTS_WITH`, `NOT_STARTS_WITH`, `CONTAINS`, `NOT_CONTAINS`, `ENDS_WITH`, `NOT_ENDS_WITH`. * Integer types support `INTEGER_EQUALS` and related comparisons; * Double types support `DOUBLE_EQUALS` and related comparisons. | Required |
| Value `textValue` | text | The text value to compare the request attribute against. Only applicable for string comparison types. | Required |
| Case sensitive `caseSensitive` | boolean | If `true`, the comparison is case-sensitive. Only applicable for string comparison types. Default: `false`. | Required |
| Value `intValue` | integer | The integer value to compare the request attribute against. Only applicable for integer comparison types. | Required |
| Value `doubleValue` | float | The floating-point value to compare the request attribute against. Only applicable for double comparison types. | Required |