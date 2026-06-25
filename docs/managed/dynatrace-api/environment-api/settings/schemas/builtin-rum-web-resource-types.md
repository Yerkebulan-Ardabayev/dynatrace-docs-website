---
title: Settings API - Resource types schema table
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/settings/schemas/builtin-rum-web-resource-types
scraped: 2026-05-12T11:44:37.343622
---

# Settings API - Resource types schema table

# Settings API - Resource types schema table

* Published Dec 05, 2023

### Resource types (`builtin:rum.web.resource-types)`

Dynatrace identifies resource types by their file extensions. In certain cases, however, downloaded resources may lack the correct file extensions. For such cases you can set up rules that define the correct resource types of these resources. These rules ensure that resource-type breakdowns are rendered properly and that the resources types in the waterfall chart are displayed correctly.

Dynatrace supports Java regular expressions syntax. Resource types of resources with URL fragments that match provided regular expressions will be overriden by the value given in the *Primary resource type* field and can be further categorized by specifying a *Secondary resource type*.

Type *^.\*\.od.{1}$* into the **Regular expression field**, select *Other* as **Primary resource type** and type *OpenDocument* into the **Secondary resource type** field to override the default resource type for resources with file extension *.od*\*.

| Schema ID | Schema groups | Scope |
| --- | --- | --- |
| `builtin:rum.web.resource-types` | * `group:web-and-mobile-monitoring` * `group:web-and-mobile-monitoring.content-resources` | `environment` |

Retrieve schema via Settings API

|  |  |  |
| --- | --- | --- |
| GET | Managed | `https://{your-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:rum.web.resource-types` |
| GET | SaaS | `https://{your-environment-id}.live.dynatrace.com/api/v2/settings/schemas/builtin:rum.web.resource-types` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:rum.web.resource-types` |

## Authentication

To execute this request, you need an access token with **Read settings** (`settings.read`) scope. To learn how to obtain and use it, see [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Parameters

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| Regular expression `regularExpression` | text | The regular expression to detect the resource. | Required |
| The primary type of the resource. `primaryResourceType` | enum | The element has these enums * `CSS` * `IMAGE` * `SCRIPT` * `OTHER` | Required |
| The secondary type of the resource. `secondaryResourceType` | text | - | Optional |