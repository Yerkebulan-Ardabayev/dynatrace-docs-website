---
title: Automatically applied tags API - GET all auto-tags
source: https://docs.dynatrace.com/managed/dynatrace-api/configuration-api/automatically-applied-tags-api/get-all
scraped: 2026-05-12T12:06:02.974114
---

# Automatically applied tags API - GET all auto-tags

# Automatically applied tags API - GET all auto-tags

* Reference
* Published Aug 09, 2019

Deprecated

This API is deprecated. Use the [Settings API](/managed/dynatrace-api/environment-api/settings "Find out what the Dynatrace Settings API offers.") with the [Automatically applied tags](/managed/dynatrace-api/environment-api/settings/schemas/builtin-tags-auto-tagging "View builtin:tags.auto-tagging settings schema table of your monitoring environment via the Dynatrace API.") (`builtin:tags.auto-tagging`) schema instead.

Lists all automatically applied tags defined in your Dynatrace environment.

The request produces an `application/json` payload.

|  |  |  |
| --- | --- | --- |
| GET | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/config/v1/autoTags` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/config/v1/autoTags` |

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

In this example, the request asks for a list of all the auto-tags in the **mySampleEnv** environment.

The API token is passed in the **Authorization** header.

The result is truncated to three entries.

#### Curl

```
curl -X GET \



https://mySampleEnv.live.dynatrace.com/api/config/v1/autoTags \



-H 'Authorization: Api-Token dt0c01.abc123.abcdefjhij1234567890'
```

#### Request URL

```
https://mySampleEnv.live.dynatrace.com/api/config/v1/autoTags
```

#### Response body

```
{



"values": [



{



"id": "368a23c5-15fa-4745-9f91-26fbbbd0756c",



"name": "MainApp"



},



{



"id": "b0e81616-01b5-437a-a2ec-7b6cc63a62a3",



"name": "Infrastructure - Windows"



},



{



"id": "7c82c170-b380-4fa7-992a-453f3e73047b",



"name": "Infrastructure - Linux"



}



]



}
```

#### Response code

200

## Related topics

* [Define and apply tags](/managed/manage/tags-and-metadata/setup/how-to-define-tags "Find out how to define and apply tags manually and automatically.")
* [Tags and metadata](/managed/manage/tags-and-metadata "Use tags and metadata to organize data in your Dynatrace environment.")