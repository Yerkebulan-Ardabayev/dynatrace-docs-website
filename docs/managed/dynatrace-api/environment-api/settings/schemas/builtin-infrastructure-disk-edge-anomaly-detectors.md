---
title: Settings API - Anomaly detection for infrastructure- Disk Edge schema table
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/settings/schemas/builtin-infrastructure-disk-edge-anomaly-detectors
---

# Settings API - Anomaly detection for infrastructure- Disk Edge schema table

# Settings API - Anomaly detection for infrastructure- Disk Edge schema table

* Published Jul 31, 2024

### Anomaly detection for infrastructure: Disk Edge (`builtin:infrastructure.disk.edge.anomaly-detectors)`

The *Disk Edge* feature within Dynatrace provides automatic detection of performance anomalies related to disk infrastructure.
Use these settings to tailor detection sensitivity based on disk characteristics such as disk name, total space, filesystem type, disk type, and/or custom metadata. Defining custom properties can help with post processing of the event.

**Policy Hierarchy and Scope**

The order of policies establishes a hierarchical structure. Disk is assigned to the first policy it matches to (based on disk name, total space, filesystem type, disk type, and/or metadata) according to the policies hierarchy.

Policies can be defined within Host, Host Group and Tenant scope. Lower scope has priority over the higher one.

