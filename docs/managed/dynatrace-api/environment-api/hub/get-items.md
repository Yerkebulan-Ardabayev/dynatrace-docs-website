---
title: Hub capabilities API - GET items
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/hub/get-items
---

# Hub capabilities API - GET items

# Hub capabilities API - GET items

* Reference
* Published Feb 07, 2023

Lists all available Hub items.

The request produces an `application/json` payload.

|  |  |  |
| --- | --- | --- |
| GET | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/v2/hub/items` |
| GET | Environment and Cluster ActiveGate (default port 9999) | `https://{your-activegate-domain}:9999/e/{your-environment-id}/api/v2/hub/items` |

## Authentication

To execute this request, you need an access token with `hub.read` scope.

To learn how to obtain and use it, see [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Parameters

| Parameter | Type | Description | In | Required |
| --- | --- | --- | --- | --- |
| nextPageKey | string | The cursor for the next page of results. You can find it in the **nextPageKey** field of the previous response.  The first page is always returned if you don't specify the **nextPageKey** query parameter.  When the **nextPageKey** is set to obtain subsequent pages, you must omit all other query parameters. | query | Optional |
| pageSize | integer | The amount of hub items in a single response payload.  The maximal allowed page size is 100.  If not set, 20 is used. | query | Optional |
| itemType | string | If provided, will filter out results based on the given item type. The element can hold these values * `EXTENSION1` * `EXTENSION2` * `TECHNOLOGY` | query | Optional |
| query | string | Filter the results for items matching the query string within id, name, author, description or any tag.  * Case insensitive * Spaces in the query string will lead to an intersection of the results of each term | query | Optional |
| installed | boolean | If provided, will restrict the result to Extensions 2.0 that have the respective installed state.  * Only applies if itemType filter is not set or EXTENSION2 | query | Optional |
| categoryId | string | If provided, will filter items that belong to the given category.  * This overrides the itemType or installed filters * For a list of category ids refer to /categories * Will return the items in the order of the category | query | Optional |
| offset | string | If provided, will skip the desired number of results, allowing for pagination in combination with page size | query | Optional |

## Response

### Response codes

| Code | Type | Description |
| --- | --- | --- |
| **200** | [ItemList](#openapi-definition-ItemList) | OK |
| **503** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Unavailable |
| **4XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Client side error. |
| **5XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Server side error. |

### Response body objects

#### The `ItemList` object

| Element | Type | Description |
| --- | --- | --- |
| items | [ItemOverview](#openapi-definition-ItemOverview)[] | A list of available items. |
| nextPageKey | string | The cursor for the next page of results. Has the value of `null` on the last page.  Use it in the **nextPageKey** query parameter to obtain subsequent pages of the result. |
| pageSize | integer | The number of entries per page. |
| totalCount | integer | The total number of entries in the result. |

#### The `ItemOverview` object

Overview of an item.

| Element | Type | Description |
| --- | --- | --- |
| activationLink | string | The activation link for a technology |
| artifactId | string | The unique ID used by the artifacts contained in releases. |
| authorLogo | string | Url for the author's logo. |
| authorName | string | Name of the author of the item. |
| clusterCompatible | boolean | Checks if the item is compatible with the cluster version. |
| comingSoon | boolean | Whether or not the item is planned to be released soon |
| description | string | Description of the item. |
| documentationLink | string | An absolute link to the documentation page of this item. |
| hasDescriptionBlocks | boolean | Whether or not the details call will contain description blocks. |
| itemId | string | Unique Id of the item. |
| logo | string | The logo of the item. Can be a URL or Base64 encoded. Intended for html tags |
| marketingLink | string | An absolute link to the marketing page of this item. |
| name | string | Name of the item. |
| notCompatibleReason | string | The reason why the item is not compatible with the cluster version. |
| tags | string[] | Grouping of items with keywords. |
| type | string | Represents the type of item. It can be TECHNOLOGY, EXTENSION1 or EXTENSION2. The element can hold these values * `EXTENSION1` * `EXTENSION2` * `TECHNOLOGY` |

#### The `ErrorEnvelope` object

| Element | Type | Description |
| --- | --- | --- |
| error | [Error](#openapi-definition-Error) | - |

#### The `Error` object

| Element | Type | Description |
| --- | --- | --- |
| code | integer | The HTTP status code |
| constraintViolations | [ConstraintViolation](#openapi-definition-ConstraintViolation)[] | A list of constraint violations |
| message | string | The error message |

#### The `ConstraintViolation` object

A list of constraint violations

| Element | Type | Description |
| --- | --- | --- |
| location | string | - |
| message | string | - |
| parameterLocation | string | -The element can hold these values * `HEADER` * `PATH` * `PAYLOAD_BODY` * `QUERY` |
| path | string | - |

### Response body JSON models

```
{



"items": [



{



"activationLink": "string",



"artifactId": "snmp-extension.dynatrace.com",



"authorLogo": "string",



"authorName": "string",



"clusterCompatible": true,



"comingSoon": true,



"description": "string",



"documentationLink": "string",



"hasDescriptionBlocks": true,



"itemId": "string",



"logo": "string",



"marketingLink": "string",



"name": "string",



"notCompatibleReason": "string",



"tags": [



"string"



],



"type": "EXTENSION1"



}



],



"nextPageKey": "AQAAABQBAAAABQ==",



"pageSize": 1,



"totalCount": 1



}
```

```
{



"error": {



"code": 1,



"constraintViolations": [



{



"location": "string",



"message": "string",



"parameterLocation": "HEADER",



"path": "string"



}



],



"message": "string"



}



}
```