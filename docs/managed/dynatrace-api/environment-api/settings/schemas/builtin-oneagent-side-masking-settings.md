---
title: Settings API - OneAgent side masking schema table
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/settings/schemas/builtin-oneagent-side-masking-settings
---

# Settings API - OneAgent side masking schema table

# Settings API - OneAgent side masking schema table

* Published Feb 26, 2024

### OneAgent side masking (`builtin:oneagent.side.masking.settings)`

Use the settings on this page to exclude sensitive data from exceptions and URLs captured directly by OneAgent, so it never leaves your environment. The settings below are executed directly on the OneAgent and will exclude the data points from being sent to Dynatrace servers. These data points will no longer be available to you in Dynatrace.

Note: The RUM JavaScript is **not** affected by these settings!

A detailed reference and change log can be found [here﻿](https://dt-url.net/kd039dm).

| Schema ID | Schema groups | Scope |
| --- | --- | --- |
| `builtin:oneagent.side.masking.settings` | * `group:preferences` * `group:privacy-settings` | `PROCESS_GROUP` - Process Group  `CLOUD_APPLICATION` - Kubernetes workload  `CLOUD_APPLICATION_NAMESPACE` - Kubernetes namespace  `KUBERNETES_CLUSTER` - Kubernetes cluster  `HOST_GROUP` - Host Group  `environment` |

Retrieve schema via Settings API

|  |  |  |
| --- | --- | --- |
| GET | Managed | `https://{your-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:oneagent.side.masking.settings` |
| GET | SaaS | `https://{your-environment-id}.live.dynatrace.com/api/v2/settings/schemas/builtin:oneagent.side.masking.settings` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:oneagent.side.masking.settings` |

## Authentication

To execute this request, you need an access token with **Read settings** (`settings.read`) scope. To learn how to obtain and use it, see [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Parameters

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| Email addresses `isEmailMaskingEnabled` | boolean | Exclude email addresses from URLs and exceptions  Enables masking of emails and user information in URLs and exceptions.  Examples: https://the-internet.com/mail/admin@the-internet.com/newItems -> https://the-internet.com/mail//newItems (`<your-dynatrace-url>/`)  ftp://user:hunter2@domain.com -> ftp://@domain.com (`<your-dynatrace-url>/`) (Domain is not masked, as it's recognised as part of the authority.) | Required |
| Query parameters `isQueryMaskingEnabled` | boolean | Exclude query parameters from URLs and web requests  Enables masking values of query parameters in URLs.  Example: **?key1=value1&key2=value2** -> **?key1=&key2=**. | Required |
| Financial and payment card numbers `isFinancialMaskingEnabled` | boolean | Exclude IBANs and payment card numbers from URLs and exceptions  Enables masking of IBAN- and payment card-like strings (numbers).  Example: https://the-internet.com/CC/1234 4321 5678 8756/test (`<your-dynatrace-url>/`) -> https://the-internet.com/CC//test (`<your-dynatrace-url>/`) | Required |
| IDs and numbers `isNumbersMaskingEnabled` | boolean | Exclude hexadecimal IDs and consecutive numbers above 5 digits from URLs and exceptions  Numbers can contain symbols **-**, **.**, **:**, ' '(whitespace) between digits, these are not counted. Maximum value is 255.  Example: https://the-internet.com/IP/123:12:32:65 -> https://the-internet.com/IP/ (`<your-dynatrace-url>/`) | Required |