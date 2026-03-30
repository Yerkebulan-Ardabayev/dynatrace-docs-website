---
title: Ограничения Dynatrace Intelligence
source: https://www.dynatrace.com/docs/dynatrace-intelligence/reference/davis-ai-limits
scraped: 2026-03-06T21:27:19.411859
---

## Проблемы и события

Ограничения применяются для каждого провайдера:

`AGENT_LOCAL_REST_API_INGEST`, `AVAILABILITY`, `BASELINING`, `EVENTS_REST_API_INGEST`, `KUBERNETES_ANOMALY_DETECTION`, `KUBERNETES_EVENT`, `LOG_EVENTS`, `METRIC_EVENTS`, `ONEAGENT`, `OPENPIPELINE_DATA_EXTRACTION`, `REAL_USER_MONITORING`, `SYNTHETIC`

| Ограничение | Лимит |
|---|---|
| Одновременно активные проблемы | 10 000 на окружение |
| Одновременно активные события (всего) | 15 000 на окружение |
| Одновременно активные события на провайдера | 4 000 |
| Обработка событий в час на провайдера | 100 000 (восполняется каждый час) |
| Максимальное время жизни события | 60 дней (затем закрывается и создается новое) |
| Интервал объединения проблем | 90 минут (после этого новые события не объединяются с проблемой) |

## Обнаружение аномалий

### Пользовательские оповещения

### Метрические события

#### Общие сведения

#### События метрических селекторов

#### События метрических ключей

### Симуляция в Notebook и Dashboard

## Агентный и генеративный ИИ Dynatrace Intelligence
