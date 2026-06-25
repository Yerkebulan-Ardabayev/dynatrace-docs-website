---
title: Dynatrace API changelog version 1.312
source: https://docs.dynatrace.com/managed/whats-new/dynatrace-api/sprint-312
scraped: 2026-05-12T11:36:09.165627
---

# Dynatrace API changelog version 1.312

# Dynatrace API changelog version 1.312

* Release notes
* Published Apr 08, 2025

Rollout start: Apr 8, 2025

## Environment API

### /rum

* `GET /rum/jsTagSri/{entity}` Early Access

  + Extensions:

    - API maturity changed from `PREVIEW` to `EARLY_ADOPTER`

### /synthetic/locations

* `POST /synthetic/locations`

  + Request:

    - Changed **PrivateSyntheticLocation** schema

      * Added property:  
        `browserExecutionSupported`
* `GET /synthetic/locations/{locationId}`

  + Return Type:

    - Changed 200 OK

      * Changed **SyntheticLocation** schema

        + Added property:  
          `browserExecutionSupported`
* `PUT /synthetic/locations/{locationId}`

  + Request:

    - Changed **PrivateSyntheticLocation** schema

      * Added property:  
        `browserExecutionSupported`

### /extensions

* `POST /extensions`

  + Return Type:

    - Changed 200 OK

      * Changed **ExtensionUploadResponseDto** schema

        + Changed property **featureSetsDetails**

          - Changed schema of dictionary value:

            * Added properties:  
              **description**  
              **displayName**  
              **isRecommended**
            * Added required property:  
              **isRecommended**
    - Changed 201 Created

      * Changed **ExtensionUploadResponseDto** schema

        + Changed property **featureSetsDetails**

          - Changed schema of dictionary value:

            * Added properties:  
              **description**  
              **displayName**  
              **isRecommended**
            * Added required property:  
              **isRecommended**
* `GET /extensions/{extensionName}/{extensionVersion}`

  + Return Type:

    - Changed 200 OK

      * Changed **Extension** schema

        + Changed property **featureSetsDetails**

          - Changed schema of dictionary value:

            * Added properties:  
              **description**  
              **displayName**  
              **isRecommended**
            * Added required property:  
              **isRecommended**
* `DELETE /extensions/{extensionName}/{extensionVersion}`

  + Return Type:

    - Changed 200 OK

      * Changed **Extension** schema

        + Changed property **featureSetsDetails**

          - Changed schema of dictionary value:

            * Added properties:  
              **description**  
              **displayName**  
              **isRecommended**
            * Added required property:  
              **isRecommended**
* `GET /hub/extensions1/{extension1FQN}`

  + Return Type:

    - Changed 200 OK

      * Changed **ItemDetails** schema

        + Changed property **extension2Details**

          - Changed property **releases**

            * Changed property **featureSets**

              + Changed schema of dictionary value:

                - Added properties:  
                  **description**  
                  **displayName**  
                  **isRecommended**
                - Added required property:  
                  **isRecommended**
* `GET /hub/extensions2/{extensionName}`

  + Return Type:

    - Changed 200 OK

      * Changed **ItemDetails** schema

        + Changed property **extension2Details**

          - Changed property **releases**

            * Changed property **featureSets**

              + Changed schema of dictionary value:

                - Added properties:  
                  **description**  
                  **displayName**  
                  **isRecommended**
                - Added required property:  
                  **isRecommended**
* `GET /hub/technologies/{slug}`

  + Return Type:

    - Changed 200 OK

      * Changed **ItemDetails** schema

        + Changed property **extension2Details**

          - Changed property **releases**

            * Changed property **featureSets**

              + Changed schema of dictionary value:

                - Added properties:  
                  **description**  
                  **displayName**  
                  **isRecommended**
                - Added required property:  
                  **isRecommended**

### /settings/schemas

* `GET /settings/schemas`

  + Return Type:

    - Changed 200 OK

      * Changed **SchemaList** schema

        + Changed property **items**

          - Added property:  
            **ownerBasedAccessControl**

## Configuration API

### /calculatedMetrics/service

