---
title: API приёма логов OneAgent
source: https://docs.dynatrace.com/managed/ingest-from/extend-dynatrace/extend-logs/oneagent-log-ingest-api
scraped: 2026-05-12T11:37:59.140301
---

# API приёма логов OneAgent

# API приёма логов OneAgent

* 3-min read
* Updated on Mar 16, 2023

OneAgent предоставляет локальный HTTP API для приёма логов по адресу `http://localhost:<port>/v2/logs/ingest`.

## Включение API приёма логов

API приёма логов можно включить на уровне окружения, хоста или группы хостов.

### На уровне окружения

Перейдите в **Settings > Log Monitoring > Log ingest rules** и включите **OneAgent log ingest API**.

### На уровне хоста или группы хостов

Перейдите в соответствующие настройки хоста или группы хостов и включите **OneAgent log ingest API**.

## Формат события лога

```json
{
  "content": "Log message text",
  "severity": "INFO",
  "timestamp": "2023-01-01T00:00:00.000Z",
  "log.source": "/var/log/myapp.log"
}
```

## Ограничения

* Максимальный размер одного события лога: 64 КБ.
* Максимальное количество событий в одном запросе: 1000.
* Скорость приёма ограничена настройками окружения.

## Пример запроса

```bash
curl -X POST "http://localhost:14499/v2/logs/ingest" \
  -H "Content-Type: application/json; charset=utf-8" \
  -d '[
    {
      "content": "Application started successfully",
      "severity": "INFO",
      "timestamp": "2023-01-01T00:00:00.000Z"
    }
  ]'
```

## Настройка порта связи

По умолчанию используется порт `14499`. Порт можно изменить в настройках OneAgent.

## Связанные темы

* [Мониторинг логов](/managed/analyze-explore-automate/log-monitoring "Узнайте, как использовать Log Analytics в Dynatrace.")
* [API приёма логов](/managed/analyze-explore-automate/log-monitoring/acquire-log-data/logs-classic-ingestion-api "Узнайте об API приёма логов.")