---
title: Deployment API - View process module configuration for OneAgent
source: https://www.dynatrace.com/docs/dynatrace-api/environment-api/deployment/oneagent/get-processmodule-config
scraped: 2026-02-27T21:31:22.906745
---

# Deployment API - View process module configuration for OneAgent

# Deployment API - View process module configuration for OneAgent

* Reference
* Published Mar 25, 2022

The request produces an `application/json` payload.

|  |  |  |
| --- | --- | --- |
| GET | SaaS | `https://{your-environment-id}.live.dynatrace.com/api/v1/deployment/installer/agent/processmoduleconfig` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}:9999/e/{your-environment-id}/api/v1/deployment/installer/agent/processmoduleconfig` |

## Authentication

To execute this request, you need an access token with `InstallerDownload` scope.

To learn how to obtain and use it, see [Tokens and authentication](/docs/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Parameters

| Parameter | Type | Description | In | Required |
| --- | --- | --- | --- | --- |
| revision | integer | The previously received revision to compare against. | query | Optional |
| sections | string | A list of comma-separated section identifiers to retrieve values for. Supported sections are 'general' and 'agentType'. Defaults to 'general'. | query | Optional |
| hostgroup | string | The name of the host group the process is part of. | query | Optional |

## Response

### Response codes

| Code | Type | Description |
| --- | --- | --- |
| **200** | [AgentProcessModuleConfigResponse](#openapi-definition-AgentProcessModuleConfigResponse) | Success |
| **304** | - | Not modified. |
| **4XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Client side error. |
| **5XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Server side error. |

### Response body objects

#### The `AgentProcessModuleConfigResponse` object

The response to a process module config request.

| Element | Type | Description |
| --- | --- | --- |
| properties | [SectionProperty[]](#openapi-definition-SectionProperty) | The properties and their sections in this response. |
| revision | integer | The new revision associated with the config. |

#### The `SectionProperty` object

A single agent property with it's associated section.

| Element | Type | Description |
| --- | --- | --- |
| key | string | The property key. |
| section | string | The section this property belongs to. |
| value | string | The property value. |

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



"properties": [



{



"key": "dockerInjection",



"section": "general",



"value": "on"



}



],



"revision": 64459404400310540



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