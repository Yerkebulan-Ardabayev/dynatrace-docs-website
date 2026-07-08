---
title: Synthetic monitors API v2 - GET all Synthetic monitors
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/synthetic-v2/synthetic-network-availability-monitors/get-all-monitors
---

# Synthetic monitors API v2 - GET all Synthetic monitors

# Synthetic monitors API v2 - GET all Synthetic monitors

* Reference
* Updated on May 05, 2026

Lists all Synthetic monitors in your environment.

The method is available only for browser and NAM monitors.

The request produces an `application/json` payload.

|  |  |  |
| --- | --- | --- |
| GET | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/v2/synthetic/monitors` |
| GET | Environment and Cluster ActiveGate (default port 9999) | `https://{your-activegate-domain}:9999/e/{your-environment-id}/api/v2/synthetic/monitors` |

## Authentication

To execute this request, you need an access token with `settings.read` scope.

To learn how to obtain and use it, see [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Parameters

| Parameter | Type | Description | In | Required |
| --- | --- | --- | --- | --- |
| monitorSelector | string | Defines the scope of the query. Only monitors matching the specified criteria are included into response.  You can add one or several of the criteria listed below. For each criterion you can specify multiple comma-separated values, unless stated otherwise. If several values are specified, the **OR** logic applies.  * Monitor type: `type(HTTP,MULTI_PROTOCOL)`. Possible values: 'HTTP', 'BROWSER', 'THIRD\_PARTY', 'MULTI\_PROTOCOL' (Note that only 'BROWSER' and 'MULTI\_PROTOCOL' are currently supported). * Management zone ID: `managementZoneId(1, 2)`. * Synthetic Location ME ID: `location(SYNTHETIC_LOCATION-123)`. * Monitored host ME ID: `monitoredEntity(HOST-123)`. * Monitor tags: `tag([context]key:value,key:value,key)`. Tags in `[context]key:value`, `key:value`, and `key` formats are detected and parsed automatically. If a key-only tag has a colon (`:`) in it, you must escape the colon with a backslash(`\`). Otherwise, the tag will be parsed as a `key:value tag`. All tag values are case-sensitive. * Monitor enablement: `enabled(true)`.  To set several criteria, separate them with a comma (`,`). Only results matching **all** criteria are included in the response. | query | Optional |

## Response

### Response codes

| Code | Type | Description |
| --- | --- | --- |
| **200** | [SyntheticMonitorListDto](#openapi-definition-SyntheticMonitorListDto) | Success |
| **4XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Client side error. |
| **5XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Server side error. |

### Response body objects

#### The `SyntheticMonitorListDto` object

List of available synthetic monitors.

| Element | Type | Description |
| --- | --- | --- |
| monitors | [SyntheticMonitorSummaryDto](#openapi-definition-SyntheticMonitorSummaryDto)[] | List of monitors. |

#### The `SyntheticMonitorSummaryDto` object

Basic monitor data.

| Element | Type | Description |
| --- | --- | --- |
| enabled | boolean | If true, the monitor is enabled. |
| entityId | string | The entity id of the monitor. |
| name | string | The name of the monitor. |
| type | string | -The element can hold these values * `BROWSER` * `HTTP` * `MULTI_PROTOCOL` * `THIRD_PARTY` |

#### The `ErrorEnvelope` object

| Element | Type | Description |
| --- | --- | --- |
| error | [Error](#openapi-definition-Error) | - |

#### The `Error` object

| Element | Type | Description |
| --- | --- | --- |
| code | integer | The HTTP status code |
| constraintViolations | [ConstraintViolation](#openapi-definition-ConstraintViolation)[] | A list of constraint violations |
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



"monitors": [



{



"enabled": "true",



"entityId": "MULTIPROTOCOL_MONITOR-63653CB579F573D1",



"name": "My network availability monitor",



"type": "MULTI_PROTOCOL"



},



{



"enabled": "false",



"entityId": "MULTIPROTOCOL_MONITOR-63653CB579F573D2",



"name": "Disabled network availability monitor",



"type": "MULTI_PROTOCOL"



}



]



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

## Related topics

* [Synthetic Monitoring](/managed/observe/digital-experience/synthetic-monitoring "Learn about Synthetic Monitoring and how to create a single-URL browser monitor, a browser clickpath, or an HTTP monitor.")