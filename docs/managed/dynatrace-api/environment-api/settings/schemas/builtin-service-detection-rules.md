---
title: Settings API - Service detection schema table
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/settings/schemas/builtin-service-detection-rules
---

# Settings API - Service detection schema table

# Settings API - Service detection schema table

* Published Jun 30, 2025

### Service detection (`builtin:service-detection-rules)`

Define rules to detect and name services based on resource attributes defined in the [Semantic Dictionary﻿](https://docs.dynatrace.com/docs/discover-dynatrace/references/semantic-dictionary/fields) and custom attributes. Rules are evaluated in order and the first matching rule applies.

| Schema ID | Schema groups | Scope |
| --- | --- | --- |
| `builtin:service-detection-rules` | * `group:service-detection` | `CLOUD_APPLICATION_NAMESPACE` - Kubernetes namespace  `KUBERNETES_CLUSTER` - Kubernetes cluster  `HOST_GROUP` - Host Group  `environment` |

Retrieve schema via Settings API

|  |  |  |
| --- | --- | --- |
| GET | Managed | `https://{your-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:service-detection-rules` |
| GET | SaaS | `https://{your-environment-id}.live.dynatrace.com/api/v2/settings/schemas/builtin:service-detection-rules` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:service-detection-rules` |

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
| Matching condition `condition` | text | Limits the scope of the service detection rule using [DQL matcher﻿](https://dt-url.net/l603wby) conditions on resource attributes.  A rule is applied only if the condition matches, otherwise the ruleset evaluation continues.  If empty, the condition will always match. | Optional |
| Service name template `serviceNameTemplate` | text | Specify resource attribute placeholders in curly braces, e.g. {service.name} or {k8s.workload.name}.  All attributes used in the placeholder are required for the rule to apply. If any of them is missing, the rule will not be applied and ruleset evaluation continues.  All resolved attribute values contribute to the final service ID. | Required |
| Additional service detection attributes `additionalRequiredAttributes` | set | Add resource attribute keys (e.g. service.namespace or k8s.workload.kind) that also detect unique services but are not included in the displayed service name.  Attributes specified here are required to apply the rule. If any of them is missing, the rule will not be applied and ruleset evaluation continues.  All attribute values contribute to the final service ID. | Required |