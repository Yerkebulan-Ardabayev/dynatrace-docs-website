---
title: Metrics API - DELETE принятую метрику
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/metric-v2/delete-metric
scraped: 2026-05-12T11:13:52.846153
---

# Metrics API - DELETE принятую метрику

# Metrics API - DELETE принятую метрику

* Справочник
* Обновлено 22 января 2026 г.

Удаляет указанную [ingested metric](/managed/ingest-from/extend-dynatrace/extend-metrics "Узнайте, как расширить наблюдаемость метрик в Dynatrace.").

* Можно удалять только метрики, принятые через Metrics v2 API.
* Нельзя удалить метрику, если у неё есть точки данных, принятые за последние два часа.
* Удалённые метрики восстановить нельзя.

|  |  |  |
| --- | --- | --- |
| DELETE | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/v2/metrics/{metricKey}` |
| DELETE | Environment и Cluster ActiveGate (порт по умолчанию 9999) | `https://{your-activegate-domain}:9999/e/{your-environment-id}/api/v2/metrics/{metricKey}` |

## Аутентификация

Для выполнения запроса нужен access-токен со scope `metrics.write`.

О том, как получить и использовать токен, смотрите [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Параметры

| Параметр | Тип | Описание | В | Обязательный |
| --- | --- | --- | --- | --- |
| metricKey | string | Ключ требуемой метрики. | path | Обязательный |

## Ответ

### Коды ответа

| Код | Тип | Описание |
| --- | --- | --- |
| **202** | - | Успех. Удаление метрики запущено. |
| **400** | - | Неудача. Метрика записывалась в течение последних двух часов. |
| **404** | - | Неудача. Метрика не найдена или ключ не удалось разобрать. |
| **500** | - | Неудача. Не удалось удалить измерения метрики. |
| **4XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Ошибка на стороне клиента. |
| **5XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Ошибка на стороне сервера. |

## Пример

В этом примере запрос удаляет метрику **cpu.temperature**. Код ответа **202** означает, что удаление успешно запущено.

API-токен передаётся в заголовке **Authorization**.

#### Curl

```
curl --request DELETE \



--url https://mySampleEnv.live.dynatrace.com/api/v2/metrics/cpu.temperature \



--header 'Authorization: Api-Token dt0c01.abc123.abcdefjhij1234567890'
```

#### URL запроса

```
https://mySampleEnv.live.dynatrace.com/api/v2/metrics/cpu.temperature
```

#### Код ответа

202

## Связанные темы

* [Extend metric observability](/managed/ingest-from/extend-dynatrace/extend-metrics "Узнайте, как расширить наблюдаемость метрик в Dynatrace.")