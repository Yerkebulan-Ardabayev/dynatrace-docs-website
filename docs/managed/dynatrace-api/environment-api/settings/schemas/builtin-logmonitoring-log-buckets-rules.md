---
title: Settings API - Log buckets schema table
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/settings/schemas/builtin-logmonitoring-log-buckets-rules
---

# Settings API - Log buckets schema table

# Settings API - Log buckets schema table

* Published Dec 05, 2023

### Log buckets (`builtin:logmonitoring.log-buckets-rules)`

Dynatrace logs are stored in buckets. You can give each bucket a unique log retention period (35 days is the default). In addition, you can use buckets to set unique access rules to different logs or log areas. To create or manage buckets go to [bucket permissions﻿](https://dt-url.net/vc034se). Read more about using buckets for logs in our [documentation﻿](https://dt-url.net/ep234n2).

| Schema ID | Schema groups | Scope |
| --- | --- | --- |
| `builtin:logmonitoring.log-buckets-rules` | * `group:log-monitoring.analysis` * `group:log-monitoring` | `environment` |

Retrieve schema via Settings API

|  |  |  |
| --- | --- | --- |
| GET | Managed | `https://{your-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:logmonitoring.log-buckets-rules` |
| GET | SaaS | `https://{your-environment-id}.live.dynatrace.com/api/v2/settings/schemas/builtin:logmonitoring.log-buckets-rules` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:logmonitoring.log-buckets-rules` |

## Authentication

To execute this request, you need an access token with **Read settings** (`settings.read`) scope. To learn how to obtain and use it, see [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Parameters

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| Enabled `enabled` | boolean | - | Required |
| Rule name `ruleName` | text | - | Required |
| Bucket `bucketName` | text | A 'bucket' is the length of time your logs will be stored. Select the bucket that's best for you. | Required |
| Matcher (DQL) `matcher` | text | - | Required |