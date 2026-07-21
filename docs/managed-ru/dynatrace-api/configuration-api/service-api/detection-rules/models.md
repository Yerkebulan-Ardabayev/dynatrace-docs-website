---
title: Service detection API - JSON models
source: https://docs.dynatrace.com/managed/dynatrace-api/configuration-api/service-api/detection-rules/models
---

# Service detection API - JSON models

# Service detection API - JSON models

* Справка
* Опубликовано 06 авг. 2019 г.

JSON модели правил **Service detection rules** API сильно различаются в зависимости от **типа** некоторых объектов. Здесь можно найти JSON модели для каждого варианта.

## Варианты объекта `ServiceDetectionRule`

Объект `ServiceDetectionRule` служит базой для всех правил обнаружения сервисов. Фактический набор полей зависит от **типа** правила.

#### FULL\_WEB\_REQUEST

FullWebRequestRule

Параметры

JSON model

#### Объект `FullWebRequestRule`

Правило обнаружения сервиса типа `FULL_WEB_REQUEST`.

| Элемент | Тип | Описание |
| --- | --- | --- |
| applicationId | [ApplicationId](#openapi-definition-ApplicationId) | Вклад обнаруженного ID приложения в расчёт ID сервиса. Доступны два взаимоисключающих варианта: * Переопределить обнаруженное значение указанным статическим значением. Новое значение указывается в поле **valueOverride**. * Динамически преобразовать обнаруженное значение. Параметры преобразования указываются в поле **transformations**. |
| conditions | [ConditionsFullWebRequestAttributeTypeDto](#openapi-definition-ConditionsFullWebRequestAttributeTypeDto)[] | Список условий правила. Если указано несколько условий, применяется логика AND. |
| contextRoot | [ContextRoot](#openapi-definition-ContextRoot) | Вклад обнаруженного контекстного корня в расчёт ID сервиса. Контекстный корень, это первый сегмент URL запроса после имени сервера. Например, в URL `www.dynatrace.com/support/help/dynatrace-api/` контекстным корнем является `support`. Доступны два варианта: * Оставить часть обнаруженного URL. Количество сегментов, которые нужно сохранить, указывается в поле **segmentsToCopyFromUrlPath**. * Динамически преобразовать обнаруженный URL. Параметры преобразования указываются в поле **transformations**. Можно использовать один или оба варианта. При использовании обоих преобразование применяется к изменённому URL. |
| description | string | Краткое описание правила. |
| enabled | boolean | Правило включено (`true`) или отключено (`false`). |
| id | string | ID правила обнаружения сервиса. |
| managementZones | string[] | Management zone (указывается по ID) группы процессов, для которой нужно создать это правило обнаружения сервиса. Здесь можно указать только 1 management zone. |
| metadata | [ConfigurationMetadata](#openapi-definition-ConfigurationMetadata) | Метаданные, полезные для отладки |
| name | string | Название правила. |
| order | string | Порядок правила в списке правил. Правила оцениваются сверху вниз. Применяется первое совпавшее правило. |
| serverName | [ServerName](#openapi-definition-ServerName) | Вклад обнаруженного имени сервера в расчёт ID сервиса. Доступны два взаимоисключающих варианта: * Переопределить обнаруженное значение указанным статическим значением. Новое значение указывается в поле **valueOverride**. * Динамически преобразовать обнаруженное значение. Параметры преобразования указываются в поле **transformations**. |
| type | string | Тип правила обнаружения сервиса. |

#### Объект `ApplicationId`

Вклад обнаруженного ID приложения в расчёт ID сервиса.

Доступны два взаимоисключающих варианта:

* Переопределить обнаруженное значение указанным статическим значением. Новое значение указывается в поле **valueOverride**.
* Динамически преобразовать обнаруженное значение. Параметры преобразования указываются в поле **transformations**.

| Элемент | Тип | Описание |
| --- | --- | --- |
| transformations | [TransformationBase](#openapi-definition-TransformationBase)[] | Преобразования, применяемые к обнаруженному значению. |
| valueOverride | string | Значение, которое нужно использовать вместо обнаруженного значения. |

#### Объект `TransformationBase`

Конфигурация преобразования обнаруженного значения.

Если указано несколько преобразований, они обрабатываются последовательно сверху вниз. Каждое преобразование применяется к результату предыдущего преобразования. Например, второе преобразование применяется к результату первого преобразования.

Фактический набор полей зависит от типа преобразования. Список фактических объектов приведён в описании поля **type** или см. [Service detection API - JSON models﻿](https://dt-url.net/2ie3slq?dt=m).

| Элемент | Тип | Описание |
| --- | --- | --- |
| type | string | Определяет фактический набор полей в зависимости от значения. См. один из следующих объектов: * `BEFORE` -> BeforeTransformation * `AFTER` -> AfterTransformation * `BETWEEN` -> BetweenTransformation * `REPLACE_BETWEEN` -> ReplaceBetweenTransformation * `REMOVE_NUMBERS` -> RemoveNumbersTransformation * `REMOVE_CREDIT_CARDS` -> RemoveCreditCardNumbersTransformation * `REMOVE_IBANS` -> RemoveIBANsTransformation * `REMOVE_IPS` -> RemoveIPsTransformation * `SPLIT_SELECT` -> SplitSelectTransformation * `TAKE_SEGMENTS` -> TakeSegmentsTransformation Элемент может принимать следующие значения * `AFTER` * `BEFORE` * `BETWEEN` * `REMOVE_CREDIT_CARDS` * `REMOVE_IBANS` * `REMOVE_IPS` * `REMOVE_NUMBERS` * `REPLACE_BETWEEN` * `SPLIT_SELECT` * `TAKE_SEGMENTS` |

#### Объект `ConditionsFullWebRequestAttributeTypeDto`

Условие правила обнаружения сервиса.

| Элемент | Тип | Описание |
| --- | --- | --- |
| attributeType | string | Тип проверяемого атрибута. Элемент может принимать следующие значения * `APPLICATION_ID` * `CONTEXT_ROOT` * `PG_TAG` * `SERVER_NAME` * `URL_HOST_NAME` * `URL_PATH` |
| compareOperations | [CompareOperation](#openapi-definition-CompareOperation)[] | Список условий для правила. Если указано несколько условий, применяется логика AND. |

#### Объект `CompareOperation`

Условие правила.

Фактический набор полей зависит от типа условия. Список фактических объектов приведён в описании поля **type** или см. [Service detection API - JSON models﻿](https://dt-url.net/2ie3slq?dt=m).

| Элемент | Тип | Описание |
| --- | --- | --- |
| type | string | Определяет фактический набор полей в зависимости от значения. См. один из следующих объектов: * `EQUALS` -> EqualsCompareOperation * `STRING_CONTAINS` -> StringContainsCompareOperation * `STARTS_WITH` -> StartsWithCompareOperation * `ENDS_WITH` -> EndsWithCompareOperation * `EXISTS` -> ExistsCompareOperation * `IP_IN_RANGE` -> IpInRangeCompareOperation * `LESS_THAN` -> LessThanCompareOperation * `GREATER_THAN` -> GreaterThanCompareOperation * `INT_EQUALS` -> IntEqualsCompareOperation * `STRING_EQUALS` -> StringEqualsCompareOperation * `TAG` -> TagCompareOperation Элемент может принимать следующие значения * `ENDS_WITH` * `EQUALS` * `EXISTS` * `GREATER_THAN` * `INT_EQUALS` * `IP_IN_RANGE` * `LESS_THAN` * `STARTS_WITH` * `STRING_CONTAINS` * `STRING_EQUALS` * `TAG` |

#### Объект `ContextRoot`

Вклад обнаруженного контекстного корня в расчёт ID сервиса.

Контекстный корень, это первый сегмент URL запроса после имени сервера. Например, в URL `www.dynatrace.com/support/help/dynatrace-api/` контекстным корнем является `support`.

Доступны два варианта:

* Оставить часть обнаруженного URL. Количество сегментов, которые нужно сохранить, указывается в поле **segmentsToCopyFromUrlPath**.
* Динамически преобразовать обнаруженный URL. Параметры преобразования указываются в поле **transformations**.

Можно использовать один или оба варианта. При использовании обоих преобразование применяется к изменённому URL.

| Элемент | Тип | Описание |
| --- | --- | --- |
| segmentsToCopyFromUrlPath | integer | Количество сегментов URL, которые нужно сохранить. URL делится косыми чертами (`/`), индексация начинается с 1 от контекстного корня. Например, если указать `2` для URL `www.dynatrace.com/support/help/dynatrace-api/`, будет использовано значение `support/help`. |
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

Вклад обнаруженного имени сервера в расчёт ID сервиса.

Доступны два взаимоисключающих варианта:

* Переопределить обнаруженное значение указанным статическим значением. Новое значение указывается в поле **valueOverride**.
* Динамически преобразовать обнаруженное значение. Параметры преобразования указываются в поле **transformations**.

| Элемент | Тип | Описание |
| --- | --- | --- |
| transformations | [TransformationBase](#openapi-definition-TransformationBase)[] | Преобразования, применяемые к обнаруженному значению. |
| valueOverride | string | Значение, которое нужно использовать вместо обнаруженного значения. |

Это модель тела запроса, показывающая возможные элементы. Её нужно адаптировать для использования в реальном запросе.

```
{



"type": "FULL_WEB_REQUEST",



"id": "f69d6702-9b6e-4c47-b94c-628acc391995",



"order": "1",



"name": "string",



"description": "string",



"enabled": true,



"conditions": [



{



"attributeType": "URL_PATH",



"compareOperations": [



{



"type": "STRING_CONTAINS",



"negate": false,



"ignoreCase": true,



"values": [



"string"



]



}



]



}



],



"applicationId": {



"transformations": [],



"valueOverride": "string"



},



"contextRoot": {



"transformations": [



{



"type": "AFTER",



"delimiter": "string"



}



],



"segmentsToCopyFromUrlPath": 2



},



"serverName": {



"transformations": [



{



"type": "BEFORE",



"delimiter": "string"



}



]



}



}
```


#### OPAQUE\_AND\_EXTERNAL\_WEB\_REQUEST


OpaqueAndExternalWebRequestRule


Параметры


модель JSON


#### Объект `OpaqueAndExternalWebRequestRule`


Правило обнаружения сервиса типа `OPAQUE_AND_EXTERNAL_WEB_REQUEST`.


| Элемент | Тип | Описание |
| --- | --- | --- |
| applicationId | [ApplicationId](#openapi-definition-ApplicationId) | Вклад в расчёт ID сервиса от обнаруженного ID приложения.  Доступны два взаимоисключающих варианта:  * Переопределить обнаруженное значение указанным статическим значением. Указать новое значение в поле **valueOverride**. * Динамически преобразовать обнаруженное значение. Указать параметры преобразования в поле **transformations**. |
| conditions | [ConditionsOpaqueAndExternalWebRequestAttributeTypeDto](#openapi-definition-ConditionsOpaqueAndExternalWebRequestAttributeTypeDto)[] | Список условий правила.  Если указано несколько условий, применяется логика AND. |
| contextRoot | [ContextRoot](#openapi-definition-ContextRoot) | Вклад в расчёт ID сервиса от обнаруженного корневого контекста.  Корневой контекст, это первый сегмент URL запроса после имени сервера. Например, в URL `www.dynatrace.com/support/help/dynatrace-api/` корневой контекст, это `support`.  Доступны два варианта:  * Сохранить часть обнаруженного URL. Указать число сегментов, которые нужно сохранить, в поле **segmentsToCopyFromUrlPath**. * Динамически преобразовать обнаруженный URL. Указать параметры преобразования в поле **transformations**.  Можно использовать один вариант или оба. При использовании обоих преобразование применяется к изменённому URL. |
| description | string | Краткое описание правила. |
| enabled | boolean | Правило включено (`true`) или отключено (`false`). |
| id | string | ID правила обнаружения сервиса. |
| managementZones | string[] | Management zone (указанная по ID) группы процессов, для которой должно быть создано это правило обнаружения сервиса.  Здесь можно указать только 1 management zone. |
| metadata | [ConfigurationMetadata](#openapi-definition-ConfigurationMetadata) | Метаданные, полезные для отладки |
| name | string | Название правила. |
| order | string | Порядок правила в списке правил.  Правила проверяются сверху вниз. Применяется первое подходящее правило. |
| port | [Port](#openapi-definition-Port) | Вклад в расчёт ID сервиса от порта, на котором был обнаружен веб-запрос. |
| publicDomainName | [PublicDomainName](#openapi-definition-PublicDomainName) | Вклад в расчёт ID сервиса от имени домена, на котором был обнаружен веб-запрос.  Доступны два взаимоисключающих варианта:  * Переопределить обнаруженное значение указанным статическим значением. Указать новое значение в поле **valueOverride**. * Динамически преобразовать обнаруженное значение. Указать параметры преобразования в поле **transformations**. |
| type | string | Тип правила обнаружения сервиса. |


#### Объект `ApplicationId`


Вклад в расчёт ID сервиса от обнаруженного ID приложения.


Доступны два взаимоисключающих варианта:


* Переопределить обнаруженное значение указанным статическим значением. Указать новое значение в поле **valueOverride**.
* Динамически преобразовать обнаруженное значение. Указать параметры преобразования в поле **transformations**.


| Элемент | Тип | Описание |
| --- | --- | --- |
| transformations | [TransformationBase](#openapi-definition-TransformationBase)[] | Преобразования, применяемые к обнаруженному значению. |
| valueOverride | string | Значение, которое нужно использовать вместо обнаруженного. |


#### Объект `TransformationBase`


Конфигурация преобразования обнаруженного значения.


Если указано несколько преобразований, они обрабатываются последовательно сверху вниз. Каждое преобразование применяется к результату предыдущего преобразования. Например, второе преобразование применяется к результату первого.


Фактический набор полей зависит от типа преобразования. Список фактических объектов приведён в описании поля **type** или см. [Service detection API - JSON models﻿](https://dt-url.net/2ie3slq?dt=m).


| Элемент | Тип | Описание |
| --- | --- | --- |
| type | string | Определяет фактический набор полей в зависимости от значения. См. один из следующих объектов:  * `BEFORE` -> BeforeTransformation * `AFTER` -> AfterTransformation * `BETWEEN` -> BetweenTransformation * `REPLACE_BETWEEN` -> ReplaceBetweenTransformation * `REMOVE_NUMBERS` -> RemoveNumbersTransformation * `REMOVE_CREDIT_CARDS` -> RemoveCreditCardNumbersTransformation * `REMOVE_IBANS` -> RemoveIBANsTransformation * `REMOVE_IPS` -> RemoveIPsTransformation * `SPLIT_SELECT` -> SplitSelectTransformation * `TAKE_SEGMENTS` -> TakeSegmentsTransformation Элемент может принимать следующие значения * `AFTER` * `BEFORE` * `BETWEEN` * `REMOVE_CREDIT_CARDS` * `REMOVE_IBANS` * `REMOVE_IPS` * `REMOVE_NUMBERS` * `REPLACE_BETWEEN` * `SPLIT_SELECT` * `TAKE_SEGMENTS` |


#### Объект `ConditionsOpaqueAndExternalWebRequestAttributeTypeDto`


Условие правила обнаружения сервиса.


| Элемент | Тип | Описание |
| --- | --- | --- |
| attributeType | string | Тип атрибута, который нужно проверить. Элемент может принимать следующие значения * `IP` * `PG_TAG` * `TOP_LEVEL_DOMAIN` * `URL` * `URL_HOST_NAME` * `URL_PATH` * `URL_PORT` |
| compareOperations | [CompareOperation](#openapi-definition-CompareOperation)[] | Список условий для правила.  Если указано несколько условий, применяется логика AND. |


#### Объект `CompareOperation`


Условие правила.


Фактический набор полей зависит от типа условия. Список фактических объектов приведён в описании поля **type** или см. [Service detection API - JSON models﻿](https://dt-url.net/2ie3slq?dt=m).


| Элемент | Тип | Описание |
| --- | --- | --- |
| type | string | Определяет фактический набор полей в зависимости от значения. См. один из следующих объектов:  * `EQUALS` -> EqualsCompareOperation * `STRING_CONTAINS` -> StringContainsCompareOperation * `STARTS_WITH` -> StartsWithCompareOperation * `ENDS_WITH` -> EndsWithCompareOperation * `EXISTS` -> ExistsCompareOperation * `IP_IN_RANGE` -> IpInRangeCompareOperation * `LESS_THAN` -> LessThanCompareOperation * `GREATER_THAN` -> GreaterThanCompareOperation * `INT_EQUALS` -> IntEqualsCompareOperation * `STRING_EQUALS` -> StringEqualsCompareOperation * `TAG` -> TagCompareOperation Элемент может принимать следующие значения * `ENDS_WITH` * `EQUALS` * `EXISTS` * `GREATER_THAN` * `INT_EQUALS` * `IP_IN_RANGE` * `LESS_THAN` * `STARTS_WITH` * `STRING_CONTAINS` * `STRING_EQUALS` * `TAG` |


#### Объект `ContextRoot`


Вклад в расчёт ID сервиса от обнаруженного корневого контекста.


Корневой контекст, это первый сегмент URL запроса после имени сервера. Например, в URL `www.dynatrace.com/support/help/dynatrace-api/` корневой контекст, это `support`.


Доступны два варианта:


* Сохранить часть обнаруженного URL. Указать число сегментов, которые нужно сохранить, в поле **segmentsToCopyFromUrlPath**.
* Динамически преобразовать обнаруженный URL. Указать параметры преобразования в поле **transformations**.


Можно использовать один вариант или оба. При использовании обоих преобразование применяется к изменённому URL.


| Элемент | Тип | Описание |
| --- | --- | --- |
| segmentsToCopyFromUrlPath | integer | Число сегментов URL, которые нужно сохранить.  URL делится косыми чертами (`/`), индексация начинается с 1 от корневого контекста.  Например, если указать `2` для URL `www.dynatrace.com/support/help/dynatrace-api/`, будет использовано значение `support/help`. |
| transformations | [ContextRootTransformation](#openapi-definition-ContextRootTransformation)[] | Преобразования, применяемые к обнаруженному значению. |


#### Объект `ContextRootTransformation`


Конфигурация преобразования обнаруженного значения.


Если указано несколько преобразований, они обрабатываются последовательно сверху вниз. Каждое преобразование применяется к результату предыдущего преобразования. Например, второе преобразование применяется к результату первого.


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


Вклад в расчёт ID сервиса от порта, на котором был обнаружен веб-запрос.


| Элемент | Тип | Описание |
| --- | --- | --- |
| doNotUseForServiceId | boolean | Порт используется (`false`) или не используется (`true`) в расчёте ID сервиса. |


#### Объект `PublicDomainName`


Вклад в расчёт ID сервиса от доменного имени, на котором был обнаружен веб-запрос.


Доступны два взаимоисключающих варианта:


* Переопределить обнаруженное значение указанным статическим значением. Указать новое значение в поле **valueOverride**.
* Динамически преобразовать обнаруженное значение. Указать параметры преобразования в поле **transformations**.


| Элемент | Тип | Описание |
| --- | --- | --- |
| copyFromHostName | boolean | Использовать (`true`) или не использовать (`false`) обнаруженное имя хоста как основу для преобразования. Неприменимо, если указано переопределение. |
| transformations | [TransformationBase](#openapi-definition-TransformationBase)[] | Преобразования, применяемые к обнаруженному значению. |
| valueOverride | string | Значение, используемое вместо обнаруженного значения. |


Это модель тела запроса, показывающая возможные элементы. Её нужно адаптировать для использования в реальном запросе.


```
{



"type": "OPAQUE_AND_EXTERNAL_WEB_REQUEST",



"id": "9c22d0b1-e731-4baf-b3d0-140d14ead3c5",



"order": "2",



"name": "string",



"description": "string",



"enabled": true,



"conditions": [



{



"attributeType": "TOP_LEVEL_DOMAIN",



"compareOperations": [



{



"type": "ENDS_WITH",



"negate": false,



"ignoreCase": true,



"values": [



"string"



]



}



]



}



],



"applicationId": null,



"contextRoot": {



"transformations": [],



"segmentsToCopyFromUrlPath": 1



},



"port": null,



"publicDomainName": null



}
```


#### FULL\_WEB\_SERVICE


FullWebServiceRule


Параметры


Модель JSON


#### Объект `FullWebServiceRule`


Правило обнаружения сервиса типа `FULL_WEB_SERVICE`.


Если есть условие с **attributeType**, установленным в `FRAMEWORK`, поле **values** из **compareOperations** ограничено следующими возможными значениями:


* `AXIS`
* `CXF`
* `HESSIAN`
* `JAX_WS_RI`
* `JBOSS`
* `JERSEY`
* `PROGRESS`
* `RESTEASY`
* `RESTLET`
* `SPRING`
* `TIBCO`
* `WEBLOGIC`
* `WEBMETHODS`
* `WEBSPHERE`
* `WINK`


| Элемент | Тип | Описание |
| --- | --- | --- |
| applicationId | [ApplicationId](#openapi-definition-ApplicationId) | Вклад в расчёт ID сервиса от обнаруженного ID приложения.  Доступны два взаимоисключающих варианта:  * Переопределить обнаруженное значение указанным статическим значением. Указать новое значение в поле **valueOverride**. * Динамически преобразовать обнаруженное значение. Указать параметры преобразования в поле **transformations**. |
| conditions | [ConditionsFullWebServiceAttributeTypeDto](#openapi-definition-ConditionsFullWebServiceAttributeTypeDto)[] | Список условий правила.  Если указано несколько условий, применяется логика AND. |
| contextRoot | [ContextRoot](#openapi-definition-ContextRoot) | Вклад в расчёт ID сервиса от обнаруженного корневого контекста.  Корневой контекст, это первый сегмент URL запроса после имени сервера. Например, в URL `www.dynatrace.com/support/help/dynatrace-api/` корневой контекст, это `support`.  Доступны два варианта:  * Сохранить часть обнаруженного URL. Указать число сегментов, которые нужно сохранить, в поле **segmentsToCopyFromUrlPath**. * Динамически преобразовать обнаруженный URL. Указать параметры преобразования в поле **transformations**.  Можно использовать один или оба варианта. При использовании обоих преобразование применяется к изменённому URL. |
| description | string | Краткое описание правила. |
| detectAsWebRequestService | boolean | Определять совпадающие запросы как полные веб-сервисы (`false`) или как сервисы веб-запросов (`true`).  Установка этого поля в `true` предотвращает определение совпадающих запросов как полных веб-сервисов. Вместо этого создаётся сервис веб-запроса. Если нужно дополнительно изменить получившийся сервис веб-запроса, нужно создать отдельное правило типа `FULL_WEB_REQUEST`.  По умолчанию `false`, совпадающие запросы определяются как полные веб-сервисы. |
| enabled | boolean | Правило включено (`true`) или отключено (`false`). |
| id | string | ID правила обнаружения сервиса. |
| managementZones | string[] | Management zone (указывается по ID) группы процессов, для которой должно быть создано это правило обнаружения сервиса.  Здесь можно указать только 1 management zone. |
| metadata | [ConfigurationMetadata](#openapi-definition-ConfigurationMetadata) | Метаданные, полезные для отладки |
| name | string | Имя правила. |
| order | string | Порядок правила в списке правил.  Правила проверяются сверху вниз. Применяется первое совпавшее правило. |
| serverName | [ServerName](#openapi-definition-ServerName) | Вклад в расчёт ID сервиса от обнаруженного имени сервера.  Доступны два взаимоисключающих варианта:  * Переопределить обнаруженное значение указанным статическим значением. Указать новое значение в поле **valueOverride**. * Динамически преобразовать обнаруженное значение. Указать параметры преобразования в поле **transformations**. |
| type | string | Тип правила обнаружения сервиса. |
| webServiceName | [WebServiceName](#openapi-definition-WebServiceName) | Вклад в расчёт ID сервиса от обнаруженного имени веб-сервиса.  Доступны два взаимоисключающих варианта:  * Переопределить обнаруженное значение указанным статическим значением. Указать новое значение в поле **valueOverride**. * Динамически преобразовать обнаруженное значение. Указать параметры преобразования в поле **transformations**. |
| webServiceNameSpace | [WebServiceNameSpace](#openapi-definition-WebServiceNameSpace) | Вклад в расчёт ID сервиса от обнаруженного пространства имён веб-сервиса.  Доступны два взаимоисключающих варианта:  * Переопределить обнаруженное значение указанным статическим значением. Указать новое значение в поле **valueOverride**. * Динамически преобразовать обнаруженное значение. Указать параметры преобразования в поле **transformations**. |


#### Объект `ApplicationId`


Вклад в расчёт ID сервиса от обнаруженного ID приложения.


Доступны два взаимоисключающих варианта:


* Переопределить обнаруженное значение указанным статическим значением. Указать новое значение в поле **valueOverride**.
* Динамически преобразовать обнаруженное значение. Указать параметры преобразования в поле **transformations**.


| Элемент | Тип | Описание |
| --- | --- | --- |
| transformations | [TransformationBase](#openapi-definition-TransformationBase)[] | Преобразования, применяемые к обнаруженному значению. |
| valueOverride | string | Значение, используемое вместо обнаруженного значения. |


#### Объект `TransformationBase`


Конфигурация преобразования обнаруженного значения.


Если указано несколько преобразований, они обрабатываются последовательно сверху вниз. Каждое преобразование применяется к результату предыдущего преобразования. Например, второе преобразование применяется к результату первого преобразования.


Фактический набор полей зависит от типа преобразования. Список фактических объектов приведён в описании поля **type** или см. [Service detection API - JSON models﻿](https://dt-url.net/2ie3slq?dt=m).


| Элемент | Тип | Описание |
| --- | --- | --- |
| type | string | Определяет фактический набор полей в зависимости от значения. См. один из следующих объектов:  * `BEFORE` -> BeforeTransformation * `AFTER` -> AfterTransformation * `BETWEEN` -> BetweenTransformation * `REPLACE_BETWEEN` -> ReplaceBetweenTransformation * `REMOVE_NUMBERS` -> RemoveNumbersTransformation * `REMOVE_CREDIT_CARDS` -> RemoveCreditCardNumbersTransformation * `REMOVE_IBANS` -> RemoveIBANsTransformation * `REMOVE_IPS` -> RemoveIPsTransformation * `SPLIT_SELECT` -> SplitSelectTransformation * `TAKE_SEGMENTS` -> TakeSegmentsTransformation Элемент может принимать следующие значения * `AFTER` * `BEFORE` * `BETWEEN` * `REMOVE_CREDIT_CARDS` * `REMOVE_IBANS` * `REMOVE_IPS` * `REMOVE_NUMBERS` * `REPLACE_BETWEEN` * `SPLIT_SELECT` * `TAKE_SEGMENTS` |


#### Объект `ConditionsFullWebServiceAttributeTypeDto`


Условие правила обнаружения сервиса.


| Элемент | Тип | Описание |
| --- | --- | --- |
| attributeType | string | Тип проверяемого атрибута. Элемент может принимать следующие значения * `APPLICATION_ID` * `CONTEXT_ROOT` * `FRAMEWORK` * `IS_SOAP_SERVICE` * `PG_TAG` * `SERVER_NAME` * `URL_HOST_NAME` * `URL_PATH` * `WEBSERVICE_METHOD` * `WEBSERVICE_NAME` * `WEBSERVICE_NAMESPACE` |
| compareOperations | [CompareOperation](#openapi-definition-CompareOperation)[] | Список условий правила.  Если указано несколько условий, применяется логика AND. |


#### Объект `CompareOperation`


Условие правила.


Фактический набор полей зависит от типа условия. Список фактических объектов приведён в описании поля **type** или см. [Service detection API - JSON models﻿](https://dt-url.net/2ie3slq?dt=m).

| Element | Type | Description |
| --- | --- | --- |
| type | string | Определяет фактический набор полей в зависимости от значения. См. один из следующих объектов:  * `EQUALS` -> EqualsCompareOperation * `STRING_CONTAINS` -> StringContainsCompareOperation * `STARTS_WITH` -> StartsWithCompareOperation * `ENDS_WITH` -> EndsWithCompareOperation * `EXISTS` -> ExistsCompareOperation * `IP_IN_RANGE` -> IpInRangeCompareOperation * `LESS_THAN` -> LessThanCompareOperation * `GREATER_THAN` -> GreaterThanCompareOperation * `INT_EQUALS` -> IntEqualsCompareOperation * `STRING_EQUALS` -> StringEqualsCompareOperation * `TAG` -> TagCompareOperation Элемент может принимать следующие значения * `ENDS_WITH` * `EQUALS` * `EXISTS` * `GREATER_THAN` * `INT_EQUALS` * `IP_IN_RANGE` * `LESS_THAN` * `STARTS_WITH` * `STRING_CONTAINS` * `STRING_EQUALS` * `TAG` |


#### Объект `ContextRoot`


Вклад в расчёт ID сервиса от обнаруженного контекстного корня.


Контекстный корень, это первый сегмент URL запроса после имени сервера. Например, в URL `www.dynatrace.com/support/help/dynatrace-api/` контекстным корнем является `support`.


Доступны два варианта:


* Сохранить часть обнаруженного URL. Указать количество сохраняемых сегментов в поле **segmentsToCopyFromUrlPath**.
* Динамически преобразовать обнаруженный URL. Указать параметры преобразования в поле **transformations**.


Можно использовать один или оба варианта. При использовании обоих преобразование применяется к изменённому URL.


| Element | Type | Description |
| --- | --- | --- |
| segmentsToCopyFromUrlPath | integer | Количество сохраняемых сегментов URL.  URL делится символами слэша (`/`), индексация начинается с 1 от контекстного корня.  Например, если указать `2` для URL `www.dynatrace.com/support/help/dynatrace-api/`, используется значение `support/help`. |
| transformations | [ContextRootTransformation](#openapi-definition-ContextRootTransformation)[] | Преобразования, применяемые к обнаруженному значению. |


#### Объект `ContextRootTransformation`


Конфигурация преобразования обнаруженного значения.


Если указано несколько преобразований, они обрабатываются последовательно сверху вниз. Каждое преобразование применяется к результату предыдущего. Например, второе преобразование применяется к результату первого.


Фактический набор полей зависит от `type` преобразования.


| Element | Type | Description |
| --- | --- | --- |
| type | string | Определяет фактический набор полей в зависимости от значения. См. один из следующих объектов:  * `BEFORE` -> BeforeTransformation * `REPLACE_BETWEEN` -> ReplaceBetweenTransformation * `REMOVE_NUMBERS` -> RemoveNumbersTransformation * `REMOVE_CREDIT_CARDS` -> RemoveCreditCardNumbersTransformation * `REMOVE_IBANS` -> RemoveIBANsTransformation * `REMOVE_IPS` -> RemoveIPsTransformation Элемент может принимать следующие значения * `BEFORE` * `REMOVE_CREDIT_CARDS` * `REMOVE_IBANS` * `REMOVE_IPS` * `REMOVE_NUMBERS` * `REPLACE_BETWEEN` |


#### Объект `ConfigurationMetadata`


Метаданные, полезные для отладки


| Element | Type | Description |
| --- | --- | --- |
| clusterVersion | string | Версия Dynatrace. |
| configurationVersions | integer[] | Отсортированный список номеров версий конфигурации. |
| currentConfigurationVersions | string[] | Отсортированный список номеров версий конфигурации. |


#### Объект `ServerName`


Вклад в расчёт ID сервиса от обнаруженного имени сервера.


Доступны два взаимоисключающих варианта:


* Переопределить обнаруженное значение указанным статическим значением. Указать новое значение в поле **valueOverride**.
* Динамически преобразовать обнаруженное значение. Указать параметры преобразования в поле **transformations**.


| Element | Type | Description |
| --- | --- | --- |
| transformations | [TransformationBase](#openapi-definition-TransformationBase)[] | Преобразования, применяемые к обнаруженному значению. |
| valueOverride | string | Значение, используемое вместо обнаруженного значения. |


#### Объект `WebServiceName`


Вклад в расчёт ID сервиса от обнаруженного имени веб-сервиса.


Доступны два взаимоисключающих варианта:


* Переопределить обнаруженное значение указанным статическим значением. Указать новое значение в поле **valueOverride**.
* Динамически преобразовать обнаруженное значение. Указать параметры преобразования в поле **transformations**.


| Element | Type | Description |
| --- | --- | --- |
| transformations | [TransformationBase](#openapi-definition-TransformationBase)[] | Преобразования, применяемые к обнаруженному значению. |
| valueOverride | string | Значение, используемое вместо обнаруженного значения. |


#### Объект `WebServiceNameSpace`


Вклад в расчёт ID сервиса от обнаруженного пространства имён веб-сервиса.


Доступны два взаимоисключающих варианта:


* Переопределить обнаруженное значение указанным статическим значением. Указать новое значение в поле **valueOverride**.
* Динамически преобразовать обнаруженное значение. Указать параметры преобразования в поле **transformations**.


| Element | Type | Description |
| --- | --- | --- |
| transformations | [TransformationBase](#openapi-definition-TransformationBase)[] | Преобразования, применяемые к обнаруженному значению. |
| valueOverride | string | Значение, используемое вместо обнаруженного значения. |


Это модель тела запроса, показывающая возможные элементы. Её нужно скорректировать для использования в реальном запросе.


```
{



"type": "FULL_WEB_SERVICE",



"id": "string",



"order": "1",



"name": "string",



"description": "string",



"enabled": true,



"conditions": [



{



"attributeType": "URL_PATH",



"compareOperations": [



{



"type": "STRING_CONTAINS",



"negate": false,



"ignoreCase": true,



"values": [



"string"



]



}



]



}



],



"detectWebRequestOnly": false,



"webServiceName" : {



"valueOverride": "string",



"transformations": []



},



"webServiceNameSpace": {



"valueOverride": "string",



"transformations": []



},



"applicationId": {



"transformations": [],



"valueOverride": "string"



},



"contextRoot": {



"transformations": [



{



"type": "AFTER",



"delimiter": "string"



}



],



"segmentsToCopyFromUrlPath": 2



},



"serverName": {



"transformations": [



{



"type": "BEFORE",



"delimiter": "string"



}



]



}



}
```

## Варианты объекта `CompareOperation`

Объект `CompareOperation` является базовым для всех операций сравнения. Фактический набор полей зависит от **type** сравнения.

### STRING_CONTAINS

StringContainsCompareOperation

Параметры

JSON model

#### Объект `StringContainsCompareOperation`

Условие типа `STRING_CONTAINS`.

Условие проверяет, содержит ли строковое значение указанный текст.

| Элемент | Тип | Описание |
| --- | --- | --- |
| ignoreCase | boolean | Условие чувствительно к регистру (`false`) или нечувствительно к регистру (`true`).  Если не задано, используется `false`, то есть условие чувствительно к регистру. |
| negate | boolean | Инвертирует действие условия. Установить `true`, чтобы превратить **contains** в **does not contain**.  Если не задано, используется `false`. |
| values | string[] | Значение для сравнения.  Если указано несколько значений, применяется логика ИЛИ. |

```
{



"type": "STRING_CONTAINS",



"negate": false,



"ignoreCase": true,



"values": [



"compareValue1",



"compareValue2"



]



}
```

### STRING_EQUALS

StringEqualsCompareOperation

Параметры

JSON model

#### Объект `StringEqualsCompareOperation`

Условие типа `STRING_EQUALS`.

Условие проверяет, равно ли строковое значение указанному тексту.

| Элемент | Тип | Описание |
| --- | --- | --- |
| ignoreCase | boolean | Условие чувствительно к регистру (`false`) или нечувствительно к регистру (`true`).  Если не задано, используется `false`, то есть условие чувствительно к регистру. |
| negate | boolean | Инвертирует действие условия. Установить `true`, чтобы превратить **equals** в **does not equal**.  Если не задано, используется `false`. |
| values | string[] | Значение для сравнения.  Если указано несколько значений, применяется логика ИЛИ. |

```
{



"type": "STRING_EQUALS",



"negate": false,



"ignoreCase": true,



"values": [



"compareValue1",



"compareValue2"



]



}
```

### STARTS_WITH

StartsWithCompareOperation

Параметры

JSON model

#### Объект `StartsWithCompareOperation`

Условие типа `STARTS_WITH`.

Условие проверяет, начинается ли строковое значение с указанного текста.

| Элемент | Тип | Описание |
| --- | --- | --- |
| ignoreCase | boolean | Условие чувствительно к регистру (`false`) или нечувствительно к регистру (`true`).  Если не задано, используется `false`, то есть условие чувствительно к регистру. |
| negate | boolean | Инвертирует действие условия. Установить `true`, чтобы превратить **starts with** в **does not start with**.  Если не задано, используется `false`. |
| values | string[] | Значение для сравнения.  Если указано несколько значений, применяется логика ИЛИ. |

```
{



"type": "STARTS_WITH",



"negate": false,



"ignoreCase": true,



"values": [



"compareValue1",



"compareValue2"



]



}
```

### ENDS_WITH

EndsWithCompareOperation

Параметры

JSON model

#### Объект `EndsWithCompareOperation`

Условие типа `ENDS_WITH`.

Условие проверяет, заканчивается ли строковое значение указанным текстом.

| Элемент | Тип | Описание |
| --- | --- | --- |
| ignoreCase | boolean | Условие чувствительно к регистру (`false`) или нечувствительно к регистру (`true`).  Если не задано, используется `false`, то есть условие чувствительно к регистру. |
| negate | boolean | Инвертирует действие условия. Установить `true`, чтобы превратить **ends with** в **does not end with**.  Если не задано, используется `false`. |
| values | string[] | Значение для сравнения.  Если указано несколько значений, применяется логика ИЛИ. |

```
{



"type": "ENDS_WITH",



"negate": false,



"ignoreCase": true,



"values": [



"compareValue1",



"compareValue2"



]



}
```

### EXISTS

ExistsCompareOperation

Параметры

JSON model

#### Объект `ExistsCompareOperation`

Условие типа `EXISTS`.

Условие проверяет, существует ли указанный атрибут.

| Элемент | Тип | Описание |
| --- | --- | --- |
| negate | boolean | Инвертирует действие условия. Установить `true`, чтобы превратить **exists** в **does not exist**.  Если не задано, используется `false`. |

```
{



"type": "EXISTS",



"negate": false



}
```

### IP_IN_RANGE

IpInRangeCompareOperation

Параметры

JSON model

#### Объект `IpInRangeCompareOperation`

Условие типа `IP_IN_RANGE`.

Условие проверяет, принадлежит ли IP-адрес указанному диапазону.

| Элемент | Тип | Описание |
| --- | --- | --- |
| lower | string | Нижняя граница диапазона IP-адресов. |
| negate | boolean | Инвертирует действие условия. Установить `true`, чтобы превратить **IP is in range** в **IP is not in range**.  Если не задано, используется `false`. |
| upper | string | Верхняя граница диапазона IP-адресов. |

```
{



"type": "IP_IN_RANGE",



"negate": false,



"lower": "192.168.0.1",



"upper": "192.168.0.10"



}
```

### INT_EQUALS

IntEqualsCompareOperation

Параметры

JSON model

#### Объект `IntEqualsCompareOperation`

Условие типа `INT_EQUALS`.

Условие проверяет, равно ли целочисленное значение указанному значению.

| Элемент | Тип | Описание |
| --- | --- | --- |
| negate | boolean | Инвертирует действие условия. Установить `true`, чтобы превратить **equals** в **does not equal**.  Если не задано, используется `false`. |
| values | integer[] | Значение для сравнения.  Если указано несколько значений, применяется логика ИЛИ. |

```
{



"type": "INT_EQUALS",



"negate": false,



"values": [



128,



258,



512



]



}
```

### LESS_THAN

LessThanCompareOperation

Параметры

JSON model

#### Объект `LessThanCompareOperation`

Условие типа `LESS_THAN`.

Условие проверяет, меньше ли целочисленное значение указанного значения.

| Элемент | Тип | Описание |
| --- | --- | --- |
| value | integer | Значение для сравнения. |

```
{



"type": "LESS_THAN",



"value": 512



}
```

### GREATER_THAN

GreaterThanCompareOperation

Параметры

JSON model

#### Объект `GreaterThanCompareOperation`

Условие типа `GREATER_THAN`.

Условие проверяет, больше ли целочисленное значение указанного значения.

| Элемент | Тип | Описание |
| --- | --- | --- |
| value | integer | Значение для сравнения. |

```
{



"type": "GREATER_THAN",



"value": 256



}
```

## Варианты объекта `TransformationBase`

Объект `TransformationBase` является базовым для всех операций преобразования. Фактический набор полей зависит от **type** преобразования.

### BEFORE

BeforeTransformation

Параметры

JSON model

#### Объект `BeforeTransformation`

Преобразование типа `BEFORE`.

Преобразование сохраняет значение до указанного разделителя и удаляет всё после него.

| Элемент | Тип | Описание |
| --- | --- | --- |
| delimiter | string | Разделитель преобразования. Преобразование сохраняет всё до этого разделителя и удаляет всё после него.  Сам разделитель не сохраняется.  Если в исходном значении встречается несколько разделителей, используется только первый. |

```
{



"type": "BEFORE",



"delimiter": "/"



}
```

### AFTER

AfterTransformation

Параметры

JSON model

#### Объект `AfterTransformation`

Преобразование типа `AFTER`. Преобразование удаляет всё до указанного разделителя и сохраняет значение после него.

| Элемент | Тип | Описание |
| --- | --- | --- |
| delimiter | string | Разделитель преобразования. Преобразование удаляет всё до этого разделителя и сохраняет всё после него.  Сам разделитель не сохраняется.  Если в исходном значении встречается несколько разделителей, используется только первый. |

```
{



"type": "AFTER",



"delimiter": "/"



}
```

### BETWEEN

BetweenTransformation

Параметры

JSON model

#### Объект `BetweenTransformation`

Преобразование типа `BETWEEN`. Преобразование сохраняет значение между указанными разделителями и удаляет всё, что находится вне их.

| Элемент | Тип | Описание |
| --- | --- | --- |
| after | string | Начальный разделитель. Преобразование удаляет всё до него. Сам разделитель не сохраняется. |
| before | string | Конечный разделитель. Преобразование удаляет всё после него. Сам разделитель не сохраняется. |

```
{



"type": "BETWEEN",



"after": "support",



"before": "/"



}
```

### REPLACE_BETWEEN

ReplaceBetweenTransformation

Параметры

JSON model

#### Объект `ReplaceBetweenTransformation`

Преобразование типа `REPLACE_BETWEEN`.

Преобразование заменяет содержимое между указанными разделителями на указанное значение. Остальная часть строки остаётся без изменений.

| Элемент | Тип | Описание |
| --- | --- | --- |
| after | string | Начальный разделитель. Преобразование заменяет всё от этого места до конечного разделителя. Сам разделитель остаётся без изменений. |
| before | string | Конечный разделитель. Преобразование заменяет всё от начального разделителя до этого места. Сам разделитель остаётся без изменений. |
| replacement | string | Значение, которое используется вместо содержимого между разделителями. |

```
{



"type": "REPLACE_BETWEEN",



"after": "support",



"before": "/",



"replacement": "newValue"



}
```

### REMOVE_NUMBERS

RemoveNumbersTransformation

Параметры

JSON model

#### Объект `RemoveNumbersTransformation`

Преобразование типа `REMOVE_NUMBERS`.

Преобразование удаляет любые числа из обнаруженного значения.

| Элемент | Тип | Описание |
| --- | --- | --- |
| includeHexNumbers | boolean | Удалять (`true`) или сохранять (`false`) шестнадцатеричные числа.  Если не задано, используется `false`, то есть шестнадцатеричные числа сохраняются. |
| minDigitCount | integer | Удалять числа, содержащие не менее *X* цифр. |

```
{



"type": "REMOVE_NUMBERS",



"minDigitCount": 2,



"includeHexNumbers": true



}
```

### REMOVE_CREDIT_CARDS

RemoveCreditCardNumbersTransformation

Параметры

JSON model

#### Объект `RemoveCreditCardNumbersTransformation`

Трансформация типа `REMOVE_CREDIT_CARDS`.

Трансформация автоматически обнаруживает и удаляет номера кредитных карт. Дополнительные параметры не нужны.

| Элемент | Тип | Описание |
| --- | --- | --- |
| type | string | Определяет фактический набор полей в зависимости от значения. См. один из следующих объектов:  * `BEFORE` -> BeforeTransformation * `AFTER` -> AfterTransformation * `BETWEEN` -> BetweenTransformation * `REPLACE_BETWEEN` -> ReplaceBetweenTransformation * `REMOVE_NUMBERS` -> RemoveNumbersTransformation * `REMOVE_CREDIT_CARDS` -> RemoveCreditCardNumbersTransformation * `REMOVE_IBANS` -> RemoveIBANsTransformation * `REMOVE_IPS` -> RemoveIPsTransformation * `SPLIT_SELECT` -> SplitSelectTransformation * `TAKE_SEGMENTS` -> TakeSegmentsTransformation Элемент может принимать следующие значения * `AFTER` * `BEFORE` * `BETWEEN` * `REMOVE_CREDIT_CARDS` * `REMOVE_IBANS` * `REMOVE_IPS` * `REMOVE_NUMBERS` * `REPLACE_BETWEEN` * `SPLIT_SELECT` * `TAKE_SEGMENTS` |

```
{



"type": "REMOVE_CREDIT_CARDS"



}
```

### REMOVE_IBANS

RemoveIBANsTransformation

Параметры

JSON model

#### Объект `RemoveIBANsTransformation`

Трансформация типа `REMOVE_IBANS`.

Трансформация автоматически обнаруживает и удаляет международные номера банковских счетов (IBAN). Дополнительные параметры не нужны.

| Элемент | Тип | Описание |
| --- | --- | --- |
| type | string | Определяет фактический набор полей в зависимости от значения. См. один из следующих объектов:  * `BEFORE` -> BeforeTransformation * `AFTER` -> AfterTransformation * `BETWEEN` -> BetweenTransformation * `REPLACE_BETWEEN` -> ReplaceBetweenTransformation * `REMOVE_NUMBERS` -> RemoveNumbersTransformation * `REMOVE_CREDIT_CARDS` -> RemoveCreditCardNumbersTransformation * `REMOVE_IBANS` -> RemoveIBANsTransformation * `REMOVE_IPS` -> RemoveIPsTransformation * `SPLIT_SELECT` -> SplitSelectTransformation * `TAKE_SEGMENTS` -> TakeSegmentsTransformation Элемент может принимать следующие значения * `AFTER` * `BEFORE` * `BETWEEN` * `REMOVE_CREDIT_CARDS` * `REMOVE_IBANS` * `REMOVE_IPS` * `REMOVE_NUMBERS` * `REPLACE_BETWEEN` * `SPLIT_SELECT` * `TAKE_SEGMENTS` |

```
{



"type": "REMOVE_IBANS"



}
```

### REMOVE_IPS

RemoveIPsTransformation

Параметры

JSON model

#### Объект `RemoveIPsTransformation`

Трансформация типа `REMOVE_IPS`.

Трансформация автоматически обнаруживает и удаляет IP-адреса. Дополнительные параметры не нужны.

| Элемент | Тип | Описание |
| --- | --- | --- |
| type | string | Определяет фактический набор полей в зависимости от значения. См. один из следующих объектов:  * `BEFORE` -> BeforeTransformation * `AFTER` -> AfterTransformation * `BETWEEN` -> BetweenTransformation * `REPLACE_BETWEEN` -> ReplaceBetweenTransformation * `REMOVE_NUMBERS` -> RemoveNumbersTransformation * `REMOVE_CREDIT_CARDS` -> RemoveCreditCardNumbersTransformation * `REMOVE_IBANS` -> RemoveIBANsTransformation * `REMOVE_IPS` -> RemoveIPsTransformation * `SPLIT_SELECT` -> SplitSelectTransformation * `TAKE_SEGMENTS` -> TakeSegmentsTransformation Элемент может принимать следующие значения * `AFTER` * `BEFORE` * `BETWEEN` * `REMOVE_CREDIT_CARDS` * `REMOVE_IBANS` * `REMOVE_IPS` * `REMOVE_NUMBERS` * `REPLACE_BETWEEN` * `SPLIT_SELECT` * `TAKE_SEGMENTS` |

```
{



"type": "REMOVE_IPS"



}
```

### SPLIT_SELECT

SplitSelectTransformation

Параметры

JSON model

#### Объект `SplitSelectTransformation`

Трансформация типа `SPLIT_SELECT`.

Трансформация разбивает обнаруженное значение на массив и сохраняет указанный элемент массива.

| Элемент | Тип | Описание |
| --- | --- | --- |
| delimiter | string | Разделитель для разбиения обнаруженного значения. Сам разделитель не сохраняется. |
| itemIndex | integer | Индекс элемента в массиве после разбиения, который нужно использовать. Индексация начинается с `1`. |

```
{



"type": "SPLIT_SELECT",



"delimiter": "/",



"itemIndex": 2



}
```

### TAKE_SEGMENTS

TakeSegmentsTransformation

Параметры

JSON model

#### Объект `TakeSegmentsTransformation`

Трансформация типа `TAKE_SEGMENTS`.

Трансформация разбивает обнаруженное значение на массив и сохраняет указанное количество первых или последних элементов.

| Элемент | Тип | Описание |
| --- | --- | --- |
| delimiter | string | Разделитель для разбиения обнаруженного значения. Сам разделитель не сохраняется. |
| segmentCount | integer | Количество элементов, которые нужно сохранить. |
| takeFromEnd | boolean | Сохраняет первые (`false`) или последние (`true`) элементы.  Если не задано, используется `false`, то есть сохраняются первые элементы. |

```
{



"type": "TAKE_SEGMENTS",



"delimiter": "/",



"takeFromEnd": false



}
```