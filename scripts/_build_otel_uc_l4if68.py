# -*- coding: utf-8 -*-
"""L4-IF.68 builder: opentelemetry/collector/use-cases hub + 8 recipe leaves.

Files (9): use-cases.md (hub) + jaeger, zipkin, fluentd, grpc, statsd, filelog,
netflow, multi-export. Same prose line-parity engine as _build_kafka_l4if67.py:
- line-parity (EN line count == RU line count),
- byte-identical code fences / blank lines / source: / scraped: / ---,
- URL identity (link/anchor targets copied verbatim inside translated lines),
- LF line endings, clean RU (no em-dash, no mojibake/BOM).

EN sources carry mojibake that norm() resolves before matching:
- BOM-class U+FEFF / `ï»¿` chars (stripped),
- `â\x80\x94` (mojibaked em-dash) -> real em-dash so TRANS keys stay readable.
RU output is built from the value side only, so it is always clean (no em-dash:
every term-definition `code`—text becomes `code`: text per style rule).

OTel Collector canon (reused from kafka L4-IF.67, extended for use-cases):
  receiver / exporter / processor -> EN (config-block kinds); component headers
  `### Receivers/Processors/Exporters` -> EN; `### Service pipeline(s)` ->
  `### Сервисный конвейер`/`### Сервисные конвейеры`; pipeline -> конвейер;
  traces -> трассировки; endpoint -> эндпоинт; span -> спан; broker -> брокер;
  topic -> топик; scrape -> сбор/собирать; bucket(histogram) -> интервал;
  OTel Collector / Collector / OTLP / OneAgent / product names -> EN; img-alt -> EN.
  Card product titles (FluentD/Jaeger/Zipkin/Prometheus/Kafka/Kubernetes/NetFlow/
  StatsD/Syslog/Journald) kept EN; descriptive titles translated.
"""

import os
import re

BOM_CLS = re.compile("[﻿ï»¿]")


def norm(s):
    s = s.replace("â", "—")  # mojibaked em-dash -> em-dash
    s = s.replace("â", "'")  # mojibaked apostrophe -> '
    return BOM_CLS.sub("", s)


BASE = os.path.join(os.path.dirname(__file__), "..", "docs")
PARENT = "ingest-from/opentelemetry/collector"
SUB = "ingest-from/opentelemetry/collector/use-cases"

REL = {"use-cases.md": PARENT}  # everything else lives in SUB

# Tooltip fragments reused verbatim across files (EN -> RU).
TT_LEARN = "Learn how to use the OpenTelemetry Collector, including the Dynatrace OTel Collector, to ingest telemetry from OpenTelemetry."
RU_LEARN = "Узнайте, как использовать OpenTelemetry Collector, включая Dynatrace OTel Collector, для приёма телеметрии из OpenTelemetry."
TT_OTLP = "Learn about the OTLP API endpoints that your application uses to export OpenTelemetry data to Dynatrace."
RU_OTLP = "Узнайте об эндпоинтах OTLP API, которые ваше приложение использует для экспорта данных OpenTelemetry в Dynatrace."
TT_LOGAPI = (
    "Learn how Dynatrace ingests OpenTelemetry log records and what limitations apply."
)
RU_LOGAPI = "Узнайте, как Dynatrace принимает записи логов OpenTelemetry и какие ограничения применяются."
TT_METAPI = (
    "Learn how Dynatrace ingests OpenTelemetry metrics and what limitations apply."
)
RU_METAPI = "Узнайте, как Dynatrace принимает метрики OpenTelemetry и какие ограничения применяются."
TT_ENRICHF = "Learn how to automatically enrich your telemetry data with Dynatrace-specific fields."
RU_ENRICHF = "Узнайте, как автоматически обогащать данные телеметрии полями, специфичными для Dynatrace."
TT_K8SENR = "Configure the OpenTelemetry Collector to enrich OTLP requests with Kubernetes data."
RU_K8SENR = (
    "Настройте OpenTelemetry Collector для обогащения запросов OTLP данными Kubernetes."
)

