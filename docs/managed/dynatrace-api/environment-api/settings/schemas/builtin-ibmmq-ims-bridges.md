---
title: Settings API - IBM MQ IMS bridges schema table
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/settings/schemas/builtin-ibmmq-ims-bridges
scraped: 2026-05-12T11:42:58.860388
---

# Settings API - IBM MQ IMS bridges schema table

# Settings API - IBM MQ IMS bridges schema table

* Published Dec 05, 2023

### IBM MQ IMS bridges (`builtin:ibmmq.ims-bridges)`

An IMS bridge is the component of IBM MQ for z/OS that allows direct access to the IMS system. Dynatrace needs to know which queue managers and queues belong to which IMS bridge for the end-to-end tracing on z/OS.

| Schema ID | Schema groups | Scope |
| --- | --- | --- |
| `builtin:ibmmq.ims-bridges` | * `group:mainframe` | `environment` |

Retrieve schema via Settings API

|  |  |  |
| --- | --- | --- |
| GET | Managed | `https://{your-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:ibmmq.ims-bridges` |
| GET | SaaS | `https://{your-environment-id}.live.dynatrace.com/api/v2/settings/schemas/builtin:ibmmq.ims-bridges` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:ibmmq.ims-bridges` |

## Authentication

To execute this request, you need an access token with **Read settings** (`settings.read`) scope. To learn how to obtain and use it, see [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Parameters

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| IMS bridge name `name` | text | - | Required |
| Queue managers `queueManagers` | Set<[QueueManager](#QueueManager)> | - | Required |

##### The `QueueManager` object

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| Queue manager name `name` | text | - | Required |
| Queues `queueManagerQueue` | set | - | Required |