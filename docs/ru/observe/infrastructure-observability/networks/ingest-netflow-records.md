---
title: Ingest NetFlow records into Dynatrace
source: https://www.dynatrace.com/docs/observe/infrastructure-observability/networks/ingest-netflow-records
scraped: 2026-03-02T21:20:28.336015
---

# Загрузка записей NetFlow в Dynatrace

# Загрузка записей NetFlow в Dynatrace

* How-to guide
* 2-min read
* Updated on Jan 19, 2026

Наблюдаемость сети обеспечивает необходимую видимость для понимания того, как приложения взаимодействуют с базовой сетью. Она позволяет командам более эффективно выявлять и устранять проблемы, начиная с мониторинга состояния устройств и расширяясь до сбора данных о потоках — таких как NetFlow — для отслеживания использования сети. Такой подход активно поддерживает оптимизацию производительности, повышает безопасность и упрощает устранение неполадок.

Это руководство показывает, как загрузить записи NetFlow в Dynatrace, настроив коллектор и используя ![Dashboards](https://dt-cdn.net/images/dashboards-512-b1f1e9690b.png "Dashboards") **Dashboards** и ![Notebooks](https://dt-cdn.net/images/notebooks-768-046137830a.webp "Notebooks") **Notebooks** для анализа данных потоков.

## Зачем мониторить сетевые потоки с Dynatrace?

Загрузка сетевых потоков в Dynatrace немедленно помещает эти данные в контекст. Данные, содержащиеся в сетевых потоках, дополняют поддерживаемые сценарии использования сети, связывая объём и направления потоков с устройствами и интерфейсами. Данные сетевых потоков можно сравнивать с данными о взаимодействии процессов для решения сетевых проблем приложений.

## Как платформа Dynatrace поддерживает загрузку NetFlow?

Dynatrace поддерживает протоколы сетевых потоков, такие как NetFlow, sFlow и IPFIX, через полностью поддерживаемую версию [OpenTelemetry Collector](/docs/ingest-from/opentelemetry/collector "Learn about the Dynatrace OTel Collector."). Специализированный приёмник сетевых потоков обеспечивает бесшовную загрузку данных потоков в платформу Dynatrace для анализа и визуализации.

## Предварительные требования

* Дистрибутив [Dynatrace Collector](/docs/ingest-from/opentelemetry/collector#dt-collector-dist "Learn about the Dynatrace OTel Collector.") с [приёмником NetFlow](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/v0.136.0/receiver/netflowreceiver).
* [URL конечной точки Dynatrace API](/docs/ingest-from/opentelemetry/otlp-api "Learn about the OTLP API endpoints that your application uses to export OpenTelemetry data to Dynatrace."), куда должны экспортироваться данные.
* [API-токен](/docs/ingest-from/opentelemetry/otlp-api#authentication-export-to-activegate "Learn about the OTLP API endpoints that your application uses to export OpenTelemetry data to Dynatrace.") с правами **Ingest logs** (`logs.ingest`) и **Ingest metrics** (`metrics.ingest`). Подробнее см. [OpenTelemetry Collector self-monitoring](/docs/ingest-from/opentelemetry/collector/self-monitoring "How to monitor OpenTelemetry Collectors with Dynatrace dashboards.").

См. [Collector Deployment](/docs/ingest-from/opentelemetry/collector/deployment "How to deploy Dynatrace OTel Collector.") и [Collector Configuration](/docs/ingest-from/opentelemetry/collector/configuration "How to configure the OpenTelemetry Collector.") для настройки вашего Collector с конфигурацией, указанной ниже.

## Шаги

В этом примере мы используем развёртывание через Docker для простоты демонстрации. Для промышленного использования рекомендуется развёртывание в качестве шлюза на кластере Kubernetes. Подробнее см. [Configure OpenTelemetry Collector for Kubernetes monitoring](/docs/ingest-from/opentelemetry/collector/use-cases/kubernetes/k8s-monitoring "Configure the OpenTelemetry Collector to monitor your Kubernetes clusters.").

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

   Ознакомьтесь с документацией [приёмника NetFlow](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/v0.136.0/receiver/netflowreceiver#netflow-receiver) для получения информации о доступных параметрах конфигурации.
2. Создайте файл `.env` для добавления переменных `DT_ENDPOINT` и `DT_API_TOKEN`.

   * `DT_ENDPOINT` — конечная точка сервера API Dynatrace. Содержит [базовый URL конечной точки API Dynatrace](/docs/ingest-from/opentelemetry/otlp-api#export-to-activegate "Learn about the OTLP API endpoints that your application uses to export OpenTelemetry data to Dynatrace."). Например, `https://{your-environment-id}.live.dynatrace.com/api/v2/otlp`. Подробнее см. [Integrate OneAgent on Azure App Service for Linux and containers](/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-appservice/integrate-oneagent-on-web-app-for-containers "Learn how to install, configure, update, and uninstall OneAgent in containerized applications on Linux.").
   * `DT_API_TOKEN` содержит [API-токен](/docs/ingest-from/opentelemetry/otlp-api#authentication-export-to-activegate "Learn about the OTLP API endpoints that your application uses to export OpenTelemetry data to Dynatrace.").

   Убедитесь, что ваш файл `.env` надёжно защищён и не доступен неавторизованным пользователям, так как он содержит конфиденциальную информацию.
3. Создайте токен доступа, перейдя в **Access Tokens** > **Generate new token** и выбрав **Ingest logs** в качестве области действия.
4. Запустите образ Collector в Docker с помощью следующей команды:

   ```
   docker run -p 2055:2055 --env-file ./.dt_token.env -v $(pwd)/otel-collector-config.yaml:/etc/otelcol/otel-collector-config.yaml ghcr.io/dynatrace/dynatrace-otel-collector/dynatrace-otel-collector:0.33.0 --config=/etc/otelcol/otel-collector-config.yaml
   ```

   После завершения процесса вы можете начать работу и обработку данных.

   Если вы хотите, чтобы процесс работал в фоновом режиме, вы можете остановить его и запустить снова с параметром `-d`.
5. Направьте ваши сетевые устройства на отправку записей NetFlow в Collector.

   Конфигурация сетевого устройства зависит от производителя. Она должна указывать IP-адрес конечной точки Dynatrace и соответствующий UDP-порт.

## Визуализация и анализ данных

### Анализ логов

Данные NetFlow загружаются в виде записей логов, которые можно запрашивать и визуализировать с помощью DQL. Вы можете использовать [![Logs](https://dt-cdn.net/images/logs-256-ae0a9ca67f.png "Logs") **Logs**](https://www.dynatrace.com/hub/detail/logs/) для просмотра логов контейнеров, захваченных OneAgent для Collector:

![OpenTelemetry errors displayed in the Logs app](https://dt-cdn.net/images/open-telemetry-errors-2163-955bbf8cf3.png)

Аналогично, ![Logs](https://dt-cdn.net/images/logs-256-ae0a9ca67f.png "Logs") **Logs** поможет вам убедиться, что трафик действительно передаётся:

![Traffic flow with NetFlow in the Logs app](https://dt-cdn.net/images/logs-netflow-trafic-flow-2022-d387c3206a.png)

### Дашборды

![Dashboards](https://dt-cdn.net/images/dashboards-512-b1f1e9690b.png "Dashboards") **Dashboards** предоставляет готовый дашборд **NetFlow Overview** в качестве отправной точки для изучения и визуализации данных NetFlow. Он включает предварительно настроенные диаграммы и метрики для анализа сетевого трафика, такие как основные источники, назначения, соединения и использование портов.

![Dashboards NetFlow Overview](https://dt-cdn.net/images/dashboards-netflow-overview-1619-1e3c5ca7d8.png)

Дашборд можно использовать как основу для дальнейшей настройки. Вы также можете создавать пользовательские дашборды для визуализации данных NetFlow с использованием различных типов диаграмм.

### Notebooks

![Notebooks](https://dt-cdn.net/images/notebooks-768-046137830a.webp "Notebooks") **Notebooks** позволяет выполнять запросы и визуализировать данные NetFlow в интерактивном режиме. Вы можете открыть новый notebook из ![Logs](https://dt-cdn.net/images/logs-256-ae0a9ca67f.png "Logs") **Logs**, перейдя в **Open with** и выбрав ![Notebooks](https://dt-cdn.net/images/notebooks-768-046137830a.webp "Notebooks") **Notebooks**.

Пример запроса DQL

С помощью этого запроса DQL вы можете получить сводку байтов по IP-адресу назначения и порту:

```
fetch logs



| filter matchesValue(flow.type, "netflow_v9")



| summarize {totalBytes= sum(toLong(flow.io.bytes)),totalPackets=sum(toLong(flow.io.packets))}, by: {destination.address,destination.port}



| sort totalBytes desc



| limit 10
```

![Summary of bytes by destination IP and port in Notebooks](https://dt-cdn.net/images/notebooks-netflow-bytes-by-dest-id-and-port-1310-aa7ceb24fe.png)

## Связанные темы

* [Ingest NetFlow with the OpenTelemetry Collector](/docs/ingest-from/opentelemetry/collector/use-cases/netflow "Configure the OpenTelemetry Collector to ingest NetFlow data.")
