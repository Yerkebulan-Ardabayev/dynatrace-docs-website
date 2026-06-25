---
title: Settings API - Business event bucket assignment schema table
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/settings/schemas/builtin-bizevents-processing-buckets-rule
scraped: 2026-05-12T11:47:23.219520
---

# Settings API - Business event bucket assignment schema table

# Settings API - Business event bucket assignment schema table

* Published Dec 05, 2023

### Business event bucket assignment (`builtin:bizevents-processing-buckets.rule)`

Business events can be stored in different buckets. The first user-defined rule that matches will determine bucket assignment. If no rules match, the default bucket will be used.

Learn to create custom buckets and more by visiting [our documentationï»¿](https://dt-url.net/4c034xt).

| Schema ID | Schema groups | Scope |
| --- | --- | --- |
| `builtin:bizevents-processing-buckets.rule` | * `group:business-analytics` * `group:business-analytics.ingest-pipeline` | `environment` |

Retrieve schema via Settings API

|  |  |  |
| --- | --- | --- |
| GET | Managed | `https://{your-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:bizevents-processing-buckets.rule` |
| GET | SaaS | `https://{your-environment-id}.live.dynatrace.com/api/v2/settings/schemas/builtin:bizevents-processing-buckets.rule` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:bizevents-processing-buckets.rule` |

## Authentication

To execute this request, you need an access token with **Read settings** (`settings.read`) scope. To learn how to obtain and use it, see [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Parameters

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| Enabled `enabled` | boolean | - | Required |
| Rule name `ruleName` | text | - | Required |
| Bucket `bucketName` | text | Events will be stored in the selected bucket. Analyze bucket contents in the log & event viewer. (`<your-dynatrace-url>//ui/logs-events?advancedQueryMode=true&query=fetch+bizevents`) | Required |
| Matcher (DQL) `matcher` | text | [See our documentationï»¿](https://dt-url.net/bp234rv) | Required |