---
title: Extensions API - GET all extension's instances
source: https://docs.dynatrace.com/managed/dynatrace-api/configuration-api/extensions-api/get-all-instances
scraped: 2026-05-12T11:19:56.000353
---

# Extensions API - GET all extension's instances

# Extensions API - GET all extension's instances

* Reference
* Published Mar 06, 2020

Lists all instances of the specified extension.

The request produces an `application/json` payload.

|  |  |  |
| --- | --- | --- |
| GET | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/config/v1/extensions/{id}/instances` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/config/v1/extensions/{id}/instances` |

## Authentication

To execute this request, you need an access token with `ReadConfig` scope.

To learn how to obtain and use it, see [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Parameters

| Parameter | Type | Description | In | Required |
| --- | --- | --- | --- | --- |
| id | string | The ID of the required extension. | path | Required |
| pageSize | integer | The number of results per result page. Must be between 1 and 500 | query | Optional |
| nextPageKey | string | The cursor for the next page of results. | query | Optional |

## Response

### Response codes

| Code | Type | Description |
| --- | --- | --- |
| **200** | [ExtensionConfigurationList](#openapi-definition-ExtensionConfigurationList) | Success |

### Response body objects

#### The `ExtensionConfigurationList` object

A list of configurations.

| Element | Type | Description |
| --- | --- | --- |
| configurationsList | [EntityShortRepresentation[]](#openapi-definition-EntityShortRepresentation) | List of configurations. |
| nextPageKey | string | The cursor for the next page of results. Has the value of `null` on the last page.  Use it in the **nextPageKey** query parameter to obtain subsequent pages of the result. |
| totalResults | integer | The total number of entries in the result. |

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



"configurationsList": [



{



"id": "HOST-E1550E0AED6A572F"



}



],



"nextPageToken": "LlUdYmu5S2MfX/ppfCInR9M=",



"totalResults": 9



}
```

## Related topics

* [Develop your own Extensions](/managed/ingest-from/extensions/develop-your-extensions "Develop your own Extensions in Dynatrace.")