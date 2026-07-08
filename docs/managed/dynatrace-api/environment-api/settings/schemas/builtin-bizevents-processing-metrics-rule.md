---
title: Settings API - Business event metric extraction schema table
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/settings/schemas/builtin-bizevents-processing-metrics-rule
---

# Settings API - Business event metric extraction schema table

# Settings API - Business event metric extraction schema table

* Published Dec 05, 2023

### Business event metric extraction (`builtin:bizevents-processing-metrics.rule)`

With [business event metrics﻿](https://dt-url.net/m3034if), you can use queries to create custom alerts representing specific business event occurrences or attribute values.

Note:

* Newly defined business event metrics can only be applied to Business Event data ingested after metric creation.
* Business Event metrics consume DDUs.

For complete details on pricing, visit [DDUs for custom metrics﻿](https://dt-url.net/vg43xi8).

| Schema ID | Schema groups | Scope |
| --- | --- | --- |
| `builtin:bizevents-processing-metrics.rule` | * `group:business-analytics` * `group:business-analytics.ingest-pipeline` | `environment` |

Retrieve schema via Settings API

|  |  |  |
| --- | --- | --- |
| GET | Managed | `https://{your-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:bizevents-processing-metrics.rule` |
| GET | SaaS | `https://{your-environment-id}.live.dynatrace.com/api/v2/settings/schemas/builtin:bizevents-processing-metrics.rule` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:bizevents-processing-metrics.rule` |

## Authentication

To execute this request, you need an access token with **Read settings** (`settings.read`) scope. To learn how to obtain and use it, see [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Parameters

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| Enabled `enabled` | boolean | - | Required |
| Key `key` | text | - | Required |
| Matcher (DQL) `matcher` | text | [See our documentation﻿](https://dt-url.net/bp234rv) | Required |
| Measure `measure` | enum | The element has these enums * `OCCURRENCE` * `ATTRIBUTE` | Required |
| Attribute `measureAttribute` | text | - | Required |
| `dimensions` | set | - | Required |