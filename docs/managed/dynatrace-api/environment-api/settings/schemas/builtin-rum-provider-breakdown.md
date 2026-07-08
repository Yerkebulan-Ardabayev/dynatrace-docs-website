---
title: Settings API - Provider breakdown schema table
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/settings/schemas/builtin-rum-provider-breakdown
---

# Settings API - Provider breakdown schema table

# Settings API - Provider breakdown schema table

* Published Dec 05, 2023

### Provider breakdown (`builtin:rum.provider-breakdown)`

Set up rules that define how your applications' downloaded content resources (images, CSS, third party widgets, and more) are displayed and categorized for analysis.

Dynatrace uses the provider host names of downloaded resources to categorize content resources into either third party resources, CDN resources, or first party resources.

Dynatrace auto-detects over 1,000 content providers out-of-the-box, including Google, Amazon, Facebook, and many more. There's nothing you need to do to set up detection of resources. If you can't find your provider in the list below, you can add it manually. To learn more, visit [Configure 3rd-party and CDN content detection﻿](https://dt-url.net/on02tdo).

| Schema ID | Schema groups | Scope |
| --- | --- | --- |
| `builtin:rum.provider-breakdown` | * `group:web-and-mobile-monitoring` * `group:web-and-mobile-monitoring.content-resources` | `environment` |

Retrieve schema via Settings API

|  |  |  |
| --- | --- | --- |
| GET | Managed | `https://{your-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:rum.provider-breakdown` |
| GET | SaaS | `https://{your-environment-id}.live.dynatrace.com/api/v2/settings/schemas/builtin:rum.provider-breakdown` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:rum.provider-breakdown` |

## Authentication

To execute this request, you need an access token with **Read settings** (`settings.read`) scope. To learn how to obtain and use it, see [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Parameters

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| Resource name `resourceName` | text | - | Required |
| Resource type `resourceType` | enum | The element has these enums * `FirstParty` * `ThirdParty` * `Cdn` | Required |
| Specify an URL for the provider's brand icon `iconUrl` | text | - | Optional |
| Domain name pattern `domainNamePatternList` | Set<[DomainNamePatternListObject](#DomainNamePatternListObject)> | - | Required |
| Submit this provider-pattern to improve auto-detection `reportPublicImprovement` | boolean | Send the patterns of this provider to Dynatrace to help us improve 3rd-party detection. | Required |

##### The `DomainNamePatternListObject` object

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| Type your domain name pattern `domainNamePattern` | text | Use a ends-with pattern for this content provider's domain | Required |