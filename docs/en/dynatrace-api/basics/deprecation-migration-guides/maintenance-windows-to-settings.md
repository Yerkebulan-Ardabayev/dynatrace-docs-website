---
title: Migrate from Maintenance windows API to Settings API
source: https://www.dynatrace.com/docs/dynatrace-api/basics/deprecation-migration-guides/maintenance-windows-to-settings
scraped: 2026-02-19T21:26:33.167994
---

# Migrate from Maintenance windows API to Settings API

# Migrate from Maintenance windows API to Settings API

* Reference
* Published Dec 21, 2022

The [Maintenance windows API](/docs/dynatrace-api/configuration-api/maintenance-windows-api "Learn what the Dynatrace maintenance windows config API offers.") has been deprecated with [Dynatrace version 1.240](/docs/whats-new/dynatrace-api/sprint-240 "Changelog for Dynatrace API version 1.240"). Its replacement is [Settings API](/docs/dynatrace-api/environment-api/settings "Find out what the Dynatrace Settings API offers.") with the **Maintenance windows** (`builtin:alerting.maintenance-window`) schema. We recommend that you migrate to the new API at your earliest convenience.

The migration affects endpoint URLs, query parameters, and response/request body parameters, as well as the scope of the token for request authentication.

## Base URL

| new Settings 2.0 | old Maintenance windows |
| --- | --- |
| `/api/v2/settings` | `/api/config/v1/maintenanceWindows` |

## Authentication token scope

| new Settings 2.0 | old Maintenance windows |
| --- | --- |
| **Read settings** (`settings.read`) **Write settings** (`settings.write`) | **Read configuration** (`ReadConfig`) **Write configuration** (`WriteConfig`) |

## Parameters

To learn about new query/body parameters, see the documentation of individual requests in [Settings API](/docs/dynatrace-api/environment-api/settings "Find out what the Dynatrace Settings API offers.").

In the Settings 2.0 framework, each maintenance window is represented by a settings object. An object contains some metadata (like the scope or creation timestamp) and the configuration itself, encapsulated in the **value** object. To learn about the parameters of the maintenance window configuration, query the **Maintenance windows** (`builtin:alerting.maintenance-window`) schema with the [GET a schema](/docs/dynatrace-api/environment-api/settings/schemas/get-schema "View a settings schema via the Dynatrace API.") request.

## Examples

Here are some examples of differences in API usage.

### List maintenance windows

Settings 2.0

Maintenance windows

To list all maintenance windows, you need the [GET objects](/docs/dynatrace-api/environment-api/settings/objects/get-objects "View multiple settings objects via the Dynatrace API.") request. In query parameters, set **schemaIds** to `builtin:alerting.maintenance-window` and **scope** to `environment`.

#### Request URL

```
GET https://mySampleEnv.live.dynatrace.com/api/v2/settings/objects?schemaIds=builtin:alerting.maintenance-window&scopes=environment
```

#### Response body

