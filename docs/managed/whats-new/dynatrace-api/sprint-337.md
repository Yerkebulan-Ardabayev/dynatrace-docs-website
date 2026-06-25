---
title: Dynatrace API changelog version 1.337
source: https://docs.dynatrace.com/managed/whats-new/dynatrace-api/sprint-337
scraped: 2026-05-12T11:35:46.914996
---

# Dynatrace API changelog version 1.337

# Dynatrace API changelog version 1.337

* Release notes
* Published Apr 08, 2026
* Rollout start on Apr 21, 2026

## Environment API v1

### /entity

* `GET /entity/applications`

  + Return Type:

    - Changed 200 OK
      Changed **Application** schema (application/json; charset=utf-8)

      * Removed properties:  
        **attributes**
* `GET /entity/applications/{meIdentifier}`

  + Return Type:

    - Changed 200 OK
      Changed **Application** schema (application/json; charset=utf-8)

      * Removed properties:  
        **attributes**
* `GET /entity/infrastructure/hosts`

  + Return Type:

    - Changed 200 OK
      Changed **Application** schema (application/json; charset=utf-8)

      * Removed properties:  
        **attributes**
* `GET /entity/infrastructure/hosts/{meIdentifier}`

  + Return Type:

    - Changed 200 OK
      Changed **Host** schema (application/json; charset=utf-8)

      * Removed properties:  
        **attributes**
* `GET /entity/infrastructure/process-groups`

  + Return Type:

    - Changed 200 OK
      Changed **ProcessGroup** schema (application/json; charset=utf-8)

      * Removed properties:  
        **attributes**
* `GET /entity/infrastructure/process-groups/{meIdentifier}`

  + Return Type:

    - Changed 200 OK
      Changed **ProcessGroup** schema (application/json; charset=utf-8)

      * Removed properties:  
        **attributes**
* `GET /entity/infrastructure/processes`

  + Return Type:

    - Changed 200 OK
      Changed **ProcessGroupInstance** schema (application/json; charset=utf-8)

      * Removed properties:  
        **attributes**
* `GET /entity/infrastructure/processes/{meIdentifier}`

  + Return Type:

    - Changed 200 OK
      Changed **ProcessGroupInstance** schema (application/json; charset=utf-8)

      * Removed properties:  
        **attributes**
* `GET /entity/services`

  + Return Type:

    - Changed 200 OK
      Changed **Service** schema (application/json; charset=utf-8)

      * Removed properties:  
        **attributes**
* `GET /entity/services/{meIdentifier}`

  + Return Type:

    - Changed 200 OK
      Changed **Service** schema (application/json; charset=utf-8)

      * Removed properties:  
        **attributes**

### /events

* `GET /events`

  + Return Type:

    - Changed 200 OK
      Changed **EventQueryResult** schema (application/json)

      * Changed property **events**

        + Removed properties:  
          **metadata**
* `GET /events/{eventId}`

  + Return Type:

    - Changed 200 OK
      Changed **EventRestEntry** schema (application/json)

      * Removed properties:  
        **metadata**
* `GET /events`

  + Return Type:

    - Changed 200 OK
      Changed **EventQueryResult** schema (application/json)

      * Changed property **events**

        + Removed properties:  
          **metadata**
* `GET /events/{eventId}`

  + Return Type:

    - Changed 200 OK
      Changed **EventRestEntry** schema (application/json)

      * Removed properties:  
        **metadata**

### /oneagents

* `GET /oneagents`

  + Return Type:

    - Changed 200 OK
      Changed **HostsListPage** schema (application/json; charset=utf-8)

      * Changed property **hosts**

        + Changed property **hostInfo**

          - Removed properties:  
            **attributes**

### /problem

* `GET /problem/details/{problemId}`

  + Return Type:

    - Changed 200 OK
      Changed **ProblemDetailsResultWrapper** schema (application/json; charset=utf-8)

      * Changed property **result**

        + Changed property **rankedEvents**

          - Removed properties:  
            **metadata**
