---
title: Azure supported services API
source: https://docs.dynatrace.com/managed/dynatrace-api/configuration-api/azure-supported-services
scraped: 2026-05-12T11:04:43.676546
---

# Azure supported services API

# Azure supported services API

* Reference
* Published May 31, 2022

Lists all Azure supported services available in your environment.

The request produces an `application/json` payload.

|  |  |  |
| --- | --- | --- |
| GET | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/config/v1/azure/supportedServices` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/config/v1/azure/supportedServices` |

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
| services | [CloudSupportedService[]](#openapi-definition-CloudSupportedService) | List of supported services metadata |

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

In this example, the request lists Azure supported services available for **mySampleEnv** environment. The result is truncated to three entries.

The API token is passed in the **Authorization** header.

#### Curl

```
curl --request GET \



--url https://mySampleEnv.live.dynatrace.com/api/config/v1/azure/supportedServices \



--header 'Authorization: Api-Token dt0c01.abc123.abcdefjhij1234567890'
```

#### Request URL

```
https://mySampleEnv.live.dynatrace.com/api/config/v1/azure/supportedServices
```

#### Response body

```
{



"services": [



{



"cloudProviderServiceType": "Microsoft.CognitiveServices/accounts",



"name": "cloud:azure:cognitiveservices:anomalydetector",



"entityType": "cloud:azure:cognitiveservices:anomalydetector",



"displayName": "Azure Anomaly Detector"



},



{



"cloudProviderServiceType": "Microsoft.CognitiveServices/accounts",



"name": "cloud:azure:cognitiveservices:textanalytics",



"entityType": "cloud:azure:cognitiveservices:textanalytics",



"displayName": "Azure Text Analytics"



},



{



"cloudProviderServiceType": "Microsoft.CognitiveServices/accounts",



"name": "cloud:azure:cognitiveservices:translator",



"entityType": "cloud:azure:cognitiveservices:translator",



"displayName": "Azure Translator"



}



]



}
```

#### Response code

200

## Related topics

* [All Azure cloud services](/managed/ingest-from/microsoft-azure-services/azure-integrations/azure-cloud-services-metrics "Monitor Azure services with Dynatrace and view available metrics.")