---
title: Settings API - Process group monitoring schema table
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/settings/schemas/builtin-process-process-monitoring
scraped: 2026-05-12T11:48:02.047094
---

# Settings API - Process group monitoring schema table

# Settings API - Process group monitoring schema table

* Published Dec 05, 2023

### Process group monitoring (`builtin:process.process-monitoring)`

Dynatrace OneAgent automatically monitors all process groups detected in your environment (processes running during OneAgent installation must be restarted to initiate monitoring).

OneAgent additionally provides deep monitoring for all processes that it can monitor at the request- and PurePath levels.

| Schema ID | Schema groups | Scope |
| --- | --- | --- |
| `builtin:process.process-monitoring` | * `group:processes-and-containers.processes` * `group:processes-and-containers` | `HOST_GROUP` - Host Group  `environment` |

Retrieve schema via Settings API

|  |  |  |
| --- | --- | --- |
| GET | Managed | `https://{your-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:process.process-monitoring` |
| GET | SaaS | `https://{your-environment-id}.live.dynatrace.com/api/v2/settings/schemas/builtin:process.process-monitoring` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:process.process-monitoring` |

## Authentication

To execute this request, you need an access token with **Read settings** (`settings.read`) scope. To learn how to obtain and use it, see [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Parameters

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| Enable automatic deep monitoring `autoMonitoring` | boolean | By disabling automatic deep monitoring the Dynatrace OneAgent will only deep monitor processes that are covered by a respective deep monitoring rule or where monitoring is enabled explicitly. Disabling only works if all installed Agents have version 1.123 or higher.  With automatic monitoring enabled, you can create rules that define exceptions to automatic process detection and monitoring. With automatic monitoring disabled, you can define rules that identify specific processes that should be monitored. Rules are applied in the order listed in the custom and built-in process monitoring rules settings. This means that you can construct complex operations for fine-grain control over the processes that are monitored in your environment. For example, you might define an inclusion rule thatâs followed by an exclusion rule covering the same process. Once created, monitoring rules can be enabled/disabled at any time. The rules will only take effect after restart of the processes in question. Alternatively, you can disable automatic monitoring entirely and instead define "Include" rules for those processes you want to monitor. | Required |