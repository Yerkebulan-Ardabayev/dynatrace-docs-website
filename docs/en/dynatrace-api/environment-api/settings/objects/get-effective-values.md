---
title: Settings API - GET effective values
source: https://www.dynatrace.com/docs/dynatrace-api/environment-api/settings/objects/get-effective-values
scraped: 2026-02-15T21:24:28.124966
---

# Settings API - GET effective values

# Settings API - GET effective values

* Reference
* Published Aug 26, 2022

Lists effective settings values for the specified schemas at the specified scope.

If there are no settings objects available for the specified schema/scope combination, the request returns default values for the settings.

The request produces an `application/json` payload.

|  |  |  |
| --- | --- | --- |
| GET | SaaS | `https://{your-environment-id}.live.dynatrace.com/api/v2/settings/effectiveValues` |
| GET | Environment ActiveGateCluster ActiveGate | `https://{your-activegate-domain}:9999/e/{your-environment-id}/api/v2/settings/effectiveValues` |

## Authentication

To execute this request, you need an access token with `settings.read` scope.

To learn how to obtain and use it, see [Tokens and authentication](/docs/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Parameters

| Parameter | Type | Description | In | Required |
| --- | --- | --- | --- | --- |
| schemaIds | string | A list of comma-separated schema IDs to which the requested objects belong.  Only considered on load of the first page, when the **nextPageKey** is not set. | query | Optional |
| scope | string | The scope that the requested objects target.  The selection only matches objects directly targeting the specified scope. For example, `environment` will not match objects that target a host within environment. For more details, please see [Dynatrace Documentationï»¿](https://dt-url.net/ky03459).  To load the first page, when the **nextPageKey** is not set, this parameter is required. | query | Optional |
| fields | string | A list of fields to be included to the response. The provided set of fields replaces the default set.  Specify the required top-level fields, separated by commas (for example, `origin,value`).  Supported fields: `summary`, `searchSummary`, `created`, `modified`, `createdBy`, `modifiedBy`, `author`, `origin`, `schemaId`, `schemaVersion`, `value`, `externalId`. | query | Optional |
| nextPageKey | string | The cursor for the next page of results. You can find it in the **nextPageKey** field of the previous response.  The first page is always returned if you don't specify the **nextPageKey** query parameter.  When the **nextPageKey** is set to obtain subsequent pages, you must omit all other query parameters. | query | Optional |
| pageSize | integer | The amount of settings objects in a single response payload.  The maximal allowed page size is 500.  If not set, 100 is used. | query | Optional |
| adminAccess | boolean | If set to true and user has settings:objects:admin permission, the endpoint will act as if the user is the owner of all objects | query | Optional |

## Response

### Response codes

| Code | Type | Description |
| --- | --- | --- |
| **200** | [EffectiveSettingsValuesList](#openapi-definition-EffectiveSettingsValuesList) | Success |
| **404** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Failed. The specified schema or scope is not found. |
| **4XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Client side error. |
| **5XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Server side error. |

### Response body objects

#### The `EffectiveSettingsValuesList` object

A list of effective settings values.

| Element | Type | Description |
| --- | --- | --- |
| items | [EffectiveSettingsValue[]](#openapi-definition-EffectiveSettingsValue) | A list of effective settings values. |
| nextPageKey | string | The cursor for the next page of results. Has the value of `null` on the last page.  Use it in the **nextPageKey** query parameter to obtain subsequent pages of the result. |
| pageSize | integer | The number of entries per page. |
| totalCount | integer | The total number of entries in the result. |

#### The `EffectiveSettingsValue` object

An effective settings value.

| Element | Type | Description |
| --- | --- | --- |
| author | string | The user (identified by a user ID or a public token ID) who performed that most recent modification. |
| created | integer | The timestamp of the creation. |
| externalId | string | The external identifier of the settings object. |
| modified | integer | The timestamp of the last modification. |
| origin | string | The origin of the settings value. |
| schemaId | string | The schema on which the object is based. |
| schemaVersion | string | The version of the schema on which the object is based. |
| searchSummary | string | A searchable summary string of the setting value. Plain text without Markdown. |
| summary | string | A short summary of settings. This can contain Markdown and will be escaped accordingly. |
| value | string | The value of the setting.  It defines the actual values of settings' parameters.  The actual content depends on the object's schema. |

#### The `AnyValue` object

A schema representing an arbitrary value type.

#### The `ErrorEnvelope` object

| Element | Type | Description |
| --- | --- | --- |
| error | [Error](#openapi-definition-Error) | - |

#### The `Error` object

| Element | Type | Description |
| --- | --- | --- |
| code | integer | The HTTP status code |
| constraintViolations | [ConstraintViolation[]](#openapi-definition-ConstraintViolation) | A list of constraint violations |
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



"author": "john.doe@example.com",



"created": 1,



"externalId": "string",



"modified": 1,



"origin": "HOST-D3A3C5A146830A79",



"schemaId": "builtin:container.built-in-monitoring-rule",



"schemaVersion": "1.0.0",



"searchSummary": "string",



"summary": "string",



"value": "string"



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