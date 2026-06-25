---
title: Журнал изменений Dynatrace API версии 1.320
source: https://docs.dynatrace.com/managed/whats-new/dynatrace-api/sprint-320
scraped: 2026-05-12T11:35:55.293534
---

# Журнал изменений Dynatrace API версии 1.320

# Журнал изменений Dynatrace API версии 1.320

* Заметки о выпуске
* Updated on Sep 24, 2025

Rollout start: Jul 29, 2025

## Environment API

### /entities

**Новые эндпоинты:**

* `GET /enties`

  + Response of the **MEtag** object

    - Added: **source**
    - Added: **sourceSetting**
  + Response of the **ManagementZone** object

    - Added: **sourceSetting**
* `GET /enties/{entityId}`

  + Response of the **MEtag** object

    - Added: **source**
    - Added: **sourceSetting**
  + Response of the **ManagementZone** object

    - Added: **sourceSetting**

**Объявлено устаревшим:**

* `POST /entities/securityContext`
* `DELETE /entities/securityContext`

### /entity/infrastructure/processes and /process-groups

* `GET /entity/infrastructure/process-groups`

  + Return Type:

    - Changed 200 OK

      * Changed **null** schema

        + Changed property **metadata**

          - Added properties:  
            **ibmCicsImsApplid**  
            **ibmCicsImsJobName**
* `GET /entity/infrastructure/process-groups/{meIdentifier}`

  + Return Type:

    - Changed 200 OK

      * Changed **ProcessGroup** schema

        + Changed property **metadata**

          - Added properties:  
            **ibmCicsImsApplid**  
            **ibmCicsImsJobName**
* `GET /entity/infrastructure/processes`

  + Return Type:

    - Changed 200 OK

      * Changed **null** schema

        + Changed property **metadata**

          - Added properties:  
            **ibmCicsImsApplid**  
            **ibmCicsImsJobName**
* `GET /entity/infrastructure/processes/{meIdentifier}`

  + Return Type:

    - Changed 200 OK

      * Changed **ProcessGroupInstance** schema

        + Changed property **metadata**

          - Added properties:  
            **ibmCicsImsApplid**  
            **ibmCicsImsJobName**

### /jsMappingFiles

**Новые эндпоинты:**

* `PUT /jsMappingFiles/content`
* `GET /jsMappingFiles/metadata`
* `PUT /jsMappingFiles/metadata`
* `DELETE /jsMappingFiles`

**Объявлено устаревшим:**

* `GET /jsMappingFiles`
* `PUT /jsMappingFiles/{minifiedJsFileUrl}/{fileType}`
* `DELETE /jsMappingFiles/{minifiedJsFileUrl}/{fileType}`
* `PUT /jsMappingFiles/{minifiedJsFileUrl}/{fileType}/metadata`

### /oneagents/managedRemoteCommunicationSettings

**Новые эндпоинты:**

* `POST /oneagents/managedRemoteCommunicationSettings/dryRun`
* `POST /oneagents/managedRemoteCommunicationSettings/execute`

### /rum/

**Новые эндпоинты:**

API maturity changed from `IN_DEVELOPMENT` to `EARLY_ADOPTER`

* `GET /rum/inlineCode/{applicationId}` Early Access
* `GET /rum/javaScriptTag/{applicationId}` Early Access
* `GET /rum/oneAgentJavaScriptTag/{applicationId}` Early Access
* `GET /rum/oneAgentJavaScriptTagWithSri/{applicationId}` Early Access

### /settings/schemas/

* `GET /settings/schemas/{schemaId}`

  + Return Type:

    - Changed 200 OK

      * Changed **SchemaDefinitionRestDto** schema

        + Changed property **schemaConstraints**

          - Added property:  
            **flattenCollections**

## Cluster API

### /cluster/maintenance

**Новые эндпоинты:**

* `GET /cluster/maintenance`
* `POST /cluster/maintenance/on`
* `POST /cluster/maintenance/off`

### /settings/schemas/

* `GET /settings/schemas/{schemaId}`

  + Return Type:

    - Changed 200 OK

      * Changed **SchemaDefinitionRestDto** schema

        + Changed property **schemaConstraints**

          - Added property:  
            **flattenCollections**