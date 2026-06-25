---
title: Alerting profiles API - GET a profile
source: https://docs.dynatrace.com/managed/dynatrace-api/configuration-api/alerting-profiles-api/get-profile
scraped: 2026-05-12T12:06:34.264066
---

# Alerting profiles API - GET a profile

# Alerting profiles API - GET a profile

* Reference
* Published Aug 16, 2019

Этот API устарел. Используйте [Settings API](/managed/dynatrace-api/environment-api/settings "Узнайте, что предлагает Dynatrace Settings API."). Ищите schema **Problem alerting profiles** (`builtin:alerting.profile`).

Возвращает параметры указанного профиля оповещений.

Запрос возвращает payload `application/json`.

|  |  |  |
| --- | --- | --- |
| GET | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/config/v1/alertingProfiles/{id}` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/config/v1/alertingProfiles/{id}` |

## Аутентификация

Для выполнения этого запроса нужен access token со scope `ReadConfig`.

Как его получить и использовать, смотрите [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Параметры

| Параметр | Тип | Описание | Где | Обязательный |
| --- | --- | --- | --- | --- |
| id | string | ID нужного профиля оповещений. | path | Required |

## Ответ

### Коды ответа

| Код | Тип | Описание |
| --- | --- | --- |
| **200** | [AlertingProfile](#openapi-definition-AlertingProfile) | Успех |

### Объекты тела ответа

#### Объект `AlertingProfile`

Конфигурация профиля оповещений.

| Элемент | Тип | Описание |
| --- | --- | --- |
| displayName | string | Имя профиля оповещений, отображаемое в UI. |
| eventTypeFilters | [AlertingEventTypeFilter[]](#openapi-definition-AlertingEventTypeFilter) | Список фильтров событий.  Для всех фильтров, которые *инвертированы* внутри этих фильтров событий, то есть для всех "Predefined", а также "Custom" (Title и/или Description), применяется логика AND. Для всех *неинвертированных* применяется логика OR. Между этими двумя группами, инвертированными и неинвертированными, применяется логика AND.  Если вы указываете и правило серьёзности, и фильтр событий, применяется логика AND. |
| id | string | ID профиля оповещений. |
| metadata | [ConfigurationMetadata](#openapi-definition-ConfigurationMetadata) | Метаданные для отладки |
| mzId | string | ID зоны управления, к которой применяется профиль оповещений. |
| rules | [AlertingProfileSeverityRule[]](#openapi-definition-AlertingProfileSeverityRule) | Список правил серьёзности.  Правила оцениваются сверху вниз. Применяется первое подходящее правило, дальнейшая оценка прекращается.  Если вы указываете и правило серьёзности, и фильтр событий, применяется логика AND. |

#### Объект `AlertingEventTypeFilter`

Конфигурация фильтра событий для профиля оповещений.

У вас есть два взаимоисключающих варианта:

* Выберите тип события из списка предопределённых событий. Укажите его в поле **predefinedEventFilter**.
* Задайте правило для пользовательских событий. Укажите его в поле **customEventFilter**.

| Элемент | Тип | Описание |
| --- | --- | --- |
| customEventFilter | [AlertingCustomEventFilter](#openapi-definition-AlertingCustomEventFilter) | Конфигурация фильтра пользовательских событий.  Фильтрует пользовательские события по заголовку или описанию. Если указаны оба, применяется логика AND. |
| predefinedEventFilter | [AlertingPredefinedEventFilter](#openapi-definition-AlertingPredefinedEventFilter) | Конфигурация фильтра предопределённых событий. |

#### Объект `AlertingCustomEventFilter`

Конфигурация фильтра пользовательских событий.

Фильтрует пользовательские события по заголовку или описанию. Если указаны оба, применяется логика AND.

| Элемент | Тип | Описание |
| --- | --- | --- |
| customDescriptionFilter | [AlertingCustomTextFilter](#openapi-definition-AlertingCustomTextFilter) | Конфигурация фильтра сопоставления. |
| customTitleFilter | [AlertingCustomTextFilter](#openapi-definition-AlertingCustomTextFilter) | Конфигурация фильтра сопоставления. |

#### Объект `AlertingCustomTextFilter`

Конфигурация фильтра сопоставления.

| Элемент | Тип | Описание |
| --- | --- | --- |
| caseInsensitive | boolean | Условие чувствительно к регистру (`false`) или нечувствительно к регистру (`true`).  Если не задано, используется `false`, что делает условие чувствительным к регистру. |
| enabled | boolean | Фильтр включён (`true`) или отключён (`false`). |
| negate | boolean | Инвертирует **operator** сравнения. Например, превращает **begins with** в **does not begin with**. |
| operator | string | Оператор сравнения.  Вы можете инвертировать его, установив **negate** в `true`. Возможные значения: * `BEGINS_WITH` * `CONTAINS` * `CONTAINS_REGEX` * `ENDS_WITH` * `EQUALS` |
| value | string | Значение для сравнения. |

#### Объект `AlertingPredefinedEventFilter`

Конфигурация фильтра предопределённых событий.

| Элемент | Тип | Описание |
| --- | --- | --- |
| eventType | string | Тип предопределённого события. Возможные значения: * `APPLICATION_ERROR_RATE_INCREASED` * `APPLICATION_SLOWDOWN` * `APPLICATION_UNEXPECTED_HIGH_LOAD` * `APPLICATION_UNEXPECTED_LOW_LOAD` * `AWS_LAMBDA_HIGH_ERROR_RATE` * `CUSTOM_APPLICATION_ERROR_RATE_INCREASED` * `CUSTOM_APPLICATION_SLOWDOWN` * `CUSTOM_APPLICATION_UNEXPECTED_HIGH_LOAD` * `CUSTOM_APPLICATION_UNEXPECTED_LOW_LOAD` * `CUSTOM_APP_CRASH_RATE_INCREASED` * `DATABASE_CONNECTION_FAILURE` * `EBS_VOLUME_HIGH_LATENCY` * `EC2_HIGH_CPU` * `ELB_HIGH_BACKEND_ERROR_RATE` * `ESXI_GUEST_ACTIVE_SWAP_WAIT` * `ESXI_GUEST_CPU_LIMIT_REACHED` * `ESXI_HOST_CPU_SATURATION` * `ESXI_HOST_DATASTORE_LOW_DISK_SPACE` * `ESXI_HOST_DISK_QUEUE_SLOW` * `ESXI_HOST_DISK_SLOW` * `ESXI_HOST_MEMORY_SATURATION` * `ESXI_HOST_NETWORK_PROBLEMS` * `ESXI_HOST_OVERLOADED_STORAGE` * `ESXI_VM_IMPACT_HOST_CPU_SATURATION` * `ESXI_VM_IMPACT_HOST_MEMORY_SATURATION` * `EXTERNAL_SYNTHETIC_TEST_OUTAGE` * `EXTERNAL_SYNTHETIC_TEST_SLOWDOWN` * `HOST_OF_SERVICE_UNAVAILABLE` * `HTTP_CHECK_GLOBAL_OUTAGE` * `HTTP_CHECK_LOCAL_OUTAGE` * `HTTP_CHECK_TEST_LOCATION_SLOWDOWN` * `MOBILE_APPLICATION_ERROR_RATE_INCREASED` * `MOBILE_APPLICATION_SLOWDOWN` * `MOBILE_APPLICATION_UNEXPECTED_HIGH_LOAD` * `MOBILE_APPLICATION_UNEXPECTED_LOW_LOAD` * `MOBILE_APP_CRASH_RATE_INCREASED` * `MONITORING_UNAVAILABLE` * `MULTI_PROTOCOL_GLOBAL_OUTAGE` * `MULTI_PROTOCOL_LOCAL_OUTAGE` * `MULTI_PROTOCOL_LOCATION_SLOWDOWN` * `OSI_DISK_LOW_INODES` * `OSI_GRACEFULLY_SHUTDOWN` * `OSI_HIGH_CPU` * `OSI_HIGH_MEMORY` * `OSI_LOW_DISK_SPACE` * `OSI_NIC_DROPPED_PACKETS_HIGH` * `OSI_NIC_ERRORS_HIGH` * `OSI_NIC_UTILIZATION_HIGH` * `OSI_SLOW_DISK` * `OSI_UNEXPECTEDLY_UNAVAILABLE` * `PGI_OF_SERVICE_UNAVAILABLE` * `PGI_UNAVAILABLE` * `PG_LOW_INSTANCE_COUNT` * `PROCESS_CRASHED` * `PROCESS_HIGH_GC_ACTIVITY` * `PROCESS_MEMORY_RESOURCE_EXHAUSTED` * `PROCESS_NA_HIGH_CONN_FAIL_RATE` * `PROCESS_NA_HIGH_LOSS_RATE` * `PROCESS_THREADS_RESOURCE_EXHAUSTED` * `RDS_HIGH_CPU` * `RDS_HIGH_LATENCY` * `RDS_LOW_MEMORY` * `RDS_LOW_STORAGE_SPACE` * `RDS_OF_SERVICE_UNAVAILABLE` * `RDS_RESTART_SEQUENCE` * `SERVICE_ERROR_RATE_INCREASED` * `SERVICE_SLOWDOWN` * `SERVICE_UNEXPECTED_HIGH_LOAD` * `SERVICE_UNEXPECTED_LOW_LOAD` * `SYNTHETIC_GLOBAL_OUTAGE` * `SYNTHETIC_LOCAL_OUTAGE` * `SYNTHETIC_NODE_OUTAGE` * `SYNTHETIC_PRIVATE_LOCATION_OUTAGE` * `SYNTHETIC_TEST_LOCATION_SLOWDOWN` |
| negate | boolean | Оповещение срабатывает, когда проблема указанной серьёзности возникает, пока указанное событие **происходит** (`false`), или пока указанное событие **не происходит** (`true`).  Например, если вы выбрали серьёзность Slowdown (`PERFORMANCE`) и событие Unexpected high traffic (`APPLICATION_UNEXPECTED_HIGH_LOAD`) с **negate**, установленным в `true`, профиль оповещений сработает только тогда, когда возникнет проблема замедления, а события неожиданно высокого трафика нет.  Рассмотрите следующий сценарий в качестве примера. Задано правило серьёзности Slowdown (`PERFORMANCE`). В зависимости от конфигурации фильтра событий (в качестве примера используется событие Unexpected high traffic (`APPLICATION_UNEXPECTED_HIGH_LOAD`)), поведение профиля оповещений одно из следующих:\* **negate** установлен в `false`: оповещение срабатывает, когда возникает проблема замедления, пока происходит событие неожиданно высокого трафика.  * **negate** установлен в `true`: оповещение срабатывает, когда возникает проблема замедления, пока нет события неожиданно высокого трафика. * правило событий не задано: оповещение срабатывает, когда возникает проблема замедления, независимо от каких-либо событий. |

#### Объект `ConfigurationMetadata`

Метаданные для отладки

| Элемент | Тип | Описание |
| --- | --- | --- |
| clusterVersion | string | Версия Dynatrace. |
| configurationVersions | integer[] | Отсортированный список номеров версий конфигурации. |
| currentConfigurationVersions | string[] | Отсортированный список номеров версий конфигурации. |

#### Объект `AlertingProfileSeverityRule`

Правило серьёзности профиля оповещений.

Правило серьёзности определяет уровень серьёзности, который должен быть достигнут, прежде чем будет отправлено оповещение об обнаруженной проблеме. Кроме того, оно ограничивает оповещение определёнными отслеживаемыми сущностями.

| Элемент | Тип | Описание |
| --- | --- | --- |
| delayInMinutes | integer | Отправить уведомление, если проблема остаётся открытой дольше *X* минут. |
| severityLevel | string | Уровень серьёзности для срабатывания оповещения. Возможные значения: * `AVAILABILITY` * `CUSTOM_ALERT` * `ERROR` * `MONITORING_UNAVAILABLE` * `PERFORMANCE` * `RESOURCE_CONTENTION` |
| tagFilter | [AlertingProfileTagFilter](#openapi-definition-AlertingProfileTagFilter) | Конфигурация фильтрации по тегам профиля оповещений. |

#### Объект `AlertingProfileTagFilter`

Конфигурация фильтрации по тегам профиля оповещений.

| Элемент | Тип | Описание |
| --- | --- | --- |
| includeMode | string | Режим фильтрации:  * `INCLUDE_ANY`: правило применяется к отслеживаемым сущностям, у которых есть хотя бы один из указанных тегов. Можно указать до 100 тегов. * `INCLUDE_ALL`: правило применяется к отслеживаемым сущностям, у которых есть **все** указанные теги. Можно указать до 10 тегов. * `NONE`: правило применяется ко всем отслеживаемым сущностям. Возможные значения: * `INCLUDE_ALL` * `INCLUDE_ANY` * `NONE` |
| tagFilters | [TagFilter[]](#openapi-definition-TagFilter) | Список обязательных тегов. |

#### Объект `TagFilter`

Фильтр отслеживаемых сущностей по тегам.

| Элемент | Тип | Описание |
| --- | --- | --- |
| context | string | Источник тега, например AWS или Cloud Foundry.  Пользовательские теги используют значение `CONTEXTLESS`. Возможные значения: * `AWS` * `AWS_GENERIC` * `AZURE` * `CLOUD_FOUNDRY` * `CONTEXTLESS` * `ENVIRONMENT` * `GOOGLE_CLOUD` * `KUBERNETES` |
| key | string | Ключ тега.  У пользовательских тегов здесь находится значение тега. |
| value | string | Значение тега.  Не применимо к пользовательским тегам. |

### JSON-модели тела ответа

```
{



"displayName": "sampleAlertingProfile",



"eventTypeFilters": [



{



"predefinedEventFilter": {



"eventType": "OSI_HIGH_CPU",



"negate": true



}



},



{



"customEventFilter": {



"customDescriptionFilter": {



"caseInsensitive": false,



"enabled": false,



"negate": true,



"operator": "CONTAINS",



"value": "filterValue"



},



"customTitleFilter": {



"caseInsensitive": true,



"enabled": true,



"negate": false,



"operator": "EQUALS",



"value": "filterValue"



}



}



}



],



"id": "12345678-abcd-1234-abcd-1234567890ab",



"mzId": "1",



"rules": [



{



"delayInMinutes": 60,



"severityLevel": "AVAILABILITY",



"tagFilter": {



"includeMode": "INCLUDE_ALL",



"tagFilters": [



{



"context": "AWS",



"key": "tagKey",



"value": "tagValue"



}



]



}



}



]



}
```

## Пример

В этом примере запрос возвращает параметры профиля оповещений **Transaction slowdown**.

API-токен передаётся в заголовке **Authorization**.

У профиля следующие параметры:

![GET example](https://dt-cdn.net/images/get-1347-c383260394.png)

GET example

#### Curl

```
curl -X GET \



https://mySampleEnv.live.dynatrace.com/api/config/v1/alertingProfiles/93ac79a3-8cba-4be5-af44-50673b5e77f2 \



-H 'Authorization: Api-Token dt0c01.abc123.abcdefjhij1234567890'
```

#### URL запроса

```
https://mySampleEnv.live.dynatrace.com/api/config/v1/alertingProfiles/93ac79a3-8cba-4be5-af44-50673b5e77f2
```

#### Тело ответа

```
{



"metadata": {



"currentConfigurationVersions": [



"7.0.0"



],



"configurationVersions": [],



"clusterVersion": "1.218.0.20210429-093737"



},



"id": "19e50c27-8aed-408f-ad44-d6a1bf856f49",



"displayName": "Transaction slowdown",



"rules": [



{



"severityLevel": "AVAILABILITY",



"tagFilter": {



"includeMode": "INCLUDE_ANY",



"tagFilters": [



{



"context": "CONTEXTLESS",



"key": "/rest",



"value": null



},



{



"context": "CONTEXTLESS",



"key": "/rest/configuration",



"value": null



}



]



},



"delayInMinutes": 1



}



],



"managementZoneId": 9130632296508575249,



"mzId": "9130632296508575249",



"eventTypeFilters": [



{



"predefinedEventFilter": {



"eventType": "APPLICATION_UNEXPECTED_HIGH_LOAD",



"negate": true



}



},



{



"predefinedEventFilter": {



"eventType": "SYNTHETIC_GLOBAL_OUTAGE",



"negate": false



}



}



]



}
```

#### Код ответа

200

## Связанные темы

* [Problem alerting profiles](/managed/analyze-explore-automate/notifications-and-alerting/alerting-profiles "Узнайте, как создавать профили оповещений и управлять ими.")
* [Dynatrace API - Tokens and authentication](/managed/dynatrace-api/basics/dynatrace-api-authentication "Как пройти аутентификацию для работы с Dynatrace API.")