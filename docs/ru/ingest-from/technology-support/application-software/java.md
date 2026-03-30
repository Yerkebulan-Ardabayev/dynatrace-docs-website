---
title: Java
source: https://www.dynatrace.com/docs/ingest-from/technology-support/application-software/java
scraped: 2026-03-05T21:26:24.102960
---

Предупреждение о несовместимости

Одновременное использование [SAP Introscope Agent](https://dt-url.net/ut039c3) и Dynatrace OneAgent в одной JVM не поддерживается. Dynatrace OneAgent при активности на одном хосте может незаметно блокировать работу Introscope Agent, препятствуя его нормальному функционированию.

Dynatrace полностью поддерживает Java, а также все основные JVM и JDK, предоставляя широкие возможности мониторинга Java:

* [Поддержка OpenTelemetry](https://github.com/open-telemetry/opentelemetry-java/) для захвата трассировок и приёма метрик.
  Дополнительные сведения см. в разделе Инструментирование Java-приложения с помощью OpenTelemetry
* Сквозная трассировка транзакций запросов к веб-сервисам, службам удалённого доступа, JMS и RabbitMQ
* OneAgent SDK для пользовательской трассировки
* Информация о базах данных SQL (через JDBC) и NoSQL базах данных, таких как MongoDB, Cassandra и Redis
* Метрики кучи, сборки мусора, потоков, JMX, процессов и многое другое
* Анализ дампов памяти — Dynatrace поддерживает дампы памяти для Oracle JVM, OpenJDK и IBM JVM
* Постоянное круглосуточное профилирование CPU производственного уровня (включая поддержку виртуальных потоков)
* Непрерывный анализ потоков для потоков приложения, JVM и агента (анализ потоков JVM ограничен Java 8 и Java 17+)

Dynatrace также поддерживает GraalVM Native Images, предоставляя широкие возможности мониторинга Java:

* Сквозная распределённая трассировка HTTP-запросов вплоть до баз данных.
* Видимость на уровне кода для диагностики проблем в приложениях.
* Анализ конкуренции за ресурсы с метриками сборки мусора и потоков.

Подробные сведения о поддерживаемых [JVM](../../technology-support.md#java "Find technical details related to Dynatrace support for specific platforms and development frameworks.") и [Native Images](../../technology-support.md#java-native-image "Find technical details related to Dynatrace support for specific platforms and development frameworks.") см. в матрице поддерживаемых технологий.

## Обработка журналов с помощью парсеров технологических пакетов

Через OpenPipeline можно использовать и настраивать технологические пакеты. Технологический пакет — это библиотека парсеров (правил обработки), которые обрабатывают журналы из различных технологий, таких как Java, .NET и Microsoft IIS.

Парсеры помогают улучшить фильтрацию, диагностику, метрики, оповещения и информационные панели, эффективно извлекая уровни журналов и соответствующие атрибуты. Технологические пакеты также можно использовать для структурирования журналов из технологий, которые Dynatrace не поддерживает из коробки.

![syslog-bundles](https://dt-cdn.net/images/env-syslogbundles-2589-90e4e38b45.png)

Дополнительные сведения см. в разделе Обработка журналов с помощью парсеров технологических пакетов.

### Темы

* Поддержка JVM
* Сборщик мусора G1 — Java 9
* Основные проблемы с памятью Java
* События и оповещения об исчерпании памяти (OOM) и исчерпании потоков (OOT) and out-of-threads (OOT) events and alerting in Dynatrace.")
* GraalVM Native Image
* Мониторинг нативных приложений Red Hat Quarkus
