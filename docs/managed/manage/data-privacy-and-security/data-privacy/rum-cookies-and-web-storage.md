---
title: Cookies and client-side storage for RUM and Session Replay
source: https://docs.dynatrace.com/managed/manage/data-privacy-and-security/data-privacy/rum-cookies-and-web-storage
---

# Cookies and client-side storage for RUM and Session Replay

# Cookies and client-side storage for RUM and Session Replay

* Reference
* Updated on May 04, 2026

Dynatrace Real User Monitoring (RUM) relies on HTTP headers, cookies, web storage, and IndexedDB. The headers used are listed in [Infrastructure pass-through requirements for RUM Classic](/managed/observe/digital-experience/rum-classic/web-applications/initial-setup/infrastructure-pass-through-requirements-classic "Learn which requests, headers, and cookies must pass through your infrastructure for RUM to work as expected."). This page describes the cookies, web storage, and IndexedDB entries used.

Cookies, web storage, and IndexedDB are used for the following purposes:

* Aggregation of user sessions
* Identification of recurring users
* Persisting the state of RUM features like [cost and traffic control](/managed/observe/digital-experience/rum-classic/web-applications/additional-configuration/configure-cost-and-traffic-control-web "Leverage the cost and traffic control setting in Dynatrace to reduce session usage for web applications.")
* Correlation of user actions with their server-side traces
* Keeping the Session Replay recording consistent across pages
* Caching Session Replay resource capture data to avoid redundant uploads

The data stored in cookies, web storage, and IndexedDB contains no personal or sensitive data. It consists of random IDs, timestamps, boolean flags, configuration, hashes, and cached resources.

## Cookies

The following table provides an overview of the cookies used in RUM and Session Replay. These are all first-party cookies.

