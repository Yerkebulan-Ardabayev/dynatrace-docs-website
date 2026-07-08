---
title: Settings API - Allowed URL pattern rules schema table
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/settings/schemas/builtin-dashboards-image-allowlist
---

# Settings API - Allowed URL pattern rules schema table

# Settings API - Allowed URL pattern rules schema table

* Published Dec 05, 2023

### Allowed URL pattern rules (`builtin:dashboards.image.allowlist)`

Configure allowed URL patterns to fetch external resources such as images. For an image to be uploaded, the configured URL must match one of the specified patterns.

| Schema ID | Schema groups | Scope |
| --- | --- | --- |
| `builtin:dashboards.image.allowlist` | * `group:dashboards` | `environment` |

Retrieve schema via Settings API

|  |  |  |
| --- | --- | --- |
| GET | Managed | `https://{your-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:dashboards.image.allowlist` |
| GET | SaaS | `https://{your-environment-id}.live.dynatrace.com/api/v2/settings/schemas/builtin:dashboards.image.allowlist` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:dashboards.image.allowlist` |

## Authentication

To execute this request, you need an access token with **Read settings** (`settings.read`) scope. To learn how to obtain and use it, see [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Parameters

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| List of URL pattern matchers `allowlist` | Set<[URLPattern](#URLPattern)> | - | Required |

##### The `URLPattern` object

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| Rule `rule` | enum | The element has these enums * `startsWith` * `equals` | Required |
| Pattern `template` | text | - | Required |