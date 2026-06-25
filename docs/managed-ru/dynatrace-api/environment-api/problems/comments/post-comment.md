---
title: Problems API - POST комментарий
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/problems/comments/post-comment
scraped: 2026-05-12T12:08:00.981989
---

# Problems API - POST комментарий

# Problems API - POST комментарий

* Справочник
* Обновлено 13 июня 2022 г.

Этот API устарел. Используйте вместо него [Problems API v2](/managed/dynatrace-api/environment-api/problems-v2 "Узнайте о возможностях Dynatrace Problems API v2.").

Добавляет комментарий к указанной проблеме.

Запрос принимает и возвращает payload в формате `application/json`.

|  |  |  |
| --- | --- | --- |
| POST | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/v1/problem/details/{problemId}/comments` |
| POST | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/v1/problem/details/{problemId}/comments` |

## Аутентификация

Для выполнения запроса нужен access-токен со scope `DataExport`.

О том, как получить и использовать токен, смотрите [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Параметры

| Параметр | Тип | Описание | В | Обязательный |
| --- | --- | --- | --- | --- |
| problemId | string | ID проблемы, в которую вы хотите добавить комментарий. | path | Обязательный |
| body | [PushProblemComment](#openapi-definition-PushProblemComment) | JSON-тело запроса, содержащее комментарий. | body | Необязательный |

### Объекты тела запроса

#### Объект `PushProblemComment`

Комментарий к проблеме.

| Поле | Тип | Описание | Обязательность |
| --- | --- | --- | --- |
| comment | string | Комментарий к проблеме. | Обязательный |
| context | string | Контекст комментария. Может содержать любую дополнительную информацию. | Необязательный |
| user | string | Автор комментария. | Обязательный |

### JSON-модель тела запроса

Это модель тела запроса, показывающая возможные поля. Для реального запроса её нужно адаптировать.

```
{



"comment": "This is a comment!",



"context": "Slack",



"user": "user1"



}
```

## Ответ

### Коды ответа

| Код | Тип | Описание |
| --- | --- | --- |
| **200** | [ProblemComment](#openapi-definition-ProblemComment) | Успех |
| **4XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Ошибка на стороне клиента. |
| **5XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Ошибка на стороне сервера. |

### Объекты тела ответа

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



"content": "string",



"context": "string",



"createdAtTimestamp": 1,



"id": "string",



"userName": "string"



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

## Пример

В этом примере запрос добавляет новый комментарий к проблеме с ID **2307087411653364173\_1538400720000V2**.

API-токен передаётся в заголовке **Authorization**.

#### Curl

```
curl -X POST \



https://mySampleEnv.live.dynatrace.com/api/v1/problem/details/2307087411653364173_1538400720000V2/comments \



-H 'Authorization: Api-Token dt0c01.abc123.abcdefjhij1234567890' \



-H 'Content-Type: application/json' \



-d '{



"comment": "This one is probably caused by network",



"user": "john.smith",



"context": "Slack"



}'
```

#### URL запроса

```
https://mySampleEnv.live.dynatrace.com/api/v1/problem/details/2307087411653364173_1538400720000V2/comments
```

#### Тело запроса

```
{



"comment": "This one is probably caused by network",



"user": "john.smith",



"context": "Slack"



}
```

#### Тело ответа

```
{



"id": "-6026872125973307382_1538400720000",



"createdAtTimestamp": 1538559856030,



"content": "This one is probably caused by network",



"userName": "john.smith",



"context": "Slack"



}
```

#### Код ответа

200

## Связанные темы

* [Davis® AI](/managed/dynatrace-intelligence "Познакомьтесь с возможностями Davis AI.")