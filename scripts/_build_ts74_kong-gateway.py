# -*- coding: utf-8 -*-
"""Builder: ingest-from/technology-support/application-software/nginx/kong-gateway.md"""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from _zos_canon_l4if71 import build_one, qa_one

REL  = "ingest-from/technology-support/application-software/nginx"
FILE = "kong-gateway.md"

TRANS = {
    # --- frontmatter ---
    "title: Kong Gateway monitoring": "title: Мониторинг Kong Gateway",
    # --- headings ---
    "# Kong Gateway monitoring": "# Kong Gateway monitoring",
    "## Kong Gateway process and logs": "## Процесс и журналы Kong Gateway",
    "### Prerequisites": "### Предварительные требования",
    "## Application traces": "## Трассировки приложения",
    "## Step 1 Configure Kong Gateway": "## Шаг 1. Настройка Kong Gateway",
    "## Step 2 Configure OpenTelemetry plugin": "## Шаг 2. Настройка плагина OpenTelemetry",
    "## Step 3 Configure OpenTelemetry Collector": "## Шаг 3. Настройка OpenTelemetry Collector",
    "## Step 3 Export Application Span Metrics": "## Шаг 3. Экспорт метрик спанов приложения",
    "## Metrics": "## Метрики",
    "## Step 1 Enable Kong Prometheus plugin": "## Шаг 1. Включение плагина Kong Prometheus",
    "### Basic configuration": "### Базовая конфигурация",
    "### Additional plugin metrics": "### Дополнительные метрики плагина",
    "## Step 2 Collect Prometheus metrics": "## Шаг 2. Сбор метрик Prometheus",
    "### Scrape metrics using ActiveGate": "### Сбор метрик с помощью ActiveGate",
    "### Scrape metrics using OpenTelemetry Collector": "### Сбор метрик с помощью OpenTelemetry Collector",
    # --- meta block ---
    "* 4-min read": "* Чтение: 4 мин",
    "* Updated on Sep 04, 2024": "* Обновлено 04 сентября 2024 г.",
    # --- tab labels (plain lines without #) ---
    "OneAgent": "OneAgent",
    "OpenTelemetry": "OpenTelemetry",
    "ActiveGate": "ActiveGate",
    "OpenTelemetry Collector": "OpenTelemetry Collector",
    # --- body prose ---
    "To enable Kong Observability in Dynatrace, you have the following options.": "Для включения мониторинга Kong в Dynatrace доступны следующие варианты.",
    "* Recommended Enable OneAgent for Gateway logs, traces, and process monitoring. This should be combined with Dynatrace Prometheus scraping to monitor Kong Gateway metrics.": "* Рекомендуется: включить OneAgent для журналов шлюза, трассировок и мониторинга процессов. Этот вариант следует сочетать со сбором метрик Prometheus в Dynatrace для мониторинга метрик Kong Gateway.",
    "* Monitor Kong using a combination of OpenTelemetry for traces and Prometheus for Kong Gateway metrics.": "* Мониторинг Kong с использованием OpenTelemetry для трассировок и Prometheus для метрик Kong Gateway.",
    "OneAgent automatically monitors the Kong Gateway process and logs.": "OneAgent автоматически отслеживает процесс Kong Gateway и его журналы.",
    "* Kong Gateway version 2.8+": "* Kong Gateway версии 2.8+",
    "* OneAgent or Dynatrace Operator is installed and available for monitoring your Kong Gateway.": "* OneAgent или Dynatrace Operator установлен и доступен для мониторинга Kong Gateway.",
    "The required installation depends on your application:": "Необходимый способ установки зависит от приложения:",
    "| If your application is running | See the instruction for |": "| Если приложение выполняется | Инструкция |",
    "| --- | --- |": "| --- | --- |",
    "| on a virtual machine or bare-metal | [OneAgent](/managed/ingest-from/dynatrace-oneagent/installation-and-operation \"Install OneAgent on a server for the very first time.\") |": "| на виртуальной машине или физическом сервере | [OneAgent](/managed/ingest-from/dynatrace-oneagent/installation-and-operation \"Установка OneAgent на сервер в первый раз.\") |",
    "| as workload in Kubernetes or OpenShift | [Dynatrace Operator](/managed/ingest-from/setup-on-k8s/deployment \"Deploy Dynatrace Operator on Kubernetes\") |": "| как рабочая нагрузка в Kubernetes или OpenShift | [Dynatrace Operator](/managed/ingest-from/setup-on-k8s/deployment \"Развёртывание Dynatrace Operator в Kubernetes\") |",
    "In addition to process and logs, OneAgent also provides Kong Gateway application traces. See [Manual runtime instrumentation](/managed/ingest-from/technology-support/application-software/nginx/manual-runtime-instrumentation \"Learn how to force instrumenting patched/non-standard NGINX binaries during runtime.\") for NGINX.": "Помимо процесса и журналов, OneAgent также предоставляет трассировки приложения Kong Gateway. См. [Инструментирование во время выполнения](/managed/ingest-from/technology-support/application-software/nginx/manual-runtime-instrumentation \"Узнайте, как принудительно инструментировать пропатченные/нестандартные двоичные файлы NGINX во время выполнения.\") для NGINX.",
    "* Kong Gateway version 3.8+": "* Kong Gateway версии 3.8+",
    "Kong Gateway requires the configuration of two settings.": "Kong Gateway требует настройки двух параметров.",
    "* `tracing_instrumentations = all`": "* `tracing_instrumentations = all`",
    "* `tracing_sampling_rate = 1.0`": "* `tracing_sampling_rate = 1.0`",
    "For further details and option, see the [Kong Gateway documentation](https://dt-url.net/2m03q66).": "Подробнее о параметрах см. в [документации Kong Gateway](https://dt-url.net/2m03q66).",
    "1. Evaluate support for logging and tracing according to the [OpenTelemetry plugin version](https://dt-url.net/1423wjw) installed in your environment.": "1. Оцените поддержку ведения журналов и трассировки согласно [версии плагина OpenTelemetry](https://dt-url.net/1423wjw), установленной в вашей среде.",
    "2. Send the following POST request (example assumes Kong Gateway 3.8+) by replacing `{HOST}`, `{PLUGIN-INSTANCE_NAME}` and `{OPENTELEMETRY_COLLECTOR}` with proper values:": "2. Отправьте следующий POST-запрос (пример рассчитан на Kong Gateway 3.8+), заменив `{HOST}`, `{PLUGIN-INSTANCE_NAME}` и `{OPENTELEMETRY_COLLECTOR}` нужными значениями:",
    "Configure your OpenTelemetry Collector to send data to your Dynatrace environment. The example below shows how to export traces and logs.": "Настройте OpenTelemetry Collector для отправки данных в среду Dynatrace. Пример ниже демонстрирует экспорт трассировок и журналов.",
    "To include span metrics for application traces, configure the collector exporters section of the OpenTelemetry Collector configuration.": "Чтобы включить метрики спанов для трассировок приложения, настройте раздел exporters коллектора в конфигурации OpenTelemetry Collector.",
    "Kong’s Prometheus plugin is a convenient way to collect Kong Gateway metrics. Dynatrace can collect these metrics directly from the Gateway produced by the Kong plugin. The default port and endpoint is `8001/metrics`.": "Плагин Prometheus для Kong является удобным способом сбора метрик Kong Gateway. Dynatrace может получать эти метрики непосредственно с шлюза через плагин Kong. Порт и эндпоинт по умолчанию: `8001/metrics`.",
    "For more information and a list of available metrics, see the [Kong Prometheus plugin documentation](https://dt-url.net/gp23qq7).": "Подробнее и со списком доступных метрик см. в [документации плагина Kong Prometheus](https://dt-url.net/gp23qq7).",
    "To enable basic configuration of the Kong Prometheus plugin send a POST request replacing `{HOST}` with the host name value.": "Чтобы включить базовую конфигурацию плагина Kong Prometheus, отправьте POST-запрос, заменив `{HOST}` именем хоста.",
    "To enable additional metrics produced by the Kong Gateway Prometheus plugin, send a POST request replacing `{HOST}` and `{PLUGIN-INSTANCE_NAME}` with proper values:": "Чтобы включить дополнительные метрики плагина Kong Gateway Prometheus, отправьте POST-запрос, заменив `{HOST}` и `{PLUGIN-INSTANCE_NAME}` нужными значениями:",
    "To check available Kong metrics, query the `/metrics` endpoint:": "Чтобы проверить доступные метрики Kong, выполните запрос к эндпоинту `/metrics`:",
    "After configuring [Kong Gateway's Prometheus plugin](https://dt-url.net/gp23qq7), metrics can be collected using the Dynatrace ActiveGate (recommended) or the OpenTelemetry Collector.": "После настройки [плагина Prometheus для Kong Gateway](https://dt-url.net/gp23qq7) метрики можно собирать с помощью Dynatrace ActiveGate (рекомендуется) или OpenTelemetry Collector.",
    "In Kubernetes, Dynatrace supports scraping of Prometheus endpoints using special annotations.": "В Kubernetes Dynatrace поддерживает сбор данных с эндпоинтов Prometheus с помощью специальных аннотаций.",
    "To learn how to collect Prometheus metrics in Kubernetes, see [Monitor Prometheus metrics](/managed/observe/infrastructure-observability/container-platform-monitoring/kubernetes-monitoring/monitor-prometheus-metrics \"Metric ingestion from Prometheus endpoints in Kubernetes, metrics alerts, and monitoring consumption.\").": "Подробнее о сборе метрик Prometheus в Kubernetes см. в разделе [Мониторинг метрик Prometheus](/managed/observe/infrastructure-observability/container-platform-monitoring/kubernetes-monitoring/monitor-prometheus-metrics \"Приём метрик с эндпоинтов Prometheus в Kubernetes, алерты на метрики и потребление мониторинга.\").",
    "You can also use the OpenTelemetry Collector’s Prometheus receiver to collect metrics from the Kong Gateway. To learn how to scrape Prometheus data using an OpenTelemetry collector, see [Scrape Prometheus metrics with the OTel Collector](/managed/ingest-from/opentelemetry/collector/use-cases/prometheus \"Configure the OpenTelemetry Collector to scrape your Prometheus data.\").": "Также можно использовать receiver Prometheus в OpenTelemetry Collector для сбора метрик Kong Gateway. Подробнее о сборе данных Prometheus с помощью OpenTelemetry Collector см. в разделе [Сбор метрик Prometheus с помощью OTel Collector](/managed/ingest-from/opentelemetry/collector/use-cases/prometheus \"Настройка OpenTelemetry Collector для сбора данных Prometheus.\").",
    "If you're running on Kubernetes, you can enrich traces, metrics, and logs using the Collector's Kubernetes attribute processor. This allows Dynatrace to map the telemetry data to the correct toplogy. To learn how to enable enrichment in the OpenTelemetry Collector, see [Enrich OTLP requests with Kubernetes data](/managed/ingest-from/opentelemetry/collector/use-cases/kubernetes/k8s-enrich \"Configure the OpenTelemetry Collector to enrich OTLP requests with Kubernetes data.\").": "При работе в Kubernetes можно обогащать трассировки, метрики и журналы с помощью процессора атрибутов Kubernetes в коллекторе. Это позволяет Dynatrace сопоставлять данные телеметрии с правильной топологией. Подробнее о включении обогащения в OpenTelemetry Collector см. в разделе [Обогащение OTLP-запросов данными Kubernetes](/managed/ingest-from/opentelemetry/collector/use-cases/kubernetes/k8s-enrich \"Настройка OpenTelemetry Collector для обогащения OTLP-запросов данными Kubernetes.\").",
}

PASS = set()

if __name__ == "__main__":
    build_one(REL, FILE, TRANS, PASS)
    qa_one(REL, FILE)
