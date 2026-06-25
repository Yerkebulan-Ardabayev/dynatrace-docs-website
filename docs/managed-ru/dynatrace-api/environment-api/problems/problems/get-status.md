---
title: Problems API - GET количество
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/problems/problems/get-status
scraped: 2026-05-12T12:07:58.972508
---

# Problems API - GET количество

# Problems API - GET количество

* Справочник
* Обновлено 13 июня 2022 г.

Этот API устарел. Используйте вместо него [Problems API v2](/managed/dynatrace-api/environment-api/problems-v2 "Узнайте о возможностях Dynatrace Problems API v2.").

Возвращает количество проблем в вашем окружении и их распределение по уровням воздействия.

Запрос возвращает payload в формате `application/json`.

|  |  |  |
| --- | --- | --- |
| GET | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/v1/problem/status` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/v1/problem/status` |

## Аутентификация

Для выполнения запроса нужен access-токен со scope `DataExport`.

О том, как получить и использовать токен, смотрите [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Параметры

Запрос не имеет настраиваемых параметров.

## Ответ

### Коды ответа

| Код | Тип | Описание |
| --- | --- | --- |
| **200** | [ProblemStatusResultWrapper](#openapi-definition-ProblemStatusResultWrapper) | Успех |
| **4XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Ошибка на стороне клиента. |
| **5XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Ошибка на стороне сервера. |

### Объекты тела ответа

#### Объект `ProblemStatusResultWrapper`

| Поле | Тип | Описание |
| --- | --- | --- |
| result | [GlobalProblemStatus](#openapi-definition-GlobalProblemStatus) | Количество открытых проблем в вашем окружении. |

#### Объект `GlobalProblemStatus`

Количество открытых проблем в вашем окружении.

| Поле | Тип | Описание |
| --- | --- | --- |
| openProblemCounts | object | Количество открытых проблем по уровням воздействия. |
| totalOpenProblemsCount | integer | Общее количество открытых проблем в вашем окружении. |

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



"result": {



"openProblemCounts": {



"APPLICATION": 1,



"ENVIRONMENT": 1,



"INFRASTRUCTURE": 1,



"SERVICE": 1



},



"totalOpenProblemsCount": 1



}



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

В этом примере запрос получает количество проблем в окружении.

API-токен передаётся в заголовке **Authorization**.

Ответ показывает, что обнаружено 34 проблемы:

* 4 затрагивают **инфраструктуру**.
* 30 затрагивают **приложения**.

#### Curl

```
curl -X GET \



https://mySampleEnv.live.dynatrace.com/api/v1/problem/status \



-H 'Authorization: Api-Token dt0c01.abc123.abcdefjhij1234567890'
```

#### URL запроса

```
https://mySampleEnv.live.dynatrace.com/api/v1/problem/status
```

#### Содержимое ответа

```
{



"result": {



"totalOpenProblemsCount": 34,



"openProblemCounts": {



"INFRASTRUCTURE": 4,



"SERVICE": 0,



"APPLICATION": 30,



"ENVIRONMENT": 0



}



}



}
```

#### Код ответа

200

## Связанные темы

* [Davis® AI](/managed/dynatrace-intelligence "Познакомьтесь с возможностями Davis AI.")