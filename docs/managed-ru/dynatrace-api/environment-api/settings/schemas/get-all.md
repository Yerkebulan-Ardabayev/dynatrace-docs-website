---
title: Settings API - GET all schemas
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/settings/schemas/get-all
scraped: 2026-05-12T11:38:44.544349
---

# Settings API - GET all schemas

# Settings API - GET all schemas

* Reference
* Published Feb 24, 2021

Возвращает список всех settings schemas, доступных в вашем окружении.

Запрос возвращает данные в формате `application/json`.

|  |  |  |
| --- | --- | --- |
| GET | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/v2/settings/schemas` |
| GET | Environment and Cluster ActiveGate (default port 9999) | `https://{your-activegate-domain}:9999/e/{your-environment-id}/api/v2/settings/schemas` |

## Аутентификация

Для выполнения запроса необходим access token со scope `settings.read`.

О том, как получить и использовать токен, см. [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Параметры

| Параметр | Тип | Описание | Где | Обязательный |
| --- | --- | --- | --- | --- |
| fields | string | Список полей, включаемых в ответ. Предоставленный набор полей заменяет набор по умолчанию.  Укажите нужные поля верхнего уровня, разделённые запятыми (например, `schemaId,displayName`).  Поддерживаемые поля: `schemaId`, `displayName`, `maturity`, `latestSchemaVersion`, `multiObject`, `ordered`, `ownerBasedAccessControl`. | query | Optional |

## Ответ

### Коды ответа

| Код | Тип | Описание |
| --- | --- | --- |
| **200** | [SchemaList](#openapi-definition-SchemaList) | Успех |
| **4XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Ошибка на стороне клиента. |
| **5XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Ошибка на стороне сервера. |

### Объекты тела ответа

#### Объект `SchemaList`

Список доступных settings schemas.

| Элемент | Тип | Описание |
| --- | --- | --- |
| items | [SchemaStub[]](#openapi-definition-SchemaStub) | Список settings schemas. |
| totalCount | integer | Количество schemas в списке. |

#### Объект `SchemaStub`

Краткое представление settings schema.

| Элемент | Тип | Описание |
| --- | --- | --- |
| displayName | string | Имя schema. |
| latestSchemaVersion | string | Самая последняя версия schema. |
| maturity | string | Зрелость schema. Возможные значения:  * PREVIEW: функции preview, как правило, недоступны массово, но могут быть доступны в отдельных окружениях в рамках программ раннего доступа. У них наиболее высокая вероятность несовместимых изменений. * EARLY\_ADOPTER: функции с пометкой "early adopter" доступны во всех окружениях, но недостаточно зрелы для обозначения "general availability". Несовместимых изменений для них не ожидается, но учитывайте, что они пока не полностью стабильны и в редких случаях могут потребоваться несовместимые изменения. * GENERAL\_AVAILABILITY: функции с пометкой "general availability" наиболее стабильны. Schemas со временем продолжают развиваться, но это делается с сохранением обратной совместимости.  В любом случае автоматизации должны использовать поле `schemaVersion` при записи settings objects. Возможные значения: * `EARLY_ADOPTER` * `GENERAL_AVAILABILITY` * `PREVIEW` |
| multiObject | boolean | Флаг multi-object. `True`, если schema является multi-object. |
| ordered | boolean | Флаг ordered. `True`, если schema является упорядоченной multi-object schema. |
| ownerBasedAccessControl | boolean | Флаг owner based access control. `True`, если у schema включён owner based access control. |
| schemaId | string | ID schema. |

#### Объект `ErrorEnvelope`

| Элемент | Тип | Описание |
| --- | --- | --- |
| error | [Error](#openapi-definition-Error) | - |

#### Объект `Error`

| Элемент | Тип | Описание |
| --- | --- | --- |
| code | integer | HTTP-код статуса |
| constraintViolations | [ConstraintViolation[]](#openapi-definition-ConstraintViolation) | Список нарушений constraints |
| message | string | Сообщение об ошибке |

#### Объект `ConstraintViolation`

Список нарушений constraints

| Элемент | Тип | Описание |
| --- | --- | --- |
| location | string | - |
| message | string | - |
| parameterLocation | string | -Возможные значения: * `HEADER` * `PATH` * `PAYLOAD_BODY` * `QUERY` |
| path | string | - |

### JSON-модели тела ответа

```
{



"items": [



{



"displayName": "Built-in container monitoring rules",



"latestSchemaVersion": "1.4.2",



"maturity": "GENERAL_AVAILABILITY",



"multiObject": true,



"ordered": false,



"ownerBasedAccessControl": true,



"schemaId": "builtin:container.built-in-monitoring-rule"



}



],



"totalCount": 1



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