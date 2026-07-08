---
title: Settings API - Declarative process grouping schema table
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/settings/schemas/builtin-declarativegrouping
---

# Settings API - Declarative process grouping schema table

# Settings API - Declarative process grouping schema table

* Published Dec 05, 2023

### Declarative process grouping (`builtin:declarativegrouping)`

Dynatrace automatically monitors process groups that are of known technology types or that consume significant resources. With declarative process grouping, you can automatically monitor additional technologies.

To add a new process group, you must first define the technology type. The technology type can be a generic technology name or a custom name. Each technology type can be associated with multiple process groups.

Next, give your process group a unique name and identifier. This name is used to identify the process group throughout your Dynatrace environment. Finally, add detection rules so that Dynatrace can automatically identify processes that belong in this group.

For complete details, see [Declarative process grouping﻿](https://dt-url.net/j142w57)

| Schema ID | Schema groups | Scope |
| --- | --- | --- |
| `builtin:declarativegrouping` | * `group:processes-and-containers.processes` * `group:processes-and-containers` | `HOST` - Host  `KUBERNETES_CLUSTER` - Kubernetes cluster  `HOST_GROUP` - Host Group  `environment` |

Retrieve schema via Settings API

|  |  |  |
| --- | --- | --- |
| GET | Managed | `https://{your-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:declarativegrouping` |
| GET | SaaS | `https://{your-environment-id}.live.dynatrace.com/api/v2/settings/schemas/builtin:declarativegrouping` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:declarativegrouping` |

## Authentication

To execute this request, you need an access token with **Read settings** (`settings.read`) scope. To learn how to obtain and use it, see [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Parameters

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| Enabled `enabled` | boolean | - | Required |
| Monitored technology name `name` | text | Note: Reported only in full-stack, infrastructure and discovery modes. | Required |
| Define the process group `detection` | [ProcessDefinition](#ProcessDefinition)[] | Enter a descriptive process group display name and a unique identifier that Dynatrace can use to recognize this process group. | Required |

##### The `ProcessDefinition` object

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| Process group display name `processGroupName` | text | - | Required |
| Process group identifier `id` | text | This identifier is used by Dynatrace to recognize this process group. | Required |
| Report process group `report` | enum | This property tells OneAgent a condition for reporting the created Process group to Dynatrace. The element has these enums * `always` * `highResourceUsage` * `never` | Required |
| Define detection rules `rules` | [DetectionCondition](#DetectionCondition)[] | Define process detection rules by selecting a process property and a condition. Each process group can have multiple detection rules associated with it. | Required |

##### The `DetectionCondition` object

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| Select process property `property` | enum | The element has these enums * `executable` * `executablePath` * `commandLine` | Required |
| Condition `condition` | text | * $contains(svc) – Matches if svc appears anywhere in the process property value. * $eq(svc.exe) – Matches if svc.exe matches the process property value exactly. * $prefix(svc) – Matches if app matches the prefix of the process property value. * $suffix(svc.py) – Matches if svc.py matches the suffix of the process property value.  For example, $suffix(svc.py) would detect processes named loyaltysvc.py and paymentssvc.py.  For more details, see [Declarative process grouping﻿](https://dt-url.net/j142w57). | Required |