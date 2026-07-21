---
title: Service detection API - GET an opaque web service rule
source: https://docs.dynatrace.com/managed/dynatrace-api/configuration-api/service-api/detection-rules/opaque-web-service/get-rule
---

# Service detection API - GET an opaque web service rule

# Service detection API - GET an opaque web service rule

* Справка
* Опубликовано 06 сентября 2019 г.

Показывает свойства указанного правила обнаружения сервиса для непрозрачных и внешних веб-сервисов.

Запрос возвращает данные в формате `application/json`.

|  |  |  |
| --- | --- | --- |
| GET | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/config/v1/service/detectionRules/OPAQUE_AND_EXTERNAL_WEB_SERVICE/{id}` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/config/v1/service/detectionRules/OPAQUE_AND_EXTERNAL_WEB_SERVICE/{id}` |

## Аутентификация

Для выполнения этого запроса нужен токен доступа со скоупом `ReadConfig`.

Подробнее о том, как его получить и использовать, см. [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Параметры

| Параметр | Тип | Описание | Расположение | Обязательный |
| --- | --- | --- | --- | --- |
| id | string | ID нужного правила обнаружения сервиса. | path | Обязательный |

## Ответ

См. [JSON models](/managed/dynatrace-api/configuration-api/service-api/detection-rules/models "Learn the variations of JSON models in the Dynatrace service detection rules API."), чтобы найти все JSON модели, зависящие от типа модели.

### Коды ответа

| Код | Тип | Описание |
| --- | --- | --- |
| **200** | [OpaqueAndExternalWebServiceRule](#openapi-definition-OpaqueAndExternalWebServiceRule) | Успех. Ответ содержит свойства указанного правила. |
| **404** | - | Ошибка. Правило с указанным ID не существует. |

### Объекты тела ответа

#### Объект `OpaqueAndExternalWebServiceRule`

Правило обнаружения сервиса типа `OPAQUE_AND_EXTERNAL_WEB_SERVICE`

| Элемент | Тип | Описание |
| --- | --- | --- |
| conditions | [ConditionsOpaqueAndExternalWebServiceAttributeTypeDto](#openapi-definition-ConditionsOpaqueAndExternalWebServiceAttributeTypeDto)[] | Список условий правила.  Если указано несколько условий, применяется логика AND. |
| description | string | Краткое описание правила. |
| detectAsWebRequestService | boolean | Обнаруживать совпадающие запросы как веб-сервисы (`false`) или как веб-request-сервисы (`true`).  Установка этого поля в `true` предотвращает обнаружение совпадающих запросов как непрозрачных веб-сервисов. Вместо этого создаётся непрозрачный веб-request-сервис. Если нужно дополнительно изменить результирующий веб-request-сервис, нужно создать отдельное правило типа `OPAQUE_AND_EXTERNAL_WEB_REQUEST`.  По умолчанию `false`, совпадающие запросы обнаруживаются как непрозрачные веб-сервисы. |
| enabled | boolean | Правило включено (`true`) или отключено (`false`). |
| id | string | ID правила обнаружения сервиса. |
| managementZones | string[] | Management zone (указывается по ID) группы процессов, для которой нужно создать это правило обнаружения сервиса.  Здесь можно указать только 1 management zone. |
| metadata | [ConfigurationMetadata](#openapi-definition-ConfigurationMetadata) | Метаданные, полезные для отладки |
| name | string | Название правила. |
| order | string | Порядок правила в списке правил.  Правила оцениваются сверху вниз. Применяется первое совпавшее правило. |
| port | [Port](#openapi-definition-Port) | Вклад порта, на котором был обнаружен веб-запрос, в расчёт ID сервиса. |
| type | string | Тип правила обнаружения сервиса. |
| urlPath | [UrlPath](#openapi-definition-UrlPath) | Вклад URL, на котором был обнаружен веб-запрос, в расчёт ID сервиса.  Есть два взаимоисключающих варианта:  * Переопределить обнаруженное значение указанным статическим значением. Указать новое значение в поле **valueOverride**. * Динамически преобразовать обнаруженное значение. Указать параметры преобразования в поле **transformations**. |

#### Объект `ConditionsOpaqueAndExternalWebServiceAttributeTypeDto`

Условие правила обнаружения сервиса.

| Элемент | Тип | Описание |
| --- | --- | --- |
| attributeType | string | Тип проверяемого атрибута. Элемент может принимать следующие значения * `ENDPOINT` * `IP` * `OPERATION_NAME` * `PG_TAG` * `URL_PATH` * `URL_PORT` |
| compareOperations | [CompareOperation](#openapi-definition-CompareOperation)[] | Список условий для правила.  Если указано несколько условий, применяется логика AND. |

#### Объект `CompareOperation`

Условие правила.

Фактический набор полей зависит от типа условия. Список фактических объектов см. в описании поля **type** или в [Service detection API - JSON models﻿](https://dt-url.net/2ie3slq?dt=m).

| Элемент | Тип | Описание |
| --- | --- | --- |
| type | string | Определяет фактический набор полей в зависимости от значения. См. один из следующих объектов:  * `EQUALS` -> EqualsCompareOperation * `STRING_CONTAINS` -> StringContainsCompareOperation * `STARTS_WITH` -> StartsWithCompareOperation * `ENDS_WITH` -> EndsWithCompareOperation * `EXISTS` -> ExistsCompareOperation * `IP_IN_RANGE` -> IpInRangeCompareOperation * `LESS_THAN` -> LessThanCompareOperation * `GREATER_THAN` -> GreaterThanCompareOperation * `INT_EQUALS` -> IntEqualsCompareOperation * `STRING_EQUALS` -> StringEqualsCompareOperation * `TAG` -> TagCompareOperation Элемент может принимать следующие значения * `ENDS_WITH` * `EQUALS` * `EXISTS` * `GREATER_THAN` * `INT_EQUALS` * `IP_IN_RANGE` * `LESS_THAN` * `STARTS_WITH` * `STRING_CONTAINS` * `STRING_EQUALS` * `TAG` |

#### Объект `ConfigurationMetadata`

Метаданные, полезные для отладки

| Элемент | Тип | Описание |
| --- | --- | --- |
| clusterVersion | string | Версия Dynatrace. |
| configurationVersions | integer[] | Отсортированный список номеров версий конфигурации. |
| currentConfigurationVersions | string[] | Отсортированный список номеров версий конфигурации. |

#### Объект `Port`

Вклад порта, на котором был обнаружен веб-запрос, в расчёт ID сервиса.

| Элемент | Тип | Описание |
| --- | --- | --- |
| doNotUseForServiceId | boolean | Порт используется (`false`) или не используется (`true`) в расчёте ID сервиса. |

#### Объект `UrlPath`

Вклад URL, на котором был обнаружен веб-запрос, в расчёт ID сервиса.

Есть два взаимоисключающих варианта:

* Переопределить обнаруженное значение указанным статическим значением. Указать новое значение в поле **valueOverride**.
* Динамически преобразовать обнаруженное значение. Указать параметры преобразования в поле **transformations**.

| Элемент | Тип | Описание |
| --- | --- | --- |
| transformations | [TransformationBase](#openapi-definition-TransformationBase)[] | Преобразования, применяемые к обнаруженному значению. |
| valueOverride | string | Значение, используемое вместо обнаруженного значения. |

#### Объект `TransformationBase`

Конфигурация преобразования обнаруженного значения.

Если указано несколько преобразований, они обрабатываются последовательно сверху вниз. Каждое преобразование применяется к результату предыдущего преобразования. Например, второе преобразование применяется к результату первого преобразования.

Фактический набор полей зависит от типа преобразования. Список фактических объектов см. в описании поля **type** или в [Service detection API - JSON models﻿](https://dt-url.net/2ie3slq?dt=m).

| Элемент | Тип | Описание |
| --- | --- | --- |
| type | string | Определяет фактический набор полей в зависимости от значения. См. один из следующих объектов:  * `BEFORE` -> BeforeTransformation * `AFTER` -> AfterTransformation * `BETWEEN` -> BetweenTransformation * `REPLACE_BETWEEN` -> ReplaceBetweenTransformation * `REMOVE_NUMBERS` -> RemoveNumbersTransformation * `REMOVE_CREDIT_CARDS` -> RemoveCreditCardNumbersTransformation * `REMOVE_IBANS` -> RemoveIBANsTransformation * `REMOVE_IPS` -> RemoveIPsTransformation * `SPLIT_SELECT` -> SplitSelectTransformation * `TAKE_SEGMENTS` -> TakeSegmentsTransformation Элемент может принимать следующие значения * `AFTER` * `BEFORE` * `BETWEEN` * `REMOVE_CREDIT_CARDS` * `REMOVE_IBANS` * `REMOVE_IPS` * `REMOVE_NUMBERS` * `REPLACE_BETWEEN` * `SPLIT_SELECT` * `TAKE_SEGMENTS` |

### Пример тела ответа JSON

```
{



"conditions": [



{



"attributeType": "URL_PATH",



"compareOperations": [



{



"ignoreCase": "false",



"invert": "false",



"type": "STRING_CONTAINS",



"values": [



"value1",



"value2"



]



}



]



}



],



"description": "REST API example",



"detectAsWebRequestService": false,



"enabled": true,



"managementZones": [



"zone 1"



],



"name": "My sample rule",



"port": {



"doNotUseForServiceId": "true"



},



"type": "OPAQUE_AND_EXTERNAL_WEB_SERVICE",



"urlPath": {



"valueOverride": "abc"



}



}
```

## Связанные темы

* [Service Detection v1](/managed/observe/application-observability/services/service-detection/service-detection-v1 "Find out how Dynatrace Service Detection v1 detects and names different types of services.")
* [Opaque services](/managed/observe/application-observability/services/service-detection/service-detection-v1/service-types/opaque-services "Understand what opaque services are.")