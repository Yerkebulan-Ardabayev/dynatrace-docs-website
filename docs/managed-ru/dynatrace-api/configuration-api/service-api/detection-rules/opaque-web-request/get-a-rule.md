---
title: Service detection API - GET an opaque web request rule
source: https://docs.dynatrace.com/managed/dynatrace-api/configuration-api/service-api/detection-rules/opaque-web-request/get-a-rule
---

# Service detection API - GET an opaque web request rule

# Service detection API - GET an opaque web request rule

* Справка
* Опубликовано 06 сентября 2019 г.

Показывает свойства указанного правила обнаружения сервисов для непрозрачных (opaque) и внешних веб-запросов.

Запрос возвращает содержимое типа `application/json`.

|  |  |  |
| --- | --- | --- |
| GET | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/config/v1/service/detectionRules/OPAQUE_AND_EXTERNAL_WEB_REQUEST/{id}` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/config/v1/service/detectionRules/OPAQUE_AND_EXTERNAL_WEB_REQUEST/{id}` |

## Аутентификация

Для выполнения этого запроса нужен токен доступа с областью действия `ReadConfig`.

О том, как получить и использовать такой токен, читай в разделе [Токены и аутентификация](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Параметры

| Параметр | Тип | Описание | Расположение | Обязательный |
| --- | --- | --- | --- | --- |
| id | string | ID нужного правила обнаружения сервисов. | путь | Обязательный |

## Ответ

Обратись к разделу [модели JSON](/managed/dynatrace-api/configuration-api/service-api/detection-rules/models "Learn the variations of JSON models in the Dynatrace service detection rules API."), чтобы найти все модели JSON, которые зависят от типа модели.

### Коды ответа

| Код | Тип | Описание |
| --- | --- | --- |
| **200** | [OpaqueAndExternalWebRequestRule](#openapi-definition-OpaqueAndExternalWebRequestRule) | Успех. Ответ содержит свойства указанного правила. |
| **404** | - | Ошибка. Правило с указанным ID не существует. |

### Объекты тела ответа


#### Объект `OpaqueAndExternalWebRequestRule`


Правило обнаружения сервиса типа `OPAQUE_AND_EXTERNAL_WEB_REQUEST`.


| Элемент | Тип | Описание |
| --- | --- | --- |
| applicationId | [ApplicationId](#openapi-definition-ApplicationId) | Вклад обнаруженного ID приложения в вычисление ID сервиса.  Доступны два взаимоисключающих варианта:  * Переопределить обнаруженное значение указанным статическим значением. Новое значение указывается в поле **valueOverride**. * Динамически преобразовать обнаруженное значение. Параметры преобразования указываются в поле **transformations**. |
| conditions | [ConditionsOpaqueAndExternalWebRequestAttributeTypeDto](#openapi-definition-ConditionsOpaqueAndExternalWebRequestAttributeTypeDto)[] | Список условий правила.  Если указано несколько условий, применяется логика AND. |
| contextRoot | [ContextRoot](#openapi-definition-ContextRoot) | Вклад обнаруженного контекстного корня в вычисление ID сервиса.  Контекстный корень, это первый сегмент URL запроса после имени сервера. Например, в URL `www.dynatrace.com/support/help/dynatrace-api/` контекстным корнем является `support`.  Доступны два варианта:  * Сохранить часть обнаруженного URL. Число сохраняемых сегментов указывается в поле **segmentsToCopyFromUrlPath**. * Динамически преобразовать обнаруженный URL. Параметры преобразования указываются в поле **transformations**.  Можно использовать один из вариантов или оба сразу. При использовании обоих преобразование применяется к изменённому URL. |
| description | string | Краткое описание правила. |
| enabled | boolean | Правило включено (`true`) или отключено (`false`). |
| id | string | ID правила обнаружения сервиса. |
| managementZones | string[] | Management zone (указывается ID) группы процессов, для которой должно быть создано это правило обнаружения сервиса.  Здесь можно указать только 1 management zone. |
| metadata | [ConfigurationMetadata](#openapi-definition-ConfigurationMetadata) | Метаданные, полезные для отладки |
| name | string | Название правила. |
| order | string | Порядок правила в списке правил.  Правила оцениваются сверху вниз. Применяется первое подходящее правило. |
| port | [Port](#openapi-definition-Port) | Вклад порта, на котором был обнаружен веб-запрос, в вычисление ID сервиса. |
| publicDomainName | [PublicDomainName](#openapi-definition-PublicDomainName) | Вклад доменного имени, на котором был обнаружен веб-запрос, в вычисление ID сервиса.  Доступны два взаимоисключающих варианта:  * Переопределить обнаруженное значение указанным статическим значением. Новое значение указывается в поле **valueOverride**. * Динамически преобразовать обнаруженное значение. Параметры преобразования указываются в поле **transformations**. |
| type | string | Тип правила обнаружения сервиса. |


#### Объект `ApplicationId`


Вклад обнаруженного ID приложения в вычисление ID сервиса.


Доступны два взаимоисключающих варианта:


* Переопределить обнаруженное значение указанным статическим значением. Новое значение указывается в поле **valueOverride**.
* Динамически преобразовать обнаруженное значение. Параметры преобразования указываются в поле **transformations**.


| Элемент | Тип | Описание |
| --- | --- | --- |
| transformations | [TransformationBase](#openapi-definition-TransformationBase)[] | Преобразования, применяемые к обнаруженному значению. |
| valueOverride | string | Значение, используемое вместо обнаруженного. |


#### Объект `TransformationBase`


Конфигурация преобразования обнаруженного значения.


Если указано несколько преобразований, они обрабатываются последовательно сверху вниз. Каждое преобразование применяется к результату предыдущего преобразования. Например, второе преобразование применяется к результату первого преобразования.


Фактический набор полей зависит от типа преобразования. Список фактических объектов приведён в описании поля **type** или см. [Service detection API - JSON models﻿](https://dt-url.net/2ie3slq?dt=m).


| Элемент | Тип | Описание |
| --- | --- | --- |
| type | string | Определяет фактический набор полей в зависимости от значения. См. один из следующих объектов:  * `BEFORE` -> BeforeTransformation * `AFTER` -> AfterTransformation * `BETWEEN` -> BetweenTransformation * `REPLACE_BETWEEN` -> ReplaceBetweenTransformation * `REMOVE_NUMBERS` -> RemoveNumbersTransformation * `REMOVE_CREDIT_CARDS` -> RemoveCreditCardNumbersTransformation * `REMOVE_IBANS` -> RemoveIBANsTransformation * `REMOVE_IPS` -> RemoveIPsTransformation * `SPLIT_SELECT` -> SplitSelectTransformation * `TAKE_SEGMENTS` -> TakeSegmentsTransformation Элемент может принимать следующие значения * `AFTER` * `BEFORE` * `BETWEEN` * `REMOVE_CREDIT_CARDS` * `REMOVE_IBANS` * `REMOVE_IPS` * `REMOVE_NUMBERS` * `REPLACE_BETWEEN` * `SPLIT_SELECT` * `TAKE_SEGMENTS` |


#### Объект `ConditionsOpaqueAndExternalWebRequestAttributeTypeDto`


Условие правила обнаружения сервиса.


| Элемент | Тип | Описание |
| --- | --- | --- |
| attributeType | string | Тип проверяемого атрибута. Элемент может принимать следующие значения * `IP` * `PG_TAG` * `TOP_LEVEL_DOMAIN` * `URL` * `URL_HOST_NAME` * `URL_PATH` * `URL_PORT` |
| compareOperations | [CompareOperation](#openapi-definition-CompareOperation)[] | Список условий для правила.  Если указано несколько условий, применяется логика AND. |


#### Объект `CompareOperation`


Условие правила.


Фактический набор полей зависит от типа условия. Список фактических объектов приведён в описании поля **type** или см. [Service detection API - JSON models﻿](https://dt-url.net/2ie3slq?dt=m).


| Элемент | Тип | Описание |
| --- | --- | --- |
| type | string | Определяет фактический набор полей в зависимости от значения. См. один из следующих объектов:  * `EQUALS` -> EqualsCompareOperation * `STRING_CONTAINS` -> StringContainsCompareOperation * `STARTS_WITH` -> StartsWithCompareOperation * `ENDS_WITH` -> EndsWithCompareOperation * `EXISTS` -> ExistsCompareOperation * `IP_IN_RANGE` -> IpInRangeCompareOperation * `LESS_THAN` -> LessThanCompareOperation * `GREATER_THAN` -> GreaterThanCompareOperation * `INT_EQUALS` -> IntEqualsCompareOperation * `STRING_EQUALS` -> StringEqualsCompareOperation * `TAG` -> TagCompareOperation Элемент может принимать следующие значения * `ENDS_WITH` * `EQUALS` * `EXISTS` * `GREATER_THAN` * `INT_EQUALS` * `IP_IN_RANGE` * `LESS_THAN` * `STARTS_WITH` * `STRING_CONTAINS` * `STRING_EQUALS` * `TAG` |


#### Объект `ContextRoot`


Вклад обнаруженного контекстного корня в вычисление ID сервиса.


Контекстный корень, это первый сегмент URL запроса после имени сервера. Например, в URL `www.dynatrace.com/support/help/dynatrace-api/` контекстным корнем является `support`.


Доступны два варианта:


* Сохранить часть обнаруженного URL. Число сохраняемых сегментов указывается в поле **segmentsToCopyFromUrlPath**.
* Динамически преобразовать обнаруженный URL. Параметры преобразования указываются в поле **transformations**.


Можно использовать один из вариантов или оба сразу. При использовании обоих преобразование применяется к изменённому URL.


| Элемент | Тип | Описание |
| --- | --- | --- |
| segmentsToCopyFromUrlPath | integer | Число сегментов URL, которые нужно сохранить.  URL делится по слэшам (`/`), индексация начинается с 1 от контекстного корня.  Например, если указать `2` для URL `www.dynatrace.com/support/help/dynatrace-api/`, используется значение `support/help`. |
| transformations | [ContextRootTransformation](#openapi-definition-ContextRootTransformation)[] | Преобразования, применяемые к обнаруженному значению. |


#### Объект `ContextRootTransformation`


Конфигурация преобразования обнаруженного значения.


Если указано несколько преобразований, они обрабатываются последовательно сверху вниз. Каждое преобразование применяется к результату предыдущего преобразования. Например, второе преобразование применяется к результату первого преобразования.


Фактический набор полей зависит от `type` преобразования.


| Элемент | Тип | Описание |
| --- | --- | --- |
| type | string | Определяет фактический набор полей в зависимости от значения. См. один из следующих объектов:  * `BEFORE` -> BeforeTransformation * `REPLACE_BETWEEN` -> ReplaceBetweenTransformation * `REMOVE_NUMBERS` -> RemoveNumbersTransformation * `REMOVE_CREDIT_CARDS` -> RemoveCreditCardNumbersTransformation * `REMOVE_IBANS` -> RemoveIBANsTransformation * `REMOVE_IPS` -> RemoveIPsTransformation Элемент может принимать следующие значения * `BEFORE` * `REMOVE_CREDIT_CARDS` * `REMOVE_IBANS` * `REMOVE_IPS` * `REMOVE_NUMBERS` * `REPLACE_BETWEEN` |


#### Объект `ConfigurationMetadata`


Метаданные, полезные для отладки


| Элемент | Тип | Описание |
| --- | --- | --- |
| clusterVersion | string | Версия Dynatrace. |
| configurationVersions | integer[] | Отсортированный список номеров версий конфигурации. |
| currentConfigurationVersions | string[] | Отсортированный список номеров версий конфигурации. |


#### Объект `Port`


Вклад порта, на котором был обнаружен веб-запрос, в вычисление ID сервиса.


| Элемент | Тип | Описание |
| --- | --- | --- |
| doNotUseForServiceId | boolean | Порт используется (`false`) или не используется (`true`) при вычислении ID сервиса. |


#### Объект `PublicDomainName`


Вклад доменного имени, на котором был обнаружен веб-запрос, в вычисление ID сервиса.


Доступны два взаимоисключающих варианта:


* Переопределить обнаруженное значение указанным статическим значением. Новое значение указывается в поле **valueOverride**.
* Динамически преобразовать обнаруженное значение. Параметры преобразования указываются в поле **transformations**.

| Element | Type | Description |
| --- | --- | --- |
| copyFromHostName | boolean | Использовать (`true`) или не использовать (`false`) обнаруженное имя хоста в качестве основы для преобразования. Не применяется, если указано переопределение. |
| transformations | [TransformationBase](#openapi-definition-TransformationBase)[] | Преобразования, применяемые к обнаруженному значению. |
| valueOverride | string | Значение, используемое вместо обнаруженного. |

### Тело ответа моделей JSON

```
{



"applicationId": {



"valueOverride": "abc"



},



"conditions": [



{



"attributeType": "URL_HOST_NAME",



"compareOperations": [



{



"ignoreCase": "false",



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



"zone1"



],



"name": "My sample rule",



"port": {



"doNotUseForServiceId": "true"



},



"publicDomainName": {



"copyFromHostName": "true",



"transformations": [



{



"delimiter": "/",



"type": "BEFORE"



}



]



},



"type": "OPAQUE_AND_EXTERNAL_WEB_REQUEST"



}
```

## Связанные темы

* [Service Detection v1](/managed/observe/application-observability/services/service-detection/service-detection-v1 "Find out how Dynatrace Service Detection v1 detects and names different types of services.")
* [Непрозрачные сервисы](/managed/observe/application-observability/services/service-detection/service-detection-v1/service-types/opaque-services "Understand what opaque services are.")
* [Мониторинг сторонних сервисов](/managed/observe/application-observability/services/service-detection/service-detection-v1/monitor-3rd-party-services "Configure how Dynatrace should monitor third-party services.")