# ---------------------------------------------------------------------------
# Shared lines across leaves (extra unused keys are harmless when spread).
S = {
    # metadata / reading time
    "* How-to guide": "* Практическое руководство",
    "* 1-min read": "* Чтение: 1 мин",
    "* 2-min read": "* Чтение: 2 мин",
    "* 3-min read": "* Чтение: 3 мин",
    "* Published Oct 11, 2023": "* Опубликовано 11 октября 2023 г.",
    "* Published Jan 26, 2024": "* Опубликовано 26 января 2024 г.",
    "* Published Jul 09, 2024": "* Опубликовано 09 июля 2024 г.",
    "* Updated on Apr 09, 2026": "* Обновлено 09 апреля 2026 г.",
    "* Updated on Jan 27, 2026": "* Обновлено 27 января 2026 г.",
    "* Updated on Mar 12, 2026": "* Обновлено 12 марта 2026 г.",
    # section headings
    "## Prerequisites": "## Предварительные требования",
    "## Demo configuration": "## Демонстрационная конфигурация",
    "## Components": "## Компоненты",
    "## Limits and limitations": "## Пределы и ограничения",
    "## Related topics": "## Связанные темы",
    "### Service pipelines": "### Сервисные конвейеры",
    "### Service pipeline": "### Сервисный конвейер",
    "Configuration validation": "Проверка конфигурации",
    "For our configuration, we configure the following components.": "Для нашей конфигурации мы настраиваем следующие компоненты.",
    "For our configuration, we use the following components.": "Для нашей конфигурации мы используем следующие компоненты.",
    "* One of the following Collector distributions:": "* Один из следующих дистрибутивов Collector:",
    # distribution bullets (variants)
    '+ The [Dynatrace OTel Collector](/managed/ingest-from/opentelemetry/collector#dt-collector-dist "%s")'
    % TT_LEARN: '+ [Dynatrace OTel Collector](/managed/ingest-from/opentelemetry/collector#dt-collector-dist "%s")'
    % RU_LEARN,
    '+ [OpenTelemetry Contrib](/managed/ingest-from/opentelemetry/collector#collector-contrib "%s")'
    % TT_LEARN: '+ [OpenTelemetry Contrib](/managed/ingest-from/opentelemetry/collector#collector-contrib "%s")'
    % RU_LEARN,
    '+ OpenTelemetry [Contrib](/managed/ingest-from/opentelemetry/collector#collector-contrib "%s")'
    % TT_LEARN: '+ OpenTelemetry [Contrib](/managed/ingest-from/opentelemetry/collector#collector-contrib "%s")'
    % RU_LEARN,
    '+ OpenTelemetry [Core](/managed/ingest-from/opentelemetry/collector#collector-core "%s") or [Contrib](/managed/ingest-from/opentelemetry/collector#collector-contrib "%s")'
    % (
        TT_LEARN,
        TT_LEARN,
    ): '+ OpenTelemetry [Core](/managed/ingest-from/opentelemetry/collector#collector-core "%s") или [Contrib](/managed/ingest-from/opentelemetry/collector#collector-contrib "%s")'
    % (RU_LEARN, RU_LEARN),
    '+ A [custom Builder version](/managed/ingest-from/opentelemetry/collector#collector-builder "%s")'
    % TT_LEARN: '+ [пользовательская версия Builder](/managed/ingest-from/opentelemetry/collector#collector-builder "%s")'
    % RU_LEARN,
    # API endpoint / token prereqs
    '* The [Dynatrace API endpoint URL](/managed/ingest-from/opentelemetry/otlp-api "%s") to which the data should be exported'
    % TT_OTLP: '* [URL эндпоинта Dynatrace API](/managed/ingest-from/opentelemetry/otlp-api "%s"), на который должны экспортироваться данные'
    % RU_OTLP,
    '* An [API token](/managed/ingest-from/opentelemetry/otlp-api#authentication-export-to-activegate "%s") with the relevant access scope (only required for SaaS and ActiveGate)'
    % TT_OTLP: '* [API-токен](/managed/ingest-from/opentelemetry/otlp-api#authentication-export-to-activegate "%s") с соответствующей областью доступа (требуется только для SaaS и ActiveGate)'
    % RU_OTLP,
    'See [Collector Deployment](/managed/ingest-from/opentelemetry/collector/deployment "How to deploy the Dynatrace OpenTelemetry Collector.") and [Collector Configuration](/managed/ingest-from/opentelemetry/collector/configuration "How to configure the OpenTelemetry Collector.") on how to set up your Collector with the configuration below.': 'См. [Развёртывание Collector](/managed/ingest-from/opentelemetry/collector/deployment "Как развернуть Dynatrace OpenTelemetry Collector.") и [Настройку Collector](/managed/ingest-from/opentelemetry/collector/configuration "Как настроить OpenTelemetry Collector."), чтобы узнать, как настроить ваш Collector с приведённой ниже конфигурацией.',
    '[Validate your settings](/managed/ingest-from/opentelemetry/collector/configuration#validate "How to configure the OpenTelemetry Collector.") to avoid any configuration issues.': '[Проверьте ваши настройки](/managed/ingest-from/opentelemetry/collector/configuration#validate "Как настроить OpenTelemetry Collector."), чтобы избежать проблем с конфигурацией.',
    # exporter paragraph (otlp_http) shared by jaeger/zipkin/fluentd/grpc/statsd/filelog/netflow
    "Under `exporters`, we specify the default [`otlp_http` exporter](https://github.com/open-telemetry/opentelemetry-collector/tree/v0.151.0/exporter/otlphttpexporter) and configure it with our Dynatrace API URL and the required authentication token.": "В разделе `exporters` мы указываем стандартный [exporter `otlp_http`](https://github.com/open-telemetry/opentelemetry-collector/tree/v0.151.0/exporter/otlphttpexporter) и настраиваем его с помощью URL нашего Dynatrace API и необходимого токена аутентификации.",
    "For this purpose, we set the following two environment variables and reference them in the configuration values for `endpoint` and `Authorization`.": "Для этого мы задаём следующие две переменные окружения и ссылаемся на них в значениях конфигурации `endpoint` и `Authorization`.",
    '* `DT_ENDPOINT` contains the [base URL of the Dynatrace API endpoint](/managed/ingest-from/opentelemetry/otlp-api#export-to-activegate "%s") (for example, `https://{your-environment-id}.live.dynatrace.com/api/v2/otlp`)'
    % TT_OTLP: '* `DT_ENDPOINT` содержит [базовый URL эндпоинта Dynatrace API](/managed/ingest-from/opentelemetry/otlp-api#export-to-activegate "%s") (например, `https://{your-environment-id}.live.dynatrace.com/api/v2/otlp`)'
    % RU_OTLP,
    '* `DT_API_TOKEN` contains the [API token](/managed/ingest-from/opentelemetry/otlp-api#authentication-export-to-activegate "%s")'
    % TT_OTLP: '* `DT_API_TOKEN` содержит [API-токен](/managed/ingest-from/opentelemetry/otlp-api#authentication-export-to-activegate "%s")'
    % RU_OTLP,
    # limits boilerplate
    'Logs are ingested using the OpenTelemetry protocol (OTLP) via the [Dynatrace OTLP API](/managed/ingest-from/opentelemetry/otlp-api "%s") and are subject to the API\'s limits and restrictions.'
    % TT_OTLP: 'Логи принимаются с помощью протокола OpenTelemetry (OTLP) через [Dynatrace OTLP API](/managed/ingest-from/opentelemetry/otlp-api "%s") и подчиняются ограничениям и лимитам этого API.'
    % RU_OTLP,
    'Metrics are ingested using the OpenTelemetry protocol (OTLP) via the [Dynatrace OTLP API](/managed/ingest-from/opentelemetry/otlp-api "%s") and are subject to the API\'s limits and restrictions.'
    % TT_OTLP: 'Метрики принимаются с помощью протокола OpenTelemetry (OTLP) через [Dynatrace OTLP API](/managed/ingest-from/opentelemetry/otlp-api "%s") и подчиняются ограничениям и лимитам этого API.'
    % RU_OTLP,
    'Data is ingested using the OpenTelemetry protocol (OTLP) via the [Dynatrace OTLP APIs](/managed/ingest-from/opentelemetry/otlp-api "%s") and is subject to the API\'s limits and restrictions.'
    % TT_OTLP: 'Данные принимаются с помощью протокола OpenTelemetry (OTLP) через [Dynatrace OTLP API](/managed/ingest-from/opentelemetry/otlp-api "%s") и подчиняются ограничениям и лимитам этого API.'
    % RU_OTLP,
    'For more information, see [Ingest OpenTelemetry logs](/managed/ingest-from/opentelemetry/otlp-api/ingest-logs "%s").'
    % TT_LOGAPI: 'Дополнительные сведения см. в разделе [Приём логов OpenTelemetry](/managed/ingest-from/opentelemetry/otlp-api/ingest-logs "%s").'
    % RU_LOGAPI,
    "For more information see:": "Дополнительные сведения см.:",
    '* [OpenTelemetry metrics limitations](/managed/ingest-from/opentelemetry/otlp-api/ingest-otlp-metrics/about-metrics-ingest "%s")'
    % TT_METAPI: '* [Ограничения метрик OpenTelemetry](/managed/ingest-from/opentelemetry/otlp-api/ingest-otlp-metrics/about-metrics-ingest "%s")'
    % RU_METAPI,
    '* [Dynatrace metrics mapping](/managed/ingest-from/opentelemetry/otlp-api/ingest-otlp-metrics/about-metrics-ingest#dynatrace-mapping "%s")'
    % TT_METAPI: '* [Сопоставление метрик Dynatrace](/managed/ingest-from/opentelemetry/otlp-api/ingest-otlp-metrics/about-metrics-ingest#dynatrace-mapping "%s")'
    % RU_METAPI,
    '* [Ingest OpenTelemetry logs](/managed/ingest-from/opentelemetry/otlp-api/ingest-logs "%s")'
    % TT_LOGAPI: '* [Приём логов OpenTelemetry](/managed/ingest-from/opentelemetry/otlp-api/ingest-logs "%s")'
    % RU_LOGAPI,
    # related topics bullets
    '* [Enrich ingested data with Dynatrace-specific fields](/managed/ingest-from/extend-dynatrace/extend-data "%s")'
    % TT_ENRICHF: '* [Обогащение принимаемых данных полями, специфичными для Dynatrace](/managed/ingest-from/extend-dynatrace/extend-data "%s")'
    % RU_ENRICHF,
    '* [Enrich OTLP requests with Kubernetes data](/managed/ingest-from/opentelemetry/collector/use-cases/kubernetes/k8s-enrich "%s")'
    % TT_K8SENR: '* [Обогащение запросов OTLP данными Kubernetes](/managed/ingest-from/opentelemetry/collector/use-cases/kubernetes/k8s-enrich "%s")'
    % RU_K8SENR,
    '* [Ingest FluentD data with the OTel Collector](/managed/ingest-from/opentelemetry/collector/use-cases/fluentd "Configure the OpenTelemetry Collector to ingest FluentD data.")': '* [Приём данных FluentD с помощью OTel Collector](/managed/ingest-from/opentelemetry/collector/use-cases/fluentd "Настройте OpenTelemetry Collector для приёма данных FluentD.")',
    '* [Ingest syslog data with the OTel Collector](/managed/ingest-from/opentelemetry/collector/use-cases/syslog "Configure the OpenTelemetry Collector to ingest syslog data into Dynatrace.")': '* [Приём данных syslog с помощью OTel Collector](/managed/ingest-from/opentelemetry/collector/use-cases/syslog "Настройте OpenTelemetry Collector для приёма данных syslog в Dynatrace.")',
    '* [Ingest logs from files with the OTel Collector](/managed/ingest-from/opentelemetry/collector/use-cases/filelog "Configure the OpenTelemetry Collector to ingest log data into Dynatrace.")': '* [Приём логов из файлов с помощью OTel Collector](/managed/ingest-from/opentelemetry/collector/use-cases/filelog "Настройте OpenTelemetry Collector для приёма данных логов в Dynatrace.")',
    '* [Scrape Prometheus metrics with the OTel Collector](/managed/ingest-from/opentelemetry/collector/use-cases/prometheus "Configure the OpenTelemetry Collector to scrape your Prometheus data.")': '* [Сбор метрик Prometheus с помощью OTel Collector](/managed/ingest-from/opentelemetry/collector/use-cases/prometheus "Настройте OpenTelemetry Collector для сбора ваших данных Prometheus.")',
}

