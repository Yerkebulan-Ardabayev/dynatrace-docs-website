---
title: Problems API - POST закрыть проблему
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/problems/problems/post-close
scraped: 2026-05-12T12:08:11.973935
---

# Problems API - POST закрыть проблему

# Problems API - POST закрыть проблему

* Справочник
* Обновлено 13 июня 2022 г.

Этот API устарел. Используйте вместо него [Problems API v2](/managed/dynatrace-api/environment-api/problems-v2 "Узнайте о возможностях Dynatrace Problems API v2.").

Закрывает указанную проблему и добавляет закрывающий комментарий.

Запрос принимает и возвращает payload в формате `application/json`.

|  |  |  |
| --- | --- | --- |
| POST | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/v1/problem/details/{problemId}/close` |
| POST | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/v1/problem/details/{problemId}/close` |

## Аутентификация

Для выполнения запроса нужен access-токен со scope `DataExport`.

О том, как получить и использовать токен, смотрите [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Параметры

| Параметр | Тип | Описание | В | Обязательный |
| --- | --- | --- | --- | --- |
| problemId | string | ID закрываемой проблемы. | path | Обязательный |
| content | string | Закрывающий комментарий. | query | Обязательный |

## Ответ

### Коды ответа

| Код | Тип | Описание |
| --- | --- | --- |
| **200** | [ProblemCloseResult](#openapi-definition-ProblemCloseResult) | Успех |
| **4XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Ошибка на стороне клиента. |
| **5XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Ошибка на стороне сервера. |

### Объекты тела ответа

#### Объект `ProblemCloseResult`

Результат закрытия проблемы.

| Поле | Тип | Описание |
| --- | --- | --- |
| closeTimestamp | integer | Метка времени, когда было инициировано закрытие. |
| closing | boolean | Проблема в процессе закрытия (`true`) или закрыта (`false`). |
| comment | [ProblemComment](#openapi-definition-ProblemComment) | Комментарий к проблеме. |
| problemId | string | ID проблемы. |

#### Объект `ProblemComment`

Комментарий к проблеме.

| Поле | Тип | Описание |
| --- | --- | --- |
| content | string | Текст комментария. |
| context | string | Контекст комментария.  Может быть любым текстовым комментарием. Задать его можно только через REST API. |
| createdAtTimestamp | integer | Метка времени создания комментария, в UTC миллисекундах. |
| id | string | ID комментария. |
| userName | string | Автор комментария. |

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



"closeTimestamp": 1,



"closing": true,



"comment": {



"content": "string",



"context": "string",



"createdAtTimestamp": 1,



"id": "string",



"userName": "string"



},



"problemId": "string"



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