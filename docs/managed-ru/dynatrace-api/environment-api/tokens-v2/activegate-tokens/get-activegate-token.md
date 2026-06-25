---
title: ActiveGate tokens API - GET токена
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/tokens-v2/activegate-tokens/get-activegate-token
scraped: 2026-05-12T12:09:55.811769
---

# ActiveGate tokens API - GET токена

# ActiveGate tokens API - GET токена

* Reference
* Published Dec 02, 2021

Возвращает метаданные ActiveGate-токена по его идентификатору.

Запрос возвращает данные в формате `application/json`.

|  |  |  |
| --- | --- | --- |
| GET | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/v2/activeGateTokens/{activeGateTokenIdentifier}` |
| GET | Environment and Cluster ActiveGate (default port 9999) | `https://{your-activegate-domain}:9999/e/{your-environment-id}/api/v2/activeGateTokens/{activeGateTokenIdentifier}` |

## Аутентификация

Для выполнения запроса необходим access token со scope `activeGateTokenManagement.read`.

О том, как получить и использовать токен, см. [Токены и аутентификация](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Параметры

| Параметр | Тип | Описание | В | Обязательность |
| --- | --- | --- | --- | --- |
| activeGateTokenIdentifier | string | Идентификатор ActiveGate-токена, состоящий из [префикса и публичной части](https://dt-url.net/rn00tjg) токена. | path | Обязательный |

## Ответ

### Коды ответа

| Код | Тип | Описание |
| --- | --- | --- |
| **200** | [ActiveGateToken](#openapi-definition-ActiveGateToken) | Успех. Ответ содержит метаданные токенов. |
| **400** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Неудача. Входные данные некорректны. |
| **404** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Неудача. Запрошенный ресурс не существует. |
| **4XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Ошибка на стороне клиента. |
| **5XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Ошибка на стороне сервера. |

### Объекты тела ответа

#### Объект `ActiveGateToken`

Метаданные ActiveGate-токена.

| Элемент | Тип | Описание |
| --- | --- | --- |
| activeGateType | string | Тип ActiveGate, для которого действителен токен. Элемент может принимать значения * `ENVIRONMENT` * `CLUSTER` |
| creationDate | string | Дата создания токена в формате ISO 8601 (`yyyy-MM-dd'T'HH:mm:ss.SSS'Z'`). |
| expirationDate | string | Дата истечения срока действия токена в формате ISO 8601 (`yyyy-MM-dd'T'HH:mm:ss.SSS'Z'`).  Если не задано, токен не истекает. |
| id | string | Идентификатор ActiveGate-токена, состоящий из [префикса и публичной части](https://dt-url.net/rn00tjg) токена. |
| lastUsedDate | string | Дата последнего использования токена в формате ISO 8601 (`yyyy-MM-dd'T'HH:mm:ss.SSS'Z'`). |
| name | string | Имя токена. |
| owner | string | Владелец токена. |
| seedToken | boolean | Токен является seed-токеном (`true`) или индивидуальным токеном (`false`). |

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



"activeGateType": "ENVIRONMENT",



"creationDate": "2020-11-22T08:15:30.144Z",



"expirationDate": "2020-11-24T08:15:30.144Z",



"id": "dt0g02.4KWZO5EF",



"lastUsedDate": "2020-11-23T08:15:30.144Z",



"name": "myToken",



"owner": "john.smith",



"seedToken": false



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

В этом примере запрос получает метаданные для токена с ID **dt0g02.abc123**.

API-токен передаётся в заголовке **Authorization**.

#### Curl

```
curl --request GET \



--url https://mySampleEnv.live.dynatrace.com//api/v2/activeGateTokens/dt0g02.abc123 \



--header 'Authorization: Api-Token dt0c01.abc123.abcdefjhij1234567890'
```

#### URL запроса

```
https://mySampleEnv.live.dynatrace.com//api/v2/activeGateTokens/dt0g02.abc123
```

#### Тело ответа

```
{



"id": "dt0g02.abc123",



"name": "system:installer",



"owner": "max.mustermann@company.com",



"creationDate": "2021-11-22T11:39:29.797Z",



"seedToken": true,



"activeGateType": "ENVIRONMENT"



}
```

#### Код ответа

200

## Связанные темы

* [Dynatrace ActiveGate](/managed/ingest-from/dynatrace-activegate "Основные понятия, связанные с ActiveGate.")