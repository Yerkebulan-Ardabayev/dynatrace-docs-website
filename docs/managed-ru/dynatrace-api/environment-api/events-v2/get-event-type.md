---
title: Events API v2 - GET типа события
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/events-v2/get-event-type
scraped: 2026-05-12T12:00:59.547632
---

# Events API v2 - GET типа события

# Events API v2 - GET типа события

* Reference
* Published Aug 06, 2021

Возвращает свойства типа события.

Запрос возвращает данные в формате `application/json`.

|  |  |  |
| --- | --- | --- |
| GET | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/v2/eventTypes/{eventType}` |
| GET | Environment and Cluster ActiveGate (default port 9999) | `https://{your-activegate-domain}:9999/e/{your-environment-id}/api/v2/eventTypes/{eventType}` |

## Аутентификация

Для выполнения запроса необходим access token со scope `events.read`.

О том, как получить и использовать токен, см. [Токены и аутентификация](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Параметры

| Параметр | Тип | Описание | В | Обязательность |
| --- | --- | --- | --- | --- |
| eventType | string | Запрашиваемый тип события. | path | Обязательный |

## Ответ

### Коды ответа

| Код | Тип | Описание |
| --- | --- | --- |
| **200** | [EventType](#openapi-definition-EventType) | Успех |
| **4XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Ошибка на стороне клиента. |
| **5XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Ошибка на стороне сервера. |

### Объекты тела ответа

#### Объект `EventType`

Конфигурация типа события.

| Элемент | Тип | Описание |
| --- | --- | --- |
| description | string | Краткое описание типа события. |
| displayName | string | Отображаемое имя типа события. |
| severityLevel | string | Уровень серьёзности, связанный с типом события. Элемент может принимать значения * `AVAILABILITY` * `CUSTOM_ALERT` * `ERROR` * `INFO` * `MONITORING_UNAVAILABLE` * `PERFORMANCE` * `RESOURCE_CONTENTION` |
| type | string | Тип события. |

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



"description": "string",



"displayName": "High CPU",



"severityLevel": "PERFORMANCE",



"type": "OSI_HIGH_CPU"



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

В этом примере запрос получает свойства типа **APPLICATION\_SLOWDOWN**.

API-токен передаётся в заголовке **Authorization**.

#### Curl

```
curl --request GET \



--url 'https://mySampleEnv.live.dynatrace.com/api/v2/eventTypes/APPLICATION_SLOWDOWN' \



--header 'Authorization: Api-Token dt0c01.abc123.abcdefjhij1234567890'
```

#### URL запроса

```
https://mySampleEnv.live.dynatrace.com/api/v2/eventTypes/APPLICATION_SLOWDOWN
```

#### Тело ответа

```
{



"type": "APPLICATION_SLOWDOWN",



"displayName": "Application slowdown",



"severityLevel": "PERFORMANCE",



"description": "User action duration degradation"



}
```

#### Код ответа

200

## Связанные темы

* [Категории событий](/managed/dynatrace-intelligence/root-cause-analysis/event-analysis-and-correlation/event-categories "Узнайте о различных категориях событий и поддерживаемых типах событий, об их уровнях серьёзности и логике их порождения.")
* [Анализ и корреляция событий](/managed/dynatrace-intelligence/root-cause-analysis/event-analysis-and-correlation "Получите представление о секции Events на каждой странице обзора хоста, процесса и сервиса.")