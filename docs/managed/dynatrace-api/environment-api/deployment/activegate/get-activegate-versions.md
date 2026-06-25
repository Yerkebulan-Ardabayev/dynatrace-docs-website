---
title: Deployment API - GET available versions of ActiveGate
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/deployment/activegate/get-activegate-versions
scraped: 2026-05-12T11:56:48.102976
---

# Deployment API - GET available versions of ActiveGate

# Deployment API - GET available versions of ActiveGate

* Reference
* Published Jul 02, 2020

Lists all available versions of the ActiveGate installer.

The request produces an `application/json` payload.

|  |  |  |
| --- | --- | --- |
| GET | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/v1/deployment/installer/gateway/versions/{osType}` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/v1/deployment/installer/gateway/versions/{osType}` |

## Authentication

To execute this request, you need an access token with `InstallerDownload` scope.

To learn how to obtain and use it, see [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Parameters

| Parameter | Type | Description | In | Required |
| --- | --- | --- | --- | --- |
| osType | string | The operating system of the installer. The element can hold these values * `windows` * `unix` | path | Required |
| arch | string | The architecture of your OS:  * `all`: Defaults to `amd64`. * `amd64`: amd64 architecture. * `s390`: S/390 architecture, only supported for Linux. * `arm64`: arm64 architecture, only supported for Linux. The element can hold these values * `all` * `amd64` * `arm64` * `s390` | query | Optional |

## Response

### Response codes

| Code | Type | Description |
| --- | --- | --- |
| **200** | [ActiveGateInstallerVersions](#openapi-definition-ActiveGateInstallerVersions) | Success. The payload contains the available versions. |
| **404** | - | Not found. See the response body for details. |
| **4XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Client side error. |
| **5XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Server side error. |

### Response body objects

#### The `ActiveGateInstallerVersions` object

A list of available versions of ActiveGate installer.

| Element | Type | Description |
| --- | --- | --- |
| availableVersions | string[] | Available versions. |

### Response body JSON models

```
{



"availableVersions": [



"string"



]



}
```