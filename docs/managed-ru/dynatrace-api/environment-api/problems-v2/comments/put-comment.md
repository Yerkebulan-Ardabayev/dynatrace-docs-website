---
title: Problems API v2 - PUT комментарий
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/problems-v2/comments/put-comment
scraped: 2026-05-12T11:57:16.811626
---

# Problems API v2 - PUT комментарий

# Problems API v2 - PUT комментарий

* Справочник
* Опубликовано 12 октября 2020 г.

Обновляет указанный комментарий к проблеме.

Запрос принимает payload в формате `application/json`.

|  |  |  |
| --- | --- | --- |
| PUT | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/v2/problems/{problemId}/comments/{commentId}` |
| PUT | Environment и Cluster ActiveGate (порт по умолчанию 9999) | `https://{your-activegate-domain}:9999/e/{your-environment-id}/api/v2/problems/{problemId}/comments/{commentId}` |

## Аутентификация

Для выполнения запроса нужен access-токен со scope `problems.write`.

О том, как получить и использовать токен, смотрите [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Параметры

| Параметр | Тип | Описание | В | Обязательный |
| --- | --- | --- | --- | --- |
| problemId | string | ID требуемой проблемы. | path | Обязательный |
| commentId | string | ID требуемого комментария. | path | Обязательный |
| body | [CommentRequestDtoImpl](#openapi-definition-CommentRequestDtoImpl) | JSON-тело запроса. Содержит обновлённый комментарий. | body | Необязательный |

### Объекты тела запроса

#### Объект `CommentRequestDtoImpl`

| Поле | Тип | Описание | Обязательность |
| --- | --- | --- | --- |
| context | string | Контекст комментария. | Необязательный |
| message | string | Текст комментария. | Обязательный |

### JSON-модель тела запроса

Это модель тела запроса, показывающая возможные поля. Для реального запроса её нужно адаптировать.

```
{



"context": "string",



"message": "string"



}
```

## Ответ

### Коды ответа

| Код | Тип | Описание |
| --- | --- | --- |
| **204** | - | Успех. Комментарий обновлён. |
| **4XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Ошибка на стороне клиента. |
| **5XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Ошибка на стороне сервера. |

### Объекты тела ответа

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