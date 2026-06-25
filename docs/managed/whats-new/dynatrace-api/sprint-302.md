---
title: Dynatrace API changelog version 1.302
source: https://docs.dynatrace.com/managed/whats-new/dynatrace-api/sprint-302
scraped: 2026-05-12T11:36:02.687490
---

# Dynatrace API changelog version 1.302

# Dynatrace API changelog version 1.302

* Release notes
* Published Oct 09, 2024

Rollout start: Oct 7, 2024

## Environment API

### /oneagents

* `GET /oneagents`

  + Parameter:

    - Changed **detailedAvailabilityState** in query

      * Added enum value:  
        `UNMONITORED_AGENT_MIGRATED`
  + Return Type:

    - Changed 200 OK

      * Changed **HostsListPage** schema

        + Changed property **hosts**

          - Changed property **detailedAvailabilityState**

            * Added enum value:  
              `UNMONITORED_AGENT_MIGRATED`

### /synthetic/locations (API v1)

* `POST /synthetic/locations`

  + Request:

    - Changed **PrivateSyntheticLocation** schema

      * Removed required property:  
        `entityId`
* `GET /synthetic/locations/{locationId}`

  + Return Type:

    - Changed 200 OK

      * Changed **SyntheticLocation** schema

        + ![Warning](https://dt-cdn.net/images/warning-16-56c09ccf83.png "Warning") Breaking change

          - Removed required property:  
            `entityId`

### /tokens

* `GET /tokens`

  + Parameter:

    - Changed permissions in query

      * Added enum value:  
        `agentTokenManagement.read`
* `POST /tokens`

  + Request:

    - Changed **CreateToken** schema

      * Changed property **scopes**

        + Added enum value:  
          `agentTokenManagement.read`
* `POST /tokens/lookup`

  + Return Type:

    - Changed 200 OK

      * Changed **TokenMetadata** schema

        + Changed property **scopes**

          - Added enum value:  
            `agentTokenManagement.read`
* `GET /tokens/{id}`

  + Return Type:

    - Changed 200 OK

      * Changed **TokenMetadata** schema

        + Changed property **scopes**

          - Added enum value:  
            `agentTokenManagement.read`
* `PUT /tokens/{id}`

  + Request:

    - Changed **UpdateToken** schema

      * Changed property **scopes**

        + Added enum value:  
          `agentTokenManagement.read`

### /apiTokens

* `GET /apiTokens`

  + Return Type:

    - Changed 200 OK

      * Changed **ApiTokenList** schema

        + Changed property **apiTokens**

          - Changed property **scopes**

            * Added enum value:  
              `agentTokenManagement.read`
* `POST /apiTokens`

  + Request:

    - Changed **ApiTokenCreate** schema

      * Changed property **scopes**

        + Added enum value:  
          `agentTokenManagement.read`
* `POST /apiTokens/lookup`

  + Return Type:

    - Changed 200 OK

      * Changed **ApiToken** schema

        + Changed property **scopes**

          - Added enum value:  
            `agentTokenManagement.read`
* `GET /apiTokens/{id}`

  + Return Type:

    - Changed 200 OK

      * Changed **ApiToken** schema

        + Changed property **scopes**

          - Added enum value:  
            `agentTokenManagement.read`
* `PUT /apiTokens/{id}`

  + Request:

    - Changed **ApiTokenUpdate** schema

      * Changed property **scopes**

        + Added enum value:  
          `agentTokenManagement.read`

### /settings

* `POST /settings/effective-permissions:resolve`

  + Return Type:

    - Changed 200 OK

      * Changed null schema

        + Added property:  
          **context**

### /synthetic/locations (API v2)

* `POST /synthetic/locations`

  + Request:

    - Changed **PrivateSyntheticLocation** schema

      * Removed required property:  
        **entityId**
* `GET /synthetic/locations/{locationId}`

  + Return Type:

    - Changed 200 OK

      * Changed **SyntheticLocation** schema

        + ![Warning](https://dt-cdn.net/images/warning-16-56c09ccf83.png "Warning") Breaking change

          - Removed required property:  
            **entityId**

### /synthetic/nodes

* `GET /synthetic/nodes`

  + Parameter:

    - Add **assignedToLocation** in query

## Configuration API

### /extensions

* `GET /extensions/{technology}/availableHosts` Early Access

  + Parameter:

    - Changed technology in path

      * Added enum value:  
        `HELIDON`

### /service

* `POST /service/requestAttributes`

  + Request:

    - Changed **RequestAttribute** schema

      * Changed property **dataSources**

        + Changed property **scope**

          - Changed property **serviceTechnology**

            * Added enum value:  
              `HELIDON`
* `POST /service/requestAttributes/validator`

  + Request:

    - Changed **RequestAttribute** schema

      * Changed property **dataSources**

        + Changed property **scope**

          - Changed property **serviceTechnology**

            * Added enum value:  
              `HELIDON`
* `GET /service/requestAttributes/{id}`

  + Return Type:

    - Changed 200 OK

      * Changed **RequestAttribute** schema

        + Changed property **dataSources**

          - Changed property **scope**

            * Changed property **serviceTechnology**

              + Added enum value:  
                `HELIDON`
* `PUT /service/requestAttributes/{id}`

  + Request:

    - Changed **RequestAttribute** schema

      * Changed property **dataSources**

        + Changed property **scope**

          - Changed property **serviceTechnology**

            * Added enum value:  
              `HELIDON`
* `POST /service/requestAttributes/{id}/validator`

  + Request:

    - Changed **RequestAttribute** schema

      * Changed property **dataSources**

        + Changed property **scope**

          - Changed property **serviceTechnology**

            * Added enum value:  
              `HELIDON`

## Related topics

* [SaaS Release Notes 1.302ï»¿](https://docs.dynatrace.com/docs/shortlink/release-notes-saas-sprint-302)