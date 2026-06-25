---
title: Settings API - Automatic injection schema table
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/settings/schemas/builtin-rum-web-automatic-injection
scraped: 2026-05-12T11:40:49.056289
---

# Settings API - Automatic injection schema table

# Settings API - Automatic injection schema table

* Published Mar 17, 2025

### Automatic injection (`builtin:rum.web.automatic-injection)`

Dynatrace OneAgent automatically injects the RUM JavaScript into the HTML head of monitored application pages. Use this page to control and adjust the injection.

| Schema ID | Schema groups | Scope |
| --- | --- | --- |
| `builtin:rum.web.automatic-injection` | * `group:rum-injection` | `APPLICATION` - Web application |

Retrieve schema via Settings API

|  |  |  |
| --- | --- | --- |
| GET | Managed | `https://{your-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:rum.web.automatic-injection` |
| GET | SaaS | `https://{your-environment-id}.live.dynatrace.com/api/v2/settings/schemas/builtin:rum.web.automatic-injection` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:rum.web.automatic-injection` |

## Authentication

To execute this request, you need an access token with **Read settings** (`settings.read`) scope. To learn how to obtain and use it, see [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Parameters

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| Real User Monitoring code source `monitoringCodeSourceSection` | [MonitoringCodeSource](#MonitoringCodeSource) | - | Required |
| Snippet format `snippetFormat` | [SnippetFormat](#SnippetFormat) | *Code Snippet:* OneAgent injects an inline script that initializes Dynatrace and dynamically downloads the monitoring code into your application. Use when you want to inject the monitoring code in deferred mode.  *Inline Code:* OneAgent injects the configuration and the monitoring code inline into your application. Use this injection type when you need to keep the number of web requests at a minimum.  *OneAgent JavaScript Tag:* OneAgent injects a JavaScript tag into your application, containing the configuration and a link to the monitoring code. This is our default injection type, since it's most versatile.  *OneAgent JavaScript tag with SRI:* OneAgent injects the configuration, a reference to an external file containing the monitoring code, and a hash that allows the browser to verify the integrity of the monitoring code before executing it.  Compare the different [injection formatsï»¿](https://dt-url.net/vx5g0ptn). | Required |
| Cache control headers `cacheControlHeaders` | [CacheControlHeaders](#CacheControlHeaders) | - | Required |

##### The `MonitoringCodeSource` object

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| Real User Monitoring code source `codeSource` | text | - | Required |
| Specify path for RUM monitoring code `monitoringCodePath` | text | Specify the URL path under which the RUM monitoring code is requested. By default, the path is set to the root or the context root. A custom URL path may be necessary if your server operates behind a firewall. | Optional |

##### The `SnippetFormat` object

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| Snippet format `snippetFormat` | text | - | Required |
| Load the monitoring code `codeSnippetType` | enum | The element has these enums * `SYNCHRONOUSLY` * `DEFERRED` | Required |
| Script execution attribute `scriptExecutionAttribute` | enum | Add the `async` attribute to download the monitoring code in parallel with parsing the page, and execute it immediately upon availability.  Add the `defer` attribute to execute the monitoring code after the page has finished parsing. The element has these enums * `async` * `defer` * `none` | Optional |

##### The `CacheControlHeaders` object

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| Optimize the value of cache control headers for use with Dynatrace Real User Monitoring `cacheControlHeaders` | boolean | [How to ensure timely configuration updates for automatic injection?ï»¿](https://dt-url.net/m9039ea) | Required |