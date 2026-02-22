---
title: Migrate from Frequent issue detection API to Settings API
source: https://www.dynatrace.com/docs/dynatrace-api/basics/deprecation-migration-guides/frequent-issues-to-settings
scraped: 2026-02-22T21:22:16.283466
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