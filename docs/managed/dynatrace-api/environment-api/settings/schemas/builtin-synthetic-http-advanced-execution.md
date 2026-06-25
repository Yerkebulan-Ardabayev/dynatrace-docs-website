---
title: Settings API - Advanced settings schema table
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/settings/schemas/builtin-synthetic-http-advanced-execution
scraped: 2026-05-12T11:43:52.342639
---

# Settings API - Advanced settings schema table

# Settings API - Advanced settings schema table

* Published Sep 25, 2025
* Preview

### Advanced settings (`builtin:synthetic.http.advanced-execution)`

Fine-tune your HTTP monitor's execution with custom settings. These settings will override the default values. For more information, visit [Advanced settings for HTTP monitorsï»¿](https://dt-url.net/wa034cl).

| Schema ID | Schema groups | Scope |
| --- | --- | --- |
| `builtin:synthetic.http.advanced-execution` | * `group:synthetic.http` | `HTTP_CHECK` - HTTP monitor |

Retrieve schema via Settings API

|  |  |  |
| --- | --- | --- |
| GET | Managed | `https://{your-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:synthetic.http.advanced-execution` |
| GET | SaaS | `https://{your-environment-id}.live.dynatrace.com/api/v2/settings/schemas/builtin:synthetic.http.advanced-execution` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:synthetic.http.advanced-execution` |

## Authentication

To execute this request, you need an access token with **Read settings** (`settings.read`) scope. To learn how to obtain and use it, see [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Parameters

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| Request timeout (ms) `requestTimeout` | integer | Supported values are between 1 000 and 60 000 ms | Optional |
| Connect timeout (ms) `connectTimeout` | integer | Supported values are between 1 000 and 60 000 ms | Optional |
| Maximum header size (B) `maxHeaderSize` | integer | Supported values are between 10 240 and 61 440 bytes | Optional |
| Monitor execution timeout (ms) `monitorExecutionTimeout` | integer | Supported values are between 10 000 and 300 000 ms | Optional |
| Script execution timeout (ms) `scriptExecutionTimeout` | integer | Supported values are between 1 000 and 10 000 ms | Optional |
| Maximum request body size (B) `maxRequestBodySize` | integer | Supported values are between 10 240 and 102 400 bytes | Optional |
| Maximum custom script size (B) `maxCustomScriptSize` | integer | Supported values are between 10 240 and 102 400 bytes | Optional |
| Maximum response body size (B) `maxResponseBodySize` | integer | Supported values are between 51 200 and 20 971 520 bytes | Optional |
| Maximum size of response body read by custom script (B) `maxResponseBodyReadByScriptSize` | integer | Supported values are between 10 240 and 102 400 bytes | Optional |
| DNS query timeout (ms) `dnsQueryTimeout` | integer | Supported values are between 1 000 and 60 000 ms | Optional |