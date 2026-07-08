---
title: Settings API - Exclude XHR requests from monitoring schema table
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/settings/schemas/builtin-rum-web-xhr-exclusion
---

# Settings API - Exclude XHR requests from monitoring schema table

# Settings API - Exclude XHR requests from monitoring schema table

* Published Dec 05, 2023

### Exclude XHR requests from monitoring (`builtin:rum.web.xhr-exclusion)`

Specify a regular expression to match all URLs that should be excluded from becoming XHR actions.

Dynatrace supports the JavaScript Regular Expressions syntax. The separation between different protocols of the URIs is not supported (every protocol of the URI will be excluded).

| Schema ID | Schema groups | Scope |
| --- | --- | --- |
| `builtin:rum.web.xhr-exclusion` | * `group:capturing` * `group:capturing.exclusions` | `APPLICATION` - Web application |

Retrieve schema via Settings API

|  |  |  |
| --- | --- | --- |
| GET | Managed | `https://{your-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:rum.web.xhr-exclusion` |
| GET | SaaS | `https://{your-environment-id}.live.dynatrace.com/api/v2/settings/schemas/builtin:rum.web.xhr-exclusion` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:rum.web.xhr-exclusion` |

## Authentication

To execute this request, you need an access token with **Read settings** (`settings.read`) scope. To learn how to obtain and use it, see [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Parameters

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| XHR exclusion rule `xhrExclusionRule` | text | **Examples:**  * \/segment1\/segment2 * dynatrace\.com * www\.dynatrace\.com\/segment1\/.\*[a-zA-Z] * www\.dynatrace\.com:8080 * www\.dynatrace\.com:([0-9]{1,4}|[1-5][0-9]{4}|6[0-4][0-9]{3}|65[0-4][0-9]{2}|655[0-2][0-9]|6553[0-5]) * www\.dynatrace\.com\?param1=value1&param2=.\*[a-zA-Z] | Required |