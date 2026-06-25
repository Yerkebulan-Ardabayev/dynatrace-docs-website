---
title: Service detection API - JSON models
source: https://docs.dynatrace.com/managed/dynatrace-api/configuration-api/service-api/detection-rules/models
scraped: 2026-05-12T12:02:42.818699
---

# Service detection API - JSON models

# Service detection API - JSON models

* Reference
* Published Aug 06, 2019

JSON-модели API **Service detection rules** сильно различаются в зависимости от поля **type** некоторых объектов. JSON-модели для каждой вариации перечислены ниже.

## Вариации объекта `ServiceDetectionRule`

Объект `ServiceDetectionRule` является базовым для всех правил обнаружения сервисов. Фактический набор полей зависит от поля **type** правила.

#### FULL\_WEB\_REQUEST

FullWebRequestRule

Parameters

JSON model

#### Объект `FullWebRequestRule`

Правило обнаружения сервисов типа `FULL_WEB_REQUEST`.

| Элемент | Тип | Описание |
| --- | --- | --- |
| applicationId | [ApplicationId](#openapi-definition-ApplicationId) | Вклад в расчёт ID сервиса от обнаруженного ID приложения.  Есть два взаимоисключающих варианта:  * Переопределить обнаруженное значение заданным статическим значением. Укажите новое значение в поле **valueOverride**. * Динамически преобразовать обнаруженное значение. Укажите параметры преобразования в поле **transformations**. |
| conditions | [ConditionsFullWebRequestAttributeTypeDto[]](#openapi-definition-ConditionsFullWebRequestAttributeTypeDto) | Список условий правила.  Если указано несколько условий, применяется логика AND. |
| contextRoot | [ContextRoot](#openapi-definition-ContextRoot) | Вклад в расчёт ID сервиса от обнаруженного context root.  Context root это первый сегмент URL запроса после имени сервера. Например, в URL `www.dynatrace.com/support/help/dynatrace-api/` context root равен `support`.  Есть два варианта:  * Сохранить часть обнаруженного URL. Укажите количество сохраняемых сегментов в поле **segmentsToCopyFromUrlPath**. * Динамически преобразовать обнаруженный URL. Укажите параметры преобразования в поле **transformations**.  Можно использовать один или оба варианта. Если используются оба, преобразование применяется к изменённому URL. |
| description | string | Краткое описание правила. |
| enabled | boolean | Правило включено (`true`) или отключено (`false`). |
| id | string | ID правила обнаружения сервисов. |
| managementZones | string[] | Зона управления (указанная по ID) группы процессов, для которой должно быть создано это правило обнаружения сервисов.  Здесь можно указать только 1 зону управления. |
| metadata | [ConfigurationMetadata](#openapi-definition-ConfigurationMetadata) | Метаданные для отладки |
| name | string | Имя правила. |
| order | string | Порядок правила в списке правил.  Правила выполняются сверху вниз. Применяется первое совпавшее правило. |
| serverName | [ServerName](#openapi-definition-ServerName) | Вклад в расчёт ID сервиса от обнаруженного имени сервера.  Есть два взаимоисключающих варианта:  * Переопределить обнаруженное значение заданным статическим значением. Укажите новое значение в поле **valueOverride**. * Динамически преобразовать обнаруженное значение. Укажите параметры преобразования в поле **transformations**. |
| type | string | Тип правила обнаружения сервисов. |

#### Объект `ApplicationId`

Вклад в расчёт ID сервиса от обнаруженного ID приложения.

Есть два взаимоисключающих варианта:

* Переопределить обнаруженное значение заданным статическим значением. Укажите новое значение в поле **valueOverride**.
* Динамически преобразовать обнаруженное значение. Укажите параметры преобразования в поле **transformations**.

| Элемент | Тип | Описание |
| --- | --- | --- |
| transformations | [TransformationBase[]](#openapi-definition-TransformationBase) | Преобразования, применяемые к обнаруженному значению. |
| valueOverride | string | Значение, используемое вместо обнаруженного значения. |

#### Объект `TransformationBase`

Конфигурация преобразования обнаруженного значения.

Если указано несколько преобразований, они обрабатываются последовательно сверху вниз. Каждое преобразование применяется к результату предыдущего преобразования. Например, второе преобразование применяется к результату первого преобразования.

Фактический набор полей зависит от типа преобразования. Список фактических объектов см. в описании поля **type** или см. [Service detection API - JSON models](https://dt-url.net/2ie3slq).

| Элемент | Тип | Описание |
| --- | --- | --- |
| type | string | Определяет фактический набор полей в зависимости от значения. Смотрите один из следующих объектов:  * `BEFORE` -> BeforeTransformation * `AFTER` -> AfterTransformation * `BETWEEN` -> BetweenTransformation * `REPLACE_BETWEEN` -> ReplaceBetweenTransformation * `REMOVE_NUMBERS` -> RemoveNumbersTransformation * `REMOVE_CREDIT_CARDS` -> RemoveCreditCardNumbersTransformation * `REMOVE_IBANS` -> RemoveIBANsTransformation * `REMOVE_IPS` -> RemoveIPsTransformation * `SPLIT_SELECT` -> SplitSelectTransformation * `TAKE_SEGMENTS` -> TakeSegmentsTransformation Возможные значения: * `AFTER` * `BEFORE` * `BETWEEN` * `REMOVE_CREDIT_CARDS` * `REMOVE_IBANS` * `REMOVE_IPS` * `REMOVE_NUMBERS` * `REPLACE_BETWEEN` * `SPLIT_SELECT` * `TAKE_SEGMENTS` |

#### Объект `ConditionsFullWebRequestAttributeTypeDto`

Условие правила обнаружения сервисов.

| Элемент | Тип | Описание |
| --- | --- | --- |
| attributeType | string | Тип проверяемого атрибута. Возможные значения: * `APPLICATION_ID` * `CONTEXT_ROOT` * `PG_TAG` * `SERVER_NAME` * `URL_HOST_NAME` * `URL_PATH` |
| compareOperations | [CompareOperation[]](#openapi-definition-CompareOperation) | Список условий правила.  Если указано несколько условий, применяется логика AND. |

#### Объект `CompareOperation`

Условие правила.

Фактический набор полей зависит от типа условия. Список фактических объектов см. в описании поля **type** или см. [Service detection API - JSON models](https://dt-url.net/2ie3slq).

| Элемент | Тип | Описание |
| --- | --- | --- |
| type | string | Определяет фактический набор полей в зависимости от значения. Смотрите один из следующих объектов:  * `EQUALS` -> EqualsCompareOperation * `STRING_CONTAINS` -> StringContainsCompareOperation * `STARTS_WITH` -> StartsWithCompareOperation * `ENDS_WITH` -> EndsWithCompareOperation * `EXISTS` -> ExistsCompareOperation * `IP_IN_RANGE` -> IpInRangeCompareOperation * `LESS_THAN` -> LessThanCompareOperation * `GREATER_THAN` -> GreaterThanCompareOperation * `INT_EQUALS` -> IntEqualsCompareOperation * `STRING_EQUALS` -> StringEqualsCompareOperation * `TAG` -> TagCompareOperation Возможные значения: * `ENDS_WITH` * `EQUALS` * `EXISTS` * `GREATER_THAN` * `INT_EQUALS` * `IP_IN_RANGE` * `LESS_THAN` * `STARTS_WITH` * `STRING_CONTAINS` * `STRING_EQUALS` * `TAG` |

#### Объект `ContextRoot`

Вклад в расчёт ID сервиса от обнаруженного context root.

Context root это первый сегмент URL запроса после имени сервера. Например, в URL `www.dynatrace.com/support/help/dynatrace-api/` context root равен `support`.

Есть два варианта:

* Сохранить часть обнаруженного URL. Укажите количество сохраняемых сегментов в поле **segmentsToCopyFromUrlPath**.
* Динамически преобразовать обнаруженный URL. Укажите параметры преобразования в поле **transformations**.

Можно использовать один или оба варианта. Если используются оба, преобразование применяется к изменённому URL.

| Элемент | Тип | Описание |
| --- | --- | --- |
| segmentsToCopyFromUrlPath | integer | Количество сохраняемых сегментов URL.  URL делится слешами (`/`), индексация начинается с 1 в context root.  Например, если вы укажете `2` для URL `www.dynatrace.com/support/help/dynatrace-api/`, используется значение `support/help`. |
| transformations | [ContextRootTransformation[]](#openapi-definition-ContextRootTransformation) | Преобразования, применяемые к обнаруженному значению. |

#### Объект `ContextRootTransformation`

Конфигурация преобразования обнаруженного значения.

Если указано несколько преобразований, они обрабатываются последовательно сверху вниз. Каждое преобразование применяется к результату предыдущего преобразования. Например, второе преобразование применяется к результату первого преобразования.

Фактический набор полей зависит от поля `type` преобразования.

| Элемент | Тип | Описание |
| --- | --- | --- |
| type | string | Определяет фактический набор полей в зависимости от значения. Смотрите один из следующих объектов:  * `BEFORE` -> BeforeTransformation * `REPLACE_BETWEEN` -> ReplaceBetweenTransformation * `REMOVE_NUMBERS` -> RemoveNumbersTransformation * `REMOVE_CREDIT_CARDS` -> RemoveCreditCardNumbersTransformation * `REMOVE_IBANS` -> RemoveIBANsTransformation * `REMOVE_IPS` -> RemoveIPsTransformation Возможные значения: * `BEFORE` * `REMOVE_CREDIT_CARDS` * `REMOVE_IBANS` * `REMOVE_IPS` * `REMOVE_NUMBERS` * `REPLACE_BETWEEN` |

#### Объект `ConfigurationMetadata`

Метаданные для отладки

| Элемент | Тип | Описание |
| --- | --- | --- |
| clusterVersion | string | Версия Dynatrace. |
| configurationVersions | integer[] | Отсортированный список номеров версий конфигурации. |
| currentConfigurationVersions | string[] | Отсортированный список номеров версий конфигурации. |

#### Объект `ServerName`

Вклад в расчёт ID сервиса от обнаруженного имени сервера.

Есть два взаимоисключающих варианта:

* Переопределить обнаруженное значение заданным статическим значением. Укажите новое значение в поле **valueOverride**.
* Динамически преобразовать обнаруженное значение. Укажите параметры преобразования в поле **transformations**.

| Элемент | Тип | Описание |
| --- | --- | --- |
| transformations | [TransformationBase[]](#openapi-definition-TransformationBase) | Преобразования, применяемые к обнаруженному значению. |
| valueOverride | string | Значение, используемое вместо обнаруженного значения. |

Это модель тела запроса, показывающая возможные элементы. Её нужно адаптировать под реальный запрос.

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

Parameters

JSON model

#### Объект `OpaqueAndExternalWebRequestRule`

Правило обнаружения сервисов типа `OPAQUE_AND_EXTERNAL_WEB_REQUEST`.

| Элемент | Тип | Описание |
| --- | --- | --- |
| applicationId | [ApplicationId](#openapi-definition-ApplicationId) | Вклад в расчёт ID сервиса от обнаруженного ID приложения.  Есть два взаимоисключающих варианта:  * Переопределить обнаруженное значение заданным статическим значением. Укажите новое значение в поле **valueOverride**. * Динамически преобразовать обнаруженное значение. Укажите параметры преобразования в поле **transformations**. |
| conditions | [ConditionsOpaqueAndExternalWebRequestAttributeTypeDto[]](#openapi-definition-ConditionsOpaqueAndExternalWebRequestAttributeTypeDto) | Список условий правила.  Если указано несколько условий, применяется логика AND. |
| contextRoot | [ContextRoot](#openapi-definition-ContextRoot) | Вклад в расчёт ID сервиса от обнаруженного context root.  Context root это первый сегмент URL запроса после имени сервера. Например, в URL `www.dynatrace.com/support/help/dynatrace-api/` context root равен `support`.  Есть два варианта:  * Сохранить часть обнаруженного URL. Укажите количество сохраняемых сегментов в поле **segmentsToCopyFromUrlPath**. * Динамически преобразовать обнаруженный URL. Укажите параметры преобразования в поле **transformations**.  Можно использовать один или оба варианта. Если используются оба, преобразование применяется к изменённому URL. |
| description | string | Краткое описание правила. |
| enabled | boolean | Правило включено (`true`) или отключено (`false`). |
| id | string | ID правила обнаружения сервисов. |
| managementZones | string[] | Зона управления (указанная по ID) группы процессов, для которой должно быть создано это правило обнаружения сервисов.  Здесь можно указать только 1 зону управления. |
| metadata | [ConfigurationMetadata](#openapi-definition-ConfigurationMetadata) | Метаданные для отладки |
| name | string | Имя правила. |
| order | string | Порядок правила в списке правил.  Правила выполняются сверху вниз. Применяется первое совпавшее правило. |
| port | [Port](#openapi-definition-Port) | Вклад в расчёт ID сервиса от порта, на котором обнаружен веб-запрос. |
| publicDomainName | [PublicDomainName](#openapi-definition-PublicDomainName) | Вклад в расчёт ID сервиса от доменного имени, на котором обнаружен веб-запрос.  Есть два взаимоисключающих варианта:  * Переопределить обнаруженное значение заданным статическим значением. Укажите новое значение в поле **valueOverride**. * Динамически преобразовать обнаруженное значение. Укажите параметры преобразования в поле **transformations**. |
| type | string | Тип правила обнаружения сервисов. |

#### Объект `ApplicationId`

Вклад в расчёт ID сервиса от обнаруженного ID приложения.

Есть два взаимоисключающих варианта:

* Переопределить обнаруженное значение заданным статическим значением. Укажите новое значение в поле **valueOverride**.
* Динамически преобразовать обнаруженное значение. Укажите параметры преобразования в поле **transformations**.

| Элемент | Тип | Описание |
| --- | --- | --- |
| transformations | [TransformationBase[]](#openapi-definition-TransformationBase) | Преобразования, применяемые к обнаруженному значению. |
| valueOverride | string | Значение, используемое вместо обнаруженного значения. |

#### Объект `TransformationBase`

Конфигурация преобразования обнаруженного значения.

Если указано несколько преобразований, они обрабатываются последовательно сверху вниз. Каждое преобразование применяется к результату предыдущего преобразования. Например, второе преобразование применяется к результату первого преобразования.

Фактический набор полей зависит от типа преобразования. Список фактических объектов см. в описании поля **type** или см. [Service detection API - JSON models](https://dt-url.net/2ie3slq).

| Элемент | Тип | Описание |
| --- | --- | --- |
| type | string | Определяет фактический набор полей в зависимости от значения. Смотрите один из следующих объектов:  * `BEFORE` -> BeforeTransformation * `AFTER` -> AfterTransformation * `BETWEEN` -> BetweenTransformation * `REPLACE_BETWEEN` -> ReplaceBetweenTransformation * `REMOVE_NUMBERS` -> RemoveNumbersTransformation * `REMOVE_CREDIT_CARDS` -> RemoveCreditCardNumbersTransformation * `REMOVE_IBANS` -> RemoveIBANsTransformation * `REMOVE_IPS` -> RemoveIPsTransformation * `SPLIT_SELECT` -> SplitSelectTransformation * `TAKE_SEGMENTS` -> TakeSegmentsTransformation Возможные значения: * `AFTER` * `BEFORE` * `BETWEEN` * `REMOVE_CREDIT_CARDS` * `REMOVE_IBANS` * `REMOVE_IPS` * `REMOVE_NUMBERS` * `REPLACE_BETWEEN` * `SPLIT_SELECT` * `TAKE_SEGMENTS` |

#### Объект `ConditionsOpaqueAndExternalWebRequestAttributeTypeDto`

Условие правила обнаружения сервисов.

| Элемент | Тип | Описание |
| --- | --- | --- |
| attributeType | string | Тип проверяемого атрибута. Возможные значения: * `IP` * `PG_TAG` * `TOP_LEVEL_DOMAIN` * `URL` * `URL_HOST_NAME` * `URL_PATH` * `URL_PORT` |
| compareOperations | [CompareOperation[]](#openapi-definition-CompareOperation) | Список условий правила.  Если указано несколько условий, применяется логика AND. |

#### Объект `CompareOperation`

Условие правила.

Фактический набор полей зависит от типа условия. Список фактических объектов см. в описании поля **type** или см. [Service detection API - JSON models](https://dt-url.net/2ie3slq).

| Элемент | Тип | Описание |
| --- | --- | --- |
| type | string | Определяет фактический набор полей в зависимости от значения. Смотрите один из следующих объектов:  * `EQUALS` -> EqualsCompareOperation * `STRING_CONTAINS` -> StringContainsCompareOperation * `STARTS_WITH` -> StartsWithCompareOperation * `ENDS_WITH` -> EndsWithCompareOperation * `EXISTS` -> ExistsCompareOperation * `IP_IN_RANGE` -> IpInRangeCompareOperation * `LESS_THAN` -> LessThanCompareOperation * `GREATER_THAN` -> GreaterThanCompareOperation * `INT_EQUALS` -> IntEqualsCompareOperation * `STRING_EQUALS` -> StringEqualsCompareOperation * `TAG` -> TagCompareOperation Возможные значения: * `ENDS_WITH` * `EQUALS` * `EXISTS` * `GREATER_THAN` * `INT_EQUALS` * `IP_IN_RANGE` * `LESS_THAN` * `STARTS_WITH` * `STRING_CONTAINS` * `STRING_EQUALS` * `TAG` |

#### Объект `ContextRoot`

Вклад в расчёт ID сервиса от обнаруженного context root.

Context root это первый сегмент URL запроса после имени сервера. Например, в URL `www.dynatrace.com/support/help/dynatrace-api/` context root равен `support`.

Есть два варианта:

* Сохранить часть обнаруженного URL. Укажите количество сохраняемых сегментов в поле **segmentsToCopyFromUrlPath**.
* Динамически преобразовать обнаруженный URL. Укажите параметры преобразования в поле **transformations**.

Можно использовать один или оба варианта. Если используются оба, преобразование применяется к изменённому URL.

| Элемент | Тип | Описание |
| --- | --- | --- |
| segmentsToCopyFromUrlPath | integer | Количество сохраняемых сегментов URL.  URL делится слешами (`/`), индексация начинается с 1 в context root.  Например, если вы укажете `2` для URL `www.dynatrace.com/support/help/dynatrace-api/`, используется значение `support/help`. |
| transformations | [ContextRootTransformation[]](#openapi-definition-ContextRootTransformation) | Преобразования, применяемые к обнаруженному значению. |

#### Объект `ContextRootTransformation`

Конфигурация преобразования обнаруженного значения.

Если указано несколько преобразований, они обрабатываются последовательно сверху вниз. Каждое преобразование применяется к результату предыдущего преобразования. Например, второе преобразование применяется к результату первого преобразования.

Фактический набор полей зависит от поля `type` преобразования.

| Элемент | Тип | Описание |
| --- | --- | --- |
| type | string | Определяет фактический набор полей в зависимости от значения. Смотрите один из следующих объектов:  * `BEFORE` -> BeforeTransformation * `REPLACE_BETWEEN` -> ReplaceBetweenTransformation * `REMOVE_NUMBERS` -> RemoveNumbersTransformation * `REMOVE_CREDIT_CARDS` -> RemoveCreditCardNumbersTransformation * `REMOVE_IBANS` -> RemoveIBANsTransformation * `REMOVE_IPS` -> RemoveIPsTransformation Возможные значения: * `BEFORE` * `REMOVE_CREDIT_CARDS` * `REMOVE_IBANS` * `REMOVE_IPS` * `REMOVE_NUMBERS` * `REPLACE_BETWEEN` |

#### Объект `ConfigurationMetadata`

Метаданные для отладки

| Элемент | Тип | Описание |
| --- | --- | --- |
| clusterVersion | string | Версия Dynatrace. |
| configurationVersions | integer[] | Отсортированный список номеров версий конфигурации. |
| currentConfigurationVersions | string[] | Отсортированный список номеров версий конфигурации. |

#### Объект `Port`

Вклад в расчёт ID сервиса от порта, на котором обнаружен веб-запрос.

| Элемент | Тип | Описание |
| --- | --- | --- |
| doNotUseForServiceId | boolean | Порт используется (`false`) или не используется (`true`) в расчёте ID сервиса. |

#### Объект `PublicDomainName`

Вклад в расчёт ID сервиса от доменного имени, на котором обнаружен веб-запрос.

Есть два взаимоисключающих варианта:

* Переопределить обнаруженное значение заданным статическим значением. Укажите новое значение в поле **valueOverride**.
* Динамически преобразовать обнаруженное значение. Укажите параметры преобразования в поле **transformations**.

| Элемент | Тип | Описание |
| --- | --- | --- |
| copyFromHostName | boolean | Использовать (`true`) или не использовать (`false`) обнаруженное имя хоста как основу для преобразования.  Не применяется, если задано переопределение. |
| transformations | [TransformationBase[]](#openapi-definition-TransformationBase) | Преобразования, применяемые к обнаруженному значению. |
| valueOverride | string | Значение, используемое вместо обнаруженного значения. |

Это модель тела запроса, показывающая возможные элементы. Её нужно адаптировать под реальный запрос.

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

Parameters

JSON model

#### Объект `FullWebServiceRule`

Правило обнаружения сервисов типа `FULL_WEB_SERVICE`.

Если у вас есть условие с **attributeType**, установленным в `FRAMEWORK`, поле **values** из **compareOperations** ограничено следующими возможными значениями:

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
| applicationId | [ApplicationId](#openapi-definition-ApplicationId) | Вклад в расчёт ID сервиса от обнаруженного ID приложения.  Есть два взаимоисключающих варианта:  * Переопределить обнаруженное значение заданным статическим значением. Укажите новое значение в поле **valueOverride**. * Динамически преобразовать обнаруженное значение. Укажите параметры преобразования в поле **transformations**. |
| conditions | [ConditionsFullWebServiceAttributeTypeDto[]](#openapi-definition-ConditionsFullWebServiceAttributeTypeDto) | Список условий правила.  Если указано несколько условий, применяется логика AND. |
| contextRoot | [ContextRoot](#openapi-definition-ContextRoot) | Вклад в расчёт ID сервиса от обнаруженного context root.  Context root это первый сегмент URL запроса после имени сервера. Например, в URL `www.dynatrace.com/support/help/dynatrace-api/` context root равен `support`.  Есть два варианта:  * Сохранить часть обнаруженного URL. Укажите количество сохраняемых сегментов в поле **segmentsToCopyFromUrlPath**. * Динамически преобразовать обнаруженный URL. Укажите параметры преобразования в поле **transformations**.  Можно использовать один или оба варианта. Если используются оба, преобразование применяется к изменённому URL. |
| description | string | Краткое описание правила. |
| detectAsWebRequestService | boolean | Обнаруживать совпадающие запросы как полные веб-сервисы (`false`) или как сервисы веб-запросов (`true`).  Установка этого поля в `true` предотвращает обнаружение совпадающих запросов как полных веб-сервисов. Вместо этого создаётся сервис веб-запросов. Если нужно дополнительно изменить получившийся сервис веб-запросов, создайте отдельное правило типа `FULL_WEB_REQUEST`.  По умолчанию `false`, совпадающие запросы обнаруживаются как полные веб-сервисы. |
| enabled | boolean | Правило включено (`true`) или отключено (`false`). |
| id | string | ID правила обнаружения сервисов. |
| managementZones | string[] | Зона управления (указанная по ID) группы процессов, для которой должно быть создано это правило обнаружения сервисов.  Здесь можно указать только 1 зону управления. |
| metadata | [ConfigurationMetadata](#openapi-definition-ConfigurationMetadata) | Метаданные для отладки |
| name | string | Имя правила. |
| order | string | Порядок правила в списке правил.  Правила выполняются сверху вниз. Применяется первое совпавшее правило. |
| serverName | [ServerName](#openapi-definition-ServerName) | Вклад в расчёт ID сервиса от обнаруженного имени сервера.  Есть два взаимоисключающих варианта:  * Переопределить обнаруженное значение заданным статическим значением. Укажите новое значение в поле **valueOverride**. * Динамически преобразовать обнаруженное значение. Укажите параметры преобразования в поле **transformations**. |
| type | string | Тип правила обнаружения сервисов. |
| webServiceName | [WebServiceName](#openapi-definition-WebServiceName) | Вклад в расчёт ID сервиса от обнаруженного имени веб-сервиса.  Есть два взаимоисключающих варианта:  * Переопределить обнаруженное значение заданным статическим значением. Укажите новое значение в поле **valueOverride**. * Динамически преобразовать обнаруженное значение. Укажите параметры преобразования в поле **transformations**. |
| webServiceNameSpace | [WebServiceNameSpace](#openapi-definition-WebServiceNameSpace) | Вклад в расчёт ID сервиса от обнаруженного пространства имён веб-сервиса.  Есть два взаимоисключающих варианта:  * Переопределить обнаруженное значение заданным статическим значением. Укажите новое значение в поле **valueOverride**. * Динамически преобразовать обнаруженное значение. Укажите параметры преобразования в поле **transformations**. |

#### Объект `ApplicationId`

Вклад в расчёт ID сервиса от обнаруженного ID приложения.

Есть два взаимоисключающих варианта:

* Переопределить обнаруженное значение заданным статическим значением. Укажите новое значение в поле **valueOverride**.
* Динамически преобразовать обнаруженное значение. Укажите параметры преобразования в поле **transformations**.

| Элемент | Тип | Описание |
| --- | --- | --- |
| transformations | [TransformationBase[]](#openapi-definition-TransformationBase) | Преобразования, применяемые к обнаруженному значению. |
| valueOverride | string | Значение, используемое вместо обнаруженного значения. |

#### Объект `TransformationBase`

Конфигурация преобразования обнаруженного значения.

Если указано несколько преобразований, они обрабатываются последовательно сверху вниз. Каждое преобразование применяется к результату предыдущего преобразования. Например, второе преобразование применяется к результату первого преобразования.

Фактический набор полей зависит от типа преобразования. Список фактических объектов см. в описании поля **type** или см. [Service detection API - JSON models](https://dt-url.net/2ie3slq).

| Элемент | Тип | Описание |
| --- | --- | --- |
| type | string | Определяет фактический набор полей в зависимости от значения. Смотрите один из следующих объектов:  * `BEFORE` -> BeforeTransformation * `AFTER` -> AfterTransformation * `BETWEEN` -> BetweenTransformation * `REPLACE_BETWEEN` -> ReplaceBetweenTransformation * `REMOVE_NUMBERS` -> RemoveNumbersTransformation * `REMOVE_CREDIT_CARDS` -> RemoveCreditCardNumbersTransformation * `REMOVE_IBANS` -> RemoveIBANsTransformation * `REMOVE_IPS` -> RemoveIPsTransformation * `SPLIT_SELECT` -> SplitSelectTransformation * `TAKE_SEGMENTS` -> TakeSegmentsTransformation Возможные значения: * `AFTER` * `BEFORE` * `BETWEEN` * `REMOVE_CREDIT_CARDS` * `REMOVE_IBANS` * `REMOVE_IPS` * `REMOVE_NUMBERS` * `REPLACE_BETWEEN` * `SPLIT_SELECT` * `TAKE_SEGMENTS` |

#### Объект `ConditionsFullWebServiceAttributeTypeDto`

Условие правила обнаружения сервисов.

| Элемент | Тип | Описание |
| --- | --- | --- |
| attributeType | string | Тип проверяемого атрибута. Возможные значения: * `APPLICATION_ID` * `CONTEXT_ROOT` * `FRAMEWORK` * `IS_SOAP_SERVICE` * `PG_TAG` * `SERVER_NAME` * `URL_HOST_NAME` * `URL_PATH` * `WEBSERVICE_METHOD` * `WEBSERVICE_NAME` * `WEBSERVICE_NAMESPACE` |
| compareOperations | [CompareOperation[]](#openapi-definition-CompareOperation) | Список условий правила.  Если указано несколько условий, применяется логика AND. |

#### Объект `CompareOperation`

Условие правила.

Фактический набор полей зависит от типа условия. Список фактических объектов см. в описании поля **type** или см. [Service detection API - JSON models](https://dt-url.net/2ie3slq).

| Элемент | Тип | Описание |
| --- | --- | --- |
| type | string | Определяет фактический набор полей в зависимости от значения. Смотрите один из следующих объектов:  * `EQUALS` -> EqualsCompareOperation * `STRING_CONTAINS` -> StringContainsCompareOperation * `STARTS_WITH` -> StartsWithCompareOperation * `ENDS_WITH` -> EndsWithCompareOperation * `EXISTS` -> ExistsCompareOperation * `IP_IN_RANGE` -> IpInRangeCompareOperation * `LESS_THAN` -> LessThanCompareOperation * `GREATER_THAN` -> GreaterThanCompareOperation * `INT_EQUALS` -> IntEqualsCompareOperation * `STRING_EQUALS` -> StringEqualsCompareOperation * `TAG` -> TagCompareOperation Возможные значения: * `ENDS_WITH` * `EQUALS` * `EXISTS` * `GREATER_THAN` * `INT_EQUALS` * `IP_IN_RANGE` * `LESS_THAN` * `STARTS_WITH` * `STRING_CONTAINS` * `STRING_EQUALS` * `TAG` |

#### Объект `ContextRoot`

Вклад в расчёт ID сервиса от обнаруженного context root.

Context root это первый сегмент URL запроса после имени сервера. Например, в URL `www.dynatrace.com/support/help/dynatrace-api/` context root равен `support`.

Есть два варианта:

* Сохранить часть обнаруженного URL. Укажите количество сохраняемых сегментов в поле **segmentsToCopyFromUrlPath**.
* Динамически преобразовать обнаруженный URL. Укажите параметры преобразования в поле **transformations**.

Можно использовать один или оба варианта. Если используются оба, преобразование применяется к изменённому URL.

| Элемент | Тип | Описание |
| --- | --- | --- |
| segmentsToCopyFromUrlPath | integer | Количество сохраняемых сегментов URL.  URL делится слешами (`/`), индексация начинается с 1 в context root.  Например, если вы укажете `2` для URL `www.dynatrace.com/support/help/dynatrace-api/`, используется значение `support/help`. |
| transformations | [ContextRootTransformation[]](#openapi-definition-ContextRootTransformation) | Преобразования, применяемые к обнаруженному значению. |

#### Объект `ContextRootTransformation`

Конфигурация преобразования обнаруженного значения.

Если указано несколько преобразований, они обрабатываются последовательно сверху вниз. Каждое преобразование применяется к результату предыдущего преобразования. Например, второе преобразование применяется к результату первого преобразования.

Фактический набор полей зависит от поля `type` преобразования.

| Элемент | Тип | Описание |
| --- | --- | --- |
| type | string | Определяет фактический набор полей в зависимости от значения. Смотрите один из следующих объектов:  * `BEFORE` -> BeforeTransformation * `REPLACE_BETWEEN` -> ReplaceBetweenTransformation * `REMOVE_NUMBERS` -> RemoveNumbersTransformation * `REMOVE_CREDIT_CARDS` -> RemoveCreditCardNumbersTransformation * `REMOVE_IBANS` -> RemoveIBANsTransformation * `REMOVE_IPS` -> RemoveIPsTransformation Возможные значения: * `BEFORE` * `REMOVE_CREDIT_CARDS` * `REMOVE_IBANS` * `REMOVE_IPS` * `REMOVE_NUMBERS` * `REPLACE_BETWEEN` |

#### Объект `ConfigurationMetadata`

Метаданные для отладки

| Элемент | Тип | Описание |
| --- | --- | --- |
| clusterVersion | string | Версия Dynatrace. |
| configurationVersions | integer[] | Отсортированный список номеров версий конфигурации. |
| currentConfigurationVersions | string[] | Отсортированный список номеров версий конфигурации. |

#### Объект `ServerName`

Вклад в расчёт ID сервиса от обнаруженного имени сервера.

Есть два взаимоисключающих варианта:

* Переопределить обнаруженное значение заданным статическим значением. Укажите новое значение в поле **valueOverride**.
* Динамически преобразовать обнаруженное значение. Укажите параметры преобразования в поле **transformations**.

| Элемент | Тип | Описание |
| --- | --- | --- |
| transformations | [TransformationBase[]](#openapi-definition-TransformationBase) | Преобразования, применяемые к обнаруженному значению. |
| valueOverride | string | Значение, используемое вместо обнаруженного значения. |

#### Объект `WebServiceName`

Вклад в расчёт ID сервиса от обнаруженного имени веб-сервиса.

Есть два взаимоисключающих варианта:

* Переопределить обнаруженное значение заданным статическим значением. Укажите новое значение в поле **valueOverride**.
* Динамически преобразовать обнаруженное значение. Укажите параметры преобразования в поле **transformations**.

| Элемент | Тип | Описание |
| --- | --- | --- |
| transformations | [TransformationBase[]](#openapi-definition-TransformationBase) | Преобразования, применяемые к обнаруженному значению. |
| valueOverride | string | Значение, используемое вместо обнаруженного значения. |

#### Объект `WebServiceNameSpace`

Вклад в расчёт ID сервиса от обнаруженного пространства имён веб-сервиса.

Есть два взаимоисключающих варианта:

* Переопределить обнаруженное значение заданным статическим значением. Укажите новое значение в поле **valueOverride**.
* Динамически преобразовать обнаруженное значение. Укажите параметры преобразования в поле **transformations**.

| Элемент | Тип | Описание |
| --- | --- | --- |
| transformations | [TransformationBase[]](#openapi-definition-TransformationBase) | Преобразования, применяемые к обнаруженному значению. |
| valueOverride | string | Значение, используемое вместо обнаруженного значения. |

Это модель тела запроса, показывающая возможные элементы. Её нужно адаптировать под реальный запрос.

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

## Вариации объекта `CompareOperation`

Объект `CompareOperation` является базовым для всех операций сравнения. Фактический набор полей зависит от поля **type** сравнения.

### STRING\_CONTAINS

StringContainsCompareOperation

Parameters

JSON model

#### Объект `StringContainsCompareOperation`

Условие типа `STRING_CONTAINS`.

Условие проверяет, содержит ли строковое значение указанный текст.

| Элемент | Тип | Описание |
| --- | --- | --- |
| ignoreCase | boolean | Условие чувствительно к регистру (`false`) или нечувствительно (`true`).  Если не задано, используется `false`, делая условие чувствительным к регистру. |
| negate | boolean | Инвертирует операцию условия. Установите `true`, чтобы превратить **contains** в **does not contain**.  Если не задано, используется `false`. |
| values | string[] | Значение для сравнения.  Если указано несколько значений, применяется логика OR. |

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

### STRING\_EQUALS

StringEqualsCompareOperation

Parameters

JSON model

#### Объект `StringEqualsCompareOperation`

Условие типа `STRING_EQUALS`.

Условие проверяет, равно ли строковое значение указанному тексту.

| Элемент | Тип | Описание |
| --- | --- | --- |
| ignoreCase | boolean | Условие чувствительно к регистру (`false`) или нечувствительно (`true`).  Если не задано, используется `false`, делая условие чувствительным к регистру. |
| negate | boolean | Инвертирует операцию условия. Установите `true`, чтобы превратить **equals** в **does not equal**.  Если не задано, используется `false`. |
| values | string[] | Значение для сравнения.  Если указано несколько значений, применяется логика OR. |

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

### STARTS\_WITH

StartsWithCompareOperation

Parameters

JSON model

#### Объект `StartsWithCompareOperation`

Условие типа `STARTS_WITH`.

Условие проверяет, начинается ли строковое значение с указанного текста.

| Элемент | Тип | Описание |
| --- | --- | --- |
| ignoreCase | boolean | Условие чувствительно к регистру (`false`) или нечувствительно (`true`).  Если не задано, используется `false`, делая условие чувствительным к регистру. |
| negate | boolean | Инвертирует операцию условия. Установите `true`, чтобы превратить **starts with** в **does not start with**.  Если не задано, используется `false`. |
| values | string[] | Значение для сравнения.  Если указано несколько значений, применяется логика OR. |

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

### ENDS\_WITH

EndsWithCompareOperation

Parameters

JSON model

#### Объект `EndsWithCompareOperation`

Условие типа `ENDS_WITH`.

Условие проверяет, заканчивается ли строковое значение указанным текстом.

| Элемент | Тип | Описание |
| --- | --- | --- |
| ignoreCase | boolean | Условие чувствительно к регистру (`false`) или нечувствительно (`true`).  Если не задано, используется `false`, делая условие чувствительным к регистру. |
| negate | boolean | Инвертирует операцию условия. Установите `true`, чтобы превратить **ends with** в **does not end with**.  Если не задано, используется `false`. |
| values | string[] | Значение для сравнения.  Если указано несколько значений, применяется логика OR. |

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

Parameters

JSON model

#### Объект `ExistsCompareOperation`

Условие типа `EXISTS`.

Условие проверяет, существует ли указанный атрибут.

| Элемент | Тип | Описание |
| --- | --- | --- |
| negate | boolean | Инвертирует операцию условия. Установите `true`, чтобы превратить **exists** в **does not exist**.  Если не задано, используется `false`. |

```
{



"type": "EXISTS",



"negate": false



}
```

### IP\_IN\_RANGE

IpInRangeCompareOperation

Parameters

JSON model

#### Объект `IpInRangeCompareOperation`

Условие типа `IP_IN_RANGE`.

Условие проверяет, принадлежит ли IP-адрес указанному диапазону.

| Элемент | Тип | Описание |
| --- | --- | --- |
| lower | string | Нижняя граница диапазона IP. |
| negate | boolean | Инвертирует операцию условия. Установите `true`, чтобы превратить **IP is in range** в **IP is not in range**.  Если не задано, используется `false`. |
| upper | string | Верхняя граница диапазона IP. |

```
{



"type": "IP_IN_RANGE",



"negate": false,



"lower": "192.168.0.1",



"upper": "192.168.0.10"



}
```

### INT\_EQUALS

IntEqualsCompareOperation

Parameters

JSON model

#### Объект `IntEqualsCompareOperation`

Условие типа `INT_EQUALS`.

Условие проверяет, равно ли целочисленное значение указанному значению.

| Элемент | Тип | Описание |
| --- | --- | --- |
| negate | boolean | Инвертирует операцию условия. Установите `true`, чтобы превратить **equals** в **does not equal**.  Если не задано, используется `false`. |
| values | integer[] | Значение для сравнения.  Если указано несколько значений, применяется логика OR. |

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

### LESS\_THAN

LessThanCompareOperation

Parameters

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

### GREATER\_THAN

GreaterThanCompareOperation

Parameters

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

## Вариации объекта `TransformationBase`

Объект `TransformationBase` является базовым для всех операций преобразования. Фактический набор полей зависит от поля **type** преобразования.

### BEFORE

BeforeTransformation

Parameters

JSON model

#### Объект `BeforeTransformation`

Преобразование типа `BEFORE`.

Преобразование сохраняет значение до указанного разделителя и удаляет всё после него.

| Элемент | Тип | Описание |
| --- | --- | --- |
| delimiter | string | Разделитель преобразования. Преобразование сохраняет всё до этого разделителя и удаляет всё после него.  Сам разделитель не сохраняется.  Если в исходном значении несколько разделителей, используется только первый. |

```
{



"type": "BEFORE",



"delimiter": "/"



}
```

### AFTER

AfterTransformation

Parameters

JSON model

#### Объект `AfterTransformation`

Преобразование типа `AFTER`.Преобразование удаляет всё до указанного разделителя и сохраняет значение после него.

| Элемент | Тип | Описание |
| --- | --- | --- |
| delimiter | string | Разделитель преобразования. Преобразование удаляет всё до этого разделителя и сохраняет всё после него.  Сам разделитель не сохраняется.  Если в исходном значении несколько разделителей, используется только первый. |

```
{



"type": "AFTER",



"delimiter": "/"



}
```

### BETWEEN

BetweenTransformation

Parameters

JSON model

#### Объект `BetweenTransformation`

Преобразование типа `BETWEEN`.Преобразование сохраняет значение между указанными разделителями и удаляет всё за их пределами.

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

### REPLACE\_BETWEEN

ReplaceBetweenTransformation

Parameters

JSON model

#### Объект `ReplaceBetweenTransformation`

Преобразование типа `REPLACE_BETWEEN`.

Преобразование заменяет содержимое между указанными разделителями указанным значением. Остальная часть строки остаётся без изменений.

| Элемент | Тип | Описание |
| --- | --- | --- |
| after | string | Начальный разделитель. Преобразование заменяет всё отсюда до конечного разделителя. Сам разделитель остаётся без изменений. |
| before | string | Конечный разделитель. Преобразование заменяет всё от начального разделителя до этого места. Сам разделитель остаётся без изменений. |
| replacement | string | Значение, используемое вместо содержимого между разделителями. |

```
{



"type": "REPLACE_BETWEEN",



"after": "support",



"before": "/",



"replacement": "newValue"



}
```

### REMOVE\_NUMBERS

RemoveNumbersTransformation

Parameters

JSON model

#### Объект `RemoveNumbersTransformation`

Преобразование типа `REMOVE_NUMBERS`.

Преобразование удаляет любые числа из обнаруженного значения.

| Элемент | Тип | Описание |
| --- | --- | --- |
| includeHexNumbers | boolean | Удалять (`true`) или сохранять (`false`) шестнадцатеричные числа.  Если не задано, используется `false`, сохраняя шестнадцатеричные числа. |
| minDigitCount | integer | Удалять числа, содержащие не менее *X* цифр. |

```
{



"type": "REMOVE_NUMBERS",



"minDigitCount": 2,



"includeHexNumbers": true



}
```

### REMOVE\_CREDIT\_CARDS

RemoveCreditCardNumbersTransformation

Parameters

JSON model

#### Объект `RemoveCreditCardNumbersTransformation`

Преобразование типа `REMOVE_CREDIT_CARDS`.

Преобразование автоматически обнаруживает и удаляет номера кредитных карт. Дополнительные параметры не нужны.

| Элемент | Тип | Описание |
| --- | --- | --- |
| type | string | Определяет фактический набор полей в зависимости от значения. Смотрите один из следующих объектов:  * `BEFORE` -> BeforeTransformation * `AFTER` -> AfterTransformation * `BETWEEN` -> BetweenTransformation * `REPLACE_BETWEEN` -> ReplaceBetweenTransformation * `REMOVE_NUMBERS` -> RemoveNumbersTransformation * `REMOVE_CREDIT_CARDS` -> RemoveCreditCardNumbersTransformation * `REMOVE_IBANS` -> RemoveIBANsTransformation * `REMOVE_IPS` -> RemoveIPsTransformation * `SPLIT_SELECT` -> SplitSelectTransformation * `TAKE_SEGMENTS` -> TakeSegmentsTransformation Возможные значения: * `AFTER` * `BEFORE` * `BETWEEN` * `REMOVE_CREDIT_CARDS` * `REMOVE_IBANS` * `REMOVE_IPS` * `REMOVE_NUMBERS` * `REPLACE_BETWEEN` * `SPLIT_SELECT` * `TAKE_SEGMENTS` |

```
{



"type": "REMOVE_CREDIT_CARDS"



}
```

### REMOVE\_IBANS

RemoveIBANsTransformation

Parameters

JSON model

#### Объект `RemoveIBANsTransformation`

Преобразование типа `REMOVE_IBANS`.

Преобразование автоматически обнаруживает и удаляет международные номера банковских счетов (IBAN). Дополнительные параметры не нужны.

| Элемент | Тип | Описание |
| --- | --- | --- |
| type | string | Определяет фактический набор полей в зависимости от значения. Смотрите один из следующих объектов:  * `BEFORE` -> BeforeTransformation * `AFTER` -> AfterTransformation * `BETWEEN` -> BetweenTransformation * `REPLACE_BETWEEN` -> ReplaceBetweenTransformation * `REMOVE_NUMBERS` -> RemoveNumbersTransformation * `REMOVE_CREDIT_CARDS` -> RemoveCreditCardNumbersTransformation * `REMOVE_IBANS` -> RemoveIBANsTransformation * `REMOVE_IPS` -> RemoveIPsTransformation * `SPLIT_SELECT` -> SplitSelectTransformation * `TAKE_SEGMENTS` -> TakeSegmentsTransformation Возможные значения: * `AFTER` * `BEFORE` * `BETWEEN` * `REMOVE_CREDIT_CARDS` * `REMOVE_IBANS` * `REMOVE_IPS` * `REMOVE_NUMBERS` * `REPLACE_BETWEEN` * `SPLIT_SELECT` * `TAKE_SEGMENTS` |

```
{



"type": "REMOVE_IBANS"



}
```

### REMOVE\_IPS

RemoveIPsTransformation

Parameters

JSON model

#### Объект `RemoveIPsTransformation`

Преобразование типа `REMOVE_IPS`.

Преобразование автоматически обнаруживает и удаляет IP-адреса. Дополнительные параметры не нужны.

| Элемент | Тип | Описание |
| --- | --- | --- |
| type | string | Определяет фактический набор полей в зависимости от значения. Смотрите один из следующих объектов:  * `BEFORE` -> BeforeTransformation * `AFTER` -> AfterTransformation * `BETWEEN` -> BetweenTransformation * `REPLACE_BETWEEN` -> ReplaceBetweenTransformation * `REMOVE_NUMBERS` -> RemoveNumbersTransformation * `REMOVE_CREDIT_CARDS` -> RemoveCreditCardNumbersTransformation * `REMOVE_IBANS` -> RemoveIBANsTransformation * `REMOVE_IPS` -> RemoveIPsTransformation * `SPLIT_SELECT` -> SplitSelectTransformation * `TAKE_SEGMENTS` -> TakeSegmentsTransformation Возможные значения: * `AFTER` * `BEFORE` * `BETWEEN` * `REMOVE_CREDIT_CARDS` * `REMOVE_IBANS` * `REMOVE_IPS` * `REMOVE_NUMBERS` * `REPLACE_BETWEEN` * `SPLIT_SELECT` * `TAKE_SEGMENTS` |

```
{



"type": "REMOVE_IPS"



}
```

### SPLIT\_SELECT

SplitSelectTransformation

Parameters

JSON model

#### Объект `SplitSelectTransformation`

Преобразование типа `SPLIT_SELECT`.

Преобразование разбивает обнаруженное значение на массив и сохраняет указанный элемент массива.

| Элемент | Тип | Описание |
| --- | --- | --- |
| delimiter | string | Разделитель для разбиения обнаруженного значения. Сам разделитель не сохраняется. |
| itemIndex | integer | Индекс используемого элемента в разбитом массиве. Индексация начинается с `1`. |

```
{



"type": "SPLIT_SELECT",



"delimiter": "/",



"itemIndex": 2



}
```

### TAKE\_SEGMENTS

TakeSegmentsTransformation

Parameters

JSON model

#### Объект `TakeSegmentsTransformation`

Преобразование типа `TAKE_SEGMENTS`.

Преобразование разбивает обнаруженное значение на массив и сохраняет указанное количество первых или последних элементов.

| Элемент | Тип | Описание |
| --- | --- | --- |
| delimiter | string | Разделитель для разбиения обнаруженного значения. Сам разделитель не сохраняется. |
| segmentCount | integer | Количество сохраняемых элементов. |
| takeFromEnd | boolean | Сохраняет первые (`false`) или последние (`true`) элементы.  Если не задано, используется `false`, сохраняя первые элементы. |

```
{



"type": "TAKE_SEGMENTS",



"delimiter": "/",



"takeFromEnd": false



}
```