---
title: Deployment API - Download BOSH tarballs of specific version
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/deployment/bosh/download-bosh-version
scraped: 2026-05-12T11:55:21.380072
---

# Deployment API - Download BOSH tarballs of specific version

# Deployment API - Download BOSH tarballs of specific version

* Reference
* Published Aug 28, 2019

Downloads BOSH release tarballs of the specified version, OneAgent included. You can fetch the list of available versions with the [GET available versions of BOSH tarballs](/managed/dynatrace-api/environment-api/deployment/bosh/get-available-version "List available versions of OneAgent BOSH tarballs via Dynatrace API.") call.

For SaaS, the call is executed on an Environment ActiveGate. Be sure to use the base of an ActiveGate, **not** the environment.

|  |  |
| --- | --- |
| GET | * Dynatrace Managed https://{your-domain}/e/{your-environment-id}/api/v1/deployment/boshrelease/agent/{osType}/version/{version} * Dynatrace SaaS https://{your-environment-activegate}:9999/e/{your-environment-id}/api/v1/deployment/boshrelease/agent/{osType}/version/{version} |

## Authentication

To execute this request, you need the **PaaS token** (`InstallerDownload`) of your environment. To learn how to obtain and use it, see [Access tokens](/managed/manage/identity-access-management/access-tokens-and-oauth-clients/access-tokens#paas-token "Learn the concept of an access token and its scopes.").

## Parameters

| Parameter | Type | Description | In | Required |
| --- | --- | --- | --- | --- |
| osType | string | The operating system of the installer. The element can hold these values * `windows` * `unix` | path | Required |
| version | string | The required version of the OneAgent in the `1.155.275.20181112-084458` format.  You can retrieve the list of available versions with the [**GET available versions of BOSH tarballs**ï»¿](https://dt-url.net/j703kdn) call. | path | Required |
| skipMetadata | boolean | Set `true` to omit the OneAgent connectivity information from the installer.  If not set, `false` is used. | query | Optional |
| networkZone | string | The network zone you want the result to be configured with. | query | Optional |

## Response

### Response codes

| Code | Type | Description |
| --- | --- | --- |
| **200** | string | Success. The payload contains the BOSH release tarball file. |
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