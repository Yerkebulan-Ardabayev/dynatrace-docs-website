---
title: Settings API - Failure detection schema table
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/settings/schemas/builtin-failure-detection-rulesets
---

# Settings API - Failure detection schema table

# Settings API - Failure detection schema table

* Published Jun 30, 2025

### Failure detection (`builtin:failure-detection-rulesets)`

Define rulesets to detect failures based on span attributes defined in the [Semantic Dictionary﻿](https://docs.dynatrace.com/docs/discover-dynatrace/references/semantic-dictionary/model/trace) and custom attributes. Rulesets are evaluated in order and the first matching one defines the failure detection result.

| Schema ID | Schema groups | Scope |
| --- | --- | --- |
| `builtin:failure-detection-rulesets` | * `group:service-detection` | `CLOUD_APPLICATION_NAMESPACE` - Kubernetes namespace  `KUBERNETES_CLUSTER` - Kubernetes cluster  `HOST_GROUP` - Host Group  `environment` |

Retrieve schema via Settings API

|  |  |  |
| --- | --- | --- |
| GET | Managed | `https://{your-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:failure-detection-rulesets` |
| GET | SaaS | `https://{your-environment-id}.live.dynatrace.com/api/v2/settings/schemas/builtin:failure-detection-rulesets` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:failure-detection-rulesets` |

## Authentication

To execute this request, you need an access token with **Read settings** (`settings.read`) scope. To learn how to obtain and use it, see [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Parameters

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| Enabled `enabled` | boolean | If enabled, the ruleset will be evaluated. | Required |
| Ruleset `ruleset` | [Ruleset](#Ruleset) | - | Required |

##### The `Ruleset` object

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| Ruleset name `rulesetName` | text | - | Required |
| Description `description` | text | - | Optional |
| Matching condition `condition` | text | Limits the scope of the failure detection ruleset using [DQL matcher﻿](https://dt-url.net/l603wby) conditions on span and resource attributes.  A ruleset is applied only if the condition matches, otherwise the evaluation continues.  If empty, the condition will always match. | Optional |
| HTTP status codes `failOnHttpResponseStatusCodes` | [failOnHttpResponseStatusCodes](#failOnHttpResponseStatusCodes) | Evaluated attribute: `http.response.status_code`  Failure detection result: `reason="http_code"`, `verdict="failure"` | Required |
| gRPC status codes `failOnGrpcStatusCodes` | [failOnGrpcStatusCodes](#failOnGrpcStatusCodes) | Evaluated attribute: `rpc.grpc.status_code`  Failure detection result: `reason="grpc_code"`, `verdict="failure"` | Required |
| Span status code `failOnSpanStatusError` | [failOnSpanStatusError](#failOnSpanStatusError) | Evaluated attribute: `span.status_code`  Failure detection result: `reason="span_status"`, `verdict="failure"` | Required |
| Exceptions `failOnExceptions` | [failOnExceptions](#failOnExceptions) | Evaluated expression: `iAny(`span.events`[][`span\_event.name`] == "exception" and` span.events`[][`exception.escaped`] != false)`  Failure detection result: `reason="exception"`, `verdict="failure"`, `exception_ids` | Required |
| Custom failure rules `failOnCustomRules` | Set<[customRule](#customRule)> | Define failure reasons based on span and request attributes.  Failure detection result: `reason="custom_rule"`, `verdict="failure"`, `custom_rule_name` | Required |
| `overrides` | [overrides](#overrides) | - | Required |

##### The `failOnHttpResponseStatusCodes` object

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| Status codes which indicate a failure on the server side `statusCodes` | text | - | Required |

##### The `failOnGrpcStatusCodes` object

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| Status codes which indicate a failure on the server side `statusCodes` | text | - | Required |

##### The `failOnSpanStatusError` object

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| Fail on span status "error" `enabled` | boolean | - | Required |

##### The `failOnExceptions` object

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| Fail on exceptions `enabled` | boolean | - | Required |
| `ignoredExceptions` | Set<[singleException](#singleException)> | - | Required |

##### The `customRule` object

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| Enabled `enabled` | boolean | - | Required |
| Rule name `ruleName` | text | - | Required |
| DQL condition `dqlCondition` | text | Custom rule based on span attributes using [DQL matcher﻿](https://dt-url.net/l603wby). | Required |

##### The `overrides` object

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| HTTP status codes `forceSuccessOnHttpResponseStatusCodes` | [forceSuccessOnHttpResponseStatusCodes](#forceSuccessOnHttpResponseStatusCodes) | Evaluated attribute: `http.response.status_code`  Failure detection result: `reason="http_code"`, `verdict="success"` | Required |
| gRPC status codes `forceSuccessOnGrpcResponseStatusCodes` | [forceSuccessOnGrpcResponseStatusCodes](#forceSuccessOnGrpcResponseStatusCodes) | Evaluated attribute: `rpc.grpc.status_code`  Failure detection result: `reason="grpc_code"`, `verdict="success"` | Required |
| Span status code `forceSuccessOnSpanStatusOk` | [forceSuccessOnSpanStatusOk](#forceSuccessOnSpanStatusOk) | Evaluated attribute: `span.status_code`  Failure detection result: `reason="span_status"`, `verdict="success"` | Required |
| Force success on specific exceptions `forceSuccessOnExceptions` | Set<[singleException](#singleException)> | Define escaped exceptions that should force success.  Evaluated expression: `iAny(`span.events`[][`span\_event.name`] == "exception" and` span.events`[][`exception.escaped`] != false)`  Failure detection result: `reason="exception"`, `verdict="success"`, `exception_ids` | Required |
| Custom success forcing rules `forceSuccessWithCustomRules` | Set<[customRule](#customRule)> | Override failures based on span and request attribute conditions.  Failure detection result: `reason="custom_rule"`, `verdict="success"`, `custom_rule_name` | Required |

##### The `singleException` object

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| Enabled `enabled` | boolean | - | Required |
| Exception type contains `type` | text | Evaluated attribute: `span.events[][exception.type]` | Optional |
| Exception message contains `message` | text | Evaluated attribute: `span.events[][exception.message]` | Optional |

##### The `forceSuccessOnHttpResponseStatusCodes` object

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| Status codes which force success on the server side `statusCodes` | text | - | Optional |

##### The `forceSuccessOnGrpcResponseStatusCodes` object

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| Status codes which force success on the server side `statusCodes` | text | - | Optional |

##### The `forceSuccessOnSpanStatusOk` object

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| Force success on span status "ok" `enabled` | boolean | - | Required |