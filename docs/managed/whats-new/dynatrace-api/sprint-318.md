---
title: Dynatrace API changelog version 1.318
source: https://docs.dynatrace.com/managed/whats-new/dynatrace-api/sprint-318
scraped: 2026-05-12T11:36:12.799425
---

# Dynatrace API changelog version 1.318

# Dynatrace API changelog version 1.318

* Release notes
* Published Jun 30, 2025

Rollout start: Jul 1, 2025

## Environment API

### /extensions/

* `GET /extensions/{extensionName}/monitoringConfigurations/status`

  + Extensions:

    - API maturity changed from `IN_DEVELOPMENT` to `GENERAL_AVAILABILITY`

* `GET /extensions/{extensionName}/{extensionVersion}/schema`

  + Return Type:

    - Changed 200 OK

      * Changed **SchemaDefinitionRestDto** schema

        + Changed property **deletionConstraints**

          - Added properties:  
            **schemaIds**  
            **type**
          - Added required property:  
            **type**

### /settings/schemas/

* `GET /settings/schemas/{schemaId}`

  + Return Type:

    - Changed 200 OK

      * Changed **SchemaDefinitionRestDto** schema

        + Changed property **deletionConstraints**

          - Added properties:  
            **schemaIds**  
            **type**
          - Added required property:  
            **type**

### /logs/ingest

* `POST /logs/ingest`

  + Request:

    - Added `application/jsonl`
    - Added `application/jsonl; charset=utf-8`
    - Added `application/jsonlines`
    - Added `application/jsonlines+json`
    - Added `application/jsonlines+json; charset=utf-8`
    - Added `application/jsonlines; charset=utf-8`
    - Added `application/x-jsonlines`
    - Added `application/x-jsonlines; charset=utf-8`
    - Added `application/x-ndjson`
    - Added `application/x-ndjson; charset=utf-8`

### /ua/entity

* `POST /ua/entity` Early Access

  + Return Type:

    - Changed 200 OK

      * Changed **UAEntityScreenDefinition** schema

        + Changed property **tags**

          - Added property:  
            **tagContextFilter**

## Cluster API

### /cluster

* `GET /cluster`

  + Return Type:

    - Changed 200 OK

      * Changed null schema (application/json)

        + Changed property **dnsEntryPointUris**

          - Deprecated changed to true

### /activeGates

* `GET /activeGates`

  + Parameter:

    - Add **fipsMode** in query
  + Return Type:

    - Changed 200 OK

      * Changed **ActiveGateList** schema

        + Changed property **activeGates**

          - Added property:  
            **fipsMode**
* `GET /activeGates/{agId}`

  + Return Type:

    - Changed 200 OK

      * Changed **ActiveGate** schema

        + Added property:  
          **fipsMode**

### /settings/schemas/

* `GET /settings/schemas/{schemaId}`

  + Return Type:

    - Changed 200 OK

      * Changed **SchemaDefinitionRestDto** schema

        + Changed property **deletionConstraints**

          - Added properties:  
            **schemaIds**  
            **type**
          - Added required property:  
            **type**