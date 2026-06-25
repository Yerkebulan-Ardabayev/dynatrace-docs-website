# -*- coding: utf-8 -*-
"""L4-IF.67 builder: opentelemetry/collector/use-cases/kafka subtree (4 files).

Same prose line-parity engine as _build_meta_l4if58.py:
- line-parity (EN line count == RU line count),
- byte-identical code fences / blank lines / source: / scraped: / ---,
- URL identity (link/anchor targets copied verbatim inside translated lines),
- LF line endings, clean RU (no em-dash, no mojibake/BOM).

EN sources carry two mojibake families that norm() resolves before matching:
- BOM-class `ï»¿` / U+FEFF before some `]` (stripped entirely),
- `â\x80\x94` (mojibaked em-dash) and `â\x80\x99` (mojibaked apostrophe) in
  kafka.md, mapped back to real chars so TRANS keys stay readable.
RU output is built from the value side only, so it is always clean.

OTel Collector component canon (this batch; reuse for collector/ remainder):
  receiver / exporter / processor -> EN (config-block kinds, parallels established
  exporter=EN); pipeline -> конвейер; OTel Collector / Collector / OTLP / Kafka -> EN.
"""

import os
import re

BOM_CLS = re.compile("[﻿ï»¿]")


def norm(s):
    s = s.replace("â", "—")  # mojibaked em-dash -> em-dash
    s = s.replace("â", "'")  # mojibaked apostrophe -> '
    return BOM_CLS.sub("", s)


BASE = os.path.join(os.path.dirname(__file__), "..", "docs")
SUB_HUB = "ingest-from/opentelemetry/collector/use-cases"
SUB_KAFKA = "ingest-from/opentelemetry/collector/use-cases/kafka"

REL = {
    "kafka.md": SUB_HUB,
    "exporter.md": SUB_KAFKA,
    "receiver.md": SUB_KAFKA,
    "kafkametrics.md": SUB_KAFKA,
}

# ---------------------------------------------------------------------------
# Recurring lines shared across the children (identical EN -> identical RU).
C = {
    # related topics
    '* [OTel Collector for ingesting telemetry into Dynatrace](/managed/ingest-from/opentelemetry/collector "Learn how to use the OpenTelemetry Collector, including the Dynatrace OTel Collector, to ingest telemetry from OpenTelemetry.")': '* [OTel Collector для приёма телеметрии в Dynatrace](/managed/ingest-from/opentelemetry/collector "Узнайте, как использовать OpenTelemetry Collector, включая Dynatrace OTel Collector, для приёма телеметрии из OpenTelemetry.")',
    '* [Forward OpenTelemetry data with the Kafka exporter](/managed/ingest-from/opentelemetry/collector/use-cases/kafka/exporter "How to configure the OpenTelemetry Collector to forward OpenTelemetry data with the Kafka exporter.")': '* [Пересылка данных OpenTelemetry с помощью exporter Kafka](/managed/ingest-from/opentelemetry/collector/use-cases/kafka/exporter "Как настроить OpenTelemetry Collector для пересылки данных OpenTelemetry с помощью exporter Kafka.")',
    '* [Receive OpenTelemetry data with the Kafka receiver](/managed/ingest-from/opentelemetry/collector/use-cases/kafka/receiver "How to configure the OpenTelemetry Collector\'s Kafka receiver to ingest OpenTelemetry from Kafka.")': '* [Приём данных OpenTelemetry с помощью receiver Kafka](/managed/ingest-from/opentelemetry/collector/use-cases/kafka/receiver "Как настроить receiver Kafka в OpenTelemetry Collector для приёма OpenTelemetry из Kafka.")',
    '* [Buffer data via Kafka with OTel Collector](/managed/ingest-from/opentelemetry/collector/use-cases/kafka "How to configure the OpenTelemetry Collector to buffer data via Kafka.")': '* [Буферизация данных через Kafka с помощью OTel Collector](/managed/ingest-from/opentelemetry/collector/use-cases/kafka "Как настроить OpenTelemetry Collector для буферизации данных через Kafka.")',
    '* [Deploy the Dynatrace OTel Collector](/managed/ingest-from/opentelemetry/collector/deployment "How to deploy the Dynatrace OpenTelemetry Collector.")': '* [Развёртывание Dynatrace OTel Collector](/managed/ingest-from/opentelemetry/collector/deployment "Как развернуть Dynatrace OpenTelemetry Collector.")',
    '* [Configure the OTel Collector](/managed/ingest-from/opentelemetry/collector/configuration "How to configure the OpenTelemetry Collector.")': '* [Настройка OTel Collector](/managed/ingest-from/opentelemetry/collector/configuration "Как настроить OpenTelemetry Collector.")',
    # prerequisites sub-bullets (Collector distributions)
    '+ [Dynatrace Collector](/managed/ingest-from/opentelemetry/collector#dt-collector-dist "Learn how to use the OpenTelemetry Collector, including the Dynatrace OTel Collector, to ingest telemetry from OpenTelemetry.")': '+ [Dynatrace Collector](/managed/ingest-from/opentelemetry/collector#dt-collector-dist "Узнайте, как использовать OpenTelemetry Collector, включая Dynatrace OTel Collector, для приёма телеметрии из OpenTelemetry.")',
    '+ [OpenTelemetry Contrib](/managed/ingest-from/opentelemetry/collector#collector-contrib "Learn how to use the OpenTelemetry Collector, including the Dynatrace OTel Collector, to ingest telemetry from OpenTelemetry.")': '+ [OpenTelemetry Contrib](/managed/ingest-from/opentelemetry/collector#collector-contrib "Узнайте, как использовать OpenTelemetry Collector, включая Dynatrace OTel Collector, для приёма телеметрии из OpenTelemetry.")',
    # Kafka server prereq + quickstart
    "* A Kafka server deployed with a reachable `BROKER_ADDRESS`.": "* Развёрнутый сервер Kafka с доступным `BROKER_ADDRESS`.",
    "For more information, see the [Kafka Apache quickstart guide](https://kafka.apache.org/quickstart).": "Дополнительные сведения см. в [руководстве по быстрому старту Apache Kafka](https://kafka.apache.org/quickstart).",
    # API endpoint / token prereqs (shared receiver + kafkametrics)
    '* The [Dynatrace API endpoint URL](/managed/ingest-from/opentelemetry/otlp-api "Learn about the OTLP API endpoints that your application uses to export OpenTelemetry data to Dynatrace.") to which the data should be exported.': '* [URL эндпоинта Dynatrace API](/managed/ingest-from/opentelemetry/otlp-api "Узнайте об эндпоинтах OTLP API, которые ваше приложение использует для экспорта данных OpenTelemetry в Dynatrace."), на который должны экспортироваться данные.',
    # components intro + validation
    "For our configuration, we configure certain components as described in the sections below.": "Для нашей конфигурации мы настраиваем определённые компоненты, как описано в разделах ниже.",
    "Configuration validation": "Проверка конфигурации",
    '[Validate your settings](/managed/ingest-from/opentelemetry/collector/configuration#validate "How to configure the OpenTelemetry Collector.") to avoid any configuration issues.': '[Проверьте ваши настройки](/managed/ingest-from/opentelemetry/collector/configuration#validate "Как настроить OpenTelemetry Collector."), чтобы избежать проблем с конфигурацией.',
    "For this purpose, we set the following two environment variables and reference them in the configuration values for `endpoint` and `Authorization`.": "Для этого мы задаём следующие две переменные окружения и ссылаемся на них в значениях конфигурации `endpoint` и `Authorization`.",
    '* `DT_ENDPOINT` contains the [base URL of the Dynatrace API endpoint](/managed/ingest-from/opentelemetry/otlp-api#export-to-activegate "Learn about the OTLP API endpoints that your application uses to export OpenTelemetry data to Dynatrace.") (for example, `https://{your-environment-id}.live.dynatrace.com/api/v2/otlp`).': '* `DT_ENDPOINT` содержит [базовый URL эндпоинта Dynatrace API](/managed/ingest-from/opentelemetry/otlp-api#export-to-activegate "Узнайте об эндпоинтах OTLP API, которые ваше приложение использует для экспорта данных OpenTelemetry в Dynatrace.") (например, `https://{your-environment-id}.live.dynatrace.com/api/v2/otlp`).',
    '* `DT_API_TOKEN` contains the [API token](/managed/ingest-from/opentelemetry/otlp-api#authentication-export-to-activegate "Learn about the OTLP API endpoints that your application uses to export OpenTelemetry data to Dynatrace.").': '* `DT_API_TOKEN` содержит [API-токен](/managed/ingest-from/opentelemetry/otlp-api#authentication-export-to-activegate "Узнайте об эндпоинтах OTLP API, которые ваше приложение использует для экспорта данных OpenTelemetry в Dynatrace.").',
}

