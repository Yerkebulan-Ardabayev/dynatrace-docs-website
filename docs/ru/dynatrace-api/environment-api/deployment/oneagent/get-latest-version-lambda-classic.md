---
title: Deployment API - View the latest OneAgent version for AWS Lambda Classic
source: https://www.dynatrace.com/docs/dynatrace-api/environment-api/deployment/oneagent/get-latest-version-lambda-classic
scraped: 2026-02-19T21:24:38.163220
---

# Deployment API - View the latest OneAgent version for AWS Lambda Classic

# Deployment API - View the latest OneAgent version for AWS Lambda Classic

* Reference
* Updated on Aug 20, 2025

This API is intended for use with the AWS Lambda Classic implementation. For details, see [AWS Lambda](/docs/ingest-from/amazon-web-services/integrate-into-aws/aws-lambda-integration "AWS Lambda capabilities and integration options").

Get the latest version names of OneAgent code modules for the Java, Node.js, and Python AWS Lambda runtimes, also including names for layers that are combined with the log collector, as well as for the standalone log collector layer.

The request produces an `application/json` payload.

|  |  |  |
| --- | --- | --- |
| GET | SaaS | `https://{your-environment-id}.live.dynatrace.com/api/v1/deployment/lambda/agent/latest` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}:9999/e/{your-environment-id}/api/v1/deployment/lambda/agent/latest` |

## Authentication

To execute this request, you need an access token with `InstallerDownload` scope.

To learn how to obtain and use it, see [Tokens and authentication](/docs/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Parameters

The request doesn't provide any configurable parameters.

## Response

### Response codes

| Code | Type | Description |
| --- | --- | --- |
| **200** | [LatestLambdaLayerNames](#openapi-definition-LatestLambdaLayerNames) | Success. The payload contains the available versions. |
| **4XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Client side error. |
| **5XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Server side error. |

### Response body objects

#### The `LatestLambdaLayerNames` object

Latest OneAgent lambda version names available

| Element | Type | Description |
| --- | --- | --- |
| collector | string | - |
| java | string | - |
| java\_with\_collector | string | - |
| nodejs | string | - |
| nodejs\_with\_collector | string | - |
| python | string | - |
| python\_with\_collector | string | - |

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



"collector": "string",



"java": "string",



"java_with_collector": "string",



"nodejs": "string",



"nodejs_with_collector": "string",



"python": "string",



"python_with_collector": "string"



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