---
title: RUM JavaScript API - GET available RUM JavaScript versions
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/rum/real-user-monitoring-javascript-code/get-available-rum-javascript-versions
scraped: 2026-05-12T11:55:55.655378
---

# RUM JavaScript API - GET available RUM JavaScript versions

# RUM JavaScript API - GET available RUM JavaScript versions

* Reference
* Published Apr 15, 2025

Получить список всех версий RUM JavaScript, доступных в окружении.

|  |  |  |
| --- | --- | --- |
| GET | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/v1/rum/jsAllAvailableVersions` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/v1/rum/jsAllAvailableVersions` |

## Аутентификация

Для выполнения запроса необходим access token со scope `RumJavaScriptTagManagement`.

О том, как получить и использовать токен, см. [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Параметры

Запрос не предоставляет настраиваемых параметров.

## Ответ

### Коды ответа

| Код | Тип | Описание |
| --- | --- | --- |
| **200** | [AllAvailableVersions](#openapi-definition-AllAvailableVersions) | Успех |
| **4XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Ошибка на стороне клиента. |
| **5XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Ошибка на стороне сервера. |

### Объекты тела ответа

#### Объект `AllAvailableVersions`

Все доступные версии RUM JavaScript

| Элемент | Тип | Описание |
| --- | --- | --- |
| versions | integer[] | Список доступных версий RUM JavaScript |

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
| parameterLocation | string | -Возможные значения: * `HEADER` * `PATH` * `PAYLOAD_BODY` * `QUERY` |
| path | string | - |

### JSON-модели тела ответа

```
{



"versions": [



10158181011154332,



10156181011154332,



10154181011154334,



10152181011154336



]



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

В этом примере запрос запрашивает доступные версии RUM JavaScript.

API-токен передаётся в заголовке **Authorization**.

#### Curl

```
curl -X GET \



https://mySampleEnv.live.dynatrace.com/api/v1/rum/jsAllAvailableVersions \



-H 'Authorization: Api-Token dt0c01.abc123.abcdefjhij1234567890'
```

#### URL запроса

```
https://mySampleEnv.live.dynatrace.com/api/v1/rum/jsAllAvailableVersions
```

#### Тело ответа

```
{



"versions": [



10158181011154332,



10156181011154332,



10154181011154334,



10152181011154336



]



}
```

#### Код ответа

200