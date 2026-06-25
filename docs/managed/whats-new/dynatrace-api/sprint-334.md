---
title: Dynatrace API changelog version 1.334
source: https://docs.dynatrace.com/managed/whats-new/dynatrace-api/sprint-334
scraped: 2026-05-12T11:35:22.103896
---

# Dynatrace API changelog version 1.334

# Dynatrace API changelog version 1.334

* Release notes
* Published Feb 26, 2026
* Rollout start on Mar 10, 2026

## Environment API

### /deployment

* `GET /deployment/lambda/layer`

  + Parameter:

    - Changed **techtype** in query

      * Added enum value:  
        `go`

### /tokens

* `GET /tokens`

  + Parameter:

    - Changed **permissions** in query

      * Added enum value:  
        `extensionDiscoveryJmx.read`
* `POST /tokens`
  Request:
  Changed **CreateToken** schema (application/json; charset=utf-8)

  + Changed property **scopes**

    - Added enum value:  
      `extensionDiscoveryJmx.read`
* `POST /tokens/lookup`
  Return Type:

  + Changed 200 OK
    Changed **TokenMetadata** schema (application/json; charset=utf-8)

    - Changed property **scopes**

      * Added enum value:  
        `extensionDiscoveryJmx.read`
* `GET /tokens/{id}`
  Return Type:

  + Changed 200 OK
    Changed **TokenMetadata** schema (application/json; charset=utf-8)

    - Changed property **scopes**

      * Added enum value:  
        `extensionDiscoveryJmx.read`
* `PUT /tokens/{id}`
  Request:
  Changed **UpdateToken** schema (application/json; charset=utf-8)

  + Changed property **scopes**

    - Added enum value:  
      `extensionDiscoveryJmx.read`

### /extensions

Early Access Added new endpoints:

* `GET /extensions/discovery/jmx/processes`
* `GET /extensions/discovery/jmx/processes/{process-id}`

### /apiTokens

* `GET /apiTokens`

  + Return Type:

    - Changed 200 OK
      Changed **ApiTokenList** schema (application/json; charset=utf-8)

      * Changed property **apiTokens**

        + Changed property **scopes**

          - Added enum value:  
            `extensionDiscoveryJmx.read`
* `POST /apiTokens`

  + Request:

    - Changed **ApiTokenCreate** schema (application/json; charset=utf-8)

      * Changed property **scopes**

        + Added enum value:  
          `extensionDiscoveryJmx.read`
* `POST /apiTokens/lookup`

  + Return Type:

    - Changed 200 OK

      * Changed **ApiToken** schema (application/json; charset=utf-8)

        + Changed property **scopes**

          - Added enum value:  
            `extensionDiscoveryJmx.read`
* `GET /apiTokens/{id}`

  + Return Type:

    - Changed 200 OK

      * Changed **ApiToken** schema (application/json; charset=utf-8)

        + Changed property **scopes**

          - Added enum value:  
            `extensionDiscoveryJmx.read`
* `PUT /apiTokens/{id}`

  + Request:

    - Changed **ApiTokenUpdate** schema (application/json; charset=utf-8)

      * Changed property **scopes**

        + Added enum value:  
          `extensionDiscoveryJmx.read`

### /rum

* `GET /rum/cookieNames`

  + Return Type:

    - Changed 200 OK

      * Changed **CookieNames** schema (application/json; charset=utf-8)

        + Added properties:  
          **sessionReplayCookieName**

## Cluster API

* `GET /cluster/maintenance`

  + Return Type:

    - Changed 200 OK

      * Changed **IPMigrationMaintenanceMode** (application/json)

        + Changed **reason** property

          - Added enum value:
            `CONVERT_TO_ONLINE`
* `POST /cluster/maintenance/off`

  + Request:

    - Changed **IpMigrationMaintenanceRequestDto** schema (application/json)

      * Changed **reason** property

        + Added enum value:
          `CONVERT_TO_ONLINE`
* `POST /cluster/maintenance/on`

  + Request:

    - Changed **IpMigrationMaintenanceRequestDto** schema (application/json)

      * Changed **reason** property

        + Added enum value:
          `CONVERT_TO_ONLINE`