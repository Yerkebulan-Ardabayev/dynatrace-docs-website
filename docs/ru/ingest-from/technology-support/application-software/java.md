---
title: Java
source: https://www.dynatrace.com/docs/ingest-from/technology-support/application-software/java
scraped: 2026-03-05T21:26:24.102960
---

# Java

# Java

* Последняя версия Dynatrace
* Справочник
* Чтение: 1 минута
* Обновлено 23 октября 2025 г.

Предупреждение о несовместимости

Одновременное использование [SAP Introscope Agent](https://dt-url.net/ut039c3) и Dynatrace OneAgent в одной JVM не поддерживается. Dynatrace OneAgent при активности на одном хосте может незаметно блокировать работу Introscope Agent, препятствуя его нормальному функционированию.

Dynatrace полностью поддерживает Java, а также все основные JVM и JDK, предоставляя широкие возможности мониторинга Java:

* [Поддержка OpenTelemetry](https://github.com/open-telemetry/opentelemetry-java/) для захвата трассировок и приёма метрик.
  Дополнительные сведения см. в разделе [Инструментирование Java-приложения с помощью OpenTelemetry](../../opentelemetry/walkthroughs/java.md "Learn how to instrument your Java application using OpenTelemetry and Dynatrace.")
* Сквозная [трассировка транзакций](../../../observe/application-observability/services.md "Learn how to monitor and analyze your services, define and use request attributes, and more.") запросов к веб-сервисам, службам удалённого доступа, JMS и RabbitMQ
* [OneAgent SDK](../../extend-dynatrace/extend-tracing/oneagent-sdk.md "The Dynatrace OneAgent SDK enables you to instrument your application manually to extend end-to-end visibility for frameworks and technologies for which there is no code module yet available.") для пользовательской трассировки
* Информация о базах данных SQL (через JDBC) и NoSQL базах данных, таких как MongoDB, Cassandra и Redis
* Метрики кучи, сборки мусора, потоков, JMX, процессов и многое другое
* Анализ дампов памяти — Dynatrace поддерживает [дампы памяти](../../../observe/application-observability/profiling-and-optimization/memory-dump-analysis.md "Learn how Dynatrace enables you to trigger, download and analyze memory dumps for Java and Node.js.") для Oracle JVM, OpenJDK и IBM JVM
* Постоянное круглосуточное профилирование CPU производственного уровня (включая поддержку виртуальных потоков)
* [Непрерывный анализ потоков](../../../observe/application-observability/profiling-and-optimization/continuous-thread-analysis.md "Continuously analyze the state of your threads and their development to quickly identify and solve performance issues in Java and Node.js processes.") для потоков приложения, JVM и агента (анализ потоков JVM ограничен Java 8 и Java 17+)

Dynatrace также поддерживает GraalVM Native Images, предоставляя широкие возможности мониторинга Java:

* Сквозная распределённая трассировка HTTP-запросов вплоть до баз данных.
* Видимость на уровне кода для диагностики проблем в приложениях.
* Анализ конкуренции за ресурсы с метриками сборки мусора и потоков.

Подробные сведения о поддерживаемых [JVM](../../technology-support.md#java "Find technical details related to Dynatrace support for specific platforms and development frameworks.") и [Native Images](../../technology-support.md#java-native-image "Find technical details related to Dynatrace support for specific platforms and development frameworks.") см. в матрице поддерживаемых технологий.

## Обработка журналов с помощью парсеров технологических пакетов

Через OpenPipeline можно использовать и настраивать технологические пакеты. Технологический пакет — это библиотека парсеров (правил обработки), которые обрабатывают журналы из различных технологий, таких как Java, .NET и Microsoft IIS.

Парсеры помогают улучшить фильтрацию, диагностику, метрики, оповещения и информационные панели, эффективно извлекая уровни журналов и соответствующие атрибуты. Технологические пакеты также можно использовать для структурирования журналов из технологий, которые Dynatrace не поддерживает из коробки.

![syslog-bundles](https://dt-cdn.net/images/env-syslogbundles-2589-90e4e38b45.png)

Дополнительные сведения см. в разделе [Обработка журналов с помощью парсеров технологических пакетов](../../../platform/openpipeline/use-cases/tutorial-technology-processor.md "Set up a processing pipeline to structure technology-specific logs according to Dynatrace Semantic Dictionary.").

### Темы

* [Поддержка JVM](java/support-for-jvms.md "Find out the major JVMs and JDKs that are supported by Dynatrace.")
* [Сборщик мусора G1 — Java 9](java/g1-garbage-collector-java-9.md "Learn how the G1 works compared to other collectors and why it can easily outperform other state-of-the-art garbage collectors on large heaps.")
* [Основные проблемы с памятью Java](java/top-java-memory-problems.md "Learn about Java memory issues such as memory leaks, high memory usage, class loader problems, and GC configuration.")
* [События и оповещения об исчерпании памяти (OOM) и исчерпании потоков (OOT)](java/set-up-event-and-memory-alerting.md "Set up out-of-memory (OOM) and out-of-threads (OOT) events and alerting in Dynatrace.")
* [GraalVM Native Image](java/graalvm-native-image.md "Install, configure, and manage Dynatrace GraalVM Native Image module.")
* [Мониторинг нативных приложений Red Hat Quarkus](java/quarkus.md "Monitor Red Hat Quarkus native applications with Dynatrace on hosts that are monitored by OneAgent.")
