---
title: Dynatrace API changelog version 1.321
source: https://docs.dynatrace.com/managed/whats-new/dynatrace-api/sprint-321
scraped: 2026-05-12T11:36:05.168288
---

# Dynatrace API changelog version 1.321

# Dynatrace API changelog version 1.321

* Release notes
* Published Jul 16, 2025

Rollout start: Aug 12, 2025

## Environment API

### /deployment/lambda/layer

* `GET /deployment/lambda/layer` Early Access

### /logs/ingest

There is an option to provide content-type with a query parameter for generic ingest (`/logs/ingest`) content-type only. The value provided in the query parameter has priority over the type specified in the content-type header.

* `POST /logs/ingest`

  + Parameter:

    - Add content-type in query