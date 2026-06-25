---
title: Extensions API - PUT global configuration
source: https://docs.dynatrace.com/managed/dynatrace-api/configuration-api/extensions-api/put-global-configuration
scraped: 2026-05-12T11:19:57.434041
---

# Extensions API - PUT global configuration

# Extensions API - PUT global configuration

* Reference
* Published Mar 06, 2020

Обновляет глобальную конфигурацию указанного расширения OneAgent или JMX.

Запрос возвращает payload `application/json`.

|  |  |  |
| --- | --- | --- |
| PUT | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/config/v1/extensions/{id}/global` |
| PUT | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/config/v1/extensions/{id}/global` |

## Аутентификация

Для выполнения этого запроса нужен access token со scope `WriteConfig`.

Как его получить и использовать, смотрите [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Параметры

| Параметр | Тип | Описание | Где | Обязательный |
| --- | --- | --- | --- | --- |
| id | string | ID расширения, которое нужно обновить. | path | Required |
| body | [GlobalExtensionConfiguration](#openapi-definition-GlobalExtensionConfiguration) | JSON-тело запроса. Содержит обновлённую конфигурацию расширения. | body | Optional |

### Объекты тела запроса

#### Объект `GlobalExtensionConfiguration`

Глобальная конфигурация расширения OneAgent и JMX

| Элемент | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| enabled | boolean | Расширение включено (`true`) или отключено (`false`). | Required |
| extensionId | string | ID расширения. | Optional |
| infraOnlyEnabled | boolean | Плагин включён (`true`) или отключён (`false`) глобально для хостов в режиме мониторинга только инфраструктуры | Optional |
| properties | object | Список параметров конфигурации.  Каждый параметр представляет собой пару «ключ-значение». | Optional |

### JSON-модель тела запроса

Это модель тела запроса, показывающая возможные элементы. Её нужно адаптировать под реальный запрос.

```
{



"id": "custom.remote.python.demo",



"properties": [



{



"defaultValue": "127.0.0.1",



"key": "serverIp",



"type": "STRING"



},



{



"defaultValue": "",



"key": "password",



"type": "PASSWORD"



},



{



"defaultValue": "dynatrace",



"key": "username",



"type": "STRING"



},



{



"defaultValue": "one",



"dropdownValues": [



"one",



"two",



"three"



],



"key": "dropdownProperty",



"type": "DROPDOWN"



}



]



}
```

## Ответ

### Коды ответа

| Код | Тип | Описание |
| --- | --- | --- |
| **204** | - | Успех. Конфигурация расширения обновлена. Ответ без тела. |
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