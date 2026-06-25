---
title: Settings API - General failure detection parameters schema table
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/settings/schemas/builtin-failure-detection-service-general-parameters
scraped: 2026-05-12T11:40:24.292429
---

# Settings API - General failure detection parameters schema table

# Settings API - General failure detection parameters schema table

* Published Dec 05, 2023

### General failure detection parameters (`builtin:failure-detection.service.general-parameters)`

Dynatrace failure detection automatically detects the vast majority of error conditions in your environment. However, detected service errors don't necessarily mean that the underlying requests have failed. There may be cases where the default service failure detection settings don't meet your particular needs. In such cases, you can configure the settings provided below. Please note that these settings are not applicable to services of type 'Span service'. For complete details, see [configure service failure detectionï»¿](https://dt-url.net/ys5k0p4y).

| Schema ID | Schema groups | Scope |
| --- | --- | --- |
| `builtin:failure-detection.service.general-parameters` | * `group:failure-detection` | `SERVICE` - Service |

Retrieve schema via Settings API

|  |  |  |
| --- | --- | --- |
| GET | Managed | `https://{your-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:failure-detection.service.general-parameters` |
| GET | SaaS | `https://{your-environment-id}.live.dynatrace.com/api/v2/settings/schemas/builtin:failure-detection.service.general-parameters` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:failure-detection.service.general-parameters` |

## Authentication

To execute this request, you need an access token with **Read settings** (`settings.read`) scope. To learn how to obtain and use it, see [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Parameters

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| Override global failure detection settings `enabled` | boolean | - | Required |
| Customize failure detection for specific exceptions and errors `exceptionRules` | [exceptionRules](#exceptionRules) | - | Required |

##### The `exceptionRules` object

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| Ignore all exceptions `ignoreAllExceptions` | boolean | - | Required |
| Success forcing exceptions `successForcingExceptions` | Set<[exception](#exception)> | Define exceptions which indicate that an entire service call should not be considered as failed. E.g. an exception indicating that the client aborted the operation. If an exception matching any of the defined patterns occurs on the **entry node** of the service, it will be considered successful. Compared to ignored exceptions, the request will be considered successful even if other exceptions occur in the same request. | Required |
| Ignored exceptions `ignoredExceptions` | Set<[exception](#exception)> | Some exceptions that are thrown by legacy or 3rd-party code indicate a specific response, not an error. Use this setting to instruct Dynatrace to treat such exceptions as non-failed requests. If an exception matching any of the defined patterns occurs on the **entry node** of the service, it will not be considered as a failure. Other exceptions occurring at the same request might still mark the request as failed. | Required |
| Custom handled exceptions `customHandledExceptions` | Set<[exception](#exception)> | There may be situations where your application code handles exceptions gracefully in a manner that these failures aren't detected by Dynatrace. Use this setting to define specific gracefully-handled exceptions that should be treated as service failures. | Required |
| Custom error rules `customErrorRules` | Set<[customErrorRule](#customErrorRule)> | Some custom error situations are only detectable via a return value or other means. To support such cases, [define a request attributeï»¿](https://dt-url.net/ys5k0p4y) that captures the required data. Then define a custom error rule that determines if the request has failed based on the value of the request attribute. | Required |
| Ignore span failure detection `ignoreSpanFailureDetection` | boolean | - | Required |

##### The `exception` object

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| Class pattern `classPattern` | text | The pattern will match if it is contained within the actual class name. | Optional |
| Exception message pattern `messagePattern` | text | Optionally, define an exception message pattern. The pattern will match if the actual exception message contains the pattern. | Optional |

##### The `customErrorRule` object

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| Request attribute `requestAttribute` | text | - | Required |
| Request attribute condition `condition` | [compareOperation](#compareOperation) | - | Required |

##### The `compareOperation` object

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| Apply this comparison `compareOperationType` | text | - | Required |
| Value `textValue` | text | - | Required |
| Case sensitive `caseSensitive` | boolean | - | Required |
| Value `intValue` | integer | - | Required |
| Value `doubleValue` | float | - | Required |