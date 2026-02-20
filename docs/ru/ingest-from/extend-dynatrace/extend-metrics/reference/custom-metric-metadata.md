---
title: Custom metric metadata
source: https://www.dynatrace.com/docs/ingest-from/extend-dynatrace/extend-metrics/reference/custom-metric-metadata
scraped: 2026-02-20T21:14:19.243526
---

# Custom metric metadata

# Custom metric metadata

* Latest Dynatrace
* 1-min read
* Updated on Nov 25, 2025

To add more context to data points and their dimensions, your custom metric can carry additional useful information, such as the unit of measurement, display name, and value ranges.

You can provide such information via custom metric metadata. Metadata is stored independently from data points and tied together by the metric key. You can push data points and set metadata in any order.

You cannot provide metadata for built-in or calculated metrics; metadata is supported only for custom ingested metrics.

## Available parameters

The following parameters are available for metric metadata.

Parameters

Example JSON

Parameter

Type

Description

displayName

string

The name of the metric in the user interface.

description

string

A short description of the metric.

unit

string

The unit of the metric.

Find the possible values in the description of the **unit** field for [built-in metrics](/docs/dynatrace-api/environment-api/metric-v2/get-descriptor "View the descriptor of a metric via Metrics v2 API.").

sourceEntityType

string

The entity type of the metric. Used for management zone filtering.

For details, see [Metric entity type](/docs/analyze-explore-automate/metrics-classic/metrics-mz#entity-based-rules "How to filter metrics by management zone and related security considerations").

tags

string[]

A list of tags applied to the metric.

metricProperties

[MetricProperties](#properties)

A list of the metric's properties.

dimensions

[MetricDimensions](#dimensions)[]

A list of the metric's dimensions.

#### The `MetricProperties` object

Properties of a metric.

Parameter

Type

Description

minValue

integer

The minimum allowed value of the metric.

maxValue

integer

The maximum allowed value of the metric.

rootCauseRelevant

boolean

Whether (`true` or `false`) the metric is related to a root cause of a problem.

A root-cause relevant metric represents a strong indicator for a faulty component.

impactRelevant

boolean

Whether (`true` or `false`) the metric is relevant to a problem's impact.

An impact-relevant metric is highly dependent on other metrics and changes because an underlying root-cause metric has changed.

valueType

string

The type of the metric's value. You have these options:

* `score`: A score metric is a metric where high values indicate a good situation, while low values indicate trouble. An example of such a metric is a success rate.
* `error`: An error metric is a metric where high values indicate trouble, while low values indicate a good situation. An example of such a metric is an error count.

latency

integer

The reporting delay of the metrics, in minutes.

The delay caused by constraints of cloud vendors or other third-party data sources that leads to a latency in data ingest on the Dynatrace side.

#### The `MetricDimensions` object

A dimension of the metric.

Parameter

Type

Description

key

string

The key of the dimension to be used in the [ingestion protocol](/docs/ingest-from/extend-dynatrace/extend-metrics/reference/metric-ingestion-protocol "Learn how the data ingestion protocol for Dynatrace Metrics API works.").

displayName

string

The name of the dimension in the user interface.

```
{



"displayName": "Total revenue",



"description": "Total store revenue by region, city, and store",



"unit": "Unspecified",



"sourceEntityType": "string",



"tags": ["KPI", "Business"],



"metricProperties": {



"maxValue": 1000000,



"minValue": 0,



"rootCauseRelevant": false,



"impactRelevant": true,



"valueType": "score",



"latency": 1



},



"dimensions": [



{



"key": "city",



"displayName": "City name"



},



{



"key": "country",



"displayName": "Country name"



},



{



"key": "region",



"displayName": "Sales region"



},



{



"key": "store",



"displayName": "Store #"



}



]



}
```

## Set metric metadata

Use the [POST an object](/docs/dynatrace-api/environment-api/settings/objects/post-object "Create or validate a settings object via the Dynatrace API.") call of the Settings API to provide metadata for your metric. Use the following parameters in the payload:

| Field | Value |
| --- | --- |
| scope | metric-{your-metric-key} |
| schemaId | builtin:metric.metadata |
| value | The desired set of metadata. See the available fields above. |

Example payload

```
[



{



"scope": "metric-business.shop.revenue",



"schemaId": "builtin:metric.metadata",



"value": {



"displayName": "Total revenue",



"description": "Total store revenue by region, city, and store",



"unit": "Unspecified",



"sourceEntityType": "string",



"tags": ["KPI", "Business"],



"metricProperties": {



"maxValue": 1000000,



"minValue": 0,



"rootCauseRelevant": false,



"impactRelevant": true,



"valueType": "score",



"latency": 1



},



"dimensions": [



{



"key": "city",



"displayName": "City name"



},



{



"key": "country",



"displayName": "Country name"



},



{



"key": "region",



"displayName": "Sales region"



},



{



"key": "store",



"displayName": "Store #"



}



]



}



}



]
```

Alternatively, you can:

* Send metadata via the [ingestion protocol](/docs/ingest-from/extend-dynatrace/extend-metrics/reference/metric-ingestion-protocol#metadata "Learn how the data ingestion protocol for Dynatrace Metrics API works.").
* Configure a metric's metadata in [Metrics browser](/docs/analyze-explore-automate/dashboards-classic/metrics-browser "Browse metrics with the Dynatrace metrics browser.").

## View metric metadata

You can retrieve the metadata of a metric via the [GET metric descriptor](/docs/dynatrace-api/environment-api/metric-v2/get-descriptor "View the descriptor of a metric via Metrics v2 API.") call of the Metrics v2 API or via the [Metrics browser](/docs/analyze-explore-automate/dashboards-classic/metrics-browser "Browse metrics with the Dynatrace metrics browser.").

## Related topics

* [Metrics API - POST ingest data points](/docs/dynatrace-api/environment-api/metric-v2/post-ingest-metrics "Ingest custom metrics to Dynatrace via Metrics v2 API.")
* [Settings API](/docs/dynatrace-api/environment-api/settings "Find out what the Dynatrace Settings API offers.")