---
title: RUM JavaScript API - GET list of injected applications
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/rum/real-user-monitoring-javascript-code/get-list-injected-applications
scraped: 2026-05-12T11:56:05.190452
---

# RUM JavaScript API - GET list of injected applications

# RUM JavaScript API - GET list of injected applications

* Reference
* Updated on May 02, 2022

Выводит список всех ваших приложений с ручным внедрением вместе с их метаданными.

Запрос возвращает данные в формате `application/json`.

|  |  |  |
| --- | --- | --- |
| GET | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/v1/rum/manualApps` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/v1/rum/manualApps` |

## Аутентификация

Для выполнения запроса необходим access token со scope `RumJavaScriptTagManagement`.

О том, как получить и использовать токен, см. [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Параметры

Запрос не предоставляет настраиваемых параметров.

## Ответ

### Коды ответа

| Код | Тип | Описание |
| --- | --- | --- |
| **200** | [ManualApplication[]](#openapi-definition-ManualApplication) | Успех |
| **4XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Ошибка на стороне клиента. |
| **5XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Ошибка на стороне сервера. |

### Объекты тела ответа

#### Объект `ResponseBody`

#### Объект `ManualApplication`

Параметры приложения с ручным внедрением.

| Элемент | Тип | Описание |
| --- | --- | --- |
| applicationId | string | ID сущности Dynatrace приложения. |
| displayName | string | Имя приложения. |
| monitoringEnabled | boolean | Мониторинг включён (`true`) или отключён (`false`). |
| revision | string | Ревизия настроек приложения. |

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
[



{



"applicationId": "APPLICATION-C15B48CBCADC863B",



"displayName": "manually injected application",



"monitoringEnabled": true,



"revision": 1456380804910



}



]
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

В этом примере запрос запрашивает все приложения окружения с ручным внедрением

API-токен передаётся в заголовке **Authorization**.

Результат усечён до трёх записей.

#### Curl

```
curl -X GET \



https://mySampleEnv.live.dynatrace.com/api/v1/rum/manualApps \



-H 'Authorization: Api-Token dt0c01.abc123.abcdefjhij1234567890'
```

#### URL запроса

```
https://mySampleEnv.live.dynatrace.com/api/v1/rum/manualApps
```

#### Тело ответа

```
[



{



"applicationId": "APPLICATION-BBFA55551D507E2B",



"displayName": "easyTravel Ionic Web",



"monitoringEnabled": true,



"revision": 1539076354681



},



{



"applicationId": "APPLICATION-31F18E1B2C50038A",



"displayName": "SaaS App Monitoring",



"monitoringEnabled": true,



"revision": 1536827568615



},



{



"applicationId": "APPLICATION-AE767ECC2D7B33BF",



"displayName": "Node JS demo",



"monitoringEnabled": true,



"revision": 1536827567516



}



]
```

#### Код ответа

200