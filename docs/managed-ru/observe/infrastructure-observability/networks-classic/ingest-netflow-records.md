---
title: Приём записей NetFlow в Dynatrace
source: https://docs.dynatrace.com/managed/observe/infrastructure-observability/networks-classic/ingest-netflow-records
scraped: 2026-05-12T12:03:22.289440
---

# Приём записей NetFlow в Dynatrace

# Приём записей NetFlow в Dynatrace

* How-to guide
* 2-min read
* Updated on Jan 19, 2026

Наблюдаемость сети обеспечивает необходимую видимость для понимания того, как приложения взаимодействуют с базовой сетью. Она позволяет командам более эффективно выявлять и устранять проблемы, начиная с мониторинга состояния устройств и переходя к сбору данных о потоках — таких как NetFlow — для отслеживания использования сети. Такой подход активно поддерживает оптимизацию производительности, повышает безопасность и упрощает устранение неполадок.

В этом руководстве показано, как принимать записи NetFlow в Dynatrace путём настройки коллектора.

## Зачем мониторить сетевые потоки с помощью Dynatrace?

Приём сетевых потоков в Dynatrace немедленно помещает эти данные в контекст. Данные, содержащиеся в сетевых потоках, дополняют поддерживаемые сценарии использования сети, связывая объём потоков и их направления с устройствами и интерфейсами. Данные сетевых потоков можно сравнивать с данными процесс-процесс для решения сетевых проблем приложений.

## Как платформа Dynatrace поддерживает приём NetFlow?

Dynatrace поддерживает протоколы сетевых потоков, такие как NetFlow, sFlow и IPFIX, через полностью поддерживаемую версию [OpenTelemetry Collector](/managed/ingest-from/opentelemetry/collector "Узнайте, как использовать OpenTelemetry Collector, включая Dynatrace OTel Collector, для приёма телеметрии из OpenTelemetry."). Специализированный получатель сетевых потоков обеспечивает бесшовный приём данных потоков на платформу Dynatrace для анализа и визуализации.

## Предварительные требования

* Дистрибутив [Dynatrace Collector](/managed/ingest-from/opentelemetry/collector#dt-collector-dist "Узнайте, как использовать OpenTelemetry Collector, включая Dynatrace OTel Collector, для приёма телеметрии из OpenTelemetry.") с [получателем NetFlow](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/v0.136.0/receiver/netflowreceiver).
* [URL конечной точки Dynatrace API](/managed/ingest-from/opentelemetry/otlp-api "Узнайте о конечных точках OTLP API, которые ваше приложение использует для экспорта данных OpenTelemetry в Dynatrace."), на которую должны экспортироваться данные.
* [Токен API](/managed/ingest-from/opentelemetry/otlp-api#authentication-export-to-activegate "Узнайте о конечных точках OTLP API, которые ваше приложение использует для экспорта данных OpenTelemetry в Dynatrace.") с областями действия **Ingest logs** (`logs.ingest`) и **Ingest metrics** (`metrics.ingest`).

Инструкции по настройке коллектора с указанной ниже конфигурацией см. в разделах [Развёртывание коллектора](/managed/ingest-from/opentelemetry/collector/deployment "Как развернуть OpenTelemetry Collector Dynatrace.") и [Конфигурация коллектора](/managed/ingest-from/opentelemetry/collector/configuration "Как настроить OpenTelemetry Collector.").

## Шаги

В данном примере развёртывание выполняется с использованием Docker для простоты демонстрации. Для производственных сценариев рекомендуется развёртывание в качестве шлюза на кластере Kubernetes. Подробности см. в разделе [Настройка OpenTelemetry Collector для мониторинга Kubernetes](/managed/ingest-from/opentelemetry/collector/use-cases/kubernetes/k8s-monitoring "Настройка OpenTelemetry Collector для мониторинга кластеров Kubernetes.").

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

   Доступные параметры конфигурации см. в документации [NetFlow receiver](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/v0.136.0/receiver/netflowreceiver#netflow-receiver).
2. Создайте файл `.env` для добавления переменных `DT_ENDPOINT` и `DT_API_TOKEN`.

   * `DT_ENDPOINT` — конечная точка сервера Dynatrace API. Содержит [базовый URL конечной точки Dynatrace API](/managed/ingest-from/opentelemetry/otlp-api#export-to-activegate "Узнайте о конечных точках OTLP API, которые ваше приложение использует для экспорта данных OpenTelemetry в Dynatrace."). Например, `https://{your-environment-id}.live.dynatrace.com/api/v2/otlp`. Подробности см. в разделе [Интеграция OneAgent в Azure App Service для Linux и контейнеров](/managed/ingest-from/microsoft-azure-services/azure-integrations/azure-appservice/integrate-oneagent-on-web-app-for-containers "Узнайте, как установить, настроить, обновить и удалить OneAgent в контейнеризованных приложениях на Linux.").
   * `DT_API_TOKEN` содержит [токен API](/managed/ingest-from/opentelemetry/otlp-api#authentication-export-to-activegate "Узнайте о конечных точках OTLP API, которые ваше приложение использует для экспорта данных OpenTelemetry в Dynatrace.").

   Убедитесь, что файл `.env` надлежащим образом защищён и не доступен неавторизованным пользователям, поскольку содержит конфиденциальную информацию.
3. Создайте токен доступа, перейдя в **Access Tokens** > **Generate new token** и выбрав **Ingest logs** в качестве области действия.
4. Запустите образ Collector в Docker с помощью следующей команды:

   ```
   docker run -p 2055:2055 --env-file ./.dt_token.env -v $(pwd)/otel-collector-config.yaml:/etc/otelcol/otel-collector-config.yaml ghcr.io/dynatrace/dynatrace-otel-collector/dynatrace-otel-collector:0.33.0 --config=/etc/otelcol/otel-collector-config.yaml
   ```

   После завершения процесса можно начать запуск и обработку данных.

   Если нужно, чтобы процесс выполнялся в фоновом режиме, можно завершить его и запустить снова с параметром `-d`.
5. Настройте сетевые устройства для отправки записей NetFlow в Collector.

   Конфигурация сетевого устройства зависит от поставщика. В ней необходимо указать IP-адрес конечной точки Dynatrace и соответствующий порт UDP.

Приём NetFlow успешно настроен. Данные сетевых потоков теперь доступны в Dynatrace для анализа.

## Связанные темы

* [Приём NetFlow с помощью OTel Collector](/managed/ingest-from/opentelemetry/collector/use-cases/netflow "Настройка OpenTelemetry Collector для приёма данных NetFlow.")