---
title: Settings API - Microsoft 365 Email Connections schema table
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/settings/schemas/app-dynatrace-microsoft365-connector-mail-connection
---

# Settings API - Microsoft 365 Email Connections schema table

# Settings API - Microsoft 365 Email Connections schema table

* Published Oct 14, 2024

### Microsoft 365 Email Connections (`app:dynatrace.microsoft365.connector:mail.connection)`

Microsoft 365 connections for sending emails

| Schema ID | Schema groups | Scope |
| --- | --- | --- |
| `app:dynatrace.microsoft365.connector:mail.connection` | - | `environment` |

Retrieve schema via Settings API

|  |  |  |
| --- | --- | --- |
| GET | Managed | `https://{your-domain}/e/{your-environment-id}/api/v2/settings/schemas/app:dynatrace.microsoft365.connector:mail.connection` |
| GET | SaaS | `https://{your-environment-id}.live.dynatrace.com/api/v2/settings/schemas/app:dynatrace.microsoft365.connector:mail.connection` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/v2/settings/schemas/app:dynatrace.microsoft365.connector:mail.connection` |

## Authentication

To execute this request, you need an access token with **Read settings** (`settings.read`) scope. To learn how to obtain and use it, see [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Parameters

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| Connection name `name` | text | A unique name for the Microsoft 365 email connection  This name needs to be unique and will be listed and selectable within the connection field of the Microsoft 365 send-email workflow action | Required |
| Directory (tenant) ID `tenant_id` | text | Directory (tenant) ID of your Azure Active Directory  Please find the Directory (tenant) ID in the Microsoft Azure Portal using the service Azure Active Directory. | Required |
| Application (client) ID `client_id` | text | Application (client) ID of your app registered in Microsoft Azure App registrations  Please find the Application (client) ID in the Microsoft Azure Portal using the service App registrations. | Required |
| "From" email address `from_address` | text | The email address from which the messages will be sent  Please provide a valid email address from which the messages will be sent. Example: service.user@company.com | Required |
| Type `type` | enum | Type of authentication method that should be used The element has these enums * `client_secret` | Required |
| Client Secret `client_secret` | secret | Client secret of your app registered in Microsoft Azure App registrations  Please find the Client Secret in the Microsoft Azure Portal using the service App registrations. | Required |