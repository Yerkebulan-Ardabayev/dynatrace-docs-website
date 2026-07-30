---
title: Settings API - Update windows for OneAgent and ActiveGate schema table
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/settings/schemas/builtin-deployment-management-update-windows
---

# Settings API - Update windows for OneAgent and ActiveGate schema table

# Settings API - Update windows for OneAgent and ActiveGate schema table

* Опубликовано 05 декабря 2023 г.

### Окна обновления для OneAgent и ActiveGate (`builtin:deployment.management.update-windows)`

Задаёт расписание автоматических обновлений OneAgent и ActiveGate.

Окна обновления применяются на следующих уровнях:

* **OneAgent:** среда, группа хостов или отдельный хост.
* **ActiveGate:** среда или отдельный ActiveGate.

| Schema ID | Schema groups | Scope |
| --- | --- | --- |
| `builtin:deployment.management.update-windows` | * `group:updates` | `environment` |

Получение схемы через Settings API

|  |  |  |
| --- | --- | --- |
| GET | Managed | `https://{your-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:deployment.management.update-windows` |
| GET | SaaS | `https://{your-environment-id}.live.dynatrace.com/api/v2/settings/schemas/builtin:deployment.management.update-windows` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:deployment.management.update-windows` |

## Authentication

Для выполнения этого запроса нужен токен доступа с областью видимости **Read settings** (`settings.read`). Порядок получения и использования токена описан в разделе [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Parameters

| Property | Type | Описание | Required |
| --- | --- | --- | --- |
| On/Off `enabled` | boolean | - | Required |
| Name `name` | text | - | Required |
| Recurrence `recurrence` | enum | Допустимые значения элемента: * `ONCE` * `DAILY` * `WEEKLY` * `MONTHLY` | Required |
| `onceRecurrence` | [onceRecurrence](#onceRecurrence) | - | Required |
| `dailyRecurrence` | [dailyRecurrence](#dailyRecurrence) | - | Required |
| `weeklyRecurrence` | [weeklyRecurrence](#weeklyRecurrence) | - | Required |
| `monthlyRecurrence` | [monthlyRecurrence](#monthlyRecurrence) | - | Required |

##### Объект `onceRecurrence`

| Property | Type | Описание | Required |
| --- | --- | --- | --- |
| Update time `recurrenceRange` | [onceWindow](#onceWindow) | - | Required |

##### Объект `dailyRecurrence`

| Property | Type | Описание | Required |
| --- | --- | --- | --- |
| Every X days `every` | integer | Каждые **X** дней: * `1` = каждый день, * `2` = каждые два дня, * `3` = каждые три дня, * и т.д. | Required |
| Update time `updateTime` | [updateTime](#updateTime) | - | Required |
| Recurrence range `recurrenceRange` | [recurrenceRange](#recurrenceRange) | - | Required |

##### Объект `weeklyRecurrence`

| Property | Type | Описание | Required |
| --- | --- | --- | --- |
| Day of the week `selectedWeekDays` | [selectedWeekDays](#selectedWeekDays) | - | Required |
| Every X weeks `every` | integer | Каждые **X** недель: * `1` = каждую неделю, * `2` = каждые две недели, * `3` = каждые три недели, * и т.д. | Required |
| Update time `updateTime` | [updateTime](#updateTime) | - | Required |
| Recurrence range `recurrenceRange` | [recurrenceRange](#recurrenceRange) | - | Required |

##### Объект `monthlyRecurrence`

| Property | Type | Описание | Required |
| --- | --- | --- | --- |
| Day of the month `selectedMonthDay` | integer | - | Required |
| Every X months `every` | integer | Каждые **X** месяцев: * `1` = каждый месяц, * `2` = каждые два месяца, * `3` = каждые три месяца, * и т.д. | Required |
| Update time `updateTime` | [updateTime](#updateTime) | - | Required |
| Recurrence range `recurrenceRange` | [recurrenceRange](#recurrenceRange) | - | Required |

##### Объект `onceWindow`

| Property | Type | Описание | Required |
| --- | --- | --- | --- |
| Start `start` | zoned\_date\_time | - | Required |
| End `end` | zoned\_date\_time | - | Required |

##### Объект `updateTime`

| Property | Type | Описание | Required |
| --- | --- | --- | --- |
| Start time (24-hour clock) `startTime` | text | - | Required |
| Time zone `timeZone` | enum | Допустимые значения элемента: * `GMT-12:00` * `GMT-11:00` * `GMT-10:00` * `GMT-09:00` * `GMT-08:00` * `GMT-07:00` * `GMT-06:00` * `GMT-05:00` * `GMT-04:00` * `GMT-03:00` * `GMT-02:00` * `GMT-01:00` * `GMT+00:00` * `GMT+01:00` * `GMT+02:00` * `GMT+03:00` * `GMT+04:00` * `GMT+05:00` * `GMT+06:00` * `GMT+07:00` * `GMT+08:00` * `GMT+09:00` * `GMT+10:00` * `GMT+11:00` * `GMT+12:00` | Required |
| Duration (minutes) `duration` | integer | - | Required |

##### Объект `recurrenceRange`

| Property | Type | Описание | Required |
| --- | --- | --- | --- |
| Start `start` | zoned\_date\_time | - | Required |
| End `end` | zoned\_date\_time | - | Required |

##### Объект `selectedWeekDays`

| Property | Type | Описание | Required |
| --- | --- | --- | --- |
| Monday `monday` | boolean | - | Required |
| Tuesday `tuesday` | boolean | - | Required |
| Wednesday `wednesday` | boolean | - | Required |
| Thursday `thursday` | boolean | - | Required |
| Friday `friday` | boolean | - | Required |
| Saturday `saturday` | boolean | - | Required |
| Sunday `sunday` | boolean | - | Required |