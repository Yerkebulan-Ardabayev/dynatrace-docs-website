---
title: Dynatrace API changelog version 1.332
source: https://docs.dynatrace.com/managed/whats-new/dynatrace-api/sprint-332
scraped: 2026-05-12T11:35:30.714477
---

# Dynatrace API changelog version 1.332

# Dynatrace API changelog version 1.332

* Release notes
* Published Feb 02, 2026
* Rollout start on Feb 10, 2026

## Environment API

### /thresholds

Removed the following endpoints:

* `GET /thresholds`
* `PUT /thresholds/{thresholdId}`
* `DELETE /thresholds/{thresholdId}`

### /logs

Early Access Added new endpoints:

* `GET /logs/export`

  + Return Type:

    - Changed 200 OK

      * Changed **ExportedLogRecordList** schema (application/json; charset=utf-8)

        + ![Warning](https://dt-cdn.net/images/warning-16-56c09ccf83.png "Warning") Breaking change

          - Changed property **results**

            * Changed property **eventType**

              + Removed enum values:
                `K8S`
                `LOG`
                `SFM`
* `GET /logs/search`

  + Return Type:

    - Changed 200 OK

      * Changed **LogRecordsList** schema (application/json; charset=utf-8)

        + ![Warning](https://dt-cdn.net/images/warning-16-56c09ccf83.png "Warning") Breaking change

          - Changed property **results**

            * Changed property **eventType**

              + Removed enum values:
                `K8S`
                `LOG`
                `SFM`

This update may affect clients that rely on strict value matching or use code-generated models with fixed enums, as generated clients and SDKs that don't accept unknown values may require updates to handle the extended value set. We recommend ensuring your implementation can gracefully process previously unseen values to maintain forward compatibility.

Added the option to pass attributes via Query Parameters and the `X_Dynatrace_Attr` header.

* `POST /logs/ingest`

  + Parameter:

    - Add `X-Dynatrace-Attr` in header.
* `POST /otlp/v1/logs`

  + Parameter:

    - Add `X-Dynatrace-Attr` in header.

### /ua

Early Access Added new endpoints:

* `POST /ua/entity`

  + Return Type:

    - Changed 200 OK

      * Changed `UAEntityScreenDefinition` schema (application/json; charset=utf-8)

        + Changed property **eventsCard**

          - Added properties: **ignoreManagementZone**
* `POST /ua/explorer`

  + Return Type:

    - Changed 200 OK

      * Changed `UAInvExScreenDefinition` schema (application/json; charset=utf-8)

        + Changed property **eventsCard**

          - Added properties: **ignoreManagementZone**
* `POST /ua/list`

  + Return Type:

    - Changed 200 OK

      * Changed `UAListScreenDefinition` schema (application/json; charset=utf-8)

        + Changed property **eventsCard**

          - Added properties: **ignoreManagementZone**

## Cluster API

### /iam/resolution/{level-type}/{level-id}

* `GET /iam/repo/{level-type}/{level-id}/bindings/groups/{group-uuid}`

  + Return Type:

    - Changed 200 OK

      * Changed `PolicyBindingsWithDetails` schema (application/json)

        + ![Warning](https://dt-cdn.net/images/warning-16-56c09ccf83.png "Warning") Breaking change

          - Changed property **bindingsDetails**

            * Removed properties: **bindings**
* `POST /iam/resolution/{level-type}/{level-id}/effectivepermissions:dry-run`

  + Request:

    - Changed `GetEffectivePermissionsFromLevelPolicyBindings` schema (application/json)

      * Changed property **bindings**

        + Added properties: **boundaries**, **parameters**, **policyUuid**

          - Removed properties: **bindingUuid**, **groupUuid**