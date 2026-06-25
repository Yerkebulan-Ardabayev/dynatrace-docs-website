---
title: Settings API - GitLab Connections schema table
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/settings/schemas/app-dynatrace-gitlab-connector-connection
scraped: 2026-05-12T11:41:04.635860
---

# Settings API - GitLab Connections schema table

# Settings API - GitLab Connections schema table

* Published Jul 31, 2024

### GitLab Connections (`app:dynatrace.gitlab.connector:connection)`

Connections containing access tokens for the GitLab Platform

(for more information read the [GitLab API documentationï»¿](https://docs.gitlab.com/ee/api/rest/ "Visit GitLab document"))

| Schema ID | Schema groups | Scope |
| --- | --- | --- |
| `app:dynatrace.gitlab.connector:connection` | - | `environment` |

Retrieve schema via Settings API

|  |  |  |
| --- | --- | --- |
| GET | Managed | `https://{your-domain}/e/{your-environment-id}/api/v2/settings/schemas/app:dynatrace.gitlab.connector:connection` |
| GET | SaaS | `https://{your-environment-id}.live.dynatrace.com/api/v2/settings/schemas/app:dynatrace.gitlab.connector:connection` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/v2/settings/schemas/app:dynatrace.gitlab.connector:connection` |

## Authentication

To execute this request, you need an access token with **Read settings** (`settings.read`) scope. To learn how to obtain and use it, see [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Parameters

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| Connection name `name` | text | A unique and clearly identifiable connection name to your GitLab instance. | Required |
| GitLab URL `url` | text | The GitLab URL instance you want to connect. For example, https://gitlab.com  Include the http(s):// prefix | Required |
| GitLab token `token` | secret | The GitLab token to use for authentication. Please note that this token is not refreshed and can expire.  GitLab token in the form of `******`. Not a secret for now due to problems retrieving it from the API functions | Required |