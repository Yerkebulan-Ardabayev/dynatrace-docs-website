---
title: Settings API - Maintenance windows schema table
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/settings/schemas/builtin-alerting-maintenance-window
---

# Settings API - Maintenance windows schema table

# Settings API - Maintenance windows schema table

* Published Dec 05, 2023

### Maintenance windows (`builtin:alerting.maintenance-window)`

Maintenance windows are typically planned, recurring periods of system downtime during which your DevOps team can perform preventative maintenance and system upgrades outside of peak traffic hours. [Documentation﻿](https://dt-url.net/5902ho9 "How to define a maintenance window")

To avoid having Dynatrace report on any performance anomalies that may result from such events, set up maintenance windows below that correspond with your organization's maintenance window schedule.

| Schema ID | Schema groups | Scope |
| --- | --- | --- |
| `builtin:alerting.maintenance-window` | * `group:maintenance` | `environment` |

Retrieve schema via Settings API

|  |  |  |
| --- | --- | --- |
| GET | Managed | `https://{your-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:alerting.maintenance-window` |
| GET | SaaS | `https://{your-environment-id}.live.dynatrace.com/api/v2/settings/schemas/builtin:alerting.maintenance-window` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:alerting.maintenance-window` |

## Authentication

To execute this request, you need an access token with **Read settings** (`settings.read`) scope. To learn how to obtain and use it, see [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Parameters

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| Enabled `enabled` | boolean | The status of the maintenance window. If `false`, it is not considered during the maintenance window evaluation. | Required |
| `generalProperties` | [GeneralProperties](#GeneralProperties) | - | Required |
| `schedule` | [Schedule](#Schedule) | - | Required |
| `filters` | Set<[Filter](#Filter)> | Add filters to limit the scope of maintenance to only select matching entities. If no filter is defined, the maintenance window is valid for the whole environment. Each filter is evaluated separately (**OR**). | Required |

##### The `GeneralProperties` object

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| Name `name` | text | - | Required |
| Description `description` | text | A short description of the maintenance purpose. | Optional |
| Maintenance type `maintenanceType` | enum | Whether the maintenance is planned or unplanned. The element has these enums * `PLANNED` * `UNPLANNED` | Required |
| Problem detection and alerting `suppression` | enum | Defines if alerting or problem generation is disabled.  * **Detect problems and alert**: Problems are generated and alerted. * **Detect problems but don't alert**: Problems are generated but no alerts are sent out. * **Disable problem detection during maintenance**: Neither problems are generated nor alerts are sent out. The element has these enums * `DETECT_PROBLEMS_AND_ALERT` * `DETECT_PROBLEMS_DONT_ALERT` * `DONT_DETECT_PROBLEMS` | Required |
| Disable synthetic monitor execution `disableSyntheticMonitorExecution` | boolean | Disables the execution of the synthetic monitors that are within [the scope of this maintenance window﻿](https://dt-url.net/0e0341m). | Required |

##### The `Schedule` object

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| Recurrence `scheduleType` | enum | Defines the recurrence type of the maintenance window.  * **Once**: One time maintenance window with start and end date time. * **Daily**: Maintenance window occurs every day during the configured time window. * **Weekly**: Maintenance window occurs each week on one day during the configured time window. * **Monthly**: Maintenance window occurs each month on one day during the configured time window. The element has these enums * `ONCE` * `DAILY` * `WEEKLY` * `MONTHLY` | Required |
| `onceRecurrence` | [OnceRecurrence](#OnceRecurrence) | - | Required |
| `dailyRecurrence` | [DailyRecurrence](#DailyRecurrence) | - | Required |
| `weeklyRecurrence` | [WeeklyRecurrence](#WeeklyRecurrence) | - | Required |
| `monthlyRecurrence` | [MonthlyRecurrence](#MonthlyRecurrence) | - | Required |

##### The `Filter` object

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| Entity type `entityType` | text | Type of entities this maintenance window should match.  If no entity type is selected all entities regardless of the type will match. | Optional |
| Entity `entityId` | text | A specific entity that should match this maintenance window.  **Note**: If an entity type filter value is set, it must be equal to the type of the selected entity. Otherwise this maintenance window will not match. | Optional |
| Entity tags `entityTags` | set | Entities which contain all of the configured tags will match this maintenance window. It is recommended to use manual tags.  **Note:** Automatically applied tags may experience delays or inconsistencies due to rule complexity and attribute variability. Entities may not be immediately tagged, impacting filter effectiveness.  It is recommended to use manual tags instead.  For more information, visit our [best practices for tagging documentation page﻿](https://dt-url.net/8203d4x). | Required |
| Management zones `managementZones` | set | Entities which are part of all the configured management zones will match this maintenance window. It is recommended to use manual tags instead.  **Note:** Management zones may experience delays or inconsistencies due to rule complexity and attribute variability. Entities may not be immediately assigned to management zones, impacting filter effectiveness.  It is recommended to use manual tags instead.  For more information, visit our [best practices for management zones documentation page﻿](https://dt-url.net/8203d4x). | Required |

##### The `OnceRecurrence` object

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| Start time `startTime` | local\_date\_time | - | Required |
| End time `endTime` | local\_date\_time | - | Required |
| Timezone `timeZone` | time\_zone | - | Required |

##### The `DailyRecurrence` object

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| Time window `timeWindow` | [TimeWindow](#TimeWindow) | - | Required |
| Recurrence range `recurrenceRange` | [RecurrenceRange](#RecurrenceRange) | - | Required |

##### The `WeeklyRecurrence` object

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| Day of week `dayOfWeek` | enum | The element has these enums * `MONDAY` * `TUESDAY` * `WEDNESDAY` * `THURSDAY` * `FRIDAY` * `SATURDAY` * `SUNDAY` | Required |
| Time window `timeWindow` | [TimeWindow](#TimeWindow) | - | Required |
| Recurrence range `recurrenceRange` | [RecurrenceRange](#RecurrenceRange) | - | Required |

##### The `MonthlyRecurrence` object

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| Day of month `dayOfMonth` | integer | If the selected day does not fall within the month, the maintenance window will be active on the last day of the month. | Required |
| Time window `timeWindow` | [TimeWindow](#TimeWindow) | - | Required |
| Recurrence range `recurrenceRange` | [RecurrenceRange](#RecurrenceRange) | - | Required |

##### The `TimeWindow` object

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| Start time `startTime` | local\_time | - | Required |
| End time `endTime` | local\_time | - | Required |
| Timezone `timeZone` | time\_zone | - | Required |

##### The `RecurrenceRange` object

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| Start date `scheduleStartDate` | local\_date | - | Required |
| End date `scheduleEndDate` | local\_date | - | Required |