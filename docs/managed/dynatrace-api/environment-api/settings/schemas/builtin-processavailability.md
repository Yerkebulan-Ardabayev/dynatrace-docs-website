---
title: Settings API - Process availability schema table
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/settings/schemas/builtin-processavailability
---

# Settings API - Process availability schema table

# Settings API - Process availability schema table

* Published Dec 05, 2023

### Process availability (`builtin:processavailability)`

This feature allows you to monitor if a minimum number of processes matching the specified monitoring rule are running on your host. If there aren't enough processes matching the rule, you receive an alert. If you also enable **Process instance snapshots**, you receive a detailed report on the activity of the most resource-consuming processes, as well as on the latest activity of the processes matching the rule.

In order to monitor the availability of a certain group of processes, you must first define a monitoring rule. Give your monitoring rule a unique name and add its detection rules to which Dynatrace will match the processes on your host.

For more details, see [Process availability﻿](https://dt-url.net/v923x37)

| Schema ID | Schema groups | Scope |
| --- | --- | --- |
| `builtin:processavailability` | * `group:processes-and-containers.processes` * `group:processes-and-containers` | `HOST` - Host  `HOST_GROUP` - Host Group  `environment` |

Retrieve schema via Settings API

|  |  |  |
| --- | --- | --- |
| GET | Managed | `https://{your-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:processavailability` |
| GET | SaaS | `https://{your-environment-id}.live.dynatrace.com/api/v2/settings/schemas/builtin:processavailability` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:processavailability` |

## Authentication

To execute this request, you need an access token with **Read settings** (`settings.read`) scope. To learn how to obtain and use it, see [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Parameters

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| Enabled `enabled` | boolean | - | Required |
| Monitoring rule name `name` | text | - | Required |
| Operating system `operatingSystem` | Set<[OperatingSystem](#OperatingSystem)> | Select the operating systems on which the monitoring rule should be applied. The element has these enums * `WINDOWS` * `LINUX` * `AIX` | Required |
| Minimum number of matching processes `minimumProcesses` | integer | Specify a minimum number of processes matching the monitoring rule. An alert is triggered if any host falls below this threshold. | Required |
| Define detection rules `rules` | [DetectionCondition](#DetectionCondition)[] | Define process detection rules by selecting a process property and a condition. Each monitoring rule can have multiple detection rules associated with it. | Required |
| Properties `metadata` | Set<[MetadataItem](#MetadataItem)> | Set of additional key-value properties to be attached to the triggered event. You can retrieve the available property keys using the [Events API v2﻿](https://dt-url.net/9622g1w). Additionally any Host resource attribute can be dynamically substituted (agent 1.325+). | Required |

##### The `DetectionCondition` object

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| Rule scope `ruleType` | enum | The element has these enums * `RuleTypeProcess` * `RuleTypeHost` | Required |
| Select process property `property` | enum | The element has these enums * `executable` * `executablePath` * `commandLine` * `fullCommandLine` * `user` | Required |
| Condition `condition` | text | * $contains(svc) – Matches if svc appears anywhere in the process property value. * $eq(svc.exe) – Matches if svc.exe matches the process property value exactly. * $prefix(svc) – Matches if app matches the prefix of the process property value. * $suffix(svc.py) – Matches if svc.py matches the suffix of the process property value.  For example, $suffix(svc.py) would detect processes named loyaltysvc.py and paymentssvc.py.  For more details, see [Process availability﻿](https://dt-url.net/v923x37). | Required |
| Resource attribute `hostMetadataCondition` | [HostMetadataCondition](#HostMetadataCondition) | Host resource attributes are dimensions enriching the host including custom metadata which are user-defined key-value pairs that you can assign to hosts monitored by Dynatrace.  By defining custom metadata, you can enrich the monitoring data with context specific to your organization's needs, such as environment names, team ownership, application versions, or any other relevant details.  See [Define tags and metadata for hosts﻿](https://dt-url.net/w3hv0kbw).  Note: Starting from version 1.325 host resource attributes are supported in addition to host custom metadata. | Required |

##### The `MetadataItem` object

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| Key `metadataKey` | text | Type 'dt.' for key hints. | Required |
| Value `metadataValue` | text | Type '{' for placeholder hints. | Required |

##### The `HostMetadataCondition` object

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| Key must exist `keyMustExist` | boolean | When enabled, the condition requires a resource attribute to exist and match the constraints; when disabled, the key is optional but must still match the constrains if it is present. | Required |
| Key `metadataKey` | text | - | Required |
| Condition `metadataCondition` | text | This string has to match a required format.  * `$match(ver*_1.2.?)` – Matches string with wildcards: `*` any number (including zero) of characters and `?` exactly one character. * `$contains(production)` – Matches if `production` appears anywhere in the host metadata value. * `$eq(production)` – Matches if `production` matches the host metadata value exactly. * `$prefix(production)` – Matches if `production` matches the prefix of the host metadata value. * `$suffix(production)` – Matches if `production` matches the suffix of the host metadata value.  Available logic operations:  * `$not($eq(production))` – Matches if the host metadata value is different from `production`. * `$and($prefix(production),$suffix(main))` – Matches if host metadata value starts with `production` and ends with `main`. * `$or($prefix(production),$suffix(main))` – Matches if host metadata value starts with `production` or ends with `main`.  Brackets **(** and **)** that are part of the matched property **must be escaped with a tilde (~)** | Required |