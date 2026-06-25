---
title: JMX-расширения
source: https://docs.dynatrace.com/managed/ingest-from/extend-dynatrace/extend-metrics/ingestion-methods/jmx-extensions
scraped: 2026-05-12T11:37:59.140301
---

# JMX-расширения

# JMX-расширения

* 5-min read
* Updated on Mar 16, 2023

JMX (Java Management Extensions) позволяет получать метрики из Java-приложений через MBeans.

## Создание JMX-расширений в веб-интерфейсе

1. Перейдите в **Settings > Monitoring > Monitored technologies**.
2. Найдите нужную технологию и выберите **Add custom extension**.
3. Выберите тип расширения **JMX** или **PMI** (для WebSphere).
4. Настройте параметры мониторинга и сохраните расширение.

## PMI-расширения

Расширения PMI (Performance Monitoring Infrastructure) применяются для мониторинга IBM WebSphere Application Server.

## Загрузка и активация расширения

После создания расширение необходимо сохранить и загрузить в окружение:

1. Нажмите **Save extension**.
2. Расширение активируется автоматически в течение нескольких минут.

## Просмотр метрик

Метрики JMX доступны в Data Explorer. Используйте Metrics Selector в Advanced mode для построения запросов.

## Разделения JMX/PMI (splittings)

Разделения позволяют получать метрики в разрезе отдельных MBean-экземпляров. Настройте разделения в конфигурации расширения.

## Ограничение метрик

Максимальное количество метрик на одно расширение: **5000**.

## Потребление мониторинга по технологиям

| Технология | DDU на хост в месяц |
| --- | --- |
| Java | 0,08 |
| WebSphere | 0,08 |
| JBoss | 0,08 |

## Связанные темы

* [Настройка JMX-расширений](/managed/ingest-from/extend-dynatrace/extend-metrics/ingestion-methods/jmx-extensions/customize-jmx-extensions "Узнайте о формате JSON для JMX-расширений.")
* [Расширение наблюдаемости метрик](/managed/ingest-from/extend-dynatrace/extend-metrics "Расширьте наблюдаемость метрик с помощью Dynatrace.")