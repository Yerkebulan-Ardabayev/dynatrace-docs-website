---
title: Settings API - Advanced detection rules schema table
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/settings/schemas/builtin-process-group-advanced-detection-rule
---

# Settings API - Advanced detection rules schema table

# Settings API - Advanced detection rules schema table

* Published Dec 05, 2023

### Advanced detection rules (`builtin:process-group.advanced-detection-rule)`

Advanced process group detection rules enable you to adapt the detection logic for deep monitored processes by **leveraging properties that are automatically detected** by OneAgent during the startup of a process.

Advanced detection rules are capable to extract additional process group and instance identifier from processes to fine tune the automatic detection logic of OneAgent. [More about custom process-group detection﻿](https://dt-url.net/1722wrz)

Note: Detection rules change the composition, makeup, and identity of a process group, not just the name. If you only need to change default name use the naming rules (`<your-dynatrace-url>//#settings/pgnamingsettings "Visit Naming rules page"`) instead.

Process-group detection rules only affect processes that are deep monitored by the Dynatrace OneAgent and require a restart of your processes to affect how processes are identified and grouped.

| Schema ID | Schema groups | Scope |
| --- | --- | --- |
| `builtin:process-group.advanced-detection-rule` | * `group:processes-and-containers.processes` * `group:processes-and-containers` | `environment` |

Retrieve schema via Settings API

|  |  |  |
| --- | --- | --- |
| GET | Managed | `https://{your-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:process-group.advanced-detection-rule` |
| GET | SaaS | `https://{your-environment-id}.live.dynatrace.com/api/v2/settings/schemas/builtin:process-group.advanced-detection-rule` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:process-group.advanced-detection-rule` |

## Authentication

To execute this request, you need an access token with **Read settings** (`settings.read`) scope. To learn how to obtain and use it, see [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Parameters

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| Enabled `enabled` | boolean | - | Required |
| Process group detection `processDetection` | [processGroupDetection](#processGroupDetection) | Apply this rule to processes where the selected property contains the specified string. | Required |
| Process group extraction `groupExtraction` | [processGroupExtraction](#processGroupExtraction) | You can define the properties that should be used to identify your process groups. | Required |
| Process instance extraction `instanceExtraction` | [processInstanceExtraction](#processInstanceExtraction) | You can define the properties that should be used to identify your process instances. | Required |

##### The `processGroupDetection` object

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| Property `property` | text | - | Required |
| Contained string `containedString` | text | (case sensitive) | Required |
| Restrict this rule to specific process types. `restrictToProcessType` | text | Note: Not all types can be detected at startup. | Optional |

##### The `processGroupExtraction` object

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| Property `property` | text | - | Required |
| `delimiter` | [delimiter](#delimiter) | Optionally delimit this property between *From* and *To*. | Required |
| Standalone rule `standaloneRule` | boolean | If this option is selected, the default Dynatrace behavior is disabled for these detected processes. Only this rule is used to separate the process group.  If this option is not selected, this rule contributes to the default Dynatrace process group detection.  [See our help page for examples.﻿](https://dt-url.net/1722wrz) | Required |

##### The `processInstanceExtraction` object

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| Property `property` | text | - | Optional |
| `delimiter` | [delimiter](#delimiter) | Optionally delimit this property between *From* and *To*. | Required |

##### The `delimiter` object

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| Delimit from `from` | text | - | Required |
| Delimit to `to` | text | - | Required |
| Ignore numbers `removeIds` | boolean | (e.g. versions, hex, dates, and build numbers) | Required |