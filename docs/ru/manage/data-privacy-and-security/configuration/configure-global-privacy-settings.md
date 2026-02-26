---
title: Configure data privacy settings
source: https://www.dynatrace.com/docs/manage/data-privacy-and-security/configuration/configure-global-privacy-settings
scraped: 2026-02-26T21:16:43.118007
---

# Configure data privacy settings

# Configure data privacy settings

* Latest Dynatrace
* How-to guide
* 5-min read
* Updated on Jan 15, 2026

Dynatrace allows you to granularly control what data you would like to capture. Depending on your use cases, you can configure Dynatrace to provide you with the right amount of [data from your monitored environments](/docs/manage/data-privacy-and-security/data-privacy/personal-data-captured-by-dynatrace "Find out what types of end-user data may be captured during Dynatrace monitoring and the methods that are available for masking personal end-user data."). However, keep in mind that it's your responsibility to protect your customers' personal data while using Dynatrace.

We offer multiple masking layers either configured in the environment-wide settingsâwhich apply to your whole tenantâor more fine-grained configuration for the following monitored entities.

* Applications
* Services (process groups)
* Log sources

To access the environment-wide data privacy settings

1. Go to **Settings** > **Preferences** > **Data privacy**. The **Data privacy** page opens.
2. Switch between the tabs to explore all the data privacy settings.

Unless otherwise stated, all settings on the **Data privacy** page apply to both the data captured from your end users' web browsers and the data captured by OneAgent on the server side.

