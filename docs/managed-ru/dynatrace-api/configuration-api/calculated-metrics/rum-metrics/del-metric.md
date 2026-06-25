---
title: Web application metrics API - DELETE a metric
source: https://docs.dynatrace.com/managed/dynatrace-api/configuration-api/calculated-metrics/rum-metrics/del-metric
scraped: 2026-05-12T11:17:51.663120
---

# Web application metrics API - DELETE a metric

# Web application metrics API - DELETE a metric

* Reference
* Published Feb 28, 2020

Удаляет указанную вычисляемую метрику веб-приложения. Удаление невозможно отменить!

|  |  |  |
| --- | --- | --- |
| DELETE | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/config/v1/calculatedMetrics/rum/{metricKey}` |
| DELETE | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/config/v1/calculatedMetrics/rum/{metricKey}` |

## Аутентификация

Для выполнения этого запроса нужен access token со scope `WriteConfig`.

Как его получить и использовать, смотрите [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Параметры

| Параметр | Тип | Описание | Где | Обязательный |
| --- | --- | --- | --- | --- |
| metricKey | string | Ключ метрики, которую нужно удалить. | path | Required |

## Ответ

### Коды ответа

| Код | Описание |
| --- | --- |
| **204** | Удалено. Ответ без тела. |

## Связанные темы

* [Создание вычисляемых метрик для веб-приложений](/managed/observe/digital-experience/web-applications/additional-configuration/rum-calculated-metrics-web "Создание вычисляемых метрик, а также пользовательских графиков на основе вычисляемых метрик для ваших веб-приложений.")