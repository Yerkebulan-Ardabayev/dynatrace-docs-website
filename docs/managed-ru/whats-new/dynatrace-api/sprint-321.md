---
title: Журнал изменений Dynatrace API версии 1.321
source: https://docs.dynatrace.com/managed/whats-new/dynatrace-api/sprint-321
scraped: 2026-05-12T11:36:05.168288
---

# Журнал изменений Dynatrace API версии 1.321

# Журнал изменений Dynatrace API версии 1.321

* Заметки о выпуске
* Published Jul 16, 2025

Rollout start: Aug 12, 2025

## Environment API

### /deployment/lambda/layer

* `GET /deployment/lambda/layer` Early Access

### /logs/ingest

Для универсального приёма (`/logs/ingest`) теперь можно указать content-type через параметр запроса. Значение, переданное в параметре запроса, имеет приоритет над типом, указанным в заголовке content-type.

* `POST /logs/ingest`

  + Parameter:

    - Add content-type in query