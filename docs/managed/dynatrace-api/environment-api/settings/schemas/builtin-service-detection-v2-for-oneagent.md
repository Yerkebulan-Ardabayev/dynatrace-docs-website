---
title: Settings API - Service Detection v2 for OneAgent schema table
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/settings/schemas/builtin-service-detection-v2-for-oneagent
---

# Settings API - Service Detection v2 for OneAgent schema table

# Settings API - Service Detection v2 for OneAgent schema table

* Published Sep 25, 2025

### Service Detection v2 for OneAgent (`builtin:service-detection-v2-for-oneagent)`

Enabling SDv2 for OneAgent will use the same attribute-based rules as OpenTelemetry for detecting services, endpoints, and failures. Refer to the [SDv2 documentation﻿](https://dt-url.net/5e0309z) for more information.

This is a **Public Preview** feature. You must complete the [access request form and agree to preview terms﻿](https://dt-url.net/cb300tiz) before enabling.

**Important**

The services matching your conditions will get new metric keys, breaking existing API queries, dashboards, and service names. Custom, opaque, third party, database, and message queue services are detected differently in SDv2. Analysis views for service to database and message queue operations will be announced in upcoming releases.

| Schema ID | Schema groups | Scope |
| --- | --- | --- |
| `builtin:service-detection-v2-for-oneagent` | * `group:service-detection` | `CLOUD_APPLICATION_NAMESPACE` - Kubernetes namespace  `KUBERNETES_CLUSTER` - Kubernetes cluster  `HOST_GROUP` - Host Group  `environment` |

Retrieve schema via Settings API

|  |  |  |
| --- | --- | --- |
| GET | Managed | `https://{your-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:service-detection-v2-for-oneagent` |
| GET | SaaS | `https://{your-environment-id}.live.dynatrace.com/api/v2/settings/schemas/builtin:service-detection-v2-for-oneagent` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:service-detection-v2-for-oneagent` |

## Authentication

To execute this request, you need an access token with **Read settings** (`settings.read`) scope. To learn how to obtain and use it, see [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Parameters

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| Enable Service detection v2 for Kubernetes workloads `enableSDV2ForKubernetesWorkloads` | boolean | - | Required |
| Matching condition for Kubernetes workloads `condition` | text | Limits the opt-in’s scope by filtering with [DQL matcher﻿](https://dt-url.net/l603wby) conditions on a selected set of attributes.  Service detection v2 is only applied if this condition matches. Allowed attributes: Resource attributes, and custom attributes. If empty, the condition will always match. | Required |
| Enable Service detection v2 for FaaS `enableSDV2ForFaaS` | boolean | - | Optional |
| Matching condition for FaaS `conditionForFaaS` | text | Limits the opt-in’s scope by filtering with [DQL matcher﻿](https://dt-url.net/l603wby) conditions on a selected set of attributes.  Service detection v2 is only applied if this condition matches. Allowed attributes: Resource attributes, and custom attributes. If empty, the condition will always match. | Required |
| Matching condition for any workload `conditionForAnyWorkload` | text | Limits the opt-in’s scope by filtering with [DQL matcher﻿](https://dt-url.net/l603wby) conditions on a selected set of attributes. Resource attributes must be present.  Service detection v2 is only applied if this condition matches. Allowed attributes: Resource attributes, and custom attributes. If empty, the condition will always match. If the set of resource attributes is missing or empty, the condition will be considered not to match. | Required |