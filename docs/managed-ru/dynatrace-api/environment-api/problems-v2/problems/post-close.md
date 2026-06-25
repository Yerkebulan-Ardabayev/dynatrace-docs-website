---
title: Problems API v2 - POST закрыть проблему
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/problems-v2/problems/post-close
scraped: 2026-05-12T11:57:25.245245
---

# Problems API v2 - POST закрыть проблему

# Problems API v2 - POST закрыть проблему

* Справочник
* Опубликовано 12 октября 2020 г.

Закрывает указанную проблему и добавляет закрывающий комментарий.

Запрос принимает и возвращает payload в формате `application/json`.

|  |  |  |
| --- | --- | --- |
| POST | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/v2/problems/{problemId}/close` |
| POST | Environment и Cluster ActiveGate (порт по умолчанию 9999) | `https://{your-activegate-domain}:9999/e/{your-environment-id}/api/v2/problems/{problemId}/close` |

## Аутентификация

Для выполнения запроса нужен access-токен со scope `problems.write`.

О том, как получить и использовать токен, смотрите [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Параметры

| Параметр | Тип | Описание | В | Обязательный |
| --- | --- | --- | --- | --- |
| problemId | string | ID требуемой проблемы. | path | Обязательный |
| body | [ProblemCloseRequestDtoImpl](#openapi-definition-ProblemCloseRequestDtoImpl) | JSON-тело запроса. Содержит закрывающий комментарий к проблеме. | body | Необязательный |

### Объекты тела запроса

#### Объект `ProblemCloseRequestDtoImpl`

| Поле | Тип | Описание | Обязательность |
| --- | --- | --- | --- |
| message | string | Текст закрывающего комментария. | Обязательный |

### JSON-модель тела запроса

Это модель тела запроса, показывающая возможные поля. Для реального запроса её нужно адаптировать.

```
{



"message": "string"



}
```

## Ответ

### Коды ответа

| Код | Тип | Описание |
| --- | --- | --- |
| **200** | [ProblemCloseResult](#openapi-definition-ProblemCloseResult) | Успех |
| **204** | - | Проблема уже закрыта, запрос не выполнялся. |
| **4XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Ошибка на стороне клиента. |
| **5XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Ошибка на стороне сервера. |

### Объекты тела ответа

#### Объект `ProblemCloseResult`

Результат закрытия проблемы.

| Поле | Тип | Описание |
| --- | --- | --- |
| closeTimestamp | integer | Метка времени, когда пользователь инициировал закрытие. |
| closing | boolean | `true`, если проблема закрывается. |
| comment | [Comment](#openapi-definition-Comment) | Комментарий к проблеме. |
| problemId | string | ID проблемы. |

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



"closeTimestamp": 1,



"closing": true,



"comment": {



"authorName": "string",



"content": "string",



"context": "string",



"createdAtTimestamp": 1,



"id": "string"



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