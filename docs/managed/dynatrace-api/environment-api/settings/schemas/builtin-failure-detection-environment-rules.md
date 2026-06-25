---
title: Settings API - Failure detection rules schema table
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/settings/schemas/builtin-failure-detection-environment-rules
scraped: 2026-05-12T11:42:47.155668
---

# Settings API - Failure detection rules schema table

# Settings API - Failure detection rules schema table

* Published Dec 05, 2023

### Failure detection rules (`builtin:failure-detection.environment.rules)`

Configure rules which services certain failure detection parameters (`<your-dynatrace-url>//ui/settings/builtin:failure-detection.environment.parameters`) should apply to. For more information please refer to [Failure detection settingsï»¿](https://dt-url.net/7v034gp).

These settings are not applied to [Unified servicesï»¿](https://dt-url.net/gy03cmt).

| Schema ID | Schema groups | Scope |
| --- | --- | --- |
| `builtin:failure-detection.environment.rules` | * `group:service-monitoring` * `group:failure-detection` | `environment` |

Retrieve schema via Settings API

|  |  |  |
| --- | --- | --- |
| GET | Managed | `https://{your-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:failure-detection.environment.rules` |
| GET | SaaS | `https://{your-environment-id}.live.dynatrace.com/api/v2/settings/schemas/builtin:failure-detection.environment.rules` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:failure-detection.environment.rules` |

## Authentication

To execute this request, you need an access token with **Read settings** (`settings.read`) scope. To learn how to obtain and use it, see [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Parameters

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| Rule name `name` | text | - | Required |
| Rule description `description` | text | - | Optional |
| Enabled `enabled` | boolean | - | Required |
| Failure detection parameters `parameterId` | setting | - | Required |
| Conditions `conditions` | Set<[condition](#condition)> | - | Required |

##### The `condition` object

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| Attribute `attribute` | enum | The attribute to be checked. The element has these enums * `PG_NAME` * `PG_TAG` * `SERVICE_MANAGEMENT_ZONE` * `SERVICE_NAME` * `SERVICE_TYPE` * `SERVICE_TAG` | Required |
| Condition to check the attribute against `predicate` | [predicate](#predicate) | - | Required |

##### The `predicate` object

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| Predicate type `predicateType` | text | - | Required |
| Names `textValues` | set | - | Required |
| Case sensitive `caseSensitive` | boolean | - | Required |
| Service types `serviceType` | Set<[serviceTypes](#serviceTypes)> | The element has these enums * `WebRequest` * `WebService` * `Database` * `Method` * `WebSite` * `Messaging` * `Mobile` * `Process` * `RMI` * `External` * `QueueListener` * `QueueInteraction` * `RemoteCall` * `SaasVendor` * `CustomApplication` * `CICS` * `IMS` * `CICSInteraction` * `IMSInteraction` * `EnterpriseServiceBus` * `zOSConnect` | Required |
| Management zones `managementZones` | set | - | Required |
| Tags (exact match) `tags` | set | - | Required |
| Tag keys `tagKeys` | set | - | Required |