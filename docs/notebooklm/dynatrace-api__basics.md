# Dynatrace Documentation: dynatrace-api/basics

Generated: 2026-02-16

Files combined: 6

---


## Source: alerting-profiles-to-settings.md


---
title: Migrate from Alerting profiles API to Settings API
source: https://www.dynatrace.com/docs/dynatrace-api/basics/deprecation-migration-guides/alerting-profiles-to-settings
scraped: 2026-02-16T21:27:28.614742
---

# Migrate from Alerting profiles API to Settings API

# Migrate from Alerting profiles API to Settings API

* Reference
* Published Dec 20, 2022

[Alerting profiles API](/docs/dynatrace-api/configuration-api/alerting-profiles-api "Learn what the Dynatrace alerting profiles API offers.") has been deprecated with [Dynatrace version 1.249](/docs/whats-new/dynatrace-api/sprint-249 "Changelog for Dynatrace API version 1.249"). Its replacement is [Settings API](/docs/dynatrace-api/environment-api/settings "Find out what the Dynatrace Settings API offers.") with the **Problem alerting profiles** (`builtin:alerting.profile`) schema. We recommend that you migrate to the new API at your earliest convenience.

The migration affects endpoint URLs, query parameters, and response/request body parameters, as well as the scope of the token for request authentication.

## Base URL

| new Settings 2.0 | old Alerting profiles |
| --- | --- |
| `/api/v2/settings` | `/api/config/v1/alertingProfiles` |

## Authentication token scope

| new Settings 2.0 | old Alerting profiles |
| --- | --- |
| **Read settings** (`settings.read`) **Write settings** (`settings.write`) | **Read configuration** (`ReadConfig`) **Write configuration** (`WriteConfig`) |

## Parameters

To learn about new query/body parameters, see the documentation of individual requests in [Settings API](/docs/dynatrace-api/environment-api/settings "Find out what the Dynatrace Settings API offers.").

In the Settings 2.0 framework, each alerting profile is represented by a settings object. An object contains some metadata (like the scope or creation timestamp) and the configuration itself, encapsulated in the **value** object. The content of the **value** is essentially the same as the configuration in the deprecated Alerting profiles API. To learn about the parameters of the alerting profile configuration, query the **Problem alerting profiles** (`builtin:alerting.profile`) schema with the [GET a schema](/docs/dynatrace-api/environment-api/settings/schemas/get-schema "View a settings schema via the Dynatrace API.") request.

## Examples

Here are some examples of differences in API usage.

### List alerting profiles

Settings 2.0

Alerting profiles

To list all alerting profiles, you need the [GET objects](/docs/dynatrace-api/environment-api/settings/objects/get-objects "View multiple settings objects via the Dynatrace API.") request. In query parameters, set **schemaIds** to `builtin:alerting.profile` and **scope** to `environment`.

#### Request URL

```
GET https://mySampleEnv.live.dynatrace.com/api/v2/settings/objects?schemaIds=builtin:alerting.profile&scopes=environment
```

#### Response body

```
{



"items": [



{



"objectId": "vu9U3hXa3q0AAAABABhidWlsdGluOmFsZXJ0aW5nLnByb2ZpbGUABnRlbmFudAAGdGVuYW50ACQ4M2Q3NDk5YS1mZDY2LTQ1OGYtOGIxNy1iYjNkMzgwN2RmMTa-71TeFdrerQ",



"value": {



"name": "Synthetic Emergencies",



"severityRules": [



{



"severityLevel": "AVAILABILITY",



"delayInMinutes": 0,



"tagFilterIncludeMode": "INCLUDE_ANY",



"tagFilter": [



"SYN_API",



"SYN_DB",



"SYN_SCH"



]



},



{



"severityLevel": "ERRORS",



"delayInMinutes": 5,



"tagFilterIncludeMode": "INCLUDE_ANY",



"tagFilter": [



"SYN_PLUGIN"



]



}



],



"eventFilters": []



}



},



{



"objectId": "vu9U3hXa3q0AAAABABhidWlsdGluOmFsZXJ0aW5nLnByb2ZpbGUABnRlbmFudAAGdGVuYW50ACQ1ODdkNzk5Yi1mNDI2LTQyNGYtYmY5NS1iZTQ4NzFiYWFlMmO-71TeFdrerQ",



"value": {



"name": "CPU high",



"severityRules": [



{



"severityLevel": "PERFORMANCE",



"delayInMinutes": 30,



"tagFilterIncludeMode": "NONE"



},



{



"severityLevel": "RESOURCE_CONTENTION",



"delayInMinutes": 30,



"tagFilterIncludeMode": "INCLUDE_ANY",



"tagFilter": [



"Holox Cluster"



]



},



{



"severityLevel": "MONITORING_UNAVAILABLE",



"delayInMinutes": 0,



"tagFilterIncludeMode": "NONE"



},



{



"severityLevel": "AVAILABILITY",



"delayInMinutes": 0,



"tagFilterIncludeMode": "NONE"



}



],



"eventFilters": []



}



}



],



"totalCount": 2,



"pageSize": 100



}
```

#### Request URL

```
GET https://mySampleEnv.live.dynatrace.com/config/v1/alertingProfiles
```

#### Response body

```
{



"values": [



{



"id": "b33b45da-a14a-4478-97d3-23fce29fd767",



"name": "Synthetic Emergencies"



},



{



"id": "39115830-1852-3f0c-a73a-f355a19d338b",



"name": "CPU high"



}



]



}
```

### Create an alerting profile

Settings 2.0

Alerting profiles

To create an alerting profile, you need the [POST an object](/docs/dynatrace-api/environment-api/settings/objects/post-object "Create or validate a settings object via the Dynatrace API.") request. In the request body, set **schemaId** to `builtin:alerting.profile` and **scope** to `environment`. Provide the alerting profile configuration in the **value** object.

The response contains the ID of the object that you need to modify the settings.

#### Request URL

```
POST https://mySampleEnv.live.dynatrace.com/api/v2/settings/objects
```

#### Request body

```
[



{



"schemaId": "builtin:alerting.profile",



"scope": "environment",



"value": {



"name": "Sample alerting profile",



"severityRules": [



{



"severityLevel": "AVAILABILITY",



"delayInMinutes": 0,



"tagFilterIncludeMode": "NONE"



}



],



"eventFilters": []



}



}



]
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
POST https://mySampleEnv.live.dynatrace.com/config/v1/alertingProfiles
```

The response contains the ID of the configuration that you need to modify the settings.

#### Request body

```
{



"displayName": "Sample alerting profile",



"severityRules": [



{



"severityLevel": "AVAILABILITY",



"delayInMinutes": 0,



"tagFilterIncludeMode": "NONE"



}



],



"eventFilters": []



}
```

#### Response body

```
{



"id": "2640173c-e9a8-31dc-9584-696969c716f5",



"name": "Sample alerting profile"



}
```

### Edit an alerting profile

Settings 2.0

Alerting profiles

To edit an alerting profile, you need the [PUT an object](/docs/dynatrace-api/environment-api/settings/objects/put-object "Edit a settings object via the Dynatrace API.") request.

#### Request URL

```
PUT https://mySampleEnv.live.dynatrace.com/api/v2/settings/objects/vu9U3hXa3q0AAAABABhidWlsdGluOmFsZXJ0aW5nLnByb2ZpbGUABnRlbmFudAAGdGVuYW50ACQzYjAwNDMwOC01ZTZjLTNkNGMtOTNjMS01ZTBiOWRhZTlhZjW-71TeFdrerQ
```

#### Request body

```
{



"schemaId": "builtin:alerting.profile",



"scope": "environment",



"value": {



"name": "Sample alerting profile",



"managementZone": "1291856336337388063",



"severityRules": [



{



"severityLevel": "AVAILABILITY",



"delayInMinutes": 0,



"tagFilterIncludeMode": "INCLUDE_ALL",



"tagFilter": [



"InfraLinux",



"InraWin"



]



}



],



"eventFilters": []



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
PUT https://mySampleEnv.live.dynatrace.com/config/v1/alertingProfiles/2640173c-e9a8-31dc-9584-696969c716f5
```

#### Request body

```
{



"name": "Sample alerting profile",



"managementZone": "1291856336337388063",



"severityRules": [



{



"severityLevel": "AVAILABILITY",



"delayInMinutes": 0,



"tagFilterIncludeMode": "INCLUDE_ALL",



"tagFilter": [



"InfraLinux",



"InraWin"



]



}



],



"eventFilters": []



}
```

