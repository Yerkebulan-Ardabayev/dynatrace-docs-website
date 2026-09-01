---
title: Dynatrace API changelog version 1.345
source: https://docs.dynatrace.com/managed/whats-new/dynatrace-api/sprint-345
---

# Dynatrace API changelog version 1.345

# Dynatrace API changelog version 1.345

* Release notes
* Published Jul 30, 2026
* Rollout start on Aug 11, 2026

## Environment API v2

### /entities

* `POST /entities/securityContext`

  + Request:

    - Changed **SecurityContextDtoImpl** schema (application/json; charset=utf-8)

      * Broken compatibility
      * Added required property **securityContext**

## Configuration API v1

### /dashboards

* `POST /dashboards`

  + Return Type:

    - Add **403 Forbidden**
* `PUT /dashboards/{id}`

  + Return Type:

    - Add **403 Forbidden**