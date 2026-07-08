---
title: Settings API - Process instance snapshots schema table
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/settings/schemas/builtin-process-visibility
---

# Settings API - Process instance snapshots schema table

# Settings API - Process instance snapshots schema table

* Published Dec 05, 2023

### Process instance snapshots (`builtin:process-visibility)`

If this feature is enabled, Dynatrace examines the most resource-consuming processes running on your host and the processes monitored by **Process availability**.
When a triggering event occurs, metrics reported 10 minutes before and 10 minutes after the event for those processes are sent to the cluster.

A graph of the resource consumption by process is available.

If **Process instance snapshots** is triggered by **Process availability**, you can see the behavior of processes before they ended, and whether they restarted within 10 minutes.

Reported process metrics:

* CPU usage (%)
* Memory usage (B)
* Incoming network traffic (KB)
* Outgoing network traffic (KB)

Metrics are reported once per minute and cover the number of processes defined in **Reported processes limit**.

Each host can report up to 60 minutes of these metrics per day. When the limit is exceeded, metrics aren't sent even when a new event arises.

Events triggering **Process instance snapshots**:

* High host CPU usage
* High system load
* High host memory usage
* High packet drop rates
* High NIC utilization rates
* High number of NIC errors
* Manual requests
* Process availability events

For details, see [Process instance snapshots﻿](https://dt-url.net/yw02uea)

| Schema ID | Schema groups | Scope |
| --- | --- | --- |
| `builtin:process-visibility` | * `group:processes-and-containers.processes` * `group:processes-and-containers` | `HOST` - Host  `HOST_GROUP` - Host Group  `environment` |

Retrieve schema via Settings API

|  |  |  |
| --- | --- | --- |
| GET | Managed | `https://{your-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:process-visibility` |
| GET | SaaS | `https://{your-environment-id}.live.dynatrace.com/api/v2/settings/schemas/builtin:process-visibility` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:process-visibility` |

## Authentication

To execute this request, you need an access token with **Read settings** (`settings.read`) scope. To learn how to obtain and use it, see [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Parameters

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| Enable Process instance snapshots `enabled` | boolean | - | Required |
| Reported processes limit `maxProcesses` | integer | The maximum amount of processes that host may report is **100** | Required |