## Related topics

* [Settings API](/docs/dynatrace-api/environment-api/settings "Find out what the Dynatrace Settings API offers.")
* [Alerting profiles API](/docs/dynatrace-api/configuration-api/alerting-profiles-api "Learn what the Dynatrace alerting profiles API offers.")


---


## Source: frequent-issues-to-settings.md


---
title: Migrate from Frequent issue detection API to Settings API
source: https://www.dynatrace.com/docs/dynatrace-api/basics/deprecation-migration-guides/frequent-issues-to-settings
scraped: 2026-02-16T21:24:39.624524
---

# Migrate from Frequent issue detection API to Settings API

# Migrate from Frequent issue detection API to Settings API

* Reference
* Published Dec 22, 2022

The [Frequent issue detection API](/docs/dynatrace-api/configuration-api/frequent-issue-detection-api "Manage frequent issue detection configuration via the Dynatrace API.") has been deprecated with [Dynatrace version 1.249](/docs/whats-new/dynatrace-api/sprint-249 "Changelog for Dynatrace API version 1.249"). Its replacement is [Settings API](/docs/dynatrace-api/environment-api/settings "Find out what the Dynatrace Settings API offers.") with the **Frequent issue detection** (`builtin:anomaly-detection.frequent-issues`) schema. We recommend that you migrate to the new API at your earliest convenience.

The migration affects endpoint URLs, query parameters, and response/request body parameters, as well as the scope of the token for request authentication.

## Base URL

| new Settings 2.0 | old Frequent issue detection |
| --- | --- |
| `/api/v2/settings` | `/api/config/v1/frequentIssueDetection` |

## Authentication token scope

| new Settings 2.0 | old Frequent issue detection |
| --- | --- |
| **Read settings** (`settings.read`) **Write settings** (`settings.write`) | **Read configuration** (`ReadConfig`) **Write configuration** (`WriteConfig`) |

## Parameters

To learn about new query/body parameters, see the documentation of individual requests in [Settings API](/docs/dynatrace-api/environment-api/settings "Find out what the Dynatrace Settings API offers.").

In the Settings 2.0 framework, each frequent issue detection configuration is represented by a settings object. An object contains some metadata (like the scope or creation timestamp) and the configuration itself, encapsulated in the **value** object. To learn about the parameters of the frequent issue detection configuration, query the **Frequent issue detection** (`builtin:anomaly-detection.frequent-issues`) schema with the [GET a schema](/docs/dynatrace-api/environment-api/settings/schemas/get-schema "View a settings schema via the Dynatrace API.") request.

## Examples

Here are some examples of differences in API usage.

### View configuration

Settings 2.0

Frequent issue detection

To view the frequent issue detection configurations, you need the [GET objects](/docs/dynatrace-api/environment-api/settings/objects/get-objects "View multiple settings objects via the Dynatrace API.") request. In query parameters, set **schemaIds** to `builtin:anomaly-detection.frequent-issues` and **scope** to `environment`.

#### Request URL

```
GET https://mySampleEnv.live.dynatrace.com/api/v2/settings/objects?schemaIds=builtin:anomaly-detection.frequent-issues&scopes=environment
```

#### Response body

```
{



"items": [



{



"objectId": "vu9U3hXa3q0AAAABAClidWlsdGluOmFub21hbHktZGV0ZWN0aW9uLmZyZXF1ZW50LWlzc3VlcwAGdGVuYW50AAZ0ZW5hbnQAJDNiNjk1ZjA4LWNhZDEtM2Y2OC04ZDM4LTQyODZkNzkzNjlkNL7vVN4V2t6t",



"value": {



"detectFrequentIssuesInApplications": true,



"detectFrequentIssuesInTransactionsAndServices": true,



"detectFrequentIssuesInInfrastructure": true



}



}



],



"totalCount": 1,



"pageSize": 500



}
```

#### Request URL

```
GET https://mySampleEnv.live.dynatrace.com/config/v1/frequentIssueDetection
```

#### Response body

```
{



"metadata": {



"currentConfigurationVersions": [



"1.0.2"



],



"configurationVersions": [],



"clusterVersion": "1.258.0.20221221-200358"



},



"frequentIssueDetectionApplicationEnabled": true,



"frequentIssueDetectionServiceEnabled": true,



"frequentIssueDetectionInfrastructureEnabled": true



}
```

### Update configuration

Settings 2.0

Frequent issue detection

To edit a maintenance window, you need the [PUT an object](/docs/dynatrace-api/environment-api/settings/objects/put-object "Edit a settings object via the Dynatrace API.") request. In the request body, set **schemaId** to `builtin:anomaly-detection.frequent-issues` and **scope** to `environment`. Provide the frequent issue detection configuration in the **value** object.

#### Request URL

```
PUT https://mySampleEnv.live.dynatrace.com/api/v2/settings/objects/vu9U3hXa3q0AAAABAClidWlsdGluOmFub21hbHktZGV0ZWN0aW9uLmZyZXF1ZW50LWlzc3VlcwAGdGVuYW50AAZ0ZW5hbnQAJDNiNjk1ZjA4LWNhZDEtM2Y2OC04ZDM4LTQyODZkNzkzNjlkNL7vVN4V2t6t
```

#### Request body

```
{



"schemaId": "builtin:alerting.maintenance-window",



"scope": "environment",



"value": {



"detectFrequentIssuesInApplications": true,



"detectFrequentIssuesInTransactionsAndServices": true,



"detectFrequentIssuesInInfrastructure": true



}



}
```

#### Response body

```
[



{



"code": 200,



"objectId": "vu9U3hXa3q0AAAABAClidWlsdGluOmFub21hbHktZGV0ZWN0aW9uLmZyZXF1ZW50LWlzc3VlcwAGdGVuYW50AAZ0ZW5hbnQAJDNiNjk1ZjA4LWNhZDEtM2Y2OC04ZDM4LTQyODZkNzkzNjlkNL7vVN4V2t6t"



}



]
```

#### Request URL

```
PUT https://mySampleEnv.live.dynatrace.com/config/v1/frequentIssueDetection/07f476c6-f1ed-4519-848d-61e52f7e2f24
```

#### Request body

```
{



"frequentIssueDetectionApplicationEnabled": true,



"frequentIssueDetectionServiceEnabled": true,



"frequentIssueDetectionInfrastructureEnabled": false



}
```

## Related topics

* [Settings API](/docs/dynatrace-api/environment-api/settings "Find out what the Dynatrace Settings API offers.")
* [Frequent issue detection API](/docs/dynatrace-api/configuration-api/frequent-issue-detection-api "Manage frequent issue detection configuration via the Dynatrace API.")


---


## Source: maintenance-windows-to-settings.md


---
title: Migrate from Maintenance windows API to Settings API
source: https://www.dynatrace.com/docs/dynatrace-api/basics/deprecation-migration-guides/maintenance-windows-to-settings
scraped: 2026-02-16T09:38:32.290276
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


---


## Source: problems-v1-to-v2.md


---
title: Migrate from Problems API v1 to Problems API v2
source: https://www.dynatrace.com/docs/dynatrace-api/basics/deprecation-migration-guides/problems-v1-to-v2
scraped: 2026-02-15T09:08:29.600639
---

# Migrate from Problems API v1 to Problems API v2

# Migrate from Problems API v1 to Problems API v2

* Reference
* Published Nov 30, 2022

[Problems API v1](/docs/dynatrace-api/environment-api/problems "Find out what the Dynatrace Problems v1 API offers.") has been deprecated with [Dynatrace version 1.243](/docs/whats-new/dynatrace-api/sprint-243 "Changelog for Dynatrace API version 1.243"). Its replacement is [Problems API v2](/docs/dynatrace-api/environment-api/problems-v2 "Find out what the Dynatrace Problems v2 API offers."). We recommend that you migrate to the new API at your earliest convenience.

The migration affects endpoint URLs, query parameters, and response/request body parameters, as well as the scope of the token for request authentication.

## New features

Events API v2 offers you the following new features:

* The [entity selector](/docs/dynatrace-api/environment-api/entity-v2/entity-selector "Configure the entity selector for Environment API endpoints.") helps you to filter problems in read requests.
* Improved problem filtering via a problem selector.
* Unified timeframe selector.

## Base URL

| new Problems v2 | old Problems v1 |
| --- | --- |
| `/api/v2/problems` | `/api/v1/problem` |

## Authentication token scope

