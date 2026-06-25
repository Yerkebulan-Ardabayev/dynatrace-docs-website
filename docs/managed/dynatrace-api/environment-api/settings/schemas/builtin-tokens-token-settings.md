---
title: Settings API - Access tokens schema table
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/settings/schemas/builtin-tokens-token-settings
scraped: 2026-05-12T11:41:15.495240
---

# Settings API - Access tokens schema table

# Settings API - Access tokens schema table

* Published Dec 05, 2023

### Access tokens (`builtin:tokens.token-settings)`

Configure Dynatrace API access token and personal access token generation. For details about tokens and authentication go to [Dynatrace API authentication documentationï»¿](https://dt-url.net/8543sda).

| Schema ID | Schema groups | Scope |
| --- | --- | --- |
| `builtin:tokens.token-settings` | * `group:integration.token-management` * `group:integration` | `environment` |

Retrieve schema via Settings API

|  |  |  |
| --- | --- | --- |
| GET | Managed | `https://{your-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:tokens.token-settings` |
| GET | SaaS | `https://{your-environment-id}.live.dynatrace.com/api/v2/settings/schemas/builtin:tokens.token-settings` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:tokens.token-settings` |

## Authentication

To execute this request, you need an access token with **Read settings** (`settings.read`) scope. To learn how to obtain and use it, see [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Parameters

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| Create Dynatrace API tokens in the new format `newDynatraceTokenFormatEnabled` | boolean | Check out this [blog postï»¿](https://dt-url.net/ho02y5r) to find out more about the new Dynatrace API token format. | Required |
| Enable personal access tokens `patEnabled` | boolean | Allow users of this environment to generate personal access tokens based on user permissions. Note that existing personal access tokens will become unusable while this setting is disabled. | Required |