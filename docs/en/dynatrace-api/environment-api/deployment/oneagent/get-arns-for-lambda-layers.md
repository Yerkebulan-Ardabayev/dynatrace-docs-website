---
title: Deployment API - View ARNs for AWS Lambda layers
source: https://www.dynatrace.com/docs/dynatrace-api/environment-api/deployment/oneagent/get-arns-for-lambda-layers
scraped: 2026-02-16T09:34:06.327232
---

# Deployment API - View ARNs for AWS Lambda layers

# Deployment API - View ARNs for AWS Lambda layers

* Reference
* Published Jul 29, 2022

This API is intended for use with the latest AWS Lambda implementation. For details, see [AWS Lambda](/docs/ingest-from/amazon-web-services/integrate-into-aws/aws-lambda-integration "AWS Lambda capabilities and integration options").

Get the Amazon Resource Names (ARNs) of the latest version of OneAgent for AWS Lambda layers for supported AWS Lambda runtimes.

Note that passing architecture, technology type, or region as a parameter returns only the relevant layers.

The request produces an `application/json` payload.

|  |  |  |
| --- | --- | --- |
| GET | SaaS | `https://{your-environment-id}.live.dynatrace.com/api/v1/deployment/lambda/layer` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}:9999/e/{your-environment-id}/api/v1/deployment/lambda/layer` |

## Authentication

To execute this request, you need an access token with `InstallerDownload` scope.

To learn how to obtain and use it, see [Tokens and authentication](/docs/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Parameters

| Parameter | Type | Description | In | Required |
| --- | --- | --- | --- | --- |
| arch | string | The architecture of your OS:  * If omitted, shows available layers for all architectures. * `x86`: x86 architecture. * `arm`: ARM architecture. The element can hold these values * `x86` * `arm` | query | Optional |
| techtype | string | Technology type of the lambda runtime. The element can hold these values * `java` * `nodejs` * `python` | query | Optional |
| withCollector | string | Specify if you want the log collector contained or log collector only. ONLY cannot be combined with techtype The element can hold these values * `included` * `excluded` * `only` | query | Optional |
| region | string | The region of the layer. It must match the region of the AWS Lambda function | query | Optional |

## Response

### Response codes

| Code | Type | Description |
| --- | --- | --- |
| **200** | [LatestLambdaLayersMetainfo](#openapi-definition-LatestLambdaLayersMetainfo) | Success. The payload contains the ARNs of the latest available layers. |
| **404** | - | Not found. See the response body for details. |
| **4XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Client side error. |
| **5XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Server side error. |

### Response body objects

#### The `LatestLambdaLayersMetainfo` object

Latest information about available AWS lambda layers

| Element | Type | Description |
| --- | --- | --- |
| arns | [LambdaDto[]](#openapi-definition-LambdaDto) | - |

#### The `LambdaDto` object

| Element | Type | Description |
| --- | --- | --- |
| arch | string | - |
| arn | string | - |
| region | string | - |
| techType | string | - |
| withCollector | string | - |

### Response body JSON models

```
{



"arns": [



{



"arch": "string",



"arn": "string",



"region": "string",



"techType": "string",



"withCollector": "string"



}



]



}
```