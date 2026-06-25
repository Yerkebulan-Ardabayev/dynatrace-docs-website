---
title: Network zones API - GET global configuration
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/network-zones/get-global-config
scraped: 2026-05-12T11:59:41.355643
---

# Network zones API - GET global configuration

# Network zones API - GET global configuration

* Reference
* Published Mar 05, 2020

Получает глобальную конфигурацию network zones в вашем окружении.

Запрос возвращает payload `application/json`.

|  |  |
| --- | --- |
| GET | * SaaS https://{your-environment-id}.live.dynatrace.com/api/v2/networkZoneSettings |

## Аутентификация

Для выполнения этого запроса нужно разрешение **Read network zones** (`networkZones.read`), назначенное вашему API-токену. Как его получить и использовать, смотрите [Authentication](/managed/dynatrace-api/basics/dynatrace-api-authentication "Узнайте, как аутентифицироваться для использования Dynatrace API.").

## Параметры

В запросе нет настраиваемых параметров.

## Ответ

### Коды ответа

| Код | Тип | Описание |
| --- | --- | --- |
| **200** | [NetworkZoneSettings](#openapi-definition-NetworkZoneSettings) | Успех |
| **4XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Ошибка клиента. |
| **5XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Ошибка сервера. |

### Объекты тела ответа

#### Объект `NetworkZoneSettings`

Глобальная конфигурация network zone.

| Элемент | Тип | Описание |
| --- | --- | --- |
| networkZonesEnabled | boolean | Функция network zones включена (`true`) или выключена (`false`). |

#### Объект `ErrorEnvelope`

| Элемент | Тип | Описание |
| --- | --- | --- |
| error | [Error](#openapi-definition-Error) | - |

#### Объект `Error`

| Элемент | Тип | Описание |
| --- | --- | --- |
| code | integer | HTTP-код состояния. |
| constraintViolations | [ConstraintViolation[]](#openapi-definition-ConstraintViolation) | Список нарушений ограничений. |
| message | string | Сообщение об ошибке. |

#### Объект `ConstraintViolation`

Список нарушений ограничений.

| Элемент | Тип | Описание |
| --- | --- | --- |
| location | string | - |
| message | string | - |
| parameterLocation | string | -Элемент может принимать значения * `HEADER` * `PATH` * `PAYLOAD_BODY` * `QUERY` |
| path | string | - |

### JSON-модели тела ответа

```
{



"networkZonesEnabled": true



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

## Связанные темы

* [Network zones](/managed/manage/network-zones "Узнайте, как работают network zones в Dynatrace.")