# ---------------------------------------------------------------------------
TRANS = {
    "kafka.md": {
        "title: Buffer data via Kafka with OTel Collector": "title: Буферизация данных через Kafka с помощью OTel Collector",
        "# Buffer data via Kafka with OTel Collector": "# Буферизация данных через Kafka с помощью OTel Collector",
        "* Explanation": "* Пояснение",
        "* 1-min read": "* Чтение: 1 мин",
        "* Updated on May 04, 2026": "* Обновлено 04 мая 2026 г.",
        "When you use Apache Kafka as the transport layer for OTLP, you add durability, scale, and flexibility to your observability pipelines.": "Когда вы используете Apache Kafka как транспортный слой для OTLP, вы повышаете надёжность, масштабируемость и гибкость своих конвейеров наблюдаемости.",
        "Kafka decouples producers (OTel Collector agents) from consumers (Collector gateways).": "Kafka разделяет производителей (агенты OTel Collector) и потребителей (шлюзы Collector).",
        "This helps to:": "Это помогает:",
        "* Absorb traffic spikes with persistent buffering.": "* Поглощать всплески трафика за счёт постоянной буферизации.",
        "* Survive network and backend failures.": "* Переживать сбои сети и бэкенда.",
        "* Enable fan-out to multiple downstream systems.": "* Обеспечивать веерное распределение данных по нескольким нижестоящим системам.",
        "You can reliably perform the necessary enrichment on high-volume, bursty telemetry—all while keeping your data streams protected.": "Необходимое обогащение телеметрии большого объёма с резкими всплесками можно надёжно выполнять, сохраняя при этом защиту потоков данных.",
        "## Overview": "## Обзор",
        "You can configure Kafka exporter, Kafka receiver, and Kafka Metrics receiver components, as shown in the figure below.": "Можно настроить компоненты Kafka exporter, Kafka receiver и Kafka Metrics receiver, как показано на рисунке ниже.",
        "* Exporter: Write OTLP data as Kafka messages on a per-signal basis (`otlp_logs`, `otlp_metrics`, `otlp_spans`).": "* Exporter: записывает данные OTLP в виде сообщений Kafka по каждому сигналу отдельно (`otlp_logs`, `otlp_metrics`, `otlp_spans`).",
        "* Receiver: Consume traces, metrics, and logs from Apache Kafka topics, and then forward these to backends such as Dynatrace.": "* Receiver: потребляет трассировки, метрики и логи из топиков Apache Kafka, а затем пересылает их в бэкенды, такие как Dynatrace.",
        "* Kafka metrics receiver: Collect Kafka's own operational metrics (for example, `broker count`) via OTLP and export them to Dynatrace.": "* Kafka metrics receiver: собирает собственные операционные метрики Kafka (например, `broker count`) через OTLP и экспортирует их в Dynatrace.",
        "Note that running Kafka may introduce additional end-to-end latencies, operational overhead, and potential bottlenecks.": "Обратите внимание, что запуск Kafka может привнести дополнительные сквозные задержки, операционные накладные расходы и потенциальные узкие места.",
        "Communication between OTel Collector and Kafka server": "Обмен данными между OTel Collector и сервером Kafka",
        "## Configuration": "## Настройка",
        "Configure your Collectors to start sending data to/from Kafka and the Dynatrace backend.": "Настройте ваши экземпляры Collector, чтобы начать отправку данных в Kafka и из неё, а также в бэкенд Dynatrace.",
        'Configure the Collector to export OTLP data to Kafka server.](/managed/ingest-from/opentelemetry/collector/use-cases/kafka/exporter "How to configure the OpenTelemetry Collector to forward OpenTelemetry data with the Kafka exporter.")[### Receiver': 'Настройте Collector для экспорта данных OTLP на сервер Kafka.](/managed/ingest-from/opentelemetry/collector/use-cases/kafka/exporter "Как настроить OpenTelemetry Collector для пересылки данных OpenTelemetry с помощью exporter Kafka.")[### Receiver',
        'Configure the Collector to receive OTLP data from Kafka server.](/managed/ingest-from/opentelemetry/collector/use-cases/kafka/receiver "How to configure the OpenTelemetry Collector\'s Kafka receiver to ingest OpenTelemetry from Kafka.")[### Kafka Metrics Receiver': 'Настройте Collector для приёма данных OTLP с сервера Kafka.](/managed/ingest-from/opentelemetry/collector/use-cases/kafka/receiver "Как настроить receiver Kafka в OpenTelemetry Collector для приёма OpenTelemetry из Kafka.")[### Kafka Metrics Receiver',
        'Configure the Collector to collect Kafka operational metrics and export them to Dynatrace.](/managed/ingest-from/opentelemetry/collector/use-cases/kafka/kafkametrics "How to configure the OpenTelemetry Collector to gather metrics from your Kafka server.")': 'Настройте Collector для сбора операционных метрик Kafka и их экспорта в Dynatrace.](/managed/ingest-from/opentelemetry/collector/use-cases/kafka/kafkametrics "Как настроить OpenTelemetry Collector для сбора метрик с вашего сервера Kafka.")',
        "## Related topics": "## Связанные темы",
        **{
            k: C[k]
            for k in (
                '* [OTel Collector for ingesting telemetry into Dynatrace](/managed/ingest-from/opentelemetry/collector "Learn how to use the OpenTelemetry Collector, including the Dynatrace OTel Collector, to ingest telemetry from OpenTelemetry.")',
                '* [Forward OpenTelemetry data with the Kafka exporter](/managed/ingest-from/opentelemetry/collector/use-cases/kafka/exporter "How to configure the OpenTelemetry Collector to forward OpenTelemetry data with the Kafka exporter.")',
                '* [Receive OpenTelemetry data with the Kafka receiver](/managed/ingest-from/opentelemetry/collector/use-cases/kafka/receiver "How to configure the OpenTelemetry Collector\'s Kafka receiver to ingest OpenTelemetry from Kafka.")',
            )
        },
        '* [Monitor Kafka with OTel Collector](/managed/ingest-from/opentelemetry/collector/use-cases/kafka/kafkametrics "How to configure the OpenTelemetry Collector to gather metrics from your Kafka server.")': '* [Мониторинг Kafka с помощью OTel Collector](/managed/ingest-from/opentelemetry/collector/use-cases/kafka/kafkametrics "Как настроить OpenTelemetry Collector для сбора метрик с вашего сервера Kafka.")',
    },
    "exporter.md": {
        "title: Forward OpenTelemetry data with the Kafka exporter": "title: Пересылка данных OpenTelemetry с помощью exporter Kafka",
        "# Forward OpenTelemetry data with the Kafka exporter": "# Пересылка данных OpenTelemetry с помощью exporter Kafka",
        "* How-to guide": "* Практическое руководство",
        "* 3-min read": "* Чтение: 3 мин",
        "* Published Nov 05, 2025": "* Опубликовано 05 ноября 2025 г.",
        "The following configuration example shows how you configure a Collector instance to export OTLP data to Kafka.": "В следующем примере конфигурации показано, как настроить экземпляр Collector для экспорта данных OTLP в Kafka.",
        "## Prerequisites": "## Предварительные требования",
        "* A deployed and configured Collector distribution, whether:": "* Развёрнутый и настроенный дистрибутив Collector, будь то:",
        **{
            k: C[k]
            for k in (
                '+ [Dynatrace Collector](/managed/ingest-from/opentelemetry/collector#dt-collector-dist "Learn how to use the OpenTelemetry Collector, including the Dynatrace OTel Collector, to ingest telemetry from OpenTelemetry.")',
                '+ [OpenTelemetry Contrib](/managed/ingest-from/opentelemetry/collector#collector-contrib "Learn how to use the OpenTelemetry Collector, including the Dynatrace OTel Collector, to ingest telemetry from OpenTelemetry.")',
            )
        },
        '+ [custom Builder version](/managed/ingest-from/opentelemetry/collector#collector-builder "Learn how to use the OpenTelemetry Collector, including the Dynatrace OTel Collector, to ingest telemetry from OpenTelemetry.")': '+ [пользовательская версия Builder](/managed/ingest-from/opentelemetry/collector#collector-builder "Узнайте, как использовать OpenTelemetry Collector, включая Dynatrace OTel Collector, для приёма телеметрии из OpenTelemetry.")',
        "* The [`kafkaexporter`](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/v0.151.0/exporter/kafkaexporter) component.": "* Компонент [`kafkaexporter`](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/v0.151.0/exporter/kafkaexporter).",
        **{
            k: C[k]
            for k in (
                "* A Kafka server deployed with a reachable `BROKER_ADDRESS`.",
                "For more information, see the [Kafka Apache quickstart guide](https://kafka.apache.org/quickstart).",
            )
        },
        "## Demo configuration": "## Демонстрационная конфигурация",
        "Here is an example YAML file for a basic Collector configuration that can be used to export OpenTelemetry traces, metrics, and logs to Kafka.": "Ниже приведён пример YAML-файла для базовой конфигурации Collector, который можно использовать для экспорта трассировок, метрик и логов OpenTelemetry в Kafka.",
        "For this configuration to work, you need to set the `BROKER_ADDRESS` environment variable.": "Чтобы эта конфигурация работала, необходимо задать переменную окружения `BROKER_ADDRESS`.",
        "The value is specific to your Kafka server.": "Значение зависит от вашего сервера Kafka.",
        **{
            k: C[k]
            for k in (
                "Configuration validation",
                '[Validate your settings](/managed/ingest-from/opentelemetry/collector/configuration#validate "How to configure the OpenTelemetry Collector.") to avoid any configuration issues.',
                "For our configuration, we configure certain components as described in the sections below.",
            )
        },
        "## Components": "## Компоненты",
        "Under `receivers`, we specify [`otlp`](https://github.com/open-telemetry/opentelemetry-collector/tree/v0.151.0/receiver/otlpreceiver) as the active receiver component for our deployment.": "В разделе `receivers` мы указываем [`otlp`](https://github.com/open-telemetry/opentelemetry-collector/tree/v0.151.0/receiver/otlpreceiver) в качестве активного компонента receiver для нашего развёртывания.",
        "This is required to accept OTLP data.": "Это необходимо для приёма данных OTLP.",
        "Under `processors`, we specify:": "В разделе `processors` мы указываем:",
        "* [`memory_limiter` processor](https://github.com/open-telemetry/opentelemetry-collector/tree/v0.151.0/processor/memorylimiterprocessor).": "* [processor `memory_limiter`](https://github.com/open-telemetry/opentelemetry-collector/tree/v0.151.0/processor/memorylimiterprocessor).",
        "* [`batch` processor](https://github.com/open-telemetry/opentelemetry-collector/tree/v0.151.0/processor/batchprocessor) as per [recommendation for the kafka exporter](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/v0.151.0/exporter/kafkaexporter#readme).": "* [processor `batch`](https://github.com/open-telemetry/opentelemetry-collector/tree/v0.151.0/processor/batchprocessor) согласно [рекомендации для exporter kafka](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/v0.151.0/exporter/kafkaexporter#readme).",
        "Under `exporters`, we specify the [`kafka` exporter](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/v0.151.0/exporter/kafkaexporter) to forward data to the Kafka server.": "В разделе `exporters` мы указываем [exporter `kafka`](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/v0.151.0/exporter/kafkaexporter) для пересылки данных на сервер Kafka.",
        "### Service pipeline": "### Сервисный конвейер",
        "Under `service`, we assemble our receiver, processors, and exporter objects into service pipelines, which will perform these steps:": "В разделе `service` мы собираем наши объекты receiver, processor и exporter в сервисные конвейеры, которые выполняют следующие шаги:",
        "1. Accept OTLP requests on the configured ports.": "1. Принимают запросы OTLP на настроенных портах.",
        "2. Use the `memory_limit` processor to make sure that the Collector doesn't run out of memory.": "2. Используют processor `memory_limit`, чтобы у Collector не закончилась память.",
        "3. Batch data using the `batch` processor.": "3. Группируют данные с помощью processor `batch`.",
        "4. Export data to Kafka server.": "4. Экспортируют данные на сервер Kafka.",
        "## Related topics": "## Связанные темы",
        **{
            k: C[k]
            for k in (
                '* [OTel Collector for ingesting telemetry into Dynatrace](/managed/ingest-from/opentelemetry/collector "Learn how to use the OpenTelemetry Collector, including the Dynatrace OTel Collector, to ingest telemetry from OpenTelemetry.")',
                '* [Buffer data via Kafka with OTel Collector](/managed/ingest-from/opentelemetry/collector/use-cases/kafka "How to configure the OpenTelemetry Collector to buffer data via Kafka.")',
                '* [Receive OpenTelemetry data with the Kafka receiver](/managed/ingest-from/opentelemetry/collector/use-cases/kafka/receiver "How to configure the OpenTelemetry Collector\'s Kafka receiver to ingest OpenTelemetry from Kafka.")',
                '* [Deploy the Dynatrace OTel Collector](/managed/ingest-from/opentelemetry/collector/deployment "How to deploy the Dynatrace OpenTelemetry Collector.")',
                '* [Configure the OTel Collector](/managed/ingest-from/opentelemetry/collector/configuration "How to configure the OpenTelemetry Collector.")',
            )
        },
    },
    "receiver.md": {
        "title: Receive OpenTelemetry data with the Kafka receiver": "title: Приём данных OpenTelemetry с помощью receiver Kafka",
        "# Receive OpenTelemetry data with the Kafka receiver": "# Приём данных OpenTelemetry с помощью receiver Kafka",
        "* How-to guide": "* Практическое руководство",
        "* 3-min read": "* Чтение: 3 мин",
        "* Published Nov 05, 2025": "* Опубликовано 05 ноября 2025 г.",
        "The following configuration example shows how you configure Kafka to read data from topics and relay this data via OTLP.": "В следующем примере конфигурации показано, как настроить Kafka для чтения данных из топиков и передачи этих данных через OTLP.",
        "## Prerequisites": "## Предварительные требования",
        "* A deployed and configured collector distribution, whether": "* Развёрнутый и настроенный дистрибутив Collector, будь то",
        **{
            k: C[k]
            for k in (
                '+ [Dynatrace Collector](/managed/ingest-from/opentelemetry/collector#dt-collector-dist "Learn how to use the OpenTelemetry Collector, including the Dynatrace OTel Collector, to ingest telemetry from OpenTelemetry.")',
                '+ [OpenTelemetry Contrib](/managed/ingest-from/opentelemetry/collector#collector-contrib "Learn how to use the OpenTelemetry Collector, including the Dynatrace OTel Collector, to ingest telemetry from OpenTelemetry.")',
            )
        },
        '+ [custom Builder version](/managed/ingest-from/opentelemetry/collector#collector-builder "Learn how to use the OpenTelemetry Collector, including the Dynatrace OTel Collector, to ingest telemetry from OpenTelemetry.")': '+ [пользовательская версия Builder](/managed/ingest-from/opentelemetry/collector#collector-builder "Узнайте, как использовать OpenTelemetry Collector, включая Dynatrace OTel Collector, для приёма телеметрии из OpenTelemetry.")',
        "* The [`kafkareceiver`](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/v0.151.0/receiver/kafkareceiver) component.": "* Компонент [`kafkareceiver`](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/v0.151.0/receiver/kafkareceiver).",
        **{
            k: C[k]
            for k in (
                "* A Kafka server deployed with a reachable `BROKER_ADDRESS`.",
                "For more information, see the [Kafka Apache quickstart guide](https://kafka.apache.org/quickstart).",
                '* The [Dynatrace API endpoint URL](/managed/ingest-from/opentelemetry/otlp-api "Learn about the OTLP API endpoints that your application uses to export OpenTelemetry data to Dynatrace.") to which the data should be exported.',
            )
        },
        '* An [API token](/managed/ingest-from/opentelemetry/otlp-api#authentication-export-to-activegate "Learn about the OTLP API endpoints that your application uses to export OpenTelemetry data to Dynatrace.") with the relevant access scope. (Only for exports to SaaS and ActiveGate.)': '* [API-токен](/managed/ingest-from/opentelemetry/otlp-api#authentication-export-to-activegate "Узнайте об эндпоинтах OTLP API, которые ваше приложение использует для экспорта данных OpenTelemetry в Dynatrace.") с соответствующей областью доступа. (Только для экспорта в SaaS и ActiveGate.)',
        "## Demo configuration": "## Демонстрационная конфигурация",
        "Here is an example YAML file for a basic Collector configuration that can be used to receive OpenTelemetry traces, metrics, and logs from Kafka.": "Ниже приведён пример YAML-файла для базовой конфигурации Collector, который можно использовать для приёма трассировок, метрик и логов OpenTelemetry из Kafka.",
        "For this configuration to work, you need to set the following environment variables.": "Чтобы эта конфигурация работала, необходимо задать следующие переменные окружения.",
        "* `BROKER_ADDRESS`: Specific to your Kafka server.": "* `BROKER_ADDRESS`: зависит от вашего сервера Kafka.",
        '* `DT_ENDPOINT`: The [base URL of the Dynatrace API endpoint](/managed/ingest-from/opentelemetry/otlp-api#export-to-activegate "Learn about the OTLP API endpoints that your application uses to export OpenTelemetry data to Dynatrace.") (for example, `https://{your-environment-id}.live.dynatrace.com/api/v2/otlp`).': '* `DT_ENDPOINT`: [базовый URL эндпоинта Dynatrace API](/managed/ingest-from/opentelemetry/otlp-api#export-to-activegate "Узнайте об эндпоинтах OTLP API, которые ваше приложение использует для экспорта данных OpenTelemetry в Dynatrace.") (например, `https://{your-environment-id}.live.dynatrace.com/api/v2/otlp`).',
        '* `DT_API_TOKEN`: The [API token](/managed/ingest-from/opentelemetry/otlp-api#authentication-export-to-activegate "Learn about the OTLP API endpoints that your application uses to export OpenTelemetry data to Dynatrace.").': '* `DT_API_TOKEN`: [API-токен](/managed/ingest-from/opentelemetry/otlp-api#authentication-export-to-activegate "Узнайте об эндпоинтах OTLP API, которые ваше приложение использует для экспорта данных OpenTelemetry в Dynatrace.").',
        **{
            k: C[k]
            for k in (
                "Configuration validation",
                '[Validate your settings](/managed/ingest-from/opentelemetry/collector/configuration#validate "How to configure the OpenTelemetry Collector.") to avoid any configuration issues.',
                "For our configuration, we configure certain components as described in the sections below.",
            )
        },
        "## Components": "## Компоненты",
        "Under `receivers`, we specify [`kafka`](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/v0.151.0/receiver/kafkareceiver) as the active receiver component for our deployment.": "В разделе `receivers` мы указываем [`kafka`](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/v0.151.0/receiver/kafkareceiver) в качестве активного компонента receiver для нашего развёртывания.",
        "This is required to receive data from Kafka server.": "Это необходимо для приёма данных с сервера Kafka.",
        "Under `exporters`, we specify the [`otlp_http` exporter](https://github.com/open-telemetry/opentelemetry-collector/tree/v0.151.0/exporter/otlphttpexporter) to forward data into Dynatrace.": "В разделе `exporters` мы указываем [exporter `otlp_http`](https://github.com/open-telemetry/opentelemetry-collector/tree/v0.151.0/exporter/otlphttpexporter) для пересылки данных в Dynatrace.",
        **{
            k: C[k]
            for k in (
                "For this purpose, we set the following two environment variables and reference them in the configuration values for `endpoint` and `Authorization`.",
                '* `DT_ENDPOINT` contains the [base URL of the Dynatrace API endpoint](/managed/ingest-from/opentelemetry/otlp-api#export-to-activegate "Learn about the OTLP API endpoints that your application uses to export OpenTelemetry data to Dynatrace.") (for example, `https://{your-environment-id}.live.dynatrace.com/api/v2/otlp`).',
                '* `DT_API_TOKEN` contains the [API token](/managed/ingest-from/opentelemetry/otlp-api#authentication-export-to-activegate "Learn about the OTLP API endpoints that your application uses to export OpenTelemetry data to Dynatrace.").',
            )
        },
        "### Service pipeline": "### Сервисный конвейер",
        "Under `service`, we assemble our receiver, and exporter objects into service pipelines, which will perform these steps:": "В разделе `service` мы собираем наши объекты receiver и exporter в сервисные конвейеры, которые выполняют следующие шаги:",
        "1. Receive data from Kafka server.": "1. Принимают данные с сервера Kafka.",
        "2. Export the data to Dynatrace.": "2. Экспортируют данные в Dynatrace.",
        "## Related topics": "## Связанные темы",
        **{
            k: C[k]
            for k in (
                '* [OTel Collector for ingesting telemetry into Dynatrace](/managed/ingest-from/opentelemetry/collector "Learn how to use the OpenTelemetry Collector, including the Dynatrace OTel Collector, to ingest telemetry from OpenTelemetry.")',
                '* [Buffer data via Kafka with OTel Collector](/managed/ingest-from/opentelemetry/collector/use-cases/kafka "How to configure the OpenTelemetry Collector to buffer data via Kafka.")',
                '* [Forward OpenTelemetry data with the Kafka exporter](/managed/ingest-from/opentelemetry/collector/use-cases/kafka/exporter "How to configure the OpenTelemetry Collector to forward OpenTelemetry data with the Kafka exporter.")',
                '* [Deploy the Dynatrace OTel Collector](/managed/ingest-from/opentelemetry/collector/deployment "How to deploy the Dynatrace OpenTelemetry Collector.")',
                '* [Configure the OTel Collector](/managed/ingest-from/opentelemetry/collector/configuration "How to configure the OpenTelemetry Collector.")',
            )
        },
    },
    "kafkametrics.md": {
        "title: Monitor Kafka with OTel Collector": "title: Мониторинг Kafka с помощью OTel Collector",
        "# Monitor Kafka with OTel Collector": "# Мониторинг Kafka с помощью OTel Collector",
        "* How-to guide": "* Практическое руководство",
        "* 3-min read": "* Чтение: 3 мин",
        "* Published Nov 26, 2025": "* Опубликовано 26 ноября 2025 г.",
        "The following configuration example shows how to configure an OTel Collector instance to scrape Kafka metrics via the `kafkametrics` receiver component and ingest them as OTLP requests into Dynatrace.": "В следующем примере конфигурации показано, как настроить экземпляр OTel Collector для сбора метрик Kafka с помощью компонента receiver `kafkametrics` и их приёма в виде запросов OTLP в Dynatrace.",
        "## Prerequisites": "## Предварительные требования",
        "To set up this configuration, ensure you have the following:": "Для настройки этой конфигурации убедитесь, что у вас есть следующее:",
        "* One of the following Collector distributions with the [kafkametrics receiver](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/v0.151.0/receiver/kafkametricsreceiver) and [cumulativetodelta processor](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/v0.151.0/processor/cumulativetodeltaprocessor)": "* Один из следующих дистрибутивов Collector с [receiver kafkametrics](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/v0.151.0/receiver/kafkametricsreceiver) и [processor cumulativetodelta](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/v0.151.0/processor/cumulativetodeltaprocessor)",
        **{
            k: C[k]
            for k in (
                '+ [Dynatrace Collector](/managed/ingest-from/opentelemetry/collector#dt-collector-dist "Learn how to use the OpenTelemetry Collector, including the Dynatrace OTel Collector, to ingest telemetry from OpenTelemetry.")',
                '+ [OpenTelemetry Contrib](/managed/ingest-from/opentelemetry/collector#collector-contrib "Learn how to use the OpenTelemetry Collector, including the Dynatrace OTel Collector, to ingest telemetry from OpenTelemetry.")',
            )
        },
        '+ [Custom Builder version](/managed/ingest-from/opentelemetry/collector#collector-builder "Learn how to use the OpenTelemetry Collector, including the Dynatrace OTel Collector, to ingest telemetry from OpenTelemetry.")': '+ [пользовательская версия Builder](/managed/ingest-from/opentelemetry/collector#collector-builder "Узнайте, как использовать OpenTelemetry Collector, включая Dynatrace OTel Collector, для приёма телеметрии из OpenTelemetry.")',
        **{
            k: C[k]
            for k in (
                "* A Kafka server deployed with a reachable `BROKER_ADDRESS`.",
                "For more information, see the [Kafka Apache quickstart guide](https://kafka.apache.org/quickstart).",
                '* The [Dynatrace API endpoint URL](/managed/ingest-from/opentelemetry/otlp-api "Learn about the OTLP API endpoints that your application uses to export OpenTelemetry data to Dynatrace.") to which the data should be exported.',
            )
        },
        '* An [API token](/managed/ingest-from/opentelemetry/otlp-api#authentication-export-to-activegate "Learn about the OTLP API endpoints that your application uses to export OpenTelemetry data to Dynatrace.") with the relevant access scope (only required for SaaS and ActiveGate).': '* [API-токен](/managed/ingest-from/opentelemetry/otlp-api#authentication-export-to-activegate "Узнайте об эндпоинтах OTLP API, которые ваше приложение использует для экспорта данных OpenTelemetry в Dynatrace.") с соответствующей областью доступа (требуется только для SaaS и ActiveGate).',
        'See [Collector Deployment](/managed/ingest-from/opentelemetry/collector/deployment "How to deploy the Dynatrace OpenTelemetry Collector.") and [Collector Configuration](/managed/ingest-from/opentelemetry/collector/configuration "How to configure the OpenTelemetry Collector.") on how to set up your Collector with the configuration below.': 'См. [Развёртывание Collector](/managed/ingest-from/opentelemetry/collector/deployment "Как развернуть Dynatrace OpenTelemetry Collector.") и [Настройку Collector](/managed/ingest-from/opentelemetry/collector/configuration "Как настроить OpenTelemetry Collector."), чтобы узнать, как настроить ваш Collector с приведённой ниже конфигурацией.',
        "## Demo configuration": "## Демонстрационная конфигурация",
        "## Components": "## Компоненты",
        "For our configuration, we configure the following components.": "Для нашей конфигурации мы настраиваем следующие компоненты.",
        "Under `receivers`, we specify the `kafkametrics` receiver.": "В разделе `receivers` мы указываем receiver `kafkametrics`.",
        "We configure it to scrape metrics from the Kafka broker specified in the `BROKER_ADDRESS` environment variable.": "Мы настраиваем его для сбора метрик с брокера Kafka, указанного в переменной окружения `BROKER_ADDRESS`.",
        "The receiver is set to collect metrics on brokers, topics, and consumers.": "Receiver настроен на сбор метрик по брокерам, топикам и потребителям.",
        "* [`memory_limiter` processor](https://github.com/open-telemetry/opentelemetry-collector/tree/v0.151.0/processor/memorylimiterprocessor).": "* [processor `memory_limiter`](https://github.com/open-telemetry/opentelemetry-collector/tree/v0.151.0/processor/memorylimiterprocessor).",
        'The `cumulativetodelta` processor is required to convert cumulative metrics (as reported by Kafka) into [delta aggregation format](/managed/ingest-from/opentelemetry/collector/configuration#delta-metrics "How to configure the OpenTelemetry Collector."), for compatibility with the Dynatrace metrics ingestion API.': 'Processor `cumulativetodelta` необходим для преобразования кумулятивных метрик (в том виде, в каком их сообщает Kafka) в [формат дельта-агрегации](/managed/ingest-from/opentelemetry/collector/configuration#delta-metrics "Как настроить OpenTelemetry Collector.") для совместимости с API приёма метрик Dynatrace.',
        "Under `exporters`, we specify the default [`otlp_http` exporter](https://github.com/open-telemetry/opentelemetry-collector/tree/v0.151.0/exporter/otlphttpexporter) and configure it with our Dynatrace API URL and the required authentication token.": "В разделе `exporters` мы указываем стандартный [exporter `otlp_http`](https://github.com/open-telemetry/opentelemetry-collector/tree/v0.151.0/exporter/otlphttpexporter) и настраиваем его с помощью URL нашего Dynatrace API и необходимого токена аутентификации.",
        **{
            k: C[k]
            for k in (
                "For this purpose, we set the following two environment variables and reference them in the configuration values for `endpoint` and `Authorization`.",
                '* `DT_ENDPOINT` contains the [base URL of the Dynatrace API endpoint](/managed/ingest-from/opentelemetry/otlp-api#export-to-activegate "Learn about the OTLP API endpoints that your application uses to export OpenTelemetry data to Dynatrace.") (for example, `https://{your-environment-id}.live.dynatrace.com/api/v2/otlp`).',
                '* `DT_API_TOKEN` contains the [API token](/managed/ingest-from/opentelemetry/otlp-api#authentication-export-to-activegate "Learn about the OTLP API endpoints that your application uses to export OpenTelemetry data to Dynatrace.").',
            )
        },
        "### Services": "### Службы",
        "Under `service`, we assemble our receiver, processor, and exporter components into a `metrics` pipeline. This pipeline:": "В разделе `service` мы собираем наши компоненты receiver, processor и exporter в конвейер `metrics`. Этот конвейер:",
        "1. Scrapes metrics from Kafka.": "1. Собирает метрики из Kafka.",
        "2. Converts cumulative metrics to delta metrics.": "2. Преобразует кумулятивные метрики в дельта-метрики.",
        "3. Exports the data to Dynatrace.": "3. Экспортирует данные в Dynatrace.",
        "## Limits and limitations": "## Пределы и ограничения",
        "### Avoid data duplication": "### Как избежать дублирования данных",
        "To avoid data duplication, make sure that only one OTel Collector scrapes a given target (for example, Kafka broker or Prometheus endpoint).": "Чтобы избежать дублирования данных, убедитесь, что данные с конкретной цели собирает только один OTel Collector (например, брокер Kafka или эндпоинт Prometheus).",
        "If you run multiple OTel Collector replicas, configure each one with a different target. This prevents duplicate metrics and unnecessary ingest costs.": "Если вы запускаете несколько реплик OTel Collector, настройте каждую из них на отдельную цель. Это предотвращает дублирование метрик и лишние затраты на приём данных.",
        "The [Target Allocator](https://opentelemetry.io/docs/platforms/kubernetes/operator/target-allocator/) automatically distributes the Prometheus targets among a pool of OTel Collectors.": "[Target Allocator](https://opentelemetry.io/docs/platforms/kubernetes/operator/target-allocator/) автоматически распределяет цели Prometheus внутри пула экземпляров OTel Collector.",
        "### Use of the `cumulativetodelta` processor": "### Использование processor `cumulativetodelta`",
        "Many OpenTelemetry receivers, including the `kafkametrics` receiver, report cumulative metrics by default. Dynatrace requires delta metrics for proper visualization and analysis.": "Многие компоненты receiver OpenTelemetry, включая receiver `kafkametrics`, по умолчанию сообщают кумулятивные метрики. Dynatrace требует дельта-метрики для корректной визуализации и анализа.",
        "To convert cumulative metrics to delta metrics, include the `cumulativetodelta` processor in your metrics pipeline.": "Чтобы преобразовать кумулятивные метрики в дельта-метрики, включите processor `cumulativetodelta` в ваш конвейер метрик.",
        "We recommend using this processor even if you expect some of the metrics to already have delta temporality, as those will be forwarded without any extra processing.": "Мы рекомендуем использовать этот processor, даже если вы ожидаете, что часть метрик уже имеет дельта-темпоральность, поскольку такие метрики будут пересылаться без дополнительной обработки.",
        "Statefulness": "Сохранение состояния",
        "The cumulativetodelta processor calculates delta by remembering the previous value of a metric. For this reason, the calculation is only accurate if the metric is continuously sent to the same instance of the OTel Collector.": "Processor cumulativetodelta вычисляет дельту, запоминая предыдущее значение метрики. По этой причине вычисление является точным только в том случае, если метрика непрерывно отправляется в один и тот же экземпляр OTel Collector.",
        "As a result, the cumulativetodelta processor may not work as expected if used in a deployment of multiple OTel Collectors. When using this processor, it's best for the data source to send data to a single OTel Collector.": "В результате processor cumulativetodelta может работать не так, как ожидается, если используется в развёртывании с несколькими экземплярами OTel Collector. При использовании этого processor лучше всего, чтобы источник данных отправлял данные в один экземпляр OTel Collector.",
        'If you need to scale your OTel Collectors while preserving processor state, use [stateful scaling](/managed/ingest-from/opentelemetry/collector/scaling#scaling-stateful-processing-using-non-pooled-collectors "How to scale the OpenTelemetry Collector.")': 'Если вам нужно масштабировать OTel Collector с сохранением состояния processor, используйте [масштабирование с сохранением состояния](/managed/ingest-from/opentelemetry/collector/scaling#scaling-stateful-processing-using-non-pooled-collectors "Как масштабировать OpenTelemetry Collector.")',
        "## Related topics": "## Связанные темы",
        **{
            k: C[k]
            for k in (
                '* [OTel Collector for ingesting telemetry into Dynatrace](/managed/ingest-from/opentelemetry/collector "Learn how to use the OpenTelemetry Collector, including the Dynatrace OTel Collector, to ingest telemetry from OpenTelemetry.")',
                '* [Deploy the Dynatrace OTel Collector](/managed/ingest-from/opentelemetry/collector/deployment "How to deploy the Dynatrace OpenTelemetry Collector.")',
                '* [Configure the OTel Collector](/managed/ingest-from/opentelemetry/collector/configuration "How to configure the OpenTelemetry Collector.")',
                '* [Receive OpenTelemetry data with the Kafka receiver](/managed/ingest-from/opentelemetry/collector/use-cases/kafka/receiver "How to configure the OpenTelemetry Collector\'s Kafka receiver to ingest OpenTelemetry from Kafka.")',
                '* [Forward OpenTelemetry data with the Kafka exporter](/managed/ingest-from/opentelemetry/collector/use-cases/kafka/exporter "How to configure the OpenTelemetry Collector to forward OpenTelemetry data with the Kafka exporter.")',
            )
        },
    },
}

