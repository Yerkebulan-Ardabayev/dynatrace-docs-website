---
title: Tenant tokens API - POST отмена ротации
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/tokens-v2/tenant-tokens/post-cancel
scraped: 2026-05-12T12:01:17.132002
---

# Tenant tokens API - POST отмена ротации

# Tenant tokens API - POST отмена ротации

* Reference
* Published Feb 23, 2021

Отменяет ротацию tenant-токена. Новый токен отбрасывается, а старый токен остаётся действительным. Если вы [настроили](/managed/manage/identity-access-management/access-tokens-and-oauth-clients/access-tokens/rotate-tenant-token "Что такое tenant-токен и как его изменить.") какие-либо OneAgent и ActiveGate на использование нового токена, необходимо восстановить старую конфигурацию.

Запрос возвращает данные в формате `application/json`.

|  |  |  |
| --- | --- | --- |
| POST | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/v2/tenantTokenRotation/cancel` |
| POST | Environment and Cluster ActiveGate (default port 9999) | `https://{your-activegate-domain}:9999/e/{your-environment-id}/api/v2/tenantTokenRotation/cancel` |

## Аутентификация

Для выполнения запроса необходим access token со scope `tenantTokenRotation.write`.

О том, как получить и использовать токен, см. [Токены и аутентификация](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Параметры

Запрос не имеет настраиваемых параметров.

## Ответ

### Коды ответа

| Код | Тип | Описание |
| --- | --- | --- |
| **200** | [TenantTokenConfig](#openapi-definition-TenantTokenConfig) | Успех. Процесс ротации отменён. Текущий tenant-токен остаётся действительным. |
| **400** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Неудача. Активного процесса ротации нет. |
| **4XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Ошибка на стороне клиента. |
| **5XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Ошибка на стороне сервера. |

### Объекты тела ответа

#### Объект `TenantTokenConfig`

Конфигурация [tenant-токена](https://dt-url.net/b403ss9?dt=m).

| Элемент | Тип | Описание |
| --- | --- | --- |
| active | [TenantToken](#openapi-definition-TenantToken) | Tenant-токен |
| old | [TenantToken](#openapi-definition-TenantToken) | Tenant-токен |

#### Объект `TenantToken`

Tenant-токен

| Элемент | Тип | Описание |
| --- | --- | --- |
| value | string | Секрет tenant-токена. |

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



"active": {



"value": "string"



},



"old": {}



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

В этом примере запрос отменяет процесс ротации, запущенный в [примере запроса start](/managed/dynatrace-api/environment-api/tokens-v2/tenant-tokens/post-start#example "Запуск ротации tenant-токена Dynatrace.").

Код ответа **200** указывает на успешный запрос. Старый токен **1234567890qrstuvwxyz** остаётся действительным, новый токен отбрасывается.

API-токен передаётся в заголовке **Authorization**.

#### Curl

```
curl -X POST \



https://mySampleEnv.live.dynatrace.com/api/v2/tenantTokenRotation/finish \



-H 'Authorization: Api-Token dt0c01.abc123.abcdefjhij1234567890' \



-H 'Accept: application/json'
```

#### Тело ответа

```
{



"active": {



"value": "1234567890qrstuvwxyz"



},



"old": {



"value": null



}



}
```

#### Код ответа

200

## Связанные темы

* [Tenant token](/managed/manage/identity-access-management/access-tokens-and-oauth-clients/access-tokens/rotate-tenant-token "Что такое tenant-токен и как его изменить.")