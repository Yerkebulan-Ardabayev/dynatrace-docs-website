---
title: Dynatrace API changelog version 1.341
source: https://docs.dynatrace.com/managed/whats-new/dynatrace-api/sprint-341
---

# Dynatrace API changelog version 1.341

# Dynatrace API changelog version 1.341

* Release notes
* Published Jun 09, 2026
* Rollout start on Jun 16, 2026

## Environment API

### GET /deployment/installer/agent/{osType}/{installerType}

* `GET /deployment/installer/agent/{osType}/{installerType}/latest`

  + Parameter:

    - Changed **include** in query

      * Added enum values:
        `ruby`
* `GET /deployment/installer/agent/{osType}/{installerType}/version/{version}`

  + Parameter:

    - Changed **include** in query

      * Added enum values:
        `ruby`
* `GET /deployment/installer/agent/{osType}/{installerType}/version/{version}/checksum`

  + Parameter:

    - Changed **include** in query

      * Added enum values:
        `ruby`

### Added custom permissions for Smartscape ingest endpoint

* `GET /tokens`

  + Parameter:

    - Changed **permissions** in query

      * Added enum values:
        `openpipeline.events_smartscape`
* `POST /tokens`

  + Request:

    - Changed **CreateToken** schema (application/json; charset=utf-8)

      * Changed property **scopes**

        + Added enum values:
          `openpipeline.events_smartscape`
* `POST /tokens/lookup`

  + Return Type:

    - Changed 200 OK
      Changed **TokenMetadata** schema (application/json; charset=utf-8)

      * Changed property **scopes**

        + Added enum values:
          `openpipeline.events_smartscape`
* `GET /tokens/{id}`

  + Return Type:

    - Changed 200 OK
      Changed **TokenMetadata** schema (application/json; charset=utf-8)

      * Changed property **scopes**

        + Added enum values:
          `openpipeline.events_smartscape`
* `PUT /tokens/{id}`

  + Request:

    - Changed **UpdateToken** schema (application/json; charset=utf-8)

      * Changed property **scopes**

        + Added enum values:
          `openpipeline.events_smartscape`
* `GET /apiTokens`

  + Return Type:

    - Changed 200 OK
      Changed **ApiTokenList** schema (application/json; charset=utf-8)

      * Changed property **apiTokens**

        + Changed property **scopes**

          - Added enum values:
            `openpipeline.events_smartscape`
* `POST /apiTokens`

  + Request:

    - Changed **ApiTokenCreate** schema (application/json; charset=utf-8)

      * Changed property **scopes**

        + Added enum values:
          `openpipeline.events_smartscape`
* `POST /apiTokens/lookup`

  + Return Type:

    - Changed 200 OK
      Changed **ApiToken** schema (application/json; charset=utf-8)

      * Changed property **scopes**

        + Added enum values:
          `openpipeline.events_smartscape`
* `GET /apiTokens/{id}`

  + Return Type:

    - Changed 200 OK
      Changed **ApiToken** schema (application/json; charset=utf-8)

      * Changed property **scopes**

        + Added enum values:
          `openpipeline.events_smartscape`
* `PUT /apiTokens/{id}`

  + Request:

    - Changed **ApiTokenUpdate** schema (application/json; charset=utf-8)

      * Changed property **scopes**

        + Added enum values:
          `openpipeline.events_smartscape`

### Asset provider for pages as documents

* `GET /extensions/{extensionName}/environmentConfiguration/assets`

  + Return Type:

    - Changed 200 OK
      Changed **ExtensionAssetsDto** schema (application/json; charset=utf-8)

      * Changed property **assets**

        + Changed property **type**

          - Added enum values:
            `DOCUMENT_SCREEN`