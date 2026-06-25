---
title: ActiveGate tokens API - DELETE токена
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/tokens-v2/activegate-tokens/delete-activegate-token
scraped: 2026-05-12T12:09:59.984198
---

# ActiveGate tokens API - DELETE токена

# ActiveGate tokens API - DELETE токена

* Reference
* Published Dec 02, 2021

Удаляет ActiveGate-токен.

|  |  |  |
| --- | --- | --- |
| DELETE | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/v2/activeGateTokens/{activeGateTokenIdentifier}` |
| DELETE | Environment and Cluster ActiveGate (default port 9999) | `https://{your-activegate-domain}:9999/e/{your-environment-id}/api/v2/activeGateTokens/{activeGateTokenIdentifier}` |

## Аутентификация

Для выполнения запроса необходим access token со scope `activeGateTokenManagement.write`.

О том, как получить и использовать токен, см. [Токены и аутентификация](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Параметры

| Параметр | Тип | Описание | В | Обязательность |
| --- | --- | --- | --- | --- |
| activeGateTokenIdentifier | string | Идентификатор удаляемого ActiveGate-токена, состоящий из [префикса и публичной части](https://dt-url.net/rn00tjg) токена. | path | Обязательный |

## Ответ

### Коды ответа

| Код | Тип | Описание |
| --- | --- | --- |
| **204** | - | Успех. У ответа нет тела. |
| **400** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Неудача. Входные данные некорректны. |
| **404** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Неудача. Запрошенный ресурс не существует. |
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

## Пример

В этом примере запрос удаляет токен с ID **dt0g02.xyz789**.

API-токен передаётся в заголовке **Authorization**.

#### Curl

```
curl --request DELETE \



--url https://mySampleEnv.live.dynatrace.com//api/v2/activeGateTokens/dt0g02.xyz789 \



--header 'Authorization: Api-Token dt0c01.abc123.abcdefjhij1234567890'
```

#### URL запроса

```
https://mySampleEnv.live.dynatrace.com//api/v2/activeGateTokens/dt0g02.xyz789
```

#### Код ответа

204

## Связанные темы

* [Dynatrace ActiveGate](/managed/ingest-from/dynatrace-activegate "Основные понятия, связанные с ActiveGate.")