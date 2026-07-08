---
title: Settings API - HTTP failure detection parameters schema table
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/settings/schemas/builtin-failure-detection-service-http-parameters
---

# Settings API - HTTP failure detection parameters schema table

# Settings API - HTTP failure detection parameters schema table

* Published Dec 05, 2023

### HTTP failure detection parameters (`builtin:failure-detection.service.http-parameters)`

Dynatrace failure detection automatically detects the vast majority of error conditions in your environment. However, detected service errors don't necessarily mean that the underlying requests have failed. There may be cases where the default service failure detection settings don't meet your particular needs. In such cases, you can configure the settings provided below. Please note that these settings are not applicable to services of type 'Span service'. For complete details, see [configure service failure detection﻿](https://dt-url.net/ys5k0p4y).

| Schema ID | Schema groups | Scope |
| --- | --- | --- |
| `builtin:failure-detection.service.http-parameters` | * `group:failure-detection` | `SERVICE` - Service |

Retrieve schema via Settings API

|  |  |  |
| --- | --- | --- |
| GET | Managed | `https://{your-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:failure-detection.service.http-parameters` |
| GET | SaaS | `https://{your-environment-id}.live.dynatrace.com/api/v2/settings/schemas/builtin:failure-detection.service.http-parameters` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:failure-detection.service.http-parameters` |

## Authentication

To execute this request, you need an access token with **Read settings** (`settings.read`) scope. To learn how to obtain and use it, see [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Parameters

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| Override global failure detection settings `enabled` | boolean | - | Required |
| HTTP response codes `httpResponseCodes` | [httpResponseCodes](#httpResponseCodes) | - | Required |
| HTTP 404 (broken links) `brokenLinks` | [brokenLinks](#brokenLinks) | HTTP 404 response codes are thrown when a web server can't find a certain page. 404s are classified as broken links on the client side and therefore aren't considered to be service failures. By enabling this setting, you can have 404s treated as server-side service failures. | Required |

##### The `httpResponseCodes` object

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| HTTP response codes which indicate an error on the server side `serverSideErrors` | text | A list of HTTP response code ranges and individual values that are treated as server-side errors. The format is a comma-separated list of ranges and values (e.g., `500-599, 402, 405-499`). Default: `500-599`. | Required |
| Treat missing HTTP response code as server side errors `failOnMissingResponseCodeServerSide` | boolean | If `true`, a missing HTTP response code on the server side is treated as a failure. Missing response codes can indicate a fire-and-forget call, a timeout, or an error. Default: `false`. | Required |
| HTTP response codes which indicate client side errors `clientSideErrors` | text | A list of HTTP response code ranges and individual values that are treated as client-side errors. The format is a comma-separated list of ranges and values (e.g., `400-499, 503, 510-599`). Default: `400-599`. | Required |
| Treat missing HTTP response code as client side error `failOnMissingResponseCodeClientSide` | boolean | If `true`, a missing HTTP response code on the client side is treated as a failure. Missing response codes can indicate a fire-and-forget call, a timeout, or an error. Default: `false`. | Required |

##### The `brokenLinks` object

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| Consider 404 HTTP response codes as failures `http404NotFoundFailures` | boolean | If `true`, HTTP 404 response codes are treated as server-side service failures. Only applicable when 404 is not already in the list of failing server-side HTTP response codes. Default: `false`. | Required |
| Rules for broken links to related domains `brokenLinkDomains` | set | If your application relies on other hosts at other domains, add the associated domain names here. Once configured, Dynatrace will consider 404s thrown by hosts at these domains to be service failures related to your application. | Required |