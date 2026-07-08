---
title: Deployment API - GET checksum of a BOSH tarball
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/deployment/bosh/get-bosh-checksum
---

# Deployment API - GET checksum of a BOSH tarball

# Deployment API - GET checksum of a BOSH tarball

* Reference
* Published Aug 28, 2019

Gets the checksum of the specified BOSH release tarball. The checksum is the SHA-256 hash of the installer file.

The request produces an `application/json` payload.

|  |  |  |
| --- | --- | --- |
| GET | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/v1/deployment/boshrelease/agent/{osType}/version/{version}/checksum` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/v1/deployment/boshrelease/agent/{osType}/version/{version}/checksum` |

## Authentication

To execute this request, you need an access token with `InstallerDownload` scope.

To learn how to obtain and use it, see [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Parameters

| Parameter | Type | Description | In | Required |
| --- | --- | --- | --- | --- |
| osType | string | The operating system of the installer. The element can hold these values * `windows` * `unix` | path | Required |
| version | string | The required version of the OneAgent in the `1.155.275.20181112-084458` format.  You can retrieve the list of available versions with the [**GET available versions of BOSH tarballs**﻿](https://dt-url.net/j703kdn) call. | path | Required |
| skipMetadata | boolean | Set `true` to omit the OneAgent connectivity information from the installer.  If not set, `false` is used. | query | Optional |
| networkZone | string | The network zone you want the result to be configured with. | query | Optional |

## Response

### Response codes

| Code | Type | Description |
| --- | --- | --- |
| **200** | [BoshReleaseChecksum](#openapi-definition-BoshReleaseChecksum) | Success |
| **4XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Client side error. |
| **5XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Server side error. |

### Response body objects

#### The `BoshReleaseChecksum` object

The checksum of the BOSH release tarball.

| Element | Type | Description |
| --- | --- | --- |
| sha256 | string | The checksum of the BOSH release tarball.  This is the sha256 hash of the installer file. |

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



"sha256": "string"



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