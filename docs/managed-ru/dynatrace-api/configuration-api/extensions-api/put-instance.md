---
title: Extensions API - PUT an extension's instance
source: https://docs.dynatrace.com/managed/dynatrace-api/configuration-api/extensions-api/put-instance
scraped: 2026-05-12T11:20:06.469478
---

# Extensions API - PUT an extension's instance

# Extensions API - PUT an extension's instance

* Reference
* Published Mar 06, 2020

Обновляет свойства указанного экземпляра расширения.

Запрос принимает payload `application/json`.

|  |  |  |
| --- | --- | --- |
| PUT | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/config/v1/extensions/{id}/instances/{configurationId}` |
| PUT | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/config/v1/extensions/{id}/instances/{configurationId}` |

## Аутентификация

Для выполнения этого запроса нужен access token со scope `WriteConfig`.

Как его получить и использовать, смотрите [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Параметры

| Параметр | Тип | Описание | Где | Обязательный |
| --- | --- | --- | --- | --- |
| id | string | ID расширения, в котором вы хотите обновить конфигурацию.  Если вы также задаёте ID расширения в теле, он должен совпадать с этим ID. | path | Required |
| configurationId | string | ID конфигурации, которую нужно обновить. | path | Required |
| body | [ExtensionConfigurationDto](#openapi-definition-ExtensionConfigurationDto) | JSON-тело запроса. Содержит обновлённые параметры конфигурации расширения. | body | Optional |

### Объекты тела запроса

#### Объект `ExtensionConfigurationDto`

| Элемент | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| activeGate | [EntityShortRepresentation](#openapi-definition-EntityShortRepresentation) | Краткое представление сущности Dynatrace. | Optional |
| enabled | boolean | Расширение включено (`true`) или отключено (`false`). | Required |
| endpointId | string | ID эндпоинта. | Optional |
| endpointName | string | Имя эндпоинта, отображаемое в Dynatrace. | Optional |
| extensionId | string | ID расширения. | Optional |
| hostId | string | ID хоста, на котором работает расширение. | Optional |
| properties | object | Список параметров расширения.  Каждый параметр представляет собой пару «ключ-значение». | Optional |
| useGlobal | boolean | Позволяет пропустить текущую конфигурацию и использовать глобальную. | Required |

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



"activeGate": {



"id": "7835970235169136995",



"name": "ActiveGate Host Name"



},



"enabled": true,



"hostId": "HOST-01A7DEFA5340A86D",



"id": "custom.remote.python.demo",



"properties": {



"dropdownProperty": "three",



"password": "",



"serverIp": "127.0.0.1",



"username": "dynatrace"



},



"useGlobal": false



}
```

## Ответ

### Коды ответа

| Код | Тип | Описание |
| --- | --- | --- |
| **204** | - | Успех. Конфигурация обновлена. Ответ без тела. |
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

* [Develop your own Extensions](/managed/ingest-from/extensions/develop-your-extensions "Разработка собственных Extensions в Dynatrace.")