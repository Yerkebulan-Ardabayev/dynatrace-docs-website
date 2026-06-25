---
title: Журнал изменений Dynatrace API версии 1.307
source: https://docs.dynatrace.com/managed/whats-new/dynatrace-api/sprint-307
scraped: 2026-05-12T11:35:28.174056
---

# Журнал изменений Dynatrace API версии 1.307

# Журнал изменений Dynatrace API версии 1.307

* Заметки о выпуске
* Published Jan 31, 2025

Rollout start: Jan 28, 2025

## Environment API

### /deployment/public/network

Новый раздел!

* `GET /deployment/public/network`

### /deployment/installer/agent/connectioninfo

![Warning](https://dt-cdn.net/images/warning-16-56c09ccf83.png "Warning") Несовместимое изменение

* `GET /deployment/installer/agent/connectioninfo`

  + Возвращаемый тип:

    - Changed 200 OK

      * Изменена схема **ConnectionInfo**

        + Нарушение совместимости

          - Изменено свойство **formattedCommunicationEndpoints**

            * Тип изменён с array на string

### /oneagents/autoUpdateProblems

Изменена зрелость API.

* `GET /oneagents/autoUpdateProblems`

  + Расширения:

    - Зрелость API изменена с `EARLY_ADOPTER` на `GENERAL_AVAILABILITY`
* `DELETE /oneagents/autoUpdateProblems`

  + Расширения:

    - Зрелость API изменена с `EARLY_ADOPTER` на `GENERAL_AVAILABILITY`

### /auditlogs

Early Access

* `GET /auditlogs`

  + Возвращаемый тип:

    - Changed 200 OK

      * Изменена схема **AuditLog**

        + Изменено свойство **auditLogs**

          - Изменено свойство **category**

            * Добавлено значение перечисления:  
              `BUILD_UNIT_V2`
* `GET /auditlogs/{id}`

  + Возвращаемый тип:

    - Changed 200 OK

      * Изменена схема **AuditLogEntry**

        + Изменено свойство **category**

          - Добавлено значение перечисления:  
            `BUILD_UNIT_V2`

### /extensions/

* `GET /extensions/{extensionName}/environmentConfiguration/assets`

  + Возвращаемый тип:

    - Changed 200 OK

      * Изменена схема **ExtensionAssetsDto**

        + Изменено свойство **assets**

          - Изменено свойство **type**

            * Добавлено значение перечисления:  
              `DOCUMENT_DASHBOARD`

### /synthetic/locations

* `GET /synthetic/locations`

  + Параметр:

    - Changed capability in query

      * Добавлено значение перечисления:  
        `HTTP_HIGH_RESOURCE`

### /settings/history

* `GET /settings/history`

  + Возвращаемый тип:

    - Changed 200 OK

      * Изменена схема **RevisionDiffPage**

        + Изменено свойство **items**

          - Добавлены свойства:  
            **appId**  
            **schemaDisplayName**  
            **schemaId**  
            **summary**

## Связанные темы

* [Заметки о выпуске SaaS 1.307](https://docs.dynatrace.com/docs/shortlink/release-notes-saas-sprint-307)