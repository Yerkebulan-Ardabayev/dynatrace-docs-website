# -*- coding: utf-8 -*-
from _otel_canon import S, SUB, build_one, qa_one

TT_OTLP = "Learn about the OTLP API endpoints that your application uses to export OpenTelemetry data to Dynatrace."
RU_OTLP = "Узнайте об эндпоинтах OTLP API, которые ваше приложение использует для экспорта данных OpenTelemetry в Dynatrace."
TT_ENRICHF = "Learn how to automatically enrich your telemetry data with Dynatrace-specific fields."
RU_ENRICHF = "Узнайте, как автоматически обогащать данные телеметрии полями, специфичными для Dynatrace."

TRANS = {
    # title / H1 (duplicated H1 line in source)
    "title: Enrich OTLP with OneAgent data (non-containerized)": "title: Обогащение OTLP данными OneAgent (вне контейнеров)",
    "# Enrich OTLP with OneAgent data (non-containerized)": "# Обогащение OTLP данными OneAgent (вне контейнеров)",
    # metadata
    "* Updated on Dec 17, 2025": "* Обновлено 17 декабря 2025 г.",
    # intro
    "The following configuration example shows how you configure a Collector instance to enrich OpenTelemetry data with OneAgent host entities.": "В следующем примере конфигурации показано, как настроить экземпляр Collector для обогащения данных OpenTelemetry сущностями хостов OneAgent.",
    "Enrichment is used for linking OpenTelemetry data to its OneAgent host and properly associating it within the topology model. For example, when ingesting logs from different hosts, tying the host entity to the respective log data allows you to run host-based log analytics tasks.": "Обогащение используется для связывания данных OpenTelemetry с их хостом OneAgent и корректного сопоставления в модели топологии. Например, при приёме логов с разных хостов привязка сущности хоста к соответствующим данным логов позволяет выполнять задачи аналитики логов на основе хостов.",
    # container note
    "Container environments": "Контейнерные среды",
    "Enrichment is specific to non-container OneAgent environments. Configuring a containerized Collector enrichment setup may lead to incorrect host and topology associations.": "Обогащение применимо только к неконтейнерным средам OneAgent. Настройка обогащения в контейнеризированном Collector может привести к некорректным сопоставлениям хостов и топологии.",
    # prerequisites (this file's resourcedetection variant + system env var suffixes)
    "* One of the following Collector distributions with the [Resource Detection processor](https://github.com/open-telemetry/opentelemetry-collector-contrib/blob/v0.151.0/processor/resourcedetectionprocessor):": "* Один из следующих дистрибутивов Collector с [processor Resource Detection](https://github.com/open-telemetry/opentelemetry-collector-contrib/blob/v0.151.0/processor/resourcedetectionprocessor):",
    "* A OneAgent running on the same host as the OTel Collector, where the OneAgent monitors in either Full-Stack, Infrastructure, or Foundation & Discovery mode.": "* OneAgent, работающий на том же хосте, что и OTel Collector, при этом OneAgent ведёт мониторинг в режиме Full-Stack, Infrastructure или Foundation & Discovery.",
    '* The [Dynatrace API endpoint URL](/managed/ingest-from/opentelemetry/otlp-api "%s") to which the data should be exported, configured as system environment variable'
    % TT_OTLP: '* [URL эндпоинта Dynatrace API](/managed/ingest-from/opentelemetry/otlp-api "%s"), на который должны экспортироваться данные, заданный как системная переменная окружения'
    % RU_OTLP,
    '* An [API token](/managed/ingest-from/opentelemetry/otlp-api#authentication-export-to-activegate "%s") with the relevant access scope (only required for SaaS and ActiveGate), configured as system environment variable'
    % TT_OTLP: '* [API-токен](/managed/ingest-from/opentelemetry/otlp-api#authentication-export-to-activegate "%s") с соответствующей областью доступа (требуется только для SaaS и ActiveGate), заданный как системная переменная окружения'
    % RU_OTLP,
    # Receivers prose (unique to enrich)
    "Under `receivers`, we specify the standard `otlp` receiver as active receiver component for our Collector instance.": "В разделе `receivers` мы указываем стандартный receiver `otlp` в качестве активного компонента receiver для нашего экземпляра Collector.",
    "This is mainly for demonstration purposes. You can specify any other valid receiver here (for example, `zipkin`).": "Это сделано в основном в демонстрационных целях. Здесь можно указать любой другой допустимый receiver (например, `zipkin`).",
    # Processors prose (unique to enrich)
    "Under `processors`, we specify the [`resourcedetection` processor](https://github.com/open-telemetry/opentelemetry-collector-contrib/blob/v0.151.0/processor/resourcedetectionprocessor) and configure it with the [Dynatrace-specific detector `dynatrace`](https://github.com/open-telemetry/opentelemetry-collector-contrib/blob/v0.151.0/processor/resourcedetectionprocessor/README.md#dynatrace).": "В разделе `processors` мы указываем [processor `resourcedetection`](https://github.com/open-telemetry/opentelemetry-collector-contrib/blob/v0.151.0/processor/resourcedetectionprocessor) и настраиваем его с помощью [специфичного для Dynatrace детектора `dynatrace`](https://github.com/open-telemetry/opentelemetry-collector-contrib/blob/v0.151.0/processor/resourcedetectionprocessor/README.md#dynatrace).",
    'With this configuration, the resource detector processor will attempt to load the following three attributes from the [OneAgent enrichment file](/managed/ingest-from/extend-dynatrace/extend-data#dynatrace-oneagent "%s"):'
    % TT_ENRICHF: 'При такой конфигурации processor определения ресурсов попытается загрузить следующие три атрибута из [файла обогащения OneAgent](/managed/ingest-from/extend-dynatrace/extend-data#dynatrace-oneagent "%s"):'
    % RU_ENRICHF,
    "If the resource detector could load these values successfully, it will add them as resource attributes to the OTLP request. No additional processor configuration is necessary.": "Если processor определения ресурсов смог успешно загрузить эти значения, он добавит их в запрос OTLP в качестве атрибутов ресурса. Дополнительная настройка processor не требуется.",
    # Exporters: "For this purpose" with `headers` (mirror statsd sibling wording)
    "For this purpose, we set the following two environment variables and reference them in the configuration values for `endpoint` and `headers`.": "Для этого мы задаём следующие две переменные окружения и ссылаемся на них в значениях конфигурации `endpoint` и `headers`.",
    # Service pipeline prose (unique to enrich)
    "Under `service`, we assemble our receiver, processor, and exporter objects into service pipelines, which will perform these steps:": "В разделе `service` мы собираем наши объекты receiver, processor и exporter в сервисные конвейеры, которые выполнят следующие шаги:",
    "* accept OTLP requests on the configured ports": "* принимают запросы OTLP на настроенных портах",
    "* enrich them with the Dynatrace-relevant host data, using the resource detector processor": "* обогащают их данными хоста, релевантными для Dynatrace, с помощью processor определения ресурсов",
    "* and export the enriched data to Dynatrace": "* и экспортируют обогащённые данные в Dynatrace",
    **S,
}
PASS = {
    "### Receivers",
    "### Processors",
    "### Exporters",
    # pure code-span attribute bullets (kept EN verbatim)
    "* `dt.entity.host`",
    "* `host.name`",
    "* `dt.smartscape.host`",
}
if __name__ == "__main__":
    build_one(SUB, "enrich.md", TRANS, PASS)
    qa_one(SUB, "enrich.md")
