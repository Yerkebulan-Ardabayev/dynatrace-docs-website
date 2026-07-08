---
title: Deployment API - Download latest OneAgent
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/deployment/oneagent/download-oneagent-latest
---

# Deployment API - Download latest OneAgent

# Deployment API - Download latest OneAgent

* Reference
* Published Aug 28, 2019

Downloads the OneAgent installer as specified in target version of [OneAgent updates](/managed/ingest-from/dynatrace-oneagent/oneagent-update#configure-oneagent-updates "Learn how to update OneAgent."). You can check the latest version number with the [GET the latest version of OneAgent](/managed/dynatrace-api/environment-api/deployment/oneagent/get-version-latest "View the latest version of OneAgent via Dynatrace API.") call.

For the `paas` or `paas-sh` installer types, you can get a configuring installer by passing additional parameters.

|  |  |  |
| --- | --- | --- |
| GET | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/v1/deployment/installer/agent/{osType}/{installerType}/latest` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/v1/deployment/installer/agent/{osType}/{installerType}/latest` |

## Authentication

To execute this request, you need an access token with `InstallerDownload` scope.

To learn how to obtain and use it, see [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Parameters

| Parameter | Type | Description | In | Required |
| --- | --- | --- | --- | --- |
| If-None-Match | string | The ETag of the previous request. Do not download if it matches the ETag of the installer. | header | Optional |
| osType | string | The operating system of the installer. The element can hold these values * `windows` * `unix` * `aix` * `solaris` * `zos` | path | Required |
| installerType | string | The type of the installer:  * `default`: Self-extracting installer for manual installation. Downloads an `.exe` file for Windows or an `.sh` file for Unix. * `default-unattended`: Self-extracting installer for unattended installation. Windows only. Downloads a `.zip` archive, containing the `.msi` installer and the batch file. This option is deprecated with OneAgent version 1.173 * `mainframe`: Downloads all code modules for z/OS combined in a single `*.pax` archive. * `paas`: Code modules installer. Downloads a `*.zip` archive, containing the `manifest.json` file with meta information or a `.jar` file for z/OS. * `paas-sh`: Code modules installer. Downloads a self-extracting shell script with the embedded `tar.gz` archive. The element can hold these values * `default` * `default-unattended` * `mainframe` * `paas` * `paas-sh` | path | Required |
| flavor | string | The flavor of your Linux distribution:  * `musl` for Linux distributions, which are using the musl C standard library, for example Alpine Linux. * `multidistro` for Linux distributions, which are using musl C and glibc standard library. * `default` for Linux distributions, which are using glibc standard library.  Only applicable to the `paas` and `paas-sh` installer types. The element can hold these values * `default` * `multidistro` * `musl` | query | Optional |
| arch | string | The architecture of your OS:  * `all`: Use this value for AIX and z/OS. Defaults to `x86` for other OS types. * `x86`: x86 architecture. * `ppc`: PowerPC architecture, only supported for AIX. * `ppcle`: PowerPC Little Endian architecture, only supported for Linux. * `sparc`: Sparc architecture, only supported for Solaris. * `arm`: ARM architecture, only supported for Linux. * `s390`: S/390 architecture, only supported for Linux.  Only applicable to the `paas` and `paas-sh` installer types. The element can hold these values * `all` * `arm` * `ppc` * `ppcle` * `s390` * `sparc` * `x86` | query | Optional |
| bitness | string | The bitness of your OS. Must be supported by the OS.  Only applicable to the `paas` and `paas-sh` installer types. The element can hold these values * `32` * `64` * `all` | query | Optional |
| include | string[] | The code modules to be included to the installer. You can specify several modules in the following format: `include=java&include=dotnet`.  Only applicable to the `paas` and `paas-sh` installer types. The element can hold these values * `all` * `java` * `java-graal-native` * `apache` * `nginx` * `nodejs` * `dotnet` * `php` * `go` * `sdk` * `envoy` * `python` | query | Optional |
| skipMetadata | boolean | Set `true` to omit the OneAgent connectivity information from the installer.  Only applicable to the `paas` and `paas-sh` installer types. | query | Optional |
| networkZone | string | The network zone you want the result to be configured with. | query | Optional |

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