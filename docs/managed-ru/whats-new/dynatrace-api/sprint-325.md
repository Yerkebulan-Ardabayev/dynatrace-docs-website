---
title: Журнал изменений Dynatrace API версии 1.325
source: https://docs.dynatrace.com/managed/whats-new/dynatrace-api/sprint-325
scraped: 2026-05-12T11:35:24.604051
---

# Журнал изменений Dynatrace API версии 1.325

# Журнал изменений Dynatrace API версии 1.325

* Заметки о выпуске
* Published Sep 30, 2025
* Rollout start on Oct 07, 2025

## Environment API

### Прекращение поддержки AMP

Создание AMP-приложений через веб-интерфейс Dynatrace или API больше невозможно.

* `GET /entity/applications`
  Return Type:

  + Changed 200 OK
    Changed null schema (application/json; charset=utf-8)
    Broken compatibility

    - Changed property **applicationType**

      * Removed enum value: `AMP`
* `GET /entity/applications/{meIdentifier}`
  Return Type:

  + Changed 200 OK
    Changed **Application** schema (application/json; charset=utf-8)
    Broken compatibility

    - Changed property **applicationType**

      * Removed enum value: `AMP`
* `GET /entity/services`
  Return Type:

  + Changed 200 OK
    Changed null schema (application/json; charset=utf-8)
    Broken compatibility

    - Changed property **serviceType**

      * Removed enum value: `AMP`
* `GET /entity/services/{meIdentifier}`
  Return Type:

  + Changed 200 OK
    Changed **Service** schema (application/json; charset=utf-8)
    Broken compatibility

    - Changed property **serviceType**

      * Removed enum value: `AMP`
* `GET /userSessionQueryLanguage/table`
  Return Type:

  + Changed 199 null
    Changed **UserSession** schema (application/json)
    Broken compatibility

    - Changed property **applicationType**

      * Removed enum value: `AMP_APPLICATION`
* `GET /userSessionQueryLanguage/tree`
  Return Type:

  + Changed 199 null
    Changed **UserSession** schema (application/json)
    Broken compatibility

    - Changed property **applicationType**

      * Removed enum value: `AMP_APPLICATION`

### Новый тип события WARNING

* `GET /events`
  Parameter:

  + Changed eventType in query

    - Added enum value: `WARNING`
      Return Type:
  + Changed 200 OK
    Changed **EventQueryResult** schema (application/json)

    - Changed property **events**

      * Changed property **eventType**

        + Added enum value: `WARNING`
* `GET /events/{eventId}`
  Return Type:

  + Changed 200 OK
    Changed **EventRestEntry** schema (application/json)

    - Changed property **eventType**

      * Added enum value: `WARNING`
* `GET /problem/details/{problemId}`
  Return Type:

  + Changed 200 OK
    Changed **ProblemDetailsResultWrapper** schema (application/json; charset=utf-8)

    - Changed property **result**

      * Changed property **rankedEvents**

        + Changed property **eventType**

          - Added enum value: `WARNING`
      * Changed property **rankedImpacts**

        + Changed property **eventType**

          - Added enum value: `WARNING`
* `GET /problem/feed`
  Return Type:

  + Changed 200 OK
    Changed **ProblemFeedResultWrapper** schema (application/json; charset=utf-8)

    - Changed property **result**

      * Changed property **problems**

        + Changed property **rankedEvents**

          - Changed property **eventType**

            * Added enum value: `WARNING`
        + Changed property **rankedImpacts**

          - Changed property **eventType**

            * Added enum value: `WARNING`
* `GET /thresholds`
  Return Type:

  + Changed 200 OK
    Changed null schema (application/json; charset=utf-8)

    - Changed property **eventType**

      * Added enum value: `WARNING`
* `PUT /thresholds/{thresholdId}`
  Return Type:

  + Changed 201 Created
    Changed **Threshold** schema (application/json; charset=utf-8)

    - Changed property **eventType**

      * Added enum value: `WARNING`
* `POST /events/ingest`
  Request:
  Changed **EventIngest** schema (application/json; charset=utf-8)

  + Changed property **eventType**

    - Added enum value: `WARNING`

### Новое значение reasonForNoSessionReplay после загрузки документа

