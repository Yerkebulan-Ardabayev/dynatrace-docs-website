---
title: Settings API - Red Hat Ansible Automation Controller Connections schema table
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/settings/schemas/app-dynatrace-redhat-ansible-automation-controller-connection
---

# Settings API - Red Hat Ansible Automation Controller Connections schema table

# Settings API - Red Hat Ansible Automation Controller Connections schema table

* Published Feb 26, 2024

### Red Hat Ansible Automation Controller Connections (`app:dynatrace.redhat.ansible:automation-controller.connection)`

Connections containing access tokens for the Red Hat Ansible app. This connection can be used for connecting to Red Hat Ansible Automation Controller as well as the open-source project AWX.

| Schema ID | Schema groups | Scope |
| --- | --- | --- |
| `app:dynatrace.redhat.ansible:automation-controller.connection` | - | `environment` |

Retrieve schema via Settings API

|  |  |  |
| --- | --- | --- |
| GET | Managed | `https://{your-domain}/e/{your-environment-id}/api/v2/settings/schemas/app:dynatrace.redhat.ansible:automation-controller.connection` |
| GET | SaaS | `https://{your-environment-id}.live.dynatrace.com/api/v2/settings/schemas/app:dynatrace.redhat.ansible:automation-controller.connection` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/v2/settings/schemas/app:dynatrace.redhat.ansible:automation-controller.connection` |

## Authentication

To execute this request, you need an access token with **Read settings** (`settings.read`) scope. To learn how to obtain and use it, see [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Parameters

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| Connection name `name` | text | A unique and clearly identifiable connection name. | Required |
| API URL `url` | text | URL of the Ansible Automation Controller API endpoint. For example, https://ansible.yourdomain.com/api/v2/ | Required |
| Type `type` | enum | Type of authentication method that should be used. The element has these enums * `api-token` | Required |
| API access token `token` | secret | API access token for the Ansible Automation Controller. Please note that this token is not refreshed and can expire. | Required |