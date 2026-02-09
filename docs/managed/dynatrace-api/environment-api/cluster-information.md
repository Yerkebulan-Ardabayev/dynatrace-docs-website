---
title: "Cluster information API"
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/cluster-information
updated: 2026-02-09
---

# Cluster information API

# Cluster information API

* Reference
* Published Sep 24, 2018

The **Cluster information** API enables you to check the version and internal time of your Dynatrace environment.

## GET cluster time

The request produces `text/plain`.

|  |  |  |
| --- | --- | --- |
| GET | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/v1/time` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/v1/time` |

The response in cluster time in UTC milliseconds.

## GET cluster version

Dynatrace innovates fast and releases a new server(cluster) version with new features every two weeks.

We operate multiple SaaS clusters worldwide and those clusters are updated at different times. As this update process is completely transparent for our customer it is hard to exactly identify when your environment is updated to a new cluster version.

This API endpoint enables you to query the actual cluster version of your environment.

The request produces an `application/json` payload.

|  |  |  |
| --- | --- | --- |
| GET | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/v1/config/clusterversion` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/v1/config/clusterversion` |

## Authentication

To execute this request, you need an access token with `DataExport` scope.

To learn how to obtain and use it, see [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

### Response

### Response codes

| Code | Type | Description |
| --- | --- | --- |
| **200** | [ClusterVersion](#openapi-definition-ClusterVersion) | Success |
| **4XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Client side error. |
| **5XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Server side error. |

### Response body objects

#### The `ClusterVersion` object

| Element | Type | Description |
| --- | --- | --- |
| version | string | The version of the Dynatrace server. |

#### The `ErrorEnvelope` object

| Element | Type | Description |
| --- | --- | --- |
| error | [Error](#openapi-definition-Error) | - |

#### The `Error` object

| Element | Type | Description |
| --- | --- | --- |
| code | integer | The HTTP status code |
| constraintViolations | [ConstraintViolation[]](#openapi-definition-ConstraintViolation) | A list of constraint violations |
| message | string | The error message |

#### The `ConstraintViolation` object

A list of constraint violations

| Element | Type | Description |
| --- | --- | --- |
| location | string | - |
| message | string | - |
| parameterLocation | string | -The element can hold these values * `HEADER` * `PATH` * `PAYLOAD_BODY` * `QUERY` |
| path | string | - |

### Response body JSON models

```
{



"version": "string"



}
```

```
{



"error": {



"code": 1,



"constraintViolations": [



{



"location": "string",



"message": "string",



"parameterLocation": "HEADER",



"path": "string"



}



],



"message": "string"



}



}
```
