---
title: RUM JavaScript API - GET configured RUM JavaScript versions
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/rum/real-user-monitoring-javascript-code/get-configured-rum-javascript-versions
scraped: 2026-05-12T11:56:01.432277
---

# RUM JavaScript API - GET configured RUM JavaScript versions

# RUM JavaScript API - GET configured RUM JavaScript versions

* Reference
* Published Apr 15, 2025

Возвращает настроенные в окружении последнюю стабильную, предыдущую стабильную и пользовательскую версии RUM JavaScript.

|  |  |  |
| --- | --- | --- |
| GET | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/v1/rum/jsConfiguredVersions` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/v1/rum/jsConfiguredVersions` |

## Аутентификация

Для выполнения запроса необходим access token со scope `RumJavaScriptTagManagement`.

О том, как получить и использовать токен, см. [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Параметры

Запрос не предоставляет настраиваемых параметров.

## Ответ

### Коды ответа

| Код | Тип | Описание |
| --- | --- | --- |
| **200** | [ConfiguredVersions](#openapi-definition-ConfiguredVersions) | Успех |
| **4XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Ошибка на стороне клиента. |
| **5XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Ошибка на стороне сервера. |

### Объекты тела ответа

#### Объект `ConfiguredVersions`

Настроенные версии RUM JavaScript LATEST\_STABLE, PREVIOUS\_STABLE и CUSTOM.

| Элемент | Тип | Описание |
| --- | --- | --- |
| custom | integer | Пользовательская настроенная версия RUM JavaScript. |
| latestIE11Supported | integer | Последняя версия RUM JavaScript с поддержкой IE11. |
| latestIESupported | integer | Последняя версия RUM JavaScript с поддержкой IE7-10. |
| latestStable | integer | Последняя стабильная версия RUM JavaScript. |
| previousStable | integer | Предыдущая стабильная версия RUM JavaScript. |

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



"latestStable": 10156181011154334,



"previousStable": 10156181011154332,



"latestIESupported": 10155181011154332,



"custom": 10156181011154330



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

В этом примере запрос запрашивает настроенные в окружении версии RUM JavaScript.

API-токен передаётся в заголовке **Authorization**.

#### Curl

```
curl -X GET \



https://mySampleEnv.live.dynatrace.com/api/v1/rum/jsConfiguredVersions \



-H 'Authorization: Api-Token dt0c01.abc123.abcdefjhij1234567890'
```

#### URL запроса

```
https://mySampleEnv.live.dynatrace.com/api/v1/rum/jsConfiguredVersions
```

#### Тело ответа

```
{



"latestStable": 10156181011154334,



"previousStable": 10156181011154332,



"latestIESupported": 10155181011154332,



"custom": 10156181011154330



}
```

#### Код ответа

200