# ---------------------------------------------------------------------------
TRANS = {
    "jaeger.md": {
        "title: Ingest Jaeger data with the OTel Collector": "title: Приём данных Jaeger с помощью OTel Collector",
        "# Ingest Jaeger data with the OTel Collector": "# Приём данных Jaeger с помощью OTel Collector",
        "The following configuration example shows how you configure a Collector instance to accept Jaeger data, transform it to OTLP, and send it to the Dynatrace backend.": "В следующем примере конфигурации показано, как настроить экземпляр Collector для приёма данных Jaeger, их преобразования в OTLP и отправки в бэкенд Dynatrace.",
        "* One of the following Collector distributions with the [Jaeger receiver](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/v0.151.0/receiver/jaegerreceiver):": "* Один из следующих дистрибутивов Collector с [receiver Jaeger](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/v0.151.0/receiver/jaegerreceiver):",
        "Under `receivers`, we specify the `jaeger` receiver as active receiver component for our Collector instance.": "В разделе `receivers` мы указываем receiver `jaeger` в качестве активного компонента receiver для нашего экземпляра Collector.",
        "The Jaeger receiver can be customized with [a few more attributes](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/v0.151.0/receiver/jaegerreceiver), which we leave with their default values in our example.": "Receiver Jaeger можно настроить с помощью [нескольких дополнительных атрибутов](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/v0.151.0/receiver/jaegerreceiver), которые в нашем примере мы оставляем со значениями по умолчанию.",
        "Under `service`, we eventually assemble our receiver and exporter objects into a traces pipeline, which will handle our Jaeger transformation to OTLP.": "В разделе `service` мы в итоге собираем наши объекты receiver и exporter в конвейер трассировок, который выполнит преобразование наших данных Jaeger в OTLP.",
        **S,
    },
    "zipkin.md": {
        "title: Ingest Zipkin data with the OTel Collector": "title: Приём данных Zipkin с помощью OTel Collector",
        "# Ingest Zipkin data with the OTel Collector": "# Приём данных Zipkin с помощью OTel Collector",
        "The following configuration example shows how you configure a Collector instance to accept Zipkin data, transform it to OTLP, and send it to the Dynatrace backend.": "В следующем примере конфигурации показано, как настроить экземпляр Collector для приёма данных Zipkin, их преобразования в OTLP и отправки в бэкенд Dynatrace.",
        "## Limitations": "## Ограничения",
        "### B3 requirements": "### Требования B3",
        "Pay attention to the B3 requirements, to avoid having spans being dropped because of shared and duplicated span identifiers. See the [propagator specification](https://opentelemetry.io/docs/specs/otel/context/api-propagators/#b3-requirements) for more details.": "Обратите внимание на требования B3, чтобы избежать отбрасывания спанов из-за общих и дублирующихся идентификаторов спанов. Подробнее см. в [спецификации пропагатора](https://opentelemetry.io/docs/specs/otel/context/api-propagators/#b3-requirements).",
        "For example, if you are using [Spring Code Sleuth](https://cloud.spring.io/spring-cloud-sleuth/2.1.x/multi/multi__propagation.html#_extracting_a_propagated_context), you can use the following configuration setting to disable span sharing:": "Например, если вы используете [Spring Code Sleuth](https://cloud.spring.io/spring-cloud-sleuth/2.1.x/multi/multi__propagation.html#_extracting_a_propagated_context), для отключения совместного использования спанов можно задать следующий параметр конфигурации:",
        "### Single Collector routing": "### Маршрутизация через один Collector",
        "Make sure to route all related Zipkin/B3 spans via the same Collector instance, to guarantee full ingestion. If you ingest some spans using OneAgent alone, they may not be properly linked and not show up as connected to your Zipkin spans.": "Убедитесь, что все связанные спаны Zipkin/B3 маршрутизируются через один и тот же экземпляр Collector, чтобы гарантировать полный приём данных. Если часть спанов принимается только с помощью OneAgent, они могут быть связаны некорректно и не отображаться как соединённые с вашими спанами Zipkin.",
        "* One of the following Collector distributions with the [Zipkin receiver](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/v0.151.0/receiver/zipkinreceiver):": "* Один из следующих дистрибутивов Collector с [receiver Zipkin](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/v0.151.0/receiver/zipkinreceiver):",
        "Under `receivers`, we specify the `zipkin` receiver as active receiver component for our Collector instance.": "В разделе `receivers` мы указываем receiver `zipkin` в качестве активного компонента receiver для нашего экземпляра Collector.",
        "The Zipkin receiver can be customized with [a few more attributes](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/v0.151.0/receiver/zipkinreceiver), which we leave with their default values in our example.": "Receiver Zipkin можно настроить с помощью [нескольких дополнительных атрибутов](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/v0.151.0/receiver/zipkinreceiver), которые в нашем примере мы оставляем со значениями по умолчанию.",
        "Under `service`, we eventually assemble our receiver and exporter objects into a traces pipeline, which will handle our Zipkin transformation to OTLP.": "В разделе `service` мы в итоге собираем наши объекты receiver и exporter в конвейер трассировок, который выполнит преобразование наших данных Zipkin в OTLP.",
        **S,
    },
    "fluentd.md": {
        "title: Ingest FluentD data with the OTel Collector": "title: Приём данных FluentD с помощью OTel Collector",
        "# Ingest FluentD data with the OTel Collector": "# Приём данных FluentD с помощью OTel Collector",
        "The following configuration example shows how to configure a Collector instance to accept FluentD events via the [Fluent Forward protocol](https://github.com/fluent/fluentd/wiki/Forward-Protocol-Specification-v1) and ingest them as OTLP requests into Dynatrace.": "В следующем примере конфигурации показано, как настроить экземпляр Collector для приёма событий FluentD по [протоколу Fluent Forward](https://github.com/fluent/fluentd/wiki/Forward-Protocol-Specification-v1) и их передачи в виде запросов OTLP в Dynatrace.",
        "* One of the following Collector distributions with the [Fluent Forward receiver](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/v0.151.0/receiver/fluentforwardreceiver):": "* Один из следующих дистрибутивов Collector с [receiver Fluent Forward](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/v0.151.0/receiver/fluentforwardreceiver):",
        "Under `receivers`, we specify the `fluentforward` receiver as the active receiver component for our Collector instance and configure it to listen on specified ports.": "В разделе `receivers` мы указываем receiver `fluentforward` в качестве активного компонента receiver для нашего экземпляра Collector и настраиваем его на прослушивание указанных портов.",
        "Under `service`, we assemble our receiver and exporter objects into a logs pipeline, which will listen on the configured address for FluentD logs and ingest the data into Dynatrace.": "В разделе `service` мы собираем наши объекты receiver и exporter в конвейер логов, который прослушивает настроенный адрес на наличие логов FluentD и принимает эти данные в Dynatrace.",
        **S,
    },
    "grpc.md": {
        "title: Transform OTLP gRPC to HTTP with the OTel Collector": "title: Преобразование OTLP gRPC в HTTP с помощью OTel Collector",
        "# Transform OTLP gRPC to HTTP with the OTel Collector": "# Преобразование OTLP gRPC в HTTP с помощью OTel Collector",
        "The following configuration example shows how you would configure a Collector instance to transform a gRPC OTLP request to its HTTP counterpart.": "В следующем примере конфигурации показано, как настроить экземпляр Collector для преобразования запроса gRPC OTLP в его аналог по HTTP.",
        "Under `receivers`, we specify the gRPC [`otlp` receiver](https://github.com/open-telemetry/opentelemetry-collector/tree/v0.151.0/receiver/otlpreceiver) as active receiver component for our Collector instance.": "В разделе `receivers` мы указываем [receiver `otlp`](https://github.com/open-telemetry/opentelemetry-collector/tree/v0.151.0/receiver/otlpreceiver) для gRPC в качестве активного компонента receiver для нашего экземпляра Collector.",
        "Under `service`, we eventually assemble our receiver and exporter objects into pipelines, which explicitly accept gRPC requests and forward them on HTTP to Dynatrace.": "В разделе `service` мы в итоге собираем наши объекты receiver и exporter в конвейеры, которые явно принимают запросы gRPC и пересылают их по HTTP в Dynatrace.",
        **S,
    },
    "statsd.md": {
        "title: Ingest StatsD data with the OTel Collector": "title: Приём данных StatsD с помощью OTel Collector",
        "# Ingest StatsD data with the OTel Collector": "# Приём данных StatsD с помощью OTel Collector",
        "The following configuration example shows how you configure a Collector instance to ingest data from an existing StatsD setup and import it as an OTLP request into Dynatrace.": "В следующем примере конфигурации показано, как настроить экземпляр Collector для приёма данных из существующей установки StatsD и их импорта в виде запроса OTLP в Dynatrace.",
        "* An application generating [StatsD messages](https://github.com/statsd/statsd/blob/master/docs/metric_types.md)": "* Приложение, генерирующее [сообщения StatsD](https://github.com/statsd/statsd/blob/master/docs/metric_types.md)",
        "* One of the following Collector distributions with the [StatsD receiver](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/v0.151.0/receiver/statsdreceiver), [transform processor](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/v0.151.0/processor/transformprocessor), and [filter processor](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/v0.151.0/processor/filterprocessor):": "* Один из следующих дистрибутивов Collector с [receiver StatsD](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/v0.151.0/receiver/statsdreceiver), [processor transform](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/v0.151.0/processor/transformprocessor) и [processor filter](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/v0.151.0/processor/filterprocessor):",
        "Under `receivers`, we specify the `statsd` receiver as active receiver component for our Collector instance. We configure the receiver to listen on all network interfaces to port `8125`, which is the port typically used for StatsD.": "В разделе `receivers` мы указываем receiver `statsd` в качестве активного компонента receiver для нашего экземпляра Collector. Мы настраиваем receiver на прослушивание всех сетевых интерфейсов на порту `8125`, который обычно используется для StatsD.",
        "The receiver is configured to aggregate histogram, timer, and distribution messages into exponential histograms, which are later processed for Dynatrace ingestion. The receiver uses auto-scaling exponential histograms, and we have selected a maximum size of `100`. This means that the histogram will begin with very granular bucket boundaries and automatically re-scale itself if it receives data points that would result in more than `100` buckets.": "Receiver настроен на агрегирование сообщений histogram, timer и distribution в экспоненциальные гистограммы, которые затем обрабатываются для приёма в Dynatrace. Receiver использует экспоненциальные гистограммы с автомасштабированием, и мы выбрали максимальный размер `100`. Это означает, что гистограмма начинается с очень детальных границ интервалов и автоматически перемасштабируется, если получает точки данных, которые привели бы к более чем `100` интервалам.",
        "For a full list of configuration parameters and supported StatsD metric types, see the [StatsD receiver documentation](https://github.com/open-telemetry/opentelemetry-collector-contrib/blob/v0.151.0/receiver/statsdreceiver/README.md).": "Полный список параметров конфигурации и поддерживаемых типов метрик StatsD см. в [документации по receiver StatsD](https://github.com/open-telemetry/opentelemetry-collector-contrib/blob/v0.151.0/receiver/statsdreceiver/README.md).",
        "For this purpose, we set the following two environment variables and reference them in the configuration values for `endpoint` and `headers`.": "Для этого мы задаём следующие две переменные окружения и ссылаемся на них в значениях конфигурации `endpoint` и `headers`.",
        "Under `service`, we assemble our receiver, processors, and exporter objects into a metrics pipeline, which accepts StatsD data and ingests it into Dynatrace.": "В разделе `service` мы собираем наши объекты receiver, processor и exporter в конвейер метрик, который принимает данные StatsD и передаёт их в Dynatrace.",
        **S,
    },
    "filelog.md": {
        "title: Ingest logs from files with the OTel Collector": "title: Приём логов из файлов с помощью OTel Collector",
        "# Ingest logs from files with the OTel Collector": "# Приём логов из файлов с помощью OTel Collector",
        "The following configuration example shows how to configure a Collector instance to monitor log files and send their log entries to the Dynatrace backend.": "В следующем примере конфигурации показано, как настроить экземпляр Collector для мониторинга файлов логов и отправки их записей логов в бэкенд Dynatrace.",
        "* One of the following Collector distributions with the [Filelog receiver](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/v0.151.0/receiver/filelogreceiver):": "* Один из следующих дистрибутивов Collector с [receiver Filelog](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/v0.151.0/receiver/filelogreceiver):",
        "## Sample log file": "## Пример файла логов",
        "For the demo configuration above, we parse the file `file.log` with the following format:": "Для приведённой выше демонстрационной конфигурации мы разбираем файл `file.log` следующего формата:",
        "Each line starts with an ISO 8601 timestamp, followed by the entry's severity level, and finishes with the log message.": "Каждая строка начинается с метки времени в формате ISO 8601, за которой следует уровень серьёзности записи, и заканчивается сообщением лога.",
        "We parse each line into its individual parts with the following regular expression:": "Мы разбираем каждую строку на отдельные части с помощью следующего регулярного выражения:",
        "Apart from the two start (`^`) and end (`$`) of line assertions, we have the following named capture groups:": "Помимо двух утверждений начала (`^`) и конца (`$`) строки, у нас есть следующие именованные группы захвата:",
        "* `(?P<time>\\d{4}-\\d{2}-\\d{2})`—Names its capture group `time` and matches a typical ISO 8601 timestamp.": "* `(?P<time>\\d{4}-\\d{2}-\\d{2})`: называет свою группу захвата `time` и сопоставляется с типичной меткой времени ISO 8601.",
        "* `(?P<sev>[A-Z]*)`—Names its capture group `sev` and matches an arbitrary number of Latin uppercase characters.": "* `(?P<sev>[A-Z]*)`: называет свою группу захвата `sev` и сопоставляется с произвольным числом латинских символов в верхнем регистре.",
        "* `(?P<msg>.*)`—Names its capture group `msg` and matches an arbitrary number of characters.": "* `(?P<msg>.*)`: называет свою группу захвата `msg` и сопоставляется с произвольным числом символов.",
        "Under `receivers`, we specify the `filelog` receiver as active receiver component for our Collector instance.": "В разделе `receivers` мы указываем receiver `filelog` в качестве активного компонента receiver для нашего экземпляра Collector.",
        "The Filelog receiver supports a number of [configuration parameters](https://github.com/open-telemetry/opentelemetry-collector-contrib/blob/v0.151.0/receiver/filelogreceiver/README.md), which enable you to customize its behavior. For our example, we use the following:": "Receiver Filelog поддерживает ряд [параметров конфигурации](https://github.com/open-telemetry/opentelemetry-collector-contrib/blob/v0.151.0/receiver/filelogreceiver/README.md), позволяющих настроить его поведение. В нашем примере мы используем следующие:",
        "* `include`—Specifies the path pattern of the files we want to ingest.": "* `include`: задаёт шаблон пути к файлам, которые мы хотим принимать.",
        "* `start_at`—Specifies if the receiver should read from the beginning of the file or, for the most recent entries only, the end.": "* `start_at`: задаёт, должен ли receiver читать с начала файла или, только для самых последних записей, с конца.",
        "* `operators`—Configures the operators we apply to each log entry. For our example, we use the [regex\\_parser](https://github.com/open-telemetry/opentelemetry-collector-contrib/blob/v0.151.0/pkg/stanza/docs/operators/regex_parser.md) operator to extract information using a regular expression.": "* `operators`: настраивает операторы, применяемые к каждой записи лога. В нашем примере мы используем оператор [regex\\_parser](https://github.com/open-telemetry/opentelemetry-collector-contrib/blob/v0.151.0/pkg/stanza/docs/operators/regex_parser.md) для извлечения информации с помощью регулярного выражения.",
        "+ `regex`—Specifies the actual regular expression. By using named capture groups (`(?P<name>)`), the receiver makes the captured data available in `attributes` under the respective name.": "+ `regex`: задаёт само регулярное выражение. Используя именованные группы захвата (`(?P<name>)`), receiver делает захваченные данные доступными в `attributes` под соответствующим именем.",
        "+ `timestamp`—Specifies where to take the entry's timestamp from (the `time` field of the regular expression) and the date format.": "+ `timestamp`: задаёт, откуда брать метку времени записи (поле `time` регулярного выражения) и формат даты.",
        "+ `severity`—Specifies where to take the entry's severity level from (the `sev` field of the regular expression).": "+ `severity`: задаёт, откуда брать уровень серьёзности записи (поле `sev` регулярного выражения).",
        "Under `service`, we eventually assemble our receiver and exporter objects into a traces pipeline, which will continuously monitor the configured files and ingest their entries into Dynatrace using OTLP.": "В разделе `service` мы в итоге собираем наши объекты receiver и exporter в конвейер трассировок, который непрерывно отслеживает настроенные файлы и принимает их записи в Dynatrace с помощью OTLP.",
        **S,
    },
    "netflow.md": {
        "title: Ingest NetFlow with the OTel Collector": "title: Приём NetFlow с помощью OTel Collector",
        "# Ingest NetFlow with the OTel Collector": "# Приём NetFlow с помощью OTel Collector",
        "The following configuration example shows how to configure a Collector instance to accept NetFlow packets and ingest them as OTLP requests into Dynatrace.": "В следующем примере конфигурации показано, как настроить экземпляр Collector для приёма пакетов NetFlow и их передачи в виде запросов OTLP в Dynatrace.",
        "* One of the following Collector distributions with the [NetFlow receiver](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/v0.151.0/receiver/netflowreceiver):": "* Один из следующих дистрибутивов Collector с [receiver NetFlow](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/v0.151.0/receiver/netflowreceiver):",
        '+ [The Dynatrace Collector](/managed/ingest-from/opentelemetry/collector#dt-collector-dist "%s")'
        % TT_LEARN: '+ [Dynatrace Collector](/managed/ingest-from/opentelemetry/collector#dt-collector-dist "%s")'
        % RU_LEARN,
        '+ [A custom Builder version](/managed/ingest-from/opentelemetry/collector#collector-builder "%s")'
        % TT_LEARN: '+ [пользовательская версия Builder](/managed/ingest-from/opentelemetry/collector#collector-builder "%s")'
        % RU_LEARN,
        '* The [Dynatrace API endpoint URL](/managed/ingest-from/opentelemetry/otlp-api "%s") to which the data should be exported.'
        % TT_OTLP: '* [URL эндпоинта Dynatrace API](/managed/ingest-from/opentelemetry/otlp-api "%s"), на который должны экспортироваться данные.'
        % RU_OTLP,
        '* An [API token](/managed/ingest-from/opentelemetry/otlp-api#authentication-export-to-activegate "%s") with the Ingest logs (`logs.ingest`) scope.'
        % TT_OTLP: '* [API-токен](/managed/ingest-from/opentelemetry/otlp-api#authentication-export-to-activegate "%s") с областью доступа Ingest logs (`logs.ingest`).'
        % RU_OTLP,
        "* A NetFlow- or sFlow-capable device that can send NetFlow packets to the OTel Collector instance.": "* Устройство с поддержкой NetFlow или sFlow, способное отправлять пакеты NetFlow в экземпляр OTel Collector.",
        "## Collector configuration": "## Конфигурация Collector",
        "Check the [NetFlow receiver](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/v0.151.0/receiver/netflowreceiver#netflow-receiver) documentation for the available configuration options.": "Доступные параметры конфигурации см. в документации по [receiver NetFlow](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/v0.151.0/receiver/netflowreceiver#netflow-receiver).",
        "We recommend setting the `sockets` parameter to match the number of CPU cores available on the Collector instance, and the `workers` parameter to twice the number of sockets. This configuration allows the Collector to process multiple incoming NetFlow packets concurrently, which improves performance.": "Мы рекомендуем задавать параметру `sockets` значение, равное числу доступных на экземпляре Collector ядер CPU, а параметру `workers` задавать удвоенное число сокетов. Такая конфигурация позволяет Collector обрабатывать несколько входящих пакетов NetFlow одновременно, что повышает производительность.",
        "For extremely large volumes of data, you should parallelize the configuration among multiple Collector instances.": "Для очень больших объёмов данных следует распараллелить конфигурацию между несколькими экземплярами Collector.",
        "Under `receivers`, we specify the `netflow` receiver as the active receiver component for our Collector instance and configure it to listen on specified ports.": "В разделе `receivers` мы указываем receiver `netflow` в качестве активного компонента receiver для нашего экземпляра Collector и настраиваем его на прослушивание указанных портов.",
        "Under `processors`, we specify the `batch` processor, which batches the incoming NetFlow packets before sending them to Dynatrace. This is useful for optimizing performance and reducing the number of requests sent.": "В разделе `processors` мы указываем processor `batch`, который группирует входящие пакеты NetFlow перед их отправкой в Dynatrace. Это полезно для оптимизации производительности и сокращения числа отправляемых запросов.",
        "Under `service`, we assemble our receiver and exporter objects into a logs pipeline, which will listen on the configured address for incoming NetFlow packets and forward them to Dynatrace using the exporter.": "В разделе `service` мы собираем наши объекты receiver и exporter в конвейер логов, который прослушивает настроенный адрес на наличие входящих пакетов NetFlow и пересылает их в Dynatrace с помощью exporter.",
        **S,
    },
    "multi-export.md": {
        "title: Send OpenTelemetry data to multiple backends": "title: Отправка данных OpenTelemetry в несколько бэкендов",
        "# Send OpenTelemetry data to multiple backends": "# Отправка данных OpenTelemetry в несколько бэкендов",
        "The following configuration example shows how to configure a Collector instance to send telemetry data to multiple backends at the same time.": "В следующем примере конфигурации показано, как настроить экземпляр Collector для одновременной отправки данных телеметрии в несколько бэкендов.",
        "* For Dynatrace:": "* Для Dynatrace:",
        '+ The [Dynatrace API endpoint URL](/managed/ingest-from/opentelemetry/otlp-api "%s") to which the data should be exported'
        % TT_OTLP: '+ [URL эндпоинта Dynatrace API](/managed/ingest-from/opentelemetry/otlp-api "%s"), на который должны экспортироваться данные'
        % RU_OTLP,
        '+ An [API token](/managed/ingest-from/opentelemetry/otlp-api#authentication-export-to-activegate "%s") with the relevant access scope (only required for SaaS and ActiveGate)'
        % TT_OTLP: '+ [API-токен](/managed/ingest-from/opentelemetry/otlp-api#authentication-export-to-activegate "%s") с соответствующей областью доступа (требуется только для SaaS и ActiveGate)'
        % RU_OTLP,
        "* The ingest URLs and any applicable authentication credentials for the other backends": "* URL для приёма и все применимые учётные данные аутентификации для других бэкендов",
        "Under `receivers`, we specify the [`otlp` receiver](https://github.com/open-telemetry/opentelemetry-collector/tree/v0.151.0/receiver/otlpreceiver) as the active receiver component for our Collector instance.": "В разделе `receivers` мы указываем [receiver `otlp`](https://github.com/open-telemetry/opentelemetry-collector/tree/v0.151.0/receiver/otlpreceiver) в качестве активного компонента receiver для нашего экземпляра Collector.",
        "Under `exporters`, we specify the following exporter instances for our backends.": "В разделе `exporters` мы указываем следующие экземпляры exporter для наших бэкендов.",
        "* An [`otlp_http` exporter](https://github.com/open-telemetry/opentelemetry-collector/tree/v0.151.0/exporter/otlphttpexporter) for Dynatrace": "* [exporter `otlp_http`](https://github.com/open-telemetry/opentelemetry-collector/tree/v0.151.0/exporter/otlphttpexporter) для Dynatrace",
        "* A gRPC [`otlp` exporter](https://github.com/open-telemetry/opentelemetry-collector/tree/v0.151.0/exporter/otlpexporter) for the cold storage system": "* [exporter `otlp`](https://github.com/open-telemetry/opentelemetry-collector/tree/v0.151.0/exporter/otlpexporter) gRPC для системы холодного хранения",
        "For the Dynatrace exporter, we set the following two environment variables and reference them in the configuration values for `endpoint` and `Authorization`.": "Для exporter Dynatrace мы задаём следующие две переменные окружения и ссылаемся на них в значениях конфигурации `endpoint` и `Authorization`.",
        "Under `service`, we eventually assemble our receiver and exporter objects into pipelines, which accept any OTLP request (HTTP and gRPC) and forward it to the configured backends, using the configured exporters.": "В разделе `service` мы в итоге собираем наши объекты receiver и exporter в конвейеры, которые принимают любой запрос OTLP (HTTP и gRPC) и пересылают его в настроенные бэкенды с помощью настроенных exporter.",
        **S,
    },
    "use-cases.md": {
        "title: OTel Collector use cases": "title: Сценарии использования OTel Collector",
        "# OTel Collector use cases": "# Сценарии использования OTel Collector",
        "* How-to guide": "* Практическое руководство",
        "* 2-min read": "* Чтение: 2 мин",
        "* Updated on Mar 12, 2026": "* Обновлено 12 марта 2026 г.",
        "## Recommended configurations": "## Рекомендуемые конфигурации",
        "When using the OTel Collector, we recommend using the following features in the basic configuration, in addition to components specific to your use case.": "При использовании OTel Collector мы рекомендуем применять в базовой конфигурации следующие функции в дополнение к компонентам, специфичным для вашего сценария использования.",
        '* [Batching](/managed/ingest-from/opentelemetry/collector/use-cases/batch "Configure the OpenTelemetry Collector to send data in batches to the Dynatrace backend.")—to improve network performance and throughput': '* [Группирование](/managed/ingest-from/opentelemetry/collector/use-cases/batch "Настройте OpenTelemetry Collector для отправки данных группами в бэкенд Dynatrace.") для повышения производительности и пропускной способности сети',
        '* [Memory Limitation](/managed/ingest-from/opentelemetry/collector/use-cases/memory "Configure the OpenTelemetry Collector to respect memory limits and not use excessive system resources.")—to avoid memory allocation related issues': '* [Ограничение памяти](/managed/ingest-from/opentelemetry/collector/use-cases/memory "Настройте OpenTelemetry Collector для соблюдения ограничений памяти и предотвращения чрезмерного использования системных ресурсов.") во избежание проблем, связанных с выделением памяти',
        '* [Kubernetes Enrichment](/managed/ingest-from/opentelemetry/collector/use-cases/kubernetes/k8s-enrich "Configure the OpenTelemetry Collector to enrich OTLP requests with Kubernetes data.")—to include Kubernetes-specific information in your requests and support data correlation in the Dynatrace backend': '* [Обогащение данными Kubernetes](/managed/ingest-from/opentelemetry/collector/use-cases/kubernetes/k8s-enrich "Настройте OpenTelemetry Collector для обогащения запросов OTLP данными Kubernetes.") для включения специфичной для Kubernetes информации в ваши запросы и поддержки корреляции данных в бэкенде Dynatrace',
        "## Use cases": "## Сценарии использования",
        "[### Batching": "[### Группирование",
        'Configure the Collector to send data in batches to the Dynatrace backend.](/managed/ingest-from/opentelemetry/collector/use-cases/batch "Configure the OpenTelemetry Collector to send data in batches to the Dynatrace backend.")[### Enrich with OneAgent': 'Настройте Collector для отправки данных группами в бэкенд Dynatrace.](/managed/ingest-from/opentelemetry/collector/use-cases/batch "Настройте OpenTelemetry Collector для отправки данных группами в бэкенд Dynatrace.")[### Обогащение с помощью OneAgent',
        'Configure the Collector to enrich data with OneAgent.](/managed/ingest-from/opentelemetry/collector/use-cases/enrich "Configure the OpenTelemetry Collector to enrich OTLP requests with OneAgent host data.")[![FluentD](https://dt-cdn.net/images/untitled-300-c72685245e.png "FluentD")': 'Настройте Collector для обогащения данных с помощью OneAgent.](/managed/ingest-from/opentelemetry/collector/use-cases/enrich "Настройте OpenTelemetry Collector для обогащения запросов OTLP данными хоста OneAgent.")[![FluentD](https://dt-cdn.net/images/untitled-300-c72685245e.png "FluentD")',
        'Configure the Collector to ingest data from FluentD.](/managed/ingest-from/opentelemetry/collector/use-cases/fluentd "Configure the OpenTelemetry Collector to ingest FluentD data.")[### gRPC to HTTP': 'Настройте Collector для приёма данных из FluentD.](/managed/ingest-from/opentelemetry/collector/use-cases/fluentd "Настройте OpenTelemetry Collector для приёма данных FluentD.")[### gRPC в HTTP',
        'Configure the Collector to transform a gRPC OTLP request to HTTP.](/managed/ingest-from/opentelemetry/collector/use-cases/grpc "Configure the OpenTelemetry Collector to transform a gRPC OTLP request to HTTP.")[### Histogram summaries': 'Настройте Collector для преобразования запроса gRPC OTLP в HTTP.](/managed/ingest-from/opentelemetry/collector/use-cases/grpc "Настройте OpenTelemetry Collector для преобразования запроса gRPC OTLP в HTTP.")[### Сводки гистограмм',
        'Configure the Collector to compute bucket summaries for histogram metrics.](/managed/ingest-from/opentelemetry/collector/use-cases/histograms "Configure the OpenTelemetry Collector to compute histogram summaries.")[![Infrastructure observability](https://cdn.bfldr.com/B686QPH3/at/5kh38tq37h2w4qtnmbp5m889/DT0434.svg?auto=webp&width=72&height=72 "Infrastructure observability")': 'Настройте Collector для вычисления сводок по интервалам для метрик-гистограмм.](/managed/ingest-from/opentelemetry/collector/use-cases/histograms "Настройте OpenTelemetry Collector для вычисления сводок гистограмм.")[![Infrastructure observability](https://cdn.bfldr.com/B686QPH3/at/5kh38tq37h2w4qtnmbp5m889/DT0434.svg?auto=webp&width=72&height=72 "Infrastructure observability")',
        "### Host monitoring": "### Мониторинг хостов",
        'Monitor your hosts that send OpenTelemetry data to Dynatrace.](/managed/ingest-from/opentelemetry/collector/use-cases/host-monitoring "How to monitor your hosts that use Collectors to send OpenTelemetry data to Dynatrace.")[![Jaeger](https://dt-cdn.net/images/jaeger-300-3d21c8cbd4-300-2d7104a994.png "Jaeger")': 'Отслеживайте ваши хосты, которые отправляют данные OpenTelemetry в Dynatrace.](/managed/ingest-from/opentelemetry/collector/use-cases/host-monitoring "Как отслеживать ваши хосты, которые используют Collector для отправки данных OpenTelemetry в Dynatrace.")[![Jaeger](https://dt-cdn.net/images/jaeger-300-3d21c8cbd4-300-2d7104a994.png "Jaeger")',
        'Configure the Collector to ingest and transform Jaeger data into Dynatrace.](/managed/ingest-from/opentelemetry/collector/use-cases/jaeger "Configure the OpenTelemetry Collector to ingest and convert Jaeger data into Dynatrace.")[![Infrastructure observability](https://cdn.bfldr.com/B686QPH3/at/5kh38tq37h2w4qtnmbp5m889/DT0434.svg?auto=webp&width=72&height=72 "Infrastructure observability")': 'Настройте Collector для приёма и преобразования данных Jaeger в Dynatrace.](/managed/ingest-from/opentelemetry/collector/use-cases/jaeger "Настройте OpenTelemetry Collector для приёма и преобразования данных Jaeger в Dynatrace.")[![Infrastructure observability](https://cdn.bfldr.com/B686QPH3/at/5kh38tq37h2w4qtnmbp5m889/DT0434.svg?auto=webp&width=72&height=72 "Infrastructure observability")',
        'Configure the Collector to ingest systemd journal logs into Dynatrace.](/managed/ingest-from/opentelemetry/collector/use-cases/journald "Configure the OpenTelemetry Collector to ingest systemd journal logs from Linux hosts into Dynatrace.")[### Kafka': 'Настройте Collector для приёма логов журнала systemd в Dynatrace.](/managed/ingest-from/opentelemetry/collector/use-cases/journald "Настройте OpenTelemetry Collector для приёма логов журнала systemd с хостов Linux в Dynatrace.")[### Kafka',
        'Configure the Collector to integrate with Apache Kafka.](/managed/ingest-from/opentelemetry/collector/use-cases/kafka "How to configure the OpenTelemetry Collector to buffer data via Kafka.")[### Kubernetes': 'Настройте Collector для интеграции с Apache Kafka.](/managed/ingest-from/opentelemetry/collector/use-cases/kafka "Как настроить OpenTelemetry Collector для буферизации данных через Kafka.")[### Kubernetes',
        'Configure the Collector to enrich OTLP requests with Kubernetes data, monitor clusters, or to ingest pod logs.](/managed/ingest-from/opentelemetry/collector/use-cases/kubernetes "Configure the OpenTelemetry Collector to ingest Kubernetes data into Dynatrace.")[### Log files': 'Настройте Collector для обогащения запросов OTLP данными Kubernetes, мониторинга кластеров или приёма логов подов.](/managed/ingest-from/opentelemetry/collector/use-cases/kubernetes "Настройте OpenTelemetry Collector для приёма данных Kubernetes в Dynatrace.")[### Файлы логов',
        'Configure the Collector to ingest log files.](/managed/ingest-from/opentelemetry/collector/use-cases/filelog "Configure the OpenTelemetry Collector to ingest log data into Dynatrace.")[### Mask sensitive data': 'Настройте Collector для приёма файлов логов.](/managed/ingest-from/opentelemetry/collector/use-cases/filelog "Настройте OpenTelemetry Collector для приёма данных логов в Dynatrace.")[### Маскирование конфиденциальных данных',
        'Configure the Collector to mask sensitive data before forwarding to Dynatrace.](/managed/ingest-from/opentelemetry/collector/use-cases/redact "Configure the OpenTelemetry Collector to mask sensitive data before forwarding to Dynatrace.")[### Memory limits': 'Настройте Collector для маскирования конфиденциальных данных перед пересылкой в Dynatrace.](/managed/ingest-from/opentelemetry/collector/use-cases/redact "Настройте OpenTelemetry Collector для маскирования конфиденциальных данных перед пересылкой в Dynatrace.")[### Ограничения памяти',
        'Configure the Collector to respect memory limits and not use excessive system resources.](/managed/ingest-from/opentelemetry/collector/use-cases/memory "Configure the OpenTelemetry Collector to respect memory limits and not use excessive system resources.")[### Multiple backends': 'Настройте Collector для соблюдения ограничений памяти и предотвращения чрезмерного использования системных ресурсов.](/managed/ingest-from/opentelemetry/collector/use-cases/memory "Настройте OpenTelemetry Collector для соблюдения ограничений памяти и предотвращения чрезмерного использования системных ресурсов.")[### Несколько бэкендов',
        'Configure the Collector to export to multiple backends.](/managed/ingest-from/opentelemetry/collector/use-cases/multi-export "Configure the OpenTelemetry Collector to send data to more than one backend.")[### NetFlow': 'Настройте Collector для экспорта в несколько бэкендов.](/managed/ingest-from/opentelemetry/collector/use-cases/multi-export "Настройте OpenTelemetry Collector для отправки данных более чем в один бэкенд.")[### NetFlow',
        'Configure the Collector to ingest NetFlow packets.](/managed/ingest-from/opentelemetry/collector/use-cases/netflow "Configure the OpenTelemetry Collector to ingest NetFlow data.")[![Prometheus](https://dt-cdn.net/images/prometheus-logo-grey-e85840f462-8e7b2967a6.svg "Prometheus")': 'Настройте Collector для приёма пакетов NetFlow.](/managed/ingest-from/opentelemetry/collector/use-cases/netflow "Настройте OpenTelemetry Collector для приёма данных NetFlow.")[![Prometheus](https://dt-cdn.net/images/prometheus-logo-grey-e85840f462-8e7b2967a6.svg "Prometheus")',
        'Configure the Collector to scrape your Prometheus data.](/managed/ingest-from/opentelemetry/collector/use-cases/prometheus "Configure the OpenTelemetry Collector to scrape your Prometheus data.")[### Sampling': 'Настройте Collector для сбора ваших данных Prometheus.](/managed/ingest-from/opentelemetry/collector/use-cases/prometheus "Настройте OpenTelemetry Collector для сбора ваших данных Prometheus.")[### Сэмплирование',
        'Configure the Collector to sample distributed traces.](/managed/ingest-from/opentelemetry/collector/use-cases/sampling "Configure the OpenTelemetry Collector to sample data using the `tail_sampling` processor.")[### StatsD': 'Настройте Collector для сэмплирования распределённых трассировок.](/managed/ingest-from/opentelemetry/collector/use-cases/sampling "Настройте OpenTelemetry Collector для сэмплирования данных с помощью processor `tail_sampling`.")[### StatsD',
        'Configure the Collector to ingest StatsD data.](/managed/ingest-from/opentelemetry/collector/use-cases/statsd "Configure the OpenTelemetry Collector to ingest StatsD data.")[### Syslog': 'Настройте Collector для приёма данных StatsD.](/managed/ingest-from/opentelemetry/collector/use-cases/statsd "Настройте OpenTelemetry Collector для приёма данных StatsD.")[### Syslog',
        'Configure the Collector to ingest syslog data.](/managed/ingest-from/opentelemetry/collector/use-cases/syslog "Configure the OpenTelemetry Collector to ingest syslog data into Dynatrace.")[### Transform and filter': 'Настройте Collector для приёма данных syslog.](/managed/ingest-from/opentelemetry/collector/use-cases/syslog "Настройте OpenTelemetry Collector для приёма данных syslog в Dynatrace.")[### Преобразование и фильтрация',
        'Configure the Collector to add, transform, and drop OpenTelemetry data.](/managed/ingest-from/opentelemetry/collector/use-cases/transform "Configure the OpenTelemetry Collector to add, transform, and drop OpenTelemetry data.")[![Zipkin](https://dt-cdn.net/images/zipkin-gray-300-7e572e6589.png "Zipkin")': 'Настройте Collector для добавления, преобразования и отбрасывания данных OpenTelemetry.](/managed/ingest-from/opentelemetry/collector/use-cases/transform "Настройте OpenTelemetry Collector для добавления, преобразования и отбрасывания данных OpenTelemetry.")[![Zipkin](https://dt-cdn.net/images/zipkin-gray-300-7e572e6589.png "Zipkin")',
        'Configure the Collector to ingest and transform Zipkin data into Dynatrace.](/managed/ingest-from/opentelemetry/collector/use-cases/zipkin "Configure the OpenTelemetry Collector to ingest and convert Zipkin data into Dynatrace.")': 'Настройте Collector для приёма и преобразования данных Zipkin в Dynatrace.](/managed/ingest-from/opentelemetry/collector/use-cases/zipkin "Настройте OpenTelemetry Collector для приёма и преобразования данных Zipkin в Dynatrace.")',
    },
}

# Lines copied verbatim (component-block headers + EN-kept card product titles).
PASS = {
    "jaeger.md": {"### Receivers", "### Exporters"},
    "zipkin.md": {"### Receivers", "### Exporters"},
    "fluentd.md": {"### Receivers", "### Exporters"},
    "grpc.md": {"### Receivers", "### Exporters"},
    "statsd.md": {"### Receivers", "### Exporters"},
    "filelog.md": {"### Receivers", "### Exporters"},
    "netflow.md": {"### Receivers", "### Processors", "### Exporters"},
    "multi-export.md": {"### Receivers", "### Exporters"},
    "use-cases.md": {
        "### FluentD",
        "### Jaeger",
        "### Journald",
        "### Prometheus",
        "### Zipkin",
    },
}


def read_lf(p):
    with open(p, "r", encoding="utf-8", newline="") as f:
        return f.read().replace("\r\n", "\n").replace("\r", "\n")


def build(fname):
    sub = REL.get(fname, SUB)
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