```
{



"items": [



{



"objectId":



"vu9U3hXa3q0AAAABACNidWlsdGluOmFsZXJ0aW5nLm1haW50ZW5hbmNlLXdpbmRvdwAGdGVuYW50AAZ0ZW5hbnQAJDgwMzdjNWM3LTdkNTgtNGQyYy04YzJkLWViMTYxMTBkZTE2Mr7vVN4V2t6t",



"value": {



"enabled": true,



"generalProperties": {



"name": "Synthetic scaling",



"description": "Maintenance window for adaptations of Synthetic monitors",



"maintenanceType": "PLANNED",



"suppression": "DETECT_PROBLEMS_DONT_ALERT",



"disableSyntheticMonitorExecution": false



},



"schedule": {



"scheduleType": "ONCE",



"onceRecurrence": {



"startTime": "2022-12-22T09:00:00",



"endTime": "2022-12-22T12:00:00",



"timeZone": "UTC"



}



},



"filters": [



{



"entityType": "HOST",



"entityTags": [



"[AWS]Usage:Synthetic"



],



"managementZones": []



}



]



}



},



{



"objectId": "vu9U3hXa3q0AAAABACNidWlsdGluOmFsZXJ0aW5nLm1haW50ZW5hbmNlLXdpbmRvdwAGdGVuYW50AAZ0ZW5hbnQAJDE3NDgxMWYxLWQ2NjYtNGJhNy1iZmU3LTk5ZGYzMjIyNjY3Mr7vVN4V2t6t",



"value": {



"enabled": true,



"generalProperties": {



"name": "Issue with pre-production environment",



"maintenanceType": "UNPLANNED",



"suppression": "DONT_DETECT_PROBLEMS",



"disableSyntheticMonitorExecution": false



},



"schedule": {



"scheduleType": "ONCE",



"onceRecurrence": {



"startTime": "2022-12-10T10:00:00",



"endTime": "2022-12-10T14:00:00",



"timeZone": "Europe/Vienna"



}



},



"filters": [



{



"entityType": "SERVICE",



"entityTags": [



"Env-pre-prod"



],



"managementZones": []



},



{



"entityType": "PROCESS_GROUP",



"entityTags": [



"Env-pre-prod"



],



"managementZones": []



}



]



}



}



],



"totalCount": 2,



"pageSize": 100,



}
```

#### Request URL

```
GET https://mySampleEnv.live.dynatrace.com/config/v1/maintenanceWindows
```

#### Response body

```
{



"values": [



{



"id": "00564256-a294-4ed5-9de6-ecba61500ed2",



"name": "Synthetic scaling",



"description": "Maintenance window for adaptations of Synthetic monitors"



},



{



"id": "01ba0f45-7abe-46a3-94b9-ce377f684973",



"name": "Issue with pre-production environment"



}



]



}
```

### Create a maintenance window

Settings 2.0

Maintenance windows

To create a maintenance window, you need the [POST an object](/docs/dynatrace-api/environment-api/settings/objects/post-object "Create or validate a settings object via the Dynatrace API.") request. In the request body, set **schemaId** to `builtin:alerting.maintenance-window` and **scope** to `environment`. Provide the maintenance window configuration in the **value** object.

The response contains the ID of the object that you need to modify the settings.

#### Request URL

```
POST https://mySampleEnv.live.dynatrace.com/api/v2/settings/objects
```

#### Request body

```
[



{



"schemaId": "builtin:alerting.maintenance-window",



"scope": "environment",



"value": {



"enabled": true,



"generalProperties": {



"name": "Sample maintenance window",



"maintenanceType": "PLANNED",



"suppression": "DETECT_PROBLEMS_AND_ALERT",



"disableSyntheticMonitorExecution": false



},



"schedule": {



"scheduleType": "MONTHLY",



"monthlyRecurrence": {



"dayOfMonth": 1,



"timeWindow": {



"startTime": "06:00:00",



"endTime": "06:30:00",



"timeZone": "Europe/Vienna"



},



"recurrenceRange": {



"scheduleStartDate": "2022-01-01",



"scheduleEndDate": "2022-12-31"



}



}



},



"filters": [



{



"entityType": "SERVICE",



"entityTags": [



"stage:pre-production"



],



"managementZones": []



}



]



}



}



]
```

#### Response body

```
[



{



"code": 200,



"objectId": "vu9U3hXa3q0AAAABACNidWlsdGluOmFsZXJ0aW5nLm1haW50ZW5hbmNlLXdpbmRvdwAGdGVuYW50AAZ0ZW5hbnQAJDVhMjg2NmE5LTJjZjQtMzIwZC1hNjMxLTI0NTAwYTQ4NmU5Zr7vVN4V2t6t"



}



]
```

#### Request URL

```
POST https://mySampleEnv.live.dynatrace.com/config/v1/maintenanceWindows
```

The response contains the ID of the configuration that you need to modify the settings.

#### Request body

