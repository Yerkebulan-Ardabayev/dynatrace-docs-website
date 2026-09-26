---
title: Dynatrace API changelog version 1.348
source: https://docs.dynatrace.com/managed/whats-new/dynatrace-api/sprint-348
---

# Dynatrace API changelog version 1.348

# Dynatrace API changelog version 1.348

* Release notes
* Published Sep 09, 2026
* Rollout start on Sep 22, 2026 (planned)

Pre-release information

This is an ongoing summary of changes in this planned release. Check back here at GA for the final version.

## Environment API v2

### /apiTokens

The following endpoints are deprecated:

* `GET /apiTokens` Deprecated
* `POST /apiTokens` Deprecated
* `POST /apiTokens/lookup` Deprecated
* `GET /apiTokens/{id}` Deprecated
* `PUT /apiTokens/{id}` Deprecated
* `DELETE /apiTokens/{id}` Deprecated

### /fleetManagement

* `GET /fleetManagement/components/containerImages`

  + Return Type:

    - Changed 200 OK
      Changed **ContainerImageData** schema (application/json; charset=utf-8)

      * Changed property **components**

        + Changed property **type**

          - Added enum values:  
            `ncc`  
            `otel-collector`  
            `target-allocator`  
            `edge-connect`

### /synthetic

* `GET /synthetic/config` Early Access

  + Return Type:

    - Changed 200 OK
      Changed **SyntheticConfigDto** schema (application/json; charset=utf-8)

      * Added property **maintenanceWindowsExcludedFromAvailability**
      * Added required property **maintenanceWindowsExcludedFromAvailability**
* `PUT /synthetic/config` Early Access

  + Request:

    - Changed **SyntheticConfigDto** schema (application/json; charset=utf-8)

      * Added property **maintenanceWindowsExcludedFromAvailability**
  + Return Type:

    - Changed 204 No Content

      * Removed media type: application/json; charset=utf-8
* `POST /synthetic/locations`

  + Request:

    - Changed **PrivateSyntheticLocation** schema (application/json; charset=utf-8)

      * Removed required property **nodes**
* `GET /synthetic/monitors` Early Access

  + Return Type:

    - Changed 200 OK
      Changed **SyntheticMonitorListDto** schema (application/json; charset=utf-8)

      * Changed property **monitors**

        + Added property **externalId**

## Configuration API v1

### /autoTags

* `POST /autoTags`

  + Request:

    - Changed **AutoTag** schema (application/json; charset=utf-8)

      * Changed property **rules**

        + Changed property **conditions**

          - Changed property **key**

            * Changed property **attribute**

              + Added enum values:  
                `GROUP_RESOURCE_ATTRIBUTES`  
                `RESOURCE_ATTRIBUTES`
* `POST /autoTags/validator`

  + Request:

    - Changed **AutoTag** schema (application/json; charset=utf-8)

      * Changed property **rules**

        + Changed property **conditions**

          - Changed property **key**

            * Changed property **attribute**

              + Added enum values:  
                `GROUP_RESOURCE_ATTRIBUTES`  
                `RESOURCE_ATTRIBUTES`
* `GET /autoTags/{id}`

  + Return Type:

    - Changed 200 OK
      Changed **AutoTag** schema (application/json; charset=utf-8)

      * Changed property **rules**

        + Changed property **conditions**

          - Changed property **key**

            * Changed property **attribute**

              + Added enum values:  
                `GROUP_RESOURCE_ATTRIBUTES`  
                `RESOURCE_ATTRIBUTES`
* `PUT /autoTags/{id}`

  + Request:

    - Changed **AutoTag** schema (application/json; charset=utf-8)

      * Changed property **rules**

        + Changed property **conditions**

          - Changed property **key**

            * Changed property **attribute**

              + Added enum values:  
                `GROUP_RESOURCE_ATTRIBUTES`  
                `RESOURCE_ATTRIBUTES`