Besides adjusting settings provided on the **Data privacy** page, you can also [mask logs captured by OneAgent](#log-masking), [restrict the view access to personal information](#restrict-view-access) as well as [mark some request attributes as confidential](#conf-attribute).

Note that Dynatrace masks data according to our [three levels of data protection](/docs/manage/data-privacy-and-security/data-privacy/levels-of-data-protection "Learn how Dynatrace protects end-user information by applying situation-dependent levels of protection."): **at capture**, **at storage**, and **at display**. In the following sections, the data privacy settings are grouped by these levels of data protection.

## Masking at capture

With masking at capture, data is masked at first contact with Dynatrace. The original data does not leave the monitored environment.

### OneAgent-side masking

OneAgent version 1.277+ for URLs  
OneAgent version 1.285+ for exception messages

To access this setting, go to **Settings** > **Preferences** > **Data privacy** > **OneAgent-side masking**.

ð´ Disabled by default

OneAgent can mask sensitive data points at first contact. The configuration is executed directly on OneAgent; the configured data points are not sent to the Dynatrace servers and are no longer available.

Depending on your use cases and data needs, you can decide whether you want to mask the following data points.

* Email addresses in URLs

  Starting with OneAgent version 1.309, you can mask email addresses that contain percent-encoded symbols. Data masking capabilities are extended to support both URL-encoded PII data removal and base64URL-encoded URLs.

  For example:

  `http://my.company.com/api/userdata/john.doe%40company.com` is masked as `http://my.company.com/api/userdata/<masked>`

  `http://my.company.com/rest/queryinfo?detail=ALL&userid=john.doe%40company.com` is masked as `http://my.company.com/rest/queryinfo?detail=ALL&userid=<masked>`
* Query parameters
* IBANs and payment card numbers
* IDs and consecutive numbers

You can apply these settings to specific monitored process groups or globally to your whole environment.

* Process group-specific Go to ![Technologies](https://dt-cdn.net/images/technologies-512-977161d83c.png "Technologies") **Technologies & Processes Classic** > process group category > process group > **Settings** > **OneAgent-side masking**.
* Environment-wide Go to **Settings** > **Preferences** > **Data privacy** > **OneAgent-side masking**.

OneAgent-side masking settings do not affect the [Dynatrace RUM JavaScript](/docs/observe/digital-experience/rum-concepts/applications#web "Learn about monitored applications in Real User Monitoring and the different application types supported by Dynatrace."). For web applications, use the [**Mask personal data in URIs** option](/docs/observe/digital-experience/web-applications/additional-configuration/configure-real-user-monitoring-according-to-gdpr#mask-uris "Learn about the privacy settings that Dynatrace provides to ensure that your web applications comply with the data-privacy regulations of your region.") to control sensitive data point masking for URLs.

To enable the benefit of multiple layers of protection, configure the masking at capture settings independently from the masking at storage and masking at display settings. Note that data points masked at capture are no longer available. Additionally applying the masking at storage settings creates a second protection layer that might be beneficial for various compliance frameworks.

### Log masking

In Log Management and Analytics, you can benefit from [fully configurable masking rules](/docs/analyze-explore-automate/logs/lma-log-ingestion/lma-log-ingestion-via-oa/lma-sensitive-data-masking "Mask sensitive information in your log data using Log Management and Analytics.") for logs captured by OneAgent.

### End-user IP address masking

To access this setting, go to **Settings** > **Preferences** > **Data privacy** > **IP masking**.

ð¢ Enabled by default

Dynatrace captures IP addresses and GPS coordinates of end users to determine the region from which they access your application.

With the **Mask end-user IP addresses and GPS coordinates** option turned on, Dynatrace masks end user IP addresses and GPS coordinates captured by Real User Monitoring and server-side monitoring. The last octet of monitored IPv4 addresses and the last 80 bits of IPv6 addresses are replaced with zeroes. GPS coordinates are rounded up to 1 decimal place (~10 km). The masking occurs within the application, monitored process, or beacon endpoint so that the data is already masked before it's sent (data in transit) to the Dynatrace cluster. Location lookups are made using anonymized IP addresses and GPS coordinates.

The **Mask end-user IP addresses and GPS coordinates** â **Mask all IP addresses** option is enabled by default for new environments.

For mobile applications, Dynatrace uses the coordinates from the device by using GPS or Wi-Fi. If the application has the permission to use this geolocation information, Dynatrace uses it to calculate the city that is closest to the reported GPS location. If not, Dynatrace uses [MaxMind Geo2 Databaseï»¿](https://www.maxmind.com/).

### User action masking

To access this setting, go to **Settings** > **Preferences** > **Data privacy** > **General**.

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

To avoid capturing personal information for user actions in your mobile applications, check the information on [mobile user action masking](/docs/observe/digital-experience/mobile-applications/additional-configuration/configure-rum-privacy-mobile#user-action-masking "Leverage privacy settings that Dynatrace provides to ensure that your mobile apps comply with the data-privacy regulations of your region.").

## Masking at storage

When masking at storage is implemented, data is sent to the Dynatrace server for optimal analysis and is masked before it's stored.

### Masking of personal data in URIs



To access this setting, go to **Settings** > **Preferences** > **Data privacy** > **General**.

ð´ Disabled by default

Dynatrace captures full URIs of requests that are sent from desktop and mobile browsers, as well as URIs of requests that are sent and received within monitored server-side processes. URIs may contain personal data, such as user names, passwords, or IDs.

When **Mask personal data in URIs** is turned on, Dynatrace detects personal dataâemail addresses, IBANs, payment card numbers, IP addresses, UUIDs, and other IDsâin URIs, headers, exception messages, and data captured for request attributes. It masks this data at storage by replacing it with the `<masked>` string. It also replaces query parameter values with the `<masked>` string. IDs and numbers must have at least 5 decimal or hexadecimal digits to be masked.

URI masking examples

As a result, the personal data is masked in the distributed trace analysis, error analysis, user action names for RUM, and elsewhere in Dynatrace.

Note that there is a difference between the data masked out with asterisks `*****` and data replaced with `<masked>`. For more details, see [Masking at display](/docs/manage/data-privacy-and-security/configuration/configure-global-privacy-settings#masking-at-display "Learn how to set up data privacy masking for end user IP addresses, geolocations, and user action names.").

## Masking at display

When data is masked at display, it's stored in its original form but is accessible only to the users of your choice.

### Restricted view access to personal data

Dynatrace automatically considers certain data points it captures as confidential and only displays them to users who have the **View sensitive request data** [permission](/docs/manage/identity-access-management/permission-management/role-based-permissions "Role-based permissions"). All other users see that the data point exists, but the personal data is masked out with asterisks `*****`.

If your organization captures personal user data such as email addresses, IP addresses, or passwords in the course of monitoring, you should restrict view access to this personal data so that only authorized users can view it. Also note that only users with the **View sensitive request data** permission can override data masking settings.

Note that the following data types are considered confidential and are masked at display:

* Requests attributes [marked as confidential](#conf-attribute)
* Client IP addresses
* Exception messages
* URL query parameters
* HTTP headers
* HTTP POST parameters
* Original captured method argument values (the resulting request attribute is treated separately)

### Confidential request attributes

[Request attributes](/docs/observe/application-observability/services/request-attributes "Understand what request attributes are and learn how to use them across all levels of all service-analysis views.") are key-value pairs of metadata that are filterable across all Dynatrace service and distributed traces views.

Dynatrace allows you to decide whether a request attribute should be [marked as confidential](/docs/observe/application-observability/services/request-attributes#confidential "Understand what request attributes are and learn how to use them across all levels of all service-analysis views."). To manage request attributes, you must have the **Manage capturing of sensitive request data** [permission](/docs/manage/identity-access-management/permission-management/role-based-permissions "Role-based permissions").

## Opt-in mode

To access this setting, go to **Settings** > **Preferences** > **Data privacy** > **General**.

ð´ Disabled by default

To give your end users the ability to decide whether their activities should be tracked or not, enable opt-in mode.

By default, RUM automatically creates [cookies](/docs/manage/data-privacy-and-security/data-privacy/cookies#dynatrace-rum-cookies "Learn about first-party cookie usage in Dynatrace."). When **Data-collection and opt-in mode** is turned on, neither OneAgent nor the RUM JavaScript sets cookies, and the RUM JavaScript doesn't capture any data. After an end user accepts your cookie policy, you can activate RUM for that user via the [`dtrum.enable()`ï»¿](https://www.dynatrace.com/support/doc/javascriptapi/doc/types/dtrum.html#enable) JavaScript API call. Using the [`dtrum.disable()`ï»¿](https://www.dynatrace.com/support/doc/javascriptapi/doc/types/dtrum.html#disable) API call, you can implement a dialog that allows end users to stop sending monitoring data to Dynatrace even after they've previously agreed to it and `dtrum.enable()` has already been called.

## Do Not Track

To access this setting, go to **Settings** > **Preferences** > **Data privacy** > **General**.

ð¢ Enabled by default

Another technique for protecting end-user privacy is the "Do Not Track" feature. When a user enables this feature, their browser adds the `DNT` HTTP request header to all outgoing web requests. This header specifies that the user prefers not to be tracked.

After you turn on **Comply with "Do Not Track" browser settings**, you can select between two options:

* **Capture anonymous user sessions for "Do Not Track"-enabled browsers**: When the `DNT` header is detected, Dynatrace captures RUM data but excludes all personal information that could lead to the identification of the user. The IP address is masked, and no [user tag](/docs/observe/digital-experience/rum-concepts/user-and-error-events#user-tagging "Learn about user and error events and the types of user and error events captured by Dynatrace.") information is sent.

  With the [**User tracking** setting](#user-tracking) enabled, Dynatrace still sets a persistent cookie to detect returning users.
* **Turn Real User Monitoring off for "Do Not Track"-enabled browsers**: When the `DNT` header is detected, Dynatrace doesn't capture any data from browsers that have the "Do Not Track" setting enabled.

If you turn off **Comply with "Do Not Track" browser settings**, Dynatrace ignores the browser's "Do Not Track" setting and the `DNT` header.

The **Comply with "Do Not Track" browser settings** â **Capture anonymous user sessions for "Do Not Track"-enabled browsers** option is enabled by default for all environments and applications.

## User tracking

To access this setting, go to **Settings** > **Preferences** > **Data privacy** > **General**.

ð´ Disabled by default

The **Use persistent cookies for user tracking** setting allows you to enable or disable the use of persistent cookies for identifying returning users.

When turned on, the RUM JavaScript sets a persistent cookie in end-user browsers that indicates that the browser has been used previously to access your application. When turned off, RUM Classic is no longer able to associate sessions with the same user across browser restarts. Learn [how we store this cookie](/docs/manage/data-privacy-and-security/data-privacy/cookies#cookie-storage "Learn about first-party cookie usage in Dynatrace.").