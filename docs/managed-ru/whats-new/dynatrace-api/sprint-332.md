---
title: Журнал изменений Dynatrace API версии 1.332
source: https://docs.dynatrace.com/managed/whats-new/dynatrace-api/sprint-332
scraped: 2026-05-12T11:35:30.714477
---

# Журнал изменений Dynatrace API версии 1.332

# Журнал изменений Dynatrace API версии 1.332

* Заметки о выпуске
* Published Feb 02, 2026
* Rollout start on Feb 10, 2026

## Environment API

### /thresholds

Удалены следующие эндпоинты:

* `GET /thresholds`
* `PUT /thresholds/{thresholdId}`
* `DELETE /thresholds/{thresholdId}`

### /logs

Early Access: Добавлены новые эндпоинты:

* `GET /logs/export`

  + Return Type:

    - Changed 200 OK

      * Changed **ExportedLogRecordList** schema (application/json; charset=utf-8)

        + ![Warning](https://dt-cdn.net/images/warning-16-56c09ccf83.png "Warning") Несовместимое изменение

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

        + ![Warning](https://dt-cdn.net/images/warning-16-56c09ccf83.png "Warning") Несовместимое изменение

          - Changed property **results**

            * Changed property **eventType**

              + Removed enum values:
                `K8S`
                `LOG`
                `SFM`

Это обновление может затронуть клиентов, которые полагаются на строгое сопоставление значений или используют сгенерированные кодом модели с фиксированными перечислениями, поскольку сгенерированные клиенты и SDK, не принимающие неизвестные значения, могут потребовать обновлений для обработки расширенного набора значений. Рекомендуется убедиться, что ваша реализация может корректно обрабатывать ранее не встречавшиеся значения для обеспечения прямой совместимости.

Добавлена возможность передачи атрибутов через параметры запроса и заголовок `X_Dynatrace_Attr`.

* `POST /logs/ingest`

  + Parameter:

    - Add `X-Dynatrace-Attr` in header.
* `POST /otlp/v1/logs`

  + Parameter:

    - Add `X-Dynatrace-Attr` in header.

### /ua

Early Access: Добавлены новые эндпоинты:

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

        + ![Warning](https://dt-cdn.net/images/warning-16-56c09ccf83.png "Warning") Несовместимое изменение

          - Changed property **bindingsDetails**

            * Removed properties: **bindings**
* `POST /iam/resolution/{level-type}/{level-id}/effectivepermissions:dry-run`

  + Request:

    - Changed `GetEffectivePermissionsFromLevelPolicyBindings` schema (application/json)

      * Changed property **bindings**

        + Added properties: **boundaries**, **parameters**, **policyUuid**

          - Removed properties: **bindingUuid**, **groupUuid**