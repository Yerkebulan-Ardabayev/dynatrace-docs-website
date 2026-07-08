---
title: Settings API - Frequent issue detection schema table
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/settings/schemas/builtin-anomaly-detection-frequent-issues
---

# Settings API - Frequent issue detection schema table

# Settings API - Frequent issue detection schema table

* Published Dec 05, 2023

### Frequent issue detection (`builtin:anomaly-detection.frequent-issues)`

Dynatrace is automatically detecting frequent issues over a period of one week. A problem is automatically converted into a frequent issue if the problem is detected multiple times throughout a day and over a weeks period of time and if it is not getting worse. Once it's classified as a frequent issue alerting is automatically disabled. In case that the frequent issue is getting worse problem alerts are again sent out. Within this page you can disable the frequent issue detection for all topological levels.  
See our [help documentation﻿](https://dt-url.net/ex4v0pcw) about frequent issue detection.

| Schema ID | Schema groups | Scope |
| --- | --- | --- |
| `builtin:anomaly-detection.frequent-issues` | * `group:anomaly-detection` | `environment` |

Retrieve schema via Settings API

|  |  |  |
| --- | --- | --- |
| GET | Managed | `https://{your-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:anomaly-detection.frequent-issues` |
| GET | SaaS | `https://{your-environment-id}.live.dynatrace.com/api/v2/settings/schemas/builtin:anomaly-detection.frequent-issues` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:anomaly-detection.frequent-issues` |

## Authentication

To execute this request, you need an access token with **Read settings** (`settings.read`) scope. To learn how to obtain and use it, see [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Parameters

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| Detect frequent issues within applications `detectFrequentIssuesInApplications` | boolean | - | Required |
| Detect frequent issues within transactions and services `detectFrequentIssuesInTransactionsAndServices` | boolean | - | Required |
| Detect frequent issues within infrastructure `detectFrequentIssuesInInfrastructure` | boolean | - | Required |
| Detect frequent issues on the environment singleton entity `detectFrequentIssuesInEnvironment` | boolean | Events raised at this level typically occur when no specific topological entity is applicable, often based on data such as logs and metrics. This does not impact the detection of issues within applications, transactions, services, or infrastructure. | Optional |