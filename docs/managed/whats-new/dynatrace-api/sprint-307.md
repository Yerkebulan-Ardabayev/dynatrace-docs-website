---
title: Dynatrace API changelog version 1.307
source: https://docs.dynatrace.com/managed/whats-new/dynatrace-api/sprint-307
---

# Dynatrace API changelog version 1.307

# Dynatrace API changelog version 1.307

* Release notes
* Published Jan 31, 2025

Rollout start: Jan 28, 2025

## Environment API

### /deployment/public/network

New!

* `GET /deployment/public/network`

### /deployment/installer/agent/connectioninfo

![Warning](https://dt-cdn.net/images/warning-16-56c09ccf83.png "Warning") Breaking change

* `GET /deployment/installer/agent/connectioninfo`

  + Return Type:

    - Changed 200 OK

      * Changed **ConnectionInfo** schema

        + Broken compatibility

          - Changed property **formattedCommunicationEndpoints**

            * Type changed from array to string

### /oneagents/autoUpdateProblems

API maturity changed.

* `GET /oneagents/autoUpdateProblems`

  + Extensions:

    - API maturity changed from `EARLY_ADOPTER` to `GENERAL_AVAILABILITY`
* `DELETE /oneagents/autoUpdateProblems`

  + Extensions:

    - API maturity changed from `EARLY_ADOPTER` to `GENERAL_AVAILABILITY`

### /auditlogs

Early Access

* `GET /auditlogs`

  + Return Type:

    - Changed 200 OK

      * Changed **AuditLog** schema

        + Changed property **auditLogs**

          - Changed property **category**

            * Added enum value:  
              `BUILD_UNIT_V2`
* `GET /auditlogs/{id}`

  + Return Type:

    - Changed 200 OK

      * Changed **AuditLogEntry** schema

        + Changed property **category**

          - Added enum value:  
            `BUILD_UNIT_V2`

### /extensions/

* `GET /extensions/{extensionName}/environmentConfiguration/assets`

  + Return Type:

    - Changed 200 OK

      * Changed **ExtensionAssetsDto** schema

        + Changed property **assets**

          - Changed property **type**

            * Added enum value:  
              `DOCUMENT_DASHBOARD`

### /synthetic/locations

* `GET /synthetic/locations`

  + Parameter:

    - Changed capability in query

      * Added enum value:  
        `HTTP_HIGH_RESOURCE`

### /settings/history

* `GET /settings/history`

  + Return Type:

    - Changed 200 OK

      * Changed **RevisionDiffPage** schema

        + Changed property **items**

          - Added properties:  
            **appId**  
            **schemaDisplayName**  
            **schemaId**  
            **summary**

## Related topics

* [SaaS Release Notes 1.307﻿](https://docs.dynatrace.com/docs/shortlink/release-notes-saas-sprint-307)