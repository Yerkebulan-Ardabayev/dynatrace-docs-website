---
title: Metrics API - DELETE принятые метрики
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/metric-v2/delete-metrics
scraped: 2026-05-12T11:27:53.271624
---

# Metrics API - DELETE принятые метрики

# Metrics API - DELETE принятые метрики

* Справочник
* Опубликовано 16 января 2026 г.

Dynatrace версии 1.330+

Удаляет [ingested metrics](/managed/ingest-from/extend-dynatrace/extend-metrics "Узнайте, как расширить наблюдаемость метрик в Dynatrace."), которые старше указанного количества дней.

* Можно удалять только метрики, принятые через Metrics v2 API.
* Удалённые метрики восстановить нельзя.

|  |  |  |
| --- | --- | --- |
| DELETE | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/v2/metrics` |
| DELETE | Environment и Cluster ActiveGate (порт по умолчанию 9999) | `https://{your-activegate-domain}:9999/e/{your-environment-id}/api/v2/metrics` |

## Аутентификация

Для выполнения запроса нужен access-токен со scope `metrics.write`.

О том, как получить и использовать токен, смотрите [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Параметры

| Параметр | Тип | Описание | В | Обязательный |
| --- | --- | --- | --- | --- |
| metricSelector | string | Выбирает метрики, рассматриваемые для удаления.  Полный набор связанных метрик можно выбрать с помощью завершающего символа подстановки звёздочки (`*`). Например, `airflow_*` выбирает все пользовательские метрики airflow, `*` выбирает все пользовательские метрики. | query | Обязательный |
| minUnusedDays | integer | Количество дней с момента последнего использования метрики. Должно быть между `30` и `1825` (5 лет). | query | Обязательный |

## Ответ

### Коды ответа

| Код | Тип | Описание |
| --- | --- | --- |
| **202** | - | Успех. Удаление метрик запущено. |
| **400** | - | Неудача. |
| **500** | - | Неудача. Не удалось выполнить массовое удаление. |
| **4XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Ошибка на стороне клиента. |
| **5XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Ошибка на стороне сервера. |

## Пример

В этом примере запрос удаляет все метрики, которые не записывались за последние 60 дней:

```
DELETE /api/v2/metrics?metricSelector=<your-selector>&minUnusedDays=60
```

## Связанные темы

* [Extend metric observability](/managed/ingest-from/extend-dynatrace/extend-metrics "Узнайте, как расширить наблюдаемость метрик в Dynatrace.")