---
title: Расширение Dynatrace
source: https://www.dynatrace.com/docs/ingest-from/extend-dynatrace
scraped: 2026-03-06T21:10:28.052302
---

* Latest Dynatrace
* 3 мин чтения

Dynatrace — это открытая и расширяемая платформа. Вы можете дополнить данные наблюдаемости, собираемые из коробки, данными, предоставляемыми стандартами и фреймворками наблюдаемости, такими как OpenTelemetry и Prometheus. Кроме того, вы можете расширить аналитические возможности Dynatrace, расширяя топологию Smartscape и доменные рабочие процессы и экраны сущностей с помощью расширений. Вы также можете экспортировать данные в сторонние системы через API и интеграции с системами уведомлений о проблемах.

Этот раздел посвящён расширению телеметрических данных и созданию расширений для централизации и автоматизации конфигурации собираемых данных.

[![Dynatrace Developer](https://dt-cdn.net/images/developer-logo-1288bebd8d.svg "Dynatrace Developer")

### Создавайте нужные вам приложения

С помощью Dynatrace AppEngine вы можете создавать пользовательскую функциональность на основе всех данных наблюдаемости, поступающих в Dynatrace, в виде пользовательских приложений. Перейдите на Dynatrace Developer, чтобы получить инструменты и поддержку, необходимые для создания невероятных приложений с минимальными усилиями.](https://developer.dynatrace.com/?internal_source=doc&internal_medium=link&internal_campaign=cross)

## Метрики

[![OpenTelemetry](https://dt-cdn.net/images/techn-icon-opentelemetry-345d0f8b0e.svg "OpenTelemetry")

### OpenTelemetry

Отправляйте метрики OpenTelemetry в Dynatrace](opentelemetry.md "Learn how to integrate and ingest OpenTelemetry data (traces, metrics, and logs) into Dynatrace.")[![Micrometer](https://dt-cdn.net/images/mircrometer-d91d5ac640.svg "Micrometer")

### Micrometer

Собирайте метрики Micrometer из JVM-приложений](extend-dynatrace/extend-metrics/ingestion-methods/micrometer.md "Learn how to send Micrometer metrics to Dynatrace.")[![Prometheus](https://dt-cdn.net/images/prometheus-b1fab729ac.svg "Prometheus")

### Prometheus

Отправляйте метрики Prometheus в Dynatrace](extend-dynatrace/extend-metrics/ingestion-methods/prometheus.md "Learn how to extend observability in Dynatrace with Prometheus metrics.")[![StatsD](https://dt-cdn.net/images/statsd-icon-bigger-800-72b34b3823.png "StatsD")

### StatsD

Отправляйте метрики StatsD в Dynatrace](extend-dynatrace/extend-metrics/ingestion-methods/statsd.md "Ingest metrics into Dynatrace using OneAgent and the ActiveGate StatsD client.")[![Telegraf](https://dt-cdn.net/images/techn-icon-telegraf-ba9e70e8d6.svg "Telegraf")

### Telegraf

Отправляйте метрики Telegraf в Dynatrace](extend-dynatrace/extend-metrics/ingestion-methods/telegraf.md "Ingest Telegraf metrics into Dynatrace.")### Oracle Database

Расширьте наблюдаемость приложений данными, получаемыми непосредственно из уровня Oracle Database.[![Microsoft SQL Server](https://dt-cdn.net/images/techn-icon-microsoft-sqlserver-60740bd3fa.svg "Microsoft SQL Server")

### Microsoft SQL Server Database

Расширьте наблюдаемость приложений данными, получаемыми непосредственно из уровня Microsoft SQL Server.](extensions/supported-extensions/data-sources/sql/microsoft-sql.md "Extend observability in Dynatrace with declarative metrics ingested from Microsoft SQL Server.")[![SNMP](https://dt-cdn.net/images/techn-icon-snmp-43de4f1139.svg "SNMP")

### SNMP

Узнайте, как мониторить сетевые устройства с помощью SNMP.](extensions/supported-extensions/data-sources/snmp.md "Learn how to extend observability in Dynatrace with declarative SNMP metrics and event ingestion.")[![WMI](https://dt-cdn.net/images/techn-icon-microsoft-e15d516aaf.svg "WMI")

### WMI

Узнайте, как мониторить устройства, предоставляющие Windows Management Instrumentation, с помощью WMI.](extensions/supported-extensions/data-sources/wmi.md "Learn how to extend observability in Dynatrace with declarative WMI metrics ingestion.")[![JMX](https://dt-cdn.net/images/techn-icon-java-3016283f6a.svg "JMX")

### JMX

Расширьте наблюдаемость ваших Java-приложений с помощью метрик JMX.](extend-dynatrace/extend-metrics/ingestion-methods/jmx-extensions.md "Learn how to extend Dynatrace monitoring to include applications you've instrumented with JMX.")### Скриптовая интеграция

Расширьте наблюдаемость метрик с помощью скриптовой интеграции Dynatrace.### API приёма метрик

Расширьте наблюдаемость метрик с помощью открытых API метрик Dynatrace.

## Логи

[![FluentD](https://dt-cdn.net/images/techn-icon-fluentd-5634f339de.svg "FluentD")

### FluentD

Узнайте, как расширить наблюдаемость логов в Dynatrace с помощью Fluentd в качестве альтернативы сбору логов на основе OneAgent.](../analyze-explore-automate/logs/lma-log-ingestion/lma-stream-logs-fluentd-k8s.md "Integrate Fluentd with Dynatrace to stream logs from nodes and pods to Dynatrace.")[![Logstash](https://dt-cdn.net/images/elastic-logstash-a3afbd4913.svg "Logstash")

### Logstash

Узнайте, как расширить наблюдаемость логов в Dynatrace с помощью Logstash в качестве альтернативы сбору логов на основе OneAgent.](https://github.com/dynatrace-oss/logstash-output-dynatrace)### API приёма логов

Расширьте наблюдаемость логов с помощью открытых API логов Dynatrace.

## Распределённые трассировки

[![OpenTelemetry](https://dt-cdn.net/images/techn-icon-opentelemetry-345d0f8b0e.svg "OpenTelemetry")

### OpenTelemetry

Узнайте, как расширить наблюдаемость с помощью трассировки OpenTelemetry.](dynatrace-oneagent/oneagent-and-opentelemetry/oneagent-otel.md "Learn how to send OpenTelemetry data to a Dynatrace OneAgent.")[![Opentracing](https://dt-cdn.net/images/techn-icon-opentracing-936f2ba1cd.svg "Opentracing")

### OpenTracing

Узнайте, как расширить наблюдаемость в Dynatrace с помощью OpenTracing.](extend-dynatrace/extend-tracing/opentracing.md "Learn how to integrate OpenTracing with Dynatrace.")### OneAgent SDK

Узнайте, как расширить наблюдаемость в Dynatrace с помощью OneAgent SDK.

## Расширения

Используя стандарты и фреймворки наблюдаемости, перечисленные ниже, вы можете отправлять метрики, трассировки, логи и данные о пользовательском опыте в Dynatrace.

Благодаря декларативному подходу и централизованному автоматизированному развёртыванию и распределению расширений, теперь вы можете принимать эти данные проще и в масштабе, а также извлекать топологический контекст наряду с определением топологии. Вы можете использовать расширения для начала мониторинга новой технологии, ещё не охваченной Dynatrace, или для внедрения новой конфигурации в вашей среде (например, организовать данные в дашборды, создать новые оповещения и ввести сложные метрики).

### Extensions 2.0

Узнайте, как расширить наблюдаемость с помощью декларативного фреймворка Extensions 2.0.

## Пользовательский опыт и поведение

### Dynatrace OpenKit

Узнайте, как расширить наблюдаемость ваших мобильных и веб-приложений с помощью Dynatrace OpenKit.

## OpenTelemetry

OpenTelemetry — это фреймворк наблюдаемости для облачного программного обеспечения, используемый для инструментирования фреймворков и компонентов и экспорта телеметрических данных (трассировок, метрик и логов). [Dynatrace является ключевым контрибьютором](https://www.dynatrace.com/news/blog/dynatrace-joins-the-opentelemetry-project/) этого проекта с открытым исходным кодом.

Вы можете использовать OpenTelemetry в Dynatrace into Dynatrace.") для:

* Расширения технологического покрытия Dynatrace для технологий, которые не поддерживаются из коробки OneAgent
* Обогащения телеметрических данных дополнительными спанами и метриками

### Основы

Узнайте, как OpenTelemetry обеспечивает наблюдаемость в современных сложных архитектурах и технологиях. into Dynatrace.")### Метрики

Узнайте, как расширить наблюдаемость с помощью метрик, поступающих из OpenTelemetry. into Dynatrace.")### Трассировки

Узнайте, как расширить наблюдаемость с помощью трассировок, поступающих из OpenTelemetry. into Dynatrace.")