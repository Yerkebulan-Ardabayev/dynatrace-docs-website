---
title: Журнал изменений Dynatrace API версии 1.304
source: https://docs.dynatrace.com/managed/whats-new/dynatrace-api/sprint-304
scraped: 2026-05-12T11:36:00.267205
---

# Журнал изменений Dynatrace API версии 1.304

# Журнал изменений Dynatrace API версии 1.304

* Заметки о выпуске
* Published Nov 05, 2024

Rollout start: Nov 4, 2024

## Environment API

### /synthetic/locations

* `POST /synthetic/locations`

  + Request:

    - Changed **PrivateSyntheticLocation** schema

      * Added property:  
        **nodeNames**

### /synthetic/nodes

* `GET /synthetic/nodes`

  + Parameter:

    - Add **isContainerized** in query

## Configuration API

### /cloudFoundry/credentials/

* `GET /cloudFoundry/credentials/{id}`

  + Return Type:

    - Changed 200 OK

      * Changed **CloudFoundryCredentials** schema

        + Changed property **endpointStatus**

          - Added enum value:  
            `FASTCHECK_TOO_MANY_SUBSCRIPTIONS`

### /kubernetes/credentials/

* `GET /kubernetes/credentials/{id}`

  + Return Type:

    - Changed 200 OK

      * Changed **KubernetesCredentials** schema

        + Changed property **endpointStatus**

          - Added enum value:  
            `FASTCHECK_TOO_MANY_SUBSCRIPTIONS`

### /extensions/{technology}/availableHosts

* `GET /extensions/{technology}/availableHosts` Early Access

  + Parameter:

    - Changed technology in path

      * Added enum values:  
        `AWS_EVENT_BRIDGE`  
        `LOGSTASH_LOGBACK_ENCODER`

### /service/requestAttributes

* `POST /service/requestAttributes`

  + Request:

    - Changed **RequestAttribute** schema

      * Changed property **dataSources**

        + Changed property **scope**

          - Changed property **serviceTechnology**

            * Added enum values:  
              `AWS_EVENT_BRIDGE`  
              `LOGSTASH_LOGBACK_ENCODER`
        + Changed property **source**

          - Added enum value:  
            `CICS_TRANSACTION_GROUP_ID`
* `POST /service/requestAttributes/validator`

  + Request:

    - Changed **RequestAttribute** schema

      * Changed property **dataSources**

        + Changed property **scope**

          - Changed property **serviceTechnology**

            * Added enum values:  
              `AWS_EVENT_BRIDGE`  
              `LOGSTASH_LOGBACK_ENCODER`
        + Changed property **source**

          - Added enum value:  
            `CICS_TRANSACTION_GROUP_ID`
* `GET /service/requestAttributes/{id}`

  + Return Type:

    - Changed 200 OK

      * Changed **RequestAttribute** schema

        + Changed property **dataSources**

          - Changed property **scope**

            * Changed property **serviceTechnology**

              + Added enum values:  
                `AWS_EVENT_BRIDGE`  
                `LOGSTASH_LOGBACK_ENCODER`
          - Changed property **source**

            * Added enum value:  
              `CICS_TRANSACTION_GROUP_ID`
* `PUT /service/requestAttributes/{id}`

  + Request:

    - Changed **RequestAttribute** schema

      * Changed property **dataSources**

        + Changed property **scope**

          - Changed property **serviceTechnology**

            * Added enum values:  
              `AWS_EVENT_BRIDGE`  
              `LOGSTASH_LOGBACK_ENCODER`
        + Changed property **source**

          - Added enum value:  
            `CICS_TRANSACTION_GROUP_ID`
* `POST /service/requestAttributes/{id}/validator`

  + Request:

    - Changed **RequestAttribute** schema

      * Changed property **dataSources**

        + Changed property **scope**

          - Changed property **serviceTechnology**

            * Added enum values:  
              `AWS_EVENT_BRIDGE`  
              `LOGSTASH_LOGBACK_ENCODER`
        + Changed property **source**

          - Added enum value:  
            `CICS_TRANSACTION_GROUP_ID`

### /calculatedMetrics/service

* `POST /calculatedMetrics/service`

  + Request:

    - Changed **CalculatedServiceMetric** schema

      * Changed property **conditions**

        + Changed property **attribute**

          - Added enum value:  
            `ONE_AGENT_ATTRIBUTE`
        + Changed property **comparisonInfo**

          - Changed property **type**

            * Added enum value:  
              `STRING_ONE_AGENT_ATTRIBUTE`
      * Changed property **dimensionDefinition**

        + Changed property **placeholders**

          - Added property: **oneAgentAttributeKey**
          - Changed property **attribute**

            * Added enum value:  
              `ONE_AGENT_ATTRIBUTE`
* `POST /calculatedMetrics/service/validator`

  + Request:

    - Changed **CalculatedServiceMetric** schema

      * Changed property **conditions**

        + Changed property **attribute**

          - Added enum value:  
            `ONE_AGENT_ATTRIBUTE`
        + Changed property **comparisonInfo**

          - Changed property **type**

            * Added enum value:  
              `STRING_ONE_AGENT_ATTRIBUTE`
      * Changed property **dimensionDefinition**

        + Changed property **placeholders**

          - Added property: **oneAgentAttributeKey**
          - Changed property **attribute**

            * Added enum value:  
              `ONE_AGENT_ATTRIBUTE`
