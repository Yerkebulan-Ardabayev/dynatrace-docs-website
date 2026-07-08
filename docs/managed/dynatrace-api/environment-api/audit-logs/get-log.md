---
title: Audit logs API - GET audit log
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/audit-logs/get-log
---

# Audit logs API - GET audit log

# Audit logs API - GET audit log

* Reference
* Published Dec 10, 2019

Fetches the audit log of your Dynatrace environment.

The full list can be lengthy, so you can narrow it down by specifying filter parameters, like tags. See the **Parameters** section for more details.

You can limit the output by using the pagination:

1. Specify the number of results per page in the **pageSize** query parameter.
2. Then use the cursor from the **nextPageKey** field of the previous response in the **nextPageKey** query parameter to obtain subsequent pages.

|  |  |  |
| --- | --- | --- |
| GET | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/v2/auditlogs` |
| GET | Environment and Cluster ActiveGate (default port 9999) | `https://{your-activegate-domain}:9999/e/{your-environment-id}/api/v2/auditlogs` |

## Authentication

To execute this request, you need an access token with `auditLogs.read` scope.

To learn how to obtain and use it, see [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Parameters

| Parameter | Type | Description | In | Required |
| --- | --- | --- | --- | --- |
| nextPageKey | string | The cursor for the next page of results. You can find it in the **nextPageKey** field of the previous response.  The first page is always returned if you don't specify the **nextPageKey** query parameter.  When the **nextPageKey** is set to obtain subsequent pages, you must omit all other query parameters. | query | Optional |
| pageSize | integer | The amount of log entries in a single response payload.  The maximal allowed page size is 5000.  If not set, 1000 is used. | query | Optional |
| filter | string | Filters the audit log. You can use the following criteria:  * User: `user("userIdentification")`. The `EQUALS` operator applies. * Event type: `eventType("value")`. The `EQUALS` operator applies. * Category of a logged operation: `category("value")`. The `EQUALS` operator applies. * Entity ID: `entityId("id")`. The `CONTAINS` operator applies. * Settings schema ID: `dt.settings.schema_id("id")`. The `EQUALS` operator applies. * Settings scope ID: `dt.settings.scope_id("id")`. The `EQUALS` operator applies. * Settings key: `dt.settings.key("key")`. The `EQUALS` operator applies. * Settings object ID: `dt.settings.object_id("id")`. The `EQUALS` operator applies.  For each criterion, you can specify multiple alternatives with comma-separated values. In this case, the OR logic applies. For example, `eventType("CREATE","UPDATE")` means eventType can be "CREATE" or "UPDATE".  You can specify multiple comma-separated criteria, such as `eventType("CREATE","UPDATE"),category("CONFIG")`. Only results matching **all** criteria are included in response.  Specify the value of a criterion as a quoted string. The following special characters must be escaped with a tilde (`~`) inside quotes:  * Tilde `~` * Quote `"` | query | Optional |
| from | string | The start of the requested timeframe.  You can use one of the following formats:  * Timestamp in UTC milliseconds. * Human-readable format of `2021-01-25T05:57:01.123+01:00`. If no time zone is specified, UTC is used. You can use a space character instead of the `T`. Seconds and fractions of a second are optional. * Relative timeframe, back from now. The format is `now-NU/A`, where `N` is the amount of time, `U` is the unit of time, and `A` is an alignment. The alignment rounds all the smaller values to the nearest zero in the past. For example, `now-1y/w` is one year back, aligned by a week.   You can also specify relative timeframe without an alignment: `now-NU`.   Supported time units for the relative timeframe are: + `m`: minutes   + `h`: hours   + `d`: days   + `w`: weeks   + `M`: months   + `y`: years  If not set, the relative timeframe of two weeks is used (`now-2w`). | query | Optional |
| to | string | The end of the requested timeframe.  You can use one of the following formats:  * Timestamp in UTC milliseconds. * Human-readable format of `2021-01-25T05:57:01.123+01:00`. If no time zone is specified, UTC is used. You can use a space character instead of the `T`. Seconds and fractions of a second are optional. * Relative timeframe, back from now. The format is `now-NU/A`, where `N` is the amount of time, `U` is the unit of time, and `A` is an alignment. The alignment rounds all the smaller values to the nearest zero in the past. For example, `now-1y/w` is one year back, aligned by a week.   You can also specify relative timeframe without an alignment: `now-NU`.   Supported time units for the relative timeframe are: + `m`: minutes   + `h`: hours   + `d`: days   + `w`: weeks   + `M`: months   + `y`: years  If not set, the current timestamp is used. | query | Optional |
| sort | string | The sorting of audit log entries:  * `timestamp`: Oldest first. * `-timestamp`: Newest first.  If not set, the newest first sorting is applied. | query | Optional |

## Response

### Response codes

| Code | Type | Description |
| --- | --- | --- |
| **200** | [AuditLog](#openapi-definition-AuditLog) | Success |
| **4XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Client side error. |
| **5XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Server side error. |

### Response body objects

#### The `AuditLog` object

The audit log of your environment.

| Element | Type | Description |
| --- | --- | --- |
| auditLogs | [AuditLogEntry](#openapi-definition-AuditLogEntry)[] | A list of audit log entries ordered by the creation timestamp. |
| nextPageKey | string | The cursor for the next page of results. Has the value of `null` on the last page.  Use it in the **nextPageKey** query parameter to obtain subsequent pages of the result. |
| pageSize | integer | The number of entries per page. |
| totalCount | integer | The total number of entries in the result. |

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
| patch | [AnyValue](#openapi-definition-AnyValue) | The patch of the recorded operation as the JSON representation.  The format is an enhanced RFC 6902. The patch also carries the previous value in the **oldValue** field. |
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



"auditLogs": [



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



],



"nextPageKey": "___a7acX3q0AAAAAACJidWlsdGluOnNlcnZpY2lUVEJCUzBaNVIxVjJOSGt6Y3oyLTcwMUZWRkxlclH__9rtpxferQ",



"pageSize": 5,



"totalCount": 10



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

In this example, the request fetches all logins (`filter=eventType(LOGIN)`) from the audit log of the **mySampleEnv** environment for the last week (`from=now-1w`).

The API token is passed in the **Authorization** header.

The response is truncated to the first three entries.

#### Curl

```
curl -X GET \



'https://mySampleEnv.live.dynatrace.com/api/v2/auditlogs?filter=eventType%28LOGIN%29&from=now-1w' \



-H 'Authorization: Api-Token dt0c01.abc123.abcdefjhij1234567890'
```

#### Request URL

```
https://mySampleEnv.live.dynatrace.com/api/v2/auditlogs?filter=eventType%28LOGIN%29&from=now-1w
```

#### Response body

```
{



"totalCount": 5820,



"nextPageKey": "vu8y3hPZ3q0AAAAAAi_neQJ8qUAAAAFu0T-ECgAAAW71TAgKAAAD6AAQZXZlbnRUeXBlKExPR0lOKQC-7zLeE9nerQ",



"auditLogs": [



{



"logId": "157607341600050000",



"eventType": "LOGIN",



"category": "WEB_UI",



"entityId": "240.204.62.255",



"environmentId": "yasmuoujsw",



"user": "Dynatrace support user #877988415",



"userType": "USER_NAME",



"userOrigin": "Forwarded: 240.204.62.255",



"timestamp": 1576073415531,



"success": true



},



{



"logId": "157607338800050000",



"eventType": "LOGIN",



"category": "WEB_UI",



"entityId": "55.199.177.119",



"environmentId": "yasmuoujsw",



"user": "Dynatrace support user #490812376",



"userType": "USER_NAME",



"userOrigin": "Forwarded: 55.199.177.119",



"timestamp": 1576073388150,



"success": true



},



{



"logId": "157607338300060000",



"eventType": "LOGIN",



"category": "WEB_UI",



"entityId": "75.16.11.184",



"environmentId": "umsaywsjuo",



"user": "Dynatrace support user #765684830",



"userType": "USER_NAME",



"userOrigin": "Forwarded: 75.16.11.184",



"timestamp": 1576073381543,



"success": true



}



]



}
```

#### Response code

200

## Related topics

* [Audit logs via API](/managed/manage/data-privacy-and-security/configuration/audit-logs-api "Learn how to manage audit logs using an API.")