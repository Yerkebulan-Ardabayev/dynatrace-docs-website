---
title: Settings API - Amazon ECR schema table
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/settings/schemas/app-dynatrace-amazon-ecr-connections
---

# Settings API - Amazon ECR schema table

# Settings API - Amazon ECR schema table

* Published Mar 17, 2025

### Amazon ECR (`app:dynatrace.amazon.ecr:connections)`

Ingest Amazon Elastic Container Registry vulnerability findings and scan events.

| Schema ID | Schema groups | Scope |
| --- | --- | --- |
| `app:dynatrace.amazon.ecr:connections` | - | `environment` |

Retrieve schema via Settings API

|  |  |  |
| --- | --- | --- |
| GET | Managed | `https://{your-domain}/e/{your-environment-id}/api/v2/settings/schemas/app:dynatrace.amazon.ecr:connections` |
| GET | SaaS | `https://{your-environment-id}.live.dynatrace.com/api/v2/settings/schemas/app:dynatrace.amazon.ecr:connections` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/v2/settings/schemas/app:dynatrace.amazon.ecr:connections` |

## Authentication

To execute this request, you need an access token with **Read settings** (`settings.read`) scope. To learn how to obtain and use it, see [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Parameters

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| Connection name `name` | text | Provide a unique display name for your connection. | Required |
| Amazon ECR scan type `scan_type` | enum | Type of scan that will be performed The element has these enums * `basic` * `enhanced` | Required |
| Ingest token ID `ingest_token_id` | text | ID of the Grail ingest token to be used in this connection | Optional |