* `GET /calculatedMetrics/service/{metricKey}`

  + Return Type:

    - Changed 200 OK

      * Changed **CalculatedServiceMetric** schema

        + Changed property **conditions**

          - Changed property **attribute**

            * Added enum value:  
              `ONE_AGENT_ATTRIBUTE`
          - Changed property **comparisonInfo**

            * Changed property **type**

              + Added enum value:  
                `STRING_ONE_AGENT_ATTRIBUTE`
        + Changed property **dimensionDefinition**

          - Changed property **placeholders**

            * Added property: **oneAgentAttributeKey**
            * Changed property **attribute**

              + Added enum value:  
                `ONE_AGENT_ATTRIBUTE`
* `PUT /calculatedMetrics/service/{metricKey}`

  + Request:

    - Changed **CalculatedServiceMetric** schema

      * Changed property **conditions**

        + Changed property **attribute**

          - Added enum value:  
            `ONE_AGENT_ATTRIBUTE`
        + Changed property **comparisonInfo**

          - Changed property **type**

            * Added enum value:  
              `STRING_ONE_AGENT_ATTRIBUTE`
      * Changed property **dimensionDefinition**

        + Changed property **placeholders**

          - Added property: **oneAgentAttributeKey**
          - Changed property **attribute**

            * Added enum value:  
              `ONE_AGENT_ATTRIBUTE`
* `POST /calculatedMetrics/service/{metricKey}/validator`

  + Request:

    - Changed **CalculatedServiceMetric** schema

      * Changed property **conditions**

        + Changed property **attribute**

          - Added enum value:  
            `ONE_AGENT_ATTRIBUTE`
        + Changed property **comparisonInfo**

          - Changed property **type**

            * Added enum value:  
              `STRING_ONE_AGENT_ATTRIBUTE`
      * Changed property **dimensionDefinition**

        + Changed property **placeholders**

          - Added property: **oneAgentAttributeKey**
          - Changed property **attribute**

            * Added enum value:  
              `ONE_AGENT_ATTRIBUTE`

### /service/requestNaming

* `POST /service/requestNaming`

  + Request:

    - Changed **RequestNaming** schema

      * Changed property **conditions**

        + Changed property **attribute**

          - Added enum value:  
            `ONE_AGENT_ATTRIBUTE`
        + Changed property **comparisonInfo**

          - Changed property **type**

            * Added enum value:  
              `STRING_ONE_AGENT_ATTRIBUTE`
      * Changed property **placeholders**

        + Added property: **oneAgentAttributeKey**
        + Changed property **attribute**

          - Added enum value:  
            `ONE_AGENT_ATTRIBUTE`
* `POST /service/requestNaming/validator`

  + Request:

    - Changed **RequestNaming** schema

      * Changed property **conditions**

        + Changed property **attribute**

          - Added enum value:  
            `ONE_AGENT_ATTRIBUTE`
        + Changed property **comparisonInfo**

          - Changed property **type**

            * Added enum value:  
              `STRING_ONE_AGENT_ATTRIBUTE`
      * Changed property **placeholders**

        + Added property: **oneAgentAttributeKey**
        + Changed property **attribute**

          - Added enum value:  
            `ONE_AGENT_ATTRIBUTE`
* `GET /service/requestNaming/{id}`

  + Return Type:

    - Changed 200 OK

      * Changed **RequestNaming** schema

        + Changed property **conditions**

          - Changed property **attribute**

            * Added enum value:  
              `ONE_AGENT_ATTRIBUTE`
          - Changed property **comparisonInfo**

            * Changed property **type**

              + Added enum value:  
                `STRING_ONE_AGENT_ATTRIBUTE`
        + Changed property **placeholders**

          - Added property: **oneAgentAttributeKey**
          - Changed property **attribute**

            * Added enum value:  
              `ONE_AGENT_ATTRIBUTE`
* `PUT /service/requestNaming/{id}`

  + Request:

    - Changed **RequestNaming** schema

      * Changed property **conditions**

        + Changed property **attribute**

          - Added enum value:  
            `ONE_AGENT_ATTRIBUTE`
        + Changed property **comparisonInfo**

          - Changed property **type**

            * Added enum value:  
              `STRING_ONE_AGENT_ATTRIBUTE`
      * Changed property **placeholders**

        + Added property: **oneAgentAttributeKey**
        + Changed property **attribute**

          - Added enum value:  
            `ONE_AGENT_ATTRIBUTE`
* `POST /service/requestNaming/{id}/validator`

  + Request:

    - Changed **RequestNaming** schema

      * Changed property **conditions**

        + Changed property **attribute**

          - Added enum value:  
            `ONE_AGENT_ATTRIBUTE`
        + Changed property **comparisonInfo**

          - Changed property **type**

            * Added enum value:  
              `STRING_ONE_AGENT_ATTRIBUTE`
      * Changed property **placeholders**

        + Added property: **oneAgentAttributeKey**
        + Changed property **attribute**

          - Added enum value:  
            `ONE_AGENT_ATTRIBUTE`

## Cluster API

### /multiDc/migration/cassandra/rebuild

* `GET /multiDc/migration/cassandra/rebuild` Early Access

  + Parameter:

    - Delete `acceptableLoadDifferencePercentage` in query

### /synthetic/locations

* `POST /synthetic/locations`

  + Request:

    - Changed **PrivateSyntheticLocation** schema

      * Added properties:  
        **countryName**  
        **regionName**
* `GET /synthetic/locations/{locationId}`

  + Return Type:

    - Changed 200 OK

      * Changed **SyntheticLocation** schema

        + Added properties:  
          **countryName**  
          **regionName**
* `PUT /synthetic/locations/{locationId}`

  + Request:

    - Changed **PrivateSyntheticLocation** schema

      * Added properties:  
        **countryName**  
        **regionName**

## Связанные темы

* [Заметки о выпуске SaaS 1.304](https://docs.dynatrace.com/docs/shortlink/release-notes-saas-sprint-304)