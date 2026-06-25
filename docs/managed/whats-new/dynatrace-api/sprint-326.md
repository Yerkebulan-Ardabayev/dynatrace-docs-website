---
title: Dynatrace API changelog version 1.326
source: https://docs.dynatrace.com/managed/whats-new/dynatrace-api/sprint-326
scraped: 2026-05-12T11:35:25.836172
---

# Dynatrace API changelog version 1.326

# Dynatrace API changelog version 1.326

* Release notes
* Published Oct 08, 2025
* Rollout start on Oct 21, 2025

## Environment API

### /extensions

* `GET /extensions/{extensionName}/environmentConfiguration/assets`

  Return Type:

  + Changed 200 OK
    Changed **ExtensionAssetsDto** schema (application/json; charset=utf-8)

    - Changed property **assets**

      * Changed property **type**

        + Added enum value:  
          `OPEN_PIPELINE`

### /metrics

New possible endpoint:

* `DELETE /metrics`

### /rum

The API maturity of the following has been changed from **EARLY\_ADOPTER** to **GENERAL\_AVAILABILITY**

* `GET /rum/inlineCode/{applicationId}`
* `GET /rum/javaScriptTag/{applicationId}`
* `GET /rum/oneAgentJavaScriptTag/{applicationId}`
* `GET /rum/oneAgentJavaScriptTagWithSri/{applicationId}`

Deprecated:

* `GET /rum/jsInlineScript/{entity}`
* `GET /rum/jsTag/{entity}`
* `GET /rum/jsTagComplete/{entity}`
* `GET /rum/jsTagSri/{entity}`

### /settings/history

* `GET /settings/history`

  Return Type:

  + Changed 200 OK
    Changed **RevisionDiffPage** schema (application/json; charset=utf-8)

    - Changed property **items**

      * Changed property **modificationInfo**

        + Added property:  
          **lastModifiedReason**

### /synthetic

* `GET /synthetic/locations/commands/apply` (EARLY\_ADOPTER)

  Parameter:

  + Added `fipsMode` in query
  + Added `squidProxyConfig` in query

## Cluster API

### /activeGates

* `POST /activeGates/remoteConfigurationManagement`

  Return Type:

  + Changed 201 Created
    Changed **RemoteConfigurationManagementJob** schema (application/json; charset=utf-8)

    - Added property:  
      **inProgressEntities**
* `GET /activeGates/remoteConfigurationManagement/current`

  Return Type:

  + Changed 200 OK
    Changed **RemoteConfigurationManagementJob** schema (application/json; charset=utf-8)

    - Added property:  
      **inProgressEntities**
* `GET /activeGates/remoteConfigurationManagement/{id}`

  Return Type:

  + Changed 200 OK
    Changed **RemoteConfigurationManagementJob** schema (application/json; charset=utf-8)

    - Added property:  
      **inProgressEntities**

### /clusterLicense

New:

* `GET /clusterLicense`
* `GET /clusterLicense/environment/total`
* `POST /clusterLicense/key`

### /environments

* GET /environments

  Return Type:

  + Changed 200 OK
    Changed **EnvironmentList** schema (application/json; charset=utf-8)
    Broken compatibility

    - Changed property **environments**

      * Changed property **storage**

        + Removed properties:  
          **logMonitoringRetention**  
          **logMonitoringStorage**
* POST /environments

  Request:

  Changed **Environment** schema (application/json; charset=utf-8)

  + Changed property **storage**

    - Removed properties:  
      **logMonitoringRetention**  
      **logMonitoringStorage**
* GET /environments/{id}

  Return Type:

  + Changed 200 OK
    Changed **Environment** schema (application/json; charset=utf-8)
    Broken compatibility

    - Changed property **storage**

      * Removed properties:  
        **logMonitoringRetention**  
        **logMonitoringStorage**
* PUT /environments/{id}

  Request:

  Changed **Environment** schema (application/json; charset=utf-8)

  + Changed property **storage**

    - Removed properties:  
      **logMonitoringRetention**  
      **logMonitoringStorage**

### /iam/repo

* `GET /iam/repo/{level-type}/{level-id}/policies`

  Parameter:

  + Changed categories in query

    - Added enum value:  
      `INTEGRATIONS`

  Return Type:

  + Changed 200 OK
    Changed **LevelPoliciesBasicDataList** schema (application/json)

    - Changed property **policies**

      * Changed property **category**

        + Added enum value:  
          `INTEGRATIONS`
* `POST /iam/repo/{level-type}/{level-id}/policies`

  Request:

  Changed **CreateOrUpdateLevelPolicyRequest** schema (application/json)

  + Changed property **category**

    - Added enum value:  
      `INTEGRATIONS`

  Return Type:

  + Changed 201 Created

    Changed Policy schema (application/json)

    - Changed property **category**

      * Added enum value:  
        `INTEGRATIONS`
* `GET /iam/repo/{level-type}/{level-id}/policies/aggregate`

  Return Type:

  + Changed 200 OK

    Changed **PolicyOverviewList** schema (application/json)

    - Changed property **policyOverviewList**

      * Changed property **category**

        + Added enum value:  
          `INTEGRATIONS`
* `POST /iam/repo/{level-type}/{level-id}/policies/validation`

  Request:

  Changed **CreateOrUpdateLevelPolicyRequest** schema (application/json)

  + Changed property **category**

    - Added enum value:  
      `INTEGRATIONS`
* `POST /iam/repo/{level-type}/{level-id}/policies/validation/{policy-uuid}`
  Request:

  Changed **CreateOrUpdateLevelPolicyRequest** schema (application/json)

  + Changed property **category**

    - Added enum value:  
      `INTEGRATIONS`
* `GET /iam/repo/{level-type}/{level-id}/policies/{uuid}`

  Return Type:

  + Changed 200 OK

    Changed Policy schema (application/json)

    - Changed property **category**

      * Added enum value:  
        `INTEGRATIONS`
* `PUT /iam/repo/{level-type}/{level-id}/policies/{uuid}`

  Request:

  Changed **CreateOrUpdateLevelPolicyRequest** schema (application/json)

  + Changed property **category**

    - Added enum value:  
      `INTEGRATIONS`

  Return Type:

  + Changed 201 Created

    Changed Policy schema (application/json)

    - Changed property **category**

      * Added enum value:  
        `INTEGRATIONS`

### /logMonitoring

Removed:

* `POST /logMonitoring/{environmentId}/enable`

### /settings/schemas

* GET /settings/schemas/{schemaId}

  Return Type:

  + Changed 200 OK

    Changed **SchemaDefinitionRestDto** schema (application/json; charset=utf-8)

    - Changed property **constraints**

      * Added property:  
        **timeout**
    - Changed property **deletionConstraints**

      * Added property:  
        **timeout**
    - Changed property **properties**

      * Changed schema of dictionary value:

        + Changed property **constraints**

          - Added property:  
            **timeout**
        + Changed property **items**

          - Changed property **constraints**

            * Added property:  
              **timeout**
    - Changed property **types**

      * Changed schema of dictionary value:

        + Changed property **constraints**

          - Added property:  
            **timeout**
        + Changed property **properties**

          - Changed schema of dictionary value:

            * Changed property **constraints**

              + Added property:  
                **timeout**
            * Changed property **items**

              + Changed property **constraints**

                - Added property:  
                  **timeout**