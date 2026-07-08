---
title: Dynatrace API changelog version 1.340
source: https://docs.dynatrace.com/managed/whats-new/dynatrace-api/sprint-340
---

# Dynatrace API changelog version 1.340

# Dynatrace API changelog version 1.340

* Release notes
* Updated on Jun 02, 2026
* Rollout start on Jun 02, 2026

## Environment API v1

### /synthetic/monitors

The following endpoints are deprecated:

* `GET /synthetic/monitors` Deprecated
* `POST /synthetic/monitors` Deprecated
* `GET /synthetic/monitors/{monitorId}` Deprecated
* `PUT /synthetic/monitors/{monitorId}` Deprecated
* `DELETE /synthetic/monitors/{monitorId}` Deprecated

### /tokens

* `GET /tokens`

  + Parameter:

    - Changed **permissions** in query

      * Added enum values:  
        `extensionDiscoveryPmi.read`
* `POST /tokens`

  + Request:

    - Changed **CreateToken** schema (application/json; charset=utf-8)

      * Changed property **scopes**

        + Added enum values:  
          `extensionDiscoveryPmi.read`
* `POST /tokens/lookup`

  + Return Type:

    - Changed 200 OK
      Changed **TokenMetadata** schema (application/json; charset=utf-8)

      * Changed property **scopes**

        + Added enum values:  
          `extensionDiscoveryPmi.read`
* `GET /tokens/{id}`

  + Return Type:

    - Changed 200 OK
      Changed **TokenMetadata** schema (application/json; charset=utf-8)

      * Changed property **scopes**

        + Added enum values:  
          `extensionDiscoveryPmi.read`
* `PUT /tokens/{id}`

  + Request:

    - Changed **UpdateToken** schema (application/json; charset=utf-8)

      * Changed property **scopes**

        + Added enum values:  
          `extensionDiscoveryPmi.read`

## Environment API v2

### /activeGates

The following endpoints are deprecated:

* `GET /activeGates/autoUpdate` Deprecated
* `PUT /activeGates/autoUpdate` Deprecated
* `POST /activeGates/autoUpdate/validator` Deprecated
* `GET /activeGates/{agId}/autoUpdate` Deprecated
* `PUT /activeGates/{agId}/autoUpdate` Deprecated
* `POST /activeGates/{agId}/autoUpdate/validator` Deprecated

### /networkZones

The following endpoints are deprecated:

* `PUT /networkZones/{id}` Deprecated
* `DELETE /networkZones/{id}` Deprecated

### /apiTokens

* `GET /apiTokens`

  + Return Type:

    - Changed 200 OK
      Changed **ApiTokenList** schema (application/json; charset=utf-8)

      * Changed property **apiTokens**

        + Changed property **scopes**

          - Added enum values:  
            `extensionDiscoveryPmi.read`
* `POST /apiTokens`

  + Request:

    - Changed **ApiTokenCreate** schema (application/json; charset=utf-8)

      * Changed property **scopes**

        + Added enum values:  
          `extensionDiscoveryPmi.read`
* `POST /apiTokens/lookup`

  + Return Type:

    - Changed 200 OK
      Changed **ApiToken** schema (application/json; charset=utf-8)

      * Changed property **scopes**

        + Added enum values:  
          `extensionDiscoveryPmi.read`
* `GET /apiTokens/{id}`

  + Return Type:

    - Changed 200 OK
      Changed **ApiToken** schema (application/json; charset=utf-8)

      * Changed property **scopes**

        + Added enum values:  
          `extensionDiscoveryPmi.read`
* `PUT /apiTokens/{id}`

  + Request:

    - Changed **ApiTokenUpdate** schema (application/json; charset=utf-8)

      * Changed property **scopes**

        + Added enum values:  
          `extensionDiscoveryPmi.read`

### /extensions

* `GET /extensions/discovery/pmi/processes` Early Access

  + API maturity changed from `IN_DEVELOPMENT` to `EARLY_ADOPTER`
* `GET /extensions/discovery/pmi/processes/{process-id}` Early Access

  + API maturity changed from `IN_DEVELOPMENT` to `EARLY_ADOPTER`

## Configuration API

### /calculatedMetrics

* `POST /calculatedMetrics/service`

  + Request:

    - Changed **CalculatedServiceMetric** schema (application/json; charset=utf-8)

      * Broken compatibility
      * Changed property **dimensionDefinition**

        + Changed property **placeholders**

          - Changed property **source**

            * Changed property **serviceTag**

              + Type changed from `object` to `null`
* `POST /calculatedMetrics/service/validator`

  + Request:

    - Changed **CalculatedServiceMetric** schema (application/json; charset=utf-8)

      * Broken compatibility
      * Changed property **dimensionDefinition**

        + Changed property **placeholders**

          - Changed property **source**

            * Changed property **serviceTag**

              + Type changed from `object` to `null`
* `GET /calculatedMetrics/service/{metricKey}`

  + Return Type:

    - Changed 200 OK
      Changed **CalculatedServiceMetric** schema (application/json; charset=utf-8)

      * Broken compatibility
      * Changed property **dimensionDefinition**

        + Changed property **placeholders**

          - Changed property **source**

            * Changed property **serviceTag**

              + Type changed from `object` to `null`
* `PUT /calculatedMetrics/service/{metricKey}`

  + Request:

    - Changed **CalculatedServiceMetric** schema (application/json; charset=utf-8)

      * Broken compatibility
      * Changed property **dimensionDefinition**

        + Changed property **placeholders**

          - Changed property **source**

            * Changed property **serviceTag**

              + Type changed from `object` to `null`
