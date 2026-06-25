---
title: Network zones API - PUT global configuration
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/network-zones/put-global-config
scraped: 2026-05-12T11:52:18.691610
---

# Network zones API - PUT global configuration

# Network zones API - PUT global configuration

* Reference
* Published Apr 20, 2020

Обновляет глобальную конфигурацию network zones в вашем окружении.

Запрос принимает payload `application/json`.

|  |  |
| --- | --- |
| PUT | * SaaS https://{your-environment-id}.live.dynatrace.com/api/v2/networkZoneSettings |

## Аутентификация

Для выполнения этого запроса нужно разрешение **Write network zones** (`networkZones.write`), назначенное вашему API-токену. Как его получить и использовать, смотрите [Authentication](/managed/dynatrace-api/basics/dynatrace-api-authentication "Узнайте, как аутентифицироваться для использования Dynatrace API.").

## Параметры

| Параметр | Тип | Описание | Где | Обязательный |
| --- | --- | --- | --- | --- |
| body | [NetworkZoneSettings](#openapi-definition-NetworkZoneSettings) | JSON-тело запроса. Содержит глобальную конфигурацию network zones. | body | Required |

### Объекты тела запроса

#### Объект `NetworkZoneSettings`

Глобальная конфигурация network zone.

| Элемент | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| networkZonesEnabled | boolean | Функция network zones включена (`true`) или выключена (`false`). | Optional |

### JSON-модель тела запроса

Это модель тела запроса, показывающая возможные элементы. Её нужно адаптировать под реальный запрос.

```
{



"networkZonesEnabled": true



}
```

## Ответ

### Коды ответа

| Код | Тип | Описание |
| --- | --- | --- |
| **204** | - | Успех. Глобальная конфигурация network zones обновлена. Ответ без тела. |
| **4XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Ошибка клиента. |
| **5XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Ошибка сервера. |

### Объекты тела ответа

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