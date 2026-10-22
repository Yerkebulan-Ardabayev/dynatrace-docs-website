---
title: Configure OTLP metrics ingestion
source: https://docs.dynatrace.com/managed/ingest-from/opentelemetry/otlp-api/ingest-otlp-metrics/configure-otlp-metrics-classic
---

# Configure OTLP metrics ingestion

# Configure OTLP metrics ingestion

* Explanation
* 3-min read
* Updated on Oct 15, 2026

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
* Even though you can modify the default attribute list, Dynatrace does not recommend that you change or remove attributes starting with `dt.*`. Dynatrace uses these attributes to [enrich ingested metrics with Dynatrace-specific dimensions](/managed/ingest-from/extend-dynatrace/extend-data "Enrich telemetry you send directly to Dynatrace by reading host and Kubernetes resource attributes from the OneAgent and Dynatrace Operator enrichment files.").
* Dynatrace allows a maximum of 50 dimensions per metric. For details, see [Limits](/managed/ingest-from/opentelemetry/otlp-api/ingest-otlp-metrics/about-metrics-ingest#api-limits-and-validations "Learn how Dynatrace ingests OpenTelemetry metrics and what limitations apply.").

The allow list applies to all ingested OTLP metrics. To drop a dimension from specific metrics only, use the [metric dimension block list](/managed/analyze-explore-automate/metrics-classic/metric-dimensions-best-practices#metric-dimension-block-list "Choose dimension tuples with care, stay within cardinality limits, avoid rejected data points, and use the metric dimension block list.").

Name conflicts

See [Attribute ingestion](/managed/ingest-from/opentelemetry/otlp-api/ingest-otlp-metrics/about-metrics-ingest#attribute-ingestion "Learn how Dynatrace ingests OpenTelemetry metrics and what limitations apply.") for details on how Dynatrace ingests data of different attributes sharing the same name.