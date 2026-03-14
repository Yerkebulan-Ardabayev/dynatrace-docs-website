---
title: Мониторинг нативных приложений Red Hat Quarkus
source: https://www.dynatrace.com/docs/ingest-from/technology-support/application-software/java/quarkus
scraped: 2026-03-04T21:28:08.700183
---

# Мониторинг нативных приложений Red Hat Quarkus


* Latest Dynatrace
* 3 мин чтения
* Обновлено 28 января 2026 г.

[Red Hat Quarkus](https://www.redhat.com/en/topics/cloud-native-apps/what-is-quarkus) — это Java-фреймворк с открытым исходным кодом, оптимизированный для нативных образов GraalVM, который делает Java полноценным участником мира микросервисов. Quarkus относится к семейству полнофункциональных фреймворков, разработанных для Kubernetes. Он включает современные библиотеки Java и соответствует последним стандартам Java.

Узнайте, как Dynatrace может отслеживать трассировки нативных Java-приложений и контролировать метрики и логи приложения Quarkus, скомпилированного в нативный образ.

## Предварительные требования

* Ваша версия GraalVM [поддерживается Dynatrace](../../../technology-support.md#java-native-image "Техническая информация о поддержке Dynatrace для определённых платформ и фреймворков разработки.").
* GraalVM настроен для сборки нативных образов. Подробнее см. руководство Quarkus [Сборка нативного исполняемого файла](https://quarkus.io/guides/building-native-image).
* OneAgent или Dynatrace Operator установлен на машине, где будет выполняться приложение.

  Необходимая установка зависит от вашего приложения:

  | Если ваше приложение работает | См. инструкции для |
  | --- | --- |
  | на виртуальной машине или физическом сервере | [OneAgent](../../../dynatrace-oneagent/installation-and-operation.md "Установка OneAgent на сервер в первый раз.") |
  | как рабочая нагрузка в Kubernetes или OpenShift | [Dynatrace Operator](../../../setup-on-k8s/deployment.md "Развёртывание Dynatrace Operator в Kubernetes") |

## Трассировки

Dynatrace может автоматически трассировать JIT-компилированные приложения Quarkus, работающие на OpenJDK HotSpot JVM и GraalVM.

Для AOT-компилированных приложений Quarkus, работающих на GraalVM, см. [GraalVM Native Image](graalvm-native-image.md "Установка, настройка и управление модулем GraalVM Native Image в Dynatrace.") для начала работы.

#### OpenTelemetry

Вы можете экспортировать информацию о трассировке Quarkus с помощью [OpenTelemetry](../../../opentelemetry.md "Узнайте, как интегрировать и загружать данные OpenTelemetry (трассировки, метрики и логи) в Dynatrace.").

Упрощённые варианты настройки при мониторинге с помощью OneAgent

Если ваша среда контролируется OneAgent, вам доступны следующие упрощённые варианты конфигурации:

* **[OneAgent OpenTelemetry Span Sensor](../../../dynatrace-oneagent/oneagent-and-opentelemetry/oneagent-otel.md#oneagent-otel-span-sensor "Узнайте, как отправлять данные OpenTelemetry в Dynatrace OneAgent.")** Рекомендуется: Автоматически захватывает вызовы API OpenTelemetry и встраивает их в трассировки OneAgent без необходимости ручной настройки экспорта OTLP. Для использования этого подхода [включите OpenTelemetry Span Sensor](../../../dynatrace-oneagent/oneagent-and-opentelemetry/configuration.md "Узнайте, как включить и настроить OneAgent Span Sensor для данных OpenTelemetry.") и **не** настраивайте ручной экспорт OTLP.
* **[Локальный эндпоинт OTLP через EEC](../../../dynatrace-oneagent/oneagent-and-opentelemetry/oneagent-otel.md#send-opentelemetry-traces-to-the-otlp-endpoint-exposed-by-oneagent "Узнайте, как отправлять данные OpenTelemetry в Dynatrace OneAgent.")**: Для неконтейнеризированных сред вы можете отправлять трассировки на локальный эндпоинт OTLP `http://localhost:14499/otlp/v1/traces` после [включения Extension Execution Controller](../../../dynatrace-oneagent/oneagent-and-opentelemetry/oneagent-otel.md#send-opentelemetry-traces-to-the-otlp-endpoint-exposed-by-oneagent "Узнайте, как отправлять данные OpenTelemetry в Dynatrace OneAgent."). Это устраняет необходимость в API-токенах и внешних эндпоинтах.

Если вы предпочитаете метод на основе OneAgent, пропустите ручную настройку ниже.

Если вы предпочитаете ручную настройку или не используете OneAgent, выполните следующие шаги.

Для ручной настройки экспорта OpenTelemetry используйте [параметры конфигурации, специфичные для Quarkus](https://dt-url.net/3g039zt), чтобы настроить экспортёр на отправку данных трассировки на один из двух доступных эндпоинтов — [ActiveGate или OneAgent](../../../opentelemetry/otlp-api.md "Узнайте об эндпоинтах OTLP API, которые ваше приложение использует для экспорта данных OpenTelemetry в Dynatrace.").

Следующий пример показывает, как настроить `application.properties` для экспорта на SaaS-эндпоинт Dynatrace. В нём указаны URL API и необходимый, процентно-кодированный [заголовок `Authorization`](../../../opentelemetry/otlp-api.md#authentication-export-to-activegate "Узнайте об эндпоинтах OTLP API, которые ваше приложение использует для экспорта данных OpenTelemetry в Dynatrace.") с API-токеном.

```
quarkus.application.name=myservice


quarkus.otel.exporter.otlp.traces.endpoint=https://{your-environment-id}.live.dynatrace.com/api/v2/otlp


quarkus.otel.exporter.otlp.traces.headers=authorization=Api-Token%20dt.....


quarkus.log.console.format=%d{HH:mm:ss} %-5p traceId=%X{traceId}, parentId=%X{parentId}, spanId=%X{spanId}, sampled=%X{sampled} [%c{2.}] (%t) %s%e%n
```

## Метрики

Red Hat рекомендует получать метрики из Quarkus через библиотеку `quarkus-micrometer-registry-prometheus`.

Чтобы узнать, как использовать метрики Micrometer в вашем приложении Quarkus, см. руководство Quarkus [Метрики Micrometer](https://quarkus.io/guides/micrometer).

Dynatrace предлагает два подхода для получения метрик Micrometer из Prometheus: через API или через расширение.

### Приём метрик Micrometer через API Dynatrace

Используйте API Dynatrace для приёма метрик, полученных из библиотеки `quarkus-micrometer-registry-prometheus`.

Подробнее о процедуре приёма см. [Отправка метрик Micrometer в Dynatrace](../../../extend-dynatrace/extend-metrics/ingestion-methods/micrometer.md "Узнайте, как отправлять метрики Micrometer в Dynatrace.").

Для нативных приложений обязательно следуйте подходу [Напрямую в Micrometer](../../../extend-dynatrace/extend-metrics/ingestion-methods/micrometer.md#properties-direct "Узнайте, как отправлять метрики Micrometer в Dynatrace.").

### Приём метрик Micrometer через расширение

Используйте [платформу Extensions 2.0](../../../extensions.md "Узнайте, как создавать и управлять расширениями Dynatrace.") Dynatrace для приёма метрик Micrometer, полученных из [источника данных Prometheus](../../../extensions/develop-your-extensions/data-sources/prometheus-extensions.md "Узнайте, как создать расширение Prometheus с помощью платформы расширений.") — для этого необходимо создать пользовательское расширение.

В качестве отправной точки вы можете использовать пример пользовательского расширения ниже. Он адаптирован для библиотеки `quarkus-micrometer-registry-prometheus`. Убедитесь, что вы используете правильный эндпоинт метрик в вашей конфигурации. Эндпоинт по умолчанию — `localhost:8080/q/metrics`.

Пример расширения на основе Prometheus

```
name: custom:com.dynatrace.extension.micrometer-quarkus


version: 1.0.0


minDynatraceVersion: "1.247"


author:


name: Dynatrace


#dashboards:


#  - path: "dashboards/dashboard_exporter.json"


#alerts:


#  - path: "alerts/alert_socket_usage.json"


prometheus:


- group: quarkus metrics


interval:


minutes: 1


featureSet: all


dimensions:


- key: quarkus


value: const:quarkus


subgroups:


# global counters


- subgroup: quarkus global counter


dimensions:


- key: global_counters


value: const:global_counters


metrics:


# HELP process_uptime_seconds The uptime of the Java virtual machine


# TYPE process_uptime_seconds gauge


- key: com.dynatrace.process.global.uptime.seconds


value: metric:process_uptime_seconds


type: gauge


featureSet: global


# HELP process_cpu_usage The "recent cpu usage" for the Java Virtual Machine process


# TYPE process_cpu_usage gauge


- key: com.dynatrace.process.global.cpu.usage


value: metric:process_cpu_usage


type: gauge


featureSet: global


# HELP system_cpu_usage The "recent cpu usage" of the system the application is running in


# TYPE system_cpu_usage gauge


- key: com.dynatrace.system.global.cpu.usage


value: metric:system_cpu_usage


type: gauge


featureSet: global


# HELP jvm_classes_unloaded_classes_total The total number of classes unloaded since the Java virtual machine has started execution


# TYPE jvm_classes_unloaded_classes_total counter


- key: com.dynatrace.jvm.classes.global.uploaded.total


value: metric:jvm_classes_unloaded_classes_total


type: count


featureSet: global


# HELP jvm_info_total JVM version info


# TYPE jvm_info_total counter


- key: com.dynatrace.jvm.global.info.total


value: metric:jvm_info_total


type: count


featureSet: global


# HELP http_server_connections_seconds_max


# TYPE http_server_connections_seconds_max gauge


- key: com.dynatrace.http.server.connections.seconds.global.max


value: metric:http_server_connections_seconds_max


type: gauge


featureSet: global


# HELP http_server_connections_seconds


# TYPE http_server_connections_seconds summary


- key: com.dynatrace.http.server.connections.seconds.active.global.count


value: metric:http_server_connections_seconds_active_count


type: count


featureSet: global


- key: com.dynatrace.http.server.connections.seconds.active.global.duration.summary


value: metric:http_server_connections_seconds_duration_sum


type: gauge


featureSet: global


# HELP process_files_max_files The maximum file descriptor count


# TYPE process_files_max_files gauge


- key: com.dynatrace.process.files.global.max


value: metric:process_files_max_files


type: gauge


featureSet: global


# HELP http_server_bytes_written_max


# TYPE http_server_bytes_written_max gauge


- key: com.dynatrace.http.server.bytes.wrriten.global.max


value: metric:http_server_bytes_written_max


type: gauge


featureSet: global


# HELP http_server_bytes_written


# TYPE http_server_bytes_written summary


- key: com.dynatrace.http.server.bytes.written.global.count


value: metric:http_server_bytes_written_count


type: count


featureSet: global


- key: com.dynatrace.http.server.bytes.written.global.summary


value: metric:http_server_bytes_written_sum


type: gauge


featureSet: global


# HELP system_load_average_1m The sum of the number of runnable entities queued to available processors and the number of runnable entities running on the available processors averaged over a period of time


# TYPE system_load_average_1m gauge


- key: com.dynatrace.system.load.average.global.lm


value: metric:system_load_average_1m


type: gauge


featureSet: global


# HELP jvm_gc_overhead_percent An approximation of the percent of CPU time used by GC activities over the last lookback period or since monitoring began, whichever is shorter, in the range [0..1]


# TYPE jvm_gc_overhead_percent gauge


- key: com.dynatrace.jvm.gc.overhead.global.percent


value: metric:jvm_gc_overhead_percent


type: gauge


featureSet: global


# HELP jvm_threads_daemon_threads The current number of live daemon threads


# TYPE jvm_threads_daemon_threads gauge


- key: com.dynatrace.jvm.threads.daemon.global.threads


value: metric:jvm_threads_daemon_threads


type: gauge


featureSet: global


# HELP jvm_threads_live_threads The current number of live threads including both daemon and non-daemon threads


# TYPE jvm_threads_live_threads gauge


- key: com.dynatrace.jvm.threads.live.global.threads


value: metric:jvm_threads_live_threads


type: gauge


featureSet: global


# HELP http_server_requests_seconds


# TYPE http_server_requests_seconds summary


- key: com.dynatrace.http.server.bytes.written.global.count


value: metric:http_server_requests_seconds_count


type: count


featureSet: global


- key: com.dynatrace.http.server.bytes.written.global.summary


value: metric:http_server_requests_seconds_sum


type: gauge


featureSet: global


# HELP http_server_requests_seconds_max


# TYPE http_server_requests_seconds_max gauge


- key: com.dynatrace.http.server.requests.seconds.max


value: metric:http_server_requests_seconds_max


type: gauge


featureSet: global


# HELP process_start_time_seconds Start time of the process since unix epoch.


# TYPE process_start_time_seconds gauge


- key: com.dynatrace.process.start.time.global.seconds


value: metric:process_start_time_seconds


type: gauge


featureSet: global


# HELP jvm_classes_loaded_classes The number of classes that are currently loaded in the Java virtual machine


# TYPE jvm_classes_loaded_classes gauge


- key: com.dynatrace.jvm.classes.loaded.global.max


value: metric:jvm_classes_loaded_classes


type: gauge


featureSet: global


# HELP jvm_threads_peak_threads The peak live thread count since the Java virtual machine started or peak was reset


# TYPE jvm_threads_peak_threads gauge


- key: com.dynatrace.jvm.threads.peak.global.threads


value: metric:jvm_threads_peak_threads


type: gauge


featureSet: global


# HELP system_cpu_count The number of processors available to the Java virtual machine


# TYPE system_cpu_count gauge


- key: com.dynatrace.system.cpu.global.counter


value: metric:system_cpu_count


type: gauge


featureSet: global


# HELP process_files_open_files The open file descriptor count


# TYPE process_files_open_files gauge


- key: com.dynatrace.process.files.open.global.files


value: metric:process_files_open_files


type: gauge


featureSet: global
```

## Логи

Dynatrace предлагает [различные варианты](../../../extend-dynatrace/extend-logs.md "Узнайте, как расширить наблюдаемость логов в Dynatrace.") для сбора логов из ваших приложений и сред.

Чтобы узнать, как настроить логирование в вашем приложении Quarkus, см. руководство Quarkus [Настройка логирования](https://quarkus.io/guides/logging).

Для процедуры ниже мы предполагаем, что ваше приложение записывает логи в файл `/var/log/quarkus-app.log`.

1. Запустите ваше нативное приложение Quarkus.
2. Перейдите в ![Hosts](https://dt-cdn.net/images/hosts-512-59f5d2dd7f.png "Hosts") **Hosts Classic** и выберите ваш хост.
3. Прокрутите вниз до раздела **Process analysis** и в списке процессов выберите процесс вашего нативного приложения Quarkus.
4. В правой части панели **Process** выберите ![More](https://dt-cdn.net/images/more-icon-01c8b008ca.svg "More") > **Settings**.
5. В настройках группы процессов выберите **Log monitoring** > **Add new log for monitoring**.
6. Введите полный путь к вашему файлу логов. Обязательно соблюдайте [требования к пути лога](../../../../analyze-explore-automate/log-monitoring/acquire-log-data/add-log-files-manually-v2.md#considerations-for-adding-text-log-files-manually "Узнайте, как вручную добавлять файлы логов для анализа.").
7. Выберите **Save changes**.
8. [Включите добавленные файлы логов](../../../../analyze-explore-automate/log-monitoring/acquire-log-data/add-log-files-sources-v2.md "Узнайте, как включать и исключать источники логов для анализа.") в хранилище логов.

## Связанные темы

* [Отправка метрик Micrometer в Dynatrace](../../../extend-dynatrace/extend-metrics/ingestion-methods/micrometer.md "Узнайте, как отправлять метрики Micrometer в Dynatrace.")
* [Управление расширениями Prometheus](../../../extend-dynatrace/extend-metrics/ingestion-methods/prometheus/prometheus-extensions.md "Узнайте, как расширить наблюдаемость в Dynatrace с помощью декларативного приёма метрик Prometheus.")
* [Источник данных Prometheus](../../../extensions/develop-your-extensions/data-sources/prometheus-extensions.md "Узнайте, как создать расширение Prometheus с помощью платформы расширений.")
* [Эндпоинты OTLP API Dynatrace](../../../opentelemetry/otlp-api.md "Узнайте об эндпоинтах OTLP API, которые ваше приложение использует для экспорта данных OpenTelemetry в Dynatrace.")