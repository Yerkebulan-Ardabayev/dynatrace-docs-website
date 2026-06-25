---
title: Events API v2 - GET всех свойств событий
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/events-v2/get-event-properties
scraped: 2026-05-12T11:12:13.267419
---

# Events API v2 - GET всех свойств событий

# Events API v2 - GET всех свойств событий

* Reference
* Published Oct 07, 2021

Выводит список всех свойств событий, которые предоставляет Dynatrace.

Запрос возвращает данные в формате `application/json`.

|  |  |  |
| --- | --- | --- |
| GET | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/v2/eventProperties` |
| GET | Environment and Cluster ActiveGate (default port 9999) | `https://{your-activegate-domain}:9999/e/{your-environment-id}/api/v2/eventProperties` |

## Аутентификация

Для выполнения запроса необходим access token со scope `events.read`.

О том, как получить и использовать токен, см. [Токены и аутентификация](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Параметры

| Параметр | Тип | Описание | В | Обязательность |
| --- | --- | --- | --- | --- |
| nextPageKey | string | Курсор для следующей страницы результатов. Его можно найти в поле **nextPageKey** предыдущего ответа.  Первая страница возвращается всегда, если параметр запроса **nextPageKey** не указан.  Когда **nextPageKey** задан для получения последующих страниц, все остальные query-параметры должны быть пропущены. | query | Опциональный |
| pageSize | integer | Количество свойств событий в одном теле ответа.  Максимально допустимый размер страницы 500.  Если не задано, используется 100. | query | Опциональный |

## Ответ

### Коды ответа

| Код | Тип | Описание |
| --- | --- | --- |
| **200** | [EventPropertiesList](#openapi-definition-EventPropertiesList) | Успех |
| **4XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Ошибка на стороне клиента. |
| **5XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Ошибка на стороне сервера. |

### Объекты тела ответа

#### Объект `EventPropertiesList`

Список свойств событий.

| Элемент | Тип | Описание |
| --- | --- | --- |
| eventProperties | [EventPropertyDetails[]](#openapi-definition-EventPropertyDetails) | Список свойств событий. |
| nextPageKey | string | Курсор для следующей страницы результатов. На последней странице имеет значение `null`.  Используйте его в параметре запроса **nextPageKey**, чтобы получить последующие страницы результата. |
| pageSize | integer | Количество записей на странице. |
| totalCount | integer | Общее количество записей в результате. |

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



"eventProperties": [



{



"description": "string",



"displayName": "Custom description",



"filterable": true,



"key": "dt.event.description",



"writable": true



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

В этом примере запрос выводит список всех доступных свойств событий, имеющихся в окружении **mySampleEnv**. Результат усечён до трёх записей.

API-токен передаётся в заголовке **Authorization**.

#### Curl

```
curl --request GET \



--url 'https://mySampleEnv.live.dynatrace.com/api/v2/eventProperties?pageSize=3' \



--header 'Authorization: Api-Token dt0c01.abc123.abcdefjhij1234567890'
```

#### URL запроса

```
https://mySampleEnv.live.dynatrace.com/api/v2/eventProperties?pageSize=3
```

#### Тело ответа

```
{



"totalCount": 23,



"pageSize": 3,



"nextPageKey": "AQAAAAMBAAAAAw==",



"eventProperties": [



{



"key": "dt.event.allow_davis_merge",



"displayName": "Allow Davis merge",



"description": "Allow Davis AI to merge this event into existing problems (true) or force creating a new problem (false)",



"writable": true



},



{



"key": "dt.event.baseline.service_method",



"displayName": "Baseline affected service method",



"description": "Lists affected service methods of the triggered service event",



"writable": false



},



{



"key": "dt.event.baseline.total_load",



"displayName": "Baseline total load",



"description": "The load (calls per minute) of the entire service or application for triggered event",



"writable": false



}



]



}
```

#### Код ответа

200

## Связанные темы

* [Анализ и корреляция событий](/managed/dynatrace-intelligence/root-cause-analysis/event-analysis-and-correlation "Получите представление о секции Events на каждой странице обзора хоста, процесса и сервиса.")