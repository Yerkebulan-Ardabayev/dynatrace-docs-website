---
title: Calculated metrics for services
source: https://docs.dynatrace.com/managed/observe/application-observability/services/calculated-service-metric
---

# Calculated metrics for services

# Calculated metrics for services

* How-to guide
* 5-min read
* Published Mar 30, 2021

Dynatrace automatically captures important metrics for services with no configuration required. You might need additional business or technical metrics that are specific to your application. These metrics can be calculated and derived based on a wide variety of available data within the captured distributed trace. You can also split these metrics by multiple dimensions, for example, a requests attribute or an HTTP method.

## Why start using OpenPipeline instead of classic calculated service metrics?

* More flexible metric creation from spans—with OpenPipeline, metrics are no longer limited to support at most 100 dimension values (“top X”).

  + You can store full dimension cardinality
  + You can combine dimensions freely
  + Powerful ingestion, processing, and transformation capabilities are available via a unified solution (that works the same for other configuration scopes, such as logs and events).
* Better scale and performance—platform-scale ingest and stream processing built to go beyond petabytes; no more 500 calculated service metrics limit per tenant.
* Security, cost management, and data governance—filter and mask sensitive or unnecessary fields; assign cost center usage to specific metrics; route data to specific Grail buckets with controlled retention durations.

Limits

* Only new data is written to calculated metrics; retrospective data is not included.
* You can have up to 500 enabled calculated metrics per environment and up to 100 enabled calculated metrics per service.
* Classic calculated metrics support at most 100 dimension values. This is referred to as the "top X" rule, as you can select fewer depending on your configuration. However you choose the top 100 dimension values, the remaining dimensions are aggregated into a single timeseries and the dimension value is accessible through a special `remainder` dimension. The [remainder](/managed/dynatrace-api/environment-api/metric-v2/metric-selector#remainder "Configure the metric selector for the Metric v2 API.") filter condition allowing you to filter on this `remainder` dimension.

## Create a calculated service metric

### Steps

1. Go to **Settings** > **Server-side service monitoring** > **Calculated service metrics** > **Create new metric**.
2. Enter the name for the metric.
   The name and the `calc:service.` prefix are added automatically to the metric key.
3. Choose the metric source from the **Metric source** list.

   * If the source is a request attribute, select the required unit.
   * Optional To exclude the data contribution of [muted requests](/managed/observe/application-observability/services/service-detection/service-detection-v1/service-monitoring-mute "Mute the monitoring of certain service requests so that you can focus on the performance of requests that affect your customers."), turn on **Ignore muted requests**.
4. Optional Select the management zone. The new metric will be restricted to data from this zone.
5. Provide conditions to define which requests are included in the calculation.

   If you provide several conditions, **all conditions must be fulfilled** to use the metric.

   1. Select **Add condition**.
   2. Select the attribute to be checked.
   3. Select the operator of the condition.
   4. If needed, specify the reference value.

      Preview shows the list of services to be included to the custom metric and the estimation of [DDU consumption](/managed/license/classic-licensing/davis-data-units/metric-cost-calculation "Understand how to calculate Davis data unit consumption and costs related to monitored metrics.").

      Preview only considers management zone and conditions based on service attributes. These attributes are marked with `[Service property]` in the attribute list.
6. Optional Add dimension to your new metric.

   1. Turn on **Split by dimension**.
   2. Choose the placeholders to define the dimension.

      * Select an available placeholder from **Dimension value pattern**.
      * Create a [custom placeholder](#placeholder).
   3. Enter a dimension name.
   4. Define the top *X* value limit.

      1. In the **Number of top values** field, specify the amount of top *X* values to be calculated for the metric.
      2. From the **Value sorting** and **Value aggregation** lists, select the sorting and aggregation of the top *X* values.
7. Review the metric source and dimension names. They will be used in the UI and API. Once a metric is created, you can't change them.
8. Select **Save metric**.

## Create a custom placeholder

When a placeholder is not available, you can create a custom placeholder. All custom placeholders must be used in the dimension value pattern, alternatevely you can delete unused custom placeholders.

Prior knowledge

### Extraction method

You have two methods to extract the value for a placeholder:

* Delimiter-based. In this case, Dynatrace extracts the value by checking the value of the source against a reference value and specified delimiter kind and position.
* Regex-based. In this case, Dynatrace uses regular expression extraction. To learn how Dynatrace uses regular expressions, see [Regular expressions in Dynatrace](/managed/manage/tags-and-metadata/reference/regular-expressions-in-dynatrace "Learn how to use regular expressions in the context of Dynatrace.").

### Extraction method for request attributes

Placeholders that are based on request attributes provide three options for value extraction:

* **First**: The first occurrence of the attribute is used to extract the value.
* **Last**: The last occurrence of the attribute is used to extract the value.
* **Count**: The value equals the number of attribute occurrences.

### Steps

To create a custom placeholder

1. While creating or editing a calculated service metric, select **Add custom placeholder**.
2. Enter a name for your placeholder. The name will be used in the **Dimension value pattern** field.
3. Select the source for the dimension.
4. Choose the [extraction method](#prior).

   If the source is a request attribute,

   1. Optional Select **Use from downstream services** checkbox to use child calls as the value source.
   2. Optional Restrict the child calls to a particular management zone or service tag.
5. Select **Add**.
6. Required Use the newly created placeholder in the dimension value pattern.

## Related topics

* [Service metrics API](/managed/dynatrace-api/configuration-api/calculated-metrics/service-metrics "Manage calculated service metrics via the Dynatrace configuration API.")
* [Multidimensional analysis](/managed/observe/application-observability/multidimensional-analysis "Configure a multidimensional analysis view and save it as a calculated metric.")