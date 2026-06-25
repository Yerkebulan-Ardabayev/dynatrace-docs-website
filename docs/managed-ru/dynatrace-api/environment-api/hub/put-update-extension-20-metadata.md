---
title: Hub capabilities API - PUT метаданных расширения 2.0
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/hub/put-update-extension-20-metadata
scraped: 2026-05-12T11:54:53.267546
---

# Hub capabilities API - PUT метаданных расширения 2.0

# Hub capabilities API - PUT метаданных расширения 2.0

* Reference
* Published Feb 07, 2023

Обновляет метаданные расширения 2.0, у которого нет метаданных, определённых Dynatrace. Любые существующие метаданные перезаписываются.

Запрос принимает данные в формате `multipart/form-data`.

|  |  |  |
| --- | --- | --- |
| PUT | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/v2/hub/extensions2/{extensionName}/metadata` |
| PUT | Environment and Cluster ActiveGate (default port 9999) | `https://{your-activegate-domain}:9999/e/{your-environment-id}/api/v2/hub/extensions2/{extensionName}/metadata` |

## Аутентификация

Для выполнения запроса необходим access token со scope `hub.write`.

О том, как получить и использовать токен, см. [Токены и аутентификация](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Параметры

| Параметр | Тип | Описание | В | Обязательность |
| --- | --- | --- | --- | --- |
| extensionName | string | Полное имя (FQN) расширения | path | Обязательный |
| body | object | - | body | Опциональный |

### Объекты тела запроса

#### Объект `RequestBody`

| Элемент | Тип | Описание | Обязательность |
| --- | --- | --- | --- |
| description | string | - | Опциональный |
| logo | string | Логотип расширения | Опциональный |
| name | string | Если оставить пустым или пробельным, в качестве имени будет использовано имя расширения | Опциональный |

### JSON-модель тела запроса

Это модель тела запроса, показывающая возможные элементы. Её необходимо адаптировать для использования в реальном запросе.

```
{



"description": "string",



"logo": "string",



"name": "string"



}
```

## Ответ

### Коды ответа

| Код | Тип | Описание |
| --- | --- | --- |
| **204** | - | Метаданные расширения загружены |
| **4XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Ошибка на стороне клиента. |
| **5XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Ошибка на стороне сервера. |

### Объекты тела ответа

#### Объект `ErrorEnvelope`

| Элемент | Тип | Описание |
| --- | --- | --- |
| error | [Error](#openapi-definition-Error) | - |

#### Объект `Error`

| Элемент | Тип | Описание |
| --- | --- | --- |
| code | integer | HTTP-код состояния |
| constraintViolations | [ConstraintViolation[]](#openapi-definition-ConstraintViolation) | Список нарушений ограничений |
| message | string | Сообщение об ошибке |

#### Объект `ConstraintViolation`

Список нарушений ограничений

| Элемент | Тип | Описание |
| --- | --- | --- |
| location | string | - |
| message | string | - |
| parameterLocation | string | -Элемент может принимать значения * `HEADER` * `PATH` * `PAYLOAD_BODY` * `QUERY` |
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