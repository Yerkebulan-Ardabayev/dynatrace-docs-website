---
title: Settings API - Endpoint detection schema table
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/settings/schemas/builtin-endpoint-detection-rules
---

# Settings API - Endpoint detection schema table

# Settings API - Endpoint detection schema table

* Published Aug 25, 2025

### Endpoint detection (`builtin:endpoint-detection-rules)`

Define rules to detect requests on endpoints based on span attributes defined in the [Semantic Dictionary﻿](https://docs.dynatrace.com/docs/discover-dynatrace/references/semantic-dictionary/fields) and custom attributes. Rules are evaluated in order and the first matching rule applies.

| Schema ID | Schema groups | Scope |
| --- | --- | --- |
| `builtin:endpoint-detection-rules` | * `group:service-detection` | `CLOUD_APPLICATION_NAMESPACE` - Kubernetes namespace  `KUBERNETES_CLUSTER` - Kubernetes cluster  `HOST_GROUP` - Host Group  `environment` |

Retrieve schema via Settings API

|  |  |  |
| --- | --- | --- |
| GET | Managed | `https://{your-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:endpoint-detection-rules` |
| GET | SaaS | `https://{your-environment-id}.live.dynatrace.com/api/v2/settings/schemas/builtin:endpoint-detection-rules` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:endpoint-detection-rules` |

## Authentication

To execute this request, you need an access token with **Read settings** (`settings.read`) scope. To learn how to obtain and use it, see [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Parameters

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| Enabled `enabled` | boolean | If enabled, the rule will be evaluated. | Required |
| Rule `rule` | [Rule](#Rule) | - | Required |

##### The `Rule` object

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| Rule name `ruleName` | text | - | Required |
| Description `description` | text | - | Optional |
| Matching condition `condition` | text | Limits the scope of the endpoint detection rule using [DQL matcher﻿](https://dt-url.net/l603wby) conditions on span and resource attributes.  A rule is applied only if the condition matches, otherwise the ruleset evaluation continues.  If empty, the condition will always match. | Optional |
| If condition matches `ifConditionMatches` | enum | The element has these enums * `DETECT_REQUEST_ON_ENDPOINT` * `SUPPRESS_REQUEST` | Required |
| Endpoint name template `endpointNameTemplate` | text | Specify attribute placeholders in curly braces, e.g. {http.route} or {rpc.method}.  Attribute value placeholders should be specified in curly braces, e.g. {http.route}, {rpc.method}. All attributes used in the placeholder are required for the rule to apply. If any of them is missing, the rule will not be applied and ruleset evaluation continues.  If the resolved endpoint name on a given span is empty, the request will be ignored. | Required |