| new Problems v2 | old Problems v1 |
| --- | --- |
| **Read problems** (`problems.read`) **Write problems** (`problems.write`) | **Access problem and event feed, metrics, and topology** (`DataExport`) |

## Parameters

To learn about new query/body parameters, see the documentation of individual requests in [Problems API v2](/docs/dynatrace-api/environment-api/problems-v2 "Find out what the Dynatrace Problems v2 API offers.").

## Example

In this example, we query a list of open problems on hosts that happened within the last two hours.

Problems v2

Problems v1

#### Request URL

```
GET https://mySampleEnv.live.dynatrace.com/api/v2/problems?from=now-2h&problemSelector=status("open")&entitySelector=type("HOST")
```

#### Response body

```
{



"totalCount": 2,



"pageSize": 50,



"problems": [



{



"problemId": "-6156404735398726308_1669823466223V2",



"displayId": "P-221194163",



"title": "Host or monitoring unavailable",



"impactLevel": "INFRASTRUCTURE",



"severityLevel": "AVAILABILITY",



"status": "OPEN",



"affectedEntities": [



{



"entityId": {



"id": "HOST-E371A974A078CC54",



"type": "HOST"



},



"name": "frontend-dev"



}



],



"impactedEntities": [



{



"entityId": {



"id": "HOST-E371A974A078CC54",



"type": "HOST"



},



"name": "frontend-dev"



}



],



"rootCauseEntity": null,



"managementZones": [



{



"id": "6143976176513989654",



"name": "Infrastructure Linux"



},



{



"id": "4067143719293196613",



"name": "dev"



},



{



"id": "-6114370715062110014",



"name": "frontent"



}



],



"entityTags": [



{



"context": "CONTEXTLESS",



"key": "frontend",



"stringRepresentation": "frontend"



},



{



"context": "CONTEXTLESS",



"key": "stage",



"value": "dev",



"stringRepresentation": "stage:dev"



}



],



"problemFilters": [



{



"id": "ca786d1f-e6cf-4451-b9dc-9c27c5c339e1",



"name": "Infrastructure alerts"



},



{



"id": "d03022be-d0e3-4089-b02d-ebec9ae87da4",



"name": "Frontend alerts"



}



],



"startTime": 1669823466223,



"endTime": -1



},



{



"problemId": "7188776519218424524_1669820820000V2",



"displayId": "P-221194115",



"title": "High memory usage",



"impactLevel": "INFRASTRUCTURE",



"severityLevel": "CUSTOM_ALERT",



"status": "OPEN",



"affectedEntities": [



{



"entityId": {



"id": "HOST-0F5789A6850FA907",



"type": "HOST"



},



"name": "easyTravel.bookingService.Win.1"



}



],



"impactedEntities": [



{



"entityId": {



"id": "HOST-0F5789A6850FA907",



"type": "HOST"



},



"name": "easyTravel.bookingService.Win.dev.1"



}



],



"rootCauseEntity": null,



"managementZones": [



{



"id": "4067143719293196613",



"name": "dev"



},



{



"id": "7918335421727549830",



"name": "Infrastructure windows"



},



{



"id": "-6239538939987181652",



"name": "Booking service"



}



],



"entityTags": [



{



"context": "CONTEXTLESS",



"key": "stage",



"value": "dev",



"stringRepresentation": "stage:dev"



},



{



"context": "CONTEXTLESS",



"key": "bookingService",



"stringRepresentation": "bookingService"



}



],



"problemFilters": [



{



"id": "ca786d1f-e6cf-4451-b9dc-9c27c5c339e1",



"name": "Infrastructure alerts"



},



{



"id": "ff956dac-8709-3546-bf2b-d82195e7ef6a",



"name": "Booking service alerts"



}



],



"startTime": 1669821000000,



"endTime": -1



}



],



"warnings": []



}
```

In Events API v1, it is not possible to select multiple entities via the entity selector. You have to rely on tags. For illustration purposes, the example payload shows the same problems, but you would have to find them in the payload by external means.

#### Request URL

```
GET https://mySampleEnv.live.dynatrace.com/api/v1/problem/feed?relativeTime=2hours&status=OPEN&tag=stage:dev
```

#### Response body

```
{



"result": {



"problems": [



{



"id": "-6156404735398726308_1669823466223V2",



"startTime": 1669823466223,



"endTime": -1,



"displayName": "P-221194163",



"impactLevel": "INFRASTRUCTURE",



"status": "OPEN",



"severityLevel": "AVAILABILITY",



"commentCount": 0,



"tagsOfAffectedEntities": [



{



"context": "CONTEXTLESS",



"key": "frontend"



},



{



"context": "CONTEXTLESS",



"key": "stage",



"value": "dev"



}



],



"rankedImpacts": [



{



"entityId": "HOST-E371A974A078CC54",



"entityName": "frontend-dev",



"severityLevel": "AVAILABILITY",



"impactLevel": "INFRASTRUCTURE",



"eventType": "CONNECTION_LOST"



}



],



"affectedCounts": {



"INFRASTRUCTURE": 1,



"SERVICE": 0,



"APPLICATION": 0,



"ENVIRONMENT": 0



},



"recoveredCounts": {



"INFRASTRUCTURE": 0,



"SERVICE": 0,



"APPLICATION": 0,



"ENVIRONMENT": 0



},



"hasRootCause": false



},



{



"id": "7188776519218424524_1669820820000V2",



"startTime": 1669821000000,



"endTime": -1,



"displayName": "P-221194115",



"impactLevel": "INFRASTRUCTURE",



"status": "OPEN",



"severityLevel": "CUSTOM_ALERT",



"commentCount": 0,



"tagsOfAffectedEntities": [



{



"context": "CONTEXTLESS",



"key": "stage",



"value": "dev"



},



{



"context": "CONTEXTLESS",



"key": "bookingService"



}



],



"rankedImpacts": [



{



"entityId": "HOST-0F5789A6850FA907",



"entityName": "easyTravel.bookingService.Win.1",



"severityLevel": "CUSTOM_ALERT",



"impactLevel": "INFRASTRUCTURE",



"eventType": "CUSTOM_ALERT"



}



],



"affectedCounts": {



"INFRASTRUCTURE": 1,



"SERVICE": 0,



"APPLICATION": 0,



"ENVIRONMENT": 0



},



"recoveredCounts": {



"INFRASTRUCTURE": 0,



"SERVICE": 0,



"APPLICATION": 0,



"ENVIRONMENT": 0



},



"hasRootCause": false



}



]



}



}
```

## Related topics

* [Problems API v2](/docs/dynatrace-api/environment-api/problems-v2 "Find out what the Dynatrace Problems v2 API offers.")
* [Problems API v1](/docs/dynatrace-api/environment-api/problems "Find out what the Dynatrace Problems v1 API offers.")


---


## Source: topology-v1-to-entity-v2.md


---
title: Migrate from Topology and Smartscape API to Monitored entities API
source: https://www.dynatrace.com/docs/dynatrace-api/basics/deprecation-migration-guides/topology-v1-to-entity-v2
scraped: 2026-02-16T21:19:01.636426
---

# Migrate from Topology and Smartscape API to Monitored entities API

# Migrate from Topology and Smartscape API to Monitored entities API

* Reference
* Published Mar 22, 2023

The [Topology and Smartscape API](/docs/dynatrace-api/environment-api/topology-and-smartscape "Learn about the Dynatrace Topology and Smartscape API.") has been deprecated with [Dynatrace version 1.263](/docs/whats-new/dynatrace-api/sprint-242 "Changelog for Dynatrace API version 1.242"). Its replacement is the [Monitored entities API](/docs/dynatrace-api/environment-api/entity-v2 "Learn about the Dynatrace Monitored entities API."). We recommend that you migrate to the new API at your earliest convenience.

This migration affects endpoint URLs, query parameters, and response/request body parameters, as well as the scope of the token for request authentication.

## New features

The Monitored entities API offers you the following new features:

* Entity type agnostic endpointâyou can query every type of entity via the same URL
* Powerful [entity selector](/docs/dynatrace-api/environment-api/entity-v2/entity-selector "Configure the entity selector for Environment API endpoints.") that helps you to filter entities you want to read
* Unified timeframe selector
* Customizable return valueâyou can control which entity properties are included in the response
* Entity types endpoints
* Custom tags endpoints

## Base URL

