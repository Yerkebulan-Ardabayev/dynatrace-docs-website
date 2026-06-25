---
title: Скриптовая интеграция OneAgent (pipe)
source: https://docs.dynatrace.com/managed/ingest-from/extend-dynatrace/extend-metrics/ingestion-methods/oneagent-pipe
scraped: 2026-05-12T11:37:59.140301
---

# Скриптовая интеграция OneAgent (pipe)

# Скриптовая интеграция OneAgent (pipe)

* 3-min read
* Updated on Mar 16, 2023

Инструмент `dynatrace_ingest` позволяет передавать метрики из скриптов и процессов в Dynatrace.

## Расположение бинарного файла

| ОС | Путь |
| --- | --- |
| Linux | `/opt/dynatrace/oneagent/agent/tools/dynatrace_ingest` |
| Windows | `%ProgramFiles%\dynatrace\oneagent\agent\tools\dynatrace_ingest.exe` |
| AIX | `/opt/dynatrace/oneagent/agent/tools/dynatrace_ingest` |

## Передача вывода процесса через pipe

```bash
my_script.sh | /opt/dynatrace/oneagent/agent/tools/dynatrace_ingest
```

## Аргументы командной строки

| Аргумент | Описание |
| --- | --- |
| `-v` | Подробный вывод (verbose) |
| `-p <port>` | Порт связи (по умолчанию 14499) |
| `-h` | Показать справку |

## Формат метрик

Формат метрик совпадает с форматом [Metric Ingestion Protocol](/managed/ingest-from/extend-dynatrace/extend-metrics/reference/metric-ingestion-protocol "Узнайте о протоколе приёма метрик."):

```
custom.metric,host=myhost gauge,42
```

## Порт связи

По умолчанию используется порт `14499`. Порт можно изменить через параметр `-p`.

## Связанные темы

* [Протокол приёма метрик](/managed/ingest-from/extend-dynatrace/extend-metrics/reference/metric-ingestion-protocol "Узнайте о протоколе приёма метрик.")
* [OneAgent Metric API](/managed/ingest-from/extend-dynatrace/extend-metrics/ingestion-methods/oneagent-metric-api "Используйте Dynatrace API для получения метрик мониторируемых сущностей.")