```
{



"name": "Sample maintenance window",



"description": "",



"type": "PLANNED",



"enabled": true,



"suppression": "DETECT_PROBLEMS_AND_ALERT",



"suppressSyntheticMonitorsExecution": false,



"scope": {



"entities": [],



"matches": [



{



"type": "SERVICE",



"tags": [



{



"context": "CONTEXTLESS",



"key": "stage",



"value": "pre-production"



}



],



"tagCombination": "AND"



}



]



},



"schedule": {



"recurrenceType": "MONTHLY",



"recurrence": {



"dayOfMonth": 1,



"startTime": "06:00",



"durationMinutes": 30



},



"start": "2022-01-01 00:00",



"end": "2022-12-31 23:59",



"zoneId": "Europe/Vienna"



}



}
```

#### Response body

```
{



"id": "07f476c6-f1ed-4519-848d-61e52f7e2f24",



"name": "Sample maintenance window"



}
```

### Edit a maintenance window

Settings 2.0

Maintenance windows

To edit a maintenance window, you need the [PUT an object](/docs/dynatrace-api/environment-api/settings/objects/put-object "Edit a settings object via the Dynatrace API.") request.

#### Request URL

```
PUT https://mySampleEnv.live.dynatrace.com/api/v2/settings/objects/vu9U3hXa3q0AAAABABhidWlsdGluOmFsZXJ0aW5nLnByb2ZpbGUABnRlbmFudAAGdGVuYW50ACQzYjAwNDMwOC01ZTZjLTNkNGMtOTNjMS01ZTBiOWRhZTlhZjW-71TeFdrerQ
```

#### Request body

```
{



"schemaId": "builtin:alerting.maintenance-window",



"scope": "environment",



"value": {



"enabled": true,



"generalProperties": {



"name": "Sample maintenance window",



"maintenanceType": "PLANNED",



"suppression": "DETECT_PROBLEMS_AND_ALERT",



"disableSyntheticMonitorExecution": false



},



"schedule": {



"scheduleType": "MONTHLY",



"monthlyRecurrence": {



"dayOfMonth": 5,



"timeWindow": {



"startTime": "01:00:00",



"endTime": "01:30:00",



"timeZone": "Europe/Vienna"



},



"recurrenceRange": {



"scheduleStartDate": "2022-01-01",



"scheduleEndDate": "2022-12-31"



}



}



},



"filters": [



{



"entityType": "SERVICE",



"entityTags": [



"stage:pre-production"



],



"managementZones": [



"5561909168316319665"



]



}



]



}



}
```

#### Response body

```
[



{



"code": 200,



"objectId": "vu9U3hXa3q0AAAABABhidWlsdGluOmFsZXJ0aW5nLnByb2ZpbGUABnRlbmFudAAGdGVuYW50ACQzYjAwNDMwOC01ZTZjLTNkNGMtOTNjMS01ZTBiOWRhZTlhZjW-71TeFdrerQ"



}



]
```

#### Request URL

```
PUT https://mySampleEnv.live.dynatrace.com/config/v1/maintenanceWindows/07f476c6-f1ed-4519-848d-61e52f7e2f24
```

#### Request body

```
{



"id": "07f476c6-f1ed-4519-848d-61e52f7e2f24",



"name": "Sample MW - old",



"description": "",



"type": "PLANNED",



"enabled": true,



"suppression": "DETECT_PROBLEMS_AND_ALERT",



"suppressSyntheticMonitorsExecution": false,



"scope": {



"entities": [],



"matches": [



{



"mzId": "5561909168316319665",



"type": "SERVICE",



"tags": [



{



"context": "CONTEXTLESS",



"key": "stage",



"value": "pre-production"



}



],



"tagCombination": "AND"



}



]



},



"schedule": {



"recurrenceType": "MONTHLY",



"recurrence": {



"dayOfMonth": 5,



"startTime": "01:00",



"durationMinutes": 30



},



"start": "2022-01-01 00:00",



"end": "2022-12-31 23:59",



"zoneId": "Europe/Vienna"



}



}
```

## Related topics

* [Settings API](/docs/dynatrace-api/environment-api/settings "Find out what the Dynatrace Settings API offers.")
* [Maintenance windows API](/docs/dynatrace-api/configuration-api/maintenance-windows-api "Learn what the Dynatrace maintenance windows config API offers.")