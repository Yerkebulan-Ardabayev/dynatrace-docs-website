---
title: Settings API - Simple detection rules schema table
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/settings/schemas/builtin-process-group-simple-detection-rule
scraped: 2026-05-12T11:45:15.561974
---

# Settings API - Simple detection rules schema table

# Settings API - Simple detection rules schema table

* Published Dec 05, 2023

### Simple detection rules (`builtin:process-group.simple-detection-rule)`

Simple process group detection rules enable you to adapt the default process-group detection logic for deep monitored processes via **environment variables** or **Java system properties**. [More about custom process-group detectionï»¿](https://dt-url.net/ty02won)

Note: Detection rules change the composition, makeup, and identity of a process group, not just the name. If you only need to change default name use the naming rules (`<your-dynatrace-url>//#settings/pgnamingsettings "Visit Naming rules page"`) instead.

Process-group detection rules only affect processes that are deep monitored by the Dynatrace OneAgent and require a restart of your processes to affect how processes are identified and grouped.

| Schema ID | Schema groups | Scope |
| --- | --- | --- |
| `builtin:process-group.simple-detection-rule` | * `group:processes-and-containers.processes` * `group:processes-and-containers` | `environment` |

Retrieve schema via Settings API

|  |  |  |
| --- | --- | --- |
| GET | Managed | `https://{your-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:process-group.simple-detection-rule` |
| GET | SaaS | `https://{your-environment-id}.live.dynatrace.com/api/v2/settings/schemas/builtin:process-group.simple-detection-rule` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:process-group.simple-detection-rule` |

## Authentication

To execute this request, you need an access token with **Read settings** (`settings.read`) scope. To learn how to obtain and use it, see [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Parameters

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| Enabled `enabled` | boolean | - | Required |
| Property source `ruleType` | enum | Source to use to separate processes into multiple process groups. The element has these enums * `prop` * `env` | Required |
| Group identifier `groupIdentifier` | text | If Dynatrace detects this property at startup of a process, it will use its value to identify process groups more granular. | Required |
| Instance identifier `instanceIdentifier` | text | Use a variable to identify instances within a process group.  The type of variable is the same as selected in 'Property source'. | Required |
| Restrict this rule to specific process types `processType` | text | Note: Not all types can be detected at startup. | Optional |