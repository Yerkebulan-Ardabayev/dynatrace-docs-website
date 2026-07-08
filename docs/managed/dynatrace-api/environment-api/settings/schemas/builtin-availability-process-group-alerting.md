---
title: Settings API - Process group availability monitoring schema table
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/settings/schemas/builtin-availability-process-group-alerting
---

# Settings API - Process group availability monitoring schema table

# Settings API - Process group availability monitoring schema table

* Published Dec 05, 2023

### Process group availability monitoring (`builtin:availability.process-group-alerting)`

Dynatrace continuously monitors the availability of this process group. Use the settings below to define the approach that Dynatrace should use for monitoring the availability of this process group.

| Schema ID | Schema groups | Scope |
| --- | --- | --- |
| `builtin:availability.process-group-alerting` | - | `PROCESS_GROUP` - Process Group |

Retrieve schema via Settings API

|  |  |  |
| --- | --- | --- |
| GET | Managed | `https://{your-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:availability.process-group-alerting` |
| GET | SaaS | `https://{your-environment-id}.live.dynatrace.com/api/v2/settings/schemas/builtin:availability.process-group-alerting` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:availability.process-group-alerting` |

## Authentication

To execute this request, you need an access token with **Read settings** (`settings.read`) scope. To learn how to obtain and use it, see [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Parameters

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| Enable process group availability monitoring `enabled` | boolean | - | Required |
| Open a new problem `alertingMode` | enum | **if any process becomes unavailable:** Dynatrace will open a new problem if a single process in this group shuts down or crashes.  **if minimum threshold is not met:** Dynatrace tracks the number of process instances that comprise this process group and treats the group as a cluster. This setting enables you to define a minimum number of process instances that must be available. A problem will be opened if this process group has fewer than the minimum number of required process instances.  Details of the related impact on service requests will be included in the problem summary.  **Note:** If a process is intentionally shutdown or retired while this setting is active, you'll need to manually close the problem. The element has these enums * `ON_PGI_UNAVAILABILITY` * `ON_INSTANCE_COUNT_VIOLATION` | Required |
| Open a new problem if the number of active process instances in the group is fewer than: `minimumInstanceThreshold` | integer | - | Required |