# Lines copied verbatim (component-block headers kept EN; card title kept EN).
PASS = {
    "kafka.md": {
        "[### Exporter",
        "![Communication between OTel Collector and Kafka server](https://cdn.bfldr.com/B686QPH3/as/8zmzr8jx66vpjsjxqkhg8jw/OpenTelemetry_-_Configuring_Kafka_exporter_receiver_and_Metrics_receiver_components_-_Light_Mode?auto=webp&format=png&position=1)",
    },
    "exporter.md": {"### Receivers", "### Processors", "### Exporters"},
    "receiver.md": {"### Receivers", "### Exporters"},
    "kafkametrics.md": {"### Receivers", "### Processors", "### Exporters"},
}


def read_lf(p):
    with open(p, "r", encoding="utf-8", newline="") as f:
        return f.read().replace("\r\n", "\n").replace("\r", "\n")


def build(fname):
    sub = REL[fname]
    en_path = os.path.join(BASE, "managed", sub, fname)
    ru_path = os.path.join(BASE, "managed-ru", sub, fname)
    en_lines = read_lf(en_path).split("\n")
    tmap = {norm(k): v for k, v in TRANS[fname].items()}
    passset = {norm(k) for k in PASS.get(fname, set())}
    out = []
    in_fence = False
    for ln in en_lines:
        raw_stripped = ln.strip()
        stripped = norm(raw_stripped)
        if raw_stripped.startswith("```"):
            in_fence = not in_fence
            out.append(ln)
            continue
        if in_fence or stripped == "" or stripped == "---":
            out.append(ln)
            continue
        if raw_stripped.startswith("source:") or raw_stripped.startswith("scraped:"):
            out.append(ln)
            continue
        if stripped in tmap:
            indent = ln[: len(ln) - len(ln.lstrip())]
            out.append(indent + tmap[stripped])
            continue
        if stripped in passset:
            out.append(ln)
            continue
        raise SystemExit(f"[{fname}] UNTRANSLATED: {ln!r}")

    assert len(out) == len(en_lines), f"{fname}: parity {len(out)} != {len(en_lines)}"
    os.makedirs(os.path.dirname(ru_path), exist_ok=True)
    with open(ru_path, "w", encoding="utf-8", newline="\n") as f:
        f.write("\n".join(out))
    print(f"OK  {fname}: {len(out)} lines -> {ru_path}")


if __name__ == "__main__":
    for fn in TRANS:
        build(fn)
