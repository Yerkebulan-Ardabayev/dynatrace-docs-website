---
title: AWS PrivateLink API - PUT configuration
source: https://docs.dynatrace.com/managed/dynatrace-api/configuration-api/aws-privatelink/put-configuration
---

# AWS PrivateLink API - PUT configuration

# AWS PrivateLink API - PUT configuration

* Reference
* Published Nov 19, 2020

Updates the configuration of AWS PrivateLink.

The request consumes and produces an `application/json` payload.

|  |  |  |
| --- | --- | --- |
| PUT | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/config/v1/aws/privateLink` |
| PUT | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/config/v1/aws/privateLink` |

## Authentication

To execute this request, you need an access token with `WriteConfig` scope.

To learn how to obtain and use it, see [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Parameters

| Parameter | Type | Description | In | Required |
| --- | --- | --- | --- | --- |
| body | [AwsPrivateLinkConfig](#openapi-definition-AwsPrivateLinkConfig) | The AWS PrivateLink configuration. | body | Required |

### Request body objects

#### The `AwsPrivateLinkConfig` object

| Element | Type | Description | Required |
| --- | --- | --- | --- |
| enabled | boolean | Is AWS PrivateLink enabled | Required |
| vpcEndpointServiceName | string | The VirtualPrivateCluster-service name | Optional |

### Request body JSON model

This is a model of the request body, showing the possible elements. It has to be adjusted for usage in an actual request.

```
{



"enabled": true,



"vpcEndpointServiceName": "string"



}
```

## Response

### Response codes

| Code | Type | Description |
| --- | --- | --- |
| **201** | [AwsPrivateLinkConfig](#openapi-definition-AwsPrivateLinkConfig) | Success. The configuration settings have been updated. |

### Response body objects

#### The `AwsPrivateLinkConfig` object

| Element | Type | Description |
| --- | --- | --- |
| enabled | boolean | Is AWS PrivateLink enabled |
| vpcEndpointServiceName | string | The VirtualPrivateCluster-service name |

### Response body JSON models

```
{



"enabled": true,



"vpcEndpointServiceName": "string"



}
```