| new Monitored entities | old Topology and Smartscape |
| --- | --- |
| `/api/v2/entities` | `/api/v1/entity/applications` `/api/v1/entity/infrastrucutre/hosts` `/api/v1/entity/infrastrucutre/processes` `/api/v1/entity/infrastrucutre/process-groups` `/api/v1/entity/services` |
| `/api/v2/entities/custom` | `/api/v1/entity/infrastructure/custom/{customDeviceId}` |
| `/api/v2/tags` | `/api/v1/entity/applications/{meIdentifier}` `/api/v1/entity/infrastrucutre/hosts/{meIdentifier}` `/api/v1/entity/infrastrucutre/process-groups/{meIdentifier}` `/api/v1/entity/services/{meIdentifier}` |

## Authentication token scope

| new Monitored entities | old Topology and Smartscape |
| --- | --- |
| **Read entities** (`entities.read`) **Write entities** (`entities.write`) | **Access problem and event feed, metrics, and topology** (`DataExport`) |

## Parameters

To learn about new query/body parameters, see the documentation of individual requests in [Monitored entities API](/docs/dynatrace-api/environment-api/entity-v2 "Learn about the Dynatrace Monitored entities API.").

## Changes in workflow

With the upgrade to the Monitored entities API, some workflows require sending additional requests or calling additional endpoints. Be sure to adapt your automation accordingly.

### Pagination

When you query entities in a bulk, pagination is used to reduce the payload size.

1. Specify the number of entities per page in the **pageSize** query parameter.
2. Use the cursor from the **nextPageKey** field of the previous response in the **nextPageKey** query parameter to obtain subsequent pages.

### Create custom devices

In the Monitored entities API, you can't assign tags to the custom device upon creation. If you need to assign tags to your custom device, use a separate request to the [POST custom tags](/docs/dynatrace-api/environment-api/custom-tags/post-tags "Assign custom tags to monitored entities via Dynatrace API.") endpoint.

### Report data to custom devices

In the Monitored entities API, you can't report data to custom devices. Use the [POST ingest data points](/docs/dynatrace-api/environment-api/metric-v2/post-ingest-metrics "Ingest custom metrics to Dynatrace via Metrics v2 API.") call instead.

## Examples

Here are some examples of differences in API usage.

### List entities

In this example, we're querying the list of hosts that were active within the last 2 hours. Also, we don't need the full information about the host: we only need monitoring mode and the list of tags, assigned to the host. The result is truncated to two entries.

Compare the following tabs to see how we do this using the new Monitored entities API and the deprecated Topology and Smartscape API:

Monitored entities API

Topology and Smartscape API

In the Monitored entities API:

* You can control which fields are returned (via the **fields** parameter). In this example, we use the **monitoringMode** and **tags** fields. Type, display name, and entity ID are always included in the response.
* The timeframe is defined via the **from** query parameter. It supports multiple formats; see the individual request documentation to learn more about them.
* The result of the query is split into pages. You can control the page size with the **pageSize** parameter. In this example, the parameter is not set; therefore, the default of 50 entries per page is used.

#### Request URL

```
https://mySampleEnv.live.dynatrace.com/api/v2/entities?fields=properties.monitoringMode,tags&entitySelector=type(%22HOST%22)&from=now-2h
```

#### Query parameters

```
fields=properties.monitoringMode,tags



entitySelector=type("HOST")



from=now-2h
```

#### Response body

```
{



"totalCount": 85,



"pageSize": 50,



"nextPageKey": "AQAMdHlwZSgiSE9TV==",



"entities": [



{



"entityId": "HOST-01A00204B50FF735",



"type": "HOST",



"displayName": "easytravel-backend.internal",



"properties": {



"monitoringMode": "FULL_STACK"



},



"tags": [



{



"context": "CONTEXTLESS",



"key": "Stage",



"value": "PreProduction",



"stringRepresentation": "Stage:PreProduction"



},



{



"context": "CONTEXTLESS",



"key": "OS",



"value": "Linux",



"stringRepresentation": "OS:Linux"



},



{



"context": "CONTEXTLESS",



"key": "backend",



"stringRepresentation": "backend"



}



]



},



{



"entityId": "HOST-0AF138A0258C7DFF",



"type": "HOST",



"displayName": "easytravel-frontend.prod",



"properties": {



"monitoringMode": "FULL_STACK"



},



"tags": [



{



"context": "CONTEXTLESS",



"key": "Stage",



"value": "Production",



"stringRepresentation": "Stage:Production"



},



{



"context": "CONTEXTLESS",



"key": "OS",



"value": "Windows",



"stringRepresentation": "OS:Windows"



},



{



"context": "CONTEXTLESS",



"key": "frontend",



"stringRepresentation": "frontend"



}



]



}



]



}
```

In the Topology and Smartscape API:

* You have limited control over returned fieldsâyou can use **includeDetails** to remove some properties, but you can't select particular fields to be included.
* The timeframe is defined via the **relativeTime** query parameter, which provides a limited amount of pre-defined values. Alternatively, you can use **startTimestamp** and **endTimestamp** fields. Additionally, the timeframe size is restricted to 3 days.
* All the entities are returned in a single payload; pagination is not available.

#### Request URL

```
https://mySampleEnv.live.dynatrace.com/api/v1/entity/infrastructure/hosts?relativeTime=2hours&includeDetails=false
```

#### Query parameters

```
relativeTime=2hours



includeDetails=false
```

#### Response body

```
[



{



"entityId": "HOST-01A00204B50FF735",



"displayName": "easytravel-backend.internal",



"discoveredName": "APM-ET-MF2",



"firstSeenTimestamp": 1627476376157,



"lastSeenTimestamp": 1679410093531,



"tags": [



{



"context": "CONTEXTLESS",



"key": "Stage",



"value": "PreProduction"



},



{



"context": "CONTEXTLESS",



"key": "OS",



"value": "Linux"



},



{



"context": "CONTEXTLESS",



"key": "backend"



}



],



"fromRelationships": {},



"toRelationships": {},



"osType": "LINUX",



"osArchitecture": "X86",



"osVersion": "Ubuntu 20.04.1 LTS (Focal Fossa) (kernel 5.4.0-135-generic)",



"hypervisorType": "VMWARE",



"ipAddresses": [



"192.168.0.1"



],



"bitness": "64bit",



"cpuCores": 4,



"logicalCpuCores": 4,



"monitoringMode": "FULL_STACK",



"networkZoneId": "default",



"agentVersion": {



"major": 1,



"minor": 259,



"revision": 339,



"timestamp": "20230228-182655",



"sourceRevision": ""



},



"consumedHostUnits": 2.0,



"userLevel": "SUPERUSER",



"autoInjection": "ENABLED",



"oneAgentCustomHostName": "easytravel-backend.internal",



"managementZones": [



{



"id": "460039148655162069",



"name": "backend"



}



]



},



{



"entityId": "HOST-0AF138A0258C7DFF",



"displayName": "easytravel-frontend.prod",



"firstSeenTimestamp": 1619706183299,



"lastSeenTimestamp": 1679409948352,



"tags": [



{



"context": "CONTEXTLESS",



"key": "Stage",



"value": "Production",



"stringRepresentation": "Stage:Production"



},



{



"context": "CONTEXTLESS",



"key": "OS",



"value": "Windows",



"stringRepresentation": "OS:Windows"



},



{



"context": "CONTEXTLESS",



"key": "frontend",



"stringRepresentation": "frontend"



}



],



"fromRelationships": {},



"toRelationships": {},



"osType": "WINDOWS",



"osArchitecture": "X86",



"osVersion": "Windows Server 2008 R2 Datacenter Service Pack 1, ver. 6.1.7601",



"hypervisorType": "XEN",



"ipAddresses": [



"192.168.0.2",



"192.168.0.3"



],



"bitness": "64bit",



"cpuCores": 1,



"logicalCpuCores": 2,



"cloudType": "EC2",



"monitoringMode": "FULL_STACK",



"networkZoneId": "default",



"agentVersion": {



"major": 1,



"minor": 247,



"revision": 277,



"timestamp": "20221006-094946",



"sourceRevision": ""



},



"consumedHostUnits": 0.5,



"userLevel": "SUPERUSER",



"autoInjection": "ENABLED",



"softwareTechnologies": [



{



"type": "CITRIX",



"edition": null,



"version": null



}



],



"managementZones": [



{



"id": "-4279023605659327282",



"name": "frontend"



}



]



}



]
```

### Assign entity tags

In this example, we assign additional tags (**Datacenter:Linz** and **Rack:014**) to hosts from the list entities example.

Compare the following tabs to see how we do this using the new Monitored entities API and the deprecated Topology and Smartscape API:

Monitored entities API

