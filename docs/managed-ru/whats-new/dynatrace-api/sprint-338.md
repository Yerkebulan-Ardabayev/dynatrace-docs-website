---
title: Журнал изменений Dynatrace API версии 1.338
source: https://docs.dynatrace.com/managed/whats-new/dynatrace-api/sprint-338
scraped: 2026-05-12T11:35:44.224227
---

# Журнал изменений Dynatrace API версии 1.338

# Журнал изменений Dynatrace API версии 1.338

* Заметки о выпуске
* Published Apr 24, 2026
* Rollout start on May 05, 2026

## Environment API v2

### /ua

* `GET /ua/{entityId}/serviceMethods` Новый Early Access

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

* `GET /allowedBeaconOriginsForCors` Объявлено устаревшим
* `PUT /allowedBeaconOriginsForCors` Объявлено устаревшим
* `POST /allowedBeaconOriginsForCors/validator` Объявлено устаревшим

### /anomalyDetection

* `GET /anomalyDetection/applications` Объявлено устаревшим
* `PUT /anomalyDetection/applications` Объявлено устаревшим
* `POST /anomalyDetection/applications/validator` Объявлено устаревшим
* `GET /anomalyDetection/aws` Объявлено устаревшим
* `PUT /anomalyDetection/aws` Объявлено устаревшим
* `POST /anomalyDetection/aws/validator` Объявлено устаревшим
* `GET /anomalyDetection/databaseServices` Объявлено устаревшим
* `PUT /anomalyDetection/databaseServices` Объявлено устаревшим
* `POST /anomalyDetection/databaseServices/validator` Объявлено устаревшим
* `GET /anomalyDetection/diskEvents` Объявлено устаревшим Early Access
* `POST /anomalyDetection/diskEvents` Объявлено устаревшим Early Access
* `POST /anomalyDetection/diskEvents/validator` Объявлено устаревшим Early Access
* `GET /anomalyDetection/diskEvents/{id}` Объявлено устаревшим Early Access
* `PUT /anomalyDetection/diskEvents/{id}` Объявлено устаревшим Early Access
* `DELETE /anomalyDetection/diskEvents/{id}` Объявлено устаревшим Early Access
* `POST /anomalyDetection/diskEvents/{id}/validator` Объявлено устаревшим Early Access
* `GET /anomalyDetection/hosts` Объявлено устаревшим
* `PUT /anomalyDetection/hosts` Объявлено устаревшим
* `POST /anomalyDetection/hosts/validator` Объявлено устаревшим
* `GET /anomalyDetection/processGroups/{id}` Объявлено устаревшим Early Access
* `PUT /anomalyDetection/processGroups/{id}` Объявлено устаревшим Early Access
* `DELETE /anomalyDetection/processGroups/{id}` Объявлено устаревшим Early Access
* `POST /anomalyDetection/processGroups/{id}/validator` Объявлено устаревшим Early Access
* `GET /anomalyDetection/services` Объявлено устаревшим
* `PUT /anomalyDetection/services` Объявлено устаревшим
* `POST /anomalyDetection/services/validator` Объявлено устаревшим
* `GET /anomalyDetection/vmware` Объявлено устаревшим
* `PUT /anomalyDetection/vmware` Объявлено устаревшим
* `POST /anomalyDetection/vmware/validator` Объявлено устаревшим

### /applicationDetectionRules

* `GET /applicationDetectionRules` Объявлено устаревшим
* `POST /applicationDetectionRules` Объявлено устаревшим
* `GET /applicationDetectionRules/hostDetection` Объявлено устаревшим
* `PUT /applicationDetectionRules/hostDetection` Объявлено устаревшим
* `POST /applicationDetectionRules/hostDetection/validator` Объявлено устаревшим
* `PUT /applicationDetectionRules/order` Объявлено устаревшим
* `POST /applicationDetectionRules/validator` Объявлено устаревшим
* `GET /applicationDetectionRules/{id}` Объявлено устаревшим
* `PUT /applicationDetectionRules/{id}` Объявлено устаревшим
* `DELETE /applicationDetectionRules/{id}` Объявлено устаревшим
* `POST /applicationDetectionRules/{id}/validator` Объявлено устаревшим

### /contentResources

* `GET /contentResources` Объявлено устаревшим
* `PUT /contentResources` Объявлено устаревшим
* `POST /contentResources/validator` Объявлено устаревшим

### /dataPrivacy

* `GET /dataPrivacy` Объявлено устаревшим
* `PUT /dataPrivacy` Объявлено устаревшим
* `POST /dataPrivacy/validator` Объявлено устаревшим

### /geographicRegions

* `GET /geographicRegions/ipAddressMappings` Объявлено устаревшим
* `PUT /geographicRegions/ipAddressMappings` Объявлено устаревшим
* `POST /geographicRegions/ipAddressMappings/validator` Объявлено устаревшим
* `GET /geographicRegions/ipDetectionHeaders` Объявлено устаревшим
* `PUT /geographicRegions/ipDetectionHeaders` Объявлено устаревшим
* `POST /geographicRegions/ipDetectionHeaders/validator` Объявлено устаревшим

### /hostgroups

* `GET /hostgroups/{id}` Объявлено устаревшим
* `GET /hostgroups/{id}/autoupdate` Объявлено устаревшим
* `PUT /hostgroups/{id}/autoupdate` Объявлено устаревшим
* `POST /hostgroups/{id}/autoupdate/validator` Объявлено устаревшим

### /hosts

* `GET /hosts/autoupdate` Объявлено устаревшим
* `PUT /hosts/autoupdate` Объявлено устаревшим
* `POST /hosts/autoupdate/validator` Объявлено устаревшим
* `GET /hosts/{id}` Объявлено устаревшим
* `GET /hosts/{id}/autoupdate` Объявлено устаревшим
* `PUT /hosts/{id}/autoupdate` Объявлено устаревшим
* `POST /hosts/{id}/autoupdate/validator` Объявлено устаревшим
* `GET /hosts/{id}/technologies` Объявлено устаревшим

### /technologies

* `GET /technologies` Объявлено устаревшим

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

* `POST /cluster/verifyConnectionToMC` Новый
* `GET /cluster/verifyConnectionToMC/{requestId}` Новый

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