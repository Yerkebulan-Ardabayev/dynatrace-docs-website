---
title: Dynatrace API changelog version 1.331
source: https://docs.dynatrace.com/managed/whats-new/dynatrace-api/sprint-331
---

# Dynatrace API changelog version 1.331

# Dynatrace API changelog version 1.331

* Release notes
* Published Jan 22, 2026
* Rollout start on Jan 27, 2026

## Environment API

### /securityProblems

Rename `discontinued` to `deprecated` to match ubiquitous language.

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