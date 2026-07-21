---
title: Service detection API - PUT a full web service rule
source: https://docs.dynatrace.com/managed/dynatrace-api/configuration-api/service-api/detection-rules/full-web-service/put-a-rule
---

# Service detection API - PUT a full web service rule

# Service detection API - PUT a full web service rule

* Справка
* Опубликовано 06 сентября 2019 г.

Обновляет существующее правило обнаружения сервисов для full web services.

Если правило с указанным ID не существует, создаётся новое правило и добавляется в конец списка правил.

Запрос принимает и возвращает данные в формате `application/json`.

|  |  |  |
| --- | --- | --- |
| PUT | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/config/v1/service/detectionRules/FULL_WEB_SERVICE/{id}` |
| PUT | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/config/v1/service/detectionRules/FULL_WEB_SERVICE/{id}` |

## Аутентификация

Для выполнения этого запроса нужен токен доступа с областью действия `WriteConfig`.

О том, как получить и использовать такой токен, см. в разделе [Токены и аутентификация](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Параметры

Модели [JSON](/managed/dynatrace-api/configuration-api/service-api/detection-rules/models "Learn the variations of JSON models in the Dynatrace service detection rules API.") можно посмотреть, чтобы найти все модели JSON, зависящие от типа модели.

| Параметр | Тип | Описание | В | Обязательный |
| --- | --- | --- | --- | --- |
| id | string | ID правила, которое нужно обновить. | path | Обязательный |
| body | [FullWebServiceRule](#openapi-definition-FullWebServiceRule) | Тело JSON запроса, содержащее обновлённые параметры правила обнаружения сервисов.  Поле **order** в этом запросе игнорируется. Чтобы задать определённый порядок, используй запрос `PUT /service/detectionRules/FULL_WEB_SERVICE/reorder`. | body | Опциональный |

### Объекты тела запроса


#### Объект `FullWebServiceRule`


Правило обнаружения сервиса типа `FULL_WEB_SERVICE`.


Если условие с **attributeType**, равным `FRAMEWORK`, поле **values** внутри **compareOperations** ограничено следующими возможными значениями:


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
| applicationId | [ApplicationId](#openapi-definition-ApplicationId) | Вклад в расчёт ID сервиса от обнаруженного ID приложения.  Доступны два взаимоисключающих варианта:  * Переопределить обнаруженное значение заданным статическим значением. Указать новое значение в поле **valueOverride**. * Динамически преобразовать обнаруженное значение. Указать параметры преобразования в поле **transformations**. | Необязательный |
| conditions | [ConditionsFullWebServiceAttributeTypeDto](#openapi-definition-ConditionsFullWebServiceAttributeTypeDto)[] | Список условий правила.  Если указано несколько условий, применяется логика И. | Необязательный |
| contextRoot | [ContextRoot](#openapi-definition-ContextRoot) | Вклад в расчёт ID сервиса от обнаруженного контекстного корня.  Контекстный корень, это первый сегмент URL запроса после имени сервера. Например, в URL `www.dynatrace.com/support/help/dynatrace-api/` контекстным корнем является `support`.  Доступны два варианта:  * Сохранить часть обнаруженного URL. Указать число сегментов, которые нужно сохранить, в поле **segmentsToCopyFromUrlPath**. * Динамически преобразовать обнаруженный URL. Указать параметры преобразования в поле **transformations**.  Можно использовать один из вариантов или оба сразу. При использовании обоих преобразование применяется к изменённому URL. | Необязательный |
| description | string | Краткое описание правила. | Необязательный |
| detectAsWebRequestService | boolean | Обнаруживать соответствующие запросы как full web services (`false`) или web request services (`true`).  Установка этого поля в `true` предотвращает обнаружение соответствующих запросов как full web services. Вместо этого создаётся web request service. Если нужно дополнительно изменить получившийся web request service, нужно создать отдельное правило типа `FULL_WEB_REQUEST`.  По умолчанию `false`, соответствующие запросы обнаруживаются как full web services. | Необязательный |
| enabled | boolean | Правило включено (`true`) или отключено (`false`). | Обязательный |
| id | string | ID правила обнаружения сервиса. | Необязательный |
| managementZones | string[] | Management zone (указывается по ID) группы процессов, для которой должно быть создано это правило обнаружения сервиса.  Здесь можно указать только 1 management zone. | Необязательный |
| metadata | [ConfigurationMetadata](#openapi-definition-ConfigurationMetadata) | Метаданные, полезные для отладки | Необязательный |
| name | string | Название правила. | Обязательный |
| order | string | Порядок правила в списке правил.  Правила проверяются сверху вниз. Применяется первое подходящее правило. | Необязательный |
| serverName | [ServerName](#openapi-definition-ServerName) | Вклад в расчёт ID сервиса от обнаруженного имени сервера.  Доступны два взаимоисключающих варианта:  * Переопределить обнаруженное значение заданным статическим значением. Указать новое значение в поле **valueOverride**. * Динамически преобразовать обнаруженное значение. Указать параметры преобразования в поле **transformations**. | Необязательный |
| type | string | Тип правила обнаружения сервиса. | Обязательный |
| webServiceName | [WebServiceName](#openapi-definition-WebServiceName) | Вклад в расчёт ID сервиса от обнаруженного имени web-сервиса.  Доступны два взаимоисключающих варианта:  * Переопределить обнаруженное значение заданным статическим значением. Указать новое значение в поле **valueOverride**. * Динамически преобразовать обнаруженное значение. Указать параметры преобразования в поле **transformations**. | Необязательный |
| webServiceNameSpace | [WebServiceNameSpace](#openapi-definition-WebServiceNameSpace) | Вклад в расчёт ID сервиса от обнаруженного пространства имён web-сервиса.  Доступны два взаимоисключающих варианта:  * Переопределить обнаруженное значение заданным статическим значением. Указать новое значение в поле **valueOverride**. * Динамически преобразовать обнаруженное значение. Указать параметры преобразования в поле **transformations**. | Необязательный |


#### Объект `ApplicationId`


Вклад в расчёт ID сервиса от обнаруженного ID приложения.


Доступны два взаимоисключающих варианта:


* Переопределить обнаруженное значение заданным статическим значением. Указать новое значение в поле **valueOverride**.
* Динамически преобразовать обнаруженное значение. Указать параметры преобразования в поле **transformations**.


| Элемент | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| transformations | [TransformationBase](#openapi-definition-TransformationBase)[] | Преобразования, применяемые к обнаруженному значению. | Необязательный |
| valueOverride | string | Значение, используемое вместо обнаруженного значения. | Необязательный |


#### Объект `TransformationBase`


Настройка преобразования обнаруженного значения.


Если указано несколько преобразований, они обрабатываются последовательно сверху вниз. Каждое преобразование применяется к результату предыдущего преобразования. Например, второе преобразование применяется к результату первого преобразования.


Фактический набор полей зависит от типа преобразования. Список фактических объектов можно найти в описании поля **type** или в разделе [Service detection API - JSON models﻿](https://dt-url.net/2ie3slq?dt=m).


| Элемент | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| type | string | Определяет фактический набор полей в зависимости от значения. См. один из следующих объектов:  * `BEFORE` -> BeforeTransformation * `AFTER` -> AfterTransformation * `BETWEEN` -> BetweenTransformation * `REPLACE_BETWEEN` -> ReplaceBetweenTransformation * `REMOVE_NUMBERS` -> RemoveNumbersTransformation * `REMOVE_CREDIT_CARDS` -> RemoveCreditCardNumbersTransformation * `REMOVE_IBANS` -> RemoveIBANsTransformation * `REMOVE_IPS` -> RemoveIPsTransformation * `SPLIT_SELECT` -> SplitSelectTransformation * `TAKE_SEGMENTS` -> TakeSegmentsTransformation Элемент может принимать следующие значения * `AFTER` * `BEFORE` * `BETWEEN` * `REMOVE_CREDIT_CARDS` * `REMOVE_IBANS` * `REMOVE_IPS` * `REMOVE_NUMBERS` * `REPLACE_BETWEEN` * `SPLIT_SELECT` * `TAKE_SEGMENTS` | Обязательный |


#### Объект `ConditionsFullWebServiceAttributeTypeDto`


Условие правила обнаружения сервиса.


| Элемент | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| attributeType | string | Тип проверяемого атрибута. Элемент может принимать следующие значения * `APPLICATION_ID` * `CONTEXT_ROOT` * `FRAMEWORK` * `IS_SOAP_SERVICE` * `PG_TAG` * `SERVER_NAME` * `URL_HOST_NAME` * `URL_PATH` * `WEBSERVICE_METHOD` * `WEBSERVICE_NAME` * `WEBSERVICE_NAMESPACE` | Обязательный |
| compareOperations | [CompareOperation](#openapi-definition-CompareOperation)[] | Список условий правила.  Если указано несколько условий, применяется логика И. | Необязательный |


#### Объект `CompareOperation`


Условие правила.


Фактический набор полей зависит от типа условия. Список фактических объектов можно найти в описании поля **type** или в разделе [Service detection API - JSON models﻿](https://dt-url.net/2ie3slq?dt=m).


| Элемент | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| type | string | Определяет фактический набор полей в зависимости от значения. См. один из следующих объектов:  * `EQUALS` -> EqualsCompareOperation * `STRING_CONTAINS` -> StringContainsCompareOperation * `STARTS_WITH` -> StartsWithCompareOperation * `ENDS_WITH` -> EndsWithCompareOperation * `EXISTS` -> ExistsCompareOperation * `IP_IN_RANGE` -> IpInRangeCompareOperation * `LESS_THAN` -> LessThanCompareOperation * `GREATER_THAN` -> GreaterThanCompareOperation * `INT_EQUALS` -> IntEqualsCompareOperation * `STRING_EQUALS` -> StringEqualsCompareOperation * `TAG` -> TagCompareOperation Элемент может принимать следующие значения * `ENDS_WITH` * `EQUALS` * `EXISTS` * `GREATER_THAN` * `INT_EQUALS` * `IP_IN_RANGE` * `LESS_THAN` * `STARTS_WITH` * `STRING_CONTAINS` * `STRING_EQUALS` * `TAG` | Обязательный |


#### Объект `ContextRoot`


Вклад в расчёт ID сервиса от обнаруженного контекстного корня.


Контекстный корень, это первый сегмент URL запроса после имени сервера. Например, в URL `www.dynatrace.com/support/help/dynatrace-api/` контекстным корнем является `support`.


Доступны два варианта:


* Сохранить часть обнаруженного URL. Указать число сегментов, которые нужно сохранить, в поле **segmentsToCopyFromUrlPath**.
* Динамически преобразовать обнаруженный URL. Указать параметры преобразования в поле **transformations**.


Можно использовать один из вариантов или оба сразу. При использовании обоих преобразование применяется к изменённому URL.


| Элемент | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| segmentsToCopyFromUrlPath | integer | Число сегментов URL, которые нужно сохранить.  URL делится по слэшам (`/`), нумерация начинается с 1 от контекстного корня.  Например, если для URL `www.dynatrace.com/support/help/dynatrace-api/` указать `2`, используется значение `support/help`. | Необязательный |
| transformations | [ContextRootTransformation](#openapi-definition-ContextRootTransformation)[] | Преобразования, применяемые к обнаруженному значению. | Необязательный |


#### Объект `ContextRootTransformation`


Настройка преобразования обнаруженного значения.

Если задано несколько преобразований, они выполняются последовательно, сверху вниз. Каждое преобразование применяется к результату предыдущего. Например, второе преобразование применяется к результату первого преобразования.

Фактический набор полей зависит от значения `type` преобразования.

| Элемент | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| type | string | Определяет фактический набор полей в зависимости от значения. См. один из следующих объектов:  * `BEFORE` -> BeforeTransformation * `REPLACE_BETWEEN` -> ReplaceBetweenTransformation * `REMOVE_NUMBERS` -> RemoveNumbersTransformation * `REMOVE_CREDIT_CARDS` -> RemoveCreditCardNumbersTransformation * `REMOVE_IBANS` -> RemoveIBANsTransformation * `REMOVE_IPS` -> RemoveIPsTransformation Элемент может принимать следующие значения * `BEFORE` * `REMOVE_CREDIT_CARDS` * `REMOVE_IBANS` * `REMOVE_IPS` * `REMOVE_NUMBERS` * `REPLACE_BETWEEN` | Обязательный |

#### Объект `ConfigurationMetadata`

Метаданные, полезные для отладки

| Элемент | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| clusterVersion | string | Версия Dynatrace. | Опциональный |
| configurationVersions | integer[] | Отсортированный список номеров версий конфигурации. | Опциональный |
| currentConfigurationVersions | string[] | Отсортированный список номеров версий конфигурации. | Опциональный |

#### Объект `ServerName`

Вклад в вычисление ID сервиса от обнаруженного имени сервера.

Доступны два взаимоисключающих варианта:

* Переопределить обнаруженное значение заданным статическим значением. Указать новое значение в поле **valueOverride**.
* Динамически преобразовать обнаруженное значение. Указать параметры преобразования в поле **transformations**.

| Элемент | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| transformations | [TransformationBase](#openapi-definition-TransformationBase)[] | Преобразования, применяемые к обнаруженному значению. | Опциональный |
| valueOverride | string | Значение, используемое вместо обнаруженного значения. | Опциональный |

#### Объект `WebServiceName`

Вклад в вычисление ID сервиса от обнаруженного имени веб-сервиса.

Доступны два взаимоисключающих варианта:

* Переопределить обнаруженное значение заданным статическим значением. Указать новое значение в поле **valueOverride**.
* Динамически преобразовать обнаруженное значение. Указать параметры преобразования в поле **transformations**.

| Элемент | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| transformations | [TransformationBase](#openapi-definition-TransformationBase)[] | Преобразования, применяемые к обнаруженному значению. | Опциональный |
| valueOverride | string | Значение, используемое вместо обнаруженного значения. | Опциональный |

#### Объект `WebServiceNameSpace`

Вклад в вычисление ID сервиса от обнаруженного пространства имён веб-сервиса.

Доступны два взаимоисключающих варианта:

* Переопределить обнаруженное значение заданным статическим значением. Указать новое значение в поле **valueOverride**.
* Динамически преобразовать обнаруженное значение. Указать параметры преобразования в поле **transformations**.

| Элемент | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| transformations | [TransformationBase](#openapi-definition-TransformationBase)[] | Преобразования, применяемые к обнаруженному значению. | Опциональный |
| valueOverride | string | Значение, используемое вместо обнаруженного значения. | Опциональный |

### Модель тела запроса JSON

Это модель тела запроса, показывающая возможные элементы. Её нужно скорректировать для использования в реальном запросе.

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

### Коды ответов

| Код | Тип | Описание |
| --- | --- | --- |
| **201** | [EntityShortRepresentation](#openapi-definition-EntityShortRepresentation) | Успех. Создано новое правило обнаружения сервиса. Ответ содержит краткое представление правила, включая ID. |
| **204** | - | Успех. Правило обнаружения сервиса обновлено. Ответ не содержит тела. |
| **400** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Ошибка. Входные данные недействительны. |

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
| constraintViolations | [ConstraintViolation](#openapi-definition-ConstraintViolation)[] | Список нарушений ограничений |
| message | string | Сообщение об ошибке |

#### Объект `ConstraintViolation`

Список нарушений ограничений

| Элемент | Тип | Описание |
| --- | --- | --- |
| location | string | - |
| message | string | - |
| parameterLocation | string | -Элемент может принимать следующие значения * `HEADER` * `PATH` * `PAYLOAD_BODY` * `QUERY` |
| path | string | - |

### Модели JSON тела ответа

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

## Проверка полезной нагрузки

Рекомендуется проверять полезную нагрузку перед отправкой её в составе реального запроса. Код ответа **204** означает, что полезная нагрузка действительна.

Запрос принимает полезную нагрузку `application/json`.

|  |  |  |
| --- | --- | --- |
| POST | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/config/v1/service/detectionRules/FULL_WEB_SERVICE/{id}/validator` |
| POST | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/config/v1/service/detectionRules/FULL_WEB_SERVICE/{id}/validator` |

### Аутентификация

Для выполнения этого запроса нужен токен доступа с областью действия `WriteConfig`.

О том, как его получить и использовать, см. [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

### Ответ

#### Коды ответов

| Код | Тип | Описание |
| --- | --- | --- |
| **204** | - | Проверено. Правило обнаружения сервиса действительно. Ответ не содержит тела. |
| **400** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Ошибка. Входные данные недействительны. |

#### Объекты тела ответа

#### Объект `ErrorEnvelope`

| Элемент | Тип | Описание |
| --- | --- | --- |
| error | [Error](#openapi-definition-Error) | - |

#### Объект `Error`

| Элемент | Тип | Описание |
| --- | --- | --- |
| code | integer | HTTP-код статуса |
| constraintViolations | [ConstraintViolation](#openapi-definition-ConstraintViolation)[] | Список нарушений ограничений |
| message | string | Сообщение об ошибке |

#### Объект `ConstraintViolation`

Список нарушений ограничений

| Элемент | Тип | Описание |
| --- | --- | --- |
| location | string | - |
| message | string | - |
| parameterLocation | string | -Элемент может принимать следующие значения * `HEADER` * `PATH` * `PAYLOAD_BODY` * `QUERY` |
| path | string | - |

#### Модели JSON тела ответа

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

## Смежные темы

* [Service Detection v1](/managed/observe/application-observability/services/service-detection/service-detection-v1 "Find out how Dynatrace Service Detection v1 detects and names different types of services.")