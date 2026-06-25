---
title: Metrics API examples - Select full metric subtree
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/metric-v2/examples/select-subtree
scraped: 2026-05-12T12:10:08.554496
---

# Metrics API examples - Select full metric subtree

# Metrics API examples - Select full metric subtree

* Reference
* Published Jun 22, 2020

The [GET metrics](/managed/dynatrace-api/environment-api/metric-v2/get-all-metrics "List all metrics available in your monitoring environment via Metrics v2 API.") endpoint provides you the ability to select the full subtree of metrics with a trailing asterisk wildcard (`*`). The asterisk wildcard selects all the metrics of the parent without the need to specify every one of them.

This example shows how to fetch the descriptors of all host CPU metrics.

To make the response shorter, we'll query only the following parameters:

* Metric key
* Display name
* Default aggregation

Of course, you can query the full descriptors of a metric. To learn how to do that, check the [select multiple metrics](/managed/dynatrace-api/environment-api/metric-v2/examples/select-multiple-metrics "List descriptors of several related metrics via Dynatrace API.") example.

## Configure the request

We have to set the following query parameters:

* **metricSelector** to `builtin:host.cpu.*`.
* **fields** to `displayName,defaultAggregation`. Note that `metricId` is omitted here, because it is always presented in the response.

You can get the response in two formats:

* JSON: set the **Accept** header of the request to `application/json`.
* CSV table: set the **Accept** header of the request to `text/csv; header=present`. If you're not interested in the header row, use `text/csv; header=absent`.

To authenticate the request, set the **Authorization** header of the request to `Api-token {your-token}`. The token must have the **Read metrics** (`metrics.read`) permission.

## Curl

Here's the Curl code of the request. Make sure to use the URL of your own environment and a real API token.

### JSON payload

```
curl -L -X GET 'https://mySampleEnv.live.dynatrace.com/api/v2/metrics?fields=displayName,defaultAggregation&metricSelector=builtin:host.cpu.*' \



-H 'Authorization: Api-Token dt0c01.abc123.abcdefjhij1234567890' \



-H 'Accept: application/json'
```

### CSV table payload

```
curl -L -X GET 'https://mySampleEnv.live.dynatrace.com/api/v2/metrics?fields=displayName,defaultAggregation&metricSelector=builtin:host.cpu.*' \



-H 'Authorization: Api-Token dt0c01.abc123.abcdefjhij1234567890' \



-H 'Accept: text/csv; header=present'
```

## Request URL

```
https://mySampleEnv.live.dynatrace.com/api/v2/metrics?fields=displayName,defaultAggregation&metricSelector=builtin:host.cpu.*
```

## Response

Both examples contain the full payload; nothing is truncated.

### JSON payload

```
{



"totalCount": 17,



"nextPageKey": null,



"metrics": [



{



"metricId": "builtin:host.cpu.entc",



"displayName": "AIX Entitlement used",



"defaultAggregation": {



"type": "avg"



}



},



{



"metricId": "builtin:host.cpu.entConfig",



"displayName": "AIX Entitlement configured",



"defaultAggregation": {



"type": "avg"



}



},



{



"metricId": "builtin:host.cpu.idle",



"displayName": "CPU idle",



"defaultAggregation": {



"type": "avg"



}



},



{



"metricId": "builtin:host.cpu.iowait",



"displayName": "CPU I/O wait",



"defaultAggregation": {



"type": "avg"



}



},



{



"metricId": "builtin:host.cpu.load",



"displayName": "System load",



"defaultAggregation": {



"type": "avg"



}



},



{



"metricId": "builtin:host.cpu.load15m",



"displayName": "System load15m",



"defaultAggregation": {



"type": "avg"



}



},



{



"metricId": "builtin:host.cpu.load5m",



"displayName": "System load5m",



"defaultAggregation": {



"type": "avg"



}



},



{



"metricId": "builtin:host.cpu.msu.avg",



"displayName": "MSU average",



"defaultAggregation": {



"type": "avg"



}



},



{



"metricId": "builtin:host.cpu.msu.capacity",



"displayName": "MSU capacity",



"defaultAggregation": {



"type": "avg"



}



},



{



"metricId": "builtin:host.cpu.other",



"displayName": "CPU other",



"defaultAggregation": {



"type": "avg"



}



},



{



"metricId": "builtin:host.cpu.physc",



"displayName": "AIX Physical consumed",



"defaultAggregation": {



"type": "avg"



}



},



{



"metricId": "builtin:host.cpu.steal",



"displayName": "CPU steal",



"defaultAggregation": {



"type": "avg"



}



},



{



"metricId": "builtin:host.cpu.system",



"displayName": "CPU system",



"defaultAggregation": {



"type": "avg"



}



},



{



"metricId": "builtin:host.cpu.usage",



"displayName": "CPU usage %",



"defaultAggregation": {



"type": "avg"



}



},



{



"metricId": "builtin:host.cpu.user",



"displayName": "CPU user",



"defaultAggregation": {



"type": "avg"



}



},



{



"metricId": "builtin:host.cpu.ziip.eligible",



"displayName": "zIIP eligible",



"defaultAggregation": {



"type": "avg"



}



},



{



"metricId": "builtin:host.cpu.ziip.usage",



"displayName": "zIIP usage",



"defaultAggregation": {



"type": "avg"



}



}



]



}
```

### CSV table payload

```
metricId,displayName,defaultAggregation



builtin:host.cpu.entc,AIX Entitlement used,avg



builtin:host.cpu.entConfig,AIX Entitlement configured,avg



builtin:host.cpu.idle,CPU idle,avg



builtin:host.cpu.iowait,CPU I/O wait,avg



builtin:host.cpu.load,System load,avg



builtin:host.cpu.load15m,System load15m,avg



builtin:host.cpu.load5m,System load5m,avg



builtin:host.cpu.msu.avg,MSU average,avg



builtin:host.cpu.msu.capacity,MSU capacity,avg



builtin:host.cpu.other,CPU other,avg



builtin:host.cpu.physc,AIX Physical consumed,avg



builtin:host.cpu.steal,CPU steal,avg



builtin:host.cpu.system,CPU system,avg



builtin:host.cpu.usage,CPU usage %,avg



builtin:host.cpu.user,CPU user,avg



builtin:host.cpu.ziip.eligible,zIIP eligible,avg



builtin:host.cpu.ziip.usage,zIIP usage,avg
```