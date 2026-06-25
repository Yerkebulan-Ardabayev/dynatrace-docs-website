---
title: Dynatrace API changelog version 1.305
source: https://docs.dynatrace.com/managed/whats-new/dynatrace-api/sprint-305
scraped: 2026-05-12T11:35:39.128164
---

# Dynatrace API changelog version 1.305

# Dynatrace API changelog version 1.305

* Release notes
* Published Dec 05, 2024

Rollout start: Dec 3, 2024

## Environment API

### /extensions/{technology}/availableHosts

* `GET /extensions/{technology}/availableHosts` Early Access

  Parameter:

  + Changed technology in path

    - Added enum value:  
      `RABBITMQ_CLIENT`

### /service/requestAttributes

* `POST /service/requestAttributes`

  Request:

  Changed **RequestAttribute** schema

  + Changed property **dataSources**

    - Changed property **scope**

      * Changed property **serviceTechnology**

        + Added enum value:  
          `RABBITMQ_CLIENT`
* `POST /service/requestAttributes/validator`

  Request:

  Changed **RequestAttribute** schema

  + Changed property **dataSources**

    - Changed property **scope**

      * Changed property **serviceTechnology**

        + Added enum value:  
          `RABBITMQ_CLIENT`
* `GET /service/requestAttributes/{id}`

  Return Type:

  + Changed 200 OK
    Changed **RequestAttribute** schema

    - Changed property **dataSources**

      * Changed property **scope**

        + Changed property **serviceTechnology**

          - Added enum value:  
            `RABBITMQ_CLIENT`
* `PUT /service/requestAttributes/{id}`

  Request:

  Changed **RequestAttribute** schema

  + Changed property **dataSources**

    - Changed property **scope**

      * Changed property **serviceTechnology**

        + Added enum value:  
          `RABBITMQ_CLIENT`
* `POST /service/requestAttributes/{id}/validator`

  Request:

  Changed **RequestAttribute** schema

  + Changed property **dataSources**

    - Changed property **scope**

      * Changed property **serviceTechnology**

        + Added enum value:  
          `RABBITMQ_CLIENT`

### /entity/infrastructure/

* `GET /entity/infrastructure/process-groups`

  Return Type:

  + Changed 200 OK
    Changed null schema

    - Changed property **metadata**

      * Added property:  
        **declarativeConfigRuleId**
* `GET /entity/infrastructure/process-groups/{meIdentifier}`

  Return Type:

  + Changed 200 OK
    Changed ProcessGroup schema

    - Changed property **metadata**

      * Added property:  
        **declarativeConfigRuleId**
* `GET /entity/infrastructure/processes`

  Return Type:

  + Changed 200 OK
    Changed null schema

    - Changed property **metadata**

      * Added property:  
        **declarativeConfigRuleId**
* `GET /entity/infrastructure/processes/{meIdentifier}`

  Return Type:

  + Changed 200 OK
    Changed ProcessGroupInstance schema

    - Changed property **metadata**

      * Added property:  
        **declarativeConfigRuleId**

### /timeseries

![Warning](https://dt-cdn.net/images/warning-16-56c09ccf83.png "Warning") Breaking change

* Deleted `PUT /timeseries`. Use [Metrics API v2](/managed/dynatrace-api/environment-api/metric-v2 "Retrieve metric information via Metrics v2 API.") instead.

## Configuration API

### /extensions/{technology}/availableHosts

* `GET /extensions/{technology}/availableHosts` Early Access

  Parameter:

  + Changed technology in path

    - Added enum value:  
      `RABBITMQ_CLIENT`

### /service/requestAttributes

* `POST /service/requestAttributes`

  Request:

  Changed **RequestAttribute** schema

  + Changed property **dataSources**

    - Changed property **scope**

      * Changed property **serviceTechnology**

        + Added enum value:  
          `RABBITMQ_CLIENT`
* `POST /service/requestAttributes/validator`

  Request:

  Changed **RequestAttribute** schema

  + Changed property **dataSources**

    - Changed property **scope**

      * Changed property **serviceTechnology**

        + Added enum value:  
          `RABBITMQ_CLIENT`
* `GET /service/requestAttributes/{id}`

  Return Type:

  + Changed 200 OK
    Changed **RequestAttribute** schema

    - Changed property **dataSources**

      * Changed property **scope**

        + Changed property **serviceTechnology**

          - Added enum value:  
            `RABBITMQ_CLIENT`
* `PUT /service/requestAttributes/{id}`

  Request:

  Changed **RequestAttribute** schema

  + Changed property **dataSources**

    - Changed property **scope**

      * Changed property **serviceTechnology**

        + Added enum value:  
          `RABBITMQ_CLIENT`
* `POST /service/requestAttributes/{id}/validator`

  Request:

  Changed **RequestAttribute** schema

  + Changed property **dataSources**

    - Changed property **scope**

      * Changed property **serviceTechnology**

        + Added enum value:  
          `RABBITMQ_CLIENT`

## Related topics

* [SaaS Release Notes 1.305ï»¿](https://docs.dynatrace.com/docs/shortlink/release-notes-saas-sprint-305)