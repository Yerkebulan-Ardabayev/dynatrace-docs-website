---
title: Configure data privacy settings for web frontends
source: https://www.dynatrace.com/docs/observe/digital-experience/new-rum-experience/web-frontends/additional-configuration/data-privacy-web
scraped: 2026-02-25T21:31:17.224176
---

# Configure data privacy settings for web frontends

# Configure data privacy settings for web frontends

* Latest Dynatrace
* How-to guide
* Published Jan 15, 2026

Ensuring compliance with GDPR and other data privacy regulations is essential for the success of your digital business. The New RUM Experience provides a comprehensive set of options that help you protect the privacy of your customersâ personal data when monitoring web frontends.

To access the data privacy settings for web frontends

1. Go to ![Experience Vitals](https://dt-cdn.net/images/experience-vitals-256-9999590b55.png "Experience Vitals") **Experience Vitals** > **Overview**.
2. Select  **Web** to view all web frontends.
3. Select the frontend you want to configure.
4. On the **Settings** tab, select **Data privacy**.

Check the sections below for the detailed description of each setting.

## Mask personal data in URIs

To access this setting, select **Data Privacy** > **General**.

ð´ Disabled by default

Dynatrace captures full URIs of requests that are sent from desktop and mobile browsers, as well as URIs of requests that are sent and received within monitored server-side processes. URIs may contain personal data, such as user names, passwords, or IDs.

When **Mask personal data in URIs** is turned on, Dynatrace detects personal dataâemail addresses, IBANs, payment card numbers, IP addresses, UUIDs, and other IDsâin URIs, headers, exception messages, and data captured for request attributes. It masks this data at storage by replacing it with the `<masked>` string. It also replaces query parameter values with the `<masked>` string. IDs and numbers must have at least 5 decimal or hexadecimal digits to be masked.

URI masking examples

As a result, personal data appearing in URIs is masked in user events.

## Use persistent cookies for user tracking

To access this setting, select **Data Privacy** > **General**.

ð´ Disabled by default

The **Use persistent cookies for user tracking** setting allows you to enable or disable the use of persistent cookies for identifying returning users.

When turned on, the RUM JavaScript sets a persistent cookie in end-user browsers that indicates that the browser has been used previously to access your frontend. When turned off, RUM Classic is no longer able to associate sessions with the same user across browser restarts. Learn [how we store this cookie](/docs/manage/data-privacy-and-security/data-privacy/cookies#cookie-storage "Learn about first-party cookie usage in Dynatrace.").

## Data-collection and opt-in mode

To access this setting, select **Data Privacy** > **General**.

ð´ Disabled by default

To give your end users the ability to decide whether their activities should be tracked or not, enable opt-in mode.

By default, RUM automatically creates [cookies](/docs/manage/data-privacy-and-security/data-privacy/cookies#dynatrace-rum-cookies "Learn about first-party cookie usage in Dynatrace."). When **Data-collection and opt-in mode** is turned on, neither OneAgent nor the RUM JavaScript sets cookies, and the RUM JavaScript doesn't capture any data. After an end user accepts your cookie policy, you can activate RUM for that user via the [`dtrum.enable()`ï»¿](https://www.dynatrace.com/support/doc/javascriptapi/doc/types/dtrum.html#enable) JavaScript API call. Using the [`dtrum.disable()`ï»¿](https://www.dynatrace.com/support/doc/javascriptapi/doc/types/dtrum.html#disable) API call, you can implement a dialog that allows end users to stop sending monitoring data to Dynatrace even after they've previously agreed to it and `dtrum.enable()` has already been called.

Both API calls are effective for RUM Classic and the New RUM Experience, therefore the [new JavaScript API](/docs/observe/digital-experience/new-rum-experience/web-frontends/new-javascript-api "Learn how to customize web frontend monitoring in the New RUM Experience using the JavaScript API.") does not provide equivalents at this point.

## Comply with "Do not Track" browser settings

To access this setting, select **Data Privacy** > **General**.

ð¢ Enabled by default

Another technique for protecting end-user privacy is the "Do Not Track" feature. When a user enables this feature, their browser adds the `DNT` HTTP request header to all outgoing web requests. This header specifies that the user prefers not to be tracked.

After you turn on **Comply with "Do Not Track" browser settings**, you can select between two options:

* **Capture anonymous user sessions for "Do Not Track"-enabled browsers**: When the `DNT` header is detected, Dynatrace captures RUM data but excludes all personal information that could lead to the identification of the user.

  + The IP address is masked.
  + In RUM Classic, no [user tag](/docs/observe/digital-experience/rum-concepts/user-and-error-events#user-tagging "Learn about user and error events and the types of user and error events captured by Dynatrace.") information is sent.
  + In the New RUM Experience, no [user identifier](/docs/observe/digital-experience/new-rum-experience/concepts/data-model#user-sessions "Get familiar with the data model at the heart of the New RUM Experience.") is sent if it was added using the [RUM Classic JavaScript APIï»¿](https://www.dynatrace.com/support/doc/javascriptapi/doc/types/dtrum.html#identifyuser). Note that the user identifier will still be sent if it was added using the [new JavaScript APIï»¿](https://www.dynatrace.com/support/doc/javascriptapi/doc-latest/functions/Types.dynatrace.identifyUser.html)

  With the [**User tracking** setting](#user-tracking) enabled, Dynatrace still sets a persistent cookie to detect returning users.
* **Turn Real User Monitoring off for "Do Not Track"-enabled browsers**: When the `DNT` header is detected, Dynatrace doesn't capture any data from browsers that have the "Do Not Track" setting enabled.

If you turn off **Comply with "Do Not Track" browser settings**, Dynatrace ignores the browser's "Do Not Track" setting and the `DNT` header.

The **Comply with "Do Not Track" browser settings** â **Capture anonymous user sessions for "Do Not Track"-enabled browsers** option is enabled by default for all environments and frontends.

## Mask end-user IP addresses and GPS coordinates

To access this setting, select **Data privacy** > **IP masking**.

ð¢ Enabled by default

To determine the region from which end users access web and mobile frontends, Dynatrace captures their IP addresses. GPS coordinates are captured only for mobile frontends.

When the **Mask end-user IP addresses and GPS coordinates** option is turned on, IP addresses are masked on the [beacon endpoint](/docs/observe/digital-experience/new-rum-experience/web-frontends/initial-setup/configure-beacon-endpoint "Learn how to configure the beacon endpoint for web frontends to meet your specific requirements."). The last octet of monitored IPv4 addresses and the last 80 bits of IPv6 addresses are replaced with zeros. [Geolocation lookups](/docs/observe/digital-experience/rum-concepts/detection-of-ip-addresses-locations-and-user-agents#geolocations "Dynatrace detects IP addresses and geolocations like a city, region, and country as well as browsers, devices, and operating systems.") are performed using masked IP addresses.