---
title: Расширение Dynatrace
source: https://docs.dynatrace.com/managed/ingest-from/extend-dynatrace
scraped: 2026-05-12T11:37:59.140301
---

# Расширение Dynatrace

# Расширение Dynatrace

* 3-min read
* Published Mar 05, 2018

Dynatrace — открытая и расширяемая платформа. Вы можете дополнить данные наблюдаемости, собираемые «из коробки», данными из стандартов и фреймворков наблюдаемости, таких как OpenTelemetry и Prometheus. Кроме того, можно расширить аналитические возможности Dynatrace, [расширив топологию Smartscape](/managed/ingest-from/extend-dynatrace/extend-topology "Убедитесь, что все входящие наблюдения богаты контекстом и анализируются в контексте связанных с ними мониторируемых объектов.") и [экраны рабочих процессов домена и объектов](/managed/ingest-from/extend-dynatrace/extend-ui "Расширение веб-интерфейса Dynatrace с помощью унифицированных страниц анализа, адаптированных под объекты.") через [расширения](/managed/ingest-from/extensions "Узнайте, как создавать расширения Dynatrace и управлять ими."). Также можно экспортировать данные во внешние системы через [API](/managed/dynatrace-api "Узнайте, что необходимо для использования API Dynatrace.") и [интеграции с системами уведомлений о проблемах](/managed/analyze-explore-automate/notifications-and-alerting/problem-notifications "Узнайте, как интегрировать сторонние системы уведомлений о проблемах с Dynatrace.").

Этот раздел посвящён расширению телеметрических данных и созданию [расширений](/managed/ingest-from/extensions "Узнайте, как создавать расширения Dynatrace и управлять ими.") для централизации и автоматизации настройки собираемых данных.