* `POST /calculatedMetrics/service/{metricKey}/validator`

  + Request:

    - Changed **CalculatedServiceMetric** schema (application/json; charset=utf-8)

      * Broken compatibility
      * Changed property **dimensionDefinition**

        + Changed property **placeholders**

          - Changed property **source**

            * Changed property **serviceTag**

              + Type changed from `object` to `null`

### /service

* `POST /service/requestNaming`

  + Request:

    - Changed **RequestNaming** schema (application/json; charset=utf-8)

      * Broken compatibility
      * Changed property **placeholders**

        + Changed property **source**

          - Changed property **serviceTag**

            * Type changed from `object` to `null`
* `POST /service/requestNaming/validator`

  + Request:

    - Changed **RequestNaming** schema (application/json; charset=utf-8)

      * Broken compatibility
      * Changed property **placeholders**

        + Changed property **source**

          - Changed property **serviceTag**

            * Type changed from `object` to `null`
* `GET /service/requestNaming/{id}`

  + Return Type:

    - Changed 200 OK
      Changed **RequestNaming** schema (application/json; charset=utf-8)

      * Broken compatibility
      * Changed property **placeholders**

        + Changed property **source**

          - Changed property **serviceTag**

            * Type changed from `object` to `null`
* `PUT /service/requestNaming/{id}`

  + Request:

    - Changed **RequestNaming** schema (application/json; charset=utf-8)

      * Broken compatibility
      * Changed property **placeholders**

        + Changed property **source**

          - Changed property **serviceTag**

            * Type changed from `object` to `null`
* `POST /service/requestNaming/{id}/validator`

  + Request:

    - Changed **RequestNaming** schema (application/json; charset=utf-8)

      * Broken compatibility
      * Changed property **placeholders**

        + Changed property **source**

          - Changed property **serviceTag**

            * Type changed from `object` to `null`

## Cluster API v1

### /multiDc/migration

* `GET /multiDc/migration/clusterState` Early Access

  + Return Type:

    - Changed 200 OK
      Changed **SingleToMultiDcMigrationClusterState** schema (application/json)

      * Changed property **migrationSteps**

        + Changed schema of dictionary value:

          - Changed property **status**

            * Added enum values:  
              `DC_RECOVERY`
      * Changed property **singleToMultiDcMigration**

        + Changed property **status**

          - Added enum values:  
            `DC_RECOVERY`
* `PUT /multiDc/migration/clusterState` Early Access

  + Parameter:

    - Changed **status** in query

      * Added enum values:  
        `DC_RECOVERY`
* `GET /multiDc/migration/clusterState/{subStep}` Early Access

  + Return Type:

    - Changed 200 OK
      Changed **MigrationState** schema (application/json)

      * Changed property **status**

        + Added enum values:  
          `DC_RECOVERY`
* `PUT /multiDc/migration/clusterState/{subStep}` Early Access

  + Parameter:

    - Changed **status** in query

      * Added enum values:  
        `DC_RECOVERY`
* `GET /multiDc/migration/inServerconfigState` Early Access

  + Return Type:

    - Changed 200 OK
      Changed **InServerConfigDatacenterMigrationState** schema (application/json)

      * Changed property **componentMigrationStates**

        + Changed schema of dictionary value:

          - Changed property **status**

            * Added enum values:  
              `DC_RECOVERY`

### /upgradeManagement

* `GET /upgradeManagement/installationFiles`

  + Return Type:

    - Changed 200 OK
      Changed null schema (application/json; charset=utf-8)

      * Added properties:  
        **countOfTenantsUsingThisAsTargetVersion**

## Cluster API v2

### /activeGates

The following endpoints are deprecated:

* `GET /activeGates/autoUpdate/{envId}` Deprecated
* `PUT /activeGates/autoUpdate/{envId}` Deprecated
* `POST /activeGates/autoUpdate/{envId}/validator` Deprecated

### /environments

* `GET /environments`

  + Return Type:

    - Changed 200 OK
      Changed **EnvironmentList** schema (application/json; charset=utf-8)

      * Changed property **environments**

        + Changed property **storage**

          - Added properties:  
            **logMonitoringV2Retention**  
            **logMonitoringV2Storage**
* `POST /environments`

  + Request:

    - Changed **Environment** schema (application/json; charset=utf-8)

      * Changed property **storage**

        + Added properties:  
          `logMonitoringV2Retention`
          `logMonitoringV2Storage`
* `GET /environments/{id}`

  + Return Type:

    - Changed 200 OK
      Changed **Environment** schema (application/json; charset=utf-8)

      * Changed property **storage**

        + Added properties:  
          `logMonitoringV2Retention`
          `logMonitoringV2Storage`
* `PUT /environments/{id}`

  + Request:

    - Changed **Environment** schema (application/json; charset=utf-8)

      * Changed property **storage**

        + Added properties:  
          `logMonitoringV2Retention`
          `logMonitoringV2Storage`

### /iam

Reverts a change introduced in [API version 1.338](/managed/whats-new/dynatrace-api/sprint-338 "Changelog for Dynatrace API version 1.338").

* `GET /iam/resolution/{level-type}/{level-id}/descendants/effectivepermissions`

  + Parameter:

    - Changed **entity\_id** in query

      * Pattern changed from `^[^{}]+$` to `null`
* `GET /iam/resolution/{level-type}/{level-id}/effectivepermissions`

  + Parameter:

    - Changed **entity\_id** in query

      * Pattern changed from `^[^{}]+$` to `null`