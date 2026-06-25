---
title: Dynatrace API changelog version 1.311
source: https://docs.dynatrace.com/managed/whats-new/dynatrace-api/sprint-311
scraped: 2026-05-12T11:36:10.357165
---

# Dynatrace API changelog version 1.311

# Dynatrace API changelog version 1.311

* Release notes
* Published Mar 27, 2025

Rollout start: Mar 25, 2025

## Environment API

### /synthetic/monitors

* `POST /synthetic/monitors`

  + Request:

    - Changed **SyntheticMonitorUpdate** schema

      ![Warning](https://dt-cdn.net/images/warning-16-56c09ccf83.png "Warning") Breaking change

      * Changed property **anomalyDetection**

        + Changed property **loadingTimeThresholds**

          - Changed property **thresholds**

            * Changed property **eventIndex**

              + Minimum changed from `1` to `0`
            * Changed property **requestIndex**

              + Minimum changed from `1` to `0`
* `GET /synthetic/monitors/{monitorId}`

  + Return Type:

    - Changed 200 OK

      * Changed **SyntheticMonitor** schema

        + Changed property **anomalyDetection**

          - Changed property **loadingTimeThresholds**

            * Changed property **thresholds**

              + Changed property **eventIndex**

                - Minimum changed from `1` to `0`
              + Changed property **requestIndex**

                - Minimum changed from `1` to `0`
* `PUT /synthetic/monitors/{monitorId}`

  + Request:

    - Changed **SyntheticMonitorUpdate** schema

      ![Warning](https://dt-cdn.net/images/warning-16-56c09ccf83.png "Warning") Breaking change

      * Changed property **anomalyDetection**

        + Changed property **loadingTimeThresholds**

          - Changed property **thresholds**

            * Changed property **eventIndex**

              + Minimum changed from `1` to `0`
            * Changed property **requestIndex**

              + Minimum changed from `1` to `0`

### /activeGates

* `GET /activeGates`

  + Parameter:

    - Changed **enabledModule** in query

      * Added enum value:  
        `DEBUGGING`
    - Changed **disabledModule** in query

      * Added enum value:  
        `DEBUGGING`
  + Return Type:

    - Changed 200 OK
    - Changed **ActiveGateList** schema

      * Changed property **activeGates**

        + Changed property **modules**

          - Changed property **type**

            * Added enum value:  
              `DEBUGGING`
* `GET /activeGates/{agId}`

  + Return Type:

    - Changed 200 OK

      * Changed **ActiveGate** schema

        + Changed property **modules**

          - Changed property **type**

            * Added enum value:  
              `DEBUGGING`

## Configuration API

### /extensions

* `GET /extensions/{technology}/availableHosts` Early Access

  + Parameter:

    - Changed technology in path

      * Added enum value: `APACHE_PEKKO`

### /service/requestAttributes

* `POST /service/requestAttributes`

  + Request:

    - Changed **RequestAttribute** schema

      * Changed property **dataSources**

        + Changed property **scope**

          - Changed property **serviceTechnology**

            * Added enum value:  
              `APACHE_PEKKO`
* `POST /service/requestAttributes/validator`

  + Request:

    - Changed **RequestAttribute** schema

      * Changed property **dataSources**

        + Changed property **scope**

          - Changed property **serviceTechnology**

            * Added enum value:  
              `APACHE_PEKKO`
* `GET /service/requestAttributes/{id}`

  + Return Type:

    - Changed 200 OK

      * Changed **RequestAttribute** schema

        + Changed property **dataSources**

          - Changed property **scope**

            * Changed property **serviceTechnology**

              + Added enum value:  
                `APACHE_PEKKO`
* `PUT /service/requestAttributes/{id}`

  + Request:

    - Changed **RequestAttribute** schema

      * Changed property **dataSources**

        + Changed property **scope**

          - Changed property **serviceTechnology**

            * Added enum value:  
              `APACHE_PEKKO`
* `POST /service/requestAttributes/{id}/validator`

  + Request:

    - Changed **RequestAttribute** schema

      * Changed property **dataSources**

        + Changed property **scope**

          - Changed property **serviceTechnology**

            * Added enum value:  
              `APACHE_PEKKO`