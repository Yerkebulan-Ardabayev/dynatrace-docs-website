---
title: Settings API - End users' data privacy schema table
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/settings/schemas/builtin-preferences-privacy
---

# Settings API - End users' data privacy schema table

# Settings API - End users' data privacy schema table

* Published Dec 05, 2023

### End users' data privacy (`builtin:preferences.privacy)`

Use the settings on this page to mask the personal data of your end users and ensure your organization's compliance with data-privacy regulations, including [GDPR﻿](https://dt-url.net/8m3u0pxk).

Unless otherwise stated, all privacy settings below apply to both the data captured with RUM Javascript and the data captured by OneAgent on the server side. These settings ensure that none of your end-users' personal data are stored by Dynatrace. For complete details on ensuring the data privacy of your end users, see [Data privacy and security﻿](https://dt-url.net/zn03sq4) in Dynatrace Help.

| Schema ID | Schema groups | Scope |
| --- | --- | --- |
| `builtin:preferences.privacy` | * `group:preferences` * `group:rum-settings` * `group:privacy-settings` | `APPLICATION` - Web application  `environment` |

Retrieve schema via Settings API

|  |  |  |
| --- | --- | --- |
| GET | Managed | `https://{your-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:preferences.privacy` |
| GET | SaaS | `https://{your-environment-id}.live.dynatrace.com/api/v2/settings/schemas/builtin:preferences.privacy` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:preferences.privacy` |

## Authentication

To execute this request, you need an access token with **Read settings** (`settings.read`) scope. To learn how to obtain and use it, see [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Parameters

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| `masking` | [Masking](#Masking) | - | Required |
| User tracking `userTracking` | [UserTracking](#UserTracking) | - | Required |
| Opt-in mode `dataCollection` | [DataCollection](#DataCollection) | To provide your end users with the ability to decide for themselves if their activities should be tracked to measure application performance and usage, enable opt-in mode. | Required |
| Do Not Track `doNotTrack` | [DoNotTrack](#DoNotTrack) | Most modern web browsers have a privacy feature called ["Do Not Track"﻿](https://dt-url.net/sb3n0pnl) that individual users may have enabled on their devices. Customize how Dynatrace should behave when it encounters this setting. | Required |

##### The `Masking` object

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| Mask personal data in URIs `personalDataUriMaskingEnabled` | boolean | Dynatrace captures the URIs and request headers sent from desktop and mobile browsers. Dynatrace also captures request data on the server-side to enable detailed performance analysis of your applications. For complete details, visit [Mask personal data in URIs﻿](https://dt-url.net/mask-personal-data-in-URIs).  URIs, query strings, headers, exception messages and data captured for request attributes can contain personal data. When this setting is enabled, Dynatrace automatically detects UUIDs, credit card numbers, email addresses, IP addresses, and other IDs and replaces those values with placeholders. The personal data is then masked in PurePath analysis, error analysis, user action naming for RUM, and elsewhere in Dynatrace. | Required |
| Mask user actions (web applications only) `userActionMaskingEnabled` | boolean | When Dynatrace detects a user action that triggers a page load or an AJAX/XHR action. To learn more about masking user actions, visit [Mask user actions﻿](https://dt-url.net/mask-user-action).  When Dynatrace detects a user action that triggers a page load or an AJAX/XHR action, it constructs a name for the user action based on:  * User event type (click on..., loading of page..., or keypress on...) * Title, caption, label, value, ID, className, or other available property of the related HTML element (for example, an image, button, checkbox, or text input field).  In most instances, the default approach to user-action naming works well, resulting in user-action names such as:  * click on "Search" on page /search.html * keypress on "Feedback" on page /contact.html * touch on "Homescreen" of page /list.jsf  In rare circumstances, confidential data (for example, email addresses, usernames, or account numbers) can be unintentionally included in user action names because the confidential data itself is included in an HTML element label, attribute, or other value (for example, click on "my Account Number: 1231231"...). If such confidential data appears in your application's user action names, enable the Mask user action names setting. This setting replaces specific HTML element names and values with generic HTML element names. With user-action name masking enabled, the user action names listed above appear as:  * click on INPUT on page /search.html * keypress on TEXTAREA on page /contact.html * touch on DIV of page /list.jsf | Required |

##### The `UserTracking` object

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| Use persistent cookies for user tracking `persistentCookieEnabled` | boolean | When enabled, Dynatrace places a [persistent cookie﻿](https://dt-url.net/313o0p4n) on all end-user devices to identify returning users. | Required |

##### The `DataCollection` object

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| Data-collection and opt-in mode `optInModeEnabled` | boolean | With [Data-collection and opt-in mode﻿](https://dt-url.net/7l3p0p3h) enabled, Real User Monitoring data isn't captured until dtrum.enable() is called for specific user sessions. | Required |

##### The `DoNotTrack` object

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| Comply with "Do Not Track" browser settings `complyWithDoNotTrack` | boolean | - | Required |
| `doNotTrack` | enum | The element has these enums * `anonymous` * `disable-rum` | Required |