* `GET /userSessionQueryLanguage/table`
  Return Type:

  + Changed 199 null
    Changed **UserSession** schema (application/json)

    - Changed property **reasonForNoSessionReplay**

      * Added enum value: `UNKNOWN_DOC_LOADED`
* `GET /userSessionQueryLanguage/tree`
  Return Type:

  + Changed 199 null
    Changed **UserSession** schema (application/json)
    Broken compatibility

    - Changed property **reasonForNoSessionReplay**

      * Added enum value: `UNKNOWN_DOC_LOADED`

### OneAgent remote configuration management API: описания ошибок в ответе

* `POST /activeGates/remoteConfigurationManagement`
  Return Type:

  + Changed 201 Created
    Changed **RemoteConfigurationManagementJob** schema (application/json; charset=utf-8)

    - Added property: **inProgressEntities**
* `GET /activeGates/remoteConfigurationManagement/current`
  Return Type:

  + Changed 200 OK
    Changed **RemoteConfigurationManagementJob** schema (application/json; charset=utf-8)

    - Added property: **inProgressEntities**
* `GET /activeGates/remoteConfigurationManagement/{id}`
  Return Type:

  + Changed 200 OK
    Changed **RemoteConfigurationManagementJob** schema (application/json; charset=utf-8)

    - Added property: **inProgressEntities**
  + `POST /oneagents/managedRemoteCommunicationSettings/dryRun`
    Return Type:

    - Changed 201 Created
      Changed **RemoteConfigurationManagementJob** schema (application/json; charset=utf-8)

      * Added property: **inProgressEntities**
* `POST /oneagents/managedRemoteCommunicationSettings/execute`
  Return Type:

  + Changed 201 Created
    Changed **RemoteConfigurationManagementJob** schema (application/json; charset=utf-8)

    - Added property: **inProgressEntities**
* `POST /oneagents/remoteConfigurationManagement`
  Return Type:

  + Changed 201 Created
    Changed **RemoteConfigurationManagementJob** schema (application/json; charset=utf-8)

    - Added property: **inProgressEntities**
* `GET /oneagents/remoteConfigurationManagement/current`
  Return Type:

  + Changed 200 OK
    Changed **RemoteConfigurationManagementJob** schema (application/json; charset=utf-8)

    - Added property: **inProgressEntities**
* `GET /oneagents/remoteConfigurationManagement/{id}`
  Return Type:

  + Changed 200 OK
    Changed **RemoteConfigurationManagementJob** schema (application/json; charset=utf-8)

    - Added property: **inProgressEntities**

### Таймаут валидации добавлен в метасхему service-settings

* `GET /extensions/{extensionName}/{extensionVersion}/schema`
  Return Type:

  + Changed 200 OK
    Changed **SchemaDefinitionRestDto** schema (application/json; charset=utf-8)

    - Changed property **constraints**

      * Added property: **timeout**
    - Changed property **deletionConstraints**

      * Added property: **timeout**
    - Changed property **properties**

      * Changed schema of dictionary value:

        + Changed property **constraints**

          - Added property: **timeout**
        + Changed property **items**

          - Changed property **constraints**

            * Added property: **timeout**
    - Changed property **types**

      * Changed schema of dictionary value:

        + Changed property **constraints**

          - Added property: **timeout**
        + Changed property **properties**

          - Changed schema of dictionary value:

            * Changed property **constraints**

              + Added property: **timeout**
            * Changed property **items**

              + Changed property **constraints**

                - Added property: **timeout**
* `GET /settings/schemas/{schemaId}`
  Return Type:

  + Changed 200 OK
    Changed **SchemaDefinitionRestDto** schema (application/json; charset=utf-8)

    - Changed property **constraints**

      * Added property: **timeout**
    - Changed property **deletionConstraints**

      * Added property: **timeout**
    - Changed property **properties**

      * Changed schema of dictionary value:

        + Changed property **constraints**

          - Added property: **timeout**
        + Changed property **items**

          - Changed property **constraints**

            * Added property: **timeout**
    - Changed property **types**

      * Changed schema of dictionary value:

        + Changed property **constraints**

          - Added property: **timeout**
        + Changed property **properties**

          - Changed schema of dictionary value:

            * Changed property **constraints**

              + Added property: **timeout**
            * Changed property **items**

              + Changed property **constraints**

                - Added property: **timeout**