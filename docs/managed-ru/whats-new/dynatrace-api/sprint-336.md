---
title: Журнал изменений Dynatrace API версии 1.336
source: https://docs.dynatrace.com/managed/whats-new/dynatrace-api/sprint-336
scraped: 2026-05-12T11:35:41.786589
---

# Журнал изменений Dynatrace API версии 1.336

# Журнал изменений Dynatrace API версии 1.336

* Заметки о выпуске
* Published Mar 30, 2026
* Rollout start on Apr 07, 2026

## Environment API

### /deployment

* `GET /deployment/lambda/layer`

  + Parameter:

    - Changed **techtype** in query

      * Added enum values: `DotNet`

### /entity

* `GET /entity/applications`

  + Return Type:

    - Changed 200 OK

      * Changed **null** schema (application/json; charset=utf-8)

        + Added properties: `attributes`
* `GET /entity/applications/{meIdentifier}`

  + Return Type:

    - Changed 200 OK

      * Changed **Application** schema (application/json; charset=utf-8)

        + Added properties: `attributes`
* `GET /entity/infrastructure/hosts`

  + Return Type:

    - Changed 200 OK

      * Changed **null** schema (application/json; charset=utf-8)

        + Added properties: `attributes`
* `GET /entity/infrastructure/hosts/{meIdentifier}`

  + Return Type:

    - Changed 200 OK

      * Changed **Host** schema (application/json; charset=utf-8)

        + Added properties: `attributes`
* `GET /entity/infrastructure/process-groups`

  + Return Type:

    - Changed 200 OK

      * Changed **null** schema (application/json; charset=utf-8)

        + Added properties: `attributes`
* `GET /entity/infrastructure/process-groups/{meIdentifier}`

  + Return Type:

    - Changed 200 OK

      * Changed **ProcessGroup** schema (application/json; charset=utf-8)

        + Added properties: `attributes`
* `GET /entity/infrastructure/processes`

  + Return Type:

    - Changed 200 OK

      * Changed **null** schema (application/json; charset=utf-8)

        + Added properties: `attributes`
* `GET /entity/infrastructure/processes/{meIdentifier}`

  + Return Type:

    - Changed 200 OK

      * Changed **ProcessGroupInstance** schema (application/json; charset=utf-8)

        + Added properties: `attributes`
* `GET /entity/services`

  + Return Type:

    - Changed 200 OK

      * Changed **null** schema (application/json; charset=utf-8)

        + Added properties: `attributes`
* `GET /entity/services/{meIdentifier}`

  + Return Type:

    - Changed 200 OK

      * Changed **Service** schema (application/json; charset=utf-8)

        + Added properties: `attributes`

### /events

* `GET /events`

  + Return Type:

    - Changed 200 OK

      * Changed **EventQueryResult** schema (application/json)

        + Changed property **events**

          - Added properties: `metadata`
* `GET /events/{eventId}`

  + Return Type:

    - Changed 200 OK

      * Changed **EventRestEntry** schema (application/json)

        + Added properties: `metadata`

### /oneagents

* `GET /oneagents`

  + Return Type:

    - Changed 200 OK

      * Changed **HostsListPage** schema (application/json; charset=utf-8)

        + Changed property **hosts**

          - Changed property **hostInfo**

            * Added properties: `attributes`

### /problem

* `GET /problem/details/{problemId}`

  + Return Type:

    - Changed 200 OK

      * Changed **ProblemDetailsResultWrapper** schema (application/json; charset=utf-8)

        + Changed property **result**

          - Changed property **rankedEvents**

            * Added properties: `metadata`
* `GET /problem/feed`

  + Return Type:

    - Changed 200 OK

      * Changed **ProblemFeedResultWrapper** schema (application/json; charset=utf-8)

        + Changed property **result**

          - Changed property **problems**

            * Changed property **rankedEvents**

              + Added properties: `metadata`

## Cluster API v1

### /cluster

* `POST /cluster/maintenance/off`

  + Request:

    - Changed **null** schema (application/json)

      * Added oneOf option: `ConvertToOnlineMaintenanceRequestDto`
* `POST /cluster/maintenance/on`

  + Request:

    - Changed **null** schema (application/json)

      * Added oneOf option: `ConvertToOnlineMaintenanceRequestDto`

### /upgradeManagement

* `GET /upgradeManagement/installationFiles`

  + Return Type:

    - Changed 200 OK

      * Changed **null** schema (application/json; charset=utf-8)

        + Changed property **status**

          - Added enum values: `INVALID_VERSION`