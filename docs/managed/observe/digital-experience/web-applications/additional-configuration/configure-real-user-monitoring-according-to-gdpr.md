---
title: Configure data privacy settings for web applications
source: https://docs.dynatrace.com/managed/observe/digital-experience/web-applications/additional-configuration/configure-real-user-monitoring-according-to-gdpr
scraped: 2026-05-12T11:08:39.820577
---

# Configure data privacy settings for web applications

# Configure data privacy settings for web applications

* How-to guide
* 2-min read
* Updated on Apr 27, 2026

Ensuring the privacy of your customers' personal data is now a key component of your digital business success. Dynatrace provides numerous privacy enhancements that make it easy for you to configure appropriate settings that protect your customers' personal data and ensure your organization's compliance with GDPR or other data privacy regulations.

For details on the global data privacy settings, see [Configure data privacy settings](/managed/manage/data-privacy-and-security/configuration/configure-global-privacy-settings "Learn how to set up data privacy masking for end user IP addresses, geolocations, and user action names.").

To access the data privacy settings for your web application

1. Go to **Web**.
2. Select the application that you want to configure.
3. In the upper-right corner of the application overview page, select **More** (**â¦**) > **Edit**.
4. From the application settings, select **General settings** > **Data privacy** > **General**. The **Data privacy** page opens.

On this page, the following settings are available:

* [Mask personal data in URIs](#mask-uris)
* [Mask user actions](#mask-user-actions)
* [User tracking](#user-tracking)
* [Opt-in mode](#user-opt-in-mode-gdpr)
* [Do Not Track](#do-not-track-gdpr)
* [Mask IPs and GPS coordinates](#mask-ip-and-gps)

Check the sections below for the detailed description of each setting.

## Mask personal data in URIs

To access this option, select **General settings** > **Data privacy** > **General** from the application settings.

ð´ Disabled by default

Dynatrace captures full URIs of requests that are sent from desktop and mobile browsers, as well as URIs of requests that are sent and received within monitored server-side processes. URIs may contain personal data, such as user names, passwords, or IDs.

When **Mask personal data in URIs** is turned on, Dynatrace detects personal dataâemail addresses, IBANs, payment card numbers, IP addresses, UUIDs, and other IDsâin URIs, headers, exception messages, and data captured for request attributes. It masks this data at storage by replacing it with the `<masked>` string. It also replaces query parameter values with the `<masked>` string. IDs and numbers must have at least 5 decimal or hexadecimal digits to be masked.

URI masking examples

| Type of personal data | Example before masking | Example after masking |
| --- | --- | --- |
| Email address | `https://example.com/user/john.doe@example.com/profile` | `https://example.com/user/<masked>/profile` |
| Query parameter value | `https://example.com?country=Austria&city=Linz` | `https://example.com?country=<masked>&city=<masked>` |
| Payment card number | `https://example.com/checkout?card=4111111111111111` | `https://example.com/checkout?card=<masked>` |
| IP address | `https://192.168.10.25/dashboard` | `https://<masked>/dashboard` |

As a result, the personal data is then masked in the distributed trace analysis, error analysis, user action names for RUM, and elsewhere in Dynatrace.

Note that there is a difference between the data masked out with asterisks `*****` and data replaced with `<masked>`. For more details, see [Masking at display](/managed/manage/data-privacy-and-security/configuration/configure-global-privacy-settings#masking-at-display "Learn how to set up data privacy masking for end user IP addresses, geolocations, and user action names.").

## Mask user actions

To access this option, select **General settings** > **Data privacy** > **General** from the application settings.

ð´ Disabled by default

The **Mask user actions (web applications only)** option affects Real User Monitoring only for web applications. With this option enabled, Dynatrace uses generic values for user action names.

When Dynatrace detects a user action that triggers a page load or an AJAX/XHR action, it constructs a name for the user action based on:

* User event type, for example, `click on...`, `loading of page...`, or `keypress on...`
* Title, caption, label, value, ID, className, or other available property of the related HTML element, for example, an image, button, checkbox, or text input field

In most instances, the default approach to user action naming works well, resulting in user action names such as:

* `click on "Search" on page /search.html`
* `keypress on "Feedback" on page /contact.html`
* `touch on "Homescreen" of page /list.jsf`

In rare circumstances, email addresses, usernames, or other confidential data may be unintentionally included in user action names. This happens when confidential data is included in an HTML element label, attribute, or other value, resulting in user action names such as `click on "My Account Number: 1231231"`. If such confidential data appears in your application's user action names, turn on **Mask user actions (web applications only)** . This setting replaces specific HTML element names and values with generic HTML element names.

With user action name masking enabled, the user action names listed above appear as:

* `click on INPUT on page /search.html`
* `keypress on TEXTAREA on page /contact.html`
* `touch on DIV of page /list.jsf`

## User tracking

To access this option, select **General settings** > **Data privacy** > **General** from the application settings.

ð´ Disabled by default

The **Use persistent cookies for user tracking** setting allows you to enable or disable the use of persistent cookies for identifying returning users.

When turned on, the RUM JavaScript sets the persistent `rxVisitor` cookie in end-user browsers that indicates that the browser has been used previously to access your application. When turned off, RUM Classic is no longer able to associate sessions with the same user across browser restarts. Learn [how we store this cookie](/managed/manage/data-privacy-and-security/data-privacy/rum-cookies-and-web-storage#web-storage "Learn how Dynatrace RUM and Session Replay use cookies, web storage, and IndexedDB.").

### Configure the cookie lifetime

By default, the `rxVisitor` cookie is stored for two years. If applicable data privacy laws require a shorter lifetime for permanent cookies, use a custom configuration property to reduce the `rxVisitor` cookie lifetime.

1. Go to **Web**.
2. Select the application that you want to configure.
3. In the upper-right corner of the application overview page, select **More** (**â¦**) > **Edit**.
4. From the application settings, select **Capturing** > **Custom configuration properties**.
5. Select **Add a custom configuration property** and enter the `rvcl=<time-in-months>` key-value pair to set your desired cookie lifetime value. The maximum is 24 months.

   For example, `rvcl=12` is 12 months.

## Opt-in mode

To access this option, select **General settings** > **Data privacy** > **General** from the application settings.

ð´ Disabled by default

To give your end users the ability to decide whether their activities should be tracked or not, enable opt-in mode.

By default, RUM automatically creates [cookies](/managed/manage/data-privacy-and-security/data-privacy/rum-cookies-and-web-storage#dynatrace-rum-cookies "Learn how Dynatrace RUM and Session Replay use cookies, web storage, and IndexedDB."). When **Data-collection and opt-in mode** is turned on, neither OneAgent nor the RUM JavaScript sets cookies, and the RUM JavaScript doesn't capture any data. After an end user accepts your cookie policy, you can activate RUM for that user via the [`dtrum.enable()`ï»¿](https://docs.dynatrace.com/javascriptapi/doc/types/dtrum.html#enable) JavaScript API call. Using the [`dtrum.disable()`ï»¿](https://docs.dynatrace.com/javascriptapi/doc/types/dtrum.html#disable) API call, you can implement a dialog that allows end users to stop sending monitoring data to Dynatrace even after they've previously agreed to it and `dtrum.enable()` has already been called.

## Do Not Track

To access this option, select **General settings** > **Data privacy** > **General** from the application settings.

ð¢ Enabled by default

Another technique for protecting end-user privacy is the "Do Not Track" feature. When a user enables this feature, their browser adds the `DNT` HTTP request header to all outgoing web requests. This header specifies that the user prefers not to be tracked.

After you turn on **Comply with "Do Not Track" browser settings**, you can select between two options:

* **Capture anonymous user sessions for "Do Not Track"-enabled browsers**: When the `DNT` header is detected, Dynatrace captures RUM data but excludes all personal information that could lead to the identification of the user. The IP address is masked, and no [user tag](/managed/observe/digital-experience/rum-concepts/user-and-error-events#user-tagging "Learn about user and error events and the types of user and error events captured by Dynatrace.") information is sent.

  With the [**User tracking** setting](#user-tracking) enabled, Dynatrace still sets a persistent cookie to detect returning users.
* **Turn Real User Monitoring off for "Do Not Track"-enabled browsers**: When the `DNT` header is detected, Dynatrace doesn't capture any data from browsers that have the "Do Not Track" setting enabled.

If you turn off **Comply with "Do Not Track" browser settings**, Dynatrace ignores the browser's "Do Not Track" setting and the `DNT` header.

The **Comply with "Do Not Track" browser settings** â **Capture anonymous user sessions for "Do Not Track"-enabled browsers** option is enabled by default for all environments and applications.

## Mask IPs and GPS coordinates

To access this option, select **General settings** > **Data privacy** > **General** > **IP masking** from the application settings.

To determine the region from which end users access web and mobile frontends, Dynatrace captures their IP addresses. GPS coordinates are captured only for mobile frontends.

When the **Mask end-user IP addresses and GPS coordinates** option is turned on, IP addresses are masked on the [beacon endpoint](/managed/observe/digital-experience/web-applications/additional-configuration/beacon-endpoint "Change the default beacon endpoint URL and send RUM beacons to Dynatrace infrastructure or another instrumented web server."). The last octet of monitored IPv4 addresses and the last 80 bits of IPv6 addresses are replaced with zeros. [Geolocation lookups](/managed/observe/digital-experience/rum-concepts/detection-of-ip-addresses-locations-and-user-agents#geolocations "Dynatrace detects IP addresses and geolocations like a city, region, and country as well as browsers, devices, and operating systems.") are performed using masked IP addresses.

## Related topics

* [Configure Session Replay for web applications](/managed/observe/digital-experience/session-replay/configure-session-replay-web "Configure monitoring consumption and data privacy settings for Session Replay.")