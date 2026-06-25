---
title: Журнал изменений Dynatrace API версии 1.313
source: https://docs.dynatrace.com/managed/whats-new/dynatrace-api/sprint-313
scraped: 2026-05-12T11:36:13.983770
---

# Журнал изменений Dynatrace API версии 1.313

# Журнал изменений Dynatrace API версии 1.313

* Заметки о выпуске
* Published Apr 24, 2025

Rollout start: Apr 22, 2025

## Environment API

### /extensions/{extensionName}/environmentConfiguration/assets/

* `GET /extensions/{extensionName}/environmentConfiguration/assets/alertTemplates/{assetId}` Новый раздел!

* `GET /extensions/{extensionName}/environmentConfiguration/assets`

  + Return Type:

    - Changed 200 OK

      * Changed **ExtensionAssetsDto** schema

        + Changed property **assets**

          - Changed property **type**

            * Added enum value:  
              `ALERT_TEMPLATE`

### /credentials/

* `POST /credentials`

  + Request:

    - Changed **Credentials** schema

      * ![Warning](https://dt-cdn.net/images/warning-16-56c09ccf83.png "Warning") Несовместимое изменение

        + Added required property:  
          `type`
* `PUT /credentials/{id}`

  + Request:

    - Changed **Credentials** schema

      * ![Warning](https://dt-cdn.net/images/warning-16-56c09ccf83.png "Warning") Несовместимое изменение

        + Added required property:  
          `type`

### /extensions/{extensionName}/{extensionVersion}/schema

* `GET /extensions/{extensionName}/{extensionVersion}/schema`

  + Return Type:

    - Changed 200 OK

      * Changed **SchemaDefinitionRestDto** schema

        + Changed property **schemaConstraints**

          - Added properties: **byteLimit**
          - Changed property **type**

            * Added enum value:  
              `BYTE_SIZE_LIMIT`

### /settings/schemas/{schemaId}

* `GET /settings/schemas/{schemaId}`

  + Return Type:

    - Changed 200 OK

      * Changed **SchemaDefinitionRestDto** schema

        + Changed property **schemaConstraints**

          - Added properties: **byteLimit**
          - Changed property **type**

            * Added enum value:  
              `BYTE_SIZE_LIMIT`

### /metrics

* `GET /metrics`

  + Return Type:

    - Changed 200 OK

      * Changed **MetricDescriptorCollection** schema

        + Changed property **metrics**

          - Changed property **transformations**

            * Added enum value:  
              `histogram`
        + Changed **MetricDescriptorCollection** schema

          - Changed property **metrics**

            * Changed property **transformations**

              + Added enum value:  
                `histogram`
        + Changed **MetricDescriptorCollection** schema

          - Changed property **metrics**

            * Changed property **transformations**

              + Added enum value:  
                `histogram`
* `GET /metrics/{metricKey}`

  + Return Type:

    - Changed 200 OK

      * Changed **MetricDescriptor** schema

        + Changed property **transformations**

          - Added enum value:  
            `histogram`
        + Changed **MetricDescriptor** schema

          - Changed property **transformations**

            * Added enum value:  
              `histogram`
        + Changed **MetricDescriptor** schema

          - Changed property **transformations**

            * Added enum value:  
              `histogram`

### /ua/

* `POST /ua/entity` Early Access

  + Return Type:

    - Changed 200 OK

      * Changed UAEntityScreenDefinition schema

        + Changed property **metricsMetadata**

          - Changed schema of dictionary value:

            * Changed property **transformations**

              + Added enum value:  
                `histogram`
* `POST /ua/list` Early Access

  + Return Type:

    - Changed 200 OK

      * Changed UAListScreenDefinition schema

        + Changed property **metricsMetadata**

          - Changed schema of dictionary value:

            * Changed property **transformations**

              + Added enum value:  
                `histogram`

## Configuration API

### /credentials/

* `POST /credentials`

  + Request:

    - Changed **Credentials** schema

      * ![Warning](https://dt-cdn.net/images/warning-16-56c09ccf83.png "Warning") Несовместимое изменение

        + Added required property: **type**
* `PUT /credentials/{id}`

  + Request:

    - Changed **Credentials** schema

      * ![Warning](https://dt-cdn.net/images/warning-16-56c09ccf83.png "Warning") Несовместимое изменение

        + Added required property: **type**