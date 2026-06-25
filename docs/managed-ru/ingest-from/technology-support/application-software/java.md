---
title: Java
source: https://docs.dynatrace.com/managed/ingest-from/technology-support/application-software/java
scraped: 2026-05-12T11:23:13.810332
---

# Java

# Java

* Справочник
* Чтение: 1 мин
* Обновлено 23 октября 2025 г.

Предупреждение о несовместимости

Одновременное использование [SAP Introscope Agent](https://dt-url.net/ut039c3) и Dynatrace OneAgent на одной JVM не поддерживается. Dynatrace OneAgent, активный на том же хосте, может незаметно блокировать Introscope Agent, мешая ему работать должным образом.

Dynatrace полностью поддерживает Java, а также все основные JVM и JDK, предоставляя широкие возможности мониторинга Java:

* [Поддержка OpenTelemetry](https://github.com/open-telemetry/opentelemetry-java/) для захвата трассировок и приёма метрик.  
  Подробнее см. в разделе [Инструментирование Java-приложения с OpenTelemetry](/managed/ingest-from/opentelemetry/walkthroughs/java "Узнайте, как инструментировать Java-приложение с помощью OpenTelemetry и Dynatrace.")
* Сквозное [трассирование транзакций](/managed/observe/application-observability/services "Узнайте, как мониторить и анализировать сервисы, задавать и использовать атрибуты запросов и многое другое.") запросов к веб-сервисам, удалённым сервисам, JMS и RabbitMQ
* [OneAgent SDK](/managed/ingest-from/extend-dynatrace/extend-tracing/oneagent-sdk "Dynatrace OneAgent SDK позволяет вручную инструментировать приложение, чтобы расширить сквозную видимость для фреймворков и технологий, для которых ещё нет готового модуля кода.") для пользовательской трассировки
* Видимость SQL-баз данных (через JDBC) и NoSQL-баз данных, таких как MongoDB, Cassandra и Redis
* Heap, сборка мусора, потоки, JMX, метрики процессов и многое другое
* Анализ дампов памяти – Dynatrace поддерживает [дампы памяти](/managed/observe/application-observability/profiling-and-optimization/memory-dump-analysis "Узнайте, как Dynatrace позволяет запускать, скачивать и анализировать дампы памяти для Java и Node.js.") для Oracle JVM, OpenJDK и IBM JVM
* Постоянное круглосуточное профилирование CPU уровня production (включая поддержку виртуальных потоков)
* [Непрерывный анализ потоков](/managed/observe/application-observability/profiling-and-optimization/continuous-thread-analysis "Непрерывно анализируйте состояние потоков и их развитие, чтобы быстро выявлять и устранять проблемы производительности в процессах Java и Node.js.") для потоков приложения, JVM и агента (анализ потоков JVM ограничен Java 8 и Java 17+)

Dynatrace также поддерживает GraalVM Native Images, предоставляя широкие возможности мониторинга Java:

* Сквозное распределённое трассирование HTTP-запросов вплоть до баз данных.
* Видимость на уровне кода для устранения проблем в приложениях.
* Анализ конкуренции за ресурсы с метриками сборки мусора и потоков.

См. матрицу поддерживаемых технологий, чтобы узнать подробности о поддерживаемых [JVM](/managed/ingest-from/technology-support#java "Технические подробности о поддержке Dynatrace для конкретных платформ и фреймворков разработки.") и [Native Images](/managed/ingest-from/technology-support#java-native-image "Технические подробности о поддержке Dynatrace для конкретных платформ и фреймворков разработки.").

### Темы

* [Поддержка JVM](/managed/ingest-from/technology-support/application-software/java/support-for-jvms "Узнайте об основных JVM и JDK, поддерживаемых Dynatrace.")
* [Сборщик мусора G1 – Java 9](/managed/ingest-from/technology-support/application-software/java/g1-garbage-collector-java-9 "Узнайте, как G1 работает в сравнении с другими сборщиками и почему он легко превосходит другие современные сборщики мусора на больших кучах.")
* [Главные проблемы памяти Java](/managed/ingest-from/technology-support/application-software/java/top-java-memory-problems "Узнайте о проблемах памяти Java, таких как утечки памяти, высокое использование памяти, проблемы загрузчика классов и настройки GC.")
* [События и оповещения о нехватке памяти (OOM) и потоков (OOT)](/managed/ingest-from/technology-support/application-software/java/set-up-event-and-memory-alerting "Настройте события и оповещения о нехватке памяти (OOM) и потоков (OOT) в Dynatrace.")
* [GraalVM Native Image](/managed/ingest-from/technology-support/application-software/java/graalvm-native-image "Установка, настройка и управление модулем Dynatrace GraalVM Native Image.")
* [Мониторинг native-приложений Red Hat Quarkus](/managed/ingest-from/technology-support/application-software/java/quarkus "Мониторинг native-приложений Red Hat Quarkus с помощью Dynatrace на хостах, мониторируемых OneAgent.")