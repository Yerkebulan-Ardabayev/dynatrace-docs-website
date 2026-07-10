---
title: ActiveGate auto-update configuration API - GET an ActiveGate
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/activegates/auto-update-config/get-instance
---

# ActiveGate auto-update configuration API - GET an ActiveGate

# ActiveGate auto-update configuration API - GET an ActiveGate

* Reference
* Published Mar 15, 2021

Gets the auto-update configuration of the specified Environment ActiveGate.

The request produces an `application/json` payload.

|  |  |  |
| --- | --- | --- |
| GET | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/v2/activeGates/{agId}/autoUpdate` |
| GET | Environment and Cluster ActiveGate (default port 9999) | `https://{your-activegate-domain}:9999/e/{your-environment-id}/api/v2/activeGates/{agId}/autoUpdate` |

## Authentication

To execute this request, you need an access token with `activeGates.read` scope.

To learn how to obtain and use it, see [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Parameters

| Parameter | Type | Description | In | Required |
| --- | --- | --- | --- | --- |
| agId | string | The ID of the required ActiveGate. | path | Required |

## Response

### Response codes

| Code | Type | Description |
| --- | --- | --- |
| **200** | [ActiveGateAutoUpdateConfig](#openapi-definition-ActiveGateAutoUpdateConfig) | Success |
| **404** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Not found. See response body for details. |
| **4XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Client side error. |
| **5XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Server side error. |

### Response body objects

#### The `ActiveGateAutoUpdateConfig` object

Configuration of the ActiveGate auto-updates.

| Element | Type | Description |
| --- | --- | --- |
| effectiveSetting | string | The actual state of the ActiveGate auto-update.  Applicable only if the **setting** parameter is set to `INHERITED`. In that case, the value is taken from the parent setting. Otherwise, it's just a duplicate of the **setting** value. The element can hold these values * `ENABLED` * `DISABLED` |
| setting | string | The state of the ActiveGate auto-update: enabled, disabled, or inherited.  If set to `INHERITED`, the setting is inherited from the global configuration set on the environment or Managed cluster level. The element can hold these values * `DISABLED` * `ENABLED` * `INHERITED` |
| targetVersion | string | The target version of the ActiveGate.  Specify the version in the `<major>.<minor>` format (for example `1.342`) or `latest`, `previous`, or `older`. |
| updateWindows | [UpdateWindowsConfig](#openapi-definition-UpdateWindowsConfig) | Basic information about all configured update windows |

#### The `UpdateWindowsConfig` object

Basic information about all configured update windows

| Element | Type | Description |
| --- | --- | --- |
| windows | [UpdateWindow](#openapi-definition-UpdateWindow)[] | List of update windows when the OneAgent update can start. If there is no value and update should be performed, the update will start at earliest convenience. |

#### The `UpdateWindow` object

Basic information about one maintenance window

| Element | Type | Description |
| --- | --- | --- |
| id | string | Identifier of maintenance window |
| name | string | The name of maintenance window |

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



"effectiveSetting": "ENABLED",



"setting": "INHERITED",



"targetVersion": "latest",



"updateWindows": {



"windows": [



{



"id": "vu9U3hXa3q0AAAABADdkeW5hdHJhY2Uuc2V0dGluZ3MuZGVwbG95bWVudC5tYW5h",



"name": "Daily maintenance window"



}



]



}



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

* [Dynatrace ActiveGate](/managed/ingest-from/dynatrace-activegate "Understand the basic concepts related to ActiveGate.")