---
title: Приём записей NetFlow в Dynatrace
source: https://www.dynatrace.com/docs/observe/infrastructure-observability/networks-classic/ingest-netflow-records
scraped: 2026-03-06T21:25:43.577365
---

# Приём записей NetFlow в Dynatrace


* Классическая версия
* Практическое руководство
* 2 мин. чтения
* Обновлено 19 января 2026 г.

Наблюдаемость сети обеспечивает необходимую видимость для понимания того, как приложения взаимодействуют с базовой сетью. Она позволяет командам более эффективно выявлять и устранять проблемы, начиная с мониторинга состояния устройств и расширяя сбор данных о потоках — таких как NetFlow — для отслеживания использования сети. Такой подход активно поддерживает оптимизацию производительности, улучшает безопасность и упрощает устранение неполадок.

В этом руководстве показано, как принимать записи NetFlow в Dynatrace, настроив коллектор и используя ![Dashboards](https://dt-cdn.net/images/dashboards-512-b1f1e9690b.png "Dashboards") **Dashboards** и ![Notebooks](https://dt-cdn.net/images/notebooks-768-046137830a.webp "Notebooks") **Notebooks** для анализа данных о потоках.

## Зачем мониторить сетевые потоки с помощью Dynatrace?

Приём сетевых потоков в Dynatrace сразу помещает эти данные в контекст. Данные, содержащиеся в сетевых потоках, дополняют поддерживаемые сценарии мониторинга сетей, связывая объём и направления потоков с устройствами и интерфейсами. Данные сетевых потоков можно сравнить с данными «процесс-к-процессу» для помощи в решении проблем приложений, вызванных сетью.

## Как платформа Dynatrace поддерживает приём NetFlow?

Dynatrace поддерживает протоколы сетевых потоков, такие как NetFlow, sFlow и IPFIX, через полностью поддерживаемую версию [OpenTelemetry Collector](../../../ingest-from/opentelemetry/collector.md "Узнайте о Dynatrace OTel Collector."). Специальный приёмник сетевых потоков обеспечивает бесшовный приём данных о потоках в платформу Dynatrace для анализа и визуализации.

## Предварительные требования

* Дистрибутив [Dynatrace Collector](../../../ingest-from/opentelemetry/collector.md#dt-collector-dist "Узнайте о Dynatrace OTel Collector.") с [приёмником NetFlow](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/v0.136.0/receiver/netflowreceiver).
* [URL конечной точки Dynatrace API](../../../ingest-from/opentelemetry/otlp-api.md "Узнайте о конечных точках OTLP API, которые ваше приложение использует для экспорта данных OpenTelemetry в Dynatrace."), на которую должны экспортироваться данные.
* [API-токен](../../../ingest-from/opentelemetry/otlp-api.md#authentication-export-to-activegate "Узнайте о конечных точках OTLP API, которые ваше приложение использует для экспорта данных OpenTelemetry в Dynatrace.") с областями **Ingest logs** (`logs.ingest`) и **Ingest metrics** (`metrics.ingest`). Подробнее см. [Самомониторинг OpenTelemetry Collector](../../../ingest-from/opentelemetry/collector/self-monitoring.md "Как мониторить OpenTelemetry Collectors с помощью панелей Dynatrace.").

См. [Развёртывание Collector](../../../ingest-from/opentelemetry/collector/deployment.md "Как развернуть Dynatrace OTel Collector.") и [Конфигурация Collector](../../../ingest-from/opentelemetry/collector/configuration.md "Как настроить OpenTelemetry Collector.") для настройки вашего Collector с конфигурацией ниже.

## Шаги

В этом примере мы развёртываем с помощью Docker для простоты демонстрации. Для производственных сценариев мы рекомендуем развёртывание в качестве шлюза на кластере Kubernetes. Подробнее см. [Настройка OpenTelemetry Collector для мониторинга Kubernetes](../../../ingest-from/opentelemetry/collector/use-cases/kubernetes/k8s-monitoring.md "Настройка OpenTelemetry Collector для мониторинга ваших кластеров Kubernetes.").

1. Для настройки экземпляра Dynatrace Collector создайте файл `otel-collector-config.yaml` и добавьте следующую конфигурацию:

   ```
   receivers:


   netflow:


   scheme: netflow


   port: 2055


   sockets: 16


   workers: 32


   netflow/sflow:


   scheme: sflow


   port: 6343


   sockets: 16


   workers: 32


   processors:


   batch:


   send_batch_size: 2000


   timeout: 30s


   exporters:


   otlp_http:


   endpoint: "${env:DT_ENDPOINT}"


   headers:


   Authorization: "Api-Token ${env:DT_API_TOKEN}"


   service:


   pipelines:


   logs:


   receivers: [netflow, netflow/sflow]


   processors: [batch]


   exporters: [otlp_http]


   telemetry:


   logs:


   level: debug
   ```

   Проверьте документацию [приёмника NetFlow](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/v0.136.0/receiver/netflowreceiver#netflow-receiver) для доступных параметров конфигурации.
2. Создайте файл `.env` для добавления переменных `DT_ENDPOINT` и `DT_API_TOKEN`.

   * `DT_ENDPOINT` — конечная точка API-сервера Dynatrace. Содержит [базовый URL конечной точки Dynatrace API](../../../ingest-from/opentelemetry/otlp-api.md#export-to-activegate "Узнайте о конечных точках OTLP API, которые ваше приложение использует для экспорта данных OpenTelemetry в Dynatrace."). Например, `https://{your-environment-id}.live.dynatrace.com/api/v2/otlp`. Подробнее см. [Интеграция OneAgent в Azure App Service для Linux и контейнеров](../../../ingest-from/microsoft-azure-services/azure-integrations/azure-appservice/integrate-oneagent-on-web-app-for-containers.md "Узнайте, как установить, настроить, обновить и удалить OneAgent в контейнерных приложениях на Linux.").
   * `DT_API_TOKEN` содержит [API-токен](../../../ingest-from/opentelemetry/otlp-api.md#authentication-export-to-activegate "Узнайте о конечных точках OTLP API, которые ваше приложение использует для экспорта данных OpenTelemetry в Dynatrace.").

   Убедитесь, что ваш файл `.env` надёжно защищён и недоступен для неавторизованного доступа, так как он содержит конфиденциальную информацию.
3. Создайте токен доступа, перейдя в **Access Tokens** > **Создать новый токен** и выбрав **Ingest logs** в качестве области.
4. Запустите образ Collector в Docker с помощью следующей команды:

   ```
   docker run -p 2055:2055 --env-file ./.dt_token.env -v $(pwd)/otel-collector-config.yaml:/etc/otelcol/otel-collector-config.yaml ghcr.io/dynatrace/dynatrace-otel-collector/dynatrace-otel-collector:0.33.0 --config=/etc/otelcol/otel-collector-config.yaml
   ```

   После завершения процесса вы можете начать запуск и обработку данных.

   Если вы хотите, чтобы процесс работал в фоновом режиме, вы можете завершить его и запустить снова с опцией `-d`.
5. Настройте ваши сетевые устройства для отправки записей NetFlow в Collector.

   Конфигурация сетевого устройства зависит от производителя. Она должна указывать IP-адрес конечной точки Dynatrace и соответствующий UDP-порт.

## Визуализация и анализ данных

### Анализ логов

Данные NetFlow принимаются как записи логов, которые можно запрашивать и визуализировать с помощью DQL. Вы можете использовать [![Logs](https://dt-cdn.net/images/logs-256-ae0a9ca67f.png "Logs") **Logs**](https://www.dynatrace.com/hub/detail/logs/) для поиска логов контейнеров, захваченных OneAgent для Collector:

![Ошибки OpenTelemetry, отображённые в приложении Logs](https://dt-cdn.net/images/open-telemetry-errors-2163-955bbf8cf3.png)

Аналогично, ![Logs](https://dt-cdn.net/images/logs-256-ae0a9ca67f.png "Logs") **Logs** может помочь вам убедиться, что трафик действительно поступает:

![Поток трафика NetFlow в приложении Logs](https://dt-cdn.net/images/logs-netflow-trafic-flow-2022-d387c3206a.png)

### Панели

![Dashboards](https://dt-cdn.net/images/dashboards-512-b1f1e9690b.png "Dashboards") **Dashboards** предоставляет готовую панель **NetFlow Overview** в качестве отправной точки для изучения и визуализации данных NetFlow. Она включает предварительно настроенные графики и метрики для анализа сетевого трафика, таких как основные источники, назначения, разговоры и использование портов.

![Обзор NetFlow в Dashboards](https://dt-cdn.net/images/dashboards-netflow-overview-1619-1e3c5ca7d8.png)

Панель может быть использована как основа для дальнейшей кастомизации. Вы также можете создать пользовательские панели для визуализации данных NetFlow с использованием различных типов графиков.

### Notebooks

![Notebooks](https://dt-cdn.net/images/notebooks-768-046137830a.webp "Notebooks") **Notebooks** позволяет запускать запросы и интерактивно визуализировать данные NetFlow. Вы можете открыть новый notebook из ![Logs](https://dt-cdn.net/images/logs-256-ae0a9ca67f.png "Logs") **Logs**, перейдя в **Открыть с помощью** и выбрав ![Notebooks](https://dt-cdn.net/images/notebooks-768-046137830a.webp "Notebooks") **Notebooks**.

Пример DQL-запроса

С помощью этого DQL-запроса вы можете получить сводку байтов по IP-адресу и порту назначения:

```
fetch logs


| filter matchesValue(flow.type, "netflow_v9")


| summarize {totalBytes= sum(toLong(flow.io.bytes)),totalPackets=sum(toLong(flow.io.packets))}, by: {destination.address,destination.port}


| sort totalBytes desc


| limit 10
```

![Сводка байтов по IP-адресу и порту назначения в Notebooks](https://dt-cdn.net/images/notebooks-netflow-bytes-by-dest-id-and-port-1310-aa7ceb24fe.png)

## Связанные темы

* [Приём NetFlow с помощью OpenTelemetry Collector](../../../ingest-from/opentelemetry/collector/use-cases/netflow.md "Настройка OpenTelemetry Collector для приёма данных NetFlow.")