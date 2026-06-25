---
title: Events API v2 - GET свойства события
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/events-v2/get-event-property
scraped: 2026-05-12T12:01:03.699342
---

# Events API v2 - GET свойства события

# Events API v2 - GET свойства события

* Reference
* Published Oct 07, 2021

Возвращает подробности о свойстве события.

Запрос возвращает данные в формате `application/json`.

|  |  |  |
| --- | --- | --- |
| GET | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/v2/eventProperties/{propertyKey}` |
| GET | Environment and Cluster ActiveGate (default port 9999) | `https://{your-activegate-domain}:9999/e/{your-environment-id}/api/v2/eventProperties/{propertyKey}` |

## Аутентификация

Для выполнения запроса необходим access token со scope `events.read`.

О том, как получить и использовать токен, см. [Токены и аутентификация](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Параметры

| Параметр | Тип | Описание | В | Обязательность |
| --- | --- | --- | --- | --- |
| propertyKey | string | Ключ запрашиваемого свойства события. | path | Обязательный |

## Ответ

### Коды ответа

| Код | Тип | Описание |
| --- | --- | --- |
| **200** | [EventPropertyDetails](#openapi-definition-EventPropertyDetails) | Успех |
| **4XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Ошибка на стороне клиента. |
| **5XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Ошибка на стороне сервера. |

### Объекты тела ответа

#### Объект `EventPropertyDetails`

Конфигурация свойства события.

| Элемент | Тип | Описание |
| --- | --- | --- |
| description | string | Краткое описание свойства события. |
| displayName | string | Отображаемое имя свойства события. |
| filterable | boolean | Свойство можно (`true`) или нельзя (`false`) использовать для фильтрации в селекторе событий. Использование в селекторе событий: `property.<key>("value-1", "value-2")` |
| key | string | Ключ свойства события. |
| writable | boolean | Свойство можно (`true`) или нельзя (`false`) задавать при загрузке события. |

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



"displayName": "Custom description",



"filterable": true,



"key": "dt.event.description",



"writable": true



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

В этом примере запрос получает подробности о свойстве события **Custom source**.

API-токен передаётся в заголовке **Authorization**.

#### Curl

```
curl --request GET \



--url 'https://mySampleEnv.live.dynatrace.com/api/v2/eventProperties/dt.event.source' \



--header 'Authorization: Api-Token dt0c01.abc123.abcdefjhij1234567890'
```

#### URL запроса

```
https://mySampleEnv.live.dynatrace.com/api/v2/eventProperties/dt.event.source
```

#### Тело ответа

```
{



"key": "dt.event.source",



"displayName": "Custom source",



"description": "The name or ID of the external source of the event",



"writable": true



}
```

#### Код ответа

200

## Связанные темы

* [Анализ и корреляция событий](/managed/dynatrace-intelligence/root-cause-analysis/event-analysis-and-correlation "Получите представление о секции Events на каждой странице обзора хоста, процесса и сервиса.")