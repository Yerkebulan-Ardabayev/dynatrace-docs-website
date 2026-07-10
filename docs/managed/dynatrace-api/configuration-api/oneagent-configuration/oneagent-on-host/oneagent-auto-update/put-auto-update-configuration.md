---
title: OneAgent auto-update API - PUT configuration
source: https://docs.dynatrace.com/managed/dynatrace-api/configuration-api/oneagent-configuration/oneagent-on-host/oneagent-auto-update/put-auto-update-configuration
---

# OneAgent auto-update API - PUT configuration

# OneAgent auto-update API - PUT configuration

* Reference
* Published Feb 03, 2020

Updates the configuration of OneAgent auto-update on the specified host.

The request consumes an `application/json` payload.

|  |  |  |
| --- | --- | --- |
| PUT | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/config/v1/hosts/{id}/autoupdate` |
| PUT | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/config/v1/hosts/{id}/autoupdate` |

## Authentication

To execute this request, you need an access token with `WriteConfig` scope.

To learn how to obtain and use it, see [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Parameters

| Parameter | Type | Description | In | Required |
| --- | --- | --- | --- | --- |
| id | string | The Dynatrace entity ID of the required host. | path | Required |
| body | [HostAutoUpdateConfig](#openapi-definition-HostAutoUpdateConfig) | The JSON body of the request. Contains OneAgent auto-update parameters. | body | Optional |

### Request body objects

#### The `HostAutoUpdateConfig` object

Configuration of OneAgent auto-update.

| Element | Type | Description | Required |
| --- | --- | --- | --- |
| effectiveSetting | string | The actual state of the auto-update on the host.  Applicable only if the **setting** parameter is set to `INHERITED`. In that case the value is taken from the host group or the environment-wide configuration. The element can hold these values * `ENABLED` * `DISABLED` | Optional |
| effectiveVersion | string | The actual version to which the OneAgent must be updated.  Applicable only if the **setting** parameter is set to `INHERITED` and the **version** parameter is set to `null`. In that case the value is taken from the host group or the environment-wide configuration. | Optional |
| id | string | The Dynatrace entity ID of the host where OneAgent is deployed. | Optional |
| metadata | [ConfigurationMetadata](#openapi-definition-ConfigurationMetadata) | Metadata useful for debugging | Optional |
| setting | string | The auto-update state of OneAgents on the host:  * `ENABLED`: OneAgent automatically updates to the most recent version. * `DISABLED`: OneAgent updates to the version specified in the **version** field. * `INHERITED`: The setting from the host group (if the host is a member of a host group) or the environment-wide configuration (if the host doesn't belong to a host group) is used. The element can hold these values * `DISABLED` * `ENABLED` * `INHERITED` | Required |
| targetVersion | string | Version to update a OneAgent to when automatic updates are enabled.  Supports relative versions `latest`, `previous` and `older` as well as specific version in `<major>.<minor>` format (for example `1.261`) or `<major>.<minor>.<revision>.<timestamp>` format (for example `1.261.178.20230313-090930`).  Only applicable when the **setting** parameter is set to `ENABLED`. | Optional |
| updateWindows | [UpdateWindowsConfig](#openapi-definition-UpdateWindowsConfig) | Basic information about all configured update windows | Optional |
| version | string | The version to which the OneAgent must be updated.  Specify the version in the `<major>.<minor>.<revision>.<timestamp>` format (for example `1.191.0.20200326-161115`). You can fetch the list of available versions with the [GET available versions﻿](https://dt-url.net/fo23rb5?dt=m) call.  If no suitable installer is found for the provided version or the value is set to `null`, OneAgent won't be updated.  Only applicable when the **effectiveSetting** value is `DISABLED`.  If the **setting** parameter is set to `INHERITED` but the **version** is still set, it will result in a one-time update: OneAgent will be updated to the specified version and the **version** value will be set to `null`. For further updates the parent setting will be used. | Optional |

#### The `ConfigurationMetadata` object

Metadata useful for debugging

| Element | Type | Description | Required |
| --- | --- | --- | --- |
| clusterVersion | string | Dynatrace version. | Optional |
| configurationVersions | integer[] | A sorted list of the version numbers of the configuration. | Optional |
| currentConfigurationVersions | string[] | A sorted list of version numbers of the configuration. | Optional |

#### The `UpdateWindowsConfig` object

Basic information about all configured update windows

| Element | Type | Description | Required |
| --- | --- | --- | --- |
| windows | [UpdateWindow](#openapi-definition-UpdateWindow)[] | List of update windows when the OneAgent update can start. If there is no value and update should be performed, the update will start at earliest convenience. | Required |

#### The `UpdateWindow` object

Basic information about one maintenance window

| Element | Type | Description | Required |
| --- | --- | --- | --- |
| id | string | Identifier of maintenance window | Required |
| name | string | The name of maintenance window | Optional |

### Request body JSON model

This is a model of the request body, showing the possible elements. It has to be adjusted for usage in an actual request.

```
{



"effectiveSetting": "DISABLED",



"effectiveVersion": "1.191.0.20200326-161115",



"id": "HOST-0123456789ABCDE",



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



"setting": "DISABLED",



"targetVersion": "latest",



"updateWindows": {



"windows": [



{



"id": "vu9U3hXa3q0AAAABADdkeW5hdHJhY2Uuc2V0dGluZ3MuZGVwbG95bWVudC5tYW5h",



"name": "Daily maintenance window"



}



]



},



"version": "1.191.0.20200326-161115"



}
```

## Response

### Response codes

| Code | Type | Description |
| --- | --- | --- |
| **204** | - | Success. The configuration has been updated. Response doesn't have a body. |
| **400** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Failed. The input is invalid |

### Response body objects

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

## Validate payload

We recommend that you validate the payload before submitting it with an actual request. A response code of **204** indicates a valid payload.

The request consumes an `application/json` payload.

|  |  |  |
| --- | --- | --- |
| POST | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/config/v1/hosts/{id}/autoupdate/validator` |
| POST | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/config/v1/hosts/{id}/autoupdate/validator` |

### Authentication

To execute this request, you need an access token with `WriteConfig` scope.

To learn how to obtain and use it, see [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

### Response

#### Response codes

| Code | Type | Description |
| --- | --- | --- |
| **204** | - | Validated. The submitted configuration is valid. Response doesn't have a body. |
| **400** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Failed. The input is invalid |

#### Response body objects

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

#### Response body JSON models

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