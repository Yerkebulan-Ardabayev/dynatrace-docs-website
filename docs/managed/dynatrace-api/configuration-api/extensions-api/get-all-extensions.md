---
title: Extensions API - GET all extensions
source: https://docs.dynatrace.com/managed/dynatrace-api/configuration-api/extensions-api/get-all-extensions
---

# Extensions API - GET all extensions

# Extensions API - GET all extensions

* Reference
* Published Mar 06, 2020

Lists all extensions uploaded to your Dynatrace environment.

The request produces an `application/json` payload.

|  |  |  |
| --- | --- | --- |
| GET | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/config/v1/extensions` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/config/v1/extensions` |

## Authentication

To execute this request, you need an access token with `ReadConfig` scope.

To learn how to obtain and use it, see [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Parameters

| Parameter | Type | Description | In | Required |
| --- | --- | --- | --- | --- |
| pageSize | integer | The number of results per result page. Must be between 1 and 500 | query | Optional |
| nextPageKey | string | The cursor for the next page of results. | query | Optional |

## Response

### Response codes

| Code | Type | Description |
| --- | --- | --- |
| **200** | [ExtensionListDto](#openapi-definition-ExtensionListDto) | Success |

### Response body objects

#### The `ExtensionListDto` object

| Element | Type | Description |
| --- | --- | --- |
| extensions | [ExtensionDto](#openapi-definition-ExtensionDto)[] | A list of extensions. |
| nextPageKey | string | The cursor for the next page of results. Has the value of `null` on the last page.  Use it in the **nextPageKey** query parameter to obtain subsequent pages of the result. |
| totalResults | integer | The total number of entries in the result. |

#### The `ExtensionDto` object

| Element | Type | Description |
| --- | --- | --- |
| id | string | - |
| name | string | - |
| type | string | -The element can hold these values * `ACTIVEGATE` * `CODEMODULE` * `JMX` * `ONEAGENT` * `PMI` * `UNKNOWN` |

### Response body JSON models

```
{



"extensions": [



{



"id": "custom.python.connectionpool",



"name": "Connection Pool",



"type": "ONEAGENT"



}



],



"nextPageToken": "LlUdYmu5S2MfX/ppfCInR9M=",



"totalResults": 9



}
```

## Related topics

* [Develop your own Extensions](/managed/ingest-from/extensions/develop-your-extensions "Develop your own Extensions in Dynatrace.")