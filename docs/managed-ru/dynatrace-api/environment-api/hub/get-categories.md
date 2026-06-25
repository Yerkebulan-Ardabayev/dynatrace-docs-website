---
title: Hub capabilities API - GET категорий
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/hub/get-categories
scraped: 2026-05-12T11:54:40.791115
---

# Hub capabilities API - GET категорий

# Hub capabilities API - GET категорий

* Reference
* Published Feb 07, 2023

Выводит список всех доступных категорий элементов Hub.

Запрос возвращает данные в формате `application/json`.

|  |  |  |
| --- | --- | --- |
| GET | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/v2/hub/categories` |
| GET | Environment and Cluster ActiveGate (default port 9999) | `https://{your-activegate-domain}:9999/e/{your-environment-id}/api/v2/hub/categories` |

## Аутентификация

Для выполнения запроса необходим access token со scope `hub.read`.

О том, как получить и использовать токен, см. [Токены и аутентификация](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Параметры

Запрос не имеет настраиваемых параметров.

## Ответ

### Коды ответа

| Код | Тип | Описание |
| --- | --- | --- |
| **200** | [CategoryList](#openapi-definition-CategoryList) | OK |
| **503** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Недоступно |
| **4XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Ошибка на стороне клиента. |
| **5XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Ошибка на стороне сервера. |

### Объекты тела ответа

#### Объект `CategoryList`

| Элемент | Тип | Описание |
| --- | --- | --- |
| items | [Category[]](#openapi-definition-Category) | Список доступных категорий. |

#### Объект `Category`

Список доступных категорий.

| Элемент | Тип | Описание |
| --- | --- | --- |
| description | string | Описание категории |
| id | string | ID категории |
| name | string | Имя категории |

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



"items": [



{



"description": "string",



"id": "string",



"name": "string"



}



]



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