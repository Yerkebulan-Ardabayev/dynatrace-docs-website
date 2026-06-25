# -*- coding: utf-8 -*-
"""L4-IF.70 builder: ingest-from/opentelemetry/otlp-api.md (hub file)."""

import sys, os

sys.path.insert(0, os.path.dirname(__file__))
from _otel_canon import S, build_one, qa_one

REL = "ingest-from/opentelemetry"
FNAME = "otlp-api.md"

TT_OTLP = "Learn about the OTLP API endpoints that your application uses to export OpenTelemetry data to Dynatrace."
RU_OTLP = "Узнайте об эндпоинтах OTLP API, которые ваше приложение использует для экспорта данных OpenTelemetry в Dynatrace."
TT_COLL = "Learn how to use the OpenTelemetry Collector, including the Dynatrace OTel Collector, to ingest telemetry from OpenTelemetry."
RU_COLL = "Узнайте, как использовать OpenTelemetry Collector, включая Dynatrace OTel Collector, для приёма телеметрии из OpenTelemetry."
TT_UC = "Configure your OpenTelemetry Collector instance for different use cases."
RU_UC = (
    "Настройте экземпляр OpenTelemetry Collector для различных сценариев использования."
)
TT_GRPC = (
    "Configure the OpenTelemetry Collector to transform a gRPC OTLP request to HTTP."
)
RU_GRPC = (
    "Настройте OpenTelemetry Collector для преобразования запроса gRPC OTLP в HTTP."
)
TT_MASK = "Configure the OpenTelemetry Collector to mask sensitive data before forwarding to Dynatrace."
RU_MASK = "Настройте OpenTelemetry Collector для маскирования конфиденциальных данных перед пересылкой в Dynatrace."
TT_ENRICH = "Learn how to automatically enrich your telemetry data with Dynatrace-specific fields."
RU_ENRICH = "Узнайте, как автоматически обогащать данные телеметрии полями, специфичными для Dynatrace."
TT_ENV = "Understand and learn how to work with monitoring environments."
RU_ENV = "Понять принцип работы со средами мониторинга и научиться с ними работать."
TT_AUTH = "Find out how to get authenticated to use the Dynatrace API."
RU_AUTH = "Узнайте, как пройти аутентификацию для работы с Dynatrace API."
TT_WALK = "Learn how to integrate and ingest OpenTelemetry data (traces, metrics, and logs) into Dynatrace."
RU_WALK = "Узнайте, как интегрировать и принимать данные OpenTelemetry (трассировки, метрики и логи) в Dynatrace."
TT_PVC = "Set up a persistent storage for containerized ActiveGate to be used as temporary storage for ingested data."
RU_PVC = "Настройте постоянное хранилище для контейнеризованного ActiveGate для использования в качестве временного хранилища принятых данных."
TT_OTLP_RECV = "https://github.com/open-telemetry/opentelemetry-collector/blob/v0.151.0/receiver/otlpreceiver/README.md"
TT_OTEL_API = "Use Dynatrace API as a target for OpenTelemetry exporters to ingest OpenTelemetry metrics, logs, and traces."
RU_OTEL_API = "Используйте Dynatrace API в качестве цели для экспортёров OpenTelemetry для приёма метрик, логов и трассировок OpenTelemetry."

