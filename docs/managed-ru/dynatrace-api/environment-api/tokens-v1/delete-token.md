---
title: Tokens API v1 - DELETE существующий токен
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/tokens-v1/delete-token
scraped: 2026-05-12T12:11:11.376981
---

# Tokens API v1 - DELETE существующий токен

# Tokens API v1 - DELETE существующий токен

* Справочник
* Обновлено 17 мая 2022 г.

Этот API устарел. Используйте вместо него [Access tokens API](/managed/dynatrace-api/environment-api/tokens-v2/api-tokens "Управление токенами аутентификации Dynatrace API.").

Обновляет указанный токен аутентификации Dynatrace API.

Этот запрос позволяет удалить любой токен, включая токены, которыми не владеет пользователь, владеющий токеном, используемым для аутентификации вызова.

|  |  |  |
| --- | --- | --- |
| DELETE | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/v1/tokens/{id}` |
| DELETE | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/v1/tokens/{id}` |

## Аутентификация

Для выполнения запроса необходим access token со scope `TenantTokenManagement`.

О том, как получить и использовать токен, см. [Токены и аутентификация](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Параметры

| Параметр | Тип | Описание | В | Обязательность |
| --- | --- | --- | --- | --- |
| id | string | ID удаляемого токена. Может быть как публичным идентификатором, так и секретом.  Вы не можете удалить токен, используемый для аутентификации запроса. | path | Обязательный |

## Ответ

### Коды ответа

| Код | Тип | Описание |
| --- | --- | --- |
| **204** | - | Успех |
| **400** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Неудача. Вы не можете удалить токен, используемый для аутентификации запроса. |
| **404** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Неудача. Запрошенный токен не найден. |
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

В этом примере запрос удаляет токен со значением ID **4e9f128e-04f9-4795-8b7c-3c14a5e885e4**. Код ответа **204** указывает, что удаление прошло успешно.

API-токен передаётся в заголовке **Authorization**.

#### Curl

```
curl -X DELETE \



https://mySampleEnv.live.dynatrace.com/api/v1/tokens/4e9f128e-04f9-4795-8b7c-3c14a5e885e4 \



-H 'Authorization: Api-Token dt0c01.abc123.abcdefjhij1234567890'
```

#### URL запроса

```
https://mySampleEnv.live.dynatrace.com/api/v1/tokens/4e9f128e-04f9-4795-8b7c-3c14a5e885e4
```

#### Код ответа

204