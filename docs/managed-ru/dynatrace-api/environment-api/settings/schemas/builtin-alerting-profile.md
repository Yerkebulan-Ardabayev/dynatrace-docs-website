---
title: Settings API - Problem alerting profiles schema table
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/settings/schemas/builtin-alerting-profile
scraped: 2026-05-12T11:41:10.433090
---

# Settings API - Problem alerting profiles schema table

# Settings API - Problem alerting profiles schema table

* Опубликовано 05 декабря 2023 г.

### Профили оповещений о problem (`builtin:alerting.profile)`

Профили оповещений позволяют настраивать тонкие правила фильтрации алертов на основе severity, влияния на клиента, ассоциированных тегов и/или длительности обнаруженных problems. Они дают точный контроль над тем, какие условия приводят к problem notifications, а какие нет. Профили оповещений также можно использовать для настройки фильтрованных интеграций problem-notification со сторонними мессенджерами: Slack, Splunk On-Call, PagerDuty.

| Schema ID | Группы схемы | Scope |
| --- | --- | --- |
| `builtin:alerting.profile` | * `group:alerting` | `environment` |

Получить schema через Settings API

|  |  |  |
| --- | --- | --- |
| GET | Managed | `https://{your-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:alerting.profile` |
| GET | SaaS | `https://{your-environment-id}.live.dynatrace.com/api/v2/settings/schemas/builtin:alerting.profile` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:alerting.profile` |

## Аутентификация

Для выполнения запроса необходим access token со scope **Read settings** (`settings.read`). О том, как получить и использовать токен, см. [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Параметры

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| Имя `name` | text | - | Required |
| Management zone `managementZone` | setting | Под фильтр попадут сущности, входящие в настроенные management zones. Вместо этого рекомендуется использовать ручные теги.  **Note:** management zones могут запаздывать или быть несогласованными из-за сложности правил и изменчивости атрибутов. Сущности могут попасть в management zone не сразу, это влияет на эффективность фильтра.  Лучше использовать ручные теги.  Подробнее см. [best practices for management zones documentation page](https://dt-url.net/8203d4x). | Optional |
| Правила severity `severityRules` | Set<[AlertingProfileSeverityRule](#AlertingProfileSeverityRule)> | Задайте правила severity для профиля. Максимум 100 severity-правил. | Required |
| Фильтры событий `eventFilters` | Set<[AlertingProfileEventFilter](#AlertingProfileEventFilter)> | Задайте фильтры событий для профиля. Максимум 100 event-фильтров. | Required |

##### Объект `AlertingProfileSeverityRule`

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| Уровень severity для problem `severityLevel` | enum | Возможные значения: * `AVAILABILITY` * `CUSTOM_ALERT` * `ERRORS` * `MONITORING_UNAVAILABLE` * `PERFORMANCE` * `RESOURCE_CONTENTION` | Required |
| Задержка отправки problem в минутах `delayInMinutes` | integer | Отправить уведомление, если problem остаётся открытой дольше X минут. | Required |
| Фильтровать problems по тегу `tagFilterIncludeMode` | enum | Возможные значения: * `NONE` * `INCLUDE_ANY` * `INCLUDE_ALL` | Required |
| Теги `tagFilter` | set | Под фильтр попадут сущности, содержащие любые/все настроенные теги. Рекомендуется использовать ручные теги.  **Note:** автоматически применяемые теги могут запаздывать или быть несогласованными из-за сложности правил и изменчивости атрибутов. Сущности могут получить тег не сразу, это влияет на эффективность фильтра.  Лучше использовать ручные теги.  Подробнее см. [best practices for tagging documentation page](https://dt-url.net/8203d4x). | Required |

##### Объект `AlertingProfileEventFilter`

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| Фильтровать problems по любому событию источника `type` | enum | Возможные значения: * `PREDEFINED` * `CUSTOM` | Required |
| `predefinedFilter` | [PredefinedEventFilter](#PredefinedEventFilter) | - | Required |
| `customFilter` | [CustomEventFilter](#CustomEventFilter) | - | Required |

##### Объект `PredefinedEventFilter`

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| Фильтровать problems по типу события Dynatrace `eventType` | enum | Возможные значения: * `EC2_HIGH_CPU` * `OSI_HIGH_CPU` * `ELB_HIGH_BACKEND_ERROR_RATE` * `PROCESS_NA_HIGH_CONN_FAIL_RATE` * `CUSTOM_APP_CRASH_RATE_INCREASED` * `CUSTOM_APPLICATION_ERROR_RATE_INCREASED` * `CUSTOM_APPLICATION_SLOWDOWN` * `CUSTOM_APPLICATION_UNEXPECTED_LOW_LOAD` * `CUSTOM_APPLICATION_UNEXPECTED_HIGH_LOAD` * `ESXI_GUEST_CPU_LIMIT_REACHED` * `ESXI_GUEST_ACTIVE_SWAP_WAIT` * `ESXI_HOST_CPU_SATURATION` * `ESXI_HOST_MEMORY_SATURATION` * `ESXI_VM_IMPACT_HOST_CPU_SATURATION` * `ESXI_VM_IMPACT_HOST_MEMORY_SATURATION` * `ESXI_HOST_NETWORK_PROBLEMS` * `ESXI_HOST_DISK_SLOW` * `EBS_VOLUME_HIGH_LATENCY` * `DATABASE_CONNECTION_FAILURE` * `SERVICE_ERROR_RATE_INCREASED` * `RDS_HIGH_LATENCY` * `OSI_NIC_UTILIZATION_HIGH` * `OSI_NIC_ERRORS_HIGH` * `OSI_NIC_DROPPED_PACKETS_HIGH` * `OSI_GRACEFULLY_SHUTDOWN` * `OSI_UNEXPECTEDLY_UNAVAILABLE` * `HOST_OF_SERVICE_UNAVAILABLE` * `ESXI_HOST_DISK_QUEUE_SLOW` * `APPLICATION_ERROR_RATE_INCREASED` * `AWS_LAMBDA_HIGH_ERROR_RATE` * `PROCESS_HIGH_GC_ACTIVITY` * `ESXI_HOST_DATASTORE_LOW_DISK_SPACE` * `OSI_LOW_DISK_SPACE` * `OSI_DISK_LOW_INODES` * `RDS_LOW_STORAGE_SPACE` * `PROCESS_MEMORY_RESOURCE_EXHAUSTED` * `OSI_HIGH_MEMORY` * `MOBILE_APP_CRASH_RATE_INCREASED` * `MOBILE_APPLICATION_ERROR_RATE_INCREASED` * `MOBILE_APPLICATION_SLOWDOWN` * `MOBILE_APPLICATION_UNEXPECTED_LOW_LOAD` * `MOBILE_APPLICATION_UNEXPECTED_HIGH_LOAD` * `MONITORING_UNAVAILABLE` * `PROCESS_NA_HIGH_LOSS_RATE` * `ESXI_HOST_OVERLOADED_STORAGE` * `PROCESS_CRASHED` * `PG_LOW_INSTANCE_COUNT` * `PGI_UNAVAILABLE` * `RDS_HIGH_CPU` * `RDS_LOW_MEMORY` * `RDS_OF_SERVICE_UNAVAILABLE` * `SERVICE_SLOWDOWN` * `RDS_RESTART_SEQUENCE` * `PGI_OF_SERVICE_UNAVAILABLE` * `OSI_SLOW_DISK` * `SYNTHETIC_NODE_OUTAGE` * `SYNTHETIC_PRIVATE_LOCATION_OUTAGE` * `PROCESS_THREADS_RESOURCE_EXHAUSTED` * `SERVICE_UNEXPECTED_HIGH_LOAD` * `APPLICATION_UNEXPECTED_HIGH_LOAD` * `SERVICE_UNEXPECTED_LOW_LOAD` * `APPLICATION_UNEXPECTED_LOW_LOAD` * `APPLICATION_SLOWDOWN` * `SYNTHETIC_GLOBAL_OUTAGE` * `SYNTHETIC_LOCAL_OUTAGE` * `SYNTHETIC_TEST_LOCATION_SLOWDOWN` * `HTTP_CHECK_GLOBAL_OUTAGE` * `HTTP_CHECK_LOCAL_OUTAGE` * `HTTP_CHECK_TEST_LOCATION_SLOWDOWN` * `MULTI_PROTOCOL_GLOBAL_OUTAGE` * `MULTI_PROTOCOL_LOCAL_OUTAGE` * `MULTI_PROTOCOL_LOCATION_SLOWDOWN` * `EXTERNAL_SYNTHETIC_TEST_OUTAGE` * `EXTERNAL_SYNTHETIC_TEST_SLOWDOWN` | Required |
| Инвертировать `negate` | boolean | - | Required |

##### Объект `CustomEventFilter`

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| Фильтр по заголовку `titleFilter` | [TextFilter](#TextFilter) | - | Optional |
| Фильтр по описанию `descriptionFilter` | [TextFilter](#TextFilter) | - | Optional |
| Фильтры по свойствам `metadataFilter` | [MetadataFilter](#MetadataFilter) | - | Optional |

##### Объект `TextFilter`

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| Оператор сравнения `operator` | enum | Возможные значения: * `BEGINS_WITH` * `ENDS_WITH` * `CONTAINS` * `REGEX_MATCHES` * `STRING_EQUALS` | Required |
| Значение `value` | text | - | Required |
| Инвертировать `negate` | boolean | - | Required |
| Включено `enabled` | boolean | - | Required |
| С учётом регистра `caseSensitive` | boolean | - | Required |

##### Объект `MetadataFilter`

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| `metadataFilterItems` | Set<[MetadataFilterItem](#MetadataFilterItem)> | Задайте фильтры для свойств события. Максимум 20 свойств. | Required |

##### Объект `MetadataFilterItem`

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| Ключ `metadataKey` | text | Введите 'dt.' для подсказок по ключам. | Required |
| Значение `metadataValue` | text | - | Required |
| Инвертировать `negate` | boolean | - | Required |