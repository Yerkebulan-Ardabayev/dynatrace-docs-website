---
title: Service detection API - GET an opaque web request rule
source: https://docs.dynatrace.com/managed/dynatrace-api/configuration-api/service-api/detection-rules/opaque-web-request/get-a-rule
scraped: 2026-05-12T11:18:25.550113
---

# Service detection API - GET an opaque web request rule

# Service detection API - GET an opaque web request rule

* Reference
* Published Sep 06, 2019

Показывает свойства указанного правила обнаружения сервисов для непрозрачных и внешних веб-запросов.

Запрос возвращает payload `application/json`.

|  |  |  |
| --- | --- | --- |
| GET | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/config/v1/service/detectionRules/OPAQUE_AND_EXTERNAL_WEB_REQUEST/{id}` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/config/v1/service/detectionRules/OPAQUE_AND_EXTERNAL_WEB_REQUEST/{id}` |

## Аутентификация

Для выполнения этого запроса нужен access token со scope `ReadConfig`.

Как его получить и использовать, смотрите [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Параметры

| Параметр | Тип | Описание | Где | Обязательный |
| --- | --- | --- | --- | --- |
| id | string | ID требуемого правила обнаружения сервисов. | path | Required |

## Ответ

Все JSON-модели, зависящие от типа модели, смотрите в [JSON models](/managed/dynatrace-api/configuration-api/service-api/detection-rules/models "Изучите вариации JSON-моделей в Dynatrace API правил обнаружения сервисов.").

### Коды ответа

| Код | Тип | Описание |
| --- | --- | --- |
| **200** | [OpaqueAndExternalWebRequestRule](#openapi-definition-OpaqueAndExternalWebRequestRule) | Успех. Тело ответа содержит свойства указанного правила. |
| **404** | - | Сбой. Правило с указанным ID не существует. |

### Объекты тела ответа

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

### JSON-модели тела ответа

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

* [Service Detection v1](/managed/observe/application-observability/services/service-detection/service-detection-v1 "Узнайте, как Dynatrace Service Detection v1 обнаруживает и именует различные типы сервисов.")
* [Opaque services](/managed/observe/application-observability/services/service-detection/service-detection-v1/service-types/opaque-services "Узнайте, что такое непрозрачные сервисы.")
* [Monitor third-party services](/managed/observe/application-observability/services/service-detection/service-detection-v1/monitor-3rd-party-services "Configure how Dynatrace should monitor third-party services.")