* `GET /problem/feed`

  + Return Type:

    - Changed 200 OK
      Changed **ProblemFeedResultWrapper** schema (application/json; charset=utf-8)

      * Changed property **result**

        + Changed property **problems**

          - Changed property **rankedEvents**

            * Removed properties:  
              **metadata**

## Environment API v2

### /credentials

* `GET /credentials`

  + Return Type:

    - Changed 200 OK
      Changed **CredentialsList** schema (application/json; charset=utf-8)

      * Changed property **credentials**

        + Changed property **scope**

          - Added enum value:  
            `EXTENSION_AUTHENTICATION`
        + Changed property **scopes**

          - Added enum value:  
            `EXTENSION_AUTHENTICATION`
* `POST /credentials`

  + Request:

    - Changed **Credentials** schema (application/json; charset=utf-8)

      * Changed property **scope**

        + Added enum value:  
          `EXTENSION_AUTHENTICATION`
      * Changed property **scopes**

        + Added enum value:  
          `EXTENSION_AUTHENTICATION`
* `GET /credentials/{id}`

  + Return Type:

    - Changed 200 OK
      Changed **CredentialsResponseElement** schema (application/json; charset=utf-8)

      * Changed property **scope**

        + Added enum value:  
          `EXTENSION_AUTHENTICATION`
      * Changed property **scopes**

        + Added enum value:  
          `EXTENSION_AUTHENTICATION`
* `PUT /credentials/{id}`

  + Request:

    - Changed **Credentials** schema (application/json; charset=utf-8)

      * Changed property **scope**

        + Added enum value:  
          `EXTENSION_AUTHENTICATION`
      * Changed property **scopes**

        + Added enum value:  
          `EXTENSION_AUTHENTICATION`

### /extensions

* `PUT /extensions/{extensionName}/monitoringConfigurations/{configurationId}/actions`

  + Return Type:

    - Changed 202 Accepted
      Changed **ExecuteActionsResponse** schema (application/json; charset=utf-8)

      * Added properties:  
        **agIds**
      * Changed property **agId**

        + Deprecated changed to true
      * Changed property **agName**

        + Deprecated changed to true

## Config API v2

### /calculatedMetrics

* `POST /calculatedMetrics/service`

  + Request:

    - Changed **CalculatedServiceMetric** schema (application/json; charset=utf-8)

      * Changed property **dimensionDefinition**

        + Changed property **placeholders**

          - Changed property **source**

            * Changed property **managementZone**

              + Deprecated changed to true
            * Changed property **serviceTag**

              + Deprecated changed to true
* `POST /calculatedMetrics/service/validator`

  + Request:

    - Changed **CalculatedServiceMetric** schema (application/json; charset=utf-8)

      * Changed property **dimensionDefinition**

        + Changed property **placeholders**

          - Changed property **source**

            * Changed property **managementZone**

              + Deprecated changed to true
            * Changed property **serviceTag**

              + Deprecated changed to true
* `GET /calculatedMetrics/service/{metricKey}`

  + Return Type:

    - Changed 200 OK
      Changed **CalculatedServiceMetric** schema (application/json; charset=utf-8)

      * Changed property **dimensionDefinition**

        + Changed property **placeholders**

          - Changed property **source**

            * Changed property **managementZone**

              + Deprecated changed to true
            * Changed property **serviceTag**

              + Deprecated changed to true
* `PUT /calculatedMetrics/service/{metricKey}`

  + Request:

    - Changed **CalculatedServiceMetric** schema (application/json; charset=utf-8)

      * Changed property **dimensionDefinition**

        + Changed property **placeholders**

          - Changed property **source**

            * Changed property **managementZone**

              + Deprecated changed to true
            * Changed property **serviceTag**

              + Deprecated changed to true