Topology and Smartscape API

In the new Monitored entities API, you can assign tags to multiple entities at the same time by selecting them via the [entity selector](/docs/dynatrace-api/environment-api/entity-v2/entity-selector "Configure the entity selector for Environment API endpoints."). In this example, we select hosts by their entity IDs.

#### Request URL

```
https://mySampleEnv.live.dynatrace.com/api/v2/tags?entitySelector=entityId(%22HOST-01A00204B50FF735%22,%22HOST-0AF138A0258C7DFF%22)
```

#### Query parameters

```
entitySelector=entityId("HOST-01A00204B50FF735","HOST-0AF138A0258C7DFF")
```

#### Request body

```
{



"tags": [



{



"key": "Datacenter",



"value": "Linz"



},



{



"key": "Rack",



"value": "014"



}



]



}
```

#### Response body

```
{



"matchedEntitiesCount": 2,



"appliedTags": [



{



"context": "CONTEXTLESS",



"key": "Datacenter",



"value": "Linz",



"stringRepresentation": "Datacenter:Linz"



},



{



"context": "CONTEXTLESS",



"key": "Rack",



"value": "014",



"stringRepresentation": "Rack:014"



}



]



}
```

In the deprecated Topology and Smartscape API, you can assign tags to one entity at a time. The example shows the tag assignment for only one of two hosts. A second request with the same payload is needed to assign tags to another host.

Moreover, the tags are not stored in the `key:value` format. You can only set the `key` part of the tag via this API.

#### Request URL

```
https://mySampleEnv.live.dynatrace.com/api/v1/entity/infrastructure/hosts/HOST-01A00204B50FF735
```

#### Request body

```
{



"tags": [



"Datacenter:Linz",



"Rack:014"



]



}
```

### Create custom devices

In this example, we create a custom device with the ID of `restExample` and the following parameters:

* type: `F5-Firewall`
* IP address `172.16.115.211`
* listen port `9999`

Compare the following tabs to see how we do this using the new Monitored entities API and the deprecated Topology and Smartscape API:

Monitored entities API

Topology and Smartscape API

#### Request URL

```
https://mySampleEnv.live.dynatrace.com/api/v2/entities/custom
```

#### Request body

```
{



"customDeviceId": "restExample",



"displayName": "F5 Firewall 24",



"ipAddresses": ["172.16.115.211"],



"listenPorts": ["9999"],



"type": "F5-Firewall",



"favicon": "http://assets.dynatrace.com/global/icons/f5.png",



"configUrl": "http://192.128.0.1:8080",



"properties": {



"Sample Property 1": "Sample value 1"



}



}
```

#### Response body

```
{



"entityId": "CUSTOM_DEVICE-1525F193C0578E2C",



"groupId": "CUSTOM_DEVICE_GROUP-FC2E2ABF54F513D8"



}
```

#### Request URL

```
https://mySampleEnv.live.dynatrace.com/api/v1/entity/infrastructure/custom/restExample
```

#### Request body

```
{



"displayName": "F5 Firewall 24",



"ipAddresses": ["172.16.115.211"],



"listenPorts": ["9999"],



"type": "F5-Firewall",



"favicon": "http://assets.dynatrace.com/global/icons/f5.png",



"configUrl": "http://192.128.0.1:8080",



"tags": ["REST example"],



"properties": {



"Sample Property 1": "Sample value 1"



}



}
```

#### Response body

```
{



"entityId": "CUSTOM_DEVICE-6A567B33AADC306E",



"groupId": "CUSTOM_DEVICE_GROUP-FC2E2ABF54F513D8"



}
```

## Related topics

* [Access tokens API](/docs/dynatrace-api/environment-api/tokens-v2/api-tokens "Manage Dynatrace API authentication tokens.")
* [Tokens API v1](/docs/dynatrace-api/environment-api/tokens-v1 "Learn how to manage Dynatrace API authentication tokens in your environment.")


---


## Source: dynatrace-api-authentication.md


---
title: Dynatrace API - Tokens and authentication
source: https://www.dynatrace.com/docs/dynatrace-api/basics/dynatrace-api-authentication
scraped: 2026-02-16T21:32:03.675529
---

# Dynatrace API - Tokens and authentication

# Dynatrace API - Tokens and authentication

* Reference
* Published Aug 23, 2018

To be authenticated to use the Dynatrace API, you need a valid [access token](/docs/manage/identity-access-management/access-tokens-and-oauth-clients/access-tokens "Learn the concept of an access token and its scopes.") or a valid [personal access token](/docs/manage/identity-access-management/access-tokens-and-oauth-clients/access-tokens/personal-access-token "Learn the concept of a personal access token and its scopes."). Access to the API is fine-grained, meaning that you also need the proper scopes assigned to the token. See the description of each request to find out which scopes are required to use it.

For details on OAuth clients, see [OAuth clients](/docs/manage/identity-access-management/access-tokens-and-oauth-clients/oauth-clients "Manage authentication and user permissions using OAuth clients.").

## Token format

Dynatrace uses a unique token format consisting of three components separated by dots (`.`).

### Token example

`<DYNATRACE_TOKEN_PLACEHOLDER>`

### Token components

Component name

Component description

prefix

The **prefix** identifies the token type.

In our example: `dt0s01`

