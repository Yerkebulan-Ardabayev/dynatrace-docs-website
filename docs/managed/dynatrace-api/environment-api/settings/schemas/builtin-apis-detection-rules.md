---
title: Settings API - API detection rules schema table
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/settings/schemas/builtin-apis-detection-rules
---

# Settings API - API detection rules schema table

# Settings API - API detection rules schema table

* Published Dec 05, 2023

### API detection rules (`builtin:apis.detection-rules)`

Modern applications use a lot of different frameworks, so stacktraces in method hotspots and exceptions can become quite long. APIs allow you to spot a component and the respective ownership that is responsible for a hotspot or degradation faster.

API detection rules look at a stacktrace frame and classify it based on classes (Java, .NET and PHP) or files (Node.js, PHP and GO) depending on the technology. The rules are executed in order and the first match decides the API. Marking APIs as third party will allow you to focus on non-third party APIs.

| Schema ID | Schema groups | Scope |
| --- | --- | --- |
| `builtin:apis.detection-rules` | * `group:service-monitoring` | `environment` |

Retrieve schema via Settings API

|  |  |  |
| --- | --- | --- |
| GET | Managed | `https://{your-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:apis.detection-rules` |
| GET | SaaS | `https://{your-environment-id}.live.dynatrace.com/api/v2/settings/schemas/builtin:apis.detection-rules` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:apis.detection-rules` |

## Authentication

To execute this request, you need an access token with **Read settings** (`settings.read`) scope. To learn how to obtain and use it, see [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Parameters

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| API name `apiName` | text | - | Required |
| Color `apiColor` | text | This color will be used to highlight APIs when viewing code level data, such as distributed traces or method hotspots. | Required |
| Technology `technology` | enum | Restrict this rule to a specific technology. The element has these enums * `Go` * `Nodejs` * `PHP` * `Java` * `dotNet` * `Python` | Optional |
| This API defines a third party library `thirdPartyApi` | boolean | - | Required |
| List of conditions `conditions` | Set<[apiRule](#apiRule)> | - | Required |

##### The `apiRule` object

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| Base `base` | enum | The element has these enums * `FQCN` * `FILE_NAME` * `PACKAGE` | Required |
| Matcher `matcher` | enum | The element has these enums * `BEGINS_WITH` * `CONTAINS` | Required |
| Pattern `pattern` | text | - | Required |