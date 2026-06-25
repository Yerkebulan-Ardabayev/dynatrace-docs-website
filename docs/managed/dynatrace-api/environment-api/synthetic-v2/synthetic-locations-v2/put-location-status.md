---
title: Synthetic locations API v2 - PUT public locations status
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/synthetic-v2/synthetic-locations-v2/put-location-status
scraped: 2026-05-12T11:59:17.283607
---

# Synthetic locations API v2 - PUT public locations status

# Synthetic locations API v2 - PUT public locations status

* Reference
* Published Jan 21, 2021

Changes the status of public synthetic locations.

The request consumes an `application/json` payload.

|  |  |  |
| --- | --- | --- |
| PUT | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/v2/synthetic/locations/status` |
| PUT | Environment and Cluster ActiveGate (default port 9999) | `https://{your-activegate-domain}:9999/e/{your-environment-id}/api/v2/synthetic/locations/status` |

## Authentication

To execute this request, you need an access token with `syntheticLocations.write` scope.

To learn how to obtain and use it, see [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Parameters

| Parameter | Type | Description | In | Required |
| --- | --- | --- | --- | --- |
| body | [SyntheticPublicLocationsStatus](#openapi-definition-SyntheticPublicLocationsStatus) | The new status of public synthetic locations. | body | Required |

### Request body objects

#### The `SyntheticPublicLocationsStatus` object

The status of public synthetic locations.

| Element | Type | Description | Required |
| --- | --- | --- | --- |
| publicLocationsEnabled | boolean | Synthetic monitors can (`true`) or can't (`false`) run on public synthetic locations. | Required |

### Request body JSON model

This is a model of the request body, showing the possible elements. It has to be adjusted for usage in an actual request.

```
{



"publicLocationsEnabled": true



}
```

## Response

### Response codes

| Code | Type | Description |
| --- | --- | --- |
| **204** | - | Success. Locations status has been updated. |
| **409** | - | Conflict. Public locations couldn't be disabled because there are monitors assigned to them. |
| **4XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Client side error. |
| **5XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Server side error. |

### Response body objects

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

## Related topics

* [Synthetic Monitoring](/managed/observe/digital-experience/synthetic-monitoring "Learn about Synthetic Monitoring and how to create a single-URL browser monitor, a browser clickpath, or an HTTP monitor.")