To learn more about Disk Edge visit its [official documentation﻿](https://dt-url.net/diskEdgeDoc).

| Schema ID | Schema groups | Scope |
| --- | --- | --- |
| `builtin:infrastructure.disk.edge.anomaly-detectors` | * `group:anomaly-detection.infrastructure` * `group:anomaly-detection` | `HOST` - Host  `HOST_GROUP` - Host Group  `environment` |

Retrieve schema via Settings API

|  |  |  |
| --- | --- | --- |
| GET | Managed | `https://{your-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:infrastructure.disk.edge.anomaly-detectors` |
| GET | SaaS | `https://{your-environment-id}.live.dynatrace.com/api/v2/settings/schemas/builtin:infrastructure.disk.edge.anomaly-detectors` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:infrastructure.disk.edge.anomaly-detectors` |

## Authentication

To execute this request, you need an access token with **Read settings** (`settings.read`) scope. To learn how to obtain and use it, see [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Parameters

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| Policy name `policyName` | text | - | Required |
| Enabled `enabled` | boolean | - | Required |
| Operating system `operatingSystem` | Set<[EOperatingSystem](#EOperatingSystem)> | Select the operating systems on which policy should be applied The element has these enums * `WINDOWS` * `LINUX` * `AIX` | Required |
| Alerts `alerts` | Set<[Alert](#Alert)> | - | Required |
| Disk name filters `diskNameFilters` | set | Disk will be included in this policy if **any** of the filters match  Disk name filter has to match a required format.  * `$match(/zSecure/snapshot?/*)` – Matches string with wildcards: `*` any number (including zero) of characters and `?` exactly one character. * `$contains(/log/)` – Matches if `/log/` appears anywhere in disk name. * `$eq(/)` – Matches if `/` matches the disk name exactly. * `$prefix(/srv/)` – Matches if `/srv/` matches the prefix of disk name. * `$suffix(/backup)` – Matches if `/backup` matches the suffix of disk name.  Available logic operations:  * `$not($eq(/usr))` – Matches if the disk name is different from `/usr`. * `$and($prefix(/var),$suffix(/backup))` – Matches if disk name starts with `/var` and ends with `/backup`. * `$or($prefix(/home/),$eq(/root))` – Matches if disk name starts with `/home` or equals `/root`.  Brackets **(** and **)** that are part of the matched disk name **must be escaped with a tilde (~)** | Required |
| Detection rules `detectionConditions` | [detectionCondition](#detectionCondition)[] | Set of rules to scope which disks the policy applies to. Rules can match based on disk properties (total space, filesystem, disk type) or host resource attributes. Each disk property type can be defined at most once per policy. | Required |
| Properties `eventProperties` | Set<[MetadataItem](#MetadataItem)> | Set of additional key-value properties to be attached to the triggered event. You can retrieve the available property keys using the [Events API v2﻿](https://dt-url.net/9622g1w). Additionally any Host resource attribute can be dynamically substituted (agent 1.325+) | Required |

##### The `Alert` object

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| Trigger `trigger` | enum | The element has these enums * `AVAILABLE_DISK_SPACE_MEBIBYTES_BELOW` * `AVAILABLE_DISK_SPACE_PERCENT_BELOW` * `AVAILABLE_INODES_NUMBER_BELOW` * `AVAILABLE_INODES_PERCENT_BELOW` * `READ_TIME_EXCEEDING` * `WRITE_TIME_EXCEEDING` * `READ_ONLY_FILE_SYSTEM` | Required |
| `thresholdPercent` | float | - | Required |
| `thresholdMilliseconds` | float | - | Required |
| `thresholdMebibytes` | float | - | Required |
| `thresholdNumber` | float | - | Required |
| `sampleCountThresholdsImmediately` | [SampleCountThresholdsImmediately](#SampleCountThresholdsImmediately) | - | Required |
| `sampleCountThresholds` | [SampleCountThresholds](#SampleCountThresholds) | - | Required |

##### The `detectionCondition` object

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| Rule scope `ruleType` | enum | Starting from agent 1.335 **disk** detection rules are supported. The element has these enums * `RuleTypeDisk` * `RuleTypeHost` | Required |
| Disk property `property` | enum | The element has these enums * `DiskTotalSpace` * `DiskFilesystem` * `DiskType` | Required |
| Disk total space thresholds `diskTotalCondition` | [DiskTotalSpaceThresholds](#DiskTotalSpaceThresholds) | Specify disk total space range in GiB | Required |
| Filesystem condition `diskFilesystemCondition` | text | Disk filesystem will be included in this policy if **any** of the filters match  Disk filesystem has to match a required format.  * `$match(ext*)` – Matches string with wildcards: `*` any number (including zero) of characters and `?` exactly one character. * `$contains(fs)` – Matches if `fs` appears anywhere in the filesystem type. * `$eq(ext4)` – Matches if `ext4` matches the filesystem type exactly. * `$prefix(ext)` – Matches if `ext` matches the prefix of the filesystem type. * `$suffix(fs)` – Matches if `fs` matches the suffix of the filesystem type.  Available logic operations:  * `$not($eq(tmpfs))` – Matches if the filesystem type is different from `tmpfs`. * `$and($prefix(ext),$suffix(4))` – Matches if filesystem type starts with `ext` and ends with `4`. * `$or($eq(xfs),$eq(btrfs))` – Matches if filesystem type equals `xfs` or `btrfs`.  Brackets **(** and **)** that are part of the matched filesystem type **must be escaped with a tilde (~)** | Required |
| `localDiskCondition` | enum | The element has these enums * `LOCAL` * `REMOTE` | Required |
| Resource attribute `hostMetadataCondition` | [HostMetadataConditionType](#HostMetadataConditionType) | Host resource attributes are dimensions enriching the host including custom metadata which are user-defined key-value pairs that you can assign to hosts monitored by Dynatrace.  By defining custom metadata, you can enrich the monitoring data with context specific to your organization's needs, such as environment names, team ownership, application versions, or any other relevant details.  See [Define tags and metadata for hosts﻿](https://dt-url.net/w3hv0kbw).  Note: Starting from version 1.325 host resource attributes are supported in addition to host custom metadata. | Required |

##### The `MetadataItem` object

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| Key `metadataKey` | text | Type 'dt.' for key hints. | Required |
| Value `metadataValue` | text | Type '{' for placeholder hints. | Required |

##### The `SampleCountThresholdsImmediately` object

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| Violating samples `violatingSamples` | integer | The number of **10-second samples** within the evaluation window that must exceed the threshold to trigger an event | Required |
| Evaluation window size for violating samples `violatingEvaluationWindow` | integer | The number of **10-second samples** that form the sliding evaluation window to detect violating samples. | Required |
| Dealerting samples `dealertingSamples` | integer | The number of **10-second samples** within the evaluation window that must be lower than the threshold to close an event | Required |
| Evaluation window size for dealerting samples `dealertingEvaluationWindow` | integer | The number of **10-second samples** that form the sliding evaluation window for dealerting. | Required |

##### The `SampleCountThresholds` object

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| Violating samples `violatingSamples` | integer | The number of **10-second samples** within the evaluation window that must exceed the threshold to trigger an event | Required |
| Evaluation window size for violating samples `violatingEvaluationWindow` | integer | The number of **10-second samples** that form the sliding evaluation window to detect violating samples. | Required |
| Dealerting samples `dealertingSamples` | integer | The number of **10-second samples** within the evaluation window that must be lower than the threshold to close an event | Required |
| Evaluation window size for dealerting samples `dealertingEvaluationWindow` | integer | The number of **10-second samples** that form the sliding evaluation window for dealerting. | Required |

##### The `DiskTotalSpaceThresholds` object

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| Threshold above (optional) `thresholdAbove` | integer | If this field is empty then there is no lower limit  Minimum total disk space in GiB | Optional |
| Threshold below (optional) `thresholdBelow` | integer | If this field is empty then there is no upper limit  Maximum total disk space in GiB | Optional |

##### The `HostMetadataConditionType` object

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| `hostMetadataCondition` | [HostMetadataCondition](#HostMetadataCondition) | - | Required |

##### The `HostMetadataCondition` object

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| Key must exist `keyMustExist` | boolean | When enabled, the condition requires a resource attribute to exist and match the constraints; when disabled, the key is optional but must still match the constrains if it is present. | Required |
| Key `metadataKey` | text | - | Required |
| Condition `metadataCondition` | text | This string has to match a required format.  * `$match(ver*_1.2.?)` – Matches string with wildcards: `*` any number (including zero) of characters and `?` exactly one character. * `$contains(production)` – Matches if `production` appears anywhere in the host metadata value. * `$eq(production)` – Matches if `production` matches the host metadata value exactly. * `$prefix(production)` – Matches if `production` matches the prefix of the host metadata value. * `$suffix(production)` – Matches if `production` matches the suffix of the host metadata value.  Available logic operations:  * `$not($eq(production))` – Matches if the host metadata value is different from `production`. * `$and($prefix(production),$suffix(main))` – Matches if host metadata value starts with `production` and ends with `main`. * `$or($prefix(production),$suffix(main))` – Matches if host metadata value starts with `production` or ends with `main`.  Brackets **(** and **)** that are part of the matched property **must be escaped with a tilde (~)** | Required |