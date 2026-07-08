---
title: Settings API - IBM MQ queue sharing groups schema table
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/settings/schemas/builtin-ibmmq-queue-sharing-group
---

# Settings API - IBM MQ queue sharing groups schema table

# Settings API - IBM MQ queue sharing groups schema table

* Published Dec 05, 2023

### IBM MQ queue sharing groups (`builtin:ibmmq.queue-sharing-group)`

A queue sharing group defines a group of queue managers that can access the same shared queues on z/OS. Dynatrace needs to know which queue managers and shared queues belong to which queue sharing group for the end-to-end tracing on z/OS.

| Schema ID | Schema groups | Scope |
| --- | --- | --- |
| `builtin:ibmmq.queue-sharing-group` | * `group:mainframe` | `environment` |

Retrieve schema via Settings API

|  |  |  |
| --- | --- | --- |
| GET | Managed | `https://{your-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:ibmmq.queue-sharing-group` |
| GET | SaaS | `https://{your-environment-id}.live.dynatrace.com/api/v2/settings/schemas/builtin:ibmmq.queue-sharing-group` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:ibmmq.queue-sharing-group` |

## Authentication

To execute this request, you need an access token with **Read settings** (`settings.read`) scope. To learn how to obtain and use it, see [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Parameters

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| Queue sharing group name `name` | text | - | Required |
| Queue managers `queueManagers` | set | - | Required |
| Shared queues `sharedQueues` | set | - | Required |