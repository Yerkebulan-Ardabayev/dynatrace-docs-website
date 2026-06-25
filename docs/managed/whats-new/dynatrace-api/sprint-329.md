---
title: Dynatrace API changelog version 1.329
source: https://docs.dynatrace.com/managed/whats-new/dynatrace-api/sprint-329
scraped: 2026-05-12T11:36:16.394057
---

# Dynatrace API changelog version 1.329

# Dynatrace API changelog version 1.329

* Release notes
* Published Nov 27, 2025
* Rollout start on Dec 09, 2025

## Environment API

### /deployment/lambda/layer

* `GET /deployment/lambda/layer`

  Extensions:

  + API maturity changed from `EARLY_ADOPTER` to `GENERAL_AVAILABILITY`

### /metrics

Added new endpoint:

* `DELETE /metrics`

Modified existing endpoint:

* `GET /metrics`

  Parameter:

  + Add `writtenSinceMode` in query

### /settings/history

* `GET /settings/history`

  Return Type:

  + Changed 200 OK
    Changed **RevisionDiffPage** schema (application/json; charset=utf-8)

    - Changed property **items**

      * Added properties:  
        **ownerAfter**  
        **ownerBefore**