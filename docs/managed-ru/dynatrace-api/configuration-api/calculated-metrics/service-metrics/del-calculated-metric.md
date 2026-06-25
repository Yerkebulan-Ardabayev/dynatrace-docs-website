---
title: Service metrics API - DELETE a metric
source: https://docs.dynatrace.com/managed/dynatrace-api/configuration-api/calculated-metrics/service-metrics/del-calculated-metric
scraped: 2026-05-12T11:15:55.235200
---

# Service metrics API - DELETE a metric

# Service metrics API - DELETE a metric

* Reference
* Published Dec 16, 2019

Удаляет указанную вычисляемую метрику сервиса. Удаление невозможно отменить!

|  |  |  |
| --- | --- | --- |
| DELETE | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/config/v1/calculatedMetrics/service/{metricKey}` |
| DELETE | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/config/v1/calculatedMetrics/service/{metricKey}` |

## Аутентификация

Для выполнения этого запроса нужен access token со scope `WriteConfig`.

Как его получить и использовать, смотрите [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Параметры

| Параметр | Тип | Описание | Где | Обязательный |
| --- | --- | --- | --- | --- |
| metricKey | string | Ключ вычисляемой метрики сервиса, которую нужно удалить. | path | Required |

## Ответ

### Коды ответа

| Код | Описание |
| --- | --- |
| **204** | Успех. Вычисляемая метрика сервиса удалена. Ответ без тела. |

## Пример

В этом примере запрос удаляет вычисляемую метрику сервиса **Requests by code**, созданную в примере [POST request example](/managed/dynatrace-api/configuration-api/calculated-metrics/service-metrics/post-calculated-metric#example "Создание вычисляемой метрики сервиса через Dynatrace API.").

API-токен передаётся в заголовке **Authorization**.

Код ответа **204** означает, что обновление прошло успешно.

#### Curl

```
curl -X DELETE \



https://mySampleEnv.live.dynatrace.com/api/config/v1/calculatedMetrics/service/calc:service.requestsbycode \



-H 'Authorization: Api-Token dt0c01.abc123.abcdefjhij1234567890'
```

#### URL запроса

```
https://mySampleEnv.live.dynatrace.com/api/config/v1/calculatedMetrics/service/calc:service.requestsbycode
```

#### Код ответа

204

## Связанные темы

* [Вычисляемые метрики для сервисов](/managed/observe/application-observability/services/calculated-service-metric "Узнайте, как создать вычисляемую метрику на основе веб-запросов.")
* [Многомерный анализ](/managed/observe/application-observability/multidimensional-analysis "Настройте представление многомерного анализа и сохраните его как вычисляемую метрику.")