The `<suffix>` used in the table is explained in [Suffix for cookie names and web storage keys](#cookie-and-web-storage-suffix).

| Cookie | Structure | Expires | Max size | Purpose |
| --- | --- | --- | --- | --- |
| `dtCookie<suffix>` | v4 session state: v\_4\_key1\_value1\_key2\_value2\_keyN\_valueN  Possible keys include:  * srv * sn * mvisitor * msn * perc * ol * mul * app:<appID>  v4 example: v\_4\_srv\_7\_sn\_4D3133F359A76AB05AAF39691696858A | Session | No set limitation, but usually less than 100 B | Tracks a visit across multiple requests. |
| `dtPC<suffix>` | <serverID>$<randomValue>\_<currentMillis>v<randomValue>e<eventCount> | Session | 58 B | Required for routing RUM beacons; includes session ID for user session aggregation. |
| `dtSa<suffix>` | <URL-encoded action name> | Session | Max number of characters in the URL | Serves as an intermediate storage for page-spanning actions. This cookie is used to save user action names, such as `Click on Login`, across different pages. This is required because page loads result in JavaScript code restart, so all contextual information must be stored in cookies. |
| `dtValidationCookie<suffix>` | The string `dTValidationCookieValue`. | Deleted after a few milliseconds; no expiry date set | Length of the string `dTValidationCookieValue`, that is `23` | Used to determine the top-level domain. |
| `rxVisitor<suffix>` | <visitorID> | Session, or permanent if [user tracking](/managed/observe/digital-experience/rum-classic/web-applications/additional-configuration/configure-real-user-monitoring-according-to-gdpr#user-tracking "Learn about the privacy settings that Dynatrace provides to ensure that your web applications comply with the data-privacy regulations of your region.") is turned on | 45 B | Contains the visitor ID to correlate sessions. |
| `rxvt<suffix>` | <timestamp>|<timestamp> | Session | 27 B | Stores the session timeout. |
| `dtsrVID<suffix>` [1](#fn-1-1-def) | <viewID> | Session | 20 B | If Session Replay is enabled, `dtsrVID` stores the ID of the current recorded view. |
| `dtSR<suffix>` [2](#fn-1-2-def) | v4 format  Possible keys:  * vwid * rfnsr * vid * st  Example: v\_4\_rfnsr\_150\_vid\_CFEOMVJRAQLDWHDQPLMORLTRGUFRLFUM-0\_st\_1\_vwid\_1764935792511 | Session | 81 B | If Session Replay is enabled, stores the required values to keep the recording consistent across pages. |

1

The `dtsrVID` cookie exists from RUM JavaScript version 1.325+ to RUM JavaScript version 1.333.

2

The optional `dtSR` cookie is available from RUM JavaScript version 1.335+.

### Configure cookie attributes

Dynatrace RUM does not support the `HttpOnly` attribute. Since `HttpOnly` cookies are inaccessible to JavaScript, the RUM JavaScript cannot read or modify them. Ensure that your infrastructure doesn't add the `HttpOnly` attribute, because this will break monitoring.

If your company's security policy requires the `Secure` and `SameSite` cookie attributes, you need to configure RUM to set them, since they aren't set by default; see [Configure RUM Classic cookie attributes](/managed/observe/digital-experience/rum-classic/web-applications/additional-configuration/configure-cookie-attributes#data-privacy-relevant-attributes "Learn which RUM cookie attributes you can configure and how.").

## Web storage

RUM and Session Replay use both `sessionStorage` and `localStorage`. The following table lists the possible entries. Some of them back up RUM and Session Replay cookies, because browsers may evict cookies when a large number of them are set.

| Key | Storage | Purpose |
| --- | --- | --- |
| `rxVisitor<suffix>` | Stored in `localStorage` when [user tracking](/managed/observe/digital-experience/rum-classic/web-applications/additional-configuration/configure-real-user-monitoring-according-to-gdpr#user-tracking "Learn about the privacy settings that Dynatrace provides to ensure that your web applications comply with the data-privacy regulations of your region.") is enabled, and in `sessionStorage` otherwise. | Backs up the `rxVisitor<suffix>` cookie. |
| `rxvisitid<suffix>` | `sessionStorage` | Backs up the session ID from the `dtPC<suffix>` cookie. |
| `rxvt<suffix>` | `sessionStorage` | Backs up the `rxvt<suffix>` cookie. |
| `dtCookie<suffix>` | `sessionStorage` | Backs up the `dtCookie<suffix>` cookie. |
| `dtSa<suffix>` | `sessionStorage` | Backs up the `dtSa<suffix>` cookie. |
| `ruxitagentjs_<appID or empty>_Store` | `localStorage` | Stores the last beacon response, which contains the RUM JavaScript configuration. |
| `dt-pVO` | `localStorage` | Indicates that persistent values were removed by using the API method [`dtrum.disablePersistentValues`﻿](https://docs.dynatrace.com/javascriptapi/doc/types/dtrum.html#disablepersistentvalues). |
| `dtsrNOSR` | `localStorage`. | Stores the severity of the latest "reason for no Session Replay" message and the `visitId`. Exists until RUM JavaScript version 1.333. |
| `dtSR<suffix>` | By default in `localStorage`, optionally in cookies. | Stores the values required to keep the recording consistent across pages when Session Replay is enabled. Exists from RUM JavaScript version 1.335. |
| `dtsrTID` | `sessionStorage` | Stores the current tab ID for Session Replay. |
| `dtsrTIDrSt` | `sessionStorage` | Boolean flag for Session Replay that indicates whether a window was opened programmatically recently. |

## IndexedDB

Session Replay uses IndexedDB to persist resource capture state across sessions. The following table lists the possible entries.

| Store Name | Purpose |
| --- | --- |
| `dT_store#global` | When Session Replay is enabled, `dT_store#global` stores content hashes of CSS resources already captured by Dynatrace. Used to avoid re-uploading unchanged resources in future sessions. |
| `dT_store#visit` | When Session Replay is enabled, `dT_store#visit` buffers captured resource content and metadata awaiting transmission, and tracks resources that could not be fetched within the current visit. |

## Suffix for cookie names and web storage keys

In environments created in Dynatrace version 1.294+, a suffix is added to cookie names and to the keys of certain web storage entries. In the tables above, this suffix is shown as `<suffix>`. It prevents interference when different Dynatrace environments have overlapping [cookie domains](/managed/observe/digital-experience/rum-classic/web-applications/additional-configuration/configure-cookie-attributes#cookie-domain "Learn which RUM cookie attributes you can configure and how.").

If you need the full cookie names to configure your firewalls and other infrastructure, you can retrieve them using the API endpoint [RUM cookie names API - GET cookie names](/managed/dynatrace-api/environment-api/rum/rum-cookie-names-get-cookie-names "View full RUM cookie names."). To find them in the UI

1. Go to **Web**.
2. Select the application that you want to configure.
3. In the upper-right corner of the application overview page, select **More** (**…**) > **Edit**.
4. From the application settings, select **Injection** > **Cookie**.
5. The cookie names are displayed on the top of the page.

## Allow users to opt in to cookies, web storage, and IndexedDB

Dynatrace cookies, web storage, and IndexedDB are required for Real User Monitoring to work. By default, Dynatrace creates them automatically. To protect your end users' privacy, you can give them the option to accept or decline cookies, web storage, and monitoring in general. This is done through [opt-in mode](/managed/observe/digital-experience/rum-classic/web-applications/additional-configuration/configure-real-user-monitoring-according-to-gdpr#user-opt-in-mode-gdpr "Learn about the privacy settings that Dynatrace provides to ensure that your web applications comply with the data-privacy regulations of your region.").

When opt-in mode is enabled, RUM is disabled by default. As a result, Dynatrace sets no cookies, does not use web storage, and does not write to IndexedDB. After an end user accepts your data privacy policy, your application must call `dtrum.enable()` through the JavaScript API to start capturing data. Dynatrace creates cookies and writes to web storage and IndexedDB only after this method is called.

For details on enabling opt-in mode, see [Configure data privacy settings for web applications in RUM Classic](/managed/observe/digital-experience/rum-classic/web-applications/additional-configuration/configure-real-user-monitoring-according-to-gdpr#user-opt-in-mode-gdpr "Learn about the privacy settings that Dynatrace provides to ensure that your web applications comply with the data-privacy regulations of your region.").

If users do not opt in, Real User Monitoring remains disabled.