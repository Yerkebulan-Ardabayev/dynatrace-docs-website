---
title: "Export license data"
source: https://docs.dynatrace.com/managed/managed-cluster/api-references/cluster-api/cluster-api-v2/export-license-data/get-export-license-data
updated: 2026-02-09
---

# Export license data

# Export license data

* Updated on Nov 25, 2025

This API call exports aggregated hourly license usage of all your environments as a ZIP file.

This API is only compatible with [Dynatrace classic licensing](/managed/license/monitoring-consumption-classic "Understand how Dynatrace monitoring consumption is calculated for classic licensing.") and does not contain billed usage.

## Authentication

To execute this request, you need the **Service Provider API** (`ServiceProviderAPI`) permission assigned to your API token. Generate your API token via Cluster Management Console (CMC). To learn how to obtain and use it, see [Cluster API - Authentication](/managed/managed-cluster/api-references/cluster-api/basics/cluster-api-authentication "How to get authenticated to use the Dynatrace Cluster API.").

The request produces an `application/octet-stream` payload.

## Endpoint

`/api/cluster/v2/license/consumption`

## Response format

The request produces an `application/octet-stream` payload.

## Response

### Response codes

| Code | Type | Description |
| --- | --- | --- |
| **200** | string | OK - license usage data export will start |
| **400** | - | Bad request. Provided time range is incorrect. |
| **422** | - | Incompatible licensing model. |
| **429** | - | License usage data is already being exported. Please wait for the first request to finish before requesting another export. |
| **500** | - | Operation failed |

### Response body objects

#### The `ResponseBody` object

## Example

In this example, you request license data from Dynatrace Managed in a range starting from March 19, 2020 6:00 (1584594000000) to June 9th, 2020 17:00 (1591714800000).

#### Curl

```
curl -X GET "https://myManaged.cluster.com/api/cluster/v2/license/consumption?startTs=1584594000000&endTs=1591714800000"



-H  "accept: application/octet-stream"
```

#### Request URL

```
https://myManaged.cluster.com/api/cluster/v2/license/consumption?startTs=1584594000000&endTs=1591714800000
```

#### Response body

ZIP file containing license data files in JSON format. For details on the JSON format, see [Export license data](/managed/managed-cluster/operation/export-license-data "Learn how to export license data from the Cluster Management Console.").

#### Response code

`200`
