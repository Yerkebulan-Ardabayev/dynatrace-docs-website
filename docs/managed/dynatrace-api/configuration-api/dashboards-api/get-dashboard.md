---
title: "Dashboards API - GET a dashboard"
source: https://docs.dynatrace.com/managed/dynatrace-api/configuration-api/dashboards-api/get-dashboard
updated: 2026-02-09
---

# Dashboards API - GET a dashboard

# Dashboards API - GET a dashboard

* Reference
* Published Jan 23, 2019

Gets parameters of the specified dashboard.

The request produces an `application/json` payload.

|  |  |  |
| --- | --- | --- |
| GET | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/config/v1/dashboards/{id}` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/config/v1/dashboards/{id}` |

## Authentication

To execute this request, you need an access token with `ReadConfig` scope.

To learn how to obtain and use it, see [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Parameters

| Parameter | Type | Description | In | Required |
| --- | --- | --- | --- | --- |
| id | string | The ID of the required dashboard. | path | Required |

## Response

Refer to [Tile JSON models](/managed/dynatrace-api/configuration-api/dashboards-api/dashboards-api-tile-models "Learn the variations of tile JSON models in the Dynatrace Dashboards Classic API.") to find JSON models for each tile type.

### Response codes

| Code | Type | Description |
| --- | --- | --- |
| **200** | [Dashboard](#openapi-definition-Dashboard) | Success. The response body contains parameters of the dashboard. |

### Response body objects

#### The `Dashboard` object

Configuration of a dashboard.

| Element | Type | Description |
| --- | --- | --- |
| dashboardMetadata | [DashboardMetadata](#openapi-definition-DashboardMetadata) | Parameters of a dashboard. |
| id | string | The ID of the dashboard. |
| metadata | [ConfigurationMetadata](#openapi-definition-ConfigurationMetadata) | Metadata useful for debugging |
| tiles | [Tile[]](#openapi-definition-Tile) | The list of tiles on the dashboard. |

#### The `DashboardMetadata` object

Parameters of a dashboard.

| Element | Type | Description |
| --- | --- | --- |
| dashboardFilter | [DashboardFilter](#openapi-definition-DashboardFilter) | Filters, applied to a dashboard. |
| dynamicFilters | [DynamicFilters](#openapi-definition-DynamicFilters) | Dashboard filter configuration of a dashboard. |
| hasConsistentColors | boolean | The tile uses consistent colors when rendering its content. |
| name | string | The name of the dashboard. |
| owner | string | The owner of the dashboard. |
| preset | boolean | The dashboard is a preset (`true`) or a custom (`false`) dashboard. |
| shared | boolean | The dashboard is shared (`true`) or private (`false`). |
| tags | string[] | A set of tags assigned to the dashboard. |
| tilesNameSize | string | The general size of the tiles tile. Default value is medium The element can hold these values * `small` * `medium` * `large` |

#### The `DashboardFilter` object

Filters, applied to a dashboard.

| Element | Type | Description |
| --- | --- | --- |
| managementZone | [EntityShortRepresentation](#openapi-definition-EntityShortRepresentation) | The short representation of a Dynatrace entity. |
| timeframe | string | The default timeframe of the dashboard. |

#### The `EntityShortRepresentation` object

The short representation of a Dynatrace entity.

| Element | Type | Description |
| --- | --- | --- |
| description | string | A short description of the Dynatrace entity. |
| id | string | The ID of the Dynatrace entity. |
| name | string | The name of the Dynatrace entity. |

#### The `DynamicFilters` object

Dashboard filter configuration of a dashboard.

| Element | Type | Description |
| --- | --- | --- |
| filters | string[] | A set of all possible global dashboard filters that can be applied to a dashboard  Currently supported values are:  ```  OS_TYPE,  SERVICE_TYPE,  DEPLOYMENT_TYPE,  APPLICATION_INJECTION_TYPE,  PAAS_VENDOR_TYPE,  DATABASE_VENDOR,  HOST_VIRTUALIZATION_TYPE,  HOST_MONITORING_MODE,  KUBERNETES_CLUSTER,  RELATED_CLOUD_APPLICATION,  RELATED_NAMESPACE,  SERVICE_TAG_KEY:<tagname>,  HOST_TAG_KEY:<tagname>,  APPLICATION_TAG_KEY:<tagname>,  CUSTOM_DIMENSION:<key>,  PROCESS_GROUP_TAG_KEY:<tagname>,  PROCESS_GROUP_INSTANCE_TAG_KEY:<tagname> ``` |
| genericTagFilters | [DashboardGenericTagFilter[]](#openapi-definition-DashboardGenericTagFilter) | A set of generic tag filters that can be applied to a dashboard |

#### The `DashboardGenericTagFilter` object

Generic tag filters that can be applied to a dashboard.

| Element | Type | Description |
| --- | --- | --- |
| displayName | string | The display name used to identify this generic filter. |
| entityTypes | string[] | Entity types affected by tag. |
| suggestionsFromEntityType | string | The entity type for which the suggestions should be provided. |
| tagKey | string | The tag key for this filter. |

#### The `ConfigurationMetadata` object

Metadata useful for debugging

| Element | Type | Description |
| --- | --- | --- |
| clusterVersion | string | Dynatrace version. |
| configurationVersions | integer[] | A sorted list of the version numbers of the configuration. |
| currentConfigurationVersions | string[] | A sorted list of version numbers of the configuration. |

#### The `Tile` object

Configuration of a tile.

The actual set of fields depends on the type of the tile. Find the list of actual objects in the description of the **tileType** field or see [Dashboards API - Tile JSON modelsï»¿](https://dt-url.net/2wc3spx).

| Element | Type | Description |
| --- | --- | --- |
| bounds | [TileBounds](#openapi-definition-TileBounds) | The position and size of a tile. |
| configured | boolean | The tile is configured and ready to use (`true`) or just placed on the dashboard (`false`). |
| isAutoRefreshDisabled | boolean | The tile auto refresh is disabled. Only works for certain tile types. |
| name | string | The name of the tile. |
| nameSize | string | The size of the tile name. Default value is null. The element can hold these values * `small` * `medium` * `large` |
| tileFilter | [TileFilter](#openapi-definition-TileFilter) | A filter applied to a tile.  It overrides dashboard's filter. |
| tileType | string | Defines the actual set of fields depending on the value. See one of the following objects:  * `DATA_EXPLORER` -> DataExplorerTile * `CUSTOM_CHARTING` -> CustomChartingTile * `DTAQL` -> UserSessionQueryTile * `MARKDOWN` -> MarkdownTile * `IMAGE` -> ImageTile * `HOSTS` -> FilterableEntityTile * `APPLICATIONS` -> FilterableEntityTile * `SERVICES` -> FilterableEntityTile * `DATABASES_OVERVIEW` -> FilterableEntityTile * `SYNTHETIC_TESTS` -> FilterableEntityTile * `APPLICATION_WORLDMAP` -> AssignedEntitiesWithMetricTile * `RESOURCES` -> AssignedEntitiesWithMetricTile * `THIRD_PARTY_MOST_ACTIVE` -> AssignedEntitiesWithMetricTile * `UEM_CONVERSIONS_PER_GOAL` -> AssignedEntitiesWithMetricTile * `HOST` -> AssignedEntitiesWithMetricTile * `PROCESS_GROUPS_ONE` -> AssignedEntitiesWithMetricTile * `SYNTHETIC_SINGLE_WEBCHECK` -> SyntheticSingleWebcheckTile * `APPLICATION` -> AssignedEntitiesTile * `VIRTUALIZATION` -> AssignedEntitiesTile * `AWS` -> AssignedEntitiesTile * `SERVICE_VERSATILE` -> AssignedEntitiesTile * `SESSION_METRICS` -> AssignedEntitiesTile * `USERS` -> AssignedEntitiesTile * `UEM_KEY_USER_ACTIONS` -> AssignedEntitiesTile * `BOUNCE_RATE` -> AssignedEntitiesTile * `UEM_CONVERSIONS_OVERALL` -> AssignedEntitiesTile * `UEM_JSERRORS_OVERALL` -> AssignedEntitiesTile * `MOBILE_APPLICATION` -> AssignedEntitiesTile * `SYNTHETIC_SINGLE_EXT_TEST` -> AssignedEntitiesTile * `SYNTHETIC_HTTP_MONITOR` -> AssignedEntitiesTile * `DATABASE` -> AssignedEntitiesTile * `CUSTOM_APPLICATION` -> AssignedEntitiesTile * `APPLICATION_METHOD` -> AssignedEntitiesTile * `LOG_ANALYTICS` -> AssignedEntitiesTile * `OPENSTACK` -> AssignedEntitiesTile * `OPENSTACK_PROJECT` -> AssignedEntitiesTile * `OPENSTACK_AV_ZONE` -> AssignedEntitiesTile * `DEVICE_APPLICATION_METHOD` -> AssignedEntitiesTile * `DEM_KEY_USER_ACTION` -> AssignedEntitiesTile * `SLO` -> AssignedEntitiesWithMetricTile * `SCALABLE_LIST` -> ScalableListTile * `HEADER` -> Tile * `OPEN_PROBLEMS` -> ProblemTile * `PURE_MODEL` -> Tile * `DOCKER` -> Tile * `NETWORK_MEDIUM` -> Tile * `APPLICATIONS_MOST_ACTIVE` -> Tile * `NETWORK` -> Tile * `UEM_ACTIVE_SESSIONS` -> Tile * `DCRUM_SERVICES` -> Tile The element can hold these values * `APPLICATION` * `APPLICATIONS` * `APPLICATIONS_MOST_ACTIVE` * `APPLICATION_METHOD` * `APPLICATION_WORLDMAP` * `AWS` * `BOUNCE_RATE` * `CUSTOM_APPLICATION` * `CUSTOM_CHARTING` * `DATABASE` * `DATABASES_OVERVIEW` * `DATA_EXPLORER` * `DCRUM_SERVICES` * `DEM_KEY_USER_ACTION` * `DEVICE_APPLICATION_METHOD` * `DOCKER` * `DTAQL` * `HEADER` * `HOST` * `HOSTS` * `IMAGE` * `LOG_ANALYTICS` * `MARKDOWN` * `MOBILE_APPLICATION` * `NETWORK` * `NETWORK_MEDIUM` * `OPENSTACK` * `OPENSTACK_AV_ZONE` * `OPENSTACK_PROJECT` * `OPEN_PROBLEMS` * `PROCESS_GROUPS_ONE` * `PURE_MODEL` * `RESOURCES` * `SCALABLE_LIST` * `SERVICES` * `SERVICE_VERSATILE` * `SESSION_METRICS` * `SLO` * `SYNTHETIC_HTTP_MONITOR` * `SYNTHETIC_SINGLE_EXT_TEST` * `SYNTHETIC_SINGLE_WEBCHECK` * `SYNTHETIC_TESTS` * `THIRD_PARTY_MOST_ACTIVE` * `UEM_ACTIVE_SESSIONS` * `UEM_CONVERSIONS_OVERALL` * `UEM_CONVERSIONS_PER_GOAL` * `UEM_JSERRORS_OVERALL` * `UEM_KEY_USER_ACTIONS` * `USERS` * `VIRTUALIZATION` |

#### The `TileBounds` object

The position and size of a tile.

| Element | Type | Description |
| --- | --- | --- |
| height | integer | The height of the tile, in pixels. |
| left | integer | The horizontal distance from the top left corner of the dashboard to the top left corner of the tile, in pixels. |
| top | integer | The vertical distance from the top left corner of the dashboard to the top left corner of the tile, in pixels. |
| width | integer | The width of the tile, in pixels. |

#### The `TileFilter` object

A filter applied to a tile.

It overrides dashboard's filter.

| Element | Type | Description |
| --- | --- | --- |
| managementZone | [EntityShortRepresentation](#openapi-definition-EntityShortRepresentation) | The short representation of a Dynatrace entity. |
| timeframe | string | The default timeframe of the tile. |

### Response body JSON models

```
{



"dashboardMetadata": {



"dashboardFilter": {



"managementZone": {



"id": "3438779970106539862",



"name": "Example Management Zone"



},



"timeframe": "l_72_HOURS"



},



"dynamicFilters": {



"filters": [



"SERVICE_TYPE"



]



},



"name": "Example Dashboard",



"owner": "Example Owner",



"shared": true



},



"metadata": {



"clusterVersion": "Mock version",



"configurationVersions": [



4,



2



]



},



"tiles": [



{



"bounds": {



"height": 38,



"left": 0,



"top": 0,



"width": 304



},



"configured": true,



"name": "Hosts",



"tileFilter": {},



"tileType": "HEADER"



},



{



"bounds": {



"height": 38,



"left": 304,



"top": 0,



"width": 304



},



"configured": true,



"name": "Applications",



"tileFilter": {},



"tileType": "HEADER"



},



{



"bounds": {



"height": 304,



"left": 0,



"top": 38,



"width": 304



},



"chartVisible": true,



"configured": true,



"name": "Host health",



"tileFilter": {



"managementZone": {



"id": "3438779970106539862",



"name": "Example Management Zone"



}



},



"tileType": "HOSTS"



},



{



"bounds": {



"height": 304,



"left": 304,



"top": 38,



"width": 304



},



"chartVisible": true,



"configured": true,



"name": "Application health",



"tileFilter": {



"managementZone": {



"id": "3438779970106539862",



"name": "Example Management Zone"



}



},



"tileType": "APPLICATIONS"



}



]



}
```

## Example

In this example, the request lists the parameters of the **Sample dashboard**, which has the ID of **2768e6ca-e199-4433-9e0d-2922aec2099b**.

The API token is passed in the **Authorization** header.

The dashboard looks like this in the UI:

![Sample dashboard](https://dt-cdn.net/images/sample-dashboard-651-0530cd435d.png)

#### Curl

```
curl -X GET \



https://mySampleEnv.live.dynatrace.com/api/config/v1/dashboards/2768e6ca-e199-4433-9e0d-2922aec2099b \



-H 'Authorization: Api-Token dt0c01.abc123.abcdefjhij1234567890'
```

#### Request URL

```
https://mySampleEnv.live.dynatrace.com/api/config/v1/dashboards/2768e6ca-e199-4433-9e0d-2922aec2099b
```

#### Response body

```
{



"metadata": {



"clusterVersion": "1.166.0.20190311-110828",



"configurationVersions": [



2



]



},



"id": "2768e6ca-e199-4433-9e0d-2922aec2099b",



"dashboardMetadata": {



"name": "Sample dashboard",



"shared": true,



"owner": "john.smith",



"sharingDetails": {



"linkShared": true,



"published": true



},



"dashboardFilter": {



"timeframe": "l_2_HOURS",



"managementZone": null



}



},



"tiles": [



{



"name": "Host health",



"tileType": "HOSTS",



"configured": true,



"bounds": {



"top": 0,



"left": 304,



"width": 304,



"height": 304



},



"tileFilter": {



"managementZone": {



"id": "9130632296508575249",



"name": "Easytravel"



}



},



"filterConfig": null,



"chartVisible": true



},



{



"name": "User behavior",



"tileType": "SESSION_METRICS",



"configured": true,



"bounds": {



"top": 0,



"left": 0,



"width": 304,



"height": 304



},



"tileFilter": {



"managementZone": null



},



"assignedEntities": [



"APPLICATION-8E41C8C247910758"



]



}



]



}
```

#### Response code

200

## Related topics

* [Dashboards](/managed/analyze-explore-automate/dashboards-classic "Learn how to create, manage, and use Dynatrace Dashboards Classic.")
