---
title: Журнал изменений Dynatrace API версии 1.329
source: https://docs.dynatrace.com/managed/whats-new/dynatrace-api/sprint-329
scraped: 2026-05-12T11:36:16.394057
---

# Журнал изменений Dynatrace API версии 1.329

# Журнал изменений Dynatrace API версии 1.329

* Заметки о выпуске
* Published Nov 27, 2025
* Rollout start on Dec 09, 2025

## Environment API

### /deployment/lambda/layer

* `GET /deployment/lambda/layer`

  Extensions:

  + API maturity changed from `EARLY_ADOPTER` to `GENERAL_AVAILABILITY`

### /metrics

Добавлен новый эндпоинт:

* `DELETE /metrics`

Изменён существующий эндпоинт:

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