* `POST /calculatedMetrics/service`

  + Request:

    - Changed **CalculatedServiceMetric** schema

      * ![Warning](https://dt-cdn.net/images/warning-16-56c09ccf83.png "Warning") Breaking change

        + Changed property **metricDefinition**

          - Changed property **metric**

            * Removed enum value:  
              `CAPTURED_FULL_SERVICE_CALLS`
* `POST /calculatedMetrics/service/validator`

  + Request:

    - Changed **CalculatedServiceMetric** schema

      * ![Warning](https://dt-cdn.net/images/warning-16-56c09ccf83.png "Warning") Breaking change

        + Changed property **metricDefinition**

          - Changed property **metric**

            * Removed enum value:  
              `CAPTURED_FULL_SERVICE_CALLS`
* `GET /calculatedMetrics/service/{metricKey}`

  + Return Type:

    - Changed 200 OK

      * Changed **CalculatedServiceMetric** schema

        + ![Warning](https://dt-cdn.net/images/warning-16-56c09ccf83.png "Warning") Breaking change

          - Changed property **metricDefinition**

            * Changed property **metric**

              + Removed enum value:  
                `CAPTURED_FULL_SERVICE_CALLS`
* `PUT /calculatedMetrics/service/{metricKey}`

  + Request:

    - Changed **CalculatedServiceMetric** schema

      * ![Warning](https://dt-cdn.net/images/warning-16-56c09ccf83.png "Warning") Breaking change

        + Changed property **metricDefinition**

          - Changed property **metric**

            * Removed enum value:  
              `CAPTURED_FULL_SERVICE_CALLS`
* `POST /calculatedMetrics/service/{metricKey}/validator`

  + Request:

    - Changed **CalculatedServiceMetric** schema

      * ![Warning](https://dt-cdn.net/images/warning-16-56c09ccf83.png "Warning") Breaking change

        + Changed property **metricDefinition**

          - Changed property **metric**

            * Removed enum value:  
              `CAPTURED_FULL_SERVICE_CALLS`

### /extensions

* `GET /extensions/{technology}/availableHosts` Early Access

  + Parameter:

    - Changed technology in path

      * Added enum value:  
        `DB2_CLIENT`

### /service/requestAttributes

* `POST /service/requestAttributes`

  + Request:

    - Changed **RequestAttribute** schema

      * Changed property **dataSources**

        + Changed property **scope**

          - Changed property **serviceTechnology**

            * Added enum value:  
              `DB2_CLIENT`
* `POST /service/requestAttributes/validator`

  + Request:

    - Changed **RequestAttribute** schema

      * Changed property **dataSources**

        + Changed property **scope**

          - Changed property **serviceTechnology**

            * Added enum value:  
              `DB2_CLIENT`
* `GET /service/requestAttributes/{id}`

  + Return Type:

    - Changed 200 OK

      * Changed **RequestAttribute** schema

        + Changed property **dataSources**

          - Changed property **scope**

            * Changed property **serviceTechnology**

              + Added enum value:  
                `DB2_CLIENT`
* `PUT /service/requestAttributes/{id}`

  + Request:

    - Changed **RequestAttribute** schema

      * Changed property **dataSources**

        + Changed property **scope**

          - Changed property **serviceTechnology**

            * Added enum value:  
              `DB2_CLIENT`
* `POST /service/requestAttributes/{id}/validator`

  + Request:

    - Changed **RequestAttribute** schema

      * Changed property **dataSources**

        + Changed property **scope**

          - Changed property **serviceTechnology**

            * Added enum value:  
              `DB2_CLIENT`

## Cluster API

### /elastic

* `POST /elastic/reloadEsClientOnAllNodes`

### /settings/schemas

* `GET /settings/schemas`

  + Return Type:

    - Changed 200 OK

      * Changed **SchemaList** schema

        + Changed property **items**

          - Added property:  
            **ownerBasedAccessControl**

### /synthetic/locations

* `POST /synthetic/locations`

  + Request:

    - Changed **PrivateSyntheticLocation** schema

      * Added property:  
        `browserExecutionSupported`
* `PUT /synthetic/locations/{locationId}`

  + Request:

    - Changed **PrivateSyntheticLocation** schema

      * Added property:  
        `browserExecutionSupported`