---
title: Журнал изменений Dynatrace API версии 1.328
source: https://docs.dynatrace.com/managed/whats-new/dynatrace-api/sprint-328
scraped: 2026-05-12T11:35:48.106733
---

# Журнал изменений Dynatrace API версии 1.328

# Журнал изменений Dynatrace API версии 1.328

* Заметки о выпуске
* Published Nov 12, 2025
* Rollout start on Nov 20, 2025

## Environment API

### /synthetic/locations/metricAdapter

Early Access: Добавлены новые эндпоинты:

* `GET /synthetic/locations/metricAdapter/commands/apply (EARLY_ADOPTER)`
* `GET /synthetic/locations/metricAdapter/commands/delete (EARLY_ADOPTER)`
* `GET /synthetic/locations/metricAdapter/yaml (EARLY_ADOPTER)`

### /synthetic/locations

Существующие эндпоинты переведены в общую доступность:

* `GET /synthetic/locations/commands/apply`

  Extensions:

  + API maturity changed from EARLY\_ADOPTER to GENERAL\_AVAILABILITY
* `GET /synthetic/locations/{locationId}/commands/delete`

  Extensions:

  + API maturity changed from EARLY\_ADOPTER to GENERAL\_AVAILABILITY
* `GET /synthetic/locations/{locationId}/yaml`

  Extensions:

  + API maturity changed from EARLY\_ADOPTER to GENERAL\_AVAILABILITY

### /rum/cookieNames

* `GET /rum/cookieNames`

  Return Type:

  + Changed 200 OK

    Changed **CookieNames** schema (application/json; charset=utf-8)

    - Added properties:

      **domainValidationCookieName**  
      **sessionTimeoutCookieName**  
      **sourceActionCookieName**

### /securityProblems/{id}

* `GET /securityProblems/{id}`

  Return Type:

  + Changed 200 OK

    Changed **SecurityProblemDetails** schema (application/json; charset=utf-8)

    - Changed property **events**

      * Changed property **reason**

        + Added enum values:

          `VULNERABILITY_DISCONTINUED`  
          `VULNERABILITY_ID_CHANGED`
* `GET /securityProblems/{id}/events`

  Return Type:

  + Changed 200 OK

    Changed **SecurityProblemEventsList** schema (application/json; charset=utf-8)

    - Changed property **events**

      * Changed property **reason**

        + Added enum values:

          `VULNERABILITY_DISCONTINUED`  
          `VULNERABILITY_ID_CHANGED`

### /extensions/{extensionName}/{extensionVersion}/schema

* `GET /extensions/{extensionName}/{extensionVersion}/schema`

  Return Type:

  + Changed 200 OK

    Changed **SchemaDefinitionRestDto** schema (application/json; charset=utf-8)

    - Added properties **maturity**
    - Added required properties **maturity**
* `GET /settings/schemas`

  Return Type:

  + Changed 200 OK

    Changed **SchemaList** schema (application/json; charset=utf-8)

    - Changed property **items**

      * Added properties **maturity**
* `GET /settings/schemas/{schemaId}`

  Return Type:

  + Changed 200 OK

    Changed **SchemaDefinitionRestDto** schema (application/json; charset=utf-8)

    - Added properties **maturity**
    - Added required properties **maturity**

## Cluster API

### /clusterLicense Early Access

* `GET /clusterLicense (EARLY_ADOPTER)`

  Return Type:

  + Changed 200 OK

    Changed **ClusterLicense** schema (application/json; charset=utf-8)

    - Added properties:

      **licenseName**

  Extensions:

  + API maturity changed from PREVIEW to EARLY\_ADOPTER
* `GET /clusterLicense/environment/total (EARLY_ADOPTER)`

  Extensions:

  + API maturity changed from IN\_DEVELOPMENT to EARLY\_ADOPTER
* `POST /clusterLicense/key (EARLY_ADOPTER)`

  Extensions:

  + API maturity changed from IN\_DEVELOPMENT to EARLY\_ADOPTER
* `POST /clusterLicense/upload (EARLY_ADOPTER)`

  Extensions:

  + API maturity changed from IN\_DEVELOPMENT to EARLY\_ADOPTER