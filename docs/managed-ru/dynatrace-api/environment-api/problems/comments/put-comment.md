---
title: Problems API - PUT комментарий
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/problems/comments/put-comment
scraped: 2026-05-12T12:08:05.039185
---

# Problems API - PUT комментарий

# Problems API - PUT комментарий

* Справочник
* Обновлено 13 июня 2022 г.

Этот API устарел. Используйте вместо него [Problems API v2](/managed/dynatrace-api/environment-api/problems-v2 "Узнайте о возможностях Dynatrace Problems API v2.").

Обновляет существующий комментарий к указанной проблеме. Поле, отсутствующее в теле, остаётся без изменений.

Запрос принимает payload в формате `application/json`.

|  |  |  |
| --- | --- | --- |
| PUT | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/v1/problem/details/{problemId}/comments/{commentId}` |
| PUT | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/v1/problem/details/{problemId}/comments/{commentId}` |

## Аутентификация

Для выполнения запроса нужен access-токен со scope `DataExport`.

О том, как получить и использовать токен, смотрите [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Параметры

| Параметр | Тип | Описание | В | Обязательный |
| --- | --- | --- | --- | --- |
| problemId | string | ID проблемы, в которой вы хотите изменить комментарий. | path | Обязательный |
| commentId | string | ID комментария, который вы хотите изменить. | path | Обязательный |
| body | [PushProblemComment](#openapi-definition-PushProblemComment) | JSON-тело запроса, содержащее обновлённый комментарий. | body | Необязательный |

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

В этом примере запрос обновляет комментарий с ID **-6026872125973307382\_1538400720000** к проблеме с ID **2307087411653364173\_1538400720000V2**.

Обновление добавляет дополнительную информацию для поля **context**.

API-токен передаётся в заголовке **Authorization**.

#### Curl

```
curl -X PUT \



https://mySampleEnv.live.dynatrace.com/api/v1/problem/details/2307087411653364173_1538400720000V2/comments/-6026872125973307382_1538400720000 \



-H 'Authorization: Api-Token dt0c01.abc123.abcdefjhij1234567890' \



-H 'Content-Type: application/json' \



-d '{



"comment": "This one is probably caused by network",



"user": "john.smith",



"context": "Slack - by Tom Johnson"



}'
```

#### URL запроса

```
https://mySampleEnv.live.dynatrace.com/api/v1/problem/details/2307087411653364173_1538400720000V2/comments/-6026872125973307382_1538400720000
```

#### Тело запроса

```
{



"comment": "This one is probably caused by network",



"context": "Slack - by Tom Johnson"



}
```

#### Тело ответа

```
{



"id": "-6026872125973307382_1538400720000",



"createdAtTimestamp": 1538559856030,



"content": "This one is probably caused by network",



"userName": "john.smith",



"context": "Slack - by Tom Johnson"



}
```

#### Код ответа

200

## Связанные темы

* [Davis® AI](/managed/dynatrace-intelligence "Познакомьтесь с возможностями Davis AI.")