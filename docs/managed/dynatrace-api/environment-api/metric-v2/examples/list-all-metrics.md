---
title: Metrics API examples - List all metrics
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/metric-v2/examples/list-all-metrics
---

# Metrics API examples - List all metrics

# Metrics API examples - List all metrics

* Reference
* Published May 26, 2020

The [GET metrics](/managed/dynatrace-api/environment-api/metric-v2/get-all-metrics "List all metrics available in your monitoring environment via Metrics v2 API.") endpoint provides you the ability to query multiple metrics, along with partial or even full descriptors of metrics.

This example shows how to fetch the list of all metrics in the environment with essential metadata.

The most important part is the metric key, as it is used to identify the metric. The key itself, however, doesn't provide much information about metric. To learn more about metrics, we can add this crucial information:

* metric name—provides more insight into what the metric measures
* unit of the metric—shows which unit the metric uses
* allowed aggregations—lists the available aggregations of the metric. The API rejects request for unsupported aggregations.

## Configure the request

To obtain the full list of metrics, you have to set the following query parameters:

* **pageSize** to `500`. The full list of metrics can be lengthy, so we're using the maximum possible value.
* **fields** to `displayName,unit,aggregationTypes`. This removes all other fields from the payload, only keeping those we're interested in. Note that `metricId` is omitted here, because it is always presented in the response.

You can get the response in two formats:

* JSON: set the **Accept** header of the request to `application/json`.
* CSV table: set the **Accept** header of the request to `text/csv; header=present`. If you're not interested in the header row, use `text/csv; header=absent`.

To authenticate the request, set the **Authorization** header of the request to `Api-token {your-token}`. The token must have the **Read metrics** (`metrics.read`) permission.

## Curl

Here's the Curl code of the request. Make sure to use the URL of your own environment and a real API token.

### JSON payload

```
curl -L -X GET 'https://mySampleEnv.live.dynatrace.com/api/v2/metrics?fields=displayName,unit,aggregationTypes&pageSize=500' \



-H 'Authorization: Api-Token dt0c01.abc123.abcdefjhij1234567890' \



-H 'Accept: application/json'
```

### CSV table payload

```
curl -L -X GET 'https://mySampleEnv.live.dynatrace.com/api/v2/metrics?fields=displayName,unit,aggregationTypes&pageSize=500' \



-H 'Authorization: Api-Token dt0c01.abc123.abcdefjhij1234567890' \



-H 'Accept: text/csv; header=present'
```

## Request URL

```
https://mySampleEnv.live.dynatrace.com/api/v2/metrics?fields=displayName,unit,aggregationTypes&pageSize=500
```

## Response

The full list of metrics is too lengthy, so in each case it is truncated to the same 3 entries.

### JSON payload

```
{



"totalCount": 1812,



"nextPageKey": null,



"metrics": [



{



"metricId": "builtin:apps.other.apdex.osAndVersion",



"displayName": "Apdex (by os and app version)",



"unit": "NotApplicable",



"aggregationTypes": [



"auto",



"value"



]



},



{



"metricId": "builtin:apps.other.keyUserActions.requestErrorCount.os",



"displayName": "Request error count (by os)",



"unit": "Count",



"aggregationTypes": [



"auto",



"value"



]



},



{



"metricId": "builtin:tech.activemq.CurrentConnectionsCount",



"displayName": "Current connections count",



"unit": "Count",



"aggregationTypes": [



"auto",



"avg",



"count",



"max",



"min",



"sum"



]



}



]



}
```

### CSV table payload

```
metricId,displayName,unit,aggregationTypes



builtin:apps.other.apdex.osAndVersion,Apdex (by os and app version),NotApplicable,"[auto, value]"



builtin:apps.other.keyUserActions.requestErrorCount.os,Request error count (by os),Count,"[auto, value]"



builtin:tech.activemq.CurrentConnectionsCount,Current connections count,Count,"[auto, avg, count, max, min, sum]"
```