---
title: Third-party synthetic API - POST сторонние события в Dynatrace
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/synthetic/third-party-synthetic/post-third-party-events
scraped: 2026-05-12T11:54:36.809237
---

# Third-party synthetic API - POST сторонние события в Dynatrace

# Third-party synthetic API - POST сторонние события в Dynatrace

* Справочник
* Опубликовано 15 мая 2020 г.

Отправляет информацию о сторонних синтетических событиях в Dynatrace.

Запрос принимает payload в формате `application/json`.

|  |  |  |
| --- | --- | --- |
| POST | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/v1/synthetic/ext/events` |
| POST | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/v1/synthetic/ext/events` |

## Аутентификация

Для выполнения запроса нужен access-токен со scope `ExternalSyntheticIntegration`.

О том, как получить и использовать токен, смотрите [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Параметры

| Параметр | Тип | Описание | В | Обязательный |
| --- | --- | --- | --- | --- |
| body | [3rdPartySyntheticEvents](#openapi-definition-3rdPartySyntheticEvents) | JSON-тело запроса. Содержит сторонние синтетические события. | body | Обязательный |

### Объекты тела запроса

#### Объект `3rdPartySyntheticEvents`

Список сторонних синтетических событий.

| Поле | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| open | [3rdPartyEventOpenNotification[]](#openapi-definition-3rdPartyEventOpenNotification) | Список открытых сторонних синтетических событий. | Необязательный |
| resolved | [3rdPartyEventResolvedNotification[]](#openapi-definition-3rdPartyEventResolvedNotification) | Список закрытых сторонних синтетических событий. | Необязательный |
| syntheticEngineName | string | Тип стороннего синтетического монитора. | Обязательный |

#### Объект `3rdPartyEventOpenNotification`

Открытое стороннее синтетическое событие.

| Поле | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| eventId | string | Уникальный ID события. | Обязательный |
| eventType | string | Тип события. Поле может принимать значения: * `testOutage` * `testSlowdown` | Обязательный |
| locationIds | string[] | Список ID сторонних синтетических локаций, где происходит событие. | Обязательный |
| name | string | Имя события. | Обязательный |
| reason | string | Причина события. | Обязательный |
| startTimestamp | integer | Метка времени начала события, в миллисекундах UTC. | Обязательный |
| testId | string | ID стороннего синтетического монитора. | Обязательный |

#### Объект `3rdPartyEventResolvedNotification`

Закрытое стороннее синтетическое событие.

| Поле | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| endTimestamp | integer | Метка времени окончания события, в миллисекундах UTC. | Обязательный |
| eventId | string | Уникальный ID события. | Обязательный |
| testId | string | ID стороннего синтетического монитора. | Обязательный |

### JSON-модель тела запроса

Это модель тела запроса, показывающая возможные поля. Её нужно скорректировать для использования в реальном запросе.

```
{



"open": [



{



"eventId": "string",



"eventType": "testOutage",



"locationIds": [



"string"



],



"name": "string",



"reason": "string",



"startTimestamp": 1,



"testId": "string"



}



],



"resolved": [



{



"endTimestamp": 1,



"eventId": "string",



"testId": "string"



}



],



"syntheticEngineName": "string"



}
```

## Ответ

### Коды ответа

| Код | Тип | Описание |
| --- | --- | --- |
| **204** | - | Успех. Информация принята и сохранена. |
| **400** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Не удалось. Входные данные недействительны. |
| **4XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Ошибка на стороне клиента. |
| **5XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Ошибка на стороне сервера. |

### Объекты тела ответа

#### Объект `ErrorEnvelope`

| Поле | Тип | Описание |
| --- | --- | --- |
| error | [Error](#openapi-definition-Error) | - |

#### Объект `Error`

| Поле | Тип | Описание |
| --- | --- | --- |
| code | integer | HTTP-код состояния |
| constraintViolations | [ConstraintViolation[]](#openapi-definition-ConstraintViolation) | Список нарушений ограничений |
| message | string | Сообщение об ошибке |

#### Объект `ConstraintViolation`

Список нарушений ограничений

| Поле | Тип | Описание |
| --- | --- | --- |
| location | string | - |
| message | string | - |
| parameterLocation | string | -Поле может принимать значения: * `HEADER` * `PATH` * `PAYLOAD_BODY` * `QUERY` |
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

## Обновление существующего стороннего монитора

Чтобы обновить существующий сторонний монитор, укажите его движок в поле **syntheticEngineName** объекта `3rdPartySyntheticTests` и его ID в поле **id** объекта `3rdPartySyntheticTest`.

Необходимо передать **все** параметры монитора. Не меняйте значения параметров, которые не нужно менять.

## Пример

В этом примере запрос добавляет событие **outage** к стороннему синтетическому монитору **example of synthetic monitor - 1** из [примера **POST third-party monitors to Dynatrace**](/managed/dynatrace-api/environment-api/synthetic/third-party-synthetic/post-third-party-monitors#example "Отправка сторонних синтетических мониторов в Dynatrace через Synthetic v1 API.").

API-токен передаётся в заголовке **Authorization**.

Можно скачать JSON тела запроса, чтобы выполнить пример запроса в вашем окружении. Обязательно замените метки времени на недавние, иначе результаты будут слишком старыми.

#### Curl

```
curl -X POST \



https://mySampleEnv.live.dynatrace.com/api/v1/synthetic/ext/events \



-H 'Authorization: Api-Token dt0c01.abc123.abcdefjhij1234567890' \



-H 'Content-Type: application/json' \



-d '{<truncated - see the Request body section below>}



'
```

#### URL запроса

```
https://mySampleEnv.live.dynatrace.com/api/v1/synthetic/ext/events
```

#### Тело запроса

```
{



"syntheticEngineName": "My third-party synthetic",



"open": [



{



"testId": "3rdPartySyntheticMonitor1",



"eventId": "extOpenEvent1-1",



"name": "example of  event",



"reason": "sample outage",



"eventType": "testOutage",



"locationIds": ["Linz1"],



"startTimestamp": 1543582285957



}



],



"resolved": []



}
```

#### Код ответа

204

#### Результат

Выделения показывают параметры, переданные в запросе.

![Внешнее синтетическое событие](https://dt-cdn.net/images/ext-monitor-event-1850-a94fba57bf.png)

Внешнее синтетическое событие