* `POST /autoTags/{id}/validator`

  + Request:

    - Changed **AutoTag** schema (application/json; charset=utf-8)

      * Changed property **rules**

        + Changed property **conditions**

          - Changed property **key**

            * Changed property **attribute**

              + Added enum values:  
                `GROUP_RESOURCE_ATTRIBUTES`  
                `RESOURCE_ATTRIBUTES`

### /conditionalNaming

* `POST /conditionalNaming/{type}`

  + Request:

    - Changed **ConditionalNamingRule** schema (application/json; charset=utf-8)

      * Changed property **rules**

        + Changed property **key**

          - Changed property **attribute**

            * Added enum values:  
              `GROUP_RESOURCE_ATTRIBUTES`  
              `RESOURCE_ATTRIBUTES`
* `POST /conditionalNaming/{type}/validator`

  + Request:

    - Changed **ConditionalNamingRule** schema (application/json; charset=utf-8)

      * Changed property **rules**

        + Changed property **key**

          - Changed property **attribute**

            * Added enum values:  
              `GROUP_RESOURCE_ATTRIBUTES`  
              `RESOURCE_ATTRIBUTES`
* `GET /conditionalNaming/{type}/{id}`

  + Return Type:

    - Changed 200 OK
      Changed **ConditionalNamingRule** schema (application/json; charset=utf-8)

      * Changed property **rules**

        + Changed property **key**

          - Changed property **attribute**

            * Added enum values:  
              `GROUP_RESOURCE_ATTRIBUTES`  
              `RESOURCE_ATTRIBUTES`
* `PUT /conditionalNaming/{type}/{id}`

  + Request:

    - Changed **ConditionalNamingRule** schema (application/json; charset=utf-8)

      * Changed property **rules**

        + Changed property **key**

          - Changed property **attribute**

            * Added enum values:  
              `GROUP_RESOURCE_ATTRIBUTES`  
              `RESOURCE_ATTRIBUTES`
* `POST /conditionalNaming/{type}/{id}/validator`

  + Request:

    - Changed **ConditionalNamingRule** schema (application/json; charset=utf-8)

      * Changed property **rules**

        + Changed property **key**

          - Changed property **attribute**

            * Added enum values:  
              `GROUP_RESOURCE_ATTRIBUTES`  
              `RESOURCE_ATTRIBUTES`

### /managementZones

* `POST /managementZones`

  + Request:

    - Changed **ManagementZone** schema (application/json; charset=utf-8)

      * Changed property **rules**

        + Changed property **conditions**

          - Changed property **key**

            * Changed property **attribute**

              + Added enum values:  
                `GROUP_RESOURCE_ATTRIBUTES`  
                `RESOURCE_ATTRIBUTES`
* `POST /managementZones/validator`

  + Request:

    - Changed **ManagementZone** schema (application/json; charset=utf-8)

      * Changed property **rules**

        + Changed property **conditions**

          - Changed property **key**

            * Changed property **attribute**

              + Added enum values:  
                `GROUP_RESOURCE_ATTRIBUTES`  
                `RESOURCE_ATTRIBUTES`
* `GET /managementZones/{id}`

  + Return Type:

    - Changed 200 OK
      Changed **ManagementZone** schema (application/json; charset=utf-8)

      * Changed property **rules**

        + Changed property **conditions**

          - Changed property **key**

            * Changed property **attribute**

              + Added enum values:  
                `GROUP_RESOURCE_ATTRIBUTES`  
                `RESOURCE_ATTRIBUTES`
* `PUT /managementZones/{id}`

  + Request:

    - Changed **ManagementZone** schema (application/json; charset=utf-8)

      * Changed property **rules**

        + Changed property **conditions**

          - Changed property **key**

            * Changed property **attribute**

              + Added enum values:  
                `GROUP_RESOURCE_ATTRIBUTES`  
                `RESOURCE_ATTRIBUTES`
* `POST /managementZones/{id}/validator`

  + Request:

    - Changed **ManagementZone** schema (application/json; charset=utf-8)

      * Changed property **rules**

        + Changed property **conditions**

          - Changed property **key**

            * Changed property **attribute**

              + Added enum values:  
                `GROUP_RESOURCE_ATTRIBUTES`  
                `RESOURCE_ATTRIBUTES`