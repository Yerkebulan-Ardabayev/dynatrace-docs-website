---
title: Service detection API - PUT an opaque web service rule
source: https://docs.dynatrace.com/managed/dynatrace-api/configuration-api/service-api/detection-rules/opaque-web-service/put-rule
---

# Service detection API - PUT an opaque web service rule

# Service detection API - PUT an opaque web service rule

* Справочник
* Опубликовано 06 сент. 2019 г.

Обновляет существующее правило обнаружения сервисов для непрозрачных (opaque) и внешних веб-сервисов.

Если правило с указанным ID не существует, создаётся новое правило и добавляется в конец списка правил.

Запрос принимает и возвращает данные в формате `application/json`.

|  |  |  |
| --- | --- | --- |
| PUT | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/config/v1/service/detectionRules/OPAQUE_AND_EXTERNAL_WEB_SERVICE/{id}` |
| PUT | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/config/v1/service/detectionRules/OPAQUE_AND_EXTERNAL_WEB_SERVICE/{id}` |

## Аутентификация

Для выполнения этого запроса нужен токен доступа с областью действия `WriteConfig`.

О том, как получить и использовать токен, см. в разделе [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Параметры

См. [JSON models](/managed/dynatrace-api/configuration-api/service-api/detection-rules/models "Learn the variations of JSON models in the Dynatrace service detection rules API."), чтобы найти все модели JSON, которые зависят от типа модели.

| Параметр | Тип | Описание | В | Обязательный |
| --- | --- | --- | --- | --- |
| id | string | ID правила, которое нужно обновить. | path | Обязательный |
| body | [OpaqueAndExternalWebServiceRule](#openapi-definition-OpaqueAndExternalWebServiceRule) | Тело запроса JSON, содержащее обновлённые параметры правила обнаружения сервиса.  Поле **order** в этом запросе игнорируется. Чтобы задать определённый порядок, нужно использовать запрос `PUT /service/detectionRules/OPAQUE_AND_EXTERNAL_WEB_SERVICE/reorder`. | body | Опционально |

### Объекты тела запроса

#### Объект `OpaqueAndExternalWebServiceRule`

Правило обнаружения сервисов типа `OPAQUE_AND_EXTERNAL_WEB_SERVICE`

| Элемент | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| conditions | [ConditionsOpaqueAndExternalWebServiceAttributeTypeDto](#openapi-definition-ConditionsOpaqueAndExternalWebServiceAttributeTypeDto)[] | Список условий правила.  Если указано несколько условий, применяется логика AND. | Опционально |
| description | string | Краткое описание правила. | Опционально |
| detectAsWebRequestService | boolean | Определять подходящие запросы как веб-сервисы (`false`) или как веб-сервисы запросов (`true`).  Установка этого поля в `true` предотвращает определение подходящих запросов как непрозрачных веб-сервисов. Вместо этого создаётся непрозрачный веб-сервис запросов. Если нужно дополнительно изменить получившийся веб-сервис запросов, нужно создать отдельное правило типа `OPAQUE_AND_EXTERNAL_WEB_REQUEST`.  По умолчанию `false`, подходящие запросы определяются как непрозрачные веб-сервисы. | Опционально |
| enabled | boolean | Правило включено (`true`) или отключено (`false`). | Обязательный |
| id | string | ID правила обнаружения сервиса. | Опционально |
| managementZones | string[] | Management zone (указанная по ID) группы процессов, для которой нужно создать это правило обнаружения сервиса.  Здесь можно указать только 1 management zone. | Опционально |
| metadata | [ConfigurationMetadata](#openapi-definition-ConfigurationMetadata) | Метаданные, полезные для отладки | Опционально |
| name | string | Название правила. | Обязательный |
| order | string | Порядок правила в списке правил.  Правила проверяются сверху вниз. Применяется первое подходящее правило. | Опционально |
| port | [Port](#openapi-definition-Port) | Вклад порта, на котором был обнаружен веб-запрос, в расчёт ID сервиса. | Опционально |
| type | string | Тип правила обнаружения сервиса. | Обязательный |
| urlPath | [UrlPath](#openapi-definition-UrlPath) | Вклад URL, на котором был обнаружен веб-запрос, в расчёт ID сервиса.  Доступны два взаимоисключающих варианта:  * Переопределить обнаруженное значение указанным статическим значением. Указать новое значение в поле **valueOverride**. * Динамически преобразовать обнаруженное значение. Указать параметры преобразования в поле **transformations**. | Опционально |

#### Объект `ConditionsOpaqueAndExternalWebServiceAttributeTypeDto`

Условие правила обнаружения сервиса.

| Элемент | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| attributeType | string | Тип атрибута, который нужно проверить. Элемент может принимать следующие значения * `ENDPOINT` * `IP` * `OPERATION_NAME` * `PG_TAG` * `URL_PATH` * `URL_PORT` | Обязательный |
| compareOperations | [CompareOperation](#openapi-definition-CompareOperation)[] | Список условий правила.  Если указано несколько условий, применяется логика AND. | Опционально |

#### Объект `CompareOperation`

Условие правила.

Фактический набор полей зависит от типа условия. Список фактических объектов см. в описании поля **type** или в разделе [Service detection API - JSON models﻿](https://dt-url.net/2ie3slq?dt=m).

| Элемент | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| type | string | Определяет фактический набор полей в зависимости от значения. См. один из следующих объектов:  * `EQUALS` -> EqualsCompareOperation * `STRING_CONTAINS` -> StringContainsCompareOperation * `STARTS_WITH` -> StartsWithCompareOperation * `ENDS_WITH` -> EndsWithCompareOperation * `EXISTS` -> ExistsCompareOperation * `IP_IN_RANGE` -> IpInRangeCompareOperation * `LESS_THAN` -> LessThanCompareOperation * `GREATER_THAN` -> GreaterThanCompareOperation * `INT_EQUALS` -> IntEqualsCompareOperation * `STRING_EQUALS` -> StringEqualsCompareOperation * `TAG` -> TagCompareOperation Элемент может принимать следующие значения * `ENDS_WITH` * `EQUALS` * `EXISTS` * `GREATER_THAN` * `INT_EQUALS` * `IP_IN_RANGE` * `LESS_THAN` * `STARTS_WITH` * `STRING_CONTAINS` * `STRING_EQUALS` * `TAG` | Обязательный |

#### Объект `ConfigurationMetadata`

Метаданные, полезные для отладки

| Элемент | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| clusterVersion | string | Версия Dynatrace. | Опционально |
| configurationVersions | integer[] | Отсортированный список номеров версий конфигурации. | Опционально |
| currentConfigurationVersions | string[] | Отсортированный список номеров версий конфигурации. | Опционально |

#### Объект `Port`

Вклад порта, на котором был обнаружен веб-запрос, в расчёт ID сервиса.

| Элемент | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| doNotUseForServiceId | boolean | Порт используется (`false`) или не используется (`true`) в расчёте ID сервиса. | Опционально |

#### Объект `UrlPath`

Вклад URL, на котором был обнаружен веб-запрос, в расчёт ID сервиса.

Доступны два взаимоисключающих варианта:

* Переопределить обнаруженное значение указанным статическим значением. Указать новое значение в поле **valueOverride**.
* Динамически преобразовать обнаруженное значение. Указать параметры преобразования в поле **transformations**.

| Элемент | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| transformations | [TransformationBase](#openapi-definition-TransformationBase)[] | Преобразования, которые нужно применить к обнаруженному значению. | Опционально |
| valueOverride | string | Значение, которое нужно использовать вместо обнаруженного значения. | Опционально |

#### Объект `TransformationBase`

Конфигурация преобразования обнаруженного значения.

Если указано несколько преобразований, они обрабатываются последовательно сверху вниз. Каждое преобразование применяется к результату предыдущего преобразования. Например, второе преобразование применяется к результату первого преобразования.

Фактический набор полей зависит от типа преобразования. Список фактических объектов см. в описании поля **type** или в разделе [Service detection API - JSON models﻿](https://dt-url.net/2ie3slq?dt=m).

| Элемент | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| type | string | Определяет фактический набор полей в зависимости от значения. См. один из следующих объектов:  * `BEFORE` -> BeforeTransformation * `AFTER` -> AfterTransformation * `BETWEEN` -> BetweenTransformation * `REPLACE_BETWEEN` -> ReplaceBetweenTransformation * `REMOVE_NUMBERS` -> RemoveNumbersTransformation * `REMOVE_CREDIT_CARDS` -> RemoveCreditCardNumbersTransformation * `REMOVE_IBANS` -> RemoveIBANsTransformation * `REMOVE_IPS` -> RemoveIPsTransformation * `SPLIT_SELECT` -> SplitSelectTransformation * `TAKE_SEGMENTS` -> TakeSegmentsTransformation Элемент может принимать следующие значения * `AFTER` * `BEFORE` * `BETWEEN` * `REMOVE_CREDIT_CARDS` * `REMOVE_IBANS` * `REMOVE_IPS` * `REMOVE_NUMBERS` * `REPLACE_BETWEEN` * `SPLIT_SELECT` * `TAKE_SEGMENTS` | Обязательный |

### Модель JSON тела запроса

Это модель тела запроса, показывающая возможные элементы. Её нужно адаптировать для использования в реальном запросе.

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

## Ответ

### Коды ответа

| Код | Тип | Описание |
| --- | --- | --- |
| **201** | [EntityShortRepresentation](#openapi-definition-EntityShortRepresentation) | Успешно. Создано новое правило обнаружения сервиса. Ответ содержит краткое представление правила, включая ID. |
| **204** | - | Успешно. Правило обнаружения сервиса обновлено. Ответ не содержит тела. |
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

### Модели тела ответа JSON

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

Рекомендуется проверять полезную нагрузку перед отправкой её с фактическим запросом. Код ответа **204** означает, что полезная нагрузка действительна.

Запрос принимает полезную нагрузку `application/json`.

|  |  |  |
| --- | --- | --- |
| POST | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/config/v1/service/detectionRules/OPAQUE_AND_EXTERNAL_WEB_SERVICE/{id}/validator` |
| POST | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/config/v1/service/detectionRules/OPAQUE_AND_EXTERNAL_WEB_SERVICE/{id}/validator` |

### Аутентификация

Для выполнения этого запроса нужен токен доступа со скоупом `WriteConfig`.

Подробнее о том, как получить и использовать его, см. [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

### Ответ

#### Коды ответа

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

#### Модели тела ответа JSON

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

## Похожие темы

* [Service Detection v1](/managed/observe/application-observability/services/service-detection/service-detection-v1 "Find out how Dynatrace Service Detection v1 detects and names different types of services.")
* [Opaque services](/managed/observe/application-observability/services/service-detection/service-detection-v1/service-types/opaque-services "Understand what opaque services are.")