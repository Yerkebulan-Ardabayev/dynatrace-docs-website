---
title: Dynatrace API changelog version 1.346
source: https://docs.dynatrace.com/managed/whats-new/dynatrace-api/sprint-346
---

# Dynatrace API changelog version 1.346

# Dynatrace API changelog version 1.346

* Release notes
* Published Aug 25, 2026
* Rollout start on Aug 25, 2026

## Environment API v1

### /deployment

* `GET /deployment/installer/agent/processgroupingconfig`

  + API maturity changed from `EARLY_ADOPTER` to `GENERAL_AVAILABILITY`

## Environment API v2

### /metrics

* `GET /metrics`

  + Return Type:

    - Changed 200 OK
      Changed **MetricDescriptorCollection** schema (application/json; charset=utf-8)

      * Changed property **metrics**

        + Changed property **transformations**

          - Added enum values:  
            `asHistogram`
            Changed **MetricDescriptorCollection** schema (text/csv; header=absent; charset=utf-8)
      * Changed property **metrics**

        + Changed property **transformations**

          - Added enum values:  
            `asHistogram`
            Changed **MetricDescriptorCollection** schema (text/csv; header=present; charset=utf-8)
      * Changed property **metrics**

        + Changed property **transformations**

          - Added enum values:  
            `asHistogram`
* `GET /metrics/{metricKey}`

  + Return Type:

    - Changed 200 OK
      Changed **MetricDescriptor** schema (application/json; charset=utf-8)

      * Changed property **transformations**

        + Added enum values:  
          `asHistogram`
          Changed **MetricDescriptor** schema (text/csv; header=absent; charset=utf-8)
      * Changed property **transformations**

        + Added enum values:  
          `asHistogram`
          Changed **MetricDescriptor** schema (text/csv; header=present; charset=utf-8)
      * Changed property **transformations**

        + Added enum values:  
          `asHistogram`

### /ua

* `POST /ua/entity` Early Access

  + Return Type:

    - Changed 200 OK
      Changed **UAEntityScreenDefinition** schema (application/json; charset=utf-8)

      * Changed property **metricsMetadata**

        + Changed schema of dictionary value:

          - Changed property **transformations**

            * Added enum values:  
              `asHistogram`
* `POST /ua/list` Early Access

  + Return Type:

    - Changed 200 OK
      Changed **UAListScreenDefinition** schema (application/json; charset=utf-8)

      * Changed property **metricsMetadata**

        + Changed schema of dictionary value:

          - Changed property **transformations**

            * Added enum values:  
              `asHistogram`

## Configuration API v1

### /extensions

* `GET /extensions/{technology}/availableHosts` Early Access

  + Parameters:

    - Changed **technology** in path

      * Added enum values:  
        `RUST`  
        `TOKIO`

### /service

* `POST /service/requestAttributes`

  + Request:

    - Changed **RequestAttribute** schema (application/json; charset=utf-8)

      * Changed property **dataSources**

        + Changed property **scope**

          - Changed property **serviceTechnology**

            * Added enum values:  
              `RUST`  
              `TOKIO`
* `POST /service/requestAttributes/validator`

  + Request:

    - Changed **RequestAttribute** schema (application/json; charset=utf-8)

      * Changed property **dataSources**

        + Changed property **scope**

          - Changed property **serviceTechnology**

            * Added enum values:  
              `RUST`  
              `TOKIO`
* `GET /service/requestAttributes/{id}`

  + Return Type:

    - Changed 200 OK
      Changed **RequestAttribute** schema (application/json; charset=utf-8)

      * Changed property **dataSources**

        + Changed property **scope**

          - Changed property **serviceTechnology**

            * Added enum values:  
              `RUST`  
              `TOKIO`
* `PUT /service/requestAttributes/{id}`

  + Request:

    - Changed **RequestAttribute** schema (application/json; charset=utf-8)

      * Changed property **dataSources**

        + Changed property **scope**

          - Changed property **serviceTechnology**

            * Added enum values:  
              `RUST`  
              `TOKIO`
* `POST /service/requestAttributes/{id}/validator`

  + Request:

    - Changed **RequestAttribute** schema (application/json; charset=utf-8)

      * Changed property **dataSources**

        + Changed property **scope**

          - Changed property **serviceTechnology**

            * Added enum values:  
              `RUST`  
              `TOKIO`