---
title: Service detection API - GET a full web request rule
source: https://docs.dynatrace.com/managed/dynatrace-api/configuration-api/service-api/detection-rules/full-web-request/get-a-rule
---

# Service detection API - GET a full web request rule

# Service detection API - GET a full web request rule

* Справка
* Опубликовано 06 сент. 2019

Показывает свойства указанного правила обнаружения сервиса для полных веб-запросов.

Запрос возвращает содержимое типа `application/json`.

|  |  |  |
| --- | --- | --- |
| GET | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/config/v1/service/detectionRules/FULL_WEB_REQUEST/{id}` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/config/v1/service/detectionRules/FULL_WEB_REQUEST/{id}` |

## Аутентификация

Для выполнения этого запроса нужен токен доступа с областью действия `ReadConfig`.

О том, как получить и использовать токен, читай в разделе [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Параметры

| Параметр | Тип | Описание | В | Обязательный |
| --- | --- | --- | --- | --- |
| id | string | ID нужного правила обнаружения сервиса. | path | Обязательный |

## Ответ

Смотри [модели JSON](/managed/dynatrace-api/configuration-api/service-api/detection-rules/models "Learn the variations of JSON models in the Dynatrace service detection rules API."), чтобы найти все модели JSON, зависящие от типа модели.

### Коды ответа

| Код | Тип | Описание |
| --- | --- | --- |
| **200** | [FullWebRequestRule](#openapi-definition-FullWebRequestRule) | Успешно. Ответ содержит свойства указанного правила. |
| **404** | - | Ошибка. Правило с указанным ID не существует. |

### Объекты тела ответа

#### Объект `FullWebRequestRule`

Правило обнаружения сервиса типа `FULL_WEB_REQUEST`.

| Элемент | Тип | Описание |
| --- | --- | --- |
| applicationId | [ApplicationId](#openapi-definition-ApplicationId) | Вклад в расчёт ID сервиса от обнаруженного ID приложения. Доступны два взаимоисключающих варианта: * переопределить обнаруженное значение статическим значением, указав новое значение в поле **valueOverride**; * динамически преобразовать обнаруженное значение, указав параметры преобразования в поле **transformations**. |
| conditions | [ConditionsFullWebRequestAttributeTypeDto](#openapi-definition-ConditionsFullWebRequestAttributeTypeDto)[] | Список условий правила. Если указано несколько условий, применяется логика AND. |
| contextRoot | [ContextRoot](#openapi-definition-ContextRoot) | Вклад в расчёт ID сервиса от обнаруженного корневого контекста. Корневой контекст, это первый сегмент URL запроса после имени сервера. Например, в URL `www.dynatrace.com/support/help/dynatrace-api/` корневым контекстом является `support`. Доступны два варианта: * сохранить часть обнаруженного URL, указав число сохраняемых сегментов в поле **segmentsToCopyFromUrlPath**; * динамически преобразовать обнаруженный URL, указав параметры преобразования в поле **transformations**. Можно использовать один вариант или оба. При использовании обоих преобразование применяется к изменённому URL. |
| description | string | Краткое описание правила. |
| enabled | boolean | Правило включено (`true`) или отключено (`false`). |
| id | string | ID правила обнаружения сервиса. |
| managementZones | string[] | Management zone (указывается по ID) группы процессов, для которой нужно создать это правило обнаружения сервиса. Здесь можно указать только 1 management zone. |
| metadata | [ConfigurationMetadata](#openapi-definition-ConfigurationMetadata) | Метаданные, полезные для отладки |
| name | string | Название правила. |
| order | string | Порядок правила в списке правил. Правила оцениваются сверху вниз. Применяется первое подходящее правило. |
| serverName | [ServerName](#openapi-definition-ServerName) | Вклад в расчёт ID сервиса от обнаруженного имени сервера. Доступны два взаимоисключающих варианта: * переопределить обнаруженное значение статическим значением, указав новое значение в поле **valueOverride**; * динамически преобразовать обнаруженное значение, указав параметры преобразования в поле **transformations**. |
| type | string | Тип правила обнаружения сервиса. |

#### Объект `ApplicationId`

Вклад в расчёт ID сервиса от обнаруженного ID приложения.

Доступны два взаимоисключающих варианта:

* переопределить обнаруженное значение статическим значением, указав новое значение в поле **valueOverride**;
* динамически преобразовать обнаруженное значение, указав параметры преобразования в поле **transformations**.

| Элемент | Тип | Описание |
| --- | --- | --- |
| transformations | [TransformationBase](#openapi-definition-TransformationBase)[] | Преобразования, применяемые к обнаруженному значению. |
| valueOverride | string | Значение, используемое вместо обнаруженного значения. |

#### Объект `TransformationBase`

Конфигурация преобразования обнаруженного значения.

Если указано несколько преобразований, они обрабатываются последовательно сверху вниз. Каждое преобразование применяется к результату предыдущего преобразования. Например, второе преобразование применяется к результату первого преобразования.

Фактический набор полей зависит от типа преобразования. Список фактических объектов приведён в описании поля **type** или в разделе [Service detection API - JSON models﻿](https://dt-url.net/2ie3slq?dt=m).

| Элемент | Тип | Описание |
| --- | --- | --- |
| type | string | Определяет фактический набор полей в зависимости от значения. См. один из следующих объектов: * `BEFORE` -> BeforeTransformation * `AFTER` -> AfterTransformation * `BETWEEN` -> BetweenTransformation * `REPLACE_BETWEEN` -> ReplaceBetweenTransformation * `REMOVE_NUMBERS` -> RemoveNumbersTransformation * `REMOVE_CREDIT_CARDS` -> RemoveCreditCardNumbersTransformation * `REMOVE_IBANS` -> RemoveIBANsTransformation * `REMOVE_IPS` -> RemoveIPsTransformation * `SPLIT_SELECT` -> SplitSelectTransformation * `TAKE_SEGMENTS` -> TakeSegmentsTransformation Элемент может принимать следующие значения * `AFTER` * `BEFORE` * `BETWEEN` * `REMOVE_CREDIT_CARDS` * `REMOVE_IBANS` * `REMOVE_IPS` * `REMOVE_NUMBERS` * `REPLACE_BETWEEN` * `SPLIT_SELECT` * `TAKE_SEGMENTS` |

#### Объект `ConditionsFullWebRequestAttributeTypeDto`

Условие правила обнаружения сервиса.

| Элемент | Тип | Описание |
| --- | --- | --- |
| attributeType | string | Тип проверяемого атрибута. Элемент может принимать следующие значения * `APPLICATION_ID` * `CONTEXT_ROOT` * `PG_TAG` * `SERVER_NAME` * `URL_HOST_NAME` * `URL_PATH` |
| compareOperations | [CompareOperation](#openapi-definition-CompareOperation)[] | Список условий правила. Если указано несколько условий, применяется логика AND. |

#### Объект `CompareOperation`

Условие правила.

Фактический набор полей зависит от типа условия. Список фактических объектов приведён в описании поля **type** или в разделе [Service detection API - JSON models﻿](https://dt-url.net/2ie3slq?dt=m).

| Элемент | Тип | Описание |
| --- | --- | --- |
| type | string | Определяет фактический набор полей в зависимости от значения. См. один из следующих объектов: * `EQUALS` -> EqualsCompareOperation * `STRING_CONTAINS` -> StringContainsCompareOperation * `STARTS_WITH` -> StartsWithCompareOperation * `ENDS_WITH` -> EndsWithCompareOperation * `EXISTS` -> ExistsCompareOperation * `IP_IN_RANGE` -> IpInRangeCompareOperation * `LESS_THAN` -> LessThanCompareOperation * `GREATER_THAN` -> GreaterThanCompareOperation * `INT_EQUALS` -> IntEqualsCompareOperation * `STRING_EQUALS` -> StringEqualsCompareOperation * `TAG` -> TagCompareOperation Элемент может принимать следующие значения * `ENDS_WITH` * `EQUALS` * `EXISTS` * `GREATER_THAN` * `INT_EQUALS` * `IP_IN_RANGE` * `LESS_THAN` * `STARTS_WITH` * `STRING_CONTAINS` * `STRING_EQUALS` * `TAG` |

#### Объект `ContextRoot`

Вклад в расчёт ID сервиса от обнаруженного корневого контекста.

Корневой контекст, это первый сегмент URL запроса после имени сервера. Например, в URL `www.dynatrace.com/support/help/dynatrace-api/` корневым контекстом является `support`.

Доступны два варианта:

* сохранить часть обнаруженного URL, указав число сохраняемых сегментов в поле **segmentsToCopyFromUrlPath**;
* динамически преобразовать обнаруженный URL, указав параметры преобразования в поле **transformations**.

Можно использовать один вариант или оба. При использовании обоих преобразование применяется к изменённому URL.

| Элемент | Тип | Описание |
| --- | --- | --- |
| segmentsToCopyFromUrlPath | integer | Число сегментов URL, которые нужно сохранить. URL делится по слэшам (`/`), индексация начинается с 1 от корневого контекста. Например, если указать `2` для URL `www.dynatrace.com/support/help/dynatrace-api/`, используется значение `support/help`. |
| transformations | [ContextRootTransformation](#openapi-definition-ContextRootTransformation)[] | Преобразования, применяемые к обнаруженному значению. |

#### Объект `ContextRootTransformation`

Конфигурация преобразования обнаруженного значения.

Если указано несколько преобразований, они обрабатываются последовательно сверху вниз. Каждое преобразование применяется к результату предыдущего преобразования. Например, второе преобразование применяется к результату первого преобразования.

Фактический набор полей зависит от `type` преобразования.

| Элемент | Тип | Описание |
| --- | --- | --- |
| type | string | Определяет фактический набор полей в зависимости от значения. См. один из следующих объектов: * `BEFORE` -> BeforeTransformation * `REPLACE_BETWEEN` -> ReplaceBetweenTransformation * `REMOVE_NUMBERS` -> RemoveNumbersTransformation * `REMOVE_CREDIT_CARDS` -> RemoveCreditCardNumbersTransformation * `REMOVE_IBANS` -> RemoveIBANsTransformation * `REMOVE_IPS` -> RemoveIPsTransformation Элемент может принимать следующие значения * `BEFORE` * `REMOVE_CREDIT_CARDS` * `REMOVE_IBANS` * `REMOVE_IPS` * `REMOVE_NUMBERS` * `REPLACE_BETWEEN` |

#### Объект `ConfigurationMetadata`

Метаданные, полезные для отладки

| Элемент | Тип | Описание |
| --- | --- | --- |
| clusterVersion | string | Версия Dynatrace. |
| configurationVersions | integer[] | Отсортированный список номеров версий конфигурации. |
| currentConfigurationVersions | string[] | Отсортированный список номеров версий конфигурации. |

#### Объект `ServerName`

Вклад в расчёт ID сервиса от обнаруженного имени сервера.

Доступны два взаимоисключающих варианта:

* переопределить обнаруженное значение статическим значением, указав новое значение в поле **valueOverride**;
* динамически преобразовать обнаруженное значение, указав параметры преобразования в поле **transformations**.

| Элемент | Тип | Описание |
| --- | --- | --- |
| transformations | [TransformationBase](#openapi-definition-TransformationBase)[] | Преобразования, применяемые к обнаруженному значению. |
| valueOverride | string | Значение, используемое вместо обнаруженного значения. |

### Тело ответа JSON моделей

```
{



"applicationId": {



"valueOverride": "abc"



},



"conditions": [



{



"attributeType": "APPLICATION_ID",



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



"contextRoot": {



"segmentsToCopyFromUrlPath": 2,



"transformations": [



{



"delimiter": "/",



"type": "BEFORE"



}



]



},



"description": "REST API example",



"enabled": true,



"managementZones": [



"zone 1"



],



"name": "My sample rule",



"serverName": {



"transformations": [



{



"delimiter": "-",



"type": "BEFORE"



}



]



},



"type": "FULL_WEB_REQUEST"



}
```

## Похожие темы

* [Service Detection v1](/managed/observe/application-observability/services/service-detection/service-detection-v1 "Find out how Dynatrace Service Detection v1 detects and names different types of services.")