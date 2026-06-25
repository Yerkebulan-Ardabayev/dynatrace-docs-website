---
title: Settings API - Cookie schema table
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/settings/schemas/builtin-rum-web-injection-cookie
scraped: 2026-05-12T11:45:33.953669
---

# Settings API - Cookie schema table

# Settings API - Cookie schema table

* Published Feb 26, 2024

### Cookie (`builtin:rum.web.injection.cookie)`

Dynatrace RUM uses cookies to correlate user actions with backend performance metrics. You can change the cookie settings here. Learn more about RUM cookies in our [documentationï»¿](https://dt-url.net/wmq1pti).

| Schema ID | Schema groups | Scope |
| --- | --- | --- |
| `builtin:rum.web.injection.cookie` | * `group:rum-injection` | `APPLICATION` - Web application |

Retrieve schema via Settings API

|  |  |  |
| --- | --- | --- |
| GET | Managed | `https://{your-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:rum.web.injection.cookie` |
| GET | SaaS | `https://{your-environment-id}.live.dynatrace.com/api/v2/settings/schemas/builtin:rum.web.injection.cookie` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:rum.web.injection.cookie` |

## Authentication

To execute this request, you need an access token with **Read settings** (`settings.read`) scope. To learn how to obtain and use it, see [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Parameters

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| Use the Secure cookie attribute for cookies set by Dynatrace `useSecureCookieAttribute` | boolean | If your application is only accessible via SSL, you can add the Secure attribute to all cookies set by Dynatrace. This setting prevents the display of warnings from PCI-compliance security scanners. Be aware that with this setting enabled Dynatrace correlation of user actions with server-side web requests is only possible over SSL connections. | Required |
| SameSite cookie attribute `sameSiteCookieAttribute` | enum | Define if your cookie should be restricted to a first-party or same-site context. Learn more about [SameSite cookies and available valuesï»¿](https://dt-url.net/yds1p8u). The element has these enums * `NOTSET` * `NONE` * `LAX` * `STRICT` | Required |
| Domain to be used for cookie placement `cookiePlacementDomain` | text | Specify an alternative domain for cookies set by Dynatrace. Keep in mind that your browser may not allow placement of cookies on certain domains (for example, top-level domains). Before typing a domain name here, confirm that the domain will accept cookies from your browser. For details, see the list of [forbidden top-level domainsï»¿](https://dt-url.net/9n6b0pfz). | Optional |