---
title: Settings API - Issue-tracking for releases schema table
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/settings/schemas/builtin-issue-tracking-integration
---

# Settings API - Issue-tracking for releases schema table

# Settings API - Issue-tracking for releases schema table

* Published Dec 05, 2023

### Issue-tracking for releases (`builtin:issue-tracking.integration)`

Query any issue-tracking system to pull issue statistics for monitored entities into Dynatrace for release analysis. For details, see [Issue-tracking integration﻿](https://dt-url.net/releasesissuetracker).

| Schema ID | Schema groups | Scope |
| --- | --- | --- |
| `builtin:issue-tracking.integration` | * `group:cloud-automation.releases` * `group:cloud-automation` | `environment` |

Retrieve schema via Settings API

|  |  |  |
| --- | --- | --- |
| GET | Managed | `https://{your-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:issue-tracking.integration` |
| GET | SaaS | `https://{your-environment-id}.live.dynatrace.com/api/v2/settings/schemas/builtin:issue-tracking.integration` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:issue-tracking.integration` |

## Authentication

To execute this request, you need an access token with **Read settings** (`settings.read`) scope. To learn how to obtain and use it, see [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Parameters

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| Enabled `enabled` | boolean | - | Required |
| Issue label `issuelabel` | text | Set a label to identify these issues, for example, `release_blocker` or `non-critical` | Required |
| Issue query `issuequery` | text | You can use the following placeholders to automatically insert values from the **Release monitoring** page in your query: `{NAME}`, `{VERSION}`, `{STAGE}`, `{PRODUCT}`. | Required |
| Issue type `issuetheme` | enum | Select the issue type to be displayed. The element has these enums * `INFO` * `ERROR` * `RESOLVED` | Required |
| Issue-tracking system `issuetrackersystem` | enum | Select the issue-tracking system you want to query. The element has these enums * `JIRA` * `GITHUB` * `GITLAB` * `SERVICENOW` * `JIRA_ON_PREMISE` * `JIRA_CLOUD` | Required |
| Target URL `url` | text | For Jira, use the base URL (for example, https://jira.yourcompany.com); for GitHub, use the repository URL (for example, https://github.com/org/repo); for GitLab, use the specific project API for a single project (for example, https://gitlab.com/api/v4/projects/:projectId), and the specific group API for a multiple projects (for example, https://gitlab.com/api/v4/groups/:groupId); for ServiceNow, use your company instance URL (for example, https://yourinstance.service-now.com/) | Required |
| Username `username` | text | - | Required |
| Password `password` | secret | - | Optional |
| Token `token` | secret | - | Optional |