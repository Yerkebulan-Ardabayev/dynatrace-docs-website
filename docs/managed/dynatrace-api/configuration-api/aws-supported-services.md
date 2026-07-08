---
title: AWS supported services API
source: https://docs.dynatrace.com/managed/dynatrace-api/configuration-api/aws-supported-services
---

# AWS supported services API

# AWS supported services API

* Reference
* Published May 31, 2022

Lists all AWS supported services available in your environment.

The request produces an `application/json` payload.

|  |  |  |
| --- | --- | --- |
| GET | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/config/v1/aws/supportedServices` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/config/v1/aws/supportedServices` |

## Authentication

To execute this request, you need an access token with `ReadConfig` scope.

To learn how to obtain and use it, see [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Parameters

The request doesn't provide any configurable parameters.

## Response

### Response codes

| Code | Type | Description |
| --- | --- | --- |
| **200** | [CloudSupportedServicesList](#openapi-definition-CloudSupportedServicesList) | Success |

### Response body objects

#### The `CloudSupportedServicesList` object

A supported services metadata list

| Element | Type | Description |
| --- | --- | --- |
| services | [CloudSupportedService](#openapi-definition-CloudSupportedService)[] | List of supported services metadata |

#### The `CloudSupportedService` object

A supported service metadata

| Element | Type | Description |
| --- | --- | --- |
| cloudProviderServiceType | string | Name of service used by cloud provider. |
| displayName | string | Display name for service on Dynatrace UI |
| entityType | string | Entity type monitored by this service |
| name | string | Service unique name used by Dynatrace. |

### Response body JSON models

```
{



"services": [



{



"cloudProviderServiceType": "string",



"displayName": "string",



"entityType": "string",



"name": "string"



}



]



}
```

## Example

In this example, the request lists AWS supported services available for **mySampleEnv** environment. The result is truncated to three entries.

The API token is passed in the **Authorization** header.

#### Curl

```
curl --request GET \



--url https://mySampleEnv.live.dynatrace.com/api/config/v1/aws/supportedServices \



--header 'Authorization: Api-Token dt0c01.abc123.abcdefjhij1234567890'
```

#### Request URL

```
https://mySampleEnv.live.dynatrace.com/api/config/v1/aws/supportedServices
```

#### Response body

```
{



"services": [



{



"cloudProviderServiceType": "AWS/ApiGateway",



"name": "APIGateway",



"entityType": "cloud:aws:api_gateway",



"displayName": "Amazon API Gateway"



},



{



"cloudProviderServiceType": "AWS/RDS",



"name": "Aurora",



"entityType": "cloud:aws:aurora",



"displayName": "Amazon Aurora"



},



{



"cloudProviderServiceType": "AWS/Neptune",



"name": "neptune",



"entityType": "cloud:aws:neptune",



"displayName": "Amazon Neptune"



}



]



}
```

#### Response code

200

## Related topics

* [All AWS cloud services](/managed/ingest-from/amazon-web-services/integrate-with-aws/aws-all-services "Monitor all AWS cloud services with Dynatrace and view available metrics.")