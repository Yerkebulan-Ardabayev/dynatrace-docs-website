---
title: Migrate from Alerting profiles API to Settings API
source: https://www.dynatrace.com/docs/dynatrace-api/basics/deprecation-migration-guides/alerting-profiles-to-settings
scraped: 2026-02-22T21:24:56.639325
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