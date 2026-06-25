---
title: Settings API - GET objects
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/settings/objects/get-objects
scraped: 2026-05-12T11:38:45.914164
---

# Settings API - GET objects

# Settings API - GET objects

* Reference
* Published Feb 24, 2021

Lists settings objects that fit the specified criteria.

The request produces an `application/json` payload.

|  |  |  |
| --- | --- | --- |
| GET | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/v2/settings/objects` |
| GET | Environment and Cluster ActiveGate (default port 9999) | `https://{your-activegate-domain}:9999/e/{your-environment-id}/api/v2/settings/objects` |

## Authentication

To execute this request, you need an access token with `settings.read` scope.

To learn how to obtain and use it, see [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Parameters

| Parameter | Type | Description | In | Required |
| --- | --- | --- | --- | --- |
| schemaIds | string | A list of comma-separated schema IDs to which the requested objects belong.  To load the first page, when the **nextPageKey** is not set, either this parameter or **scopes** is required.  To load all objects belonging to the given schema IDs leave the **scopes** parameter empty. | query | Optional |
| scopes | string | A list of comma-separated scopes, that the requested objects target.  The selection only matches objects directly targeting the specified scopes. For example, `environment` will not match objects that target a host within environment. For more details, please see [Dynatrace Documentationï»¿](https://dt-url.net/ky03459).  To load the first page, when the **nextPageKey** is not set, either this parameter or **schemaIds** is required.  To load all objects belonging to the given scopes leave the **schemaIds** parameter empty. | query | Optional |
| externalIds | string | A list of comma-separated external IDs that the requested objects have.  Each external ID has a maximum length of 500 characters.  Only considered on load of the first page, when the **nextPageKey** is not set. | query | Optional |
| fields | string | A list of fields to be included to the response. The provided set of fields replaces the default set.  Specify the required top-level fields, separated by commas (for example, `objectId,value`).  Supported fields: `objectId`, `summary`, `searchSummary`, `created`, `modified`, `createdBy`, `modifiedBy`, `author`, `updateToken`, `scope`, `modificationInfo` (deprecated), `resourceContext`, `owner`, `schemaId`, `schemaVersion`, `value`, `externalId`. | query | Optional |
| filter | string | The filter parameter, as explained [hereï»¿](https://dt-url.net/platform-services-filtering).  Filtering is supported on the following fields:  * `created` * `modified` * `createdBy` * `modifiedBy` * `author` (deprecated, will not work for future schemas) * `value` with properties and sub-properties separated by dot (for example, `value.owningApp = 'Notebooks'`)  If this parameter is omitted, all settings objects will be returned. The maximum nesting depth (via parentheses) is 5. The maximum expression length is 1024 characters.  Note that only fields included to the response via `fields` can be used for filtering. | query | Optional |
| sort | string | The sort parameter, as explained [hereï»¿](https://dt-url.net/platform-services-filtering).  Sorting is supported on the following fields:  * `created` * `modified` * `createdBy` * `modifiedBy` * `author` (deprecated, will not work for future schemas) * `value` with properties and sub-properties separated by dot (for example, `value.owningApp`)  Note that only fields included to the response via `fields` can be used for sorting. | query | Optional |
| nextPageKey | string | The cursor for the next page of results. You can find it in the **nextPageKey** field of the previous response.  The first page is always returned if you don't specify the **nextPageKey** query parameter.  When the **nextPageKey** is set to obtain subsequent pages, you must omit all other query parameters. | query | Optional |
| pageSize | integer | The amount of settings objects in a single response payload.  The maximal allowed page size is 500.  If not set, 100 is used. | query | Optional |
| adminAccess | boolean | If set to true and user has settings:objects:admin permission, the endpoint will act as if the user is the owner of all objects | query | Optional |

## Response

### Response codes

| Code | Type | Description |
| --- | --- | --- |
| **200** | [ObjectsList](#openapi-definition-ObjectsList) | Success. Accessible objects returned. |
| **403** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Failed. Forbidden. |
| **404** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Failed. The specified schema or scope is not found. |
| **4XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Client side error. |
| **5XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Server side error. |

### Response body objects

#### The `ObjectsList` object

A list of settings objects.

| Element | Type | Description |
| --- | --- | --- |
| items | [SettingsObject[]](#openapi-definition-SettingsObject) | A list of settings objects. |
| nextPageKey | string | The cursor for the next page of results. Has the value of `null` on the last page.  Use it in the **nextPageKey** query parameter to obtain subsequent pages of the result. |
| pageSize | integer | The number of entries per page. |
| totalCount | integer | The total number of entries in the result. |

#### The `SettingsObject` object

A settings object.

| Element | Type | Description |
| --- | --- | --- |
| author | string | The user (identified by a user ID or a public token ID) who performed that most recent modification. |
| created | integer | The timestamp of the creation. |
| createdBy | string | The unique identifier of the user who created the settings object. |
| externalId | string | The external identifier of the settings object. |
| ~~modificationInfo~~ | [ModificationInfo](#openapi-definition-ModificationInfo) | DEPRECATED  The modification info for a single updatable setting. Replaced by `resourceContext`. |
| modified | integer | The timestamp of the last modification. |
| modifiedBy | string | The unique identifier of the user who performed the most recent modification. |
| objectId | string | The ID of the settings object. |
| owner | [Identity](#openapi-definition-Identity) | An Identity describing either a user, a group, or the all-users group (applying to all users). |
| resourceContext | [ResourceContext](#openapi-definition-ResourceContext) | The resource context, which contains additional permission information about the object. |
| schemaId | string | The schema on which the object is based. |
| schemaVersion | string | The version of the schema on which the object is based. |
| scope | string | The scope that the object targets. For more details, please see [Dynatrace Documentationï»¿](https://dt-url.net/ky03459). |
| searchSummary | string | A searchable summary string of the setting value. Plain text without Markdown. |
| summary | string | A short summary of settings. This can contain Markdown and will be escaped accordingly. |
| updateToken | string | The update token of the object. You can use it to detect simultaneous modifications by different users.  It is generated upon retrieval (GET requests). If set on update (PUT request) or deletion, the update/deletion will be allowed only if there wasn't any change between the retrieval and the update.  If omitted on update/deletion, the operation overrides the current value or deletes it without any checks. |
| value | string | The value of the setting.  It defines the actual values of settings' parameters.  The actual content depends on the object's schema. |

#### The `ModificationInfo` object

The modification info for a single updatable setting. Replaced by `resourceContext`.

| Element | Type | Description |
| --- | --- | --- |
| deletable | boolean | If settings value can be deleted |
| first | boolean | If non-moveable settings value is in the first group of non-moveable settings, or in the last (start or end of list) |
| modifiable | boolean | If settings value can be modified |
| modifiablePaths | string[] | Property paths which are modifiable, regardless of the state of `modifiable` |
| movable | boolean | If settings value can be moved/reordered. Only applicable for ordered list schema |
| nonModifiablePaths | string[] | Property paths which are not modifiable, when `modifiable` is true |

#### The `Identity` object

An Identity describing either a user, a group, or the all-users group (applying to all users).

| Element | Type | Description |
| --- | --- | --- |
| id | string | The user id or user group id if type is 'user' or 'group', missing if type is 'all-users'. |
| type | string | The type of the identity. The element can hold these values * `all-users` * `group` * `user` |

#### The `ResourceContext` object

The resource context, which contains additional permission information about the object.

| Element | Type | Description |
| --- | --- | --- |
| modifications | [Modification](#openapi-definition-Modification) | The additional modification details for this settings object. |
| operations | string[] | The allowed operations on this settings object. The element can hold these values * `delete` * `read` * `write` |

#### The `Modification` object

The additional modification details for this settings object.

| Element | Type | Description |
| --- | --- | --- |
| first | boolean | If non-moveable settings object is in the first group of non-moveable settings, or in the last (start or end of list). |
| modifiablePaths | string[] | Property paths which are modifiable, regardless if the `write` operation is allowed. |
| movable | boolean | If settings object can be moved/reordered. Only applicable for ordered list schema. |
| nonModifiablePaths | string[] | Property paths which are not modifiable, even if the `write` operation is allowed. |

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



"createdBy": "fab17b7a-2eb2-4c95-b818-743d94be2c30",



"externalId": "string",



"modificationInfo": {



"deletable": true,



"first": true,



"modifiable": true,



"modifiablePaths": [



"string"



],



"movable": true,



"nonModifiablePaths": [



"string"



]



},



"modified": 1,



"modifiedBy": "fab17b7a-2eb2-4c95-b818-743d94be2c30",



"objectId": "Y2ktaGdyb3VwLTEyMythZjhjOThlOS0wN2I0LTMyMGEtOTQzNi02NTEyMmVlNWY4NGQ=",



"owner": {



"id": "string",



"type": "user"



},



"resourceContext": {



"modifications": {



"first": true,



"modifiablePaths": [



"string"



],



"movable": true,



"nonModifiablePaths": [



"string"



]



},



"operations": [



"delete"



]



},



"schemaId": "builtin:container.built-in-monitoring-rule",



"schemaVersion": "1.0.0",



"scope": "HOST-D3A3C5A146830A79",



"searchSummary": "string",



"summary": "string",



"updateToken": "Y2ktaGdyb3VwLTEyMythZjhjOThlOS0wN2I0LTMyMGEtOTQzNi02NTEyMmVlNWY4NGQ=",



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