---
title: Dynatrace API changelog version 1.338
source: https://docs.dynatrace.com/managed/whats-new/dynatrace-api/sprint-338
scraped: 2026-05-12T11:35:44.224227
---

# Dynatrace API changelog version 1.338

# Dynatrace API changelog version 1.338

* Release notes
* Published Apr 24, 2026
* Rollout start on May 05, 2026

## Environment API v2

### /ua

* `GET /ua/{entityId}/serviceMethods` New Early Access

### /activeGateTokens

* `GET /activeGateTokens`

  + Return Type:

    - Changed 200 OK
      Changed **ActiveGateTokenList** schema (application/json; charset=utf-8)

      * Changed property **activeGateTokens**

        + Removed properties:  
          **empty**
        + Removed properties:  
          **activeGateType**  
          **seedToken**
        + Removed required properties:  
          **activeGateType**
* `POST /activeGateTokens`

  + Request:

    - Changed **ActiveGateTokenCreate** schema (application/json; charset=utf-8)

      * Removed properties:  
        **activeGateType**  
        **seedToken**
      * Removed required properties:  
        **activeGateType**
* `GET /activeGateTokens/{activeGateTokenIdentifier}`

  + Return Type:

    - Changed 200 OK
      Changed **ActiveGateToken** schema (application/json; charset=utf-8)

      * Removed properties:  
        **activeGateType**  
        **seedToken**
      * Removed required properties:  
        **activeGateType**

### /synthetic

* `POST /synthetic/executions/{executionId}`

  + Return Type:

    - Add 200 OK
    - Deleted 201 Created

## Configuration API v1

### /ua

* `POST /ua/entity` Early Access

  + Return Type:

    - Changed 200 OK
      Changed **UAEntityScreenDefinition** schema (application/json; charset=utf-8)

      * Changed property **attributeTables**

        + Changed property **filtering**

          - Changed property **entityFilter**

            * Changed property **entityFilterGroups**

              + Changed property **filters**

                - Added properties:  
                  **minPromptLength**
      * Changed property **entitiesLists**

        + Added properties:  
          **useServiceMethodsEndpoint**
        + Changed property **filtering**

          - Changed property **entityFilter**

            * Changed property **entityFilterGroups**

              + Changed property **filters**

                - Added properties:  
                  **minPromptLength**
      * Changed property **filter**

        + Changed property **entityFilter**

          - Changed property **entityFilterGroups**

            * Changed property **filters**

              + Added properties:  
                **minPromptLength**
      * Changed property **metricTables**

        + Changed property **filtering**

          - Changed property **entityFilter**

            * Changed property **entityFilterGroups**

              + Changed property **filters**

                - Added properties:  
                  **minPromptLength**
* `POST /ua/list` Early Access

  + Return Type:

    - Changed 200 OK
      Changed **UAListScreenDefinition** schema (application/json; charset=utf-8)

      * Changed property **entitiesLists**

        + Added properties:  
          **useServiceMethodsEndpoint**
        + Changed property **filtering**

          - Changed property **entityFilter**

            * Changed property **entityFilterGroups**

              + Changed property **filters**

                - Added properties:  
                  **minPromptLength**
      * Changed property **filter**

        + Changed property **entityFilter**

          - Changed property **entityFilterGroups**

            * Changed property **filters**

              + Added properties:  
                **minPromptLength**

### /allowedBeaconOriginsForCors

* `GET /allowedBeaconOriginsForCors` Deprecated
* `PUT /allowedBeaconOriginsForCors` Deprecated
* `POST /allowedBeaconOriginsForCors/validator` Deprecated

### /anomalyDetection

* `GET /anomalyDetection/applications` Deprecated
* `PUT /anomalyDetection/applications` Deprecated
* `POST /anomalyDetection/applications/validator` Deprecated
* `GET /anomalyDetection/aws` Deprecated
* `PUT /anomalyDetection/aws` Deprecated
* `POST /anomalyDetection/aws/validator` Deprecated
* `GET /anomalyDetection/databaseServices` Deprecated
* `PUT /anomalyDetection/databaseServices` Deprecated
* `POST /anomalyDetection/databaseServices/validator` Deprecated
* `GET /anomalyDetection/diskEvents` Deprecated Early Access
* `POST /anomalyDetection/diskEvents` Deprecated Early Access
* `POST /anomalyDetection/diskEvents/validator` Deprecated Early Access
* `GET /anomalyDetection/diskEvents/{id}` Deprecated Early Access
* `PUT /anomalyDetection/diskEvents/{id}` Deprecated Early Access
* `DELETE /anomalyDetection/diskEvents/{id}` Deprecated Early Access
* `POST /anomalyDetection/diskEvents/{id}/validator` Deprecated Early Access
* `GET /anomalyDetection/hosts` Deprecated
* `PUT /anomalyDetection/hosts` Deprecated
* `POST /anomalyDetection/hosts/validator` Deprecated
* `GET /anomalyDetection/processGroups/{id}` Deprecated Early Access
* `PUT /anomalyDetection/processGroups/{id}` Deprecated Early Access
* `DELETE /anomalyDetection/processGroups/{id}` Deprecated Early Access
* `POST /anomalyDetection/processGroups/{id}/validator` Deprecated Early Access
* `GET /anomalyDetection/services` Deprecated
* `PUT /anomalyDetection/services` Deprecated
* `POST /anomalyDetection/services/validator` Deprecated
* `GET /anomalyDetection/vmware` Deprecated
* `PUT /anomalyDetection/vmware` Deprecated
* `POST /anomalyDetection/vmware/validator` Deprecated

