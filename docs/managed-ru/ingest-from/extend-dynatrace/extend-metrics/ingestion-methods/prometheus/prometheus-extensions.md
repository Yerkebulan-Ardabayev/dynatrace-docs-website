---
title: Расширения Prometheus
source: https://docs.dynatrace.com/managed/ingest-from/extend-dynatrace/extend-metrics/ingestion-methods/prometheus/prometheus-extensions
scraped: 2026-05-12T11:37:59.140301
---

# Расширения Prometheus

# Расширения Prometheus

* 5-min read
* Updated on Mar 16, 2023

Расширения Prometheus позволяют настроить сбор метрик с эндпоинтов Prometheus через пошаговый мастер в интерфейсе Dynatrace.

## Пошаговая настройка (6 шагов)

1. Перейдите в **Hub**, найдите расширение Prometheus и выберите **Set up**.
2. Выберите тип мониторинга: **Local** (локальный) или **Remote** (удалённый).
3. Укажите URL эндпоинта Prometheus.
4. Настройте дополнительные параметры (тайм-аут, количество повторных попыток).
5. Настройте автообнаружение, если необходимо.
6. Активируйте расширение.

## Локальный и удалённый мониторинг

* **Локальный** — сбор метрик с эндпоинтов на том же хосте, где запущен OneAgent.
* **Удалённый** — сбор метрик с удалённых эндпоинтов через ActiveGate.

## Расширенные свойства

| Свойство | Описание |
| --- | --- |
| Тайм-аут | Максимальное время ожидания ответа от эндпоинта |
| Количество повторных попыток | Число попыток при ошибке соединения |

## Автообнаружение

Автообнаружение позволяет динамически обнаруживать новые эндпоинты Prometheus на основе правил.

## Конфигурация мониторинга в формате JSON

```json
{
  "endpointUrl": "http://localhost:9090/metrics",
  "technology": "prometheus",
  "group": "my_prometheus_group"
}
```

## Связанные темы

* [Метрики Prometheus](/managed/ingest-from/extend-dynatrace/extend-metrics/ingestion-methods/prometheus "Узнайте о подходах к интеграции Prometheus.")
* [Расширение наблюдаемости метрик](/managed/ingest-from/extend-dynatrace/extend-metrics "Расширьте наблюдаемость метрик с помощью Dynatrace.")