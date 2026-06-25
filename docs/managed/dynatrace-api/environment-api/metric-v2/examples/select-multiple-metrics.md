---
title: Metrics API examples - Select multiple metrics
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/metric-v2/examples/select-multiple-metrics
scraped: 2026-05-12T12:10:04.516117
---

# Metrics API examples - Select multiple metrics

# Metrics API examples - Select multiple metrics

* Reference
* Published Jun 16, 2020

The [GET metrics](/managed/dynatrace-api/environment-api/metric-v2/get-all-metrics "List all metrics available in your monitoring environment via Metrics v2 API.") endpoint provides you the ability to query multiple metrics, along with partial or even full descriptors of metrics.

This example shows how to fetch the descriptors of several metrics of one parent:

* CPU idle (`builtin:host.cpu.idle`)
* System load (`builtin:host.cpu.load`)
* CPU usage % (`builtin:host.cpu.usage`)

For each, we'll query the full descriptors:

* Metric key
* Display name
* Description
* Units
* Supported entity types
* Supported aggregations
* Default aggregation
* Supported transformations
* Dimensions

## Configure the request

We have to set the following query parameters:

* **metricSelector** to `builtin:host.cpu.(idle,usage,load)`
* **fields** to `displayName,description,unit,entityType,aggregationTypes,transformations,defaultAggregation,dimensionDefinitions`. Note that `metricId` is omitted here, because it is always presented in the response.

You can get the response in two formats:

* JSON: set the **Accept** header of the request to `application/json`.
* CSV table: set the **Accept** header of the request to `text/csv; header=present`. If you're not interested in the header row, use `text/csv; header=absent`.

To authenticate the request, set the **Authorization** header of the request to `Api-token {your-token}`. The token must have the **Read metrics** (`metrics.read`) permission.

## Curl

Here's the Curl code of the request. Be sure to use the URL of your own environment and a real API token.

### JSON payload

```
curl -L -X GET 'https://mySampleEnv.live.dynatrace.com/api/v2/metrics?fields=displayName,description,unit,entityType,aggregationTypes,transformations,defaultAggregation,dimensionDefinitions&metricSelector=builtin:host.cpu.(idle,usage,load)' \



-H 'Authorization: Api-Token dt0c01.abc123.abcdefjhij1234567890' \



-H 'Accept: application/json'
```

### CSV table payload

```
curl -L -X GET 'https://mySampleEnv.live.dynatrace.com/api/v2/metrics?fields=displayName,description,unit,entityType,aggregationTypes,transformations,defaultAggregation,dimensionDefinitions&metricSelector=builtin:host.cpu.(idle,usage,load)' \



-H 'Authorization: Api-Token dt0c01.abc123.abcdefjhij1234567890' \



-H 'Accept: text/csv; header=present'
```

## Request URL

```
https://mySampleEnv.live.dynatrace.com/api/v2/metrics?fields=displayName,description,unit,entityType,aggregationTypes,transformations,defaultAggregation,dimensionDefinitions&metricSelector=builtin:host.cpu.(idle,usage,load)
```

## Response

Both examples contains full payload, nothing is truncated.

### JSON payload

```
{



"totalCount": 3,



"nextPageKey": null,



"metrics": [



{



"metricId": "builtin:host.cpu.idle",



"displayName": "CPU idle",



"description": "",



"unit": "Percent",



"entityType": [



"HOST"



],



"aggregationTypes": [



"auto",



"avg",



"max",



"min"



],



"transformations": [



"filter",



"fold",



"merge",



"names",



"parents"



],



"defaultAggregation": {



"type": "avg"



},



"dimensionDefinitions": [



{



"key": "dt.entity.host",



"name": "Host",



"index": 0,



"type": "ENTITY"



}



]



},



{



"metricId": "builtin:host.cpu.load",



"displayName": "System load",



"description": "",



"unit": "Ratio",



"entityType": [



"HOST"



],



"aggregationTypes": [



"auto",



"avg",



"max",



"min"



],



"transformations": [



"filter",



"fold",



"merge",



"names",



"parents"



],



"defaultAggregation": {



"type": "avg"



},



"dimensionDefinitions": [



{



"key": "dt.entity.host",



"name": "Host",



"index": 0,



"type": "ENTITY"



}



]



},



{



"metricId": "builtin:host.cpu.usage",



"displayName": "CPU usage %",



"description": "Percentage of CPU time currently utilized.",



"unit": "Percent",



"entityType": [



"HOST"



],



"aggregationTypes": [



"auto",



"avg",



"max",



"min"



],



"transformations": [



"filter",



"fold",



"merge",



"names",



"parents"



],



"defaultAggregation": {



"type": "avg"



},



"dimensionDefinitions": [



{



"key": "dt.entity.host",



"name": "Host",



"index": 0,



"type": "ENTITY"



}



]



}



]



}
```

### CSV table payload

```
metricId,displayName,description,unit,entityType,aggregationTypes,transformations,defaultAggregation,dimensionDefinitions



builtin:host.cpu.idle,CPU idle,,Percent,[HOST],"[auto, avg, max, min]","[filter, fold, merge, names, parents]",avg,[Host:ENTITY]



builtin:host.cpu.load,System load,,Ratio,[HOST],"[auto, avg, max, min]","[filter, fold, merge, names, parents]",avg,[Host:ENTITY]



builtin:host.cpu.usage,CPU usage %,Percentage of CPU time currently utilized.,Percent,[HOST],"[auto, avg, max, min]","[filter, fold, merge, names, parents]",avg,[Host:ENTITY]
```