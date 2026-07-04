---
title: Мониторинг нативных приложений Red Hat Quarkus
source: https://docs.dynatrace.com/managed/ingest-from/technology-support/application-software/java/quarkus
scraped: 2026-05-12T12:04:34.218723
---

# Мониторинг нативных приложений Red Hat Quarkus

# Мониторинг нативных приложений Red Hat Quarkus

* Чтение: 3 мин
* Обновлено 28 января 2026 г.

[Red Hat Quarkus](https://www.redhat.com/en/topics/cloud-native-apps/what-is-quarkus), это Java-фреймворк с открытым исходным кодом, оптимизированный для GraalVM Native Images, чтобы сделать Java полноценным участником мира микросервисов. Quarkus принадлежит к семейству full-stack фреймворков, адаптированных для Kubernetes. Он включает современные библиотеки Java и следует последним стандартам Java.

Узнайте, как Dynatrace может трассировать нативные Java-приложения и отслеживать метрики и логи приложения Quarkus, скомпилированного как native image.

## Предварительные требования

* Ваша версия GraalVM [поддерживается Dynatrace](/managed/ingest-from/technology-support#java-native-image "Технические подробности о поддержке Dynatrace конкретных платформ и фреймворков разработки.").
* GraalVM настроен на сборку native images. Подробнее см. в руководстве Quarkus [Building a native executable](https://quarkus.io/guides/building-native-image).
* OneAgent или Dynatrace Operator установлен на машине, где будет выполняться приложение.

  Необходимая установка зависит от вашего приложения:

  | Если ваше приложение работает | См. инструкцию для |
  | --- | --- |
  | на виртуальной машине или физическом сервере | [OneAgent](/managed/ingest-from/dynatrace-oneagent/installation-and-operation "Установка OneAgent на сервер в первый раз.") |
  | как рабочая нагрузка в Kubernetes или OpenShift | [Dynatrace Operator](/managed/ingest-from/setup-on-k8s/deployment "Развёртывание Dynatrace Operator в Kubernetes") |

## Трассировки

Dynatrace может автоматически трассировать Quarkus-приложения, скомпилированные в режиме JIT (just-in-time) и выполняемые на OpenJDK HotSpot JVM и GraalVM.

Для Quarkus-приложений, скомпилированных в режиме AOT (ahead-of-time) и выполняемых на GraalVM, см. [GraalVM Native Image](/managed/ingest-from/technology-support/application-software/java/graalvm-native-image "Установка, настройка и управление модулем Dynatrace GraalVM Native Image.") для начала работы.

#### OpenTelemetry

Информацию трассировки Quarkus можно экспортировать с помощью [OpenTelemetry](/managed/ingest-from/opentelemetry "Узнайте, как интегрировать и принимать данные OpenTelemetry (трассировки, метрики и логи) в Dynatrace.").

Упрощённые варианты настройки при мониторинге через OneAgent

Если ваша среда отслеживается OneAgent, вам доступны следующие упрощённые варианты настройки:

* **[OneAgent OpenTelemetry Span Sensor](/managed/ingest-from/dynatrace-oneagent/oneagent-and-opentelemetry/oneagent-otel#oneagent-otel-span-sensor "Узнайте, как отправлять данные OpenTelemetry в Dynatrace OneAgent.")** Рекомендуется: автоматически захватывает вызовы OpenTelemetry API и сшивает их в трассировки OneAgent без необходимости в ручной настройке экспорта OTLP. Чтобы использовать этот подход, [включите OpenTelemetry Span Sensor](/managed/ingest-from/dynatrace-oneagent/oneagent-and-opentelemetry/configuration "Узнайте, как включить и настроить OneAgent Span Sensor для данных OpenTelemetry.") и **не** настраивайте ручной экспорт OTLP.
* **[Локальный эндпоинт OTLP через EEC](/managed/ingest-from/dynatrace-oneagent/oneagent-and-opentelemetry/oneagent-otel#send-opentelemetry-traces-to-the-otlp-endpoint-exposed-by-oneagent "Узнайте, как отправлять данные OpenTelemetry в Dynatrace OneAgent.")**: для неконтейнеризованных сред можно отправлять трассировки на локальный эндпоинт OTLP по адресу `http://localhost:14499/otlp/v1/traces` после [включения Extension Execution Controller](/managed/ingest-from/dynatrace-oneagent/oneagent-and-opentelemetry/oneagent-otel#send-opentelemetry-traces-to-the-otlp-endpoint-exposed-by-oneagent "Узнайте, как отправлять данные OpenTelemetry в Dynatrace OneAgent."). Это устраняет необходимость в API-токенах и внешних эндпоинтах.

Если вы предпочитаете метод на основе OneAgent, пропустите ручную настройку ниже.

Если вы предпочитаете ручную настройку или не используете OneAgent, выполните следующие шаги.

Чтобы вручную настроить экспорт OpenTelemetry, используйте [специфичные для Quarkus параметры настройки](https://dt-url.net/3g039zt) для настройки экспортёра на отправку данных трассировки на один из двух доступных эндпоинтов, [ActiveGate или OneAgent](/managed/ingest-from/opentelemetry/otlp-api "Узнайте об эндпоинтах OTLP API, которые ваше приложение использует для экспорта данных OpenTelemetry в Dynatrace.").

В следующем примере показано, как настроить `application.properties` для экспорта на эндпоинт Dynatrace SaaS. Он указывает URL API и необходимый заголовок [`Authorization`](/managed/ingest-from/opentelemetry/otlp-api#authentication-export-to-activegate "Узнайте об эндпоинтах OTLP API, которые ваше приложение использует для экспорта данных OpenTelemetry в Dynatrace.") в процентной кодировке с API-токеном.

```
quarkus.application.name=myservice



quarkus.otel.exporter.otlp.traces.endpoint=https://{your-cluster-dns}/e/{your-environment-id}/api/v2/otlp



quarkus.otel.exporter.otlp.traces.headers=authorization=Api-Token%20dt.....



quarkus.log.console.format=%d{HH:mm:ss} %-5p traceId=%X{traceId}, parentId=%X{parentId}, spanId=%X{spanId}, sampled=%X{sampled} [%c{2.}] (%t) %s%e%n
```

## Метрики

Red Hat рекомендует получать метрики из Quarkus с помощью библиотеки `quarkus-micrometer-registry-prometheus`.

Чтобы узнать, как использовать метрики Micrometer в приложении Quarkus, см. руководство Quarkus [Micrometer metrics](https://quarkus.io/guides/micrometer).

Dynatrace предлагает два подхода к получению метрик Micrometer из Prometheus: через API или через расширение.

### Приём метрик Micrometer через Dynatrace API

Используйте Dynatrace API для приёма метрик, полученных из библиотеки `quarkus-micrometer-registry-prometheus`.

Подробнее о процедуре приёма см. [Отправка метрик Micrometer в Dynatrace](/managed/ingest-from/extend-dynatrace/extend-metrics/ingestion-methods/micrometer "Узнайте, как отправлять метрики Micrometer в Dynatrace.").

Для нативно собранных приложений обязательно следуйте подходу [Directly in Micrometer](/managed/ingest-from/extend-dynatrace/extend-metrics/ingestion-methods/micrometer#properties-direct "Узнайте, как отправлять метрики Micrometer в Dynatrace.").

### Приём метрик Micrometer через расширение

Используйте платформу Dynatrace [Extension 2.0](/managed/ingest-from/extensions "Узнайте, как создавать Dynatrace Extensions и управлять ими.") для приёма метрик Micrometer, полученных из [источника данных Prometheus](/managed/ingest-from/extensions/develop-your-extensions/data-sources/prometheus-extensions "Узнайте, как создать расширение Prometheus с помощью платформы Extensions."), для этого необходимо создать пользовательское расширение.

В качестве отправной точки можно использовать приведённый ниже пример пользовательского расширения. Он адаптирован под библиотеку `quarkus-micrometer-registry-prometheus`. Обязательно используйте правильный эндпоинт метрик в своей конфигурации. Эндпоинт по умолчанию: `localhost:8080/q/metrics`.

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

Dynatrace предлагает [различные варианты](/managed/ingest-from/extend-dynatrace/extend-logs "Узнайте, как расширить наблюдаемость логов в Dynatrace.") для сбора логов из ваших приложений и сред.

Чтобы узнать, как настроить логирование в приложении Quarkus, см. руководство Quarkus [Configuring logging](https://quarkus.io/guides/logging).

Для приведённой ниже процедуры предполагается, что ваше приложение записывает логи в файл `/var/log/quarkus-app.log`.

1. Запустите нативное приложение Quarkus.
2. Перейдите в **Hosts** и выберите свой хост.
3. Прокрутите вниз до раздела **Process analysis** и в списке процессов выберите процесс своего нативного приложения Quarkus.
4. В правой части панели **Process** выберите ![More](https://dt-cdn.net/images/more-icon-01c8b008ca.svg "More") > **Settings**.
5. В настройках группы процессов выберите **Log monitoring** > **Add new log for monitoring**.
6. Введите полный путь к файлу логов. Обязательно соблюдайте [требования к пути логов](/managed/analyze-explore-automate/log-monitoring/acquire-log-data/add-log-files-manually-v2#considerations-for-adding-text-log-files-manually "Узнайте, как вручную добавлять файлы логов для анализа.").
7. Выберите **Save changes**.
8. [Включите добавленные файлы логов](/managed/analyze-explore-automate/log-monitoring/acquire-log-data/add-log-files-sources-v2 "Узнайте, как включать и исключать источники логов для анализа.") в своё хранилище логов.

## Связанные темы

* [Отправка метрик Micrometer в Dynatrace](/managed/ingest-from/extend-dynatrace/extend-metrics/ingestion-methods/micrometer "Узнайте, как отправлять метрики Micrometer в Dynatrace.")
* [Управление расширениями Prometheus](/managed/ingest-from/extend-dynatrace/extend-metrics/ingestion-methods/prometheus/prometheus-extensions "Узнайте, как расширить наблюдаемость в Dynatrace с помощью декларативного приёма метрик Prometheus.")
* [Источник данных Prometheus](/managed/ingest-from/extensions/develop-your-extensions/data-sources/prometheus-extensions "Узнайте, как создать расширение Prometheus с помощью платформы Extensions.")
* [Эндпоинты Dynatrace OTLP API](/managed/ingest-from/opentelemetry/otlp-api "Узнайте об эндпоинтах OTLP API, которые ваше приложение использует для экспорта данных OpenTelemetry в Dynatrace.")