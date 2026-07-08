---
title: Dynatrace API changelog version 1.317
source: https://docs.dynatrace.com/managed/whats-new/dynatrace-api/sprint-317
---

# Dynatrace API changelog version 1.317

# Dynatrace API changelog version 1.317

* Release notes
* Published Jun 24, 2025

Rollout start: Jun 17, 2025

## Environment API

### /extensions/{extensionName}/monitoringConfigurations/

* `GET /extensions/{extensionName}/monitoringConfigurations/{configurationId}/audit` New!
* `GET /extensions/{extensionName}/monitoringConfigurations/{configurationId}/status`

  + Return Type:

    - Changed 200 OK

      * Changed ExtensionStatusDto schema

        + Broken compatibility

          - Changed property **status**

            * Added enum values:  
              `PENDING`  
              `WARNING`
          - Removed required property **timestamp**

### /activeGates

* `GET /activeGates`

  + Parameter:

    - Add **fipsMode** in query
  + Return Type:

    - Changed 200 OK

      * Changed **ActiveGateList** schema

        + Changed property **activeGates**

          - Added property **fipsMode**
* `GET /activeGates/{agId}`

  + Return Type:

    - Changed 200 OK

      * Changed **ActiveGate** schema

        + Added property **fipsMode**

## Configuration API

### /extensions/{technology}/availableHosts

* `GET /extensions/{technology}/availableHosts` Early Access

  + Parameter:

    - Changed technology in path

      * Added enum value:  
        `KOTLIN_COROUTINES`

### /service/requestAttributes/

* `POST /service/requestAttributes`

  + Request:

    - Changed **RequestAttribute** schema

      * Changed property **dataSources**

        + Changed property **scope**

          - Changed property **serviceTechnology**

            * Added enum value:  
              `KOTLIN_COROUTINES`
* `POST /service/requestAttributes/validator`

  + Request:

    - Changed **RequestAttribute** schema

      * Changed property **dataSources**

        + Changed property **scope**

          - Changed property **serviceTechnology**

            * Added enum value:  
              `KOTLIN_COROUTINES`
* `GET /service/requestAttributes/{id}`

  + Return Type:

    - Changed 200 OK

      * Changed **RequestAttribute** schema

        + Changed property **dataSources**

          - Changed property **scope**

            * Changed property **serviceTechnology**

              + Added enum value:  
                `KOTLIN_COROUTINES`
* `PUT /service/requestAttributes/{id}`

  + Request:

    - Changed **RequestAttribute** schema

      * Changed property **dataSources**

        + Changed property **scope**

          - Changed property **serviceTechnology**

            * Added enum value:  
              `KOTLIN_COROUTINES`
* `POST /service/requestAttributes/{id}/validator`

  + Request:

    - Changed **RequestAttribute** schema

      * Changed property **dataSources**

        + Changed property **scope**

          - Changed property **serviceTechnology**

            * Added enum value:  
              `KOTLIN_COROUTINES`