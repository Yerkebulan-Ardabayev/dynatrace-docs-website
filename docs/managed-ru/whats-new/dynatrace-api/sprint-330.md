---
title: Журнал изменений Dynatrace API версии 1.330
source: https://docs.dynatrace.com/managed/whats-new/dynatrace-api/sprint-330
scraped: 2026-05-12T11:36:17.676077
---

# Журнал изменений Dynatrace API версии 1.330

# Журнал изменений Dynatrace API версии 1.330

* Заметки о выпуске
* Published Dec 30, 2025
* Rollout start on Jan 13, 2026

## Environment API

### /apiTokens

* `GET /apiTokens`

  + Return Type:

    - Changed 200 OK

      * Changed **ApiTokenList** schema (application/json; charset=utf-8)

        + ![Warning](https://dt-cdn.net/images/warning-16-56c09ccf83.png "Warning") Несовместимое изменение

          - Changed property **apiTokens**
          - Changed property **scopes**

            * Removed enum values:
              `analyzers.read`
              `analyzers.write`
* `POST /apiTokens`

  + Request:

    - Changed **ApiTokenCreate** schema (application/json; charset=utf-8)

      * ![Warning](https://dt-cdn.net/images/warning-16-56c09ccf83.png "Warning") Несовместимое изменение

        + Changed property **scopes**

          - Removed enum values:
            `analyzers.read`
            `analyzers.write`
* `POST /apiTokens/lookup`

  + Return Type:

    - Changed 200 OK

      * Changed **ApiToken** schema (application/json; charset=utf-8)

        + ![Warning](https://dt-cdn.net/images/warning-16-56c09ccf83.png "Warning") Несовместимое изменение

          - Changed property **scopes**
          - Removed enum values:
            `analyzers.read`
            `analyzers.write`
* `GET /apiTokens/{id}`

  + Return Type:

    - Changed 200 OK

      * Changed **ApiToken** schema (application/json; charset=utf-8)

        + ![Warning](https://dt-cdn.net/images/warning-16-56c09ccf83.png "Warning") Несовместимое изменение

          - Changed property **scopes**

            * Removed enum values:
              `analyzers.read`
              `analyzers.write`
* `PUT /apiTokens/{id}`

  + Request:

    - Changed **ApiTokenUpdate** schema (application/json; charset=utf-8)

      * ![Warning](https://dt-cdn.net/images/warning-16-56c09ccf83.png "Warning") Несовместимое изменение

        + Changed property **scopes**

          - Removed enum values:
            `analyzers.read`
            `analyzers.write`

### /extensions

Удалены следующие эндпоинты:

* `GET /extensions/{extensionName}/environmentConfiguration/events`
* `GET /extensions/{extensionName}/monitoringConfigurations/{configurationId}/events`

### /logs/ingest

* `POST /logs/ingest`

  + Parameter:

    - Add `structure` in query
    - Add `X-Dynatrace-Options` in header
  + Return Type:

    - Add `502 Bad Gateway`
    - Add `504 Gateway Timeout`

### /maintenance

Это несовместимое изменение, скрывающее `tagKey` из схемы. POST-запрос с `tagKey` по-прежнему действителен, но, как и раньше, не имеет эффекта.

* `GET /maintenance`

  + Return Type:

    - Changed 200 OK

      * Changed **null** schema (application/json)

        + Changed property **scope**

          - Changed property **matches**

            * Changed property **tags**

              + Removed property **tagKey**
* `POST /maintenance`

  + Request:

    - Changed **MaintenanceWindow** schema (application/json)

      * Changed property **scope**

        + Changed property **matches**

          - Changed property **tags**

            * Removed property **tagKey**
* `GET /maintenance/{uid}`

  + Return Type:

    - Changed 200 OK

      * Changed **MaintenanceWindow** schema (application/json)

        + Changed property **scope**

          - Changed property **matches**

            * Changed property **tags**

              + Removed property **tagKey**

### /otlp/v1/logs

* `POST /otlp/v1/logs`

  + Parameter:

    - Add `structure` in query
    - Add `X-Dynatrace-Options` in header
  + Request:

    - Changed **ExportLogsServiceRequest** schema (application/x-protobuf)

      * ![Warning](https://dt-cdn.net/images/warning-16-56c09ccf83.png "Warning") Несовместимое изменение

        + Type changed from array to object
  + Return Type:

    - Add `502 Bad Gateway`
    - Add `504 Gateway Timeout`

### /rnMappingFiles

Добавлены новые эндпоинты Early Access:

* `GET /rnMappingFiles`

  + Extensions:

    - API maturity changed from `IN_DEVELOPMENT` to `EARLY_ADOPTER`
* `GET /rnMappingFiles/{appId}`

  + Extensions:

    - API maturity changed from `IN_DEVELOPMENT` to `EARLY_ADOPTER`
* `GET /rnMappingFiles/{appId}/{bundleName}/{platform}/{fileName}/{bundleVersion}`

  + Extensions:

    - API maturity changed from `IN_DEVELOPMENT` to `EARLY_ADOPTER`
* `PUT /rnMappingFiles/{appId}/{bundleName}/{platform}/{fileName}/{bundleVersion}`

  + Extensions:

    - API maturity changed from `IN_DEVELOPMENT` to `EARLY_ADOPTER`
* `DELETE /rnMappingFiles/{appId}/{bundleName}/{platform}/{fileName}/{bundleVersion}`

  + Extensions:

    - API maturity changed from `IN_DEVELOPMENT` to `EARLY_ADOPTER`
* `PUT /rnMappingFiles/{appId}/{bundleName}/{platform}/{fileName}/{bundleVersion}/metadata`

  + Extensions:

    - API maturity changed from `IN_DEVELOPMENT` to `EARLY_ADOPTER`

### /synthetic/nodes

* `GET /synthetic/nodes`

  + Return Type:

    - Changed 200 OK

      * Changed **Nodes** schema (application/json; charset=utf-8)

        + Changed property **nodes**

          - ![Warning](https://dt-cdn.net/images/warning-16-56c09ccf83.png "Warning") Несовместимое изменение

            * Added required property **capabilities**
* `GET /synthetic/nodes/{nodeId}`

  + Return Type:

    - Changed 200 OK

      * Changed **Node** schema (application/json; charset=utf-8)

        + ![Warning](https://dt-cdn.net/images/warning-16-56c09ccf83.png "Warning") Несовместимое изменение

          - Added required property **capabilities**

### /tokens

* `GET /tokens`

  + Parameter:

    - Changed `permissions` in query

      * Removed enum values:
        `analyzers.read`
        `analyzers.write`
* `POST /tokens`

  + Request:

    - Changed **CreateToken** schema (application/json; charset=utf-8)

      * ![Warning](https://dt-cdn.net/images/warning-16-56c09ccf83.png "Warning") Несовместимое изменение

        + Changed property **scopes**

          - Removed enum values:
            `analyzers.read`
            `analyzers.write`
* `POST /tokens/lookup`

  + Return Type:

    - Changed 200 OK

      * Changed **TokenMetadata** schema (application/json; charset=utf-8)

        + ![Warning](https://dt-cdn.net/images/warning-16-56c09ccf83.png "Warning") Несовместимое изменение

          - Changed property **scopes**

            * Removed enum values:
              `analyzers.read`
              `analyzers.write`
* `GET /tokens/{id}`

  + Return Type:

    - Changed 200 OK

      * Changed **TokenMetadata** schema (application/json; charset=utf-8)
      * ![Warning](https://dt-cdn.net/images/warning-16-56c09ccf83.png "Warning") Несовместимое изменение

        + Changed property **scopes**

          - Removed enum values:
            `analyzers.read`
            `analyzers.write`
* `PUT /tokens/{id}`

  + Request:

    - Changed **UpdateToken** schema (application/json; charset=utf-8)

      * ![Warning](https://dt-cdn.net/images/warning-16-56c09ccf83.png "Warning") Несовместимое изменение

        + Changed property **scopes**

          - Removed enum values:
            `analyzers.read`
            `analyzers.write`

## Config API

### /calculatedMetrics/service

* `POST /calculatedMetrics/service`

  + Request:

    - Changed **CalculatedServiceMetric** schema (application/json; charset=utf-8)

      * Changed property **dimensionDefinition**

        + Changed property **placeholders**

          - Changed property **source**

            * Changed property **serviceTag**

              + Removed property **tagKey**
* `POST /calculatedMetrics/service/validator`

  + Request:

    - Changed **CalculatedServiceMetric** schema (application/json; charset=utf-8)

      * Changed property **dimensionDefinition**

        + Changed property **placeholders**

          - Changed property **source**

            * Changed property **serviceTag**

              + Removed property **tagKey**
* `GET /calculatedMetrics/service/{metricKey}`

  + Return Type:

    - Changed 200 OK

      * Changed **CalculatedServiceMetric** schema (application/json; charset=utf-8)

        + ![Warning](https://dt-cdn.net/images/warning-16-56c09ccf83.png "Warning") Несовместимое изменение

          - Changed property **dimensionDefinition**

            * Changed property **placeholders**

              + Changed property **source**

                - Changed property **serviceTag**

                  * Removed property **tagKey**
* `PUT /calculatedMetrics/service/{metricKey}`

  + Request:

    - Changed **CalculatedServiceMetric** schema (application/json; charset=utf-8)

      * Changed property **dimensionDefinition**

        + Changed property **placeholders**

          - Changed property **source**

            * Changed property **serviceTag**

              + Removed property **tagKey**
* `POST /calculatedMetrics/service/{metricKey}/validator`

  + Request:

    - Changed **CalculatedServiceMetric** schema (application/json; charset=utf-8)

      * Changed property **dimensionDefinition**

        + Changed property **placeholders**

          - Changed property **source**

            * Changed property **serviceTag**

              + Removed property **tagKey**

### /extensions

Добавлен новый эндпоинт Early Access:

* `GET /extensions/{technology}/availableHosts`

  + Parameter:

    - Changed technology in path

      * Added enum value:
        `DOCKERDEAMON`

### /service/requestAttributes

* `POST /service/requestAttributes`

  + Request:

    - Changed **RequestAttribute** schema (application/json; charset=utf-8)

      * Changed property **dataSources**

        + Changed property **scope**

          - Changed property **serviceTechnology**

            * Added enum value:
              `DOCKERDEAMON`
* `POST /service/requestAttributes/validator`

  + Request:

    - Changed **RequestAttribute** schema (application/json; charset=utf-8)

      * Changed property **dataSources**

        + Changed property **scope**

          - Changed property **serviceTechnology**

            * Added enum value:
              `DOCKERDEAMON`
* `GET /service/requestAttributes/{id}`

  + Return Type:

    - Changed 200 OK

      * Changed **RequestAttribute** schema (application/json; charset=utf-8)

        + Changed property **dataSources**

          - Changed property **scope**

            * Changed property **serviceTechnology**

              + Added enum value:
                `DOCKERDEAMON`
* `PUT /service/requestAttributes/{id}`

  + Request:

    - Changed **RequestAttribute** schema (application/json; charset=utf-8)

      * Changed property **dataSources**

        + Changed property **scope**

          - Changed property **serviceTechnology**

            * Added enum value:
              `DOCKERDEAMON`
* `POST /service/requestAttributes/{id}/validator`

  + Request:

    - Changed **RequestAttribute** schema (application/json; charset=utf-8)

      * Changed property **dataSources**

        + Changed property **scope**

          - Changed property **serviceTechnology**

            * Added enum value:
              `DOCKERDEAMON`

### /service/requestNaming

* `POST /service/requestNaming`

  + Request:

    - Changed **RequestNaming** schema (application/json; charset=utf-8)

      * Changed property **placeholders**

        + Changed property **source**

          - Changed property **serviceTag**

            * Removed property **tagKey**
* `POST /service/requestNaming/validator`

  + Request:

    - Changed **RequestNaming** schema (application/json; charset=utf-8)

      * Changed property **placeholders**

        + Changed property **source**

          - Changed property **serviceTag**

            * Removed property **tagKey**
* `GET /service/requestNaming/{id}`

  + Return Type:

    - Changed 200 OK

      * Changed **RequestNaming** schema (application/json; charset=utf-8)

        + ![Warning](https://dt-cdn.net/images/warning-16-56c09ccf83.png "Warning") Несовместимое изменение

          - Changed property **placeholders**

            * Changed property **source**

              + Changed property **serviceTag**

                - Removed property **tagKey**
* `PUT /service/requestNaming/{id}`

  + Request:

    - Changed **RequestNaming** schema (application/json; charset=utf-8)

      * Changed property **placeholders**

        + Changed property **source**

          - Changed property **serviceTag**

            * Removed property **tagKey**
* `POST /service/requestNaming/{id}/validator`

  + Request:

    - Changed **RequestNaming** schema (application/json; charset=utf-8)

      * Changed property **placeholders**

        + Changed property **source**

          - Changed property **serviceTag**

            * Removed property **tagKey**