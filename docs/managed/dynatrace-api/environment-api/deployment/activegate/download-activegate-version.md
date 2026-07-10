---
title: Deployment API - Download ActiveGate of specific version
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/deployment/activegate/download-activegate-version
---

# Deployment API - Download ActiveGate of specific version

# Deployment API - Download ActiveGate of specific version

* Reference
* Updated on Jun 23, 2026

Downloads the ActiveGate installer of the specified version. You can fetch the list of available ActiveGate versions with the [GET available versions of ActiveGate](/managed/dynatrace-api/environment-api/deployment/activegate/get-activegate-versions "List available versions of ActiveGate via Dynatrace API.") call.

In Dynatrace Managed version 1.344+, when a version is set as an ActiveGate **target version** in [ActiveGate auto-update configuration](/managed/dynatrace-api/environment-api/activegates/auto-update-config "Manage auto-update configuration of your Environment ActiveGates via the Dynatrace API."), the cluster preserves its installer (build-unit protection). The installer therefore remains downloadable through this endpoint even after older builds of the same main version are pruned during normal cluster maintenance.

|  |  |  |
| --- | --- | --- |
| GET | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/v1/deployment/installer/gateway/{osType}/version/{version}` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/v1/deployment/installer/gateway/{osType}/version/{version}` |

## Authentication

To execute this request, you need an access token with `InstallerDownload` scope.

To learn how to obtain and use it, see [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Parameters

| Parameter | Type | Description | In | Required |
| --- | --- | --- | --- | --- |
| If-None-Match | string | The ETag of the previous request. Do not download if it matches the ETag of the installer. | header | Optional |
| osType | string | The operating system of the installer. The element can hold these values * `windows` * `unix` | path | Required |
| version | string | The required version of the ActiveGate installer, in `1.155.275.20181112-084458` format.  You can retrieve the list of available versions with the [**GET available versions of ActiveGate**﻿](https://dt-url.net/kh43rha?dt=m) call. | path | Required |
| networkZone | string | The network zone you want the result to be configured with. Provided network zone must exist, otherwise the request will fail. Requires at least ActiveGate version 1.247. | query | Optional |
| arch | string | The architecture of your OS:  * `all`: Defaults to `amd64`. * `amd64`: amd64 architecture. * `s390`: S/390 architecture, only supported for Linux. * `arm64`: arm64 architecture, only supported for Linux. The element can hold these values * `all` * `amd64` * `arm64` * `s390` | query | Optional |

## Response

### Response codes

| Code | Type | Description |
| --- | --- | --- |
| **200** | string | Success. The payload contains the installer file. |
| **304** | - | Not modified. You already have the latest version of the installer. The response does not contain a payload. |
| **4XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Client side error. |
| **5XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Server side error. |

### Response body objects

#### The `ResponseBody` object

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