[![Dynatrace Developer](https://dt-cdn.net/images/developer-logo-1288bebd8d.svg "Dynatrace Developer")

### Создайте нужные вам приложения

С помощью Dynatrace AppEngine вы можете создавать пользовательскую функциональность на основе всех данных наблюдаемости, загруженных в Dynatrace, в виде пользовательских приложений. Перейдите в Dynatrace Developer, чтобы получить инструменты и поддержку для создания отличных приложений с минимальными усилиями.](https://developer.dynatrace.com/?utm_source=doc&utm_medium=link&utm_campaign=cross)

## Метрики

[![OpenTelemetry](https://dt-cdn.net/images/techn-icon-opentelemetry-345d0f8b0e.svg "OpenTelemetry")

### OpenTelemetry

Отправка метрик OpenTelemetry в Dynatrace](/managed/ingest-from/opentelemetry "Узнайте, как интегрировать и принимать данные OpenTelemetry (трассировки, метрики и логи) в Dynatrace.")[![Micrometer](https://dt-cdn.net/images/mircrometer-d91d5ac640.svg "Micrometer")

### Micrometer

Сбор метрик Micrometer из JVM-приложений](/managed/ingest-from/extend-dynatrace/extend-metrics/ingestion-methods/micrometer "Узнайте, как отправлять метрики Micrometer в Dynatrace.")[![Prometheus](https://dt-cdn.net/images/prometheus-b1fab729ac.svg "Prometheus")

### Prometheus

Отправка метрик Prometheus в Dynatrace](/managed/ingest-from/extend-dynatrace/extend-metrics/ingestion-methods/prometheus "Узнайте, как расширить наблюдаемость в Dynatrace с помощью метрик Prometheus.")[![StatsD](https://dt-cdn.net/images/statsd-icon-bigger-800-72b34b3823.png "StatsD")

### StatsD

Отправка метрик StatsD в Dynatrace](/managed/ingest-from/extend-dynatrace/extend-metrics/ingestion-methods/statsd "Прием метрик в Dynatrace с использованием OneAgent и клиента ActiveGate StatsD.")[![Telegraf](https://dt-cdn.net/images/techn-icon-telegraf-ba9e70e8d6.svg "Telegraf")

### Telegraf

Отправка метрик Telegraf в Dynatrace](/managed/ingest-from/extend-dynatrace/extend-metrics/ingestion-methods/telegraf "Прием метрик Telegraf в Dynatrace.")[### Oracle Database

Расширение наблюдаемости приложений за счёт данных, получаемых непосредственно из Oracle Database.](/managed/ingest-from/extensions/supported-extensions/data-sources/sql/oraclesql "Узнайте, как расширить наблюдаемость в Dynatrace с помощью декларативных метрик из Oracle Database.")[![Microsoft SQL Server](https://dt-cdn.net/images/techn-icon-microsoft-sqlserver-60740bd3fa.svg "Microsoft SQL Server")

### Microsoft SQL Server Database

Расширение наблюдаемости приложений за счёт данных, получаемых непосредственно из Microsoft SQL Server.](/managed/ingest-from/extensions/supported-extensions/data-sources/sql/microsoft-sql "Расширение наблюдаемости в Dynatrace с помощью декларативных метрик из Microsoft SQL Server.")[![SNMP](https://dt-cdn.net/images/techn-icon-snmp-43de4f1139.svg "SNMP")

### SNMP

Мониторинг сетевых устройств с использованием SNMP.](/managed/ingest-from/extensions/supported-extensions/data-sources/snmp "Узнайте, как расширить наблюдаемость в Dynatrace с помощью декларативного приёма метрик и событий SNMP.")[![WMI](https://dt-cdn.net/images/techn-icon-microsoft-e15d516aaf.svg "WMI")

### WMI

Мониторинг устройств, использующих Windows Management Instrumentation, с помощью WMI.](/managed/ingest-from/extensions/supported-extensions/data-sources/wmi "Узнайте, как расширить наблюдаемость в Dynatrace с помощью декларативного приёма метрик WMI.")[![JMX](https://dt-cdn.net/images/techn-icon-java-3016283f6a.svg "JMX")

### JMX

Расширение наблюдаемости Java-приложений с помощью метрик JMX.](/managed/ingest-from/extend-dynatrace/extend-metrics/ingestion-methods/jmx-extensions "Узнайте, как расширить мониторинг Dynatrace на приложения, инструментированные с помощью JMX.")[### Scripting integration

Расширение наблюдаемости метрик через scripting integration Dynatrace.](/managed/ingest-from/extend-dynatrace/extend-metrics/ingestion-methods/oneagent-pipe "Узнайте, как принимать метрики с помощью локальной scripting integration.")[### API приёма метрик

Расширение наблюдаемости метрик через открытые Metric API Dynatrace.](/managed/ingest-from/extend-dynatrace/extend-metrics/ingestion-methods/oneagent-metric-api "Используйте API Dynatrace для получения метрик мониторируемых объектов.")

## Логи

[![FluentD](https://dt-cdn.net/images/techn-icon-fluentd-5634f339de.svg "FluentD")

### FluentD

Расширение наблюдаемости логов в Dynatrace с помощью Fluentd в качестве альтернативы сбору логов через OneAgent.](/managed/upgrade/unavailable-in-managed "Выбранный раздел недоступен в Dynatrace Managed.")[![Logstash](https://dt-cdn.net/images/elastic-logstash-a3afbd4913.svg "Logstash")

### Logstash

Расширение наблюдаемости логов в Dynatrace с помощью Logstash в качестве альтернативы сбору логов через OneAgent.](https://github.com/dynatrace-oss/logstash-output-dynatrace)[### API приёма логов

Расширение наблюдаемости логов через открытые Log API Dynatrace.](/managed/analyze-explore-automate/log-monitoring/acquire-log-data/logs-classic-ingestion-api "Узнайте, как Dynatrace принимает данные логов и каковы возможные ограничения.")

## Распределённые трассировки

[![OpenTelemetry](https://dt-cdn.net/images/techn-icon-opentelemetry-345d0f8b0e.svg "OpenTelemetry")

### OpenTelemetry

Расширение наблюдаемости с помощью трассировки OpenTelemetry.](/managed/ingest-from/dynatrace-oneagent/oneagent-and-opentelemetry/oneagent-otel "Узнайте, как отправлять данные OpenTelemetry в Dynatrace OneAgent.")[![Opentracing](https://dt-cdn.net/images/techn-icon-opentracing-936f2ba1cd.svg "Opentracing")

### OpenTracing

Расширение наблюдаемости в Dynatrace с помощью OpenTracing.](/managed/ingest-from/extend-dynatrace/extend-tracing/opentracing "Узнайте, как интегрировать OpenTracing с Dynatrace.")[### OneAgent SDK

Расширение наблюдаемости в Dynatrace с помощью OneAgent SDK.](/managed/ingest-from/extend-dynatrace/extend-tracing/oneagent-sdk "Dynatrace OneAgent SDK позволяет вручную инструментировать приложение для сквозной видимости фреймворков и технологий, для которых ещё нет кодового модуля.")

## Расширения

Используя перечисленные ниже стандарты и фреймворки наблюдаемости, вы можете отправлять метрики, трассировки, логи и данные пользовательского опыта в Dynatrace.

Благодаря декларативному подходу, централизованному и автоматизированному развёртыванию и распространению [расширений](/managed/ingest-from/extensions "Узнайте, как создавать расширения Dynatrace и управлять ими."), теперь можно легко принимать эти данные в масштабе и получать топологический контекст вместе с определением топологии. [Расширения](/managed/ingest-from/extensions "Узнайте, как создавать расширения Dynatrace и управлять ими.") можно использовать для начала мониторинга новой технологии, которая ещё не охвачена Dynatrace, или для добавления новой конфигурации в ваше окружение (например, организации данных в дашборды, создания новых оповещений и внедрения сложных метрик).

[### Extensions 2.0

Узнайте, как расширить наблюдаемость с помощью декларативного фреймворка Extensions 2.0.](/managed/ingest-from/extensions "Узнайте, как создавать расширения Dynatrace и управлять ими.")

## Пользовательский опыт и поведение

[### Dynatrace OpenKit

Узнайте, как расширить наблюдаемость мобильных и веб-приложений с помощью Dynatrace OpenKit.](/managed/ingest-from/extend-dynatrace/openkit "Узнайте, как инструментировать приложение с помощью OpenKit, использовать методы API Dynatrace OpenKit и многое другое.")

## OpenTelemetry

OpenTelemetry — это фреймворк наблюдаемости для облачных приложений, используемый для инструментирования фреймворков и компонентов и экспорта телеметрических данных (трассировок, метрик и логов). [Dynatrace является ключевым участником](https://www.dynatrace.com/news/blog/dynatrace-joins-the-opentelemetry-project/) этого проекта с открытым исходным кодом.

[OpenTelemetry в Dynatrace](/managed/ingest-from/opentelemetry "Узнайте, как интегрировать и принимать данные OpenTelemetry (трассировки, метрики и логи) в Dynatrace.") можно использовать для:

* Расширения технологического охвата Dynatrace для технологий, не поддерживаемых OneAgent «из коробки»
* Обогащения телеметрических данных дополнительными span-ами и метриками

[### Основы

Узнайте, как OpenTelemetry обеспечивает наблюдаемость в современных сложных архитектурах и технологиях.](/managed/ingest-from/opentelemetry "Узнайте, как интегрировать и принимать данные OpenTelemetry (трассировки, метрики и логи) в Dynatrace.")[### Метрики

Узнайте, как расширить наблюдаемость с помощью метрик, полученных из OpenTelemetry.](/managed/ingest-from/opentelemetry "Узнайте, как интегрировать и принимать данные OpenTelemetry (трассировки, метрики и логи) в Dynatrace.")[### Трассировки

Узнайте, как расширить наблюдаемость с помощью трассировок, полученных из OpenTelemetry.](/managed/ingest-from/opentelemetry "Узнайте, как интегрировать и принимать данные OpenTelemetry (трассировки, метрики и логи) в Dynatrace.")