* `POST /calculatedMetrics/service/{metricKey}/validator`

  + Request:

    - Changed **CalculatedServiceMetric** schema (application/json; charset=utf-8)

      * Changed property **dimensionDefinition**

        + Changed property **placeholders**

          - Changed property **source**

            * Changed property **managementZone**

              + Deprecated changed to true
            * Changed property **serviceTag**

              + Deprecated changed to true

### /credentials

* `GET /credentials`

  + Return Type:

    - Changed 200 OK
      Changed **CredentialsList** schema (application/json; charset=utf-8)

      * Changed property **credentials**

        + Changed property **scope**

          - Added enum value:  
            `EXTENSION_AUTHENTICATION`
        + Changed property **scopes**

          - Added enum value:  
            `EXTENSION_AUTHENTICATION`
* `POST /credentials`

  + Request:

    - Changed **Credentials** schema (application/json; charset=utf-8)

      * Changed property **scope**

        + Added enum value:  
          `EXTENSION_AUTHENTICATION`
      * Changed property **scopes**

        + Added enum value:  
          `EXTENSION_AUTHENTICATION`
* `GET /credentials/{id}`

  + Return Type:

    - Changed 200 OK
      Changed **CredentialsResponseElement** schema (application/json; charset=utf-8)

      * Changed property **scope**

        + Added enum value:  
          `EXTENSION_AUTHENTICATION`
      * Changed property **scopes**

        + Added enum value:  
          `EXTENSION_AUTHENTICATION`
* `PUT /credentials/{id}`

  + Request:

    - Changed **Credentials** schema (application/json; charset=utf-8)

      * Changed property **scope**

        + Added enum value:  
          `EXTENSION_AUTHENTICATION`
      * Changed property **scopes**

        + Added enum value:  
          `EXTENSION_AUTHENTICATION`

### /extensions

* `GET /extensions/{technology}/availableHosts` (EARLY\_ADOPTER)

  + Parameter:

    - Changed **technology** in path

      * Added enum values:  
        `KTOR_CLIENT`  
        `KTOR_SERVER`
* `POST /service/requestAttributes`

  + Request:

    - Changed **RequestAttribute** schema (application/json; charset=utf-8)

      * Changed property **dataSources**

        + Changed property **scope**

          - Changed property **serviceTechnology**

            * Added enum values:  
              `KTOR_CLIENT`  
              `KTOR_SERVER`

### /service

* `POST /service/requestAttributes`

  + Request:

    - Changed **RequestAttribute** schema (application/json; charset=utf-8)

      * Changed property **dataSources**

        + Changed property **scope**

          - Changed property **serviceTechnology**

            * Deprecated changed to true
          - Changed property **tagOfProcessGroup**

            * Deprecated changed to true
* `POST /service/requestAttributes/validator`

  + Request:

    - Changed **RequestAttribute** schema (application/json; charset=utf-8)

      * Changed property **dataSources**

        + Changed property **scope**

          - Changed property **serviceTechnology**

            * Deprecated changed to true
          - Changed property **tagOfProcessGroup**

            * Deprecated changed to true
* `GET /service/requestAttributes/{id}`

  + Return Type:

    - Changed 200 OK
      Changed **RequestAttribute** schema (application/json; charset=utf-8)

      * Changed property **dataSources**

        + Changed property **scope**

          - Changed property **serviceTechnology**

            * Deprecated changed to true
          - Changed property **tagOfProcessGroup**

            * Deprecated changed to true
* `PUT /service/requestAttributes/{id}`

  + Request:

    - Changed **RequestAttribute** schema (application/json; charset=utf-8)

      * Changed property **dataSources**

        + Changed property **scope**

          - Changed property **serviceTechnology**

            * Deprecated changed to true
          - Changed property **tagOfProcessGroup**

            * Deprecated changed to true
* `POST /service/requestAttributes/{id}/validator`

  + Request:

    - Changed **RequestAttribute** schema (application/json; charset=utf-8)

      * Changed property **dataSources**

        + Changed property **scope**

          - Changed property **serviceTechnology**

            * Deprecated changed to true
          - Changed property **tagOfProcessGroup**

            * Deprecated changed to true
