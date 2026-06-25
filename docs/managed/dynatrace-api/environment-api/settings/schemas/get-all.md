---
title: Settings API - GET all schemas
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/settings/schemas/get-all
scraped: 2026-05-12T11:38:44.544349
---

# Settings API - GET all schemas

# Settings API - GET all schemas

* Reference
* Published Feb 24, 2021

Lists all settings schemas available in your environment.

The request produces an `application/json` payload.

|  |  |  |
| --- | --- | --- |
| GET | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/v2/settings/schemas` |
| GET | Environment and Cluster ActiveGate (default port 9999) | `https://{your-activegate-domain}:9999/e/{your-environment-id}/api/v2/settings/schemas` |

## Authentication

To execute this request, you need an access token with `settings.read` scope.

To learn how to obtain and use it, see [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Parameters

| Parameter | Type | Description | In | Required |
| --- | --- | --- | --- | --- |
| fields | string | A list of fields to be included to the response. The provided set of fields replaces the default set.  Specify the required top-level fields, separated by commas (for example, `schemaId,displayName`).  Supported fields: `schemaId`, `displayName`, `maturity`, `latestSchemaVersion`, `multiObject`, `ordered`, `ownerBasedAccessControl`. | query | Optional |

## Response

### Response codes

| Code | Type | Description |
| --- | --- | --- |
| **200** | [SchemaList](#openapi-definition-SchemaList) | Success |
| **4XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Client side error. |
| **5XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Server side error. |

### Response body objects

#### The `SchemaList` object

The list of available settings schemas.

| Element | Type | Description |
| --- | --- | --- |
| items | [SchemaStub[]](#openapi-definition-SchemaStub) | A list of settings schemas. |
| totalCount | integer | The number of schemas in the list. |

#### The `SchemaStub` object

The short representation of the settings schema.

| Element | Type | Description |
| --- | --- | --- |
| displayName | string | The name of the schema. |
| latestSchemaVersion | string | The most recent version of the schema. |
| maturity | string | The maturity of the schema. Possible values:  * PREVIEW: Preview features are not generally available, but might be available in specific environments as part of early-access programs. These are the most likely to change in incompatible ways. * EARLY\_ADOPTER: Features marked "early adopter" are available in all environments, but are not mature enough to warrant the "general availability" designation. We don't expect incompatible changes for these, but please be aware, that these are not fully stable yet and incompatible changes may be necessary in rare cases. * GENERAL\_AVAILABILITY: Features marked "general availability" are the most stable. While the schemas will still evolve over time, care will be taken to only do so in a backward-compatible manner.  In any case, automations should make use of the `schemaVersion` field when writing settings objects. The element can hold these values * `EARLY_ADOPTER` * `GENERAL_AVAILABILITY` * `PREVIEW` |
| multiObject | boolean | Multi-object flag. `True` if the schema is a multi-object schema |
| ordered | boolean | Ordered flag. `True` if the schema is an ordered multi-object schema. |
| ownerBasedAccessControl | boolean | Owner based access control flag. `True` if the schema has owner based access control enabled. |
| schemaId | string | The ID of the schema. |

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



"displayName": "Built-in container monitoring rules",



"latestSchemaVersion": "1.4.2",



"maturity": "GENERAL_AVAILABILITY",



"multiObject": true,



"ordered": false,



"ownerBasedAccessControl": true,



"schemaId": "builtin:container.built-in-monitoring-rule"



}



],



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