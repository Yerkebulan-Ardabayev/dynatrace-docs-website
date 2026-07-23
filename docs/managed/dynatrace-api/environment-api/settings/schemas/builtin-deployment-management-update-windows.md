---
title: Settings API - Update windows for OneAgent updates schema table
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/settings/schemas/builtin-deployment-management-update-windows
---

# Settings API - Update windows for OneAgent updates schema table

# Settings API - Update windows for OneAgent updates schema table

* Published Dec 05, 2023

### Update windows for OneAgent and ActiveGate (`builtin:deployment.management.update-windows)`

Define when automatic updates for OneAgent and ActiveGate should run.

Apply update windows at these scopes:

* **OneAgent:** environment, host group, or individual host.
* **ActiveGate:** environment or individual ActiveGate.

| Schema ID | Schema groups | Scope |
| --- | --- | --- |
| `builtin:deployment.management.update-windows` | * `group:updates` | `environment` |

Retrieve schema via Settings API

|  |  |  |
| --- | --- | --- |
| GET | Managed | `https://{your-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:deployment.management.update-windows` |
| GET | SaaS | `https://{your-environment-id}.live.dynatrace.com/api/v2/settings/schemas/builtin:deployment.management.update-windows` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:deployment.management.update-windows` |

## Authentication

To execute this request, you need an access token with **Read settings** (`settings.read`) scope. To learn how to obtain and use it, see [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Parameters

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| On/Off `enabled` | boolean | - | Required |
| Name `name` | text | - | Required |
| Recurrence `recurrence` | enum | The element has these enums * `ONCE` * `DAILY` * `WEEKLY` * `MONTHLY` | Required |
| `onceRecurrence` | [onceRecurrence](#onceRecurrence) | - | Required |
| `dailyRecurrence` | [dailyRecurrence](#dailyRecurrence) | - | Required |
| `weeklyRecurrence` | [weeklyRecurrence](#weeklyRecurrence) | - | Required |
| `monthlyRecurrence` | [monthlyRecurrence](#monthlyRecurrence) | - | Required |

##### The `onceRecurrence` object

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| Update time `recurrenceRange` | [onceWindow](#onceWindow) | - | Required |

##### The `dailyRecurrence` object

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| Every X days `every` | integer | Every **X** days:  * `1` = every day, * `2` = every two days, * `3` = every three days, * etc. | Required |
| Update time `updateTime` | [updateTime](#updateTime) | - | Required |
| Recurrence range `recurrenceRange` | [recurrenceRange](#recurrenceRange) | - | Required |

##### The `weeklyRecurrence` object

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| Day of the week `selectedWeekDays` | [selectedWeekDays](#selectedWeekDays) | - | Required |
| Every X weeks `every` | integer | Every **X** weeks:  * `1` = every week, * `2` = every two weeks, * `3` = every three weeks, * etc. | Required |
| Update time `updateTime` | [updateTime](#updateTime) | - | Required |
| Recurrence range `recurrenceRange` | [recurrenceRange](#recurrenceRange) | - | Required |

##### The `monthlyRecurrence` object

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| Day of the month `selectedMonthDay` | integer | - | Required |
| Every X months `every` | integer | Every **X** months:  * `1` = every month, * `2` = every two months, * `3` = every three months, * etc. | Required |
| Update time `updateTime` | [updateTime](#updateTime) | - | Required |
| Recurrence range `recurrenceRange` | [recurrenceRange](#recurrenceRange) | - | Required |

##### The `onceWindow` object

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| Start `start` | zoned\_date\_time | - | Required |
| End `end` | zoned\_date\_time | - | Required |

##### The `updateTime` object

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| Start time (24-hour clock) `startTime` | text | - | Required |
| Time zone `timeZone` | enum | The element has these enums * `GMT-12:00` * `GMT-11:00` * `GMT-10:00` * `GMT-09:00` * `GMT-08:00` * `GMT-07:00` * `GMT-06:00` * `GMT-05:00` * `GMT-04:00` * `GMT-03:00` * `GMT-02:00` * `GMT-01:00` * `GMT+00:00` * `GMT+01:00` * `GMT+02:00` * `GMT+03:00` * `GMT+04:00` * `GMT+05:00` * `GMT+06:00` * `GMT+07:00` * `GMT+08:00` * `GMT+09:00` * `GMT+10:00` * `GMT+11:00` * `GMT+12:00` | Required |
| Duration (minutes) `duration` | integer | - | Required |

##### The `recurrenceRange` object

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| Start `start` | zoned\_date\_time | - | Required |
| End `end` | zoned\_date\_time | - | Required |

##### The `selectedWeekDays` object

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| Monday `monday` | boolean | - | Required |
| Tuesday `tuesday` | boolean | - | Required |
| Wednesday `wednesday` | boolean | - | Required |
| Thursday `thursday` | boolean | - | Required |
| Friday `friday` | boolean | - | Required |
| Saturday `saturday` | boolean | - | Required |
| Sunday `sunday` | boolean | - | Required |