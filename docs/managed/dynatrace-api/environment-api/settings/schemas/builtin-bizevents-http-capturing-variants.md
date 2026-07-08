---
title: Settings API - OneAgent Business events capturing variants schema table
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/settings/schemas/builtin-bizevents-http-capturing-variants
---

# Settings API - OneAgent Business events capturing variants schema table

# Settings API - OneAgent Business events capturing variants schema table

* Published Mar 17, 2025

### OneAgent Business events capturing variants (`builtin:bizevents.http.capturing-variants)`

OneAgent capturing variants.

Capture rules tell OneAgent to capture generic content-types, add capture variants below.

| Schema ID | Schema groups | Scope |
| --- | --- | --- |
| `builtin:bizevents.http.capturing-variants` | * `group:business-analytics.business-events-sources` * `group:business-analytics` | `HOST` - Host  `HOST_GROUP` - Host Group  `environment` |

Retrieve schema via Settings API

|  |  |  |
| --- | --- | --- |
| GET | Managed | `https://{your-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:bizevents.http.capturing-variants` |
| GET | SaaS | `https://{your-environment-id}.live.dynatrace.com/api/v2/settings/schemas/builtin:bizevents.http.capturing-variants` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:bizevents.http.capturing-variants` |

## Authentication

To execute this request, you need an access token with **Read settings** (`settings.read`) scope. To learn how to obtain and use it, see [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Parameters

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| Content-type matcher `contentTypeMatcher` | enum | The element has these enums * `EQUALS` * `STARTS_WITH` * `ENDS_WITH` * `CONTAINS` | Required |
| Content-type match value `contentTypeValue` | text | - | Required |
| Parser `parser` | enum | The element has these enums * `JSON` * `XML` * `URL encoded` * `Text` * `Raw` | Required |