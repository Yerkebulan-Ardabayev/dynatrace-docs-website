---
title: Understand extensions data sources
source: https://www.dynatrace.com/docs/ingest-from/extensions/supported-extensions/data-sources
scraped: 2026-03-06T21:36:47.888698
---

# Знакомство с источниками данных расширений

# Знакомство с источниками данных расширений

* Latest Dynatrace
* Explanation
* 5-min read
* Published Oct 24, 2025

В Dynatrace источник данных — это предопределённый, специфичный для технологии метод сбора данных мониторинга из внешних систем или сервисов с использованием фреймворка расширений Dynatrace Extensions: либо [расширений, предоставляемых Dynatrace](/docs/ingest-from/extensions/supported-extensions "Learn more about the supported extensions."), либо [пользовательских расширений, разработанных вами](/docs/ingest-from/extensions/develop-your-extensions "Develop your own Extensions in Dynatrace.").

Источник данных расширений упрощает мониторинг, предоставляя декларативный, специфичный для технологии способ приёма данных.

Он оптимизирован для распространённых сценариев использования (таких как SQL, WMI или Prometheus) и при этом сохраняет гибкость благодаря источнику данных на основе Python для нестандартных ситуаций.

## Источник данных является декларативным

Расширения определяют, что именно нужно отслеживать и как подключиться к источнику данных — вместо написания подробных скриптов или пользовательской логики сбора данных.

## Источник данных является опinionated (опinionated approach)

Dynatrace предоставляет конкретный, оптимизированный способ получения данных от каждой поддерживаемой технологии, обеспечивая последовательность, высочайшие стандарты безопасности и лучшие практики мониторинга.

## Типы источников данных

Dynatrace предлагает встроенные источники данных для широко используемых технологий, каждый из которых адаптирован к конкретным протоколам, API или методам сбора данных:

### Источник данных SQL

Используется для сбора метрик или результатов запросов из реляционных баз данных.

Настраивается декларативно для выполнения SQL-запросов к базе данных и получения структурированных данных (например, производительность запросов, размеры таблиц, пулы соединений).

См. [SQL extensions](/docs/ingest-from/extensions/supported-extensions/data-sources/sql "Extend observability in Dynatrace with declarative metrics ingested from SQL-based extensions.").

### Источник данных WMI

Использует Windows Management Instrumentation (WMI) для мониторинга систем Windows.

Предоставляет доступ к счётчикам производительности, системным метрикам и сведениям об оборудовании в стандартизированном формате.

См. [Manage WMI extensions](/docs/ingest-from/extensions/supported-extensions/data-sources/wmi "Learn how to extend observability in Dynatrace with declarative WMI metrics ingestion.").

### Источник данных Prometheus

Разработан для сбора метрик с Prometheus-совместимых конечных точек.

Идеально подходит для приёма данных временных рядов из приложений или сервисов, предоставляющих метрики Prometheus.

См.

### Источник данных SNMP

Dynatrace предоставляет фреймворк, который вы можете использовать для расширения наблюдаемости за данными, получаемыми непосредственно с устройств под управлением SNMP. Для этого Dynatrace позволяет масштабно вносить данные SNMP в Dynatrace в контексте всех остальных данных.

Вы также можете расширить аналитику данных, связанных с SNMP-ловушками (SNMP traps), возникающими в вашей инфраструктуре.

См. [Manage SNMP extensions](/docs/ingest-from/extensions/supported-extensions/data-sources/snmp "Learn how to extend observability in Dynatrace with declarative SNMP metrics and event ingestion.").

### Источник данных Python (гибкий вариант)

Позволяет писать пользовательские скрипты на Python для сбора данных из технологий, не поддерживаемых другими источниками данных.

Особенно полезен, когда необходимо взаимодействовать с пользовательскими API, проприетарными системами или нишевыми технологиями.
