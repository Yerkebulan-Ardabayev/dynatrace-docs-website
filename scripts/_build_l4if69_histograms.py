# -*- coding: utf-8 -*-
from _otel_canon import S, SUB, build_one, qa_one

TT_LEARN = "Learn how to use the OpenTelemetry Collector, including the Dynatrace OTel Collector, to ingest telemetry from OpenTelemetry."
RU_LEARN = "Узнайте, как использовать OpenTelemetry Collector, включая Dynatrace OTel Collector, для приёма телеметрии из OpenTelemetry."

TRANS = {
    # title / H1 (H1 appears twice in source)
    "title: Compute histogram summaries with the OTel Collector": "title: Вычисление сводок гистограмм с помощью OTel Collector",
    "# Compute histogram summaries with the OTel Collector": "# Вычисление сводок гистограмм с помощью OTel Collector",
    # metadata unique to this file
    "* Published Apr 08, 2024": "* Опубликовано 08 апреля 2024 г.",
    # intro
    "This page describes how to ingest histograms via the OTel Collector, which can help you to reduce costs associated with ingestion.": "На этой странице описывается, как принимать гистограммы с помощью OTel Collector, что может помочь сократить затраты, связанные с приёмом данных.",
    "You can also use the OTLP ingest API to ingest histograms directly, without additional data manipulation.": "Можно также использовать OTLP ingest API для прямого приёма гистограмм без дополнительной обработки данных.",
    "The following configuration example shows how to use the Collector to compute and ingest summaries of histogram buckets, such as the overall sum of all values in the bucket and their total count.": "В следующем примере конфигурации показано, как использовать Collector для вычисления и приёма сводок по интервалам гистограмм, таких как общая сумма всех значений в интервале и их общий счётчик.",
    # prerequisites bullet unique to this file (transform + filter processors)
    "* One of the following Collector distributions with the [transform](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/v0.151.0/processor/transformprocessor) and [filter](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/v0.151.0/processor/filterprocessor) processors:": "* Один из следующих дистрибутивов Collector с processor [transform](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/v0.151.0/processor/transformprocessor) и [filter](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/v0.151.0/processor/filterprocessor):",
    # Receivers
    "Under `receivers`, we specify the standard `otlp` receiver as active receiver component for our Collector instance and configure it to accept OTLP requests on gRPC and HTTP.": "В разделе `receivers` мы указываем стандартный receiver `otlp` в качестве активного компонента receiver для нашего экземпляра Collector и настраиваем его на приём запросов OTLP по gRPC и HTTP.",
    # Processors
    "Under `processors`, we configure the following two processor instances:": "В разделе `processors` мы настраиваем следующие два экземпляра processor:",
    "* [`transform`](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/v0.151.0/processor/transformprocessor), to compute the desired sum and count values of the histograms:": "* [`transform`](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/v0.151.0/processor/transformprocessor), чтобы вычислить нужные значения суммы и счётчика для гистограмм:",
    "+ We first use the function [`extract_count_metric`](https://github.com/open-telemetry/opentelemetry-collector-contrib/blob/v0.151.0/processor/transformprocessor/README.md#extract_count_metric) to compute the number of values in each histogram bucket.": "+ Сначала мы используем функцию [`extract_count_metric`](https://github.com/open-telemetry/opentelemetry-collector-contrib/blob/v0.151.0/processor/transformprocessor/README.md#extract_count_metric) для вычисления числа значений в каждом интервале гистограммы.",
    "+ Then, we use the function [`extract_sum_metric`](https://github.com/open-telemetry/opentelemetry-collector-contrib/blob/v0.151.0/processor/transformprocessor/README.md#extract_sum_metric) to compute the total sum of all of its values and convert it to a gauge using [`convert_sum_to_gauge`](https://github.com/open-telemetry/opentelemetry-collector-contrib/blob/v0.151.0/processor/transformprocessor/README.md#convert_sum_to_gauge).": "+ Затем мы используем функцию [`extract_sum_metric`](https://github.com/open-telemetry/opentelemetry-collector-contrib/blob/v0.151.0/processor/transformprocessor/README.md#extract_sum_metric) для вычисления общей суммы всех его значений и преобразуем её в gauge с помощью [`convert_sum_to_gauge`](https://github.com/open-telemetry/opentelemetry-collector-contrib/blob/v0.151.0/processor/transformprocessor/README.md#convert_sum_to_gauge).",
    "* [`filter`](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/v0.151.0/processor/filterprocessor), to drop the existing histogram buckets (based on `type`) and avoid histogram-related error messages.": "* [`filter`](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/v0.151.0/processor/filterprocessor), чтобы отбросить существующие интервалы гистограмм (на основе `type`) и избежать сообщений об ошибках, связанных с гистограммами.",
    "With this configuration, the Collector drops histogram metrics and creates in their place two new metrics for the sum and item count of each respective histogram.": "При такой конфигурации Collector отбрасывает метрики-гистограммы и создаёт вместо них две новые метрики для суммы и счётчика элементов каждой соответствующей гистограммы.",
    # env var intro (colon variant; S has the period-terminated form)
    "For this purpose, we set the following two environment variables and reference them in the configuration values for `endpoint` and `Authorization`:": "Для этого мы задаём следующие две переменные окружения и ссылаемся на них в значениях конфигурации `endpoint` и `Authorization`:",
    # Service pipelines (note: source heading is plural "### Service pipelines", in S)
    "Under `service`, we assemble our receiver and exporter objects into a metric pipeline and enable the two processors by referencing them under `processors`.": "В разделе `service` мы собираем наши объекты receiver и exporter в конвейер метрик и включаем оба экземпляра processor, ссылаясь на них в разделе `processors`.",
    **S,
}
PASS = {"### Receivers", "### Processors", "### Exporters"}
if __name__ == "__main__":
    build_one(SUB, "histograms.md", TRANS, PASS)
    qa_one(SUB, "histograms.md")
