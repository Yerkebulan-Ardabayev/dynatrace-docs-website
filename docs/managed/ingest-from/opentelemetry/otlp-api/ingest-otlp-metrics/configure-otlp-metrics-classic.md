---
title: Configure OTLP metrics ingestion (Dynatrace Classic)
source: https://docs.dynatrace.com/managed/ingest-from/opentelemetry/otlp-api/ingest-otlp-metrics/configure-otlp-metrics-classic
---

# Configure OTLP metrics ingestion (Dynatrace Classic)

# Configure OTLP metrics ingestion (Dynatrace Classic)

* Explanation
* 3-min read
* Published May 11, 2026

To make these configuration changes, go to **Settings** > **Metrics** > **OpenTelemetry metrics**.

These settings affect your metric dimensions. Modifying any of them will cause your metrics to change, which may have an impact on existing dashboards, events, and alerts that make use of these dimensions. In this case, they will need to be updated manually.

### Add Meter name and version as metric dimensions

When **Add Meter name and version as metric dimensions** is turned on, the Meter name (also referred to as `InstrumentationScope` or `InstrumentationLibrary` in OpenTelemetry SDKs)
and version are automatically added as dimensions (`otel.scope.name` and `otel.scope.version`) to ingested OTLP metrics.

### Configure resource and scope attributes to be added as dimensions

In the section **Allow list: resource and scope attributes** you can configure which resource and scope attributes to add as dimensions to ingested OTLP metrics.

When the toggle **Add the resource and scope attributes configured below as dimensions** is turned on, the attributes defined in the list will be added as dimensions to ingested OTLP metrics if they are present in the OpenTelemetry resource or in the instrumentation scope.

Dynatrace defines a set of default attributes that we consider relevant and beneficial to have on all of your metrics. You can modify the defaults and add extra attributes that you want to have in all of your metrics from the OpenTelemetry resource/instrumentation scope.

* The attributes configured on the settings page are only added as dimensions to ingested OTLP metrics when the toggle **Add the resource and scope attributes configured below as dimensions** (see above) is turned on.
* Attribute names are case-sensitive and must be configured with the original name, as exported to Dynatrace by the telemetry source and before any possible transformation took place. For example, an attribute named `My:attribute` will be renamed to `my_attribute` upon ingestion
  (see [name rules](/managed/ingest-from/opentelemetry/otlp-api/ingest-otlp-metrics/about-metrics-ingest#dimension-keys "Learn how Dynatrace ingests OpenTelemetry metrics and what limitations apply.")) but still needs to be configured as `My:attribute` in the settings page.
* Even though you can modify the default attribute list, Dynatrace does not recommend that you change or remove attributes starting with `dt.*`. Dynatrace uses these attributes to [enrich ingested metrics with Dynatrace-specific dimensions](/managed/ingest-from/extend-dynatrace/extend-data "Learn how to automatically enrich your telemetry data with Dynatrace-specific fields.").
* Dynatrace allows a maximum of 50 dimensions per metric. For details, see [Limits](/managed/ingest-from/opentelemetry/otlp-api/ingest-otlp-metrics/about-metrics-ingest#api-limits-and-validations "Learn how Dynatrace ingests OpenTelemetry metrics and what limitations apply.").

Name conflicts

See [Attribute ingestion](/managed/ingest-from/opentelemetry/otlp-api/ingest-otlp-metrics/about-metrics-ingest#attribute-ingestion "Learn how Dynatrace ingests OpenTelemetry metrics and what limitations apply.") for details on how Dynatrace ingests data of different attributes sharing the same name.

### Ingest complete explicit bucket histograms

By default, Dynatrace ingests the histogram's `min|max|sum|count` values and drops the buckets. However, you can opt in to also ingest the buckets from explicit histograms.

Go to **Settings** > **Metrics** > **Histograms** and turn on **Ingest complete explicit bucket histograms**,

The setting applies to all explicit bucket histogram metrics in your environment. After you turn it on or off, it may take a few minutes for the settings to be applied.

Once buckets are ingested, they can be found by appending the suffix `_bucket` to the histogram's metric name. For example, `http.server.request.duration_bucket` for a histogram metric named `http.server.request.duration`.