---
title: Events API v2 - GET всех типов событий
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/events-v2/get-event-types
scraped: 2026-05-12T11:12:42.431255
---

# Events API v2 - GET всех типов событий

# Events API v2 - GET всех типов событий

* Reference
* Published Aug 06, 2021

Выводит список всех типов событий, которые могут возникнуть в вашем окружении.

Запрос возвращает данные в формате `application/json`.

|  |  |  |
| --- | --- | --- |
| GET | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/v2/eventTypes` |
| GET | Environment and Cluster ActiveGate (default port 9999) | `https://{your-activegate-domain}:9999/e/{your-environment-id}/api/v2/eventTypes` |

## Аутентификация

Для выполнения запроса необходим access token со scope `events.read`.

О том, как получить и использовать токен, см. [Токены и аутентификация](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Параметры

| Параметр | Тип | Описание | В | Обязательность |
| --- | --- | --- | --- | --- |
| nextPageKey | string | Курсор для следующей страницы результатов. Его можно найти в поле **nextPageKey** предыдущего ответа.  Первая страница возвращается всегда, если параметр запроса **nextPageKey** не указан.  Когда **nextPageKey** задан для получения последующих страниц, все остальные query-параметры должны быть пропущены. | query | Опциональный |
| pageSize | integer | Количество типов событий в одном теле ответа.  Максимально допустимый размер страницы 500.  Если не задано, используется 100. | query | Опциональный |

## Ответ

### Коды ответа

| Код | Тип | Описание |
| --- | --- | --- |
| **200** | [EventTypeList](#openapi-definition-EventTypeList) | Успех |
| **4XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Ошибка на стороне клиента. |
| **5XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Ошибка на стороне сервера. |

### Объекты тела ответа

#### Объект `EventTypeList`

Список типов событий.

| Элемент | Тип | Описание |
| --- | --- | --- |
| eventTypeInfos | [EventType[]](#openapi-definition-EventType) | Список типов событий. |
| nextPageKey | string | Курсор для следующей страницы результатов. На последней странице имеет значение `null`.  Используйте его в параметре запроса **nextPageKey**, чтобы получить последующие страницы результата. |
| pageSize | integer | Количество записей на странице. |
| totalCount | integer | Общее количество записей в результате. |

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



"eventTypeInfos": [



{



"description": "string",



"displayName": "High CPU",



"severityLevel": "PERFORMANCE",



"type": "OSI_HIGH_CPU"



}



],



"nextPageKey": "AQAAABQBAAAABQ==",



"pageSize": 1,



"totalCount": 1



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

В этом примере запрос выводит список всех типов событий, которые могут быть созданы в окружении **mySampleEnv**. Результат усечён до трёх записей.

API-токен передаётся в заголовке **Authorization**.

#### Curl

```
curl --request GET \



--url 'https://mySampleEnv.live.dynatrace.com/api/v2/eventTypes?pageSize=3' \



--header 'Authorization: Api-Token dt0c01.abc123.abcdefjhij1234567890'
```

#### URL запроса

```
https://mySampleEnv.live.dynatrace.com/api/v2/eventTypes?pageSize=3
```

#### Тело ответа

```
{



"totalCount": 144,



"pageSize": 3,



"nextPageKey": "AQAAAGQBAAAAZA==",



"eventTypeInfos": [



{



"type": "APPLICATION_UNEXPECTED_LOW_LOAD",



"displayName": "Application low traffic",



"severityLevel": "AVAILABILITY",



"description": "Unexpected low traffic"



},



{



"type": "MOBILE_APP_CRASH_RATE_INCREASED",



"displayName": "Mobile app crash rate increase",



"severityLevel": "ERROR"



},



{



"type": "APPLICATION_SLOWDOWN",



"displayName": "Application slowdown",



"severityLevel": "PERFORMANCE",



"description": "User action duration degradation"



}



]



}
```

#### Код ответа

200

## Связанные темы

* [Категории событий](/managed/dynatrace-intelligence/root-cause-analysis/event-analysis-and-correlation/event-categories "Узнайте о различных категориях событий и поддерживаемых типах событий, об их уровнях серьёзности и логике их порождения.")
* [Анализ и корреляция событий](/managed/dynatrace-intelligence/root-cause-analysis/event-analysis-and-correlation "Получите представление о секции Events на каждой странице обзора хоста, процесса и сервиса.")