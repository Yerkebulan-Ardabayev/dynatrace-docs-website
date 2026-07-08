---
title: Settings API - Service splitting schema table
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/settings/schemas/builtin-service-splitting-rules
---

# Settings API - Service splitting schema table

# Settings API - Service splitting schema table

* Published Jun 30, 2025

### Service splitting (`builtin:service-splitting-rules)`

Define rules to split services based on resource attributes defined in the [Semantic Dictionary﻿](https://docs.dynatrace.com/docs/discover-dynatrace/references/semantic-dictionary/fields) and custom attributes. Rules are evaluated in order and the first matching rule applies.

| Schema ID | Schema groups | Scope |
| --- | --- | --- |
| `builtin:service-splitting-rules` | * `group:service-detection` | `CLOUD_APPLICATION_NAMESPACE` - Kubernetes namespace  `KUBERNETES_CLUSTER` - Kubernetes cluster  `HOST_GROUP` - Host Group  `environment` |

Retrieve schema via Settings API

|  |  |  |
| --- | --- | --- |
| GET | Managed | `https://{your-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:service-splitting-rules` |
| GET | SaaS | `https://{your-environment-id}.live.dynatrace.com/api/v2/settings/schemas/builtin:service-splitting-rules` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:service-splitting-rules` |

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
| Matching condition `condition` | text | Limits the scope of the service splitting rule using [DQL matcher﻿](https://dt-url.net/l603wby) conditions on resource attributes.  A rule is applied only if the condition matches, otherwise the ruleset evaluation continues.  If empty, the condition will always match. | Optional |
| Split services by resource attributes `serviceSplittingAttributes` | Set<[splitBy](#splitBy)> | Define the entire set of resource attributes that should split your services in the matching scope.  Each attribute that exists will contribute to the final service ID. | Required |

##### The `splitBy` object

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| Attribute key `key` | text | - | Required |