---
title: Custom metric metadata
source: https://www.dynatrace.com/docs/ingest-from/extend-dynatrace/extend-metrics/reference/custom-metric-metadata
scraped: 2026-02-24T21:33:02.304727
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

#### The `MetricProperties` object

Properties of a metric.

#### The `MetricDimensions` object

A dimension of the metric.

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