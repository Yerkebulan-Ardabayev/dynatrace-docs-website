---
title: Settings API - Exclude/Include browsers from monitoring schema table
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/settings/schemas/builtin-rum-web-browser-exclusion
---

# Settings API - Exclude/Include browsers from monitoring schema table

# Settings API - Exclude/Include browsers from monitoring schema table

* Published Dec 05, 2023

### Exclude/Include browsers from monitoring (`builtin:rum.web.browser-exclusion)`

If you want to exclude certain outdated browser types from your list of monitored browsers, create [browser exclusion﻿](https://dt-url.net/0e2z0pp0) rules for the browsers that are to be excluded.

| Schema ID | Schema groups | Scope |
| --- | --- | --- |
| `builtin:rum.web.browser-exclusion` | * `group:capturing` * `group:capturing.exclusions` | `APPLICATION` - Web application |

Retrieve schema via Settings API

|  |  |  |
| --- | --- | --- |
| GET | Managed | `https://{your-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:rum.web.browser-exclusion` |
| GET | SaaS | `https://{your-environment-id}.live.dynatrace.com/api/v2/settings/schemas/builtin:rum.web.browser-exclusion` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:rum.web.browser-exclusion` |

## Authentication

To execute this request, you need an access token with **Read settings** (`settings.read`) scope. To learn how to obtain and use it, see [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Parameters

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| Browser exclusion list `browserExclusionList` | [BrowserExclusionListObject](#BrowserExclusionListObject)[] | - | Required |
| These are the only browsers that should be monitored `browserExclusionInclude` | boolean | - | Required |

##### The `BrowserExclusionListObject` object

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| Browser `browserName` | enum | The element has these enums * `ANDROID_WEBKIT` * `CHROME` * `CHROME_HEADLESS` * `FIREFOX` * `INTERNET_EXPLORER` * `OPERA` * `SAFARI` * `EDGE` * `BOTS_AND_SPIDERS` | Required |
| Browser version comparator `versionComparator` | enum | The element has these enums * `GREATER_OR_EQUAL` * `EQUALS` * `LESS_OR_EQUAL` | Required |
| Version `version` | integer | - | Required |
| Platform `platform` | enum | The element has these enums * `ALL` * `MOBILE` * `DESKTOP` | Required |