### /applicationDetectionRules

* `GET /applicationDetectionRules` Deprecated
* `POST /applicationDetectionRules` Deprecated
* `GET /applicationDetectionRules/hostDetection` Deprecated
* `PUT /applicationDetectionRules/hostDetection` Deprecated
* `POST /applicationDetectionRules/hostDetection/validator` Deprecated
* `PUT /applicationDetectionRules/order` Deprecated
* `POST /applicationDetectionRules/validator` Deprecated
* `GET /applicationDetectionRules/{id}` Deprecated
* `PUT /applicationDetectionRules/{id}` Deprecated
* `DELETE /applicationDetectionRules/{id}` Deprecated
* `POST /applicationDetectionRules/{id}/validator` Deprecated

### /contentResources

* `GET /contentResources` Deprecated
* `PUT /contentResources` Deprecated
* `POST /contentResources/validator` Deprecated

### /dataPrivacy

* `GET /dataPrivacy` Deprecated
* `PUT /dataPrivacy` Deprecated
* `POST /dataPrivacy/validator` Deprecated

### /geographicRegions

* `GET /geographicRegions/ipAddressMappings` Deprecated
* `PUT /geographicRegions/ipAddressMappings` Deprecated
* `POST /geographicRegions/ipAddressMappings/validator` Deprecated
* `GET /geographicRegions/ipDetectionHeaders` Deprecated
* `PUT /geographicRegions/ipDetectionHeaders` Deprecated
* `POST /geographicRegions/ipDetectionHeaders/validator` Deprecated

### /hostgroups

* `GET /hostgroups/{id}` Deprecated
* `GET /hostgroups/{id}/autoupdate` Deprecated
* `PUT /hostgroups/{id}/autoupdate` Deprecated
* `POST /hostgroups/{id}/autoupdate/validator` Deprecated

### /hosts

* `GET /hosts/autoupdate` Deprecated
* `PUT /hosts/autoupdate` Deprecated
* `POST /hosts/autoupdate/validator` Deprecated
* `GET /hosts/{id}` Deprecated
* `GET /hosts/{id}/autoupdate` Deprecated
* `PUT /hosts/{id}/autoupdate` Deprecated
* `POST /hosts/{id}/autoupdate/validator` Deprecated
* `GET /hosts/{id}/technologies` Deprecated

### /technologies

* `GET /technologies` Deprecated

### /extensions

* `GET /extensions/{technology}/availableHosts` Early Access

  + Parameter:

    - Changed **technology** in path

      * Added enum values:  
        `R2DBC`
      * Removed enum values:  
        `DOCKERDEAMON`  
        `MONGODB_ROUTER`  
        `OPENSTACK`

### /service

* `POST /service/requestAttributes`

  + Request:

    - Changed **RequestAttribute** schema (application/json; charset=utf-8)

      * Changed property **dataSources**

        + Changed property **scope**

          - Changed property **serviceTechnology**

            * Added enum values:  
              `R2DBC`
            * Removed enum values:  
              `DOCKERDEAMON`  
              `MONGODB_ROUTER`  
              `OPENSTACK`
* `POST /service/requestAttributes/validator`

  + Request:

    - Changed **RequestAttribute** schema (application/json; charset=utf-8)

      * Changed property **dataSources**

        + Changed property **scope**

          - Changed property **serviceTechnology**

            * Added enum values:  
              `R2DBC`
            * Removed enum values:  
              `DOCKERDEAMON`  
              `MONGODB_ROUTER`  
              `OPENSTACK`
* `GET /service/requestAttributes/{id}`

  + Return Type:

    - Changed 200 OK
      Changed **RequestAttribute** schema (application/json; charset=utf-8)

      * Changed property **dataSources**

        + Changed property **scope**

          - Changed property **serviceTechnology**

            * Added enum values:  
              `R2DBC`
            * Removed enum values:  
              `DOCKERDEAMON`  
              `MONGODB_ROUTER`  
              `OPENSTACK`
* `PUT /service/requestAttributes/{id}`

  + Request:

    - Changed **RequestAttribute** schema (application/json; charset=utf-8)

      * Changed property **dataSources**

        + Changed property **scope**

          - Changed property **serviceTechnology**

            * Added enum values:  
              `R2DBC`
            * Removed enum values:  
              `DOCKERDEAMON`  
              `MONGODB_ROUTER`  
              `OPENSTACK`
* `POST /service/requestAttributes/{id}/validator`

  + Request:

    - Changed **RequestAttribute** schema (application/json; charset=utf-8)

      * Changed property **dataSources**

        + Changed property **scope**

          - Changed property **serviceTechnology**

            * Added enum values:  
              `R2DBC`
            * Removed enum values:  
              `DOCKERDEAMON`  
              `MONGODB_ROUTER`  
              `OPENSTACK`

## Cluster API v1

### /cluster

* `POST /cluster/verifyConnectionToMC` New
* `GET /cluster/verifyConnectionToMC/{requestId}` New

## Cluster API v2

### /iam

* `GET /iam/resolution/{level-type}/{level-id}/descendants/effectivepermissions`

  + Parameter:

    - Changed **entity\_id** in query

      * Pattern changed from null to `^[^{}]+$`
* `GET /iam/resolution/{level-type}/{level-id}/effectivepermissions`

  + Parameter:

    - Changed **entity\_id** in query

      * Pattern changed from null to `^[^{}]+$`