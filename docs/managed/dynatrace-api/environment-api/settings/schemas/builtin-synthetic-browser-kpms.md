---
title: Settings API - Key performance metrics schema table
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/settings/schemas/builtin-synthetic-browser-kpms
---

# Settings API - Key performance metrics schema table

# Settings API - Key performance metrics schema table

* Published Dec 05, 2023

### Key performance metrics (`builtin:synthetic.browser.kpms)`

Select the [key performance metric﻿](https://dt-url.net/kpms) that best represents the user experience of this synthetic monitor.

**Visually complete** is the default metric for load and XHR actions. It measures how long it takes for the visible portion of each user’s browser screen to be fully rendered.

The key performance metric for custom actions is always **User action duration**.

| Schema ID | Schema groups | Scope |
| --- | --- | --- |
| `builtin:synthetic.browser.kpms` | * `group:synthetic.browser` | `SYNTHETIC_TEST` - Synthetic monitor |

Retrieve schema via Settings API

|  |  |  |
| --- | --- | --- |
| GET | Managed | `https://{your-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:synthetic.browser.kpms` |
| GET | SaaS | `https://{your-environment-id}.live.dynatrace.com/api/v2/settings/schemas/builtin:synthetic.browser.kpms` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:synthetic.browser.kpms` |

## Authentication

To execute this request, you need an access token with **Read settings** (`settings.read`) scope. To learn how to obtain and use it, see [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Parameters

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| Load action key performance metric `loadActionKpm` | enum | The element has these enums * `USER_ACTION_DURATION` * `VISUALLY_COMPLETE` * `SPEED_INDEX` * `DOM_INTERACTIVE` * `LOAD_EVENT_START` * `LOAD_EVENT_END` * `RESPONSE_START` * `RESPONSE_END` * `LARGEST_CONTENTFUL_PAINT` * `CUMULATIVE_LAYOUT_SHIFT` | Required |
| XHR action key performance metric `xhrActionKpm` | enum | The element has these enums * `USER_ACTION_DURATION` * `VISUALLY_COMPLETE` * `RESPONSE_START` * `RESPONSE_END` | Required |