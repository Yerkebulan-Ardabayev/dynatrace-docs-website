---
title: Metric units API - GET единица
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/metrics-units/get-unit
scraped: 2026-05-12T11:11:49.691997
---

# Metric units API - GET единица

# Metric units API - GET единица

* Справочник
* Опубликовано 11 февраля 2022 г.

Получает свойства единицы измерения метрики.

Запрос возвращает payload в формате `application/json`.

|  |  |  |
| --- | --- | --- |
| GET | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/v2/units/{unitId}` |
| GET | Environment and Cluster ActiveGate (default port 9999) | `https://{your-activegate-domain}:9999/e/{your-environment-id}/api/v2/units/{unitId}` |

## Аутентификация

Для выполнения запроса нужен access-токен со scope `metrics.read`.

О том, как получить и использовать токен, смотрите [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Параметры

| Параметр | Тип | Описание | В | Обязательный |
| --- | --- | --- | --- | --- |
| unitId | string | ID требуемой единицы. | path | Обязательный |

## Ответ

### Коды ответа

| Код | Тип | Описание |
| --- | --- | --- |
| **200** | [Unit](#openapi-definition-Unit) | Успех |
| **404** | - | Не найдено. Запрашиваемый ресурс не найден или запрос некорректен. |
| **4XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Ошибка на стороне клиента. |
| **5XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Ошибка на стороне сервера. |

### Объекты тела ответа

#### Объект `Unit`

Метаданные единицы.

| Элемент | Тип | Описание |
| --- | --- | --- |
| description | string | Краткое описание единицы. |
| displayName | string | Отображаемое имя единицы. |
| displayNamePlural | string | Отображаемое имя единицы во множественном числе. |
| symbol | string | Символ единицы. |
| unitId | string | ID единицы. |

### JSON-модели тела ответа

```
{



"description": "The second is the base unit of time and defined as 1/86400 of a day.",



"displayName": "second",



"displayNamePlural": "seconds",



"symbol": "s",



"unitId": "Second"



}
```

## Пример

В этом примере запрос получает метаданные единицы **Ratio**.

API-токен передаётся в заголовке **Authorization**.

#### Curl

```
curl --request GET \



--url https://mySampleEnv.live.dynatrace.com//api/v2/units/MebiByte \



--header 'Authorization: Api-Token dt0c01.abc123.abcdefjhij1234567890'
```

#### URL запроса

```
https://mySampleEnv.live.dynatrace.com//api/v2/units/MebiByte
```

#### Тело ответа

```
{



"unitId": "MebiByte",



"displayName": "mebibyte",



"symbol": "MiB",



"description": "1048576.0 byte"



}
```

#### Код ответа

200