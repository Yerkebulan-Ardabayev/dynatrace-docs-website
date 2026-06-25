---
title: Settings API - Maintenance windows schema table
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/settings/schemas/builtin-alerting-maintenance-window
scraped: 2026-05-12T11:44:43.607307
---

# Settings API - Maintenance windows schema table

# Settings API - Maintenance windows schema table

* Опубликовано 05 декабря 2023 г.

### Maintenance windows (`builtin:alerting.maintenance-window)`

Maintenance windows, как правило, это плановые повторяющиеся периоды downtime, в течение которых DevOps-команда выполняет профилактическое обслуживание и системные обновления вне часов пиковой нагрузки. [Documentation](https://dt-url.net/5902ho9 "How to define a maintenance window")

Чтобы Dynatrace не сообщал об аномалиях производительности, вызванных такими событиями, настройте ниже maintenance windows в соответствии с графиком обслуживания вашей организации.

| Schema ID | Группы схемы | Scope |
| --- | --- | --- |
| `builtin:alerting.maintenance-window` | * `group:maintenance` | `environment` |

Получить schema через Settings API

|  |  |  |
| --- | --- | --- |
| GET | Managed | `https://{your-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:alerting.maintenance-window` |
| GET | SaaS | `https://{your-environment-id}.live.dynatrace.com/api/v2/settings/schemas/builtin:alerting.maintenance-window` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:alerting.maintenance-window` |

## Аутентификация

Для выполнения запроса необходим access token со scope **Read settings** (`settings.read`). О том, как получить и использовать токен, см. [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Параметры

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| Включено `enabled` | boolean | Статус maintenance window. Если `false`, при вычислении maintenance window не учитывается. | Required |
| `generalProperties` | [GeneralProperties](#GeneralProperties) | - | Required |
| `schedule` | [Schedule](#Schedule) | - | Required |
| `filters` | Set<[Filter](#Filter)> | Добавьте фильтры, чтобы ограничить scope maintenance только совпадающими сущностями. Если фильтр не задан, maintenance window действует для всего environment. Каждый фильтр оценивается отдельно (**OR**). | Required |

##### Объект `GeneralProperties`

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| Имя `name` | text | - | Required |
| Описание `description` | text | Краткое описание цели обслуживания. | Optional |
| Тип обслуживания `maintenanceType` | enum | Является обслуживание плановым или внеплановым. Возможные значения: * `PLANNED` * `UNPLANNED` | Required |
| Обнаружение problem и оповещения `suppression` | enum | Определяет, отключаются ли оповещения или генерация problems.  * **Detect problems and alert**: Problems генерируются, оповещения отправляются. * **Detect problems but don't alert**: Problems генерируются, но оповещения не отправляются. * **Disable problem detection during maintenance**: Ни problems не генерируются, ни оповещения не отправляются. Возможные значения: * `DETECT_PROBLEMS_AND_ALERT` * `DETECT_PROBLEMS_DONT_ALERT` * `DONT_DETECT_PROBLEMS` | Required |
| Отключить выполнение synthetic-мониторов `disableSyntheticMonitorExecution` | boolean | Отключает выполнение synthetic-мониторов, попадающих в [the scope of this maintenance window](https://dt-url.net/0e0341m). | Required |

##### Объект `Schedule`

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| Повторяемость `scheduleType` | enum | Определяет тип повторяемости maintenance window.  * **Once**: однократное maintenance window с датой и временем начала и окончания. * **Daily**: maintenance window повторяется каждый день в заданном временном окне. * **Weekly**: maintenance window повторяется раз в неделю в один и тот же день в заданном временном окне. * **Monthly**: maintenance window повторяется раз в месяц в один и тот же день в заданном временном окне. Возможные значения: * `ONCE` * `DAILY` * `WEEKLY` * `MONTHLY` | Required |
| `onceRecurrence` | [OnceRecurrence](#OnceRecurrence) | - | Required |
| `dailyRecurrence` | [DailyRecurrence](#DailyRecurrence) | - | Required |
| `weeklyRecurrence` | [WeeklyRecurrence](#WeeklyRecurrence) | - | Required |
| `monthlyRecurrence` | [MonthlyRecurrence](#MonthlyRecurrence) | - | Required |

##### Объект `Filter`

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| Тип сущности `entityType` | text | Тип сущностей, на которые должно распространяться это maintenance window.  Если тип сущности не выбран, под фильтр попадают все сущности независимо от типа. | Optional |
| Сущность `entityId` | text | Конкретная сущность, которая должна попадать под это maintenance window.  **Note**: если задан фильтр по типу сущности, он должен соответствовать типу выбранной сущности, иначе maintenance window не сработает. | Optional |
| Теги сущности `entityTags` | set | Под фильтр попадут сущности, содержащие все настроенные теги. Рекомендуется использовать ручные теги.  **Note:** автоматически применяемые теги могут запаздывать или быть несогласованными из-за сложности правил и изменчивости атрибутов. Сущности могут получить тег не сразу, это влияет на эффективность фильтра.  Лучше использовать ручные теги.  Подробнее см. [best practices for tagging documentation page](https://dt-url.net/8203d4x). | Required |
| Management zones `managementZones` | set | Под фильтр попадут сущности, входящие во все настроенные management zones. Вместо этого рекомендуется использовать ручные теги.  **Note:** management zones могут запаздывать или быть несогласованными из-за сложности правил и изменчивости атрибутов. Сущности могут попасть в management zone не сразу, это влияет на эффективность фильтра.  Лучше использовать ручные теги.  Подробнее см. [best practices for management zones documentation page](https://dt-url.net/8203d4x). | Required |

##### Объект `OnceRecurrence`

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| Время начала `startTime` | local\_date\_time | - | Required |
| Время окончания `endTime` | local\_date\_time | - | Required |
| Часовой пояс `timeZone` | time\_zone | - | Required |

##### Объект `DailyRecurrence`

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| Временное окно `timeWindow` | [TimeWindow](#TimeWindow) | - | Required |
| Диапазон повторения `recurrenceRange` | [RecurrenceRange](#RecurrenceRange) | - | Required |

##### Объект `WeeklyRecurrence`

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| День недели `dayOfWeek` | enum | Возможные значения: * `MONDAY` * `TUESDAY` * `WEDNESDAY` * `THURSDAY` * `FRIDAY` * `SATURDAY` * `SUNDAY` | Required |
| Временное окно `timeWindow` | [TimeWindow](#TimeWindow) | - | Required |
| Диапазон повторения `recurrenceRange` | [RecurrenceRange](#RecurrenceRange) | - | Required |

##### Объект `MonthlyRecurrence`

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| День месяца `dayOfMonth` | integer | Если выбранный день в месяце отсутствует, maintenance window будет активно в последний день месяца. | Required |
| Временное окно `timeWindow` | [TimeWindow](#TimeWindow) | - | Required |
| Диапазон повторения `recurrenceRange` | [RecurrenceRange](#RecurrenceRange) | - | Required |

##### Объект `TimeWindow`

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| Время начала `startTime` | local\_time | - | Required |
| Время окончания `endTime` | local\_time | - | Required |
| Часовой пояс `timeZone` | time\_zone | - | Required |

##### Объект `RecurrenceRange`

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| Дата начала `scheduleStartDate` | local\_date | - | Required |
| Дата окончания `scheduleEndDate` | local\_date | - | Required |