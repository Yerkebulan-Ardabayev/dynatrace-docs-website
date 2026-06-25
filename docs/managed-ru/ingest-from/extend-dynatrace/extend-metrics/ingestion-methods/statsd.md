---
title: Интеграция со StatsD
source: https://docs.dynatrace.com/managed/ingest-from/extend-dynatrace/extend-metrics/ingestion-methods/statsd
scraped: 2026-05-12T11:37:59.140301
---

# Интеграция со StatsD

# Интеграция со StatsD

* 4-min read
* Updated on Mar 16, 2023

Dynatrace поддерживает приём метрик StatsD через OneAgent или ActiveGate.

## Включение DynatraceStatsD

Включение осуществляется на уровне окружения, группы хостов или хоста.

### На уровне окружения

Перейдите в **Settings > Monitoring > Monitored technologies** и включите **DynatraceStatsD**.

### На уровне группы хостов или хоста

Настройка доступна в соответствующих параметрах хоста или группы.

## Удалённый StatsD через ActiveGate

Для приёма метрик StatsD с удалённых источников используйте ActiveGate:

1. Установите ActiveGate.
2. Настройте клиент StatsD для отправки данных на порт `18126` ActiveGate.

## Порты связи

| Режим | Порт |
| --- | --- |
| OneAgent (локальный) | `18125` |
| ActiveGate (удалённый) | `18126` |

## Безопасность

StatsD использует UDP, поэтому данные передаются без аутентификации. Рекомендуется ограничить доступ к портам StatsD через настройки брандмауэра.

## Формат метрик StatsD

```
metric.name:value|type[|@sample_rate][|#tag1:value1,tag2:value2]
```

Примеры:

```
custom.counter:1|c
custom.gauge:42|g
custom.timer:320|ms
```

## Ограничения источника данных

| Параметр | Значение |
| --- | --- |
| Максимальный размер пакета UDP | 65507 байт |
| Максимальная длина имени метрики | 250 символов |

## Связанные темы

* [Протокол приёма метрик](/managed/ingest-from/extend-dynatrace/extend-metrics/reference/metric-ingestion-protocol "Узнайте о протоколе приёма метрик.")
* [Расширение наблюдаемости метрик](/managed/ingest-from/extend-dynatrace/extend-metrics "Расширьте наблюдаемость метрик с помощью Dynatrace.")