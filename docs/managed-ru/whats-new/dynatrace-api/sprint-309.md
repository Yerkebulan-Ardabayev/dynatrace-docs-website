---
title: Журнал изменений Dynatrace API версии 1.309
source: https://docs.dynatrace.com/managed/whats-new/dynatrace-api/sprint-309
scraped: 2026-05-12T11:35:51.646210
---

# Журнал изменений Dynatrace API версии 1.309

# Журнал изменений Dynatrace API версии 1.309

* Заметки о выпуске
* Published Mar 03, 2025

Rollout start: Feb 25, 2025

## Environment API

### /anonymize/anonymizationJobs

* `PUT /anonymize/anonymizationJobs`

  + Параметр:

    - Changed **additionalField** in query

      * Добавлены значения перечисления:  
        `errors.name`  
        `errors.domain`

### /synthetic/locations

* `POST /synthetic/locations`

  + Запрос:

    - Изменена схема **PrivateSyntheticLocation**

      * Удалено обязательное свойство: **nodes**

### /auditlogs

* `GET /auditlogs` Early Access

  + Возвращаемый тип:

    - Changed 200 OK

      * Изменена схема **AuditLog**

        + Изменено свойство **auditLogs**

          - Изменено свойство **eventType**

            * Добавлено значение перечисления:  
              `REORDER`
* `GET /auditlogs/{id}` Early Access

  + Возвращаемый тип:

    - Changed 200 OK

      * Изменена схема **AuditLogEntry**

        + Изменено свойство **eventType**

          - Добавлено значение перечисления:  
            `REORDER`

## Configuration API

### /applications/web

* `POST /applications/web`

  + Запрос:

    - Изменена схема **WebApplicationConfig**

      * Изменено свойство **monitoringSettings**

        + Изменено свойство **injectionMode**

          - Добавлены значения перечисления:  
            `JAVASCRIPT_TAG_COMPLETE`  
            `JAVASCRIPT_TAG_SRI`
* `GET /applications/web/default`

  + Возвращаемый тип:

    - Changed 200 OK

      * Изменена схема **WebApplicationConfig**

        + Изменено свойство **monitoringSettings**

          - Изменено свойство **injectionMode**

            * Добавлены значения перечисления:  
              `JAVASCRIPT_TAG_COMPLETE`  
              `JAVASCRIPT_TAG_SRI`
* `PUT /applications/web/default`

  + Запрос:

    - Изменена схема **WebApplicationConfig**

      * Изменено свойство **monitoringSettings**

        + Изменено свойство **injectionMode**

          - Добавлены значения перечисления:  
            `JAVASCRIPT_TAG_COMPLETE`  
            `JAVASCRIPT_TAG_SRI`
* `POST /applications/web/default/validator`

  + Запрос:

    - Изменена схема **WebApplicationConfig**

      * Изменено свойство **monitoringSettings**

        + Изменено свойство **injectionMode**

          - Добавлены значения перечисления:  
            `JAVASCRIPT_TAG_COMPLETE`  
            `JAVASCRIPT_TAG_SRI`
* `POST /applications/web/validator`

  + Запрос:

    - Изменена схема **WebApplicationConfig**

      * Изменено свойство **monitoringSettings**

        + Изменено свойство **injectionMode**

          - Добавлены значения перечисления:  
            `JAVASCRIPT_TAG_COMPLETE`  
            `JAVASCRIPT_TAG_SRI`
* `GET /applications/web/{id}`

  + Возвращаемый тип:

    - Changed 200 OK

      * Изменена схема **WebApplicationConfig**

        + Изменено свойство **monitoringSettings**

          - Изменено свойство **injectionMode**

            * Добавлены значения перечисления:  
              `JAVASCRIPT_TAG_COMPLETE`  
              `JAVASCRIPT_TAG_SRI`
* `PUT /applications/web/{id}`

  + Запрос:

    - Изменена схема **WebApplicationConfig**

      * Изменено свойство **monitoringSettings**

        + Изменено свойство **injectionMode**

          - Добавлены значения перечисления:  
            `JAVASCRIPT_TAG_COMPLETE`  
            `JAVASCRIPT_TAG_SRI`
* `POST /applications/web/{id}/validator`

  + Запрос:

    - Изменена схема **WebApplicationConfig**

      * Изменено свойство **monitoringSettings**

        + Изменено свойство **injectionMode**

          - Добавлены значения перечисления:  
            `JAVASCRIPT_TAG_COMPLETE`  
            `JAVASCRIPT_TAG_SRI`