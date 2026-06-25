---
title: Журнал изменений Dynatrace API версии 1.335
source: https://docs.dynatrace.com/managed/whats-new/dynatrace-api/sprint-335
scraped: 2026-05-12T11:35:42.965778
---

# Журнал изменений Dynatrace API версии 1.335

# Журнал изменений Dynatrace API версии 1.335

* Заметки о выпуске
* Published Mar 16, 2026
* Rollout start on Mar 24, 2026

## Environment API

### /ua

Early Access: Изменены типы возвращаемых данных:

* `POST /ua/entity`

  + Return Type:

    - Changed 200 OK

      * Changed **UAEntityScreenDefinition** schema (application/json; charset=utf-8)

        + Changed property **chartGroups**

          - Changed property **charts**

            * Changed property **visualizationType**

              + Added enum values: `HISTOGRAM`
        + Changed property **entitiesLists**

          - Changed property **charts**

            * Changed property **visualizationType**

              + Added enum values: `HISTOGRAM`
        + Changed property **metricTables**

          - Changed property **charts**

            * Changed property **visualizationType**

              + Added enum values: `HISTOGRAM`
* `POST /ua/explorer`

  + Return Type:

    - Changed 200 OK

      * Changed **UAInvExScreenDefinition** schema (application/json; charset=utf-8)

        + Changed property **chartGroups**

          - Changed property **charts**

            * Changed property **visualizationType**

              + Added enum values: `HISTOGRAM`
* `POST /ua/list`

  + Return Type:

    - Changed 200 OK

      * Changed **UAListScreenDefinition** schema (application/json; charset=utf-8)

        + Changed property **chartGroups**

          - Changed property **charts**

            * Changed property **visualizationType**

              + Added enum values: `HISTOGRAM`
        + Changed property **entitiesLists**

          - Changed property **charts**

            * Changed property **visualizationType**

              + Added enum values: `HISTOGRAM`