* `POST /service/requestNaming`

  + Request:

    - Changed **RequestNaming** schema (application/json; charset=utf-8)

      * Changed property **managementZones**

        + Deprecated changed to true
      * Changed property **placeholders**

        + Changed property **source**

          - Changed property **managementZone**

            * Deprecated changed to true
          - Changed property **serviceTag**

            * Deprecated changed to true
* `POST /service/requestNaming/validator`

  + Request:

    - Changed **RequestNaming** schema (application/json; charset=utf-8)

      * Changed property **managementZones**

        + Deprecated changed to true
      * Changed property **placeholders**

        + Changed property **source**

          - Changed property **managementZone**

            * Deprecated changed to true
          - Changed property **serviceTag**

            * Deprecated changed to true
* `GET /service/requestNaming/{id}`

  + Return Type:

    - Changed 200 OK
      Changed **RequestNaming** schema (application/json; charset=utf-8)

      * Changed property **managementZones**

        + Deprecated changed to true
      * Changed property **placeholders**

        + Changed property **source**

          - Changed property **managementZone**

            * Deprecated changed to true
          - Changed property **serviceTag**

            * Deprecated changed to true
* `PUT /service/requestNaming/{id}`

  + Request:

    - Changed **RequestNaming** schema (application/json; charset=utf-8)

      * Changed property **managementZones**

        + Deprecated changed to true
      * Changed property **placeholders**

        + Changed property **source**

          - Changed property **managementZone**

            * Deprecated changed to true
          - Changed property **serviceTag**

            * Deprecated changed to true
* `POST /service/requestNaming/{id}/validator`

  + Request:

    - Changed **RequestNaming** schema (application/json; charset=utf-8)

      * Changed property **managementZones**

        + Deprecated changed to true
      * Changed property **placeholders**

        + Changed property **source**

          - Changed property **managementZone**

            * Deprecated changed to true
          - Changed property **serviceTag**

            * Deprecated changed to true
* `GET /extensions/{technology}/availableHosts` (EARLY\_ADOPTER)

  + Parameter:

    - Changed **technology** in path

      * Added enum values:  
        `KTOR_CLIENT`  
        `KTOR_SERVER`
* `POST /service/requestAttributes`

  + Request:

    - Changed **RequestAttribute** schema (application/json; charset=utf-8)

      * Changed property **dataSources**

        + Changed property **scope**

          - Changed property **serviceTechnology**

            * Added enum values:  
              `KTOR_CLIENT`  
              `KTOR_SERVER`
* `POST /service/requestAttributes/validator`

  + Request:

    - Changed **RequestAttribute** schema (application/json; charset=utf-8)

      * Changed property **dataSources**

        + Changed property **scope**

          - Changed property **serviceTechnology**

            * Added enum values:  
              `KTOR_CLIENT`  
              `KTOR_SERVER`
* `GET /service/requestAttributes/{id}`

  + Return Type:

    - Changed 200 OK
      Changed **RequestAttribute** schema (application/json; charset=utf-8)

      * Changed property **dataSources**

        + Changed property **scope**

          - Changed property **serviceTechnology**

            * Added enum values:  
              `KTOR_CLIENT`  
              `KTOR_SERVER`
* `PUT /service/requestAttributes/{id}`

  + Request:

    - Changed **RequestAttribute** schema (application/json; charset=utf-8)

      * Changed property **dataSources**

        + Changed property **scope**

          - Changed property **serviceTechnology**

            * Added enum values:  
              `KTOR_CLIENT`  
              `KTOR_SERVER`
* `POST /service/requestAttributes/{id}/validator`

  + Request:

    - Changed **RequestAttribute** schema (application/json; charset=utf-8)

      * Changed property **dataSources**

        + Changed property **scope**

          - Changed property **serviceTechnology**

            * Added enum values:  
              `KTOR_CLIENT`  
              `KTOR_SERVER`