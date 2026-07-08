---
title: Dynatrace API changelog version 1.319
source: https://docs.dynatrace.com/managed/whats-new/dynatrace-api/sprint-319
---

# Dynatrace API changelog version 1.319

# Dynatrace API changelog version 1.319

* Release notes
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