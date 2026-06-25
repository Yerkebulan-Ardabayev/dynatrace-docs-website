---
title: Журнал изменений Dynatrace API версии 1.319
source: https://docs.dynatrace.com/managed/whats-new/dynatrace-api/sprint-319
scraped: 2026-05-12T11:35:56.435195
---

# Журнал изменений Dynatrace API версии 1.319

# Журнал изменений Dynatrace API версии 1.319

* Заметки о выпуске
* Published Jul 16, 2025

Rollout start: Jul 15, 2025

## Environment API

### /monitoringstate

* `GET /monitoringstate`

  + Return Type:

    - Changed 200 OK

      * Changed **MonitoredStates** schema

        + Changed property **monitoringStates**

          - Changed property **state**

            * Added enum value:  
              `process_group_pgr_group_update_suppressed`