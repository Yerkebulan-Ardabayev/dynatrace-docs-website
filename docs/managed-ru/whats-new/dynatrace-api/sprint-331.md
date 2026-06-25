---
title: Журнал изменений Dynatrace API версии 1.331
source: https://docs.dynatrace.com/managed/whats-new/dynatrace-api/sprint-331
scraped: 2026-05-12T11:35:33.086309
---

# Журнал изменений Dynatrace API версии 1.331

# Журнал изменений Dynatrace API версии 1.331

* Заметки о выпуске
* Published Jan 22, 2026
* Rollout start on Jan 27, 2026

## Environment API

### /securityProblems

Переименование `discontinued` в `deprecated` для соответствия принятой терминологии.

```
- GET    /securityProblems/{id}



Return Type:



- Changed 200 OK



Changed SecurityProblemDetails schema (application/json; charset=utf-8)



Broken compatibility



- Changed property [events]



- Changed property [reason]



- Added enum values: [VULNERABILITY_DEPRECATED]



- Removed enum values: [VULNERABILITY_DISCONTINUED]



- GET    /securityProblems/{id}/events



Return Type:



- Changed 200 OK



Changed SecurityProblemEventsList schema (application/json; charset=utf-8)



Broken compatibility



- Changed property [events]



- Changed property [reason]



- Added enum values: [VULNERABILITY_DEPRECATED]



- Removed enum values: [VULNERABILITY_DISCONTINUED]
```