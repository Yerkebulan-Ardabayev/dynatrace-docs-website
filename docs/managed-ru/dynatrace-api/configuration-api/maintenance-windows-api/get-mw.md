---
title: Maintenance windows API - GET a maintenance window
source: https://docs.dynatrace.com/managed/dynatrace-api/configuration-api/maintenance-windows-api/get-mw
scraped: 2026-05-12T12:06:27.832585
---

# Maintenance windows API - GET a maintenance window

# Maintenance windows API - GET a maintenance window

* Reference
* Updated on Apr 28, 2020

Этот API устарел. Используйте [Settings API](/managed/dynatrace-api/environment-api/settings "Узнайте, что предлагает Dynatrace Settings API.") со schema **Maintenance windows** (`builtin:alerting.maintenance-window`).

Возвращает параметры указанного maintenance window.

Запрос возвращает payload `application/json`.

|  |  |  |
| --- | --- | --- |
| GET | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/config/v1/maintenanceWindows/{id}` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/config/v1/maintenanceWindows/{id}` |

## Аутентификация

Для выполнения этого запроса нужен access token со scope `ReadConfig`.

Как его получить и использовать, смотрите [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Параметры

| Параметр | Тип | Описание | Где | Обязательный |
| --- | --- | --- | --- | --- |
| id | string | ID запрашиваемого maintenance window. | path | Required |

## Ответ

### Коды ответа

| Код | Тип | Описание |
| --- | --- | --- |
| **200** | [MaintenanceWindow](#openapi-definition-MaintenanceWindow) | Успех |

### Объекты тела ответа

#### Объект `MaintenanceWindow`

Конфигурация maintenance window.

| Элемент | Тип | Описание |
| --- | --- | --- |
| description | string | Краткое описание цели обслуживания. |
| id | string | ID maintenance window. |
| metadata | [ConfigurationMetadata](#openapi-definition-ConfigurationMetadata) | Метаданные, полезные для отладки. |
| name | string | Имя maintenance window, отображаемое в UI. |
| schedule | [Schedule](#openapi-definition-Schedule) | Расписание maintenance window. |
| scope | [Scope](#openapi-definition-Scope) | Область действия maintenance window.  Область ограничивает подавление обнаружения проблем и алертов определёнными сущностями Dynatrace. Может содержать список сущностей и/или правила сопоставления для динамического формирования области.  Если область не задана, подавление обнаружения проблем и алертов применяется ко всему окружению. |
| suppressSyntheticMonitorsExecution | boolean | Подавлять выполнение синтетических мониторов во время обслуживания. |
| suppression | string | Тип подавления алертов и обнаружения проблем во время обслуживания. Элемент может принимать значения * `DETECT_PROBLEMS_AND_ALERT` * `DETECT_PROBLEMS_DONT_ALERT` * `DONT_DETECT_PROBLEMS` |
| type | string | Тип обслуживания: запланированное или внеплановое. Элемент может принимать значения * `PLANNED` * `UNPLANNED` |

#### Объект `ConfigurationMetadata`

Метаданные, полезные для отладки.

| Элемент | Тип | Описание |
| --- | --- | --- |
| clusterVersion | string | Версия Dynatrace. |
| configurationVersions | integer[] | Отсортированный список номеров версий конфигурации. |
| currentConfigurationVersions | string[] | Отсортированный список номеров версий конфигурации. |

#### Объект `Schedule`

Расписание maintenance window.

| Элемент | Тип | Описание |
| --- | --- | --- |
| end | string | Дата и время окончания периода действия maintenance window в формате yyyy-mm-dd HH:mm. |
| recurrence | [Recurrence](#openapi-definition-Recurrence) | Периодичность maintenance window. |
| recurrenceType | string | Тип периодичности расписания. Элемент может принимать значения * `DAILY` * `MONTHLY` * `ONCE` * `WEEKLY` |
| start | string | Дата и время начала периода действия maintenance window в формате yyyy-mm-dd HH:mm. |
| zoneId | string | Часовой пояс времени начала и окончания. Часовой пояс по умолчанию: UTC.  Можно использовать формат UTC-смещения `UTC+01:00` или формат базы данных IANA Time Zone (например, `Europe/Vienna`). |

#### Объект `Recurrence`

Периодичность maintenance window.

| Элемент | Тип | Описание |
| --- | --- | --- |
| dayOfMonth | integer | День месяца для ежемесячного обслуживания.  Значение `31` интерпретируется как последний день месяца для месяцев, в которых нет 31-го числа. Значение `30` также интерпретируется как последний день месяца для февраля. |
| dayOfWeek | string | День недели для еженедельного обслуживания.  Формат: полное название дня в верхнем регистре, например `THURSDAY`. Элемент может принимать значения * `FRIDAY` * `MONDAY` * `SATURDAY` * `SUNDAY` * `THURSDAY` * `TUESDAY` * `WEDNESDAY` |
| durationMinutes | integer | Длительность maintenance window в минутах. |
| startTime | string | Время начала maintenance window в формате HH:mm. |

#### Объект `Scope`

Область действия maintenance window.

Область ограничивает подавление обнаружения проблем и алертов определёнными сущностями Dynatrace. Может содержать список сущностей и/или правила сопоставления для динамического формирования области.

Если область не задана, подавление обнаружения проблем и алертов применяется ко всему окружению.

| Элемент | Тип | Описание |
| --- | --- | --- |
| entities | string[] | Список сущностей Dynatrace (например, хостов или сервисов), включаемых в область.  Допустимые значения: ID сущностей Dynatrace. |
| matches | [MonitoredEntityFilter[]](#openapi-definition-MonitoredEntityFilter) | Список правил сопоставления для динамического формирования области.  Если задано несколько правил, применяется логика OR. |

#### Объект `MonitoredEntityFilter`

Правило сопоставления для сущностей Dynatrace.

| Элемент | Тип | Описание |
| --- | --- | --- |
| mzId | string | ID management zone, к которой должны принадлежать сопоставленные сущности. |
| tagCombination | string | Логика, применяемая при наличии нескольких тегов: AND/OR.  Если не задано, используется логика OR. Элемент может принимать значения * `AND` * `OR` |
| tags | [TagInfo[]](#openapi-definition-TagInfo) | Тег, используемый для сопоставления.  Можно использовать пользовательские теги из UI, теги AWS, Cloud Foundry, OpenShift/Kubernetes и теги на основе переменных окружения. |
| type | string | Тип сущностей Dynatrace (например, хостов или сервисов), которые нужно подбирать через сопоставление. Элемент может принимать значения * `APM_SECURITY_GATEWAY` * `APPLICATION` * `APPLICATION_METHOD` * `APPLICATION_METHOD_GROUP` * `APPMON_SERVER` * `APPMON_SYSTEM_PROFILE` * `AUTO_SCALING_GROUP` * `AUXILIARY_SYNTHETIC_TEST` * `AWS_APPLICATION_LOAD_BALANCER` * `AWS_AVAILABILITY_ZONE` * `AWS_CREDENTIALS` * `AWS_LAMBDA_FUNCTION` * `AWS_NETWORK_LOAD_BALANCER` * `AZURE_API_MANAGEMENT_SERVICE` * `AZURE_APPLICATION_GATEWAY` * `AZURE_APP_SERVICE_PLAN` * `AZURE_COSMOS_DB` * `AZURE_CREDENTIALS` * `AZURE_EVENT_HUB` * `AZURE_EVENT_HUB_NAMESPACE` * `AZURE_FUNCTION_APP` * `AZURE_IOT_HUB` * `AZURE_LOAD_BALANCER` * `AZURE_MGMT_GROUP` * `AZURE_REDIS_CACHE` * `AZURE_REGION` * `AZURE_SERVICE_BUS_NAMESPACE` * `AZURE_SERVICE_BUS_QUEUE` * `AZURE_SERVICE_BUS_TOPIC` * `AZURE_SQL_DATABASE` * `AZURE_SQL_ELASTIC_POOL` * `AZURE_SQL_SERVER` * `AZURE_STORAGE_ACCOUNT` * `AZURE_SUBSCRIPTION` * `AZURE_TENANT` * `AZURE_VM` * `AZURE_VM_SCALE_SET` * `AZURE_WEB_APP` * `BROWSER` * `CF_APPLICATION` * `CF_FOUNDATION` * `CINDER_VOLUME` * `CLOUD_APPLICATION` * `CLOUD_APPLICATION_INSTANCE` * `CLOUD_APPLICATION_NAMESPACE` * `CLOUD_NETWORK_INGRESS` * `CLOUD_NETWORK_POLICY` * `CONTAINER_GROUP` * `CONTAINER_GROUP_INSTANCE` * `CUSTOM_APPLICATION` * `CUSTOM_DEVICE` * `CUSTOM_DEVICE_GROUP` * `DCRUM_APPLICATION` * `DCRUM_SERVICE` * `DCRUM_SERVICE_INSTANCE` * `DEVICE_APPLICATION_METHOD` * `DEVICE_APPLICATION_METHOD_GROUP` * `DISK` * `DOCKER_CONTAINER_GROUP` * `DOCKER_CONTAINER_GROUP_INSTANCE` * `DYNAMO_DB_TABLE` * `EBS_VOLUME` * `EC2_INSTANCE` * `ELASTIC_LOAD_BALANCER` * `ENVIRONMENT` * `EXTERNAL_SYNTHETIC_TEST_STEP` * `GCP_ZONE` * `GEOLOCATION` * `GEOLOC_SITE` * `GOOGLE_COMPUTE_ENGINE` * `HOST` * `HOST_GROUP` * `HTTP_CHECK` * `HTTP_CHECK_STEP` * `HYPERVISOR` * `HYPERVISOR_CLUSTER` * `HYPERVISOR_DISK` * `KUBERNETES_CLUSTER` * `KUBERNETES_NODE` * `KUBERNETES_SERVICE` * `MOBILE_APPLICATION` * `MULTIPROTOCOL_MONITOR` * `NETWORK_INTERFACE` * `NEUTRON_SUBNET` * `OPENSTACK_PROJECT` * `OPENSTACK_REGION` * `OPENSTACK_VM` * `OS` * `PROCESS_GROUP` * `PROCESS_GROUP_INSTANCE` * `QUEUE` * `QUEUE_INSTANCE` * `RELATIONAL_DATABASE_SERVICE` * `S3BUCKET` * `SERVICE` * `SERVICE_INSTANCE` * `SERVICE_METHOD` * `SERVICE_METHOD_GROUP` * `SWIFT_CONTAINER` * `SYNTHETIC_LOCATION` * `SYNTHETIC_TEST` * `SYNTHETIC_TEST_STEP` * `VCENTER` * `VIRTUALMACHINE` * `VMWARE_DATACENTER` |

#### Объект `TagInfo`

Тег сущности Dynatrace.

| Элемент | Тип | Описание |
| --- | --- | --- |
| context | string | Источник тега, например AWS или Cloud Foundry.  Пользовательские теги используют значение `CONTEXTLESS`. Элемент может принимать значения * `AWS` * `AWS_GENERIC` * `AZURE` * `CLOUD_FOUNDRY` * `CONTEXTLESS` * `ENVIRONMENT` * `GOOGLE_CLOUD` * `KUBERNETES` |
| key | string | Ключ тега.  У пользовательских тегов здесь находится значение тега. |
| value | string | Значение тега.  Не применимо к пользовательским тегам. |

### JSON-модели тела ответа

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

## Пример

В этом примере запрос запрашивает свойства maintenance window **infrastructure maintenance** с ID **0b989446-e56f-4837-a521-96f4d39a9b76**.

У конфигурации следующие настройки:

![GET example](https://dt-cdn.net/images/get-example-980-48060ed670.png)

GET example

API-токен передаётся в заголовке **Authorization**.

#### Curl

```
curl -X GET \



"https://mySampleEnv.live.dynatrace.com/api/config/v1/maintenanceWindows/0b989446-e56f-4837-a521-96f4d39a9b76" \



-H 'Authorization: Api-Token dt0c01.abc123.abcdefjhij1234567890'
```

#### URL запроса

```
https://mySampleEnv.live.dynatrace.com/api/config/v1/maintenanceWindows/0b989446-e56f-4837-a521-96f4d39a9b76
```

#### Тело ответа

```
{



"metadata": {



"configurationVersions": [



0



],



"clusterVersion": "1.175.0.20190731-075319"



},



"id": "0b989446-e56f-4837-a521-96f4d39a9b76",



"name": "infrastructure maintenance",



"description": "Monthly check-up of infrastructure",



"type": "PLANNED",



"suppression": "DETECT_PROBLEMS_DONT_ALERT",



"scope": {



"entities": [],



"matches": [



{



"type": "HOST",



"managementZoneId": null,



"tags": [



{



"context": "CONTEXTLESS",



"key": "InfWindows"



},



{



"context": "CONTEXTLESS",



"key": "InfLinux"



}



],



"tagCombination": "OR"



}



]



},



"schedule": {



"recurrenceType": "MONTHLY",



"recurrence": {



"dayOfWeek": null,



"dayOfMonth": 31,



"startTime": "19:00",



"durationMinutes": 60



},



"start": "2019-07-01 00:00",



"end": "2020-07-31 23:59",



"zoneId": "Europe/Vienna"



}



}
```

#### Код ответа

200

## Связанные темы

* [Maintenance windows](/managed/analyze-explore-automate/notifications-and-alerting/maintenance-windows "Узнайте, когда использовать maintenance window. О поддерживаемых типах maintenance window.")