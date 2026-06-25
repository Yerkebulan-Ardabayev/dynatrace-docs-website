---
title: Settings API - Update windows for OneAgent updates schema table
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/settings/schemas/builtin-deployment-management-update-windows
scraped: 2026-05-12T11:41:30.622902
---

# Settings API - Update windows for OneAgent updates schema table

# Settings API - Update windows for OneAgent updates schema table

* Published Dec 05, 2023

### Окна обновления для OneAgent (`builtin:deployment.management.update-windows)`

Задайте окна обновления: как часто и когда обновлять instances OneAgent. Вы сможете применить эти окна к OneAgents, Host Groups или ко всему Environment в экранах настроек Automatic Update.

| Schema ID | Schema groups | Scope |
| --- | --- | --- |
| `builtin:deployment.management.update-windows` | * `group:updates` | `environment` |

Получить schema через Settings API

|  |  |  |
| --- | --- | --- |
| GET | Managed | `https://{your-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:deployment.management.update-windows` |
| GET | SaaS | `https://{your-environment-id}.live.dynatrace.com/api/v2/settings/schemas/builtin:deployment.management.update-windows` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:deployment.management.update-windows` |

## Аутентификация

Для выполнения запроса необходим access token со scope **Read settings** (`settings.read`). О том, как получить и использовать токен, см. [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Параметры

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| Вкл./Выкл. `enabled` | boolean | - | Required |
| Имя `name` | text | - | Required |
| Периодичность `recurrence` | enum | Возможные значения: * `ONCE` * `DAILY` * `WEEKLY` * `MONTHLY` | Required |
| `onceRecurrence` | [onceRecurrence](#onceRecurrence) | - | Required |
| `dailyRecurrence` | [dailyRecurrence](#dailyRecurrence) | - | Required |
| `weeklyRecurrence` | [weeklyRecurrence](#weeklyRecurrence) | - | Required |
| `monthlyRecurrence` | [monthlyRecurrence](#monthlyRecurrence) | - | Required |

##### Объект `onceRecurrence`

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| Время обновления `recurrenceRange` | [onceWindow](#onceWindow) | - | Required |

##### Объект `dailyRecurrence`

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| Каждые X дней `every` | integer | Каждые **X** дней:  * `1` = ежедневно, * `2` = раз в два дня, * `3` = раз в три дня, * и т. д. | Required |
| Время обновления `updateTime` | [updateTime](#updateTime) | - | Required |
| Диапазон периодичности `recurrenceRange` | [recurrenceRange](#recurrenceRange) | - | Required |

##### Объект `weeklyRecurrence`

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| День недели `selectedWeekDays` | [selectedWeekDays](#selectedWeekDays) | - | Required |
| Каждые X недель `every` | integer | Каждые **X** недель:  * `1` = еженедельно, * `2` = раз в две недели, * `3` = раз в три недели, * и т. д. | Required |
| Время обновления `updateTime` | [updateTime](#updateTime) | - | Required |
| Диапазон периодичности `recurrenceRange` | [recurrenceRange](#recurrenceRange) | - | Required |

##### Объект `monthlyRecurrence`

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| День месяца `selectedMonthDay` | integer | - | Required |
| Каждые X месяцев `every` | integer | Каждые **X** месяцев:  * `1` = ежемесячно, * `2` = раз в два месяца, * `3` = раз в три месяца, * и т. д. | Required |
| Время обновления `updateTime` | [updateTime](#updateTime) | - | Required |
| Диапазон периодичности `recurrenceRange` | [recurrenceRange](#recurrenceRange) | - | Required |

##### Объект `onceWindow`

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| Начало `start` | zoned\_date\_time | - | Required |
| Конец `end` | zoned\_date\_time | - | Required |

##### Объект `updateTime`

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| Время начала (24-часовой формат) `startTime` | text | - | Required |
| Часовой пояс `timeZone` | enum | Возможные значения: * `GMT-12:00` * `GMT-11:00` * `GMT-10:00` * `GMT-09:00` * `GMT-08:00` * `GMT-07:00` * `GMT-06:00` * `GMT-05:00` * `GMT-04:00` * `GMT-03:00` * `GMT-02:00` * `GMT-01:00` * `GMT+00:00` * `GMT+01:00` * `GMT+02:00` * `GMT+03:00` * `GMT+04:00` * `GMT+05:00` * `GMT+06:00` * `GMT+07:00` * `GMT+08:00` * `GMT+09:00` * `GMT+10:00` * `GMT+11:00` * `GMT+12:00` | Required |
| Длительность (минуты) `duration` | integer | - | Required |

##### Объект `recurrenceRange`

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| Начало `start` | zoned\_date\_time | - | Required |
| Конец `end` | zoned\_date\_time | - | Required |

##### Объект `selectedWeekDays`

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| Понедельник `monday` | boolean | - | Required |
| Вторник `tuesday` | boolean | - | Required |
| Среда `wednesday` | boolean | - | Required |
| Четверг `thursday` | boolean | - | Required |
| Пятница `friday` | boolean | - | Required |
| Суббота `saturday` | boolean | - | Required |
| Воскресенье `sunday` | boolean | - | Required |