See [Token prefixes](#token-format-prefixes) below for a table of standard prefixes.

public portion

The **public portion** of the token is a 24-character public identifier.

In our example: `ST2EY72KQINMH574WMNVI7YN`

token identifier

The **token identifier** is the combination of the **prefix** and the **public portion**. A token identifier can be safely displayed in the UI and can be used for logging purposes.

In our example: `<DYNATRACE_TOKEN_PLACEHOLDER>`

secret portion

The **secret portion** of the token is a 64-character string that should be treated like a password:

* Don't display it
* Don't store it in log files
* Rotate it instantly if it's leaked

In our example: `G3DFPBEJYMODIDAEX454M7YWBUVEFOWKPRVMWFASS64NFH52PX6BNDVFFM572RZM`

### Token prefixes

Prefix

Description

`dt0s01`

This is an API token. It's used as an authorization method: a valid token allows the user to make changes within the Dynatrace account through SCIM.

* It is generated once.
* Do not reveal the secret portion of a `dt0s01` token.
* The public portion is used for identification in the web UI, but you generally should not reveal it (or any portion of this token).
* This token remains in effect until invalidated by the customer, so you must rotate it instantly if it is ever leaked.

`dt0s02`

OAuth2 Clients created by users through Account Management to be used with Dynatrace Apps and Account Management API.

`dt0s03`

OAuth2 Clients for internal and external services and integrations.

`dt0s04`

Chat and identity linking.

`dt0s06`

This is an OAuth2 Refresh Token, which is used to retrieve a new Access Token and generally changes frequently (typically every 5 to 15 minutes).

`dt0s08`

OAuth2 Clients for internal and external services and integrations.

`dt0s09`

Chat and identity linking.

`dt0s16`

Platform Token enabling programmatic access to Dynatrace platform services.

## Generate a token

Access token

Personal access token

To generate an access token:

1. Go to ![Access tokens](https://dt-cdn.net/images/access-tokens-512-a766b810b8.png "Access tokens") **Access Tokens**.
2. Select **Generate new token**.
3. Enter a name for your token.  
   Dynatrace doesn't enforce unique token names. You can create multiple tokens with the same name. Be sure to provide a meaningful name for each token you generate. Proper naming helps you to efficiently manage your tokens and perhaps delete them when they're no longer needed.
4. Select the required scopes for the token.
5. Select **Generate token**.
6. Copy the generated token to the clipboard. Store the token in a password manager for future use.

   You can only access your token once upon creation. You can't reveal it afterward.

To generate a personal access token

1. Go to **Personal Access Tokens** (accessible via the [user menu](/docs/discover-dynatrace/get-started/dynatrace-ui#user-menu-previous-dynatrace "Navigate the latest Dynatrace") in the previous Dynatrace).
2. Select **Generate new token**.
3. Enter a name for your token.  
   Dynatrace doesn't enforce unique token names. You can create multiple tokens with the same name. Be sure to provide a meaningful name for each token you generate. Proper naming helps you to efficiently manage your tokens and perhaps delete them when they're no longer needed.
4. Select the required scopes for the token.
5. Select **Generate token**.
6. Copy the generated token to the clipboard. Store the token in a password manager for future use.

   You can only access your token once upon creation. You can't reveal it afterward.

You can assign multiple scopes to a single token, or you can generate several tokens, each with different access levels and use them accordinglyâcheck your organization's security policies for the best practice.

To change the scope of an existing token, use the [PUT a token call](/docs/dynatrace-api/environment-api/tokens-v2/api-tokens/put-token "Update an access token via Dynatrace API.") of the Access tokens API. Note that you need to submit the existing scopes if you want to keep them. Any existing scope missing in the payload is removed.

Alternatively, you can use the [POST a token](/docs/dynatrace-api/environment-api/tokens-v2/api-tokens/post-token "Create an access token via Dynatrace API.") call to generate a token.

## Token scopes

Access token

Personal access token

### OpenPipeline

Name

API value

Description

OpenPipeline - Ingest Events

`openpipeline.events`

Grants access to [POST Built-in generic events](/docs/platform/openpipeline/reference/openpipeline-ingest-api/generic-events/events-generic-builtin "Ingest generic events from built-in endpoints via OpenPipeline Ingest API.") request of the OpenPipeline Ingest API.

OpenPipeline - Ingest Events, Software Development Lifecycle

`openpipeline.events_sdlc`

Grants access to [POST Built-in SLDC events](/docs/platform/openpipeline/reference/openpipeline-ingest-api/sdlc-events/events-sdlc-builtin "Ingest SDLC events from built-in endpoints via OpenPipeline Ingest API.") request of the OpenPipeline Ingest API.

OpenPipeline - Ingest Events, Software Development Lifecycle (Custom)

`openpipeline.events_sdlc.custom`

Grants access to [POST Custom SLDC events](/docs/platform/openpipeline/reference/openpipeline-ingest-api/sdlc-events/events-sdlc-custom-endpoint "Configure a custom SDLC event endpoint via OpenPipeline Ingest API.") request of the OpenPipeline Ingest API.

OpenPipeline - Ingest Security Events (Built-in)

`openpipeline.events_security`

Grants access to [POST Built-in security events](/docs/platform/openpipeline/reference/openpipeline-ingest-api/security-events/events-security-builtin "Ingest security events from built-in endpoints via OpenPipeline Ingest API.") request of the OpenPipeline Ingest API.

OpenPipeline - Ingest Security Events (Custom)

`openpipeline.events_security.custom`

Grants access to [POST Custom security events](/docs/platform/openpipeline/reference/openpipeline-ingest-api/security-events/events-security-custom-endpoint "Configure a custom security event endpoint via OpenPipeline Ingest API.") request of the OpenPipeline Ingest API.

OpenPipeline - Ingest Events (Custom)

`openpipeline.events.custom`

Grants access to [POST Custom generic event endpoint](/docs/platform/openpipeline/reference/openpipeline-ingest-api/generic-events/events-generic-custom-endpoint "Configure a custom generic event endpoint via OpenPipeline Ingest API.") request of the OpenPipeline Ingest API.

### API v2

Name

API value

Description

Read ActiveGates

`activeGates.read`

Grants access to GET requests of the [ActiveGates API](/docs/dynatrace-api/environment-api/activegates "Learn what the Dynatrace ActiveGate API offers.").

Write ActiveGates

`activeGates.write`

Grants access to POST and DELETE requests of the [ActiveGates API](/docs/dynatrace-api/environment-api/activegates "Learn what the Dynatrace ActiveGate API offers.").

Create ActiveGate tokens

`activeGateTokenManagement.create`

Grants access to the POST request of the ActiveGate tokens API.

Read ActiveGate tokens

`activeGateTokenManagement.read`

Grants access to GET requests of the ActiveGate tokens API.

Write ActiveGate tokens

`activeGateTokenManagement.write`

Grants access to POST and DELETE requests of the ActiveGate tokens API.

Read API tokens

`apiTokens.read`

Grants access to GET requests of the [Access tokens API](/docs/dynatrace-api/environment-api/tokens-v2/api-tokens "Manage Dynatrace API authentication tokens.").

Write API tokens

`apiTokens.write`

Grants access to POST, PUT, and DELETE requests of the [Access tokens API](/docs/dynatrace-api/environment-api/tokens-v2/api-tokens "Manage Dynatrace API authentication tokens.").

Read attacks

`attacks.read`

Grants access to GET requests of the Attacks API and the [Settings API](/docs/dynatrace-api/environment-api/settings "Find out what the Dynatrace Settings API offers.") for Application Protection (`builtin:appsec.attack-protection-settings`, `builtin:appsec.attack-protection-advanced-config`, and `builtin:appsec.attack-protection-allowlist-config schemas`).

Write Application Protection settings

`attacks.write`

Grants access to POST, PUT, and DELETE requests of the [Settings API](/docs/dynatrace-api/environment-api/settings "Find out what the Dynatrace Settings API offers.") for Application Protection (`builtin:appsec.attack-protection-settings`, `builtin:appsec.attack-protection-advanced-config`, and `builtin:appsec.attack-protection-allowlist-config schemas`).

Read audit logs

`auditLogs.read`

Grants access to the [audit log](/docs/manage/data-privacy-and-security/configuration/audit-logs-api "Learn how to manage audit logs using an API.").

Read credential vault entries

`credentialVault.read`

Grants access to GET requests of the [Credential vault API](/docs/dynatrace-api/environment-api/credential-vault "Learn what the Dynatrace API for credentials offers.").

Write credential vault entries

`credentialVault.write`

Grants access to POST, PUT, and DELETE requests of the [Credential vault API](/docs/dynatrace-api/environment-api/credential-vault "Learn what the Dynatrace API for credentials offers.").

Read entities

`entities.read`

Grants access to GET requests of the [Monitored entities](/docs/dynatrace-api/environment-api/entity-v2 "Learn about the Dynatrace Monitored entities API.") and [Custom tags](/docs/dynatrace-api/environment-api/custom-tags "Manage custom tags of the monitored entities via the Dynatrace API.") APIs.

Write entities

`entities.write`

Grants access to POST, PUT, and DELETE requests of the [Monitored entities](/docs/dynatrace-api/environment-api/entity-v2 "Learn about the Dynatrace Monitored entities API.") and [Custom tags](/docs/dynatrace-api/environment-api/custom-tags "Manage custom tags of the monitored entities via the Dynatrace API.") APIs.

Ingest events

`events.ingest`

Grants access to POST request of the [Events API v2](/docs/dynatrace-api/environment-api/events-v2 "Find out what you can do with the Dynatrace Events API v2.").

Read events

`events.read`

Grants access to GET requests of the [Events API v2](/docs/dynatrace-api/environment-api/events-v2 "Find out what you can do with the Dynatrace Events API v2.").

Read extensions monitoring configuration

`extensionConfigurations.read`

Grants access to GET requests from the **Extensions monitoring configuration** section of the [Extensions 2.0 API](/docs/dynatrace-api/environment-api/extensions-20 "Learn how to manage extensions with the Dynatrace Extensions 2.0 API.").

Write extensions monitoring configuration

`extensionConfigurations.write`

Grants access to POST, PUT, and DELETE requests from the **Extensions monitoring configuration** section of the [Extensions 2.0 API](/docs/dynatrace-api/environment-api/extensions-20 "Learn how to manage extensions with the Dynatrace Extensions 2.0 API.").

Read extensions environment configuration

`extensionEnvironment.read`

Grants access to GET requests from the **Extensions environment configuration** section of the [Extensions 2.0 API](/docs/dynatrace-api/environment-api/extensions-20 "Learn how to manage extensions with the Dynatrace Extensions 2.0 API.").

Write extensions environment configuration

`extensionEnvironment.write`

Grants access to POST, PUT, and DELETE requests from the **Extensions environment configuration** section of the [Extensions 2.0 API](/docs/dynatrace-api/environment-api/extensions-20 "Learn how to manage extensions with the Dynatrace Extensions 2.0 API.").

Read extensions

`extensions.read`

Grants access to GET requests from the **Extensions** section of the [Extensions 2.0 API](/docs/dynatrace-api/environment-api/extensions-20 "Learn how to manage extensions with the Dynatrace Extensions 2.0 API.").

Write extensions

`extensions.write`

Grants access to POST, PUT, and DELETE requests from the **Extensions** section of the [Extensions 2.0 API](/docs/dynatrace-api/environment-api/extensions-20 "Learn how to manage extensions with the Dynatrace Extensions 2.0 API.").

Read Geographic regions

`geographicRegions.read`

Grants access to the [Geographic regions API](/docs/dynatrace-api/environment-api/rum/geographic-regions "View requests available through the Dynatrace Geographic regions API.").

Install and update Hub items

`hub.install`

Grants permission to install and update extensions via the [Hub items API](/docs/dynatrace-api/environment-api/hub "Learn how to access Dynatrace Hub features via the Hub items API.").

Read Hub related data

`hub.read`

Grants access to GET requests of the [Hub items API](/docs/dynatrace-api/environment-api/hub "Learn how to access Dynatrace Hub features via the Hub items API.").

Manage metadata of Hub items

`hub.write`

Grants permission to manage metadata of Hub items via the [Hub items API](/docs/dynatrace-api/environment-api/hub "Learn how to access Dynatrace Hub features via the Hub items API.").

Read JavaScript mapping files

`javaScriptMappingFiles.read`

Write JavaScript mapping files

`javaScriptMappingFiles.write`

Ingest logs

`logs.ingest`

Grants access to the [POST ingest logs](/docs/dynatrace-api/environment-api/log-monitoring-v2/post-ingest-logs "Push custom logs to Dynatrace via the Log Monitoring API v2.") request of the Log Monitoring API v2 as well as the [OpenTelemetry log ingest API](/docs/ingest-from/opentelemetry/otlp-api "Learn about the OTLP API endpoints that your application uses to export OpenTelemetry data to Dynatrace.").

Read logs

`logs.read`

Grants access to the GET requests of the [Log Monitoring API v2](/docs/dynatrace-api/environment-api/log-monitoring-v2 "Find out what you can do with the Log Monitoring API v2.")

Ingest metrics

`metrics.ingest`

Grants access to the [POST ingest data points](/docs/dynatrace-api/environment-api/metric-v2/post-ingest-metrics "Ingest custom metrics to Dynatrace via Metrics v2 API.") request of the Metrics v2 API as well as the [OpenTelemetry metrics ingest API](/docs/ingest-from/opentelemetry/otlp-api "Learn about the OTLP API endpoints that your application uses to export OpenTelemetry data to Dynatrace.").

Read metrics

`metrics.read`

Grants access to GET requests of the [Metrics API v2](/docs/dynatrace-api/environment-api/metric-v2 "Retrieve metric information via Metrics v2 API.").

Write metrics

`metrics.write`

Grants access to the [DELETE a custom metric](/docs/dynatrace-api/environment-api/metric-v2/delete-metric "Delete a metric ingested via Metrics v2 API.") request of the Metrics API v2.

Read network zones

`networkZones.read`

Grants access to GET requests of the [Network zones API](/docs/dynatrace-api/environment-api/network-zones "Manage network zones via the Dynatrace API.").

Write network zones

`networkZones.write`

Grants access to POST, PUT, and DELETE requests of the [Network zones API](/docs/dynatrace-api/environment-api/network-zones "Manage network zones via the Dynatrace API.").

Read OneAgents

`oneAgents.read`

Grants access to GET requests of the [OneAgents API](/docs/dynatrace-api/environment-api/oneagent-on-a-host/get-all-hosts-with-oneagents "Check the configuration of OneAgent instances on your hosts via Dynatrace API.").

Write OneAgents

`oneAgents.write`

Grants access to POST and DELETE requests of the [OneAgents API](/docs/dynatrace-api/environment-api/oneagent-on-a-host/get-all-hosts-with-oneagents "Check the configuration of OneAgent instances on your hosts via Dynatrace API.").

Ingest OpenTelemetry traces

`openTelemetryTrace.ingest`

Grants permission to [ingest OpenTelemetry traces](/docs/ingest-from/opentelemetry "Learn how to integrate and ingest OpenTelemetry data (traces, metrics, and logs) into Dynatrace.").

Read problems

`problems.read`

Grants access to GET requests of the [Problems API v2](/docs/dynatrace-api/environment-api/problems-v2 "Find out what the Dynatrace Problems v2 API offers.").

Write problems

`problems.write`

Grants access to POST, PUT, and DELETE requests of the [Problems API v2](/docs/dynatrace-api/environment-api/problems-v2 "Find out what the Dynatrace Problems v2 API offers.").

Read releases

`releases.read`

Grants access to the [Releases API](/docs/dynatrace-api/environment-api/releaseapi "Find out what the Dynatrace Releases API offers.").

Read security problems

`securityProblems.read`

Grants access to GET requests of the [Security problems API](/docs/dynatrace-api/environment-api/application-security/vulnerabilities "Find out what the vulnerabilities API offers.").

Write security problems

`securityProblems.write`

Grants access to POST requests of the [Security problems API](/docs/dynatrace-api/environment-api/application-security/vulnerabilities "Find out what the vulnerabilities API offers.").

Read settings

`settings.read`

Grants access to GET requests of the [Settings API](/docs/dynatrace-api/environment-api/settings "Find out what the Dynatrace Settings API offers.").

Write settings

`settings.write`

Grants access to POST and DELETE requests of the [Settings API](/docs/dynatrace-api/environment-api/settings "Find out what the Dynatrace Settings API offers.").

Read SLO

`slo.read`

Grants access to GET requests of the [Service-level objectives API](/docs/dynatrace-api/environment-api/service-level-objectives-classic "Find out what the Dynatrace SLO API classic offers.").

Write SLO

`slo.write`

Grants access to POST, PUT, and DELETE requests of the [Service-level objectives API](/docs/dynatrace-api/environment-api/service-level-objectives-classic "Find out what the Dynatrace SLO API classic offers.").

Read synthetic monitor execution results

`syntheticExecutions.read`

Grants access to GET requests of the `/synthetic/executions` API.

Write synthetic monitor execution results

`syntheticExecutions.write`

Grants access to POST request of `/synthetic/executions` API.

Read synthetic locations

`syntheticLocations.read`

Grants access to GET requests of the [Synthetic locations API v2](/docs/dynatrace-api/environment-api/synthetic-v2/synthetic-locations-v2 "Manage synthetic locations via the Synthetic v2 API.") and [Synthetic nodes API v2](/docs/dynatrace-api/environment-api/synthetic-v2/synthetic-nodes-v2 "Manage synthetic nodes via the Synthetic v2 API.").

Write synthetic locations

`syntheticLocations.write`

Grants access to POST, PUT, and DELETE requests of the [Synthetic locations API v2](/docs/dynatrace-api/environment-api/synthetic-v2/synthetic-locations-v2 "Manage synthetic locations via the Synthetic v2 API.") and [Synthetic nodes API v2](/docs/dynatrace-api/environment-api/synthetic-v2/synthetic-nodes-v2 "Manage synthetic nodes via the Synthetic v2 API.").

Tenant token rotation

`tenantTokenRotation.write`

Grants access to the [Tenant tokens API](/docs/dynatrace-api/environment-api/tokens-v2/tenant-tokens "Rotate Dynatrace tenant tokens.").

Look up a single trace

`traces.lookup`

Checks for the presence of a trace in cross-environment tracing.

Read Unified Analysis page

`unifiedAnalysis.read`

Grants access to the Unified analysis schema in the [Settings API](/docs/dynatrace-api/environment-api/settings "Find out what the Dynatrace Settings API offers.").

### API v1

Name

API value

Description

Access problems and event feed, metrics, and topology

`DataExport`

Grants access to various calls of [Environment API](/docs/dynatrace-api/environment-api "Find out what you need to use the environment section of the Dynatrace API.").

Create and read synthetic monitors, locations, and nodes

`ExternalSyntheticIntegration`

Grants access to the [Synthetic API](/docs/dynatrace-api/environment-api/synthetic "Find out what the Dynatrace Synthetic v1 API offers.").

Read synthetic monitors, locations, and nodes

`ReadSyntheticData`

Grants access to GET requests of [Synthetic API](/docs/dynatrace-api/environment-api/synthetic "Find out what the Dynatrace Synthetic v1 API offers.").

Read configuration

`ReadConfig`

Grants access to GET calls of [Configuration API](/docs/dynatrace-api/configuration-api "Find out what you need to use the configuration section of the Dynatrace API.").

Write configuration

`WriteConfig`

Grants access to POST, PUT, and DELETE calls of [Configuration API](/docs/dynatrace-api/configuration-api "Find out what you need to use the configuration section of the Dynatrace API.").

Change data privacy settings

`DataPrivacy`

Grants access to [Data privacy API](/docs/dynatrace-api/configuration-api/data-privacy-api "Learn what the Dynatrace data privacy config API offers.") and data privacy calls of [Web application configuration API](/docs/dynatrace-api/configuration-api/rum/web-application-configuration-api "Learn what the Dynatrace web application config API offers.").

User sessions

`DTAQLAccess`

Grants access to [User sessions API](/docs/dynatrace-api/environment-api/rum/user-sessions "Learn what the Dynatrace User Sessions Query language API offers.").

Anonymize user sessions for data privacy reasons

`UserSessionAnonymization`

Grants access to [Anonymization API](/docs/dynatrace-api/environment-api/anonymization "Find out how fulfill GDPR requirements by using the Dynatrace API to remove user data.").

Mobile symbol file management

`DssFileManagement`

Grants access to [Mobile symbolication API](/docs/dynatrace-api/configuration-api/mobile-symbolication-api "Manage mobile symbol files via the Dynatrace API.").

Real User Monitoring JavaScript tag management

`RumJavaScriptTagManagement`

Grants access to [Real User Monitoring JavaScript API](/docs/dynatrace-api/environment-api/rum/real-user-monitoring-javascript-code "Learn how you can use the Dynatrace API to set up and maintain your manually injected applications using the Real User Monitoring JavaScript API.").

ActiveGate certificate management

`ActiveGateCertManagement`

Grants permission to [configure certificate](/docs/ingest-from/dynatrace-activegate/configuration/configure-custom-ssl-certificate-on-activegate "Learn how to configure the SSL certificate on your ActiveGate.") on private ActiveGates.

Fetch data from a remote environment

`RestRequestForwarding`

Grants permission to fetch data from [remote Dynatrace environments](/docs/dynatrace-api/configuration-api/remote-environments "Manage configurations of remote Dynatrace environments via the Dynatrace configuration API.") for multi-environment dashboarding.

Capture request data

`CaptureRequestData`

Grants access to [Request attributes API](/docs/dynatrace-api/configuration-api/service-api/request-attributes-api "Learn what the Dynatrace request attribute config API offers.").

Read log content

`LogExport`

Grants access to [Log Monitoring API](/docs/dynatrace-api/environment-api/log-monitoring-v2 "Find out what you can do with the Log Monitoring API v2.").

### PaaS

Name

API value

Description

Download OneAgent and ActiveGate installers

`InstallerDownload`

Allows download of installers via [Deployment API](/docs/dynatrace-api/environment-api/deployment "Download OneAgent and ActiveGate installers via Dynatrace API.").

Create support alerts

`SupportAlert`

Allows creation of [support alerts](/docs/observe/application-observability/profiling-and-optimization/crash-analysis#support-alert "Learn how Dynatrace can help you gain insight into process crashes.") for crash analysis.

### Other

Name

API value

Description

Upload plugins using the command line

`PluginUpload`

Grants permission to upload OneAgent extensions via [Extension SDK](/docs/ingest-from/extensions/develop-your-extensions "Develop your own Extensions in Dynatrace.").

Dynatrace provides the following permissions for personal access tokens. You can set them in the web UI as described above or via the [**Access tokens** API](/docs/dynatrace-api/environment-api/tokens-v2/api-tokens "Manage Dynatrace API authentication tokens.").

Name

API value

Description

Read API tokens

`apiTokens.read`

Grants access to GET requests of the [Access tokens API](/docs/dynatrace-api/environment-api/tokens-v2/api-tokens "Manage Dynatrace API authentication tokens.").

Write API tokens

`apiTokens.write`

Grants access to POST, PUT, and DELETE requests of the [Access tokens API](/docs/dynatrace-api/environment-api/tokens-v2/api-tokens "Manage Dynatrace API authentication tokens.").

Read entities

`entities.read`

Grants access to GET requests of the [Monitored entities](/docs/dynatrace-api/environment-api/entity-v2 "Learn about the Dynatrace Monitored entities API.") and [Custom tags](/docs/dynatrace-api/environment-api/custom-tags "Manage custom tags of the monitored entities via the Dynatrace API.") APIs.

Write entities

`entities.write`

Grants access to POST, PUT, and DELETE requests of the [Monitored entities](/docs/dynatrace-api/environment-api/entity-v2 "Learn about the Dynatrace Monitored entities API.") and [Custom tags](/docs/dynatrace-api/environment-api/custom-tags "Manage custom tags of the monitored entities via the Dynatrace API.") APIs.

Read metrics

`metrics.read`

Grants access to GET requests of the [Metrics API v2](/docs/dynatrace-api/environment-api/metric-v2 "Retrieve metric information via Metrics v2 API.").

Write metrics

`metrics.write`

Grants access to the [DELETE a custom metric](/docs/dynatrace-api/environment-api/metric-v2/delete-metric "Delete a metric ingested via Metrics v2 API.") request of the Metrics API v2.

Read network zones

`networkZones.read`

Grants access to GET requests of the [Network zones API](/docs/dynatrace-api/environment-api/network-zones "Manage network zones via the Dynatrace API.").

Write network zones

`networkZones.write`

Grants access to POST, PUT, and DELETE requests of the [Network zones API](/docs/dynatrace-api/environment-api/network-zones "Manage network zones via the Dynatrace API.").

Read problems

`problems.read`

Grants access to GET requests of the [Problems API v2](/docs/dynatrace-api/environment-api/problems-v2 "Find out what the Dynatrace Problems v2 API offers.").

Write problems

`problems.write`

Grants access to POST, PUT, and DELETE requests of the [Problems API v2](/docs/dynatrace-api/environment-api/problems-v2 "Find out what the Dynatrace Problems v2 API offers.").

Read releases

`releases.read`

Grants access to the [Releases API](/docs/dynatrace-api/environment-api/releaseapi "Find out what the Dynatrace Releases API offers.").

Read security problems

`securityProblems.read`

Grants access to GET requests of the [Security problems API](/docs/dynatrace-api/environment-api/application-security/vulnerabilities "Find out what the vulnerabilities API offers.").

Write security problems

`securityProblems.write`

Grants access to POST requests of the [Security problems API](/docs/dynatrace-api/environment-api/application-security/vulnerabilities "Find out what the vulnerabilities API offers.").

Read settings

`settings.read`

Grants access to GET requests of the [Settings API](/docs/dynatrace-api/environment-api/settings "Find out what the Dynatrace Settings API offers.").

Write settings

`settings.write`

Grants access to POST and DELETE requests of the [Settings API](/docs/dynatrace-api/environment-api/settings "Find out what the Dynatrace Settings API offers.").

Read SLO

`slo.read`

Grants access to GET requests of the [Service-level objectives API](/docs/dynatrace-api/environment-api/service-level-objectives-classic "Find out what the Dynatrace SLO API classic offers.").

Write SLO

`slo.write`

Grants access to POST, PUT, and DELETE requests of the [Service-level objectives API](/docs/dynatrace-api/environment-api/service-level-objectives-classic "Find out what the Dynatrace SLO API classic offers.").

## Authenticate

You have two options to pass your API token: in the **Authorization** HTTP header or in the **api-token** query parameter.

We recommend that you use the **Authorization** header, as URLs (along with tokens passed within them) might be logged in various locations. Users might also bookmark the URLs or share them in plain text. Therefore, placing authentication tokens into the URL increases the risk that they will be captured by an attacker.

HTTP header

Query parameter

You can authenticate by attaching the token to the **Authorization** HTTP header preceding the **Api-Token** realm.

```
--header 'Authorization: Api-Token dt0c01.abc123.abcdefjhij1234567890'
```

The following example shows authentication via HTTP header.

```
curl --request GET \



--url https://mySampleEnv.live.dynatrace.com/api/v1/config/clusterversion \



--header 'Authorization: Api-Token dt0c01.abc123.abcdefjhij1234567890'
```

You can authenticate by adding the token as the value of the **api-token** query parameter.

```
curl --request GET \



--url 'https://mySampleEnv.live.dynatrace.com/api/v1/config/clusterversion?api-token=abcdefjhij1234567890' \
```

### Authentication in the API Explorer

Select the lock ![Lock](https://dt-cdn.net/images/blue-lock-icon-77090b9928.svg "Lock") icon next to any end point to display information about the OAuth 2.0 tokens that secure that endpoint. Each endpoint requires a specific token type.

You can also unlock all endpoints by selecting **Authorize**. In the displayed dialog, you can then see which token permissions are necessary for each API endpoint. By entering your OAuth 2.0 token into the global **Available authorizations** dialog, you can unlock all related API endpoints.

## Related topics

* [Access tokens classic](/docs/manage/identity-access-management/access-tokens-and-oauth-clients/access-tokens "Learn the concept of an access token and its scopes.")


---
