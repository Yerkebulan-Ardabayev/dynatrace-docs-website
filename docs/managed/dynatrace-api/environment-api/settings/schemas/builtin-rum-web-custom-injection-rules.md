---
title: Settings API - Define custom injection rules schema table
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/settings/schemas/builtin-rum-web-custom-injection-rules
---

# Settings API - Define custom injection rules schema table

# Settings API - Define custom injection rules schema table

* Published Aug 26, 2024

### Define custom injection rules (`builtin:rum.web.custom-injection-rules)`

Define custom injection rules to control when and where RUM is automatically injected into your application's pages.

| Schema ID | Schema groups | Scope |
| --- | --- | --- |
| `builtin:rum.web.custom-injection-rules` | * `group:rum-injection` | `APPLICATION` - Web application |

Retrieve schema via Settings API

|  |  |  |
| --- | --- | --- |
| GET | Managed | `https://{your-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:rum.web.custom-injection-rules` |
| GET | SaaS | `https://{your-environment-id}.live.dynatrace.com/api/v2/settings/schemas/builtin:rum.web.custom-injection-rules` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:rum.web.custom-injection-rules` |

## Authentication

To execute this request, you need an access token with **Read settings** (`settings.read`) scope. To learn how to obtain and use it, see [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Parameters

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| Enable rule `enabled` | boolean | - | Required |
| Operator `operator` | enum | **Example**:  **For the URL:**  `http://www.example.com:8080/lorem/ipsum.jsp?mode=desktop`  A rule can be specified on the URL pattern:  `/lorem/ipsum.jsp`  Using the operator:  `URL ends with`  **Result:**  If URL ends with .jsp do not inject the JavaScript library The element has these enums * `AllPages` * `Equals` * `Starts` * `Ends` * `Contains` | Required |
| URL pattern `urlPattern` | text | - | Required |
| Rule `rule` | enum | The element has these enums * `Automatic` * `BeforeSpecificHtml` * `AfterSpecificHtml` * `DoNotInject` | Required |
| `htmlPattern` | text | - | Required |