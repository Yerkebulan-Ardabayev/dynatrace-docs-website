---
title: Kubernetes credentials API - GET all credentials
source: https://docs.dynatrace.com/managed/dynatrace-api/configuration-api/k8s-credentials-api-api/get-all
scraped: 2026-05-12T12:14:52.105988
---

# Kubernetes credentials API - GET all credentials

# Kubernetes credentials API - GET all credentials

* Reference
* Published Jul 22, 2019

This API is deprecated. Use the [Settings API](/managed/dynatrace-api/environment-api/settings "Find out what the Dynatrace Settings API offers.") with the [Kubernetes connection settings](/managed/dynatrace-api/environment-api/settings/schemas/builtin-cloud-kubernetes "View builtin:cloud.kubernetes settings schema table of your monitoring environment via the Dynatrace API.") (`builtin:cloud.kubernetes`) and the [Kubernetes platform monitoring settings](/managed/dynatrace-api/environment-api/settings/schemas/builtin-cloud-kubernetes-monitoring "View builtin:cloud.kubernetes.monitoring settings schema table of your monitoring environment via the Dynatrace API.") (`builtin:cloud.kubernetes.monitoring`) schemas instead.

Lists all available Kubernetes credentials configurations.

The request produces an `application/json` payload.

|  |  |  |
| --- | --- | --- |
| GET | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/config/v1/kubernetes/credentials` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/config/v1/kubernetes/credentials` |

## Authentication

To execute this request, you need an access token with `ReadConfig` scope.

To learn how to obtain and use it, see [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Parameter

The request doesn't provide any configurable parameters.

## Response

### Response codes

| Code | Type | Description |
| --- | --- | --- |
| **200** | [KubernetesConfigStubListDto](#openapi-definition-KubernetesConfigStubListDto) | Success |

### Response body objects

#### The `KubernetesConfigStubListDto` object

| Element | Type | Description |
| --- | --- | --- |
| values | [KubernetesConfigShortRepresentation[]](#openapi-definition-KubernetesConfigShortRepresentation) | - |

#### The `KubernetesConfigShortRepresentation` object

The short representation of a kubernetes configuration.

| Element | Type | Description |
| --- | --- | --- |
| description | string | A short description of the Dynatrace entity. |
| endpointUrl | string | The URL of the Kubernetes API server.  It must be unique within a Dynatrace environment.  The URL must valid according to RFC 2396. Leading or trailing whitespaces are not allowed. |
| id | string | The ID of the Dynatrace entity. |
| name | string | The name of the Dynatrace entity. |

### Response body JSON models

```
{



"values": [



{



"description": "string",



"endpointUrl": "string",



"id": "string",



"name": "string"



}



]



}
```

## Related topics

* [Explore Kubernetes in Dynatrace Hubï»¿](https://www.dynatrace.com/hub/?filter=kubernetes&utm_source=doc&utm_medium=link&utm_campaign=cross)