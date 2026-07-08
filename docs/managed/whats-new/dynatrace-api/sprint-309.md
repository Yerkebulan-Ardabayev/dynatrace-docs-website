---
title: Dynatrace API changelog version 1.309
source: https://docs.dynatrace.com/managed/whats-new/dynatrace-api/sprint-309
---

# Dynatrace API changelog version 1.309

# Dynatrace API changelog version 1.309

* Release notes
* Published Mar 03, 2025

Rollout start: Feb 25, 2025

## Environment API

### /anonymize/anonymizationJobs

* `PUT /anonymize/anonymizationJobs`

  + Parameter:

    - Changed **additionalField** in query

      * Added enum values:  
        `errors.name`  
        `errors.domain`

### /synthetic/locations

* `POST /synthetic/locations`

  + Request:

    - Changed **PrivateSyntheticLocation** schema

      * Removed required property: **nodes**

### /auditlogs

* `GET /auditlogs` Early Access

  + Return Type:

    - Changed 200 OK

      * Changed **AuditLog** schema

        + Changed property **auditLogs**

          - Changed property **eventType**

            * Added enum value:  
              `REORDER`
* `GET /auditlogs/{id}` Early Access

  + Return Type:

    - Changed 200 OK

      * Changed **AuditLogEntry** schema

        + Changed property **eventType**

          - Added enum value:  
            `REORDER`

## Configuration API

### /applications/web

* `POST /applications/web`

  + Request:

    - Changed **WebApplicationConfig** schema

      * Changed property **monitoringSettings**

        + Changed property **injectionMode**

          - Added enum values:  
            `JAVASCRIPT_TAG_COMPLETE`  
            `JAVASCRIPT_TAG_SRI`
* `GET /applications/web/default`

  + Return Type:

    - Changed 200 OK

      * Changed **WebApplicationConfig** schema

        + Changed property **monitoringSettings**

          - Changed property **injectionMode**

            * Added enum values:  
              `JAVASCRIPT_TAG_COMPLETE`  
              `JAVASCRIPT_TAG_SRI`
* `PUT /applications/web/default`

  + Request:

    - Changed **WebApplicationConfig** schema

      * Changed property **monitoringSettings**

        + Changed property **injectionMode**

          - Added enum values:  
            `JAVASCRIPT_TAG_COMPLETE`  
            `JAVASCRIPT_TAG_SRI`
* `POST /applications/web/default/validator`

  + Request:

    - Changed **WebApplicationConfig** schema

      * Changed property **monitoringSettings**

        + Changed property **injectionMode**

          - Added enum values:  
            `JAVASCRIPT_TAG_COMPLETE`  
            `JAVASCRIPT_TAG_SRI`
* `POST /applications/web/validator`

  + Request:

    - Changed **WebApplicationConfig** schema

      * Changed property **monitoringSettings**

        + Changed property **injectionMode**

          - Added enum values:  
            `JAVASCRIPT_TAG_COMPLETE`  
            `JAVASCRIPT_TAG_SRI`
* `GET /applications/web/{id}`

  + Return Type:

    - Changed 200 OK

      * Changed **WebApplicationConfig** schema

        + Changed property **monitoringSettings**

          - Changed property **injectionMode**

            * Added enum values:  
              `JAVASCRIPT_TAG_COMPLETE`  
              `JAVASCRIPT_TAG_SRI`
* `PUT /applications/web/{id}`

  + Request:

    - Changed **WebApplicationConfig** schema

      * Changed property **monitoringSettings**

        + Changed property **injectionMode**

          - Added enum values:  
            `JAVASCRIPT_TAG_COMPLETE`  
            `JAVASCRIPT_TAG_SRI`
* `POST /applications/web/{id}/validator`

  + Request:

    - Changed **WebApplicationConfig** schema

      * Changed property **monitoringSettings**

        + Changed property **injectionMode**

          - Added enum values:  
            `JAVASCRIPT_TAG_COMPLETE`  
            `JAVASCRIPT_TAG_SRI`