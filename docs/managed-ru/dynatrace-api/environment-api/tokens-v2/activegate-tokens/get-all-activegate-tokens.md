---
title: ActiveGate tokens API - GET всех токенов
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/tokens-v2/activegate-tokens/get-all-activegate-tokens
scraped: 2026-05-12T12:09:57.836002
---

# ActiveGate tokens API - GET всех токенов

# ActiveGate tokens API - GET всех токенов

* Reference
* Published Dec 02, 2021

Выводит список всех ActiveGate-токенов, доступных в вашем окружении.

Объём вывода можно ограничить с помощью пагинации:

1. Укажите количество результатов на странице в параметре запроса **pageSize**.
2. Затем используйте курсор из поля **nextPageKey** предыдущего ответа в параметре запроса **nextPageKey**, чтобы получить последующие страницы.

Запрос возвращает данные в формате `application/json`.

|  |  |  |
| --- | --- | --- |
| GET | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/v2/activeGateTokens` |
| GET | Environment and Cluster ActiveGate (default port 9999) | `https://{your-activegate-domain}:9999/e/{your-environment-id}/api/v2/activeGateTokens` |

## Аутентификация

Для выполнения запроса необходим access token со scope `activeGateTokenManagement.read`.

О том, как получить и использовать токен, см. [Токены и аутентификация](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Параметры

| Параметр | Тип | Описание | В | Обязательность |
| --- | --- | --- | --- | --- |
| nextPageKey | string | Курсор для следующей страницы результатов. Его можно найти в поле **nextPageKey** предыдущего ответа.  Первая страница возвращается всегда, если параметр запроса **nextPageKey** не указан.  Когда **nextPageKey** задан для получения последующих страниц, все остальные query-параметры должны быть пропущены. | query | Опциональный |
| pageSize | integer | Количество ActiveGate-токенов в одном теле ответа.  Максимально допустимый размер страницы 3000, минимальный 100.  Если не задано, используется 100. | query | Опциональный |

## Ответ

### Коды ответа

| Код | Тип | Описание |
| --- | --- | --- |
| **200** | [ActiveGateTokenList](#openapi-definition-ActiveGateTokenList) | Успех. Ответ содержит список ActiveGate-токенов. |
| **400** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Неудача. Входные данные некорректны. |
| **404** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Неудача. Запрошенный ресурс не существует. |
| **4XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Ошибка на стороне клиента. |
| **5XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Ошибка на стороне сервера. |

### Объекты тела ответа

#### Объект `ActiveGateTokenList`

Список ActiveGate-токенов.

| Элемент | Тип | Описание |
| --- | --- | --- |
| activeGateTokens | [ActiveGateToken[]](#openapi-definition-ActiveGateToken) | Список ActiveGate-токенов. |
| nextPageKey | string | Курсор для следующей страницы результатов. На последней странице имеет значение `null`.  Используйте его в параметре запроса **nextPageKey**, чтобы получить последующие страницы результата. |
| pageSize | integer | Количество записей на странице. |
| totalCount | integer | Общее количество записей в результате. |

#### Объект `ActiveGateToken`

Метаданные ActiveGate-токена.

| Элемент | Тип | Описание |
| --- | --- | --- |
| activeGateType | string | Тип ActiveGate, для которого действителен токен. Элемент может принимать значения * `ENVIRONMENT` * `CLUSTER` |
| creationDate | string | Дата создания токена в формате ISO 8601 (`yyyy-MM-dd'T'HH:mm:ss.SSS'Z'`). |
| expirationDate | string | Дата истечения срока действия токена в формате ISO 8601 (`yyyy-MM-dd'T'HH:mm:ss.SSS'Z'`).  Если не задано, токен не истекает. |
| id | string | Идентификатор ActiveGate-токена, состоящий из [префикса и публичной части](https://dt-url.net/rn00tjg?dt=m) токена. |
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



"activeGateTokens": {



"activeGateType": "ENVIRONMENT",



"creationDate": "2020-11-22T08:15:30.144Z",



"expirationDate": "2020-11-24T08:15:30.144Z",



"id": "dt0g02.4KWZO5EF",



"lastUsedDate": "2020-11-23T08:15:30.144Z",



"name": "myToken",



"owner": "john.smith",



"seedToken": "false"



},



"nextPageKey": "AAAAAAAAAAAAAABOAAAAAAAAAAAAAAA6ACQAEAAAABgACgAITFdXQk1BRzYAAAhtZXRhZGF0YQB___-bf___m3iIYxfF7xVQvY72rwblQkcAAwAAAAAAAADHAAAAZA==",



"pageSize": 100,



"totalCount": 1000



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

В этом примере запрос выводит список всех ActiveGate-токенов, доступных в окружении **mySampleEnv**.

API-токен передаётся в заголовке **Authorization**.

Результат усечён до трёх записей.

#### Curl

```
curl --request GET \



--url https://mySampleEnv.live.dynatrace.com//api/v2/activeGateTokens \



--header 'Authorization: Api-Token dt0c01.abc123.abcdefjhij1234567890'
```

#### URL запроса

```
https://mySampleEnv.live.dynatrace.com//api/v2/activeGateTokens
```

#### Тело ответа

```
{



"totalCount": 3,



"pageSize": 3,



"activeGateTokens": [



{



"id": "dt0g02.abc123",



"name": "system:installer",



"owner": "max.mustermann@company.com",



"creationDate": "2021-11-22T11:39:29.797Z",



"seedToken": true,



"activeGateType": "ENVIRONMENT"



},



{



"id": "dt0g02.321cba",



"name": "system:installer",



"owner": "john.smith@company.com",



"creationDate": "2021-11-30T14:11:40.913Z",



"seedToken": true,



"activeGateType": "ENVIRONMENT"



},



{



"id": "dt0g02.123abc",



"name": "system:initial-setup",



"owner": "mary.brown@company.com",



"creationDate": "2021-10-22T13:48:00.135Z",



"lastUsedDate": "2021-12-02T11:52:17.201Z",



"seedToken": false,



"activeGateType": "ENVIRONMENT"



},



]



}
```

#### Код ответа

200

## Связанные темы

* [Dynatrace ActiveGate](/managed/ingest-from/dynatrace-activegate "Основные понятия, связанные с ActiveGate.")