---
title: Журнал изменений Dynatrace API версии 1.333
source: https://docs.dynatrace.com/managed/whats-new/dynatrace-api/sprint-333
scraped: 2026-05-12T11:35:19.517753
---

# Журнал изменений Dynatrace API версии 1.333

# Журнал изменений Dynatrace API версии 1.333

* Заметки о выпуске
* Published Feb 12, 2026
* Rollout start on Feb 24, 2026

## Environment API

### DELETE /metrics

* `DELETE /metrics`

  + Parameter:

    - Changed **minUnusedDays** in query

      * Required changed from `false` to `true`

### GET /rum/cookieNames

* `GET /rum/cookieNames`

  + Return Type:

    - Changed 200 OK

      * Changed **CookieNames** schema (application/json; charset=utf-8)

        + Added property: **sessionReplayViewIdCookieName**

## Configuration API

### Добавлены значения serviceTechnology: `MONGODB_ROUTER` и `OPENSTACK`

* `GET /extensions/{technology}/availableHosts` Early Access

  + Parameter:

    - Changed technology in path

      * Added enum values:  
        `MONGODB_ROUTER`  
        `OPENSTACK`
* `POST /service/requestAttributes`

  + Request:

    - Changed RequestAttribute schema (application/json; charset=utf-8)

      * Changed property **dataSources**

        + Changed property **scope**

          - Changed property **serviceTechnology**

            * Added enum values:  
              `MONGODB_ROUTER`  
              `OPENSTACK`
* `POST /service/requestAttributes/validator`

  + Request:

    - Changed RequestAttribute schema (application/json; charset=utf-8)

      * Changed property **dataSources**

        + Changed property **scope**

          - Changed property **serviceTechnology**

            * Added enum values:  
              `MONGODB_ROUTER`  
              `OPENSTACK`
* `GET /service/requestAttributes/{id}`

  + Return Type:

    - Changed 200 OK

      * Changed RequestAttribute schema (application/json; charset=utf-8)

        + Changed property **dataSources**

          - Changed property **scope**

            * Changed property **serviceTechnology**

              + Added enum values:  
                `MONGODB_ROUTER`  
                `OPENSTACK`
* `PUT /service/requestAttributes/{id}`

  + Request:

    - Changed RequestAttribute schema (application/json; charset=utf-8)

      * Changed property **dataSources**

        + Changed property **scope**

          - Changed property **serviceTechnology**

            * Added enum values:  
              `MONGODB_ROUTER`  
              `OPENSTACK`
* `POST /service/requestAttributes/{id}/validator`

  + Request:

    - Changed RequestAttribute schema (application/json; charset=utf-8)

      * Changed property **dataSources**

        + Changed property **scope**

          - Changed property **serviceTechnology**

            * Added enum values:  
              `MONGODB_ROUTER`  
              `OPENSTACK`