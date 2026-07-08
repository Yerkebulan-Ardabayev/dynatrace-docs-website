---
title: Settings API - Manual insertion schema table
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/settings/schemas/builtin-rum-web-manual-insertion
---

# Settings API - Manual insertion schema table

# Settings API - Manual insertion schema table

* Published Aug 04, 2025

### Manual insertion (`builtin:rum.web.manual-insertion)`

Manually insert one of the snippet formats below into the pages of your application. Learn more about the different [snippet formats﻿](https://dt-url.net/vx5g0ptn). All formats are also available via the [API﻿](https://dt-url.net/oz43wab), allowing you to automate their insertion as part of your build process.

| Schema ID | Schema groups | Scope |
| --- | --- | --- |
| `builtin:rum.web.manual-insertion` | * `group:rum-injection` | `APPLICATION` - Web application |

Retrieve schema via Settings API

|  |  |  |
| --- | --- | --- |
| GET | Managed | `https://{your-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:rum.web.manual-insertion` |
| GET | SaaS | `https://{your-environment-id}.live.dynatrace.com/api/v2/settings/schemas/builtin:rum.web.manual-insertion` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:rum.web.manual-insertion` |

## Authentication

To execute this request, you need an access token with **Read settings** (`settings.read`) scope. To learn how to obtain and use it, see [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Parameters

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| Javascript tag `javascriptTag` | [javascriptTag](#javascriptTag) | JavaScript tag references an external file containing monitoring code and configuration. Due to its dynamic update mechanism, it is recommended for most use cases. | Required |
| OneAgent JavaScript Tag `oneagentJavascriptTag` | [oneagentJavascriptTag](#oneagentJavascriptTag) | OneAgent JavaScript tag includes configuration and a reference to an external file containing the monitoring code. It needs to be updated after configuration changes and monitoring code updates. | Required |
| OneAgent JavaScript Tag with SRI `oneagentJavascriptTagSRI` | [oneagentJavascriptTagSRI](#oneagentJavascriptTagSRI) | OneAgent JavaScript tag with SRI includes configuration, a reference to an external file containing the monitoring code, and a hash that allows the browser to verify the integrity of the monitoring code before executing it. It needs to be updated after configuration changes and monitoring code updates. | Required |
| Code Snippet `codeSnippet` | [codeSnippet](#codeSnippet) | Code snippet is a piece of inline code that implements basic functionality and loads the full functionality either synchronously or deferred. Even though it implements an update mechanism, regular updates are still required to guarantee compatibility. | Required |

##### The `javascriptTag` object

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| Cache monitoring code and configuration for `cacheDuration` | enum | The element has these enums * `1` * `3` * `6` * `12` * `24` * `72` * `144` | Required |
| Script execution attribute `scriptExecutionAttribute` | enum | Add the `async` attribute to download the monitoring code in parallel with parsing the page, and execute it immediately upon availability.  Add the `defer` attribute to execute the monitoring code after the page has finished parsing. The element has these enums * `async` * `defer` * `none` | Optional |
| Add crossorigin=anonymous attribute `crossoriginAnonymous` | boolean | Add the `crossorigin=anonymous` attribute to capture JavaScript error messages and W3C resource timings | Required |

##### The `oneagentJavascriptTag` object

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| Script execution attribute `scriptExecutionAttribute` | enum | Add the `async` attribute to download the monitoring code in parallel with parsing the page, and execute it immediately upon availability  Add the `defer` attribute to execute the monitoring code after the page has finished parsing The element has these enums * `async` * `defer` * `none` | Optional |

##### The `oneagentJavascriptTagSRI` object

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| Script execution attribute `scriptExecutionAttribute` | enum | Add the `async` attribute to download the monitoring code in parallel with parsing the page, and execute it immediately upon availability  Add the `defer` attribute to execute the monitoring code after the page has finished parsing The element has these enums * `async` * `defer` * `none` | Optional |

##### The `codeSnippet` object

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| Load the monitoring code `codeSnippetType` | enum | The element has these enums * `SYNCHRONOUSLY` * `DEFERRED` | Required |