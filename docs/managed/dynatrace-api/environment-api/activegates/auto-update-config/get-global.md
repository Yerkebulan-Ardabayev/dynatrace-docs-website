---
title: ActiveGate auto-update configuration API - GET global
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/activegates/auto-update-config/get-global
---

# ActiveGate auto-update configuration API - GET global

# ActiveGate auto-update configuration API - GET global

* Reference
* Published Mar 15, 2021

Gets the global auto-update configuration of Environment ActiveGates.

The request produces an `application/json` payload.

|  |  |  |
| --- | --- | --- |
| GET | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/v2/activeGates/autoUpdate` |
| GET | Environment and Cluster ActiveGate (default port 9999) | `https://{your-activegate-domain}:9999/e/{your-environment-id}/api/v2/activeGates/autoUpdate` |

## Authentication

To execute this request, you need an access token with `activeGates.read` scope.

To learn how to obtain and use it, see [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Parameters

The request doesn't provide any configurable parameters.

## Response

### Response codes

| Code | Type | Description |
| --- | --- | --- |
| **200** | [ActiveGateGlobalAutoUpdateConfig](#openapi-definition-ActiveGateGlobalAutoUpdateConfig) | Success |
| **4XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Client side error. |
| **5XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Server side error. |

### Response body objects

#### The `ActiveGateGlobalAutoUpdateConfig` object

Global configuration of ActiveGates auto-update.

| Element | Type | Description |
| --- | --- | --- |
| globalSetting | string | The state of auto-updates for all ActiveGates connected to the environment or Managed cluster.  This setting is inherited by all ActiveGates that have the `INHERITED` setting. The element can hold these values * `ENABLED` * `DISABLED` |
| metadata | [ConfigurationMetadata](#openapi-definition-ConfigurationMetadata) | Metadata useful for debugging |
| targetVersion | string | Version to update a ActiveGate to when automatic updates are enabled.  Supports relative versions `latest`, `previous` and `older` as well as specific version in `<major>.<minor>` format (for example `1.261`).  Only applicable when the **setting** parameter is set to `ENABLED`. |
| updateWindows | [UpdateWindowsConfig](#openapi-definition-UpdateWindowsConfig) | Basic information about all configured update windows |

#### The `ConfigurationMetadata` object

Metadata useful for debugging

| Element | Type | Description |
| --- | --- | --- |
| clusterVersion | string | Dynatrace version. |
| configurationVersions | integer[] | A sorted list of the version numbers of the configuration. |
| currentConfigurationVersions | string[] | A sorted list of version numbers of the configuration. |

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



"globalSetting": "ENABLED",



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