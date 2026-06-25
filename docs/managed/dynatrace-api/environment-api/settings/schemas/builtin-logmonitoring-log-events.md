---
title: Settings API - Log events schema table
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/settings/schemas/builtin-logmonitoring-log-events
scraped: 2026-05-12T11:49:23.296096
---

# Settings API - Log events schema table

# Settings API - Log events schema table

* Published Dec 05, 2023

### Log events (`builtin:logmonitoring.log-events)`

Configure log patterns that trigger events for alerting and DavisÂ® analysis. Note that log event detection incurs [billing costsï»¿](https://dt-url.net/hk03ulj)

| Schema ID | Schema groups | Scope |
| --- | --- | --- |
| `builtin:logmonitoring.log-events` | * `group:log-monitoring.analysis` * `group:log-monitoring` | `environment` |

Retrieve schema via Settings API

|  |  |  |
| --- | --- | --- |
| GET | Managed | `https://{your-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:logmonitoring.log-events` |
| GET | SaaS | `https://{your-environment-id}.live.dynatrace.com/api/v2/settings/schemas/builtin:logmonitoring.log-events` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:logmonitoring.log-events` |

## Authentication

To execute this request, you need an access token with **Read settings** (`settings.read`) scope. To learn how to obtain and use it, see [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Parameters

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| Enabled `enabled` | boolean | - | Required |
| Summary `summary` | text | The textual summary of the log event entry | Required |
| Matcher `query` | text | - | Required |
| Event template `eventTemplate` | [EventTemplate](#EventTemplate) | - | Required |

##### The `EventTemplate` object

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| Title `title` | text | The title of the event to trigger. Type '{' for placeholder hints. | Required |
| Description `description` | text | The description of the event to trigger. Type '{' for placeholder hints. | Required |
| Event type `eventType` | enum | The event type to trigger. The element has these enums * `INFO` * `ERROR` * `AVAILABILITY` * `SLOWDOWN` * `RESOURCE` * `CUSTOM_ALERT` * `CUSTOM_ANNOTATION` * `CUSTOM_CONFIGURATION` * `CUSTOM_DEPLOYMENT` * `MARKED_FOR_TERMINATION` * `WARNING` | Required |
| Allow merge `davisMerge` | boolean | DavisÂ® AI will try to merge this event into existing problems, otherwise a new problem will always be created. | Required |
| Properties `metadata` | Set<[MetadataItem](#MetadataItem)> | Set of additional key-value properties to be attached to the triggered event. You can retrieve the available property keys using the [Events API v2ï»¿](https://dt-url.net/9622g1w). | Required |

##### The `MetadataItem` object

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| Key `metadataKey` | text | Type 'dt.' for key hints. | Required |
| Value `metadataValue` | text | Type '{' for placeholder hints. | Required |