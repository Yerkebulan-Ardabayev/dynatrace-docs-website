# -*- coding: utf-8 -*-
"""L4-IF.69 builder for prometheus.md (Scrape Prometheus metrics with the OTel
Collector). Mirrors already-shipped siblings; only lines unique to this file are
added here, the rest resolve from the shared S canon.
"""

from _otel_canon import S, SUB, build_one, qa_one

TT_OTLP = "Learn about the OTLP API endpoints that your application uses to export OpenTelemetry data to Dynatrace."
RU_OTLP = "Узнайте об эндпоинтах OTLP API, которые ваше приложение использует для экспорта данных OpenTelemetry в Dynatrace."
TT_LEARN = "Learn how to use the OpenTelemetry Collector, including the Dynatrace OTel Collector, to ingest telemetry from OpenTelemetry."
RU_LEARN = "Узнайте, как использовать OpenTelemetry Collector, включая Dynatrace OTel Collector, для приёма телеметрии из OpenTelemetry."

TRANS = {
    # ----- lines unique to prometheus.md -----
    "title: Scrape Prometheus metrics with the OTel Collector": "title: Сбор метрик Prometheus с помощью OTel Collector",
    "# Scrape Prometheus metrics with the OTel Collector": "# Сбор метрик Prometheus с помощью OTel Collector",
    "* Updated on May 04, 2026": "* Обновлено 04 мая 2026 г.",
    "The following configuration example shows how you configure a Collector instance to scrape data from an existing Prometheus setup and import it as an OTLP request into Dynatrace.": "В следующем примере конфигурации показано, как настроить экземпляр Collector для сбора данных из существующей установки Prometheus и их импорта в виде запроса OTLP в Dynatrace.",
    "* A Prometheus instance running on port 8888": "* Экземпляр Prometheus, работающий на порту 8888",
    "* One of the following Collector distributions with the [Prometheus receiver](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/v0.151.0/receiver/prometheusreceiver), the [metric start time processor](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/v0.151.0/processor/metricstarttimeprocessor), and the [cumulative-to-delta processor](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/v0.151.0/processor/cumulativetodeltaprocessor):": "* Один из следующих дистрибутивов Collector с [receiver Prometheus](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/v0.151.0/receiver/prometheusreceiver), [processor metric start time](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/v0.151.0/processor/metricstarttimeprocessor) и [processor cumulative-to-delta](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/v0.151.0/processor/cumulativetodeltaprocessor):",
    "Dynatrace Collector v0.41.0+": "Dynatrace Collector v0.41.0+",
    "The example pipeline below uses the [`metricstarttime` processor](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/v0.151.0/processor/metricstarttimeprocessor), which adds start timestamps to metrics, and the [`cumulativetodelta` processor](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/v0.151.0/processor/cumulativetodeltaprocessor), which converts the metrics to delta temporality.": "В приведённом ниже конвейере используется [processor `metricstarttime`](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/v0.151.0/processor/metricstarttimeprocessor), который добавляет к метрикам начальные метки времени, и [processor `cumulativetodelta`](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/v0.151.0/processor/cumulativetodeltaprocessor), который преобразует метрики в дельта-темпоральность.",
    "Dynatrace OTel Collector v0.40.0 or earlier": "Dynatrace OTel Collector v0.40.0 или ранее",
    "To keep adjusting start times in the Prometheus receiver, run the Collector with the following flag:": "Чтобы продолжить корректировать начальные значения времени в receiver Prometheus, запустите Collector со следующим флагом:",
    "Cumulativetodelta processor recommendation": "Рекомендация по processor cumulativetodelta",
    "It is recommended to set the `max_staleness` parameter of the [cumulativetodelta processor](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/v0.151.0/processor/cumulativetodeltaprocessor) to a value higher than how often the Collector receives metrics (e.g., how often metrics via OTLP are received, or how long the Prometheus scrape interval is). This ensures that no references to abandoned metric streams accumulate in memory over time.": "Рекомендуется задавать параметру `max_staleness` [processor cumulativetodelta](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/v0.151.0/processor/cumulativetodeltaprocessor) значение, превышающее частоту получения метрик Collector (например, частоту получения метрик через OTLP или длительность интервала сбора Prometheus). Это гарантирует, что со временем в памяти не накапливаются ссылки на заброшенные потоки метрик.",
    "Under `receivers`, we specify the `prometheus` receiver as active receiver component for our Collector instance. We configure the receiver with the two jobs `node-exporter` and `opentelemetry-collector` under `scrape_configs`, to fetch data from the specified hosts once a minute (`scrape_interval: 60s`).": "В разделе `receivers` мы указываем receiver `prometheus` в качестве активного компонента receiver для нашего экземпляра Collector. Мы настраиваем receiver двумя заданиями `node-exporter` и `opentelemetry-collector` в разделе `scrape_configs`, чтобы получать данные с указанных хостов раз в минуту (`scrape_interval: 60s`).",
    "For a full list of configuration parameters, see the [Prometheus documentation](https://github.com/prometheus/prometheus/blob/v2.28.1/docs/configuration/configuration.md).": "Полный список параметров конфигурации см. в [документации Prometheus](https://github.com/prometheus/prometheus/blob/v2.28.1/docs/configuration/configuration.md).",
    'Under `processors`, we specify the [`cumulativetodelta` processor](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/v0.151.0/processor/cumulativetodeltaprocessor) to convert the metrics emitted by the Prometheus receiver to their [delta aggregation format](/managed/ingest-from/opentelemetry/collector/configuration#delta-metrics "How to configure the OpenTelemetry Collector.").': 'В разделе `processors` мы указываем [processor `cumulativetodelta`](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/v0.151.0/processor/cumulativetodeltaprocessor), чтобы преобразовать метрики, выдаваемые receiver Prometheus, в их [формат дельта-агрегации](/managed/ingest-from/opentelemetry/collector/configuration#delta-metrics "Как настроить OpenTelemetry Collector.").',
    "In Dynatrace Collector v0.41.0+, we specify the": "В Dynatrace Collector v0.41.0+ мы указываем",
    "[`metricstarttime`": "[processor `metricstarttime`](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/v0.151.0/processor/metricstarttimeprocessor),",
    "processor](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/v0.151.0/processor/metricstarttimeprocessor)": "чтобы",
    "to add start timestamps to the metrics. This is required to properly convert the metrics to delta temporality.": "добавить к метрикам начальные метки времени. Это необходимо для корректного преобразования метрик в дельта-темпоральность.",
    "Under `service`, we assemble our receiver, processor, and exporter objects into a metrics pipeline, which will execute the Prometheus jobs, convert their metrics to delta values, and ingest the data into Dynatrace.": "В разделе `service` мы собираем наши объекты receiver, processor и exporter в конвейер метрик, который выполняет задания Prometheus, преобразует их метрики в дельта-значения и принимает данные в Dynatrace.",
    "To avoid data duplication, make sure that only one OTel Collector scrapes a given target (for example, Kafka broker or Prometheus endpoint).": "Во избежание дублирования данных убедитесь, что заданную цель собирает только один OTel Collector (например, брокер Kafka или эндпоинт Prometheus).",
    "If you run multiple OTel Collector replicas, configure each one with a different target. This prevents duplicate metrics and unnecessary ingest costs.": "Если вы запускаете несколько реплик OTel Collector, настройте каждую из них на свою цель. Это предотвращает дублирование метрик и лишние затраты на приём данных.",
    "The [Target Allocator](https://opentelemetry.io/docs/platforms/kubernetes/operator/target-allocator/) automatically distributes the Prometheus targets among a pool of OTel Collectors.": "[Target Allocator](https://opentelemetry.io/docs/platforms/kubernetes/operator/target-allocator/) автоматически распределяет цели Prometheus между пулом OTel Collector.",
    '* [Prometheus data source](/managed/ingest-from/extensions/develop-your-extensions/data-sources/prometheus-extensions "Learn how to create a Prometheus extension using the Extensions framework.")': '* [Источник данных Prometheus](/managed/ingest-from/extensions/develop-your-extensions/data-sources/prometheus-extensions "Узнайте, как создать расширение Prometheus с помощью фреймворка Extensions.")',
    # ----- distribution bullets (variants present in this file but ensure exact strings) -----
    '+ The [Dynatrace OTel Collector](/managed/ingest-from/opentelemetry/collector#dt-collector-dist "%s")'
    % TT_LEARN: '+ [Dynatrace OTel Collector](/managed/ingest-from/opentelemetry/collector#dt-collector-dist "%s")'
    % RU_LEARN,
    '+ OpenTelemetry [Contrib](/managed/ingest-from/opentelemetry/collector#collector-contrib "%s")'
    % TT_LEARN: '+ OpenTelemetry [Contrib](/managed/ingest-from/opentelemetry/collector#collector-contrib "%s")'
    % RU_LEARN,
    '+ A [custom Builder version](/managed/ingest-from/opentelemetry/collector#collector-builder "%s")'
    % TT_LEARN: '+ [пользовательская версия Builder](/managed/ingest-from/opentelemetry/collector#collector-builder "%s")'
    % RU_LEARN,
    **S,
}

PASS = {"### Receivers", "### Processors", "### Exporters"}

if __name__ == "__main__":
    build_one(SUB, "prometheus.md", TRANS, PASS)
    qa_one(SUB, "prometheus.md")
