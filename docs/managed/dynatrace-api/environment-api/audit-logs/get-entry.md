---
title: Audit logs API - GET audit log entry
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/audit-logs/get-entry
scraped: 2026-05-12T11:36:52.040804
---

# Audit logs API - GET audit log entry

# Audit logs API - GET audit log entry

* Reference
* Published Dec 10, 2019

Fetches the specified entry of the audit log.

|  |  |  |
| --- | --- | --- |
| GET | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/v2/auditlogs/{id}` |
| GET | Environment and Cluster ActiveGate (default port 9999) | `https://{your-activegate-domain}:9999/e/{your-environment-id}/api/v2/auditlogs/{id}` |

## Authentication

To execute this request, you need an access token with `auditLogs.read` scope.

To learn how to obtain and use it, see [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Parameters

| Parameter | Type | Description | In | Required |
| --- | --- | --- | --- | --- |
| id | string | The ID of the required log entry. | path | Required |

## Response

### Response codes

| Code | Type | Description |
| --- | --- | --- |
| **200** | [AuditLogEntry](#openapi-definition-AuditLogEntry) | Success |
| **400** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Failed. Invalid ID format. |
| **404** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Failed. The requested resource doesn't exist. |
| **4XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Client side error. |
| **5XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Server side error. |

### Response body objects

#### The `AuditLogEntry` object

An entry of the audit log.

| Element | Type | Description |
| --- | --- | --- |
| category | string | The category of the recorded operation. The element can hold these values * `ACTIVEGATE_TOKEN` * `BUILD_UNIT_V2` * `CONFIG` * `MANUAL_TAGGING_SERVICE` * `TENANT_LIFECYCLE` * `TOKEN` * `WEB_UI` |
| dt.settings.key | string | The key of the affected object of a setting for entries of category `CONFIG`. |
| dt.settings.object\_id | string | The ID of the affected object of a setting for entries of category `CONFIG`. |
| dt.settings.object\_summary | string | The value summary for entries of category `CONFIG`. |
| dt.settings.schema\_id | string | The schema ID or config ID for entries of category `CONFIG`. |
| dt.settings.scope\_id | string | The persistence scope for entries of category `CONFIG`, e.g. an ME identifier. |
| dt.settings.scope\_name | string | The display name of the scope for entries of category `CONFIG`. |
| entityId | string | The ID of an entity from the **category**.  For example, it can be config ID for the `CONFIG` category or token ID for the `TOKEN` category. |
| environmentId | string | The ID of the Dynatrace environment where the recorded operation occurred. |
| eventType | string | The type of the recorded operation.  * `LOGIN` -> A user logged in * `LOGOUT` -> A user logged out * `CREATE` -> An object was created * `UPDATE` -> An object was updated * `DELETE` -> An object was deleted * `REVOKE` -> An Active Gate token was revoked * `TAG_ADD` -> A manual tag was added * `TAG_REMOVE` -> A manual tag was removed * `TAG_UPDATE` -> A manual tag was updated * `REMOTE_CONFIGURATION_MANAGEMENT` -> A Remote Configuration Management related operation occurred The element can hold these values * `CREATE` * `DELETE` * `LOGIN` * `LOGOUT` * `REORDER` * `REVOKE` * `TAG_ADD` * `TAG_REMOVE` * `TAG_UPDATE` * `UPDATE` |
| logId | string | The ID of the log entry. |
| message | string | The logged message. |
| patch | string | The patch of the recorded operation as the JSON representation.  The format is an enhanced RFC 6902. The patch also carries the previous value in the **oldValue** field. |
| success | boolean | The recorded operation is successful (`true`) or failed (`false`). |
| timestamp | integer | The timestamp of the record creation, in UTC milliseconds. |
| user | string | The ID of the user who performed the recorded operation. |
| userOrigin | string | The origin and the IP address of the **user**. |
| userType | string | The type of the authentication of the **user**.  * `USER_NAME` -> User was logged in the UI * `TOKEN_HASH` -> URL Token or DevOps Token, the hash of the token is logged * `SERVICE_NAME` -> No authenticated user at all, this action was performed by a system service automatically * `PUBLIC_TOKEN_IDENTIFIER` -> API Token, the public token id is logged The element can hold these values * `PUBLIC_TOKEN_IDENTIFIER` * `SERVICE_NAME` * `TOKEN_HASH` * `USER_NAME` |

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



"category": "CONFIG",



"entityId": "MOBILE_RUM: MOBILE_APPLICATION-752C223D59734CD2",



"environmentId": "prod-env-13",



"eventType": "UPDATE",



"logId": "197425568800060000",



"patch": [



{



"oldValue": 20000,



"op": "replace",



"path": "/refreshTimeIntervalMillis",



"value": 30000



}



],



"success": true,



"timestamp": 1974255688445,



"user": "test.user@company.com",



"userOrigin": "webui (192.168.0.2)",



"userType": "USER_NAME"



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

## Example

In this example, the request gets the audit log entry with the ID of **157607396300050000**.

This entry stores information about a change to the configuration of the dashboard with the ID of **14b3bfe7-69d8-48bf-b08a-4f9a2ff3f703**. The change is a repositioning and resizing of a tile done by the Dynatrace user with user ID **643541629**.

The API token is passed in the **Authorization** header.

#### Curl

```
curl -X GET \



'https://mySampleEnv.live.dynatrace.com/api/v2/auditlogs/157607396300050000' \



-H 'Authorization: Api-Token dt0c01.abc123.abcdefjhij1234567890'
```

#### Request URL

```
https://mySampleEnv.live.dynatrace.com/api/v2/auditlogs/157607396300050000
```

#### Response body

```
{



"logId": "157607396300050000",



"eventType": "UPDATE",



"category": "CONFIG",



"entityId": "DASHBOARDS_SETTINGS: 14b3bfe7-69d8-48bf-b08a-4f9a2ff3f703",



"environmentId": "yasmuoujsw",



"user": "Dynatrace user #643541629",



"userType": "USER_NAME",



"userOrigin": "webui (240.204.62.255)",



"timestamp": 1576074315483,



"success": true,



"patch": [



{



"op": "replace",



"path": "/tiles/24/top",



"value": 304,



"oldValue": 380



},



{



"op": "replace",



"path": "/tiles/24/left",



"value": 304,



"oldValue": 798



},



{



"op": "replace",



"path": "/tiles/24/width",



"value": 608,



"oldValue": 304



},



{



"op": "replace",



"path": "/tiles/24/height",



"value": 608,



"oldValue": 304



}



]



}
```

#### Response code

200

## Related topics

* [Audit logs via API](/managed/manage/data-privacy-and-security/configuration/audit-logs-api "Learn how to manage audit logs using an API.")