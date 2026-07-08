---
title: Dynatrace API changelog version 1.306
source: https://docs.dynatrace.com/managed/whats-new/dynatrace-api/sprint-306
---

# Dynatrace API changelog version 1.306

# Dynatrace API changelog version 1.306

* Release notes
* Published Jan 15, 2025

Rollout start: Jan 13, 2025

## Environment API

### /anonymize/

* `PUT /anonymize/anonymizationJobs`

  + Parameter:

    - Add `internalApplicationId` in query

### /otlp/v1

* `POST /otlp/v1/metrics`

  + Return Type:

    - Add 415 Unsupported Media Type
* `POST /otlp/v1/traces`

  + Return Type:

    - Add 415 Unsupported Media Type

### /settings/effective-permissions

![Warning](https://dt-cdn.net/images/warning-16-56c09ccf83.png "Warning") Breaking change

* `POST /settings/effective-permissions:resolve`

  + Request:

    - Changed ResolutionRequest schema
  + Broken compatibility

    - Added required property: **permissions**

## Configuration API

### /applications/web

* `POST /applications/web`

  + Request:

    - Changed WebApplicationConfig schema

      * Changed property **monitoringSettings**

        + Added property: **libraryFileFromCdn**
* `GET /applications/web/default`

  + Return Type:

    - Changed 200 OK

      * Changed WebApplicationConfig schema

        + Changed property **monitoringSettings**

          - Added property: **libraryFileFromCdn**
* `PUT /applications/web/default`

  + Request:

    - Changed WebApplicationConfig schema

      * Changed property **monitoringSettings**

        + Added property: **libraryFileFromCdn**
* `POST /applications/web/default/validator`

  + Request:

    - Changed WebApplicationConfig schema

      * Changed property **monitoringSettings**

        + Added property: **libraryFileFromCdn**
* `POST /applications/web/validator`

  + Request:

    - Changed WebApplicationConfig schema

      * Changed property **monitoringSettings**

        + Added property: **libraryFileFromCdn**
* `GET /applications/web/{id}`

  + Return Type:

    - Changed 200 OK

      * Changed WebApplicationConfig schema

        + Changed property **monitoringSettings**

          - Added property: **libraryFileFromCdn**
* `PUT /applications/web/{id}`

  + Request:

    - Changed WebApplicationConfig schema

      * Changed property **monitoringSettings**

        + Added property: **libraryFileFromCdn**
* `POST /applications/web/{id}/validator`

  + Request:

    - Changed WebApplicationConfig schema

      * Changed property **monitoringSettings**

        + Added property: **libraryFileFromCdn**

### /frequentIssueDetection

* `GET /frequentIssueDetection`

  + Return Type:

    - Changed 200 OK

      * Changed **FrequentIssueDetectionConfig** schema

        + Added property: **frequentIssueDetectionEnvironmentEnabled**
* `PUT /frequentIssueDetection`

  + Request:

    - Changed **FrequentIssueDetectionConfig** schema

      * Added property: **frequentIssueDetectionEnvironmentEnabled**
* `POST /frequentIssueDetection/validator`

  + Request:

    - Changed **FrequentIssueDetectionConfig** schema

      * Added property: **frequentIssueDetectionEnvironmentEnabled**

### /extensions/{technology}

* `GET /extensions/{technology}/availableHosts` Early Access

  + Parameter:

    - Changed technology in path

      * Added enum values: **KOTLIN**

### /service/requestAttributes

* `POST /service/requestAttributes`

  + Request:

    - Changed **RequestAttribute** schema

      * Changed property **dataSources**

        + Added property: **iibNodeTypeCondition**
        + Changed property **scope**

          - Changed property **serviceTechnology**

            * Added enum value:  
              `KOTLIN`
* `POST /service/requestAttributes/validator`

  + Request:

    - Changed **RequestAttribute** schema

      * Changed property **dataSources**

        + Added property: **iibNodeTypeCondition**
        + Changed property **scope**

          - Changed property **serviceTechnology**

            * Added enum value:  
              `KOTLIN`
* `GET /service/requestAttributes/{id}`

  + Return Type:

    - Changed 200 OK

      * Changed **RequestAttribute** schema

        + Changed property **dataSources**

          - Added property: **iibNodeTypeCondition**
          - Changed property **scope**

            * Changed property **serviceTechnology**

              + Added enum value:  
                `KOTLIN`
* `PUT /service/requestAttributes/{id}`

  + Request:

    - Changed **RequestAttribute** schema

      * Changed property **dataSources**

        + Added property: **iibNodeTypeCondition**
        + Changed property **scope**

          - Changed property **serviceTechnology**

            * Added enum value:  
              `KOTLIN`
* `POST /service/requestAttributes/{id}/validator`

  + Request:

    - Changed **RequestAttribute** schema

      * Changed property **dataSources**

        + Added property: **iibNodeTypeCondition**
        + Changed property **scope**

          - Changed property **serviceTechnology**

            * Added enum value:  
              `KOTLIN`

### /hosts/{id}

* `GET /hosts/{id}`

  + Return Type:

    - Changed 200 OK

      * Changed **HostConfig** schema

        + Changed property **techMonitoringConfigList**

          - Changed property **technologies**

            * Changed property **type**

              + Added enum value:  
                `PYTHON`
* `GET /hosts/{id}/technologies`

  + Return Type:

    - Changed 200 OK

      * Changed **TechMonitoringList** schema

        + Changed property **technologies**

          - Changed property **type**

            * Added enum value:  
              `PYTHON`

### /technologies

* `GET /technologies`

  + Return Type:

    - Changed 200 OK

      * Changed **TechMonitoringList** schema

        + Changed property **technologies**

          - Changed property **type**

            * Added enum value:  
              `PYTHON`

## Cluster API

### /nodeManagement/joining

* `POST /nodeManagement/joining`

  + Parameter:

    - Add **rackName** in query

### /settings

* `GET /settings/effectiveValues`

  + Parameter:

    - Add **adminAccess** in query
* `GET /settings/history`

  + Parameter:

    - Add **adminAccess** in query
* `GET /settings/objects`

  + Parameter:

    - Add **adminAccess** in query
* `POST /settings/objects`

  + Parameter:

    - Add **adminAccess** in query
* `GET /settings/objects/{objectId}`

  + Parameter:

    - Add **adminAccess** in query
* `PUT /settings/objects/{objectId}`

  + Parameter:

    - Add **adminAccess** in query
* `DELETE /settings/objects/{objectId}`

  + Parameter:

    - Add **adminAccess** in query

## Related topics

* [SaaS Release Notes 1.306﻿](https://docs.dynatrace.com/docs/shortlink/release-notes-saas-sprint-306)