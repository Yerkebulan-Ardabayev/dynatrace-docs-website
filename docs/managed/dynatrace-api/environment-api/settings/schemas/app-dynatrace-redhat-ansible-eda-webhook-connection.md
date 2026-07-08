---
title: Settings API - Red Hat Event-Driven Ansible Connections schema table
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/settings/schemas/app-dynatrace-redhat-ansible-eda-webhook-connection
---

# Settings API - Red Hat Event-Driven Ansible Connections schema table

# Settings API - Red Hat Event-Driven Ansible Connections schema table

* Published Apr 22, 2024

### Red Hat Event-Driven Ansible Connections (`app:dynatrace.redhat.ansible:eda-webhook.connection)`

Connections containing access tokens for the Red Hat Ansible app. This connection can be used for connecting to the DT Event-Driven plugin within Red Hat Event-Driven Ansible.

| Schema ID | Schema groups | Scope |
| --- | --- | --- |
| `app:dynatrace.redhat.ansible:eda-webhook.connection` | - | `environment` |

Retrieve schema via Settings API

|  |  |  |
| --- | --- | --- |
| GET | Managed | `https://{your-domain}/e/{your-environment-id}/api/v2/settings/schemas/app:dynatrace.redhat.ansible:eda-webhook.connection` |
| GET | SaaS | `https://{your-environment-id}.live.dynatrace.com/api/v2/settings/schemas/app:dynatrace.redhat.ansible:eda-webhook.connection` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/v2/settings/schemas/app:dynatrace.redhat.ansible:eda-webhook.connection` |

## Authentication

To execute this request, you need an access token with **Read settings** (`settings.read`) scope. To learn how to obtain and use it, see [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Parameters

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| Connection name `name` | text | A unique and clearly identifiable connection name. | Required |
| Use Red Hat Event Streams `eventStreamEnabled` | boolean | Flag if Red Hat Event Stream is use for Event-Driven Ansible | Optional |
| API URL `url` | text | URL of the Event-Driven Ansible source plugin webhook. For example, https://eda.yourdomain.com:5010 | Required |
| Type `type` | enum | Type of authentication method that should be used. The element has these enums * `api-token` | Required |
| API access token `token` | secret | API access token for the Event-Driven Ansible Controller. Please note that this token is not refreshed and can expire. | Required |