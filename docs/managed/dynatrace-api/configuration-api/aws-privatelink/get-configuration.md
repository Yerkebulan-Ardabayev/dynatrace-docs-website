---
title: AWS PrivateLink API - GET configuration
source: https://docs.dynatrace.com/managed/dynatrace-api/configuration-api/aws-privatelink/get-configuration
scraped: 2026-05-12T11:21:11.724160
---

# AWS PrivateLink API - GET configuration

# AWS PrivateLink API - GET configuration

* Reference
* Published Nov 19, 2020

Gets the configuration of AWS PrivateLink.

The request produces an `application/json` payload.

|  |  |  |
| --- | --- | --- |
| GET | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/config/v1/aws/privateLink` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/config/v1/aws/privateLink` |

## Authentication

To execute this request, you need an access token with `ReadConfig` scope.

To learn how to obtain and use it, see [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Parameters

The request doesn't provide any configurable parameters.

## Response

### Response codes

| Code | Type | Description |
| --- | --- | --- |
| **200** | [AwsPrivateLinkConfig](#openapi-definition-AwsPrivateLinkConfig) | Success. The result is provided in the response body. |

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