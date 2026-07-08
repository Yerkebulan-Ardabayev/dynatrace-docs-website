---
title: Dynatrace API changelog version 1.308
source: https://docs.dynatrace.com/managed/whats-new/dynatrace-api/sprint-308
---

# Dynatrace API changelog version 1.308

# Dynatrace API changelog version 1.308

* Release notes
* Published Feb 13, 2025

Rollout start: Feb 11, 2025

## Environment API

### /settings/history

* `GET /settings/history`

  + Return Type:

    - Changed 200 OK

      * Changed **RevisionDiffPage** schema

        + Changed property **items**

          - Added property:  
            **source**

### /synthetic/locations

* `GET /synthetic/locations`

  + Return Type:

    - Changed 200 OK

      * Changed **SyntheticLocations** schema

        + Changed property **locations**

          - Added properties:  
            **deploymentType**  
            **lastModificationTimestamp**

## Cluster API

### /synthetic/locations

* `GET /synthetic/locations`

  + Return Type:

    - Changed 200 OK

      * Changed **SyntheticLocations** schema

        + Changed property **locations**

          - Added properties:  
            **deploymentType**  
            **lastModificationTimestamp**

## Related topics

* [SaaS Release Notes 1.308﻿](https://docs.dynatrace.com/docs/shortlink/release-notes-saas-sprint-308)