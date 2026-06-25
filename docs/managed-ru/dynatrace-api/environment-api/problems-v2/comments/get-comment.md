---
title: Problems API v2 - GET комментарий
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/problems-v2/comments/get-comment
scraped: 2026-05-12T11:57:29.372212
---

# Problems API v2 - GET комментарий

# Problems API v2 - GET комментарий

* Справочник
* Опубликовано 12 октября 2020 г.

Возвращает указанный комментарий к проблеме.

Запрос возвращает payload в формате `application/json`.

|  |  |  |
| --- | --- | --- |
| GET | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/v2/problems/{problemId}/comments/{commentId}` |
| GET | Environment и Cluster ActiveGate (порт по умолчанию 9999) | `https://{your-activegate-domain}:9999/e/{your-environment-id}/api/v2/problems/{problemId}/comments/{commentId}` |

## Аутентификация

Для выполнения запроса нужен access-токен со scope `problems.read`.

О том, как получить и использовать токен, смотрите [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Параметры

| Параметр | Тип | Описание | В | Обязательный |
| --- | --- | --- | --- | --- |
| problemId | string | ID требуемой проблемы. | path | Обязательный |
| commentId | string | ID требуемого комментария. | path | Обязательный |

## Ответ

### Коды ответа

| Код | Тип | Описание |
| --- | --- | --- |
| **200** | [Comment](#openapi-definition-Comment) | Успех |
| **4XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Ошибка на стороне клиента. |
| **5XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Ошибка на стороне сервера. |

### Объекты тела ответа

#### Объект `Comment`

Комментарий к проблеме.

| Поле | Тип | Описание |
| --- | --- | --- |
| authorName | string | Пользователь, написавший комментарий. |
| content | string | Текст комментария. |
| context | string | Контекст комментария. |
| createdAtTimestamp | integer | Метка времени создания комментария, в UTC миллисекундах. |
| id | string | ID комментария. |

#### Объект `ErrorEnvelope`

| Поле | Тип | Описание |
| --- | --- | --- |
| error | [Error](#openapi-definition-Error) | - |

#### Объект `Error`

| Поле | Тип | Описание |
| --- | --- | --- |
| code | integer | HTTP-код состояния. |
| constraintViolations | [ConstraintViolation[]](#openapi-definition-ConstraintViolation) | Список нарушений ограничений. |
| message | string | Сообщение об ошибке. |

#### Объект `ConstraintViolation`

Список нарушений ограничений.

| Поле | Тип | Описание |
| --- | --- | --- |
| location | string | - |
| message | string | - |
| parameterLocation | string | Поле может принимать значения: * `HEADER` * `PATH` * `PAYLOAD_BODY` * `QUERY` |
| path | string | - |

### JSON-модели тела ответа

```
{



"authorName": "string",



"content": "string",



"context": "string",



"createdAtTimestamp": 1,



"id": "string"



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

## Связанные темы

* [Davis® AI](/managed/dynatrace-intelligence "Познакомьтесь с возможностями Davis AI.")