---
title: Azure credentials API - GET all credentials
source: https://docs.dynatrace.com/managed/dynatrace-api/configuration-api/azure-credentials-api/get-all
scraped: 2026-05-12T11:16:31.081425
---

# Azure credentials API - GET all credentials

# Azure credentials API - GET all credentials

* Reference
* Published Feb 25, 2020

Lists all available Azure credentials configurations.

The request produces an `application/json` payload.

|  |  |  |
| --- | --- | --- |
| GET | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/config/v1/azure/credentials` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/config/v1/azure/credentials` |

## Authentication

To execute this request, you need an access token with `ReadConfig` scope.

To learn how to obtain and use it, see [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Parameters

The request doesn't provide any configurable parameters.

## Response

### Response codes

| Code | Type | Description |
| --- | --- | --- |
| **200** | [StubList](#openapi-definition-StubList) | Success |

### Response body objects

#### The `StubList` object

An ordered list of short representations of Dynatrace entities.

| Element | Type | Description |
| --- | --- | --- |
| values | [EntityShortRepresentation[]](#openapi-definition-EntityShortRepresentation) | An ordered list of short representations of Dynatrace entities. |

#### The `EntityShortRepresentation` object

The short representation of a Dynatrace entity.

| Element | Type | Description |
| --- | --- | --- |
| description | string | A short description of the Dynatrace entity. |
| id | string | The ID of the Dynatrace entity. |
| name | string | The name of the Dynatrace entity. |

### Response body JSON models

```
{



"values": [



{



"description": "Dynatrace entity 1 for the REST API example",



"id": "6a98d7bc-abb9-44f8-ae6a-73e68e71812a",



"name": "Dynatrace entity 1"



},



{



"id": "ee70f7d3-9a4e-4f5f-94d2-c9d6156f1618",



"name": "Dynatrace entity 2"



},



{



"id": "8cdabe77-9e1a-4be8-b3df-269dd6fa9d7f"



}



]



}
```

## Example

In this example, the request lists all Azure credentials available in the **mySampleEnv** environment.

The API token is passed in the **Authorization** header.

The result is truncated to two entries.

#### Curl

```
curl -X GET \



https://mySampleEnv.live.dynatrace.com/api/config/v1/azure/credentials \



-H 'Authorization: Api-Token dt0c01.abc123.abcdefjhij1234567890'
```

#### Request URL

```
https://mySampleEnv.live.dynatrace.com/api/config/v1/azure/credentials
```

#### Response body

```
{



"values": [



{



"id": "AZURE_CREDENTIALS-357FDA338DAAF338",



"name": "Booking application"



},



{



"id": "AZURE_CREDENTIALS-04FBA9920F29874B",



"name": "Pre-production"



}



]



}
```

#### Response code

200

## Related topics

* [Microsoft Azure Integrations](/managed/ingest-from/microsoft-azure-services/azure-integrations "Set up Dynatrace deep code monitoring on Azure using OneAgent or OpenTelemetry.")