---
title: Service detection API - POST a full web service rule
source: https://docs.dynatrace.com/managed/dynatrace-api/configuration-api/service-api/detection-rules/full-web-service/post-a-rule
scraped: 2026-05-12T11:18:46.154926
---

# Service detection API - POST a full web service rule

# Service detection API - POST a full web service rule

* Reference
* Published Sep 06, 2019

Создаёт новое правило обнаружения сервисов для полных веб-сервисов.

Запрос принимает и возвращает payload `application/json`.

|  |  |  |
| --- | --- | --- |
| POST | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/config/v1/service/detectionRules/FULL_WEB_SERVICE` |
| POST | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/config/v1/service/detectionRules/FULL_WEB_SERVICE` |

## Аутентификация

Для выполнения этого запроса нужен access token со scope `WriteConfig`.

Как его получить и использовать, смотрите [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Параметры

Все JSON-модели, зависящие от типа модели, смотрите в [JSON models](/managed/dynatrace-api/configuration-api/service-api/detection-rules/models "Изучите вариации JSON-моделей в Dynatrace API правил обнаружения сервисов.").

| Параметр | Тип | Описание | Где | Обязательный |
| --- | --- | --- | --- | --- |
| position | string | Позиция нового правила:  * `APPEND`: в конце списка правил. * `PREPEND`: вверху списка правил. Возможные значения: * `APPEND` * `PREPEND` | query | Optional |
| body | [FullWebServiceRule](#openapi-definition-FullWebServiceRule) | JSON-тело запроса, содержащее параметры нового правила обнаружения сервисов.  Не указывайте ID правила!  Поле **order** в этом запросе игнорируется. Чтобы задать определённый порядок, используйте запрос `PUT /service/detectionRules/FULL_WEB_SERVICE/reorder`. | body | Optional |

### Объекты тела запроса

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

| Элемент | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| applicationId | [ApplicationId](#openapi-definition-ApplicationId) | Вклад в расчёт ID сервиса от обнаруженного ID приложения.  Есть два взаимоисключающих варианта:  * Переопределить обнаруженное значение заданным статическим значением. Укажите новое значение в поле **valueOverride**. * Динамически преобразовать обнаруженное значение. Укажите параметры преобразования в поле **transformations**. | Optional |
| conditions | [ConditionsFullWebServiceAttributeTypeDto[]](#openapi-definition-ConditionsFullWebServiceAttributeTypeDto) | Список условий правила.  Если указано несколько условий, применяется логика AND. | Optional |
| contextRoot | [ContextRoot](#openapi-definition-ContextRoot) | Вклад в расчёт ID сервиса от обнаруженного context root.  Context root это первый сегмент URL запроса после имени сервера. Например, в URL `www.dynatrace.com/support/help/dynatrace-api/` context root равен `support`.  Есть два варианта:  * Сохранить часть обнаруженного URL. Укажите количество сохраняемых сегментов в поле **segmentsToCopyFromUrlPath**. * Динамически преобразовать обнаруженный URL. Укажите параметры преобразования в поле **transformations**.  Можно использовать один или оба варианта. Если используются оба, преобразование применяется к изменённому URL. | Optional |
| description | string | Краткое описание правила. | Optional |
| detectAsWebRequestService | boolean | Обнаруживать совпадающие запросы как полные веб-сервисы (`false`) или как сервисы веб-запросов (`true`).  Установка этого поля в `true` предотвращает обнаружение совпадающих запросов как полных веб-сервисов. Вместо этого создаётся сервис веб-запросов. Если нужно дополнительно изменить получившийся сервис веб-запросов, создайте отдельное правило типа `FULL_WEB_REQUEST`.  По умолчанию `false`, совпадающие запросы обнаруживаются как полные веб-сервисы. | Optional |
| enabled | boolean | Правило включено (`true`) или отключено (`false`). | Required |
| id | string | ID правила обнаружения сервисов. | Optional |
| managementZones | string[] | Зона управления (указанная по ID) группы процессов, для которой должно быть создано это правило обнаружения сервисов.  Здесь можно указать только 1 зону управления. | Optional |
| metadata | [ConfigurationMetadata](#openapi-definition-ConfigurationMetadata) | Метаданные для отладки | Optional |
| name | string | Имя правила. | Required |
| order | string | Порядок правила в списке правил.  Правила выполняются сверху вниз. Применяется первое совпавшее правило. | Optional |
| serverName | [ServerName](#openapi-definition-ServerName) | Вклад в расчёт ID сервиса от обнаруженного имени сервера.  Есть два взаимоисключающих варианта:  * Переопределить обнаруженное значение заданным статическим значением. Укажите новое значение в поле **valueOverride**. * Динамически преобразовать обнаруженное значение. Укажите параметры преобразования в поле **transformations**. | Optional |
| type | string | Тип правила обнаружения сервисов. | Required |
| webServiceName | [WebServiceName](#openapi-definition-WebServiceName) | Вклад в расчёт ID сервиса от обнаруженного имени веб-сервиса.  Есть два взаимоисключающих варианта:  * Переопределить обнаруженное значение заданным статическим значением. Укажите новое значение в поле **valueOverride**. * Динамически преобразовать обнаруженное значение. Укажите параметры преобразования в поле **transformations**. | Optional |
| webServiceNameSpace | [WebServiceNameSpace](#openapi-definition-WebServiceNameSpace) | Вклад в расчёт ID сервиса от обнаруженного пространства имён веб-сервиса.  Есть два взаимоисключающих варианта:  * Переопределить обнаруженное значение заданным статическим значением. Укажите новое значение в поле **valueOverride**. * Динамически преобразовать обнаруженное значение. Укажите параметры преобразования в поле **transformations**. | Optional |

#### Объект `ApplicationId`

Вклад в расчёт ID сервиса от обнаруженного ID приложения.

Есть два взаимоисключающих варианта:

* Переопределить обнаруженное значение заданным статическим значением. Укажите новое значение в поле **valueOverride**.
* Динамически преобразовать обнаруженное значение. Укажите параметры преобразования в поле **transformations**.

| Элемент | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| transformations | [TransformationBase[]](#openapi-definition-TransformationBase) | Преобразования, применяемые к обнаруженному значению. | Optional |
| valueOverride | string | Значение, используемое вместо обнаруженного значения. | Optional |

#### Объект `TransformationBase`

Конфигурация преобразования обнаруженного значения.

Если указано несколько преобразований, они обрабатываются последовательно сверху вниз. Каждое преобразование применяется к результату предыдущего преобразования. Например, второе преобразование применяется к результату первого преобразования.

Фактический набор полей зависит от типа преобразования. Список фактических объектов см. в описании поля **type** или см. [Service detection API - JSON models](https://dt-url.net/2ie3slq).

| Элемент | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| type | string | Определяет фактический набор полей в зависимости от значения. Смотрите один из следующих объектов:  * `BEFORE` -> BeforeTransformation * `AFTER` -> AfterTransformation * `BETWEEN` -> BetweenTransformation * `REPLACE_BETWEEN` -> ReplaceBetweenTransformation * `REMOVE_NUMBERS` -> RemoveNumbersTransformation * `REMOVE_CREDIT_CARDS` -> RemoveCreditCardNumbersTransformation * `REMOVE_IBANS` -> RemoveIBANsTransformation * `REMOVE_IPS` -> RemoveIPsTransformation * `SPLIT_SELECT` -> SplitSelectTransformation * `TAKE_SEGMENTS` -> TakeSegmentsTransformation Возможные значения: * `AFTER` * `BEFORE` * `BETWEEN` * `REMOVE_CREDIT_CARDS` * `REMOVE_IBANS` * `REMOVE_IPS` * `REMOVE_NUMBERS` * `REPLACE_BETWEEN` * `SPLIT_SELECT` * `TAKE_SEGMENTS` | Required |

#### Объект `ConditionsFullWebServiceAttributeTypeDto`

Условие правила обнаружения сервисов.

| Элемент | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| attributeType | string | Тип проверяемого атрибута. Возможные значения: * `APPLICATION_ID` * `CONTEXT_ROOT` * `FRAMEWORK` * `IS_SOAP_SERVICE` * `PG_TAG` * `SERVER_NAME` * `URL_HOST_NAME` * `URL_PATH` * `WEBSERVICE_METHOD` * `WEBSERVICE_NAME` * `WEBSERVICE_NAMESPACE` | Required |
| compareOperations | [CompareOperation[]](#openapi-definition-CompareOperation) | Список условий правила.  Если указано несколько условий, применяется логика AND. | Optional |

#### Объект `CompareOperation`

Условие правила.

Фактический набор полей зависит от типа условия. Список фактических объектов см. в описании поля **type** или см. [Service detection API - JSON models](https://dt-url.net/2ie3slq).

| Элемент | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| type | string | Определяет фактический набор полей в зависимости от значения. Смотрите один из следующих объектов:  * `EQUALS` -> EqualsCompareOperation * `STRING_CONTAINS` -> StringContainsCompareOperation * `STARTS_WITH` -> StartsWithCompareOperation * `ENDS_WITH` -> EndsWithCompareOperation * `EXISTS` -> ExistsCompareOperation * `IP_IN_RANGE` -> IpInRangeCompareOperation * `LESS_THAN` -> LessThanCompareOperation * `GREATER_THAN` -> GreaterThanCompareOperation * `INT_EQUALS` -> IntEqualsCompareOperation * `STRING_EQUALS` -> StringEqualsCompareOperation * `TAG` -> TagCompareOperation Возможные значения: * `ENDS_WITH` * `EQUALS` * `EXISTS` * `GREATER_THAN` * `INT_EQUALS` * `IP_IN_RANGE` * `LESS_THAN` * `STARTS_WITH` * `STRING_CONTAINS` * `STRING_EQUALS` * `TAG` | Required |

#### Объект `ContextRoot`

Вклад в расчёт ID сервиса от обнаруженного context root.

Context root это первый сегмент URL запроса после имени сервера. Например, в URL `www.dynatrace.com/support/help/dynatrace-api/` context root равен `support`.

Есть два варианта:

* Сохранить часть обнаруженного URL. Укажите количество сохраняемых сегментов в поле **segmentsToCopyFromUrlPath**.
* Динамически преобразовать обнаруженный URL. Укажите параметры преобразования в поле **transformations**.

Можно использовать один или оба варианта. Если используются оба, преобразование применяется к изменённому URL.

| Элемент | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| segmentsToCopyFromUrlPath | integer | Количество сохраняемых сегментов URL.  URL делится слешами (`/`), индексация начинается с 1 в context root.  Например, если вы укажете `2` для URL `www.dynatrace.com/support/help/dynatrace-api/`, используется значение `support/help`. | Optional |
| transformations | [ContextRootTransformation[]](#openapi-definition-ContextRootTransformation) | Преобразования, применяемые к обнаруженному значению. | Optional |

#### Объект `ContextRootTransformation`

Конфигурация преобразования обнаруженного значения.

Если указано несколько преобразований, они обрабатываются последовательно сверху вниз. Каждое преобразование применяется к результату предыдущего преобразования. Например, второе преобразование применяется к результату первого преобразования.

Фактический набор полей зависит от поля `type` преобразования.

| Элемент | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| type | string | Определяет фактический набор полей в зависимости от значения. Смотрите один из следующих объектов:  * `BEFORE` -> BeforeTransformation * `REPLACE_BETWEEN` -> ReplaceBetweenTransformation * `REMOVE_NUMBERS` -> RemoveNumbersTransformation * `REMOVE_CREDIT_CARDS` -> RemoveCreditCardNumbersTransformation * `REMOVE_IBANS` -> RemoveIBANsTransformation * `REMOVE_IPS` -> RemoveIPsTransformation Возможные значения: * `BEFORE` * `REMOVE_CREDIT_CARDS` * `REMOVE_IBANS` * `REMOVE_IPS` * `REMOVE_NUMBERS` * `REPLACE_BETWEEN` | Required |

#### Объект `ConfigurationMetadata`

Метаданные для отладки

| Элемент | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| clusterVersion | string | Версия Dynatrace. | Optional |
| configurationVersions | integer[] | Отсортированный список номеров версий конфигурации. | Optional |
| currentConfigurationVersions | string[] | Отсортированный список номеров версий конфигурации. | Optional |

#### Объект `ServerName`

Вклад в расчёт ID сервиса от обнаруженного имени сервера.

Есть два взаимоисключающих варианта:

* Переопределить обнаруженное значение заданным статическим значением. Укажите новое значение в поле **valueOverride**.
* Динамически преобразовать обнаруженное значение. Укажите параметры преобразования в поле **transformations**.

| Элемент | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| transformations | [TransformationBase[]](#openapi-definition-TransformationBase) | Преобразования, применяемые к обнаруженному значению. | Optional |
| valueOverride | string | Значение, используемое вместо обнаруженного значения. | Optional |

#### Объект `WebServiceName`

Вклад в расчёт ID сервиса от обнаруженного имени веб-сервиса.

Есть два взаимоисключающих варианта:

* Переопределить обнаруженное значение заданным статическим значением. Укажите новое значение в поле **valueOverride**.
* Динамически преобразовать обнаруженное значение. Укажите параметры преобразования в поле **transformations**.

| Элемент | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| transformations | [TransformationBase[]](#openapi-definition-TransformationBase) | Преобразования, применяемые к обнаруженному значению. | Optional |
| valueOverride | string | Значение, используемое вместо обнаруженного значения. | Optional |

#### Объект `WebServiceNameSpace`

Вклад в расчёт ID сервиса от обнаруженного пространства имён веб-сервиса.

Есть два взаимоисключающих варианта:

* Переопределить обнаруженное значение заданным статическим значением. Укажите новое значение в поле **valueOverride**.
* Динамически преобразовать обнаруженное значение. Укажите параметры преобразования в поле **transformations**.

| Элемент | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| transformations | [TransformationBase[]](#openapi-definition-TransformationBase) | Преобразования, применяемые к обнаруженному значению. | Optional |
| valueOverride | string | Значение, используемое вместо обнаруженного значения. | Optional |

### JSON-модель тела запроса

Это модель тела запроса, показывающая возможные элементы. Её нужно адаптировать под реальный запрос.

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



"detectAsWebRequestService": false,



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



"type": "FULL_WEB_SERVICE",



"webServiceName": {



"valueOverride": "abc"



},



"webServiceNameSpace": {



"valueOverride": "abc"



}



}
```

## Ответ

### Коды ответа

| Код | Тип | Описание |
| --- | --- | --- |
| **201** | [EntityShortRepresentation](#openapi-definition-EntityShortRepresentation) | Успех. Новое правило обнаружения сервисов создано. Тело ответа содержит краткое представление правила, включая ID. |
| **400** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Сбой. Невалидный ввод. |

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
| code | integer | HTTP-код статуса |
| constraintViolations | [ConstraintViolation[]](#openapi-definition-ConstraintViolation) | Список нарушений ограничений |
| message | string | Сообщение об ошибке |

#### Объект `ConstraintViolation`

Список нарушений ограничений

| Элемент | Тип | Описание |
| --- | --- | --- |
| location | string | - |
| message | string | - |
| parameterLocation | string | -Возможные значения: * `HEADER` * `PATH` * `PAYLOAD_BODY` * `QUERY` |
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

## Validate payload

Рекомендуется валидировать payload перед отправкой реального запроса. Код ответа **204** означает валидный payload.

Запрос принимает payload `application/json`.

|  |  |  |
| --- | --- | --- |
| POST | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/config/v1/service/detectionRules/FULL_WEB_SERVICE/validator` |
| POST | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/config/v1/service/detectionRules/FULL_WEB_SERVICE/validator` |

### Аутентификация

Для выполнения этого запроса нужен access token со scope `WriteConfig`.

Как его получить и использовать, смотрите [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

### Ответ

#### Коды ответа

| Код | Тип | Описание |
| --- | --- | --- |
| **204** | - | Validated. Правило обнаружения сервисов валидно. Ответ без тела. |
| **400** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Сбой. Невалидный ввод. |

#### Объекты тела ответа

#### Объект `ErrorEnvelope`

| Элемент | Тип | Описание |
| --- | --- | --- |
| error | [Error](#openapi-definition-Error) | - |

#### Объект `Error`

| Элемент | Тип | Описание |
| --- | --- | --- |
| code | integer | HTTP-код статуса |
| constraintViolations | [ConstraintViolation[]](#openapi-definition-ConstraintViolation) | Список нарушений ограничений |
| message | string | Сообщение об ошибке |

#### Объект `ConstraintViolation`

Список нарушений ограничений

| Элемент | Тип | Описание |
| --- | --- | --- |
| location | string | - |
| message | string | - |
| parameterLocation | string | -Возможные значения: * `HEADER` * `PATH` * `PAYLOAD_BODY` * `QUERY` |
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

## Связанные темы

* [Service Detection v1](/managed/observe/application-observability/services/service-detection/service-detection-v1 "Узнайте, как Dynatrace Service Detection v1 обнаруживает и именует различные типы сервисов.")