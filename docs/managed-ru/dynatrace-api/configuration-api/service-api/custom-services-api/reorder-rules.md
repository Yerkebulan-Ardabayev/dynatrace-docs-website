---
title: Custom services API - PUT reorder rules
source: https://docs.dynatrace.com/managed/dynatrace-api/configuration-api/service-api/custom-services-api/reorder-rules
scraped: 2026-05-12T11:18:13.025244
---

# Custom services API - PUT reorder rules

# Custom services API - PUT reorder rules

* Reference
* Published Sep 02, 2019

Правила пользовательских сервисов выполняются сверху вниз; применяется первое совпавшее правило.

Этот запрос изменяет порядок правил пользовательских сервисов в соответствии с порядком ID в теле запроса. Правила, отсутствующие в теле запроса, сохраняют свой относительный порядок, но помещаются **после** всех правил, присутствующих в запросе.

Запрос принимает payload `application/json`.

|  |  |  |
| --- | --- | --- |
| PUT | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/config/v1/service/customServices/{technology}/order` |
| PUT | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/config/v1/service/customServices/{technology}/order` |

## Аутентификация

Для выполнения этого запроса нужен access token со scope `WriteConfig`.

Как его получить и использовать, смотрите [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Параметры

| Параметр | Тип | Описание | Где | Обязательный |
| --- | --- | --- | --- | --- |
| technology | string | Технология пользовательских сервисов для обновления. Возможные значения: * `dotNet` * `go` * `java` * `nodeJS` * `php` | path | Required |
| body | [StubList](#openapi-definition-StubList) | JSON-тело запроса, содержащее ID пользовательских сервисов в нужном порядке. Любые дополнительные свойства (*name*, *description*) игнорируются. | body | Optional |

### Объекты тела запроса

#### Объект `StubList`

Упорядоченный список кратких представлений сущностей Dynatrace.

| Элемент | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| values | [EntityShortRepresentation[]](#openapi-definition-EntityShortRepresentation) | Упорядоченный список кратких представлений сущностей Dynatrace. | Required |

#### Объект `EntityShortRepresentation`

Краткое представление сущности Dynatrace.

| Элемент | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| description | string | Краткое описание сущности Dynatrace. | Optional |
| id | string | ID сущности Dynatrace. | Required |
| name | string | Имя сущности Dynatrace. | Optional |

### JSON-модель тела запроса

Это модель тела запроса, показывающая возможные элементы. Её нужно адаптировать под реальный запрос.

```
{



"values": [



{



"description": "Dynatrace entity 1 for the REST API example",



"id": "6a98d7bc-abb9-44f8-ae6a-73e68e71812a",



"name": "Dynatrace entity 1"



},



{



"id": "ee70f7d3-9a4e-4f5f-94d2-c9d6156f1618",



"name": "Dynatrace entity 2"



},



{



"id": "8cdabe77-9e1a-4be8-b3df-269dd6fa9d7f"



}



]



}
```

## Ответ

### Коды ответа

| Код | Тип | Описание |
| --- | --- | --- |
| **204** | - | Успех. Пользовательские сервисы обновлены. Ответ без тела. |
| **400** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Сбой. Невалидный ввод |

### Объекты тела ответа

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

* [Define custom services](/managed/observe/application-observability/services/service-detection/service-detection-v1/service-types/custom-services "Определите точки входа (метод, класс или интерфейс) для пользовательских сервисов, не использующих стандартные протоколы.")