TRANS = {
    # frontmatter / title
    "title: Dynatrace OTLP API endpoints": "title: Эндпоинты Dynatrace OTLP API",
    # h1
    "# Dynatrace OTLP API endpoints": "# Эндпоинты Dynatrace OTLP API",
    # metadata
    "* Explanation": "* Пояснение",
    "* 8-min read": "* Чтение: 8 мин",
    "* Updated on Jan 09, 2026": "* Обновлено 09 января 2026 г.",
    # intro paragraph
    "The [OpenTelemetry Protocol (OTLP)﻿](https://opentelemetry.io/docs/specs/otlp/) is the principal network protocol for the exchange of telemetry data between OpenTelemetry-backed services and applications.": "Протокол [OpenTelemetry Protocol (OTLP)](https://opentelemetry.io/docs/specs/otlp/) является основным сетевым протоколом для обмена данными телеметрии между сервисами и приложениями на базе OpenTelemetry.",
    "Dynatrace provides native OTLP endpoints with the following services:": "Dynatrace предоставляет нативные OTLP-эндпоинты для следующих сервисов:",
    "* The Dynatrace Managed platform.": "* Платформа Dynatrace Managed.",
    "* ActiveGate instances.": "* Экземпляры ActiveGate.",
    'Alternatively, you can deploy the [Dynatrace Collector](/managed/ingest-from/opentelemetry/collector "%s") as an intermediary service application to batch requests and improve network performance, or to transform requests before forwarding them to Dynatrace (for example, [mask sensitive data](/managed/ingest-from/opentelemetry/collector/use-cases/redact "%s")).'
    % (
        TT_COLL,
        TT_MASK,
    ): 'Кроме того, можно развернуть [Dynatrace Collector](/managed/ingest-from/opentelemetry/collector "%s") в качестве промежуточного сервисного приложения для группировки запросов и повышения производительности сети или для преобразования запросов перед их пересылкой в Dynatrace (например, [маскирование конфиденциальных данных](/managed/ingest-from/opentelemetry/collector/use-cases/redact "%s")).'
    % (RU_COLL, RU_MASK),
    # ## Default ingest paths
    "## Default ingest paths": "## Пути приёма данных по умолчанию",
    "The ingest paths used by Dynatrace for the individual signal types follow the [standard OpenTelemetry paths﻿](https://opentelemetry.io/docs/specs/otel/protocol/exporter/#endpoint-urls-for-otlphttp).": "Пути приёма данных, используемые Dynatrace для отдельных типов сигналов, соответствуют [стандартным путям OpenTelemetry](https://opentelemetry.io/docs/specs/otel/protocol/exporter/#endpoint-urls-for-otlphttp).",
    # table header row
    "| Signal Type | Path |": "| Тип сигнала | Путь |",
    # table data rows
    "| Traces | `/v1/traces` |": "| Трассировки | `/v1/traces` |",
    "| Metrics | `/v1/metrics` |": "| Метрики | `/v1/metrics` |",
    "| Logs | `/v1/logs` |": "| Логи | `/v1/logs` |",
    # paragraph after table
    'Depending on the configuration, you may need to append these paths individually to the base URLs of the following service endpoints when specifying the export URLs. This can happen either in-code, when using [manual instrumentation](/managed/ingest-from/opentelemetry/walkthroughs "%s"), or using the standard [environment variables﻿](https://opentelemetry.io/docs/languages/sdk-configuration/otlp-exporter/#endpoint-configuration).'
    % TT_WALK: 'В зависимости от конфигурации может потребоваться добавить эти пути отдельно к базовым URL следующих эндпоинтов сервисов при указании URL экспорта. Это может происходить либо в коде при использовании [ручного инструментирования](/managed/ingest-from/opentelemetry/walkthroughs "%s"), либо с помощью стандартных [переменных окружения](https://opentelemetry.io/docs/languages/sdk-configuration/otlp-exporter/#endpoint-configuration).'
    % RU_WALK,
    # ## Export to Dynatrace
    "## Export to Dynatrace": "## Экспорт в Dynatrace",
    "### Base URLs": "### Базовые URL",
    'The following addresses provide the base URLs for your OTLP ingest configuration. Use the URL applicable to your type of environment and replace the relevant part with your [environment ID](/managed/discover-dynatrace/get-started/monitoring-environment "%s").'
    % TT_ENV: 'Следующие адреса предоставляют базовые URL для настройки приёма OTLP. Используйте URL, подходящий для вашего типа среды, и замените соответствующую часть на ваш [идентификатор среды](/managed/discover-dynatrace/get-started/monitoring-environment "%s").'
    % RU_ENV,
    "You will also use the base URL if you define the `OTEL_EXPORTER_OTLP_ENDPOINT` environment variable, see [Environment variables](#environment-variables).": "Базовый URL также используется при определении переменной окружения `OTEL_EXPORTER_OTLP_ENDPOINT`, см. раздел [Переменные окружения](#environment-variables).",
    # Base URLs table
    "| API Type | Base URL |": "| Тип API | Базовый URL |",
    "| Dynatrace Managed | `https://{your-domain}/e/{your-environment-id}/api/v2/otlp` |": "| Dynatrace Managed | `https://{your-domain}/e/{your-environment-id}/api/v2/otlp` |",
    "| Environment ActiveGate[1](#fn-1-1-def) | `https://{your-activegate-domain}:9999/e/{your-environment-id}/api/v2/otlp` |": "| Environment ActiveGate[1](#fn-1-1-def) | `https://{your-activegate-domain}:9999/e/{your-environment-id}/api/v2/otlp` |",
    "| Containerized Environment ActiveGate[2](#fn-1-2-def) | `https://{your-activegate-domain}/e/{your-environment-id}/api/v2/otlp` |": "| Containerized Environment ActiveGate[2](#fn-1-2-def) | `https://{your-activegate-domain}/e/{your-environment-id}/api/v2/otlp` |",
    # footnotes
    "Environment ActiveGates listen by default on port `9999`. If you changed that port, adjust the port in the URL accordingly.": "Environment ActiveGate по умолчанию прослушивают порт `9999`. Если этот порт был изменён, скорректируйте порт в URL соответствующим образом.",
    'A [PVC](/managed/ingest-from/setup-on-k8s/guides/deployment-and-configuration/activegate-pvc "%s") is required for this setup.'
    % TT_PVC: 'Для этой настройки требуется [PVC](/managed/ingest-from/setup-on-k8s/guides/deployment-and-configuration/activegate-pvc "%s").'
    % RU_PVC,
    # ### URL examples
    "### URL examples": "### Примеры URL",
    "The following example URLs illustrate combinations of base URLs and paths for signal types.": "Следующие примеры URL иллюстрируют комбинации базовых URL и путей для типов сигналов.",
    # #### Cluster ActiveGate
    "#### Cluster ActiveGate": "#### Cluster ActiveGate",
    # Cluster ActiveGate table
    "| Signal type | URL |": "| Тип сигнала | URL |",
    "| Traces | `https://{your-domain}/e/{your-environment-id}/api/v2/otlp/v1/traces` |": "| Трассировки | `https://{your-domain}/e/{your-environment-id}/api/v2/otlp/v1/traces` |",
    "| Metrics | `https://{your-domain}/e/{your-environment-id}/api/v2/otlp/v1/metrics` |": "| Метрики | `https://{your-domain}/e/{your-environment-id}/api/v2/otlp/v1/metrics` |",
    "| Logs | `https://{your-domain}/e/{your-environment-id}/api/v2/otlp/v1/logs` |": "| Логи | `https://{your-domain}/e/{your-environment-id}/api/v2/otlp/v1/logs` |",
    # #### Environment ActiveGate
    "#### Environment ActiveGate": "#### Environment ActiveGate",
    # Environment ActiveGate table
    "| Traces | `https://{your-activegate-domain}:9999/e/{your-environment-id}/api/v2/otlp/v1/traces` |": "| Трассировки | `https://{your-activegate-domain}:9999/e/{your-environment-id}/api/v2/otlp/v1/traces` |",
    "| Metrics | `https://{your-activegate-domain}:9999/e/{your-environment-id}/api/v2/otlp/v1/metrics` |": "| Метрики | `https://{your-activegate-domain}:9999/e/{your-environment-id}/api/v2/otlp/v1/metrics` |",
    "| Logs | `https://{your-activegate-domain}:9999/e/{your-environment-id}/api/v2/otlp/v1/logs` |": "| Логи | `https://{your-activegate-domain}:9999/e/{your-environment-id}/api/v2/otlp/v1/logs` |",
    # Information enrichment callout
    "Information enrichment": "Обогащение информацией",
    "Vanilla OTLP exports to ActiveGate require manual enrichment of Dynatrace host information to have the proper topology information.": "Для стандартных экспортов OTLP в ActiveGate требуется ручное обогащение информацией о хосте Dynatrace для получения корректных данных топологии.",
    'To do so, make sure your traces have the correct mapping resource attributes set. The list of applicable attributes can be found in (or imported from) the [enrichment files](/managed/ingest-from/extend-dynatrace/extend-data "%s").'
    % TT_ENRICH: 'Для этого убедитесь, что в ваших трассировках заданы корректные атрибуты ресурса сопоставления. Список применимых атрибутов можно найти в [файлах обогащения](/managed/ingest-from/extend-dynatrace/extend-data "%s") (или импортировать оттуда).'
    % RU_ENRICH,
    # ### API limitations
    "### API limitations": "### Ограничения API",
    "Calls to Dynatrace API endpoints have the following limitations.": "Вызовы к эндпоинтам Dynatrace API имеют следующие ограничения.",
    "* gRPC is not supported.": "* gRPC не поддерживается.",
    "API calls need to use HTTP.": "Вызовы API должны использовать HTTP.",
    'You can use a Collector to transform a gRPC OTLP request to its HTTP counterpart, see [Transform OTLP gRPC to HTTP with the OTel Collector](/managed/ingest-from/opentelemetry/collector/use-cases/grpc "%s").'
    % TT_GRPC: 'Для преобразования запроса gRPC OTLP в его аналог по HTTP можно использовать Collector, см. [Преобразование OTLP gRPC в HTTP с помощью OTel Collector](/managed/ingest-from/opentelemetry/collector/use-cases/grpc "%s").'
    % RU_GRPC,
    "* JSON is not supported for Protocol Buffers.": "* JSON не поддерживается для Protocol Buffers.",
    "Binary format must be used.": "Необходимо использовать двоичный формат.",
    # ### Environment variables
    "### Environment variables": "### Переменные окружения",
    "When you configure your application to export to Dynatrace, one way is to configure certain environment variables as described below.": "При настройке приложения для экспорта в Dynatrace можно задать определённые переменные окружения, как описано ниже.",
    'For more information about language-specific configuration, see [Instrument your application](/managed/ingest-from/opentelemetry/walkthroughs "%s").'
    % TT_WALK: 'Дополнительные сведения о конфигурации для конкретных языков см. в разделе [Инструментирование вашего приложения](/managed/ingest-from/opentelemetry/walkthroughs "%s").'
    % RU_WALK,
    # ### Authentication and access tokens (Export to Dynatrace section)
    "### Authentication and access tokens": "### Аутентификация и токены доступа",
    'For exports to ActiveGate, authentication is handled using an API access token and the `Authorization` HTTP header.\nFor more information on access tokens, see [Dynatrace API - Tokens and authentication](/managed/dynatrace-api/basics/dynatrace-api-authentication "%s").'
    % TT_AUTH: None,  # multi-line won't match; handle as individual lines
    "For exports to ActiveGate, authentication is handled using an API access token and the `Authorization` HTTP header.": "Для экспортов в ActiveGate аутентификация осуществляется с помощью API-токена доступа и HTTP-заголовка `Authorization`.",
    'For more information on access tokens, see [Dynatrace API - Tokens and authentication](/managed/dynatrace-api/basics/dynatrace-api-authentication "%s").'
    % TT_AUTH: 'Дополнительные сведения о токенах доступа см. в разделе [Dynatrace API: токены и аутентификация](/managed/dynatrace-api/basics/dynatrace-api-authentication "%s").'
    % RU_AUTH,
    'To create an access token, in Dynatrace, go to ![Access tokens](https://dt-cdn.net/images/access-tokens-512-a766b810b8.png "Access tokens") **Access Tokens**.': 'Для создания токена доступа в Dynatrace перейдите в ![Access tokens](https://dt-cdn.net/images/access-tokens-512-a766b810b8.png "Access tokens") **Access Tokens**.',
    "Use the appropriate access scopes for the signals that you want to export.": "Используйте соответствующие области доступа для сигналов, которые требуется экспортировать.",
    "You can combine scopes in a single token, and also add scopes to an existing token.": "Области доступа можно объединять в одном токене, а также добавлять их к существующему токену.",
    "* Traces: `openTelemetryTrace.ingest`": "* Трассировки: `openTelemetryTrace.ingest`",
    "* Metrics: `metrics.ingest`": "* Метрики: `metrics.ingest`",
    "* Logs: `logs.ingest`": "* Логи: `logs.ingest`",
    # ### Network requirements (Export to Dynatrace section)
    "### Network requirements": "### Сетевые требования",
    "Verify that the following are true:": "Убедитесь, что выполняются следующие условия:",
    "* TCP port is not blocked": "* TCP-порт не заблокирован",
    "Because OTLP communication with ActiveGate takes place over the ports 443 (for SaaS and Managed) or 9999 (for Environment ActiveGates), make sure that the TCP port in question is not blocked by a firewall or any other network management solution you might be using.": "Поскольку OTLP-взаимодействие с ActiveGate осуществляется через порты 443 (для SaaS и Managed) или 9999 (для Environment ActiveGate), убедитесь, что соответствующий TCP-порт не заблокирован межсетевым экраном или другим применяемым решением для управления сетью.",
    "* Your system's certificate trust store is up to date": "* Хранилище доверенных сертификатов системы актуально",
    "To avoid possible SSL certificate issues with expired or missing default root certificates, make sure that your system's certificate trust store is up to date.": "Чтобы избежать возможных проблем с SSL-сертификатами из-за просроченных или отсутствующих корневых сертификатов по умолчанию, убедитесь, что хранилище доверенных сертификатов вашей системы актуально.",
    # ## Export to the OTel Collector
    "## Export to the OTel Collector": "## Экспорт в OTel Collector",
    'Using the OTel Collector as an intermediate gateway allows you to streamline and optimize your telemetry data and requests centrally. See [OTel Collector use cases](/managed/ingest-from/opentelemetry/collector/use-cases "%s") for more information and sample configurations for popular Collector use cases.'
    % TT_UC: 'Использование OTel Collector в качестве промежуточного шлюза позволяет централизованно оптимизировать данные телеметрии и запросы. Дополнительные сведения и примеры конфигураций для популярных сценариев использования Collector см. в разделе [Сценарии использования OTel Collector](/managed/ingest-from/opentelemetry/collector/use-cases "%s").'
    % RU_UC,
    'See [OTel Collector for ingesting telemetry into Dynatrace](/managed/ingest-from/opentelemetry/collector "%s") for more details on how to configure a Collector instance.'
    % TT_COLL: 'Дополнительные сведения о настройке экземпляра Collector см. в разделе [OTel Collector для приёма телеметрии в Dynatrace](/managed/ingest-from/opentelemetry/collector "%s").'
    % RU_COLL,
    # gRPC conversion callout
    "gRPC conversion": "Преобразование gRPC",
    "As Dynatrace currently requires OTLP exports with HTTP, you can use the OTel Collector to convert gRPC exports to HTTP.": "Поскольку Dynatrace в настоящее время требует экспорта OTLP по HTTP, можно использовать OTel Collector для преобразования экспортов gRPC в HTTP.",
    'See [Transform OTLP gRPC to HTTP with the OTel Collector](/managed/ingest-from/opentelemetry/collector/use-cases/grpc "%s") for more details.'
    % TT_GRPC: 'Дополнительные сведения см. в разделе [Преобразование OTLP gRPC в HTTP с помощью OTel Collector](/managed/ingest-from/opentelemetry/collector/use-cases/grpc "%s").'
    % RU_GRPC,
    # ### Authentication and TLS (Export to OTel Collector section)
    "### Authentication and TLS": "### Аутентификация и TLS",
    "Whether you need to use TLS and authenticate your requests against the OTel Collector depends on your particular Collector setup/configuration. By default, the [OTLP receiver﻿](https://github.com/open-telemetry/opentelemetry-collector/blob/v0.151.0/receiver/otlpreceiver/README.md) is configured for plain-text HTTP and does not require authentication.": "Необходимость использования TLS и аутентификации запросов к OTel Collector зависит от конкретной настройки и конфигурации Collector. По умолчанию [receiver OTLP](https://github.com/open-telemetry/opentelemetry-collector/blob/v0.151.0/receiver/otlpreceiver/README.md) настроен для работы по HTTP без шифрования и не требует аутентификации.",
    "The eventual outbound connection from the OTel Collector to Dynatrace always requires authentication and TLS.": "Исходящее соединение из OTel Collector в Dynatrace всегда требует аутентификации и TLS.",
    # ### Network requirements (Export to OTel Collector section)
    # Same heading key as above - but it appears twice in the file.
    # build_one matches each line independently, same key resolves to same value - OK.
    "* Network ports not blocked": "* Сетевые порты не заблокированы",
    "Make sure the network ports required by the configured receiver instances are not blocked by a firewall or any other network management solution used as part of your infrastructure.": "Убедитесь, что сетевые порты, необходимые для настроенных экземпляров receiver, не заблокированы межсетевым экраном или другим решением для управления сетью, используемым в вашей инфраструктуре.",
    # ## Related topics
    '* [OpenTelemetry Protocol (OTLP) ingest API](/managed/dynatrace-api/environment-api/opentelemetry "%s")'
    % TT_OTEL_API: '* [API приёма OpenTelemetry Protocol (OTLP)](/managed/dynatrace-api/environment-api/opentelemetry "%s")'
    % RU_OTEL_API,
    **S,
}

# Remove the multi-line None sentinel if present
TRANS = {k: v for k, v in TRANS.items() if v is not None}

# Table separators, bare footnote markers — no Russian, copy verbatim
PASS = {
    "| --- | --- |",
    "1",
    "2",
}

if __name__ == "__main__":
    build_one(REL, FNAME, TRANS, PASS)
    qa_one(REL, FNAME)
