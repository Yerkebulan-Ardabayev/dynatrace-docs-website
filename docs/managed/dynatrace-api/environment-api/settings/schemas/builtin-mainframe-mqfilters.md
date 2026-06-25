---
title: Settings API - IBM MQ filters schema table
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/settings/schemas/builtin-mainframe-mqfilters
scraped: 2026-05-12T11:41:19.274971
---

# Settings API - IBM MQ filters schema table

# Settings API - IBM MQ filters schema table

* Published Dec 05, 2023

### IBM MQ filters (`builtin:mainframe.mqfilters)`

Dynatrace automatically traces CICS and IMS transactions originating from IBM MQ queues. To limit tracing to certain queues, specify their names in the include lists. To exclude queues from tracing, specify their names in the exclude lists. For IMS, these lists apply to message processing regions.

To only trace specific transactions submitted via the IMS bridge, specify their transaction IDs in the include list or exclude list.

| Schema ID | Schema groups | Scope |
| --- | --- | --- |
| `builtin:mainframe.mqfilters` | * `group:mainframe` | `environment` |

Retrieve schema via Settings API

|  |  |  |
| --- | --- | --- |
| GET | Managed | `https://{your-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:mainframe.mqfilters` |
| GET | SaaS | `https://{your-environment-id}.live.dynatrace.com/api/v2/settings/schemas/builtin:mainframe.mqfilters` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:mainframe.mqfilters` |

## Authentication

To execute this request, you need an access token with **Read settings** (`settings.read`) scope. To learn how to obtain and use it, see [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Parameters

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| CICS: Included MQ queues `cicsMqQueueIdIncludes` | set | - | Required |
| CICS: Excluded MQ queues `cicsMqQueueIdExcludes` | set | - | Required |
| IMS: Included MQ queues `imsMqQueueIdIncludes` | set | - | Required |
| IMS: Excluded MQ queues `imsMqQueueIdExcludes` | set | - | Required |
| IMS bridge: Included transaction IDs `imsCrTrnIdIncludes` | set | When you add a transaction ID to the include list, all the remaining transactions are ignored. | Required |
| IMS bridge: Excluded transaction IDs `imsCrTrnIdExcludes` | set | When you add a transaction ID to the exclude list remaining transactions are still monitored. | Required |