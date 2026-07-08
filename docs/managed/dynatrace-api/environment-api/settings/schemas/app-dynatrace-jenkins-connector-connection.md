---
title: Settings API - Jenkins Connections schema table
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/settings/schemas/app-dynatrace-jenkins-connector-connection
---

# Settings API - Jenkins Connections schema table

# Settings API - Jenkins Connections schema table

* Published Mar 17, 2025

### Jenkins Connections (`app:dynatrace.jenkins.connector:connection)`

Connections contain the access information for the Jenkins app. This connection can be used to connect to the Jenkins instance.

| Schema ID | Schema groups | Scope |
| --- | --- | --- |
| `app:dynatrace.jenkins.connector:connection` | - | `environment` |

Retrieve schema via Settings API

|  |  |  |
| --- | --- | --- |
| GET | Managed | `https://{your-domain}/e/{your-environment-id}/api/v2/settings/schemas/app:dynatrace.jenkins.connector:connection` |
| GET | SaaS | `https://{your-environment-id}.live.dynatrace.com/api/v2/settings/schemas/app:dynatrace.jenkins.connector:connection` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/v2/settings/schemas/app:dynatrace.jenkins.connector:connection` |

## Authentication

To execute this request, you need an access token with **Read settings** (`settings.read`) scope. To learn how to obtain and use it, see [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Parameters

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| Connection name `name` | text | The name of the Jenkins connection | Required |
| Jenkins URL `url` | text | Base URL of your Jenkins instance (e.g. https://[YOUR\_JENKINS\_DOMAIN]/) | Required |
| Username `username` | text | The name of your Jenkins user (e.g. jenkins) | Required |
| Password `password` | secret | The password of the user or API token obtained from the Jenkins UI (Dashboard > User > Configure > API Token) | Required |