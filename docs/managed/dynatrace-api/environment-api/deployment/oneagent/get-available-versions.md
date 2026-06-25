---
title: Deployment API - List available versions of OneAgent
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/deployment/oneagent/get-available-versions
scraped: 2026-05-12T11:58:31.687130
---

# Deployment API - List available versions of OneAgent

# Deployment API - List available versions of OneAgent

* Reference
* Published Aug 28, 2019

Lists all available versions of OneAgent installer.

The request produces an `application/json` payload.

|  |  |  |
| --- | --- | --- |
| GET | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/v1/deployment/installer/agent/versions/{osType}/{installerType}` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/v1/deployment/installer/agent/versions/{osType}/{installerType}` |

## Authentication

To execute this request, you need an access token with `InstallerDownload` scope.

To learn how to obtain and use it, see [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Parameters

| Parameter | Type | Description | In | Required |
| --- | --- | --- | --- | --- |
| osType | string | The operating system of the installer. The element can hold these values * `windows` * `unix` * `aix` * `solaris` * `zos` | path | Required |
| installerType | string | The type of the installer:  * `default`: Self-extracting installer for manual installation. Downloads an `.exe` file for Windows or an `.sh` file for Unix. * `default-unattended`: Self-extracting installer for unattended installation. Windows only. Downloads a `.zip` archive, containing the `.msi` installer and the batch file. This option is deprecated with OneAgent version 1.173 * `mainframe`: Downloads all code modules for z/OS combined in a single `*.pax` archive. * `paas`: Code modules installer. Downloads a `*.zip` archive, containing the `manifest.json` file with meta information or a `.jar` file for z/OS. * `paas-sh`: Code modules installer. Downloads a self-extracting shell script with the embedded `tar.gz` archive. The element can hold these values * `default` * `default-unattended` * `mainframe` * `paas` * `paas-sh` | path | Required |
| flavor | string | The flavor of your Linux distribution:  * `musl` for Linux distributions, which are using the musl C standard library, for example Alpine Linux. * `multidistro` for Linux distributions, which are using musl C and glibc standard library. * `default` for Linux distributions, which are using glibc standard library.  Only applicable to the `paas` and `paas-sh` installer types. The element can hold these values * `default` * `multidistro` * `musl` | query | Optional |
| arch | string | The architecture of your OS:  * `all`: Use this value for AIX and z/OS. Defaults to `x86` for other OS types. * `x86`: x86 architecture. * `ppc`: PowerPC architecture, only supported for AIX. * `ppcle`: PowerPC Little Endian architecture, only supported for Linux. * `sparc`: Sparc architecture, only supported for Solaris. * `arm`: ARM architecture, only supported for Linux. * `s390`: S/390 architecture, only supported for Linux.  Only applicable to the `paas` and `paas-sh` installer types. The element can hold these values * `all` * `arm` * `ppc` * `ppcle` * `s390` * `sparc` * `x86` | query | Optional |

## Response

### Response codes

| Code | Type | Description |
| --- | --- | --- |
| **200** | [AgentInstallerVersions](#openapi-definition-AgentInstallerVersions) | Success. The payload contains the available versions. |
| **4XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Client side error. |
| **5XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Server side error. |

### Response body objects

#### The `AgentInstallerVersions` object

A list of available versions of OneAgent installer.

| Element | Type | Description |
| --- | --- | --- |
| availableVersions | string[] | A list of available versions of OneAgent installer. |

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



"availableVersions": [



"string"



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