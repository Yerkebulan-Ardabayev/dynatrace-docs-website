---
title: Settings API - OS services monitoring schema table
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/settings/schemas/builtin-os-services-monitoring
---

# Settings API - OS services monitoring schema table

# Settings API - OS services monitoring schema table

* Published Dec 05, 2023

### OS services monitoring (`builtin:os-services-monitoring)`

Set up alerts for OS services in undesirable states both for Windows and Linux systemd.
Note: If monitoring is turned on for full availability metric, custom metric consumption takes place. Refer to [documentation﻿](https://dt-url.net/vl03xzk) for more details.

Please provide feedback to us about this feature on [Dynatrace Community﻿](https://dt-url.net/nl02tbm).

In order to set up the alert for a certain group of OS services, you must first define a new policy. Specify which service's states you would like to be alerted about and then add detection rules in order to tell Dynatrace which exact OS services you are interested in. You may specify multiple detection rules.

Note that policies are specified for each of supported operating systems individually and that some of the parameters and properties vary between them.

| Schema ID | Schema groups | Scope |
| --- | --- | --- |
| `builtin:os-services-monitoring` | * `group:monitoring` | `HOST` - Host  `HOST_GROUP` - Host Group  `environment` |

Retrieve schema via Settings API

|  |  |  |
| --- | --- | --- |
| GET | Managed | `https://{your-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:os-services-monitoring` |
| GET | SaaS | `https://{your-environment-id}.live.dynatrace.com/api/v2/settings/schemas/builtin:os-services-monitoring` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:os-services-monitoring` |

## Authentication

To execute this request, you need an access token with **Read settings** (`settings.read`) scope. To learn how to obtain and use it, see [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Parameters

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| Enabled `enabled` | boolean | - | Required |
| System `system` | enum | The element has these enums * `WINDOWS` * `LINUX` | Required |
| Rule name `name` | text | - | Required |
| Monitor `monitoring` | boolean | Toggle the switch in order to enable or disable availability metric monitoring for this policy. Availability metrics produce custom metrics. Refer to [documentation﻿](https://dt-url.net/vl03xzk) for consumption examples. Each monitored service consumes one custom metric.  **The feature can't be configured on hosts in Discovery mode** | Required |
| Alert `alerting` | boolean | Toggle the switch in order to enable or disable alerting for this policy | Required |
| Alert if service is not installed `notInstalledAlerting` | boolean | By default, Dynatrace does not alert if the service is not installed. Toggle the switch to enable or disable this feature | Required |
| Service status condition for alerting `statusConditionWindows` | text | This string has to match a required format. See [OS services monitoring﻿](https://dt-url.net/vl03xzk).  * `$eq(paused)` – Matches services that are in paused state.  Available logic operations:  * `$not($eq(paused))` – Matches services that are in state different from paused. * `$or($eq(paused),$eq(running))` – Matches services that are either in paused or running state.  Use one of the following values as a parameter for this condition:  * `running` * `stopped` * `start_pending` * `stop_pending` * `continue_pending` * `pause_pending` * `paused` | Required |
| Service status condition for alerting `statusConditionLinux` | text | This string has to match a required format. See [OS services monitoring﻿](https://dt-url.net/vl03xzk).  * `$eq(failed)` – Matches services that are in failed state.  Available logic operations:  * `$not($eq(active))` – Matches services with state different from active. * `$or($eq(inactive),$eq(failed))` – Matches services that are either in inactive or failed state.  Use one of the following values as a parameter for this condition:  * `reloading` * `activating` * `deactivating` * `failed` * `inactive` * `active` | Required |
| Alerting delay `alertActivationDuration` | integer | The number of **10-second measurement cycles** before alerting is triggered  Set this value to control the speed of alerting. One is the lowest setting equal to one 10-second sample. If you set this value to 30, alerting is triggered after 5 minutes. | Required |
| Detection rules `detectionConditionsWindows` | [windowsDetectionCondition](#windowsDetectionCondition)[] | - | Required |
| Detection rules `detectionConditionsLinux` | [linuxDetectionCondition](#linuxDetectionCondition)[] | - | Required |
| Properties `metadata` | Set<[MetadataItem](#MetadataItem)> | Set of additional key-value properties to be attached to the triggered event. You can retrieve the available property keys using the [Events API v2﻿](https://dt-url.net/9622g1w). Additionally any Host resource attribute can be dynamically substituted (agent 1.325+). | Required |

##### The `windowsDetectionCondition` object

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| Rule scope `ruleType` | enum | The element has these enums * `RuleTypeOsService` * `RuleTypeHost` | Optional |
| Service property `property` | enum | The element has these enums * `DisplayName` * `ServiceName` * `Path` * `StartupType` * `Manufacturer` | Required |
| Condition `condition` | text | This string has to match a required format. See [OS services monitoring﻿](https://dt-url.net/vl03xzk).  * `$match(ip?tables*)` – Matches string with wildcards: `*` any number (including zero) of characters and `?` exactly one character. * `$contains(ssh)` – Matches if `ssh` appears anywhere in the service's property value. * `$eq(sshd)` – Matches if `sshd` matches the service's property value exactly. * `$prefix(ss)` – Matches if `ss` matches the prefix of the service's property value. * `$suffix(hd)` – Matches if `hd` matches the suffix of the service's property value.  Available logic operations:  * `$not($eq(sshd))` – Matches if the service's property value is different from `sshd`. * `$and($prefix(ss),$suffix(hd))` – Matches if service's property value starts with `ss` and ends with `hd`. * `$or($prefix(ss),$suffix(hd))` – Matches if service's property value starts with `ss` or ends with `hd`.  Brackets **(** and **)** that are part of the matched property **must be escaped with a tilde (~)** | Required |
| Condition `startupCondition` | text | This string has to match a required format. See [OS services monitoring﻿](https://dt-url.net/vl03xzk).  * `$eq(manual)` – Matches services that are started manually.  Available logic operations:  * `$not($eq(auto))` – Matches services with startup type different from Automatic. * `$or($eq(auto),$eq(manual))` – Matches if service's startup type is either Automatic or Manual.  Use one of the following values as a parameter for this condition:  * `manual` for Manual * `manual_trigger` for Manual (Trigger Start) * `auto` for Automatic * `auto_delay` for Automatic (Delayed Start) * `auto_trigger` for Automatic (Trigger Start) * `auto_delay_trigger` for Automatic (Delayed Start, Trigger Start) * `disabled` for Disabled | Required |
| Resource attribute `hostMetadataCondition` | [HostMetadataCondition](#HostMetadataCondition) | - | Required |

##### The `linuxDetectionCondition` object

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| Rule scope `ruleType` | enum | The element has these enums * `RuleTypeOsService` * `RuleTypeHost` | Optional |
| Service property `property` | enum | The element has these enums * `ServiceName` * `StartupType` | Required |
| Condition `condition` | text | This string has to match a required format. See [OS services monitoring﻿](https://dt-url.net/vl03xzk).  * `$match(ip?tables*)` – Matches string with wildcards: `*` any number (including zero) of characters and `?` exactly one character. * `$contains(ssh)` – Matches if `ssh` appears anywhere in the service's property value. * `$eq(sshd)` – Matches if `sshd` matches the service's property value exactly. * `$prefix(ss)` – Matches if `ss` matches the prefix of the service's property value. * `$suffix(hd)` – Matches if `hd` matches the suffix of the service's property value.  Available logic operations:  * `$not($eq(sshd))` – Matches if the service's property value is different from `sshd`. * `$and($prefix(ss),$suffix(hd))` – Matches if service's property value starts with `ss` and ends with `hd`. * `$or($prefix(ss),$suffix(hd))` – Matches if service's property value starts with `ss` or ends with `hd`.  Brackets **(** and **)** that are part of the matched property **must be escaped with a tilde (~)** | Required |
| Condition `startupCondition` | text | This string has to match a required format. See [OS services monitoring﻿](https://dt-url.net/vl03xzk).  * `$eq(enabled)` – Matches services with startup type equal to enabled.  Available logic operations:  * `$not($eq(enabled))` – Matches services with startup type different from enabled. * `$or($eq(enabled),$eq(disabled))` - Matches services that are either enabled or disabled.  Use one of the following values as a parameter for this condition:  * `enabled` * `enabled-runtime` * `static` * `disabled` * `indirect` * `linked` * `linked-runtime` | Required |
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