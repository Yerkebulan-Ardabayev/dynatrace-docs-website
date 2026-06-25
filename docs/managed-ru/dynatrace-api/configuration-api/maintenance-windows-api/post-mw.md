---
title: Maintenance windows API - POST a maintenance window
source: https://docs.dynatrace.com/managed/dynatrace-api/configuration-api/maintenance-windows-api/post-mw
scraped: 2026-05-12T12:06:21.472310
---

# Maintenance windows API - POST a maintenance window

# Maintenance windows API - POST a maintenance window

* Reference
* Updated on Apr 28, 2020

Этот API устарел. Используйте [Settings API](/managed/dynatrace-api/environment-api/settings "Узнайте, что предлагает Dynatrace Settings API.") со schema **Maintenance windows** (`builtin:alerting.maintenance-window`).

Создаёт новое maintenance window.

Запрос принимает и возвращает payload `application/json`.

|  |  |  |
| --- | --- | --- |
| POST | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/config/v1/maintenanceWindows` |
| POST | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/config/v1/maintenanceWindows` |

## Аутентификация

Для выполнения этого запроса нужен access token со scope `WriteConfig`.

Как его получить и использовать, смотрите [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Параметры

В теле не должен указываться ID. ID присваивается Dynatrace автоматически.

| Параметр | Тип | Описание | Где | Обязательный |
| --- | --- | --- | --- | --- |
| body | [MaintenanceWindow](#openapi-definition-MaintenanceWindow) | JSON-тело запроса. Содержит параметры нового maintenance window. | body | Optional |

### Объекты тела запроса

#### Объект `MaintenanceWindow`

Конфигурация maintenance window.

| Элемент | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| description | string | Краткое описание цели обслуживания. | Required |
| id | string | ID maintenance window. | Optional |
| metadata | [ConfigurationMetadata](#openapi-definition-ConfigurationMetadata) | Метаданные, полезные для отладки. | Optional |
| name | string | Имя maintenance window, отображаемое в UI. | Required |
| schedule | [Schedule](#openapi-definition-Schedule) | Расписание maintenance window. | Required |
| scope | [Scope](#openapi-definition-Scope) | Область действия maintenance window.  Область ограничивает подавление обнаружения проблем и алертов определёнными сущностями Dynatrace. Может содержать список сущностей и/или правила сопоставления для динамического формирования области.  Если область не задана, подавление обнаружения проблем и алертов применяется ко всему окружению. | Optional |
| suppressSyntheticMonitorsExecution | boolean | Подавлять выполнение синтетических мониторов во время обслуживания. | Optional |
| suppression | string | Тип подавления алертов и обнаружения проблем во время обслуживания. Элемент может принимать значения * `DETECT_PROBLEMS_AND_ALERT` * `DETECT_PROBLEMS_DONT_ALERT` * `DONT_DETECT_PROBLEMS` | Required |
| type | string | Тип обслуживания: запланированное или внеплановое. Элемент может принимать значения * `PLANNED` * `UNPLANNED` | Required |

#### Объект `ConfigurationMetadata`

Метаданные, полезные для отладки.

| Элемент | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| clusterVersion | string | Версия Dynatrace. | Optional |
| configurationVersions | integer[] | Отсортированный список номеров версий конфигурации. | Optional |
| currentConfigurationVersions | string[] | Отсортированный список номеров версий конфигурации. | Optional |

#### Объект `Schedule`

Расписание maintenance window.

| Элемент | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| end | string | Дата и время окончания периода действия maintenance window в формате yyyy-mm-dd HH:mm. | Required |
| recurrence | [Recurrence](#openapi-definition-Recurrence) | Периодичность maintenance window. | Optional |
| recurrenceType | string | Тип периодичности расписания. Элемент может принимать значения * `DAILY` * `MONTHLY` * `ONCE` * `WEEKLY` | Required |
| start | string | Дата и время начала периода действия maintenance window в формате yyyy-mm-dd HH:mm. | Required |
| zoneId | string | Часовой пояс времени начала и окончания. Часовой пояс по умолчанию: UTC.  Можно использовать формат UTC-смещения `UTC+01:00` или формат базы данных IANA Time Zone (например, `Europe/Vienna`). | Required |

#### Объект `Recurrence`

Периодичность maintenance window.

| Элемент | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| dayOfMonth | integer | День месяца для ежемесячного обслуживания.  Значение `31` интерпретируется как последний день месяца для месяцев, в которых нет 31-го числа. Значение `30` также интерпретируется как последний день месяца для февраля. | Optional |
| dayOfWeek | string | День недели для еженедельного обслуживания.  Формат: полное название дня в верхнем регистре, например `THURSDAY`. Элемент может принимать значения * `FRIDAY` * `MONDAY` * `SATURDAY` * `SUNDAY` * `THURSDAY` * `TUESDAY` * `WEDNESDAY` | Optional |
| durationMinutes | integer | Длительность maintenance window в минутах. | Required |
| startTime | string | Время начала maintenance window в формате HH:mm. | Required |

#### Объект `Scope`

Область действия maintenance window.

Область ограничивает подавление обнаружения проблем и алертов определёнными сущностями Dynatrace. Может содержать список сущностей и/или правила сопоставления для динамического формирования области.

Если область не задана, подавление обнаружения проблем и алертов применяется ко всему окружению.

| Элемент | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| entities | string[] | Список сущностей Dynatrace (например, хостов или сервисов), включаемых в область.  Допустимые значения: ID сущностей Dynatrace. | Required |
| matches | [MonitoredEntityFilter[]](#openapi-definition-MonitoredEntityFilter) | Список правил сопоставления для динамического формирования области.  Если задано несколько правил, применяется логика OR. | Required |

#### Объект `MonitoredEntityFilter`

Правило сопоставления для сущностей Dynatrace.

| Элемент | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| mzId | string | ID management zone, к которой должны принадлежать сопоставленные сущности. | Optional |
| tagCombination | string | Логика, применяемая при наличии нескольких тегов: AND/OR.  Если не задано, используется логика OR. Элемент может принимать значения * `AND` * `OR` | Optional |
| tags | [TagInfo[]](#openapi-definition-TagInfo) | Тег, используемый для сопоставления.  Можно использовать пользовательские теги из UI, теги AWS, Cloud Foundry, OpenShift/Kubernetes и теги на основе переменных окружения. | Required |
| type | string | Тип сущностей Dynatrace (например, хостов или сервисов), которые нужно подбирать через сопоставление. Элемент может принимать значения * `APM_SECURITY_GATEWAY` * `APPLICATION` * `APPLICATION_METHOD` * `APPLICATION_METHOD_GROUP` * `APPMON_SERVER` * `APPMON_SYSTEM_PROFILE` * `AUTO_SCALING_GROUP` * `AUXILIARY_SYNTHETIC_TEST` * `AWS_APPLICATION_LOAD_BALANCER` * `AWS_AVAILABILITY_ZONE` * `AWS_CREDENTIALS` * `AWS_LAMBDA_FUNCTION` * `AWS_NETWORK_LOAD_BALANCER` * `AZURE_API_MANAGEMENT_SERVICE` * `AZURE_APPLICATION_GATEWAY` * `AZURE_APP_SERVICE_PLAN` * `AZURE_COSMOS_DB` * `AZURE_CREDENTIALS` * `AZURE_EVENT_HUB` * `AZURE_EVENT_HUB_NAMESPACE` * `AZURE_FUNCTION_APP` * `AZURE_IOT_HUB` * `AZURE_LOAD_BALANCER` * `AZURE_MGMT_GROUP` * `AZURE_REDIS_CACHE` * `AZURE_REGION` * `AZURE_SERVICE_BUS_NAMESPACE` * `AZURE_SERVICE_BUS_QUEUE` * `AZURE_SERVICE_BUS_TOPIC` * `AZURE_SQL_DATABASE` * `AZURE_SQL_ELASTIC_POOL` * `AZURE_SQL_SERVER` * `AZURE_STORAGE_ACCOUNT` * `AZURE_SUBSCRIPTION` * `AZURE_TENANT` * `AZURE_VM` * `AZURE_VM_SCALE_SET` * `AZURE_WEB_APP` * `BROWSER` * `CF_APPLICATION` * `CF_FOUNDATION` * `CINDER_VOLUME` * `CLOUD_APPLICATION` * `CLOUD_APPLICATION_INSTANCE` * `CLOUD_APPLICATION_NAMESPACE` * `CLOUD_NETWORK_INGRESS` * `CLOUD_NETWORK_POLICY` * `CONTAINER_GROUP` * `CONTAINER_GROUP_INSTANCE` * `CUSTOM_APPLICATION` * `CUSTOM_DEVICE` * `CUSTOM_DEVICE_GROUP` * `DCRUM_APPLICATION` * `DCRUM_SERVICE` * `DCRUM_SERVICE_INSTANCE` * `DEVICE_APPLICATION_METHOD` * `DEVICE_APPLICATION_METHOD_GROUP` * `DISK` * `DOCKER_CONTAINER_GROUP` * `DOCKER_CONTAINER_GROUP_INSTANCE` * `DYNAMO_DB_TABLE` * `EBS_VOLUME` * `EC2_INSTANCE` * `ELASTIC_LOAD_BALANCER` * `ENVIRONMENT` * `EXTERNAL_SYNTHETIC_TEST_STEP` * `GCP_ZONE` * `GEOLOCATION` * `GEOLOC_SITE` * `GOOGLE_COMPUTE_ENGINE` * `HOST` * `HOST_GROUP` * `HTTP_CHECK` * `HTTP_CHECK_STEP` * `HYPERVISOR` * `HYPERVISOR_CLUSTER` * `HYPERVISOR_DISK` * `KUBERNETES_CLUSTER` * `KUBERNETES_NODE` * `KUBERNETES_SERVICE` * `MOBILE_APPLICATION` * `MULTIPROTOCOL_MONITOR` * `NETWORK_INTERFACE` * `NEUTRON_SUBNET` * `OPENSTACK_PROJECT` * `OPENSTACK_REGION` * `OPENSTACK_VM` * `OS` * `PROCESS_GROUP` * `PROCESS_GROUP_INSTANCE` * `QUEUE` * `QUEUE_INSTANCE` * `RELATIONAL_DATABASE_SERVICE` * `S3BUCKET` * `SERVICE` * `SERVICE_INSTANCE` * `SERVICE_METHOD` * `SERVICE_METHOD_GROUP` * `SWIFT_CONTAINER` * `SYNTHETIC_LOCATION` * `SYNTHETIC_TEST` * `SYNTHETIC_TEST_STEP` * `VCENTER` * `VIRTUALMACHINE` * `VMWARE_DATACENTER` | Optional |

#### Объект `TagInfo`

Тег сущности Dynatrace.

| Элемент | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| context | string | Источник тега, например AWS или Cloud Foundry.  Пользовательские теги используют значение `CONTEXTLESS`. Элемент может принимать значения * `AWS` * `AWS_GENERIC` * `AZURE` * `CLOUD_FOUNDRY` * `CONTEXTLESS` * `ENVIRONMENT` * `GOOGLE_CLOUD` * `KUBERNETES` | Required |
| key | string | Ключ тега.  У пользовательских тегов здесь находится значение тега. | Required |
| value | string | Значение тега.  Не применимо к пользовательским тегам. | Optional |

### JSON-модель тела запроса

Это модель тела запроса, показывающая возможные элементы. Её нужно адаптировать под реальный запрос.

```
{



"description": "An example Maintenance window",



"metadata": {



"clusterVersion": "Mock version",



"configurationVersions": [



4,



2



]



},



"name": "Example Window",



"schedule": {



"end": "2019-02-27 00:00",



"recurrence": {



"dayOfMonth": "23",



"durationMinutes": "60",



"startTime": "16:28"



},



"recurrenceType": "MONTHLY",



"start": "2018-08-02 00:00",



"zoneId": "Europe/Vienna"



},



"scope": {



"entities": [



"HOST-0000000000123456"



],



"matches": [



{



"mzId": "123456789",



"tagCombination": "AND",



"tags": [



{



"context": "AWS",



"key": "testkey",



"value": "testvalue"



}



],



"type": "HOST"



}



]



},



"suppressSyntheticMonitorsExecution": "true",



"suppression": "DETECT_PROBLEMS_AND_ALERT",



"type": "UNPLANNED"



}
```

## Ответ

### Коды ответа

| Код | Тип | Описание |
| --- | --- | --- |
| **201** | [EntityShortRepresentation](#openapi-definition-EntityShortRepresentation) | Успех. Новое maintenance window создано. Тело ответа содержит его ID. |
| **400** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Ошибка. Входные данные некорректны. |

### Объекты тела ответа

#### Объект `EntityShortRepresentation`

Краткое представление сущности Dynatrace.

| Элемент | Тип | Описание |
| --- | --- | --- |
| description | string | Краткое описание сущности Dynatrace. |
| id | string | ID сущности Dynatrace. |
| name | string | Имя сущности Dynatrace. |

#### Объект `ErrorEnvelope`

| Элемент | Тип | Описание |
| --- | --- | --- |
| error | [Error](#openapi-definition-Error) | - |

#### Объект `Error`

| Элемент | Тип | Описание |
| --- | --- | --- |
| code | integer | HTTP-код состояния. |
| constraintViolations | [ConstraintViolation[]](#openapi-definition-ConstraintViolation) | Список нарушений ограничений. |
| message | string | Сообщение об ошибке. |

#### Объект `ConstraintViolation`

Список нарушений ограничений.

| Элемент | Тип | Описание |
| --- | --- | --- |
| location | string | - |
| message | string | - |
| parameterLocation | string | -Элемент может принимать значения * `HEADER` * `PATH` * `PAYLOAD_BODY` * `QUERY` |
| path | string | - |

### JSON-модели тела ответа

```
{



"description": "Dynatrace entity for the REST API example",



"id": "6a98d7bc-abb9-44f8-ae6a-73e68e71812a",



"name": "Dynatrace entity"



}
```

```
{



"error": {



"code": 1,



"constraintViolations": [



{



"location": "string",



"message": "string",



"parameterLocation": "HEADER",



"path": "string"



}



],



"message": "string"



}



}
```

## Валидация payload

Рекомендуется проверять payload перед отправкой реального запроса. Код ответа **204** означает, что payload корректен.

Запрос принимает payload `application/json`.

|  |  |  |
| --- | --- | --- |
| POST | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/config/v1/maintenanceWindows/validator` |
| POST | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/config/v1/maintenanceWindows/validator` |

### Аутентификация

Для выполнения этого запроса нужен access token со scope `WriteConfig`.

Как его получить и использовать, смотрите [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

### Ответ

#### Коды ответа

| Код | Тип | Описание |
| --- | --- | --- |
| **204** | - | Валидация пройдена. Отправленная конфигурация корректна. Ответ без тела. |
| **400** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Ошибка. Входные данные некорректны. |

#### Объекты тела ответа

#### Объект `ErrorEnvelope`

| Элемент | Тип | Описание |
| --- | --- | --- |
| error | [Error](#openapi-definition-Error) | - |

#### Объект `Error`

| Элемент | Тип | Описание |
| --- | --- | --- |
| code | integer | HTTP-код состояния. |
| constraintViolations | [ConstraintViolation[]](#openapi-definition-ConstraintViolation) | Список нарушений ограничений. |
| message | string | Сообщение об ошибке. |

#### Объект `ConstraintViolation`

Список нарушений ограничений.

| Элемент | Тип | Описание |
| --- | --- | --- |
| location | string | - |
| message | string | - |
| parameterLocation | string | -Элемент может принимать значения * `HEADER` * `PATH` * `PAYLOAD_BODY` * `QUERY` |
| path | string | - |

#### JSON-модели тела ответа

```
{



"error": {



"code": 1,



"constraintViolations": [



{



"location": "string",



"message": "string",



"parameterLocation": "HEADER",



"path": "string"



}



],



"message": "string"



}



}
```

## Пример

В этом примере запрос создаёт новое maintenance window для **разового запланированного** обслуживания. Maintenance window начинается в **8:00 утра** и заканчивается в **13:00** 31 июля 2019 года. Оно затрагивает приложение с ID **APPLICATION-61A89B82DF26BCFC** и все хосты, у которых есть пользовательский тег **MainApp**. Обнаружение проблем подавляется во время этого обслуживания.

API-токен передаётся в заголовке **Authorization**.

Тело запроса объёмное, поэтому в секции **Curl** оно усечено. Полное тело смотрите в секции **Request body**. Можно скачать или скопировать пример тела запроса, чтобы попробовать у себя. Используйте ID сущностей и теги, которые есть в вашем окружении. Список отслеживаемых сущностей можно получить через [**Topology and Smartscape API**](/managed/dynatrace-api/environment-api/topology-and-smartscape "Узнайте о Dynatrace Topology and Smartscape API."), а список тегов получают через [**Automatically applied tags API**](/managed/dynatrace-api/configuration-api/automatically-applied-tags-api "Узнайте, что предлагает Dynatrace automatically applied tags API.").

#### Curl

```
curl -X POST \



"https://mySampleEnv.live.dynatrace.com/api/config/v1/maintenanceWindows" \



-H 'Authorization: Api-Token dt0c01.abc123.abcdefjhij1234567890' \



-H 'Content-Type: application/json' \



-d '{ <truncated - see the Request body section > }'
```

#### URL запроса

```
https://mySampleEnv.live.dynatrace.com/api/config/v1/maintenanceWindows
```

#### Тело запроса

```
{



"name": "Main app update",



"description": "Deployment of a new version of the main application",



"type": "PLANNED",



"suppression": "DONT_DETECT_PROBLEMS",



"scope": {



"entities": ["APPLICATION-61A89B82DF26BCFC"],



"matches": [



{



"type": "HOST",



"mzId": null,



"tags": [



{



"context": "CONTEXTLESS",



"key": "MainApp"



}



],



"tagCombination": "OR"



}



]



},



"schedule": {



"recurrenceType": "ONCE",



"start": "2019-07-31 08:00",



"end": "2019-07-31 13:00",



"zoneId": "Europe/Vienna"



}



}
```

#### Тело ответа

```
{



"id": "ac6f245d-e945-4e0c-85b1-8c134d0b05ad",



"name": "Main app update",



"description": "Deployment of a new version of the main app"



}
```

#### Код ответа

201

#### Результат

Новое maintenance window в UI выглядит так:

![POST example](https://dt-cdn.net/images/post-example-971-3dd3f9b318.png)

POST example

## Связанные темы

* [Maintenance windows](/managed/analyze-explore-automate/notifications-and-alerting/maintenance-windows "Узнайте, когда использовать maintenance window. О поддерживаемых типах maintenance window.")