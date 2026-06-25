---
title: Extensions API - GET states of an extension
source: https://docs.dynatrace.com/managed/dynatrace-api/configuration-api/extensions-api/get-state
scraped: 2026-05-12T11:19:53.366984
---

# Extensions API - GET states of an extension

# Extensions API - GET states of an extension

* Reference
* Published Mar 06, 2020

Lists the endpoint states of the specified extension.

States are stored in server memory and are cleared with restart.

The request produces an `application/json` payload.

|  |  |  |
| --- | --- | --- |
| GET | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/config/v1/extensions/{id}/states` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/config/v1/extensions/{id}/states` |

## Authentication

To execute this request, you need an access token with `ReadConfig` scope.

To learn how to obtain and use it, see [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Parameters

| Parameter | Type | Description | In | Required |
| --- | --- | --- | --- | --- |
| id | string | The ID of the required extension. | path | Required |
| pageSize | integer | The number of results per result page. Must be between 1 and 500 | query | Optional |
| nextPageKey | string | The cursor for the next page of results. | query | Optional |
| state | string | Extension state to filter. The element can hold these values * `DISABLED` * `ERROR_AUTH` * `ERROR_COMMUNICATION_FAILURE` * `ERROR_CONFIG` * `ERROR_TIMEOUT` * `ERROR_UNKNOWN` * `INCOMPATIBLE` * `LIMIT_REACHED` * `NOTHING_TO_REPORT` * `OK` * `STATE_TYPE_UNKNOWN` * `UNINITIALIZED` * `UNSUPPORTED` * `WAITING_FOR_STATE` | query | Optional |

## Response

### Response codes

| Code | Type | Description |
| --- | --- | --- |
| **200** | [ExtensionStateList](#openapi-definition-ExtensionStateList) | Success |

### Response body objects

#### The `ExtensionStateList` object

A list of extension states.

| Element | Type | Description |
| --- | --- | --- |
| nextPageKey | string | The cursor for the next page of results. Has the value of `null` on the last page.  Use it in the **nextPageKey** query parameter to obtain subsequent pages of the result. |
| states | [ExtensionState[]](#openapi-definition-ExtensionState) | A list of extension states. |
| totalResults | integer | The total number of entries in the result. |

#### The `ExtensionState` object

The state of the extension.

| Element | Type | Description |
| --- | --- | --- |
| endpointId | string | The ID of the endpoint where the state is detected - Active Gate only. |
| extensionId | string | The ID of the extension. |
| hostId | string | The ID of the host on which the extension runs. |
| processId | string | The ID of the entity on which the extension is active. |
| state | string | The state of the extension. The element can hold these values * `ERROR_AUTH` * `ERROR_COMMUNICATION_FAILURE` * `ERROR_CONFIG` * `ERROR_TIMEOUT` * `ERROR_UNKNOWN` * `INCOMPATIBLE` * `LIMIT_REACHED` * `NOTHING_TO_REPORT` * `OK` * `STATE_TYPE_UNKNOWN` * `UNINITIALIZED` * `UNSUPPORTED` * `WAITING_FOR_STATE` |
| stateDescription | string | A short description of the state. |
| timestamp | integer | The timestamp when the state was detected, in UTC milliseconds. |
| version | string | The version of the extension (for example `1.0.0`). |

### Response body JSON models

```
{



"nextPageToken": "LlUdYmu5S2MfX/ppfCInR9M=",



"states": [



{



"endpointId": "null",



"extensionId": "custom.python.connectionpool",



"hostId": "HOST-01A7DEFA5340A86D",



"processId": "PROCESS_GROUP_INSTANCE-2182DF2E20E3E067",



"state": "OK",



"stateDescription": "",



"timestamp": 1578578108213,



"version": "1.82"



}



],



"totalResults": 9



}
```

## Related topics

* [Develop your own Extensions](/managed/ingest-from/extensions/develop-your-extensions "Develop your own Extensions in Dynatrace.")