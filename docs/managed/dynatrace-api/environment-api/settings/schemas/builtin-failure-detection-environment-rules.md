---
title: Settings API - Failure detection rules schema table
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/settings/schemas/builtin-failure-detection-environment-rules
---

# Settings API - Failure detection rules schema table

# Settings API - Failure detection rules schema table

* Published Dec 05, 2023

### Failure detection rules (`builtin:failure-detection.environment.rules)`

Configure rules which services certain failure detection parameters (`<your-dynatrace-url>//ui/settings/builtin:failure-detection.environment.parameters`) should apply to. For more information please refer to [Failure detection settings﻿](https://dt-url.net/7v034gp).

These settings are not applied to [Unified services﻿](https://dt-url.net/gy03cmt).

To programmatically manage these settings, see [API Reference﻿](https://docs.dynatrace.com/docs/shortlink/service-failure-detection#settings-api).

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
| Rule name `name` | text | The display name of this failure detection rule. | Required |
| Rule description `description` | text | A short description of this failure detection rule. | Optional |
| Enabled `enabled` | boolean | Whether this rule is enabled. Disabled rules are not evaluated. | Required |
| Failure detection parameters `parameterId` | setting | The ID of the failure detection parameter set to apply when this rule matches. The parameter set must already exist. | Required |
| Conditions `conditions` | Set<[condition](#condition)> | A list of conditions for this rule. All conditions must be fulfilled for the rule to match a service. | Required |

##### The `condition` object

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| Attribute `attribute` | enum | The attribute to be checked. The element has these enums * `PG_NAME` * `PG_TAG` * `SERVICE_MANAGEMENT_ZONE` * `SERVICE_NAME` * `SERVICE_TYPE` * `SERVICE_TAG` | Required |
| Condition to check the attribute against `predicate` | [predicate](#predicate) | The predicate that tests the value of the attribute.  The actual set of fields depends on the type of the predicate. Find the list of actual objects in the description of the type field or see [Failure detection API - JSON models﻿](https://dt-url.net/9sg3swf). | Required |

##### The `predicate` object

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| Predicate type `predicateType` | text | The type of predicate to apply. Available types depend on the condition attribute:  * `SERVICE_NAME` and `PG_NAME` support `STRING_EQUALS`, `STARTS_WITH`, `ENDS_WITH`, `CONTAINS`; * `SERVICE_TYPE` supports `SERVICE_TYPE_EQUALS`; * `SERVICE_MANAGEMENT_ZONE` supports `MANAGEMENT_ZONES_CONTAINS_ALL`; * `SERVICE_TAG` and `PG_TAG` support `TAG_EQUALS` and `TAG_KEY_EQUALS`. | Required |
| Names `textValues` | set | A list of text values to match against. The rule matches if the attribute value matches any of these values according to the predicate type. | Required |
| Case sensitive `caseSensitive` | boolean | If `true`, the string comparison is case-sensitive. Default: `false`. | Required |
| Service types `serviceType` | Set<[serviceTypes](#serviceTypes)> | A set of service types to match against. The rule matches if the service type is contained in this set. Only applicable for predicate type `SERVICE_TYPE_EQUALS`. The element has these enums * `WebRequest` * `WebService` * `Database` * `Method` * `WebSite` * `Messaging` * `Mobile` * `Process` * `RMI` * `External` * `QueueListener` * `QueueInteraction` * `RemoteCall` * `SaasVendor` * `CustomApplication` * `CICS` * `IMS` * `CICSInteraction` * `IMSInteraction` * `EnterpriseServiceBus` * `zOSConnect` | Required |
| Management zones `managementZones` | set | A set of management zone references. The rule matches if the service belongs to all specified management zones. Only applicable for predicate type `MANAGEMENT_ZONES_CONTAINS_ALL`. | Required |
| Tags (exact match) `tags` | set | A set of tags to match exactly. The rule matches if the entity has all specified tags (both key and value must match). Only applicable for predicate type `TAG_EQUALS`. | Required |
| Tag keys `tagKeys` | set | A set of tag keys to match. The rule matches if the entity has tags with all specified keys, regardless of tag value. Only applicable for predicate type `TAG_KEY_EQUALS`. | Required |