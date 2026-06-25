---
title: Get details about the current cluster maintenance state
source: https://docs.dynatrace.com/managed/dynatrace-api/cluster-api/cluster-api-v1/cluster-v1/get-cluster-maintenance
scraped: 2026-05-12T12:12:41.958990
---

# Get details about the current cluster maintenance state

# Get details about the current cluster maintenance state

* Published Sep 29, 2025

This API request gets details about the current cluster maintenance state.

## Authentication

To execute this request, you need the **Service Provider API** (`ServiceProviderAPI`) permission assigned to your API token. Generate your API token via Cluster Management Console (CMC). To learn how to obtain and use it, see [Cluster API - Tokens and authentication](/managed/dynatrace-api/cluster-api/cluster-api-authentication "How to get authenticated to use the Dynatrace Cluster API.").

## Endpoint

`/api/v1.0/cluster/maintenance`

## Parameter

The request doesn't provide any configurable parameters.

## Response

### Response codes

| Code | Type | Description |
| --- | --- | --- |
| **200** | [IPMigrationMaintenanceMode](#openapi-definition-IPMigrationMaintenanceMode) | Success |

### Response body objects

#### The `IPMigrationMaintenanceMode` object

Details for cluster maintenance triggered by the IP migration

| Element | Type | Description |
| --- | --- | --- |
| ended | [TriggeredByResponseDto](#openapi-definition-TriggeredByResponseDto) | The data about who and when the maintenance state ended. |
| jsonObjectForReasonMessage | string | - |
| metadata | [IpMigrationMetadataResponseDto](#openapi-definition-IpMigrationMetadataResponseDto) | Optional metadata |
| nodeId | integer | The node id. |
| reason | string | The reason behind the maintenance mode. The element can hold these values * `IP_MIGRATION` |
| started | [TriggeredByResponseDto](#openapi-definition-TriggeredByResponseDto) | The data about who and when the maintenance state ended. |

#### The `TriggeredByResponseDto` object

The data about who and when the maintenance state ended.

| Element | Type | Description |
| --- | --- | --- |
| date | string | Trigger date. |
| user | string | Trigger by. |

#### The `IpMigrationMetadataResponseDto` object

Optional metadata

| Element | Type | Description |
| --- | --- | --- |
| newIp | string | - |
| oldIp | string | - |

### Response body JSON models

```
{



"ended": {



"date": "2025-07-09T08:38:08.690Z",



"user": "admin"



},



"metadata": {



"newIp": "172.31.101.10",



"oldIp": "172.31.101.9"



},



"nodeId": 1,



"reason": "IP_MIGRATION",



"started": {



"date": "2025-07-08T08:38:08.690Z",



"user": "admin"



}



}
```

#### Response body

```
{



"ended": {



"date": "2025-07-09T08:38:08.690Z",



"user": "admin"



},



"metadata": {



"newIp": "172.31.101.10",



"oldIp": "172.31.101.9"



},



"nodeId": 1,



"reason": "IP_MIGRATION",



"started": {



"date": "2025-07-08T08:38:08.690Z",



"user": "admin"



}



}
```

#### Response code

200