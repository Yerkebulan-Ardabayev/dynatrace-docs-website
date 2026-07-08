---
title: Dynatrace API changelog version 1.322
source: https://docs.dynatrace.com/managed/whats-new/dynatrace-api/sprint-322
---

# Dynatrace API changelog version 1.322

# Dynatrace API changelog version 1.322

* Release notes
* Updated on Aug 21, 2025

Rollout start: Aug 26, 2025

## Environment API

### /entity/infrastructure/process-groups and process-groups

* `GET /entity/infrastructure/process-groups`

  + Return Type:

    - Changed 200 OK

      * Changed null schema (application/json; charset=utf-8)

        + Changed property **metadata**

          - Added properties:  
            **azure.containerapp.dnssuffix**  
            **azure.containerapp.name**  
            **pythonModule**  
            **pythonScript**  
            **pythonScriptPath**
* `GET /entity/infrastructure/process-groups/{meIdentifier}`

  + Return Type:

    - Changed 200 OK

      * Changed **ProcessGroup** schema (application/json; charset=utf-8)

        + Changed property **metadata**

          - Added properties:  
            **azure.containerapp.dnssuffix**  
            **azure.containerapp.name**  
            **pythonModule**  
            **pythonScript**  
            **pythonScriptPath**
* `GET /entity/infrastructure/processes`

  + Return Type:

    - Changed 200 OK

      * Changed null schema (application/json; charset=utf-8)

        + Changed property **metadata**

          - Added properties:  
            **azure.containerapp.dnssuffix**  
            **azure.containerapp.name**  
            **pythonModule**  
            **pythonScript**  
            **pythonScriptPath**
* `GET /entity/infrastructure/processes/{meIdentifier}`

  + Return Type:

    - Changed 200 OK

      * Changed **ProcessGroupInstance** schema (application/json; charset=utf-8)

        + Changed property **metadata**

          - Added properties:  
            **azure.containerapp.dnssuffix**  
            **azure.containerapp.name**  
            **pythonModule**  
            **pythonScript**  
            **pythonScriptPath**

### /rum/

* `GET /rum/jsTagSri/{entity}`

  + Extensions:

    - API maturity changed from EARLY\_ADOPTER to GENERAL\_AVAILABILITY

### /settings/history

* `GET /settings/history`

  + Return Type:

    - Add 400 Bad Request

### /synthetic/locations

* `POST /synthetic/locations`

  + Request:

    - Changed **PrivateSyntheticLocation** schema (application/json; charset=utf-8)

      * Added property:  
        **fipsMode**
* `GET /synthetic/locations/{locationId}`

  + Return Type:

    - Changed 200 OK

      * Changed **SyntheticLocation** schema (application/json; charset=utf-8)

        + Added property:  
          **fipsMode**

### /synthetic/executions

* `GET /synthetic/executions`

  + Return Type:

    - Changed 200 OK

      * Changed **SyntheticOnDemandExecutions** schema (application/json; charset=utf-8)

        + Broken compatibility

          - Changed property **executions**

            * Changed property **nextExecutionId**

              + Type changed from integer(int64) to string
* `POST /synthetic/executions/batch`

  + Return Type:

    - Changed 201 Created

      * Changed **SyntheticOnDemandExecutionResult** schema (application/json; charset=utf-8)

        + Broken compatibility

          - Changed property **triggeringProblemsDetails**

            * Changed property **executionId**

              + Type changed from integer(int64) to string
* `GET /synthetic/executions/batch/{batchId}`

  + Return Type:

    - Changed 200 OK

      * Changed **SyntheticOnDemandBatchStatus** schema (application/json; charset=utf-8)

        + Broken compatibility

          - Changed property **triggeringProblems**

            * Changed property **executionId**

              + Type changed from integer(int64) to string
* `GET /synthetic/executions/{executionId}`

  + Return Type:

    - Changed 200 OK

      * Changed **SyntheticOnDemandExecution** schema (application/json; charset=utf-8)

        + Broken compatibility

          - Changed property **nextExecutionId**

            * Type changed from integer(int64) to string
* `POST /synthetic/executions/{executionId}`

  + Return Type:

    - Changed 201 Created

      * Changed **SyntheticOnDemandExecutionResult** schema (application/json; charset=utf-8)

        + Broken compatibility

          - Changed property **triggeringProblemsDetails**

            * Changed property **executionId**

              + Type changed from integer(int64) to string
* `GET /synthetic/executions/{executionId}/fullReport`

  + Return Type:

    - Changed 200 OK

      * Changed **SyntheticOnDemandExecution** schema (application/json; charset=utf-8)

        + Broken compatibility

          - Changed property **nextExecutionId**

            * Type changed from integer(int64) to string

## Configuration API

### /service/requestAttributes

* `POST /service/requestAttributes`

  + Request:

    - Changed **RequestAttribute** schema (application/json; charset=utf-8)

      * Changed property **dataSources**

        + Changed property **cicsSDKMethodNodeCondition**

          - Changed property **operator**

            * Added enum value:  
              `NOT_EMPTY`
        + Changed property **iibLabelMethodNodeCondition**

          - Changed property **operator**

            * Added enum value:  
              `NOT_EMPTY`
        + Changed property **iibMethodNodeCondition**

          - Changed property **operator**

            * Added enum value:  
              `NOT_EMPTY`
        + Changed property **iibNodeTypeCondition**

          - Changed property **operator**

            * Added enum value:  
              `NOT_EMPTY`
        + Changed property **valueProcessing**

          - Changed property **valueCondition**

            * Changed property **operator**

              + Added enum value:  
                `NOT_EMPTY`
* `POST /service/requestAttributes/validator`

  + Request:

    - Changed **RequestAttribute** schema (application/json; charset=utf-8)

      * Changed property **dataSources**

        + Changed property **cicsSDKMethodNodeCondition**

          - Changed property **operator**

            * Added enum value:  
              `NOT_EMPTY`
        + Changed property **iibLabelMethodNodeCondition**

          - Changed property **operator**

            * Added enum value:  
              `NOT_EMPTY`
        + Changed property **iibMethodNodeCondition**

          - Changed property **operator**

            * Added enum value:  
              `NOT_EMPTY`
        + Changed property **iibNodeTypeCondition**

          - Changed property **operator**

            * Added enum value:  
              `NOT_EMPTY`
        + Changed property **valueProcessing**

          - Changed property **valueCondition**

            * Changed property **operator**

              + Added enum value:  
                `NOT_EMPTY`
* `GET /service/requestAttributes/{id}`

  + Return Type:

    - Changed 200 OK

      * Changed **RequestAttribute** schema (application/json; charset=utf-8)

        + Changed property **dataSources**

          - Changed property **cicsSDKMethodNodeCondition**

            * Changed property **operator**

              + Added enum value:  
                `NOT_EMPTY`
          - Changed property **iibLabelMethodNodeCondition**

            * Changed property **operator**

              + Added enum value:  
                `NOT_EMPTY`
          - Changed property **iibMethodNodeCondition**

            * Changed property **operator**

              + Added enum value:  
                `NOT_EMPTY`
          - Changed property **iibNodeTypeCondition**

            * Changed property **operator**

              + Added enum value:  
                `NOT_EMPTY`
          - Changed property **valueProcessing**

            * Changed property **valueCondition**

              + Changed property **operator**

                - Added enum value:  
                  `NOT_EMPTY`
* `PUT /service/requestAttributes/{id}`

  + Request:

    - Changed **RequestAttribute** schema (application/json; charset=utf-8)

      * Changed property **dataSources**

        + Changed property **cicsSDKMethodNodeCondition**

          - Changed property **operator**

            * Added enum value:  
              `NOT_EMPTY`
        + Changed property **iibLabelMethodNodeCondition**

          - Changed property **operator**

            * Added enum value:  
              `NOT_EMPTY`
        + Changed property **iibMethodNodeCondition**

          - Changed property **operator**

            * Added enum value:  
              `NOT_EMPTY`
        + Changed property **iibNodeTypeCondition**

          - Changed property **operator**

            * Added enum value:  
              `NOT_EMPTY`
        + Changed property **valueProcessing**

          - Changed property **valueCondition**

            * Changed property **operator**

              + Added enum value:  
                `NOT_EMPTY`
* `POST /service/requestAttributes/{id}/validator`

  + Request:

    - Changed **RequestAttribute** schema (application/json; charset=utf-8)

      * Changed property **dataSources**

        + Changed property **cicsSDKMethodNodeCondition**

          - Changed property **operator**

            * Added enum value:  
              `NOT_EMPTY`
        + Changed property **iibLabelMethodNodeCondition**

          - Changed property **operator**

            * Added enum value:  
              `NOT_EMPTY`
        + Changed property **iibMethodNodeCondition**

          - Changed property **operator**

            * Added enum value:  
              `NOT_EMPTY`
        + Changed property **iibNodeTypeCondition**

          - Changed property **operator**

            * Added enum value:  
              `NOT_EMPTY`
        + Changed property **valueProcessing**

          - Changed property **valueCondition**

            * Changed property **operator**

              + Added enum value:  
                `NOT_EMPTY`

## Cluster API

### /cluster/maintenance

* `GET /cluster/maintenance`

  + Return Type:

    - Changed 200 OK

      * Changed null schema (application/json)

        + Changed **IPMigrationMaintenanceMode**

          - Added property:  
            **jsonObjectForReasonMessage**

### /iam/

* `POST /iam/repo/{level-type}/{level-id}/policies`

  + Return Type:

    - Changed 201 Created

      * Changed **Policy** schema (application/json)

        + Changed property **statements**

          - Changed property **conditions**

            * Changed property **operator**

              + Added enum value:  
                `MATCH`
* `GET /iam/repo/{level-type}/{level-id}/policies/{uuid}`

  + Return Type:

    - Changed 200 OK

      * Changed **Policy** schema (application/json)

        + Changed property **statements**

          - Changed property **conditions**

            * Changed property **operator**

              + Added enum value:  
                `MATCH`
* `PUT /iam/repo/{level-type}/{level-id}/policies/{uuid}`

  + Return Type:

    - Changed 201 Created

      * Changed **Policy** schema (application/json)

        + Changed property **statements**

          - Changed property **conditions**

            * Changed property **operator**

              + Added enum value:  
                `MATCH`
* `GET /iam/resolution/{level-type}/{level-id}/descendants/effectivepermissions`

  + Return Type:

    - Changed 200 OK

      * Changed DescendantsEffectivePermissions schema (application/json)

        + Changed property **descendantLevelsEffectivePermissions**

          - Changed schema of dictionary value:

            * Changed property **effectivePermissions**

              + Changed property **effects**

                - Changed property **conditions**

                  * Changed property **operator**

                    + Added enum value:  
                      `MATCH`
                - Changed property **effectivePolicies**

                  * Changed property **policy**

                    + Changed property **statements**

                      - Changed property **conditions**

                        * Changed property **operator**

                          + Added enum value:  
                            `MATCH`
* `GET /iam/resolution/{level-type}/{level-id}/effectivepermissions`

  + Return Type:

    - Changed 200 OK

      * Changed EffectivePermissions schema (application/json)

        + Changed property **effectivePermissions**

          - Changed property **effects**

            * Changed property **conditions**

              + Changed property **operator**

                - Added enum value:  
                  `MATCH`
            * Changed property **effectivePolicies**

              + Changed property **policy**

                - Changed property **statements**

                  * Changed property **conditions**

                    + Changed property **operator**

                      - Added enum value:  
                        `MATCH`
* `POST /iam/resolution/{level-type}/{level-id}/effectivepermissions:dry-run`

  + Return Type:

    - Changed 200 OK

      * Changed EffectivePermissions schema (application/json)

        + Changed property **effectivePermissions**

          - Changed property **effects**

            * Changed property **conditions**

              + Changed property **operator**

                - Added enum value:  
                  `MATCH`
            * Changed property **effectivePolicies**

              + Changed property **policy**

                - Changed property **statements**

                  * Changed property **conditions**

                    + Changed property **operator**

                      - Added enum value:  
                        `MATCH`

### /settings/history

* `GET /settings/history`

  + Return Type:

    - Add 400 Bad Request

### /synthetic/locations

* `POST /synthetic/locations`

  + Request:

    - Changed **PrivateSyntheticLocation** schema (application/json; charset=utf-8)

      * Added property:  
        **fipsMode**
* `PUT /synthetic/locations/{locationId}`

  + Request:

    - Changed **PrivateSyntheticLocation** schema (application/json; charset=utf-8)

      * Added property:  
        **fipsMode**