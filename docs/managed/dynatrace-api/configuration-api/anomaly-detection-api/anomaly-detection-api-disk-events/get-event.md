---
title: Disk events anomaly detection API - GET an event
source: https://docs.dynatrace.com/managed/dynatrace-api/configuration-api/anomaly-detection-api/anomaly-detection-api-disk-events/get-event
scraped: 2026-05-12T11:20:23.825410
---

# Disk events anomaly detection API - GET an event

# Disk events anomaly detection API - GET an event

* Reference
* Published Aug 29, 2019

Gets the parameters of the specified disk event rule.

The request produces an `application/json` payload.

|  |  |  |
| --- | --- | --- |
| GET | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/config/v1/anomalyDetection/diskEvents/{id}` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/config/v1/anomalyDetection/diskEvents/{id}` |

## Authentication

To execute this request, you need an access token with `ReadConfig` scope.

To learn how to obtain and use it, see [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Parameters

| Parameter | Type | Description | In | Required |
| --- | --- | --- | --- | --- |
| id | string | The ID of the required disk event rule. | path | Required |

## Response

### Response codes

| Code | Type | Description |
| --- | --- | --- |
| **200** | [DiskEventAnomalyDetectionConfig](#openapi-definition-DiskEventAnomalyDetectionConfig) | Success |

### Response body objects

#### The `DiskEventAnomalyDetectionConfig` object

| Element | Type | Description |
| --- | --- | --- |
| diskNameFilter | [DiskNameFilter](#openapi-definition-DiskNameFilter) | Narrows the rule usage down to disks, matching the specified criteria. |
| enabled | boolean | Disk event rule enabled/disabled. |
| hostGroupId | string | Narrows the rule usage down to disks that run on hosts that themselves run on the specified host group. |
| id | string | The ID of the disk event rule. |
| metadata | [ConfigurationMetadata](#openapi-definition-ConfigurationMetadata) | Metadata useful for debugging |
| metric | string | The metric to monitor. The element can hold these values * `LOW_DISK_SPACE` * `LOW_INODES` * `READ_TIME_EXCEEDING` * `WRITE_TIME_EXCEEDING` |
| name | string | The name of the disk event rule. |
| samples | integer | The number of samples to evaluate. |
| tagFilters | [TagFilter[]](#openapi-definition-TagFilter) | Narrows the rule usage down to the hosts matching the specified tags. |
| threshold | number | The threshold to trigger disk event.  * A percentage for `LowDiskSpace` or `LowInodes` metrics. * In milliseconds for `ReadTimeExceeding` or `WriteTimeExceeding` metrics. |
| violatingSamples | integer | The number of samples that must violate the threshold to trigger an event. Must not exceed the number of evaluated samples. |

#### The `DiskNameFilter` object

Narrows the rule usage down to disks, matching the specified criteria.

| Element | Type | Description |
| --- | --- | --- |
| operator | string | Comparison operator. The element can hold these values * `CONTAINS` * `DOES_NOT_CONTAIN` * `DOES_NOT_EQUAL` * `DOES_NOT_START_WITH` * `EQUALS` * `STARTS_WITH` |
| value | string | Value to compare to. |

#### The `ConfigurationMetadata` object

Metadata useful for debugging

| Element | Type | Description |
| --- | --- | --- |
| clusterVersion | string | Dynatrace version. |
| configurationVersions | integer[] | A sorted list of the version numbers of the configuration. |
| currentConfigurationVersions | string[] | A sorted list of version numbers of the configuration. |

#### The `TagFilter` object

A tag-based filter of monitored entities.

| Element | Type | Description |
| --- | --- | --- |
| context | string | The origin of the tag, such as AWS or Cloud Foundry.  Custom tags use the `CONTEXTLESS` value. The element can hold these values * `AWS` * `AWS_GENERIC` * `AZURE` * `CLOUD_FOUNDRY` * `CONTEXTLESS` * `ENVIRONMENT` * `GOOGLE_CLOUD` * `KUBERNETES` |
| key | string | The key of the tag.  Custom tags have the tag value here. |
| value | string | The value of the tag.  Not applicable to custom tags. |

### Response body JSON models

```
{



"diskNameFilter": {



"operator": "CONTAINS",



"value": "string"



},



"enabled": true,



"hostGroupId": "string",



"id": "string",



"metadata": {



"clusterVersion": "1.192.1",



"configurationVersions": [



4,



2



],



"currentConfigurationVersions": [



"1.0.4",



"1.23"



]



},



"metric": "LOW_DISK_SPACE",



"name": "string",



"samples": 10,



"tagFilters": [



{



"context": "AWS",



"key": "string",



"value": "string"



}



],



"threshold": 1,



"violatingSamples": 8



}
```

## Example

In this example, the request lists the parameters of the **low disk** custom disk event rule.

The API token is passed in the **Authorization** header.

The rule has the following parameters:

![Custom disk events rule](https://dt-cdn.net/images/disk-events-rule-1324-e32280d1ac.png)

Custom disk events rule

#### Curl

```
curl -X GET \



https://mySampleEnv.live.dynatrace.com/api/config/v1/anomalyDetection/diskEvents/3f7b8234-95dc-44d0-9c1b-a5f0e8e19fd0 \



-H 'Authorization: Api-Token dt0c01.abc123.abcdefjhij1234567890'
```

#### Request URL

```
https://mySampleEnv.live.dynatrace.com/api/config/v1/anomalyDetection/diskEvents/3f7b8234-95dc-44d0-9c1b-a5f0e8e19fd0
```

#### Response body

```
{



"metadata": {



"clusterVersion": "1.164.0.20190206-143829",



"configurationVersions": [



2



]



},



"id": "3f7b8234-95dc-44d0-9c1b-a5f0e8e19fd0",



"name": "low disk",



"enabled": true,



"metric": "LOW_DISK_SPACE",



"threshold": 2,



"samples": 5,



"violatingSamples": 3,



"diskNameFilter": null,



"tagFilters": []



}
```

#### Response code

200

## Related topics

* [DavisÂ® AI](/managed/dynatrace-intelligence "Get familiar with the capabilities of Davis AI.")