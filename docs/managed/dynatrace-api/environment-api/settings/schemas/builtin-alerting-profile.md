---
title: Settings API - Problem alerting profiles schema table
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/settings/schemas/builtin-alerting-profile
scraped: 2026-05-12T11:41:10.433090
---

# Settings API - Problem alerting profiles schema table

# Settings API - Problem alerting profiles schema table

* Published Dec 05, 2023

### Problem alerting profiles (`builtin:alerting.profile)`

Alerting profiles enable you to set up fine-grained alert-filtering rules that are based on the severity, customer impact, associated tags, and/or duration of detected problems. They enable you to control exactly which conditions result in problem notifications and which don't. Alerting profiles can also be used to set up filtered problem-notification integrations with 3rd party messaging systems like Slack, Splunk On-Call, and PagerDuty.

| Schema ID | Schema groups | Scope |
| --- | --- | --- |
| `builtin:alerting.profile` | * `group:alerting` | `environment` |

Retrieve schema via Settings API

|  |  |  |
| --- | --- | --- |
| GET | Managed | `https://{your-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:alerting.profile` |
| GET | SaaS | `https://{your-environment-id}.live.dynatrace.com/api/v2/settings/schemas/builtin:alerting.profile` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:alerting.profile` |

## Authentication

To execute this request, you need an access token with **Read settings** (`settings.read`) scope. To learn how to obtain and use it, see [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Parameters

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| Name `name` | text | - | Required |
| Management zone `managementZone` | setting | Entities which are part of the configured management zones will match this alerting profile. It is recommended to use manual tags instead.  **Note:** Management zones may experience delays or inconsistencies due to rule complexity and attribute variability. Entities may not be immediately assigned to management zones, impacting filter effectiveness.  It is recommended to use manual tags instead.  For more information, visit our [best practices for management zones documentation pageï»¿](https://dt-url.net/8203d4x). | Optional |
| Severity rules `severityRules` | Set<[AlertingProfileSeverityRule](#AlertingProfileSeverityRule)> | Define severity rules for profile. A maximum of 100 severity rules is allowed. | Required |
| Event filters `eventFilters` | Set<[AlertingProfileEventFilter](#AlertingProfileEventFilter)> | Define event filters for profile. A maximum of 100 event filters is allowed. | Required |

##### The `AlertingProfileSeverityRule` object

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| Problem severity level `severityLevel` | enum | The element has these enums * `AVAILABILITY` * `CUSTOM_ALERT` * `ERRORS` * `MONITORING_UNAVAILABLE` * `PERFORMANCE` * `RESOURCE_CONTENTION` | Required |
| Problem send delay in minutes `delayInMinutes` | integer | Send a notification if a problem remains open longer than X minutes. | Required |
| Filter problems by tag `tagFilterIncludeMode` | enum | The element has these enums * `NONE` * `INCLUDE_ANY` * `INCLUDE_ALL` | Required |
| Tags `tagFilter` | set | Entities which contain any/all of the configured tags will match this alerting profile. It is recommended to use manual tags.  **Note:** Automatically applied tags may experience delays or inconsistencies due to rule complexity and attribute variability. Entities may not be immediately tagged, impacting filter effectiveness.  It is recommended to use manual tags instead.  For more information, visit our [best practices for tagging documentation pageï»¿](https://dt-url.net/8203d4x). | Required |

##### The `AlertingProfileEventFilter` object

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| Filter problems by any event of source `type` | enum | The element has these enums * `PREDEFINED` * `CUSTOM` | Required |
| `predefinedFilter` | [PredefinedEventFilter](#PredefinedEventFilter) | - | Required |
| `customFilter` | [CustomEventFilter](#CustomEventFilter) | - | Required |

##### The `PredefinedEventFilter` object

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| Filter problems by a Dynatrace event type `eventType` | enum | The element has these enums * `EC2_HIGH_CPU` * `OSI_HIGH_CPU` * `ELB_HIGH_BACKEND_ERROR_RATE` * `PROCESS_NA_HIGH_CONN_FAIL_RATE` * `CUSTOM_APP_CRASH_RATE_INCREASED` * `CUSTOM_APPLICATION_ERROR_RATE_INCREASED` * `CUSTOM_APPLICATION_SLOWDOWN` * `CUSTOM_APPLICATION_UNEXPECTED_LOW_LOAD` * `CUSTOM_APPLICATION_UNEXPECTED_HIGH_LOAD` * `ESXI_GUEST_CPU_LIMIT_REACHED` * `ESXI_GUEST_ACTIVE_SWAP_WAIT` * `ESXI_HOST_CPU_SATURATION` * `ESXI_HOST_MEMORY_SATURATION` * `ESXI_VM_IMPACT_HOST_CPU_SATURATION` * `ESXI_VM_IMPACT_HOST_MEMORY_SATURATION` * `ESXI_HOST_NETWORK_PROBLEMS` * `ESXI_HOST_DISK_SLOW` * `EBS_VOLUME_HIGH_LATENCY` * `DATABASE_CONNECTION_FAILURE` * `SERVICE_ERROR_RATE_INCREASED` * `RDS_HIGH_LATENCY` * `OSI_NIC_UTILIZATION_HIGH` * `OSI_NIC_ERRORS_HIGH` * `OSI_NIC_DROPPED_PACKETS_HIGH` * `OSI_GRACEFULLY_SHUTDOWN` * `OSI_UNEXPECTEDLY_UNAVAILABLE` * `HOST_OF_SERVICE_UNAVAILABLE` * `ESXI_HOST_DISK_QUEUE_SLOW` * `APPLICATION_ERROR_RATE_INCREASED` * `AWS_LAMBDA_HIGH_ERROR_RATE` * `PROCESS_HIGH_GC_ACTIVITY` * `ESXI_HOST_DATASTORE_LOW_DISK_SPACE` * `OSI_LOW_DISK_SPACE` * `OSI_DISK_LOW_INODES` * `RDS_LOW_STORAGE_SPACE` * `PROCESS_MEMORY_RESOURCE_EXHAUSTED` * `OSI_HIGH_MEMORY` * `MOBILE_APP_CRASH_RATE_INCREASED` * `MOBILE_APPLICATION_ERROR_RATE_INCREASED` * `MOBILE_APPLICATION_SLOWDOWN` * `MOBILE_APPLICATION_UNEXPECTED_LOW_LOAD` * `MOBILE_APPLICATION_UNEXPECTED_HIGH_LOAD` * `MONITORING_UNAVAILABLE` * `PROCESS_NA_HIGH_LOSS_RATE` * `ESXI_HOST_OVERLOADED_STORAGE` * `PROCESS_CRASHED` * `PG_LOW_INSTANCE_COUNT` * `PGI_UNAVAILABLE` * `RDS_HIGH_CPU` * `RDS_LOW_MEMORY` * `RDS_OF_SERVICE_UNAVAILABLE` * `SERVICE_SLOWDOWN` * `RDS_RESTART_SEQUENCE` * `PGI_OF_SERVICE_UNAVAILABLE` * `OSI_SLOW_DISK` * `SYNTHETIC_NODE_OUTAGE` * `SYNTHETIC_PRIVATE_LOCATION_OUTAGE` * `PROCESS_THREADS_RESOURCE_EXHAUSTED` * `SERVICE_UNEXPECTED_HIGH_LOAD` * `APPLICATION_UNEXPECTED_HIGH_LOAD` * `SERVICE_UNEXPECTED_LOW_LOAD` * `APPLICATION_UNEXPECTED_LOW_LOAD` * `APPLICATION_SLOWDOWN` * `SYNTHETIC_GLOBAL_OUTAGE` * `SYNTHETIC_LOCAL_OUTAGE` * `SYNTHETIC_TEST_LOCATION_SLOWDOWN` * `HTTP_CHECK_GLOBAL_OUTAGE` * `HTTP_CHECK_LOCAL_OUTAGE` * `HTTP_CHECK_TEST_LOCATION_SLOWDOWN` * `MULTI_PROTOCOL_GLOBAL_OUTAGE` * `MULTI_PROTOCOL_LOCAL_OUTAGE` * `MULTI_PROTOCOL_LOCATION_SLOWDOWN` * `EXTERNAL_SYNTHETIC_TEST_OUTAGE` * `EXTERNAL_SYNTHETIC_TEST_SLOWDOWN` | Required |
| Negate `negate` | boolean | - | Required |

##### The `CustomEventFilter` object

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| Title filter `titleFilter` | [TextFilter](#TextFilter) | - | Optional |
| Description filter `descriptionFilter` | [TextFilter](#TextFilter) | - | Optional |
| Property filters `metadataFilter` | [MetadataFilter](#MetadataFilter) | - | Optional |

##### The `TextFilter` object

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| Operator of the comparison `operator` | enum | The element has these enums * `BEGINS_WITH` * `ENDS_WITH` * `CONTAINS` * `REGEX_MATCHES` * `STRING_EQUALS` | Required |
| Value `value` | text | - | Required |
| Negate `negate` | boolean | - | Required |
| Enabled `enabled` | boolean | - | Required |
| Case sensitive `caseSensitive` | boolean | - | Required |

##### The `MetadataFilter` object

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| `metadataFilterItems` | Set<[MetadataFilterItem](#MetadataFilterItem)> | Define filters for event properties. A maximum of 20 properties is allowed. | Required |

##### The `MetadataFilterItem` object

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| Key `metadataKey` | text | Type 'dt.' for key hints. | Required |
| Value `metadataValue` | text | - | Required |
| Negate `negate` | boolean | - | Required |