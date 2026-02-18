# Dynatrace Documentation: manage/data-privacy-and-security

Generated: 2026-02-18

Files combined: 10

---


## Source: configure-global-privacy-settings.md


---
title: Configure data privacy settings
source: https://www.dynatrace.com/docs/manage/data-privacy-and-security/configuration/configure-global-privacy-settings
scraped: 2026-02-18T05:38:11.338366
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

Type of personal data

Example before masking

Example after masking

Email address

`https://example.com/user/john.doe@example.com/profile`

`https://example.com/user/<masked>/profile`

Query parameter value

`https://example.com?country=Austria&city=Linz`

`https://example.com?country=<masked>&city=<masked>`

Payment card number

`https://example.com/checkout?card=4111111111111111`

`https://example.com/checkout?card=<masked>`

IP address

`https://192.168.10.25/dashboard`

`https://<masked>/dashboard`

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


---


## Source: adaptive-data-retention.md


---
title: Adaptive Data Retention
source: https://www.dynatrace.com/docs/manage/data-privacy-and-security/data-privacy/adaptive-data-retention
scraped: 2026-02-18T05:56:44.610462
---

# Adaptive Data Retention

# Adaptive Data Retention

* Latest Dynatrace
* 6-min read
* Updated on Jan 18, 2023

Adaptive Data Retention doesn't apply to Grail-enabled deployments.

Dynatrace periodically deletes transaction storage, Session Replay storage, and Log monitoring storage data that is older than the configured retention time. Adaptive Data Retention is a functionality according to which Dynatrace periodically increases or decreases the retention time of this data if the tenant environment storage quota is exceeded.

Each data type stored on a disk has a default retention time, which specifies how long that data type can be stored on disk. See [Data retention periods](/docs/manage/data-privacy-and-security/data-privacy/data-retention-periods "Check retention times for various data types.") for more details.

The maximum amount of a given data type that can be stored on disk is determined as follows:

* The configured retention time defines how long data of a certain type should be stored on the disk. Older data is periodically deleted.
* The adapted retention time is the configured retention time reduced by a factor calculated when the tenant data exceeds its quota. If this condition doesn't apply, the adapted retention time is equal to the configured retention time.

For example, suppose all of the following statements are true:

* The configured retention time of Session Replay storage data is 10 days
* The environment has exceeded its session storage data quota
* The factor for calculating adapted retention time is 10%

In this case, the adapted retention time would be 9 days for session storage data:  
Real retention time = 10 days Ã ((100 â 10) 100) = 10 Ã 0.9 = 9 days

This would result in all Session Replay storage data older than 9 days being deleted immediately, even though the configured retention time is 10 days.

### How retention time is adapted

Retention time is decreased if the environment uses more disk space than its quota allows. This condition is continuously evaluated. If it's violated, retention time is decreased and deletion of data older than the adapted retention time begins.

After data is deleted according to the adapted retention time:

* If enough data was deleted and neither of the conditions is currently violated, then the retention time is increased again.
* If at least one of the conditions is still violated, the retention time is further decreased, and more data is deleted.

### What to do if the retention time is adapted

Adaptation of data retention time can be caused by an undersized disk or an inappropriate quota.

To prevent unwanted adaptation of retention time for data:

* Increase your quota
* Increase your disk size

## FAQ

Adaptive Data Retention is impacted by several factors. Under certain rare circumstances, the adaptation of retention time can lead to excessive data deletion for an environment. As a result, the amount of processed data that is retained and the amount of available storage, which is limited by disk space or quota, are not aligned.

To mitigate this issue:

* Increase the available disk space or quota.
* Decrease the retention time for that environment so that adaptation has less impact.

### How does a decrease in retention time affect retention time adaptation?

Because retention time adaptation is a percentage of your data retention time, a longer data retention time proportionally causes more dataâand therefore more hoursâto be deleted.

### How does adding a new environment affect the existing environments on a cluster running on full disks?

As the new environment takes up disk space, the existing environments' retention times are gradually decreased. After some time, all of the cluster's environments have the same percentage change of their configured data retention times.

### Why is the current retention time lower than the configured retention time even though there seems to be enough free disk space?

Some deviation is expected. When the deviation is too extreme, the required disk space for the configured retention time usually diverges heavily from the available disk space. Try setting the retention times to a more realistic value better suiting the currently available disk space.


---


## Source: data-protection.md


---
title: Data protection at Dynatrace
source: https://www.dynatrace.com/docs/manage/data-privacy-and-security/data-privacy/data-protection
scraped: 2026-02-18T05:51:34.499559
---

# Data protection at Dynatrace

# Data protection at Dynatrace

* Latest Dynatrace
* 4-min read
* Published May 17, 2018

We're committed to protecting the security, privacy, and availability of the Dynatrace Software Intelligence Platform. The security of your data and digital experience is a key priority for us, and we strive to protect and process your data responsibly. Proper care for data is at the core of our business.

Dynatrace enables you to be in full control of your data. With appropriate defaults in place, you determine what data to share with Dynatrace. To prevent unauthorized access, maintain data accuracy, and ensure the correct use of information, Dynatrace has physical, technical, and organizational procedures in place to safeguard your data with multiple layers of protection.

## Data minimization strategy

Dynatrace provides you with the opportunity to follow the principle of data minimization, with an aim to reduce the processing of data to a strict minimum. You control the data sent to Dynatrace with the built-in mechanisms including [data masking rules](/docs/manage/data-privacy-and-security/configuration/configure-global-privacy-settings "Learn how to set up data privacy masking for end user IP addresses, geolocations, and user action names."), [user action naming rules](/docs/observe/digital-experience/web-applications/initial-setup/create-custom-names-for-user-actions "Customize automatically generated user action names for your web applications."), [Anonymization API](/docs/dynatrace-api/environment-api/anonymization "Find out how fulfill GDPR requirements by using the Dynatrace API to remove user data."), and more. We enable you to obtain the full value of Dynatrace products and services without the necessity of sharing personal data (aside from authentication purposes) with Dynatrace.

## Privacy and security by design

Dynatrace values your privacy and trust, so we have implemented the concepts of privacy and security by design. These concepts transparently empower you to control your data and make specific privacy choices. Dynatrace assists you in making these choices and aims to ensure that privacy and security components are embedded in all parts of the product right from the beginning. This way, privacy becomes an integral part of the Dynatrace Software Intelligence Platform without diminishing the core functionality. Furthermore, our "privacy and security by design" approach allows for best-in-class [privacy and security defaults](/docs/manage/data-privacy-and-security/configuration/configure-global-privacy-settings "Learn how to set up data privacy masking for end user IP addresses, geolocations, and user action names.") out-of-the-box.

## Automated testing

To ensure best-in-class privacy, Dynatrace relies on extensive automated testing for all new and existing product functionality. Ongoing automated testing ensures the efficiency of the privacy measures that are deployed at each stage of the Dynatrace product lifecycle.

Our automated tests are:

* Adjusted and performed for every new release (bi-weekly schedule)
* Regularly reviewed to ensure 100% test coverage (bi-monthly schedule)
* Checked as part of a yearly privacy framework review

## Employee enablement

At Dynatrace, we recognize that our high data privacy and security standards depend on the awareness and engagement of each Dynatrace employee. With a culture of privacy and security risk awareness, focused data privacy principles, and recurring individual cybersecurity and privacy training, we empower our employees to sustain our market leadership in privacy and security. Easily accessible help channels and data privacy partnerships throughout the company further reinforce the culture of data privacy and security at Dynatrace.

## Access control

You control whether Dynatrace has access to your data. Only users who are members of the monitoring environment's administrative groups, which are tightly controlled by you, can grant or revoke access to the collected data. For information on what options you have for managing access control in Dynatrace, see [Role-based permissions](/docs/manage/identity-access-management/permission-management/role-based-permissions "Role-based permissions").

When you need our support, authorized Dynatrace employeesâspecifically, second- and third-level support representativesâcan be granted access to view your data. Such access is restricted by a strong "need to access" policy. Each access is logged, time-stamped, and made available to you in an automated way via our REST API. All authorized Dynatrace employees are bound by strict confidentiality agreements.

## Monitoring and audit logging

All systems operated by Dynatrace are subject to health and security monitoring, audit logging, and automated system log analysis. When Dynatrace support is requested for remote installations, access to your systems is recorded in [audit logs](/docs/manage/data-privacy-and-security/configuration/audit-logs-api "Learn how to manage audit logs using an API.").

## Data retention management

To perform monitoring services, Dynatrace retains only the data that you elect to share and stores it in your Dynatrace Cluster. Dynatrace automatically deletes data that is older than the configured [retention periods](/docs/manage/data-privacy-and-security/data-privacy/data-retention-periods "Check retention times for various data types."). Dynatrace also provides [Adaptive Data Retention](/docs/manage/data-privacy-and-security/data-privacy/adaptive-data-retention "Find out how the retention time for the data stored in the transaction, Session Replay, and Log monitoring storages is adjusted.") as functionality to periodically increase or decrease the data retention time when your environment storage quota is exceeded.

## Alignment with data protection laws

Dynatrace provides flexible [data privacy settings](/docs/manage/data-privacy-and-security/configuration/configure-global-privacy-settings "Learn how to set up data privacy masking for end user IP addresses, geolocations, and user action names.") that enable you to fine-tune your environment and application configuration according to regional privacy laws.

## Security controls

Dynatrace also provides multi-layered [security controls](/docs/manage/data-privacy-and-security/data-security/data-security-controls "Learn about data security and operational security controls.") to keep your data safe.


---


## Source: data-retention-periods.md


---
title: Data retention periods
source: https://www.dynatrace.com/docs/manage/data-privacy-and-security/data-privacy/data-retention-periods
scraped: 2026-02-18T05:38:17.229442
---

# Data retention periods

# Data retention periods

* Latest Dynatrace
* 8-min read
* Updated on Jan 28, 2026

Dynatrace stores and retains different types of monitored data from your environments. The monitoring data is stored on the Dynatrace cluster. The following table shows the general retention periods for service data (distributed traces), Real User Monitoring (user actions and user sessions), synthetic monitors, Log Management and Analytics, and metric time series data.

## Trial accounts

After a 15-day trial account expires, Dynatrace continues to store the monitoring data from the account for 30 days to ensure that no data is lost.

## Purchased accounts

For active Dynatrace accounts, the following retention rates are set by default:

Data type

Retention rate

[Distributed tracing powered by Grail](#traces-grail)

Configurable, from `10 days` to `10 years` of retention time

[Distributed traces Classic](#traces-classic)

`10 days`

[Services Classic: Requests and request attributes](#request-attributes)

`35 days`

[RUM Classic: User action data](#rum-aggregated)

`35 days`

[RUM Classic: User sessions](#rum-user-session)

`35 days`

[RUM Classic: Mobile crashes](#rum-mobile-crashes)

`35 days`

[RUM Classic: Session Replay](#rum-session-replay)

`35 days`

[New RUM Experience: User events](#new-rum-user-events-and-sessions)

`35 days`

[New RUM Experience: User sessions](#new-rum-user-events-and-sessions)

`35 days`

Synthetic

`35 days`

[Log Management and Analytics](#log-management)

Configurable, with maximum `10 years` of retention time

[Log Monitoring Classic](#log-monitoring)

`35 days`

[Metrics powered by Grail](#metrics-grail)

`15 months`

[Metrics Classic](#metrics-classic)

`5 years`

[OneAgent diagnostics](#diagnostics) (support archives and analysis results)

`30 days`

[Davis problems and events](/docs/dynatrace-intelligence "Get familiar with the capabilities of Dynatrace Intelligence.")

`14 months`

[Security data powered by Grail](#security-grail)

1 to 3 years depending on source (`3 years` for Dynatrace-generated, `1 year` for third-party)

[Security data Classic](#security-classic)

Open vulnerabilities: retained until resolution; Resolved vulnerabilities: `365 days`; Events: `365 days`

## Distributed tracing powered by Grail

With [Distributed tracing powered by Grail](/docs/observe/application-observability/distributed-tracing "Trace and analyze in real time highly distributed systems with Grail.") you can to ingest, process, retain, and analyze trace data stored in the Grail data lakehouse in SaaS environments.

With Grail storage, you don't have to worry about managing data storage performance, availability, or free space. Select the desired retention period for your traces in the [bucket configuration](/docs/observe/application-observability/distributed-tracing/storage "Manage data storage and retention for Distributed Tracing powered by Grail."). For span buckets, the available retention period ranges from 10 days to 10 years, with an additional week.

## Distributed traces Classic

Dynatrace stores the complete details of every transaction for 10 days . This enables you to analyze individual transactions and get all the details available with your [instrumentation](/docs/observe/application-observability/distributed-traces "Gain observability into highly distributed, cloud-native architectures to effectively trace and analyze transactions in real time.").

For trial users, an additional storage-size limit applies, which might lead to shorter retention times.

### Code-level insights

Code-level insights are available with OneAgent instrumentation for 10 days.

After 10 days, session data is optimized for aggregated views. Non-aggregated and aggregated code-level data produce comparable results for longer timeframes, while differences may be expected for shorter timeframes.

## Services Classic: Requests and request attributes

Short-term storage of the data related to service metrics used in [multidimensional analysis](/docs/observe/application-observability/multidimensional-analysis "Configure a multidimensional analysis view and save it as a calculated metric.") and [request charting](/docs/observe/application-observability/services-classic#charts "Learn about Dynatrace's classic service monitoring"). This data is available for 35 days with the following interval granularity levels:

| Timeframe | Interval granularity |
| --- | --- |
| Less than 20 minutes | 10 seconds |
| 20â40 minutes | 20 seconds |
| 40â60 minutes | 30 seconds |
| More than 1 hour | 1 minute |

A short-timeframe analysis accesses code-level data that is available for 10 days.

After 10 days, session data is optimized for aggregated views. Non-aggregated and aggregated code-level data produce comparable results for longer timeframes, while differences may be expected for shorter timeframes.

## RUM Classic: User action data

Aggregated user action metrics, which are used in tables like **Top user actions** and **Top JavaScript errors**, are available for 35 days. After 10 days, user actions data is optimized for aggregated views, and some individual user actions become unavailable for individual analysis. However, the sample set is large enough for statistically correct aggregations.

For [key user actions](/docs/observe/digital-experience/rum-concepts/user-actions#key-user-actions "Learn what user actions are and how they help you understand what users do with your application."), raw user action data is also kept for 35 days. The retention for timeseries data of key user actions is the same as for [timeseries metrics](/docs/manage/data-privacy-and-security/data-privacy/data-retention-periods#metrics-classic "Check retention times for various data types.").

## RUM Classic: User sessions

Includes Session Replay data. All user session data is stored for 35 days. Note that waterfall analysis and JavaScript error data is stored with [distributed trace code-level insights and errors](#purepath).

## RUM Classic: Mobile crashes

Includes all crash data and stack traces of mobile and custom applications. The data is stored for 35 days.

Note

The crash reporting data displayed in the application detailed page may differ from such data in the statistics page. For these pages, it is pulled from different storage, and has a different retention period.

![Crash count in the application detailed page](https://dt-cdn.net/images/screenshot-2025-07-25-1329111-841-6e117f2c42.png)

![Total crash count in the crash statistics page](https://dt-cdn.net/images/screenshot-2025-07-25-13373334-841-563d3575e2.png)

## RUM Classic: Session Replay

Minimum size of required Session Replay storage volume is entirely load-dependent. A maximum size isn't required.

A dedicated disk is used for Session Replay data.

## New RUM Experience: User events and user sessions

The default retention time for both user eventsâincluding user interactionsâand user sessions is 35 days. You can extend data retention by joining the [Extended Retention for RUM & Synthetic preview](/docs/whats-new/preview-releases#extended-retention-for-rum-and-synthetic "Learn about our Preview releases and how you can participate in them.").

## Log Management and Analytics

Log Management and Analytics enables you to ingest, process, retain and analyze log data stored in the [Grail](/docs/analyze-explore-automate/logs "Log Management and Analytics provides a unified approach to controlling and studying your log data in Dynatrace.") data lakehouse in SaaS environments.

With Grail storage, you don't have to worry about managing data storage performance, availability, or free space. Select the desired retention period for your logs in the [bucket configuration](/docs/analyze-explore-automate/logs/lma-bucket-assignment "Your log data can be stored in data retention buckets based on specific retention periods."). For log buckets, the available retention period ranges from 1 day to 10 years, with an additional week.

## Log Monitoring Classic

Log Monitoring Classic enables you to store all logs centrally within external storage. This makes log data available independent of log files themselves.

Log files are stored in Amazon Elastic File System in the zone where your Dynatrace environment resides. You don't have to worry about storage performance, availability, or free space. Disk storage costs are included in your Log Monitoring Classic subscription.

## Memory dumps

Memory dumps are immediately deleted from the disk once they're uploaded to ActiveGate. When an upload isn't possible, memory dumps up to 20 GB are stored on the disk for up to 2 hours.

## Metrics powered by Grail

Metrics powered by Grail provides a default 1-minute interval granularity for 15 months. Metrics with this granularity and retention can be accessed via Platform applications, such as [Dashboards and Notebooks](/docs/analyze-explore-automate/dashboards-and-notebooks "Dashboards and Notebooks"). Learn more at [Metrics Limits](/docs/analyze-explore-automate/metrics/limits "Reference of metrics powered by Grail").

## Metrics Classic

The following interval granularity levels are available for dashboarding and API access:

| Timeframe | Interval granularity |
| --- | --- |
| 0â14 days | 1 minute |
| 14â28 days | 5 minutes |
| 28â400 days | 1 hour |
| 400 daysâ5 years | 1 day |

To provide accurate calculations for timeseries metrics, Dynatrace uses the [P2 algorithmï»¿](https://dl.acm.org/citation.cfm?id=4378) to calculate the quantiles dynamically. This algorithm is known to yield good results and it works well with values in the long tails of value distributions. However, the aggregation algorithm is neither associative (`(a + b ) + c == a + ( b + c )`) nor commutative (`a + b + c == c + b + a`). For some metrics, for example, response times, this might lead to different quantile values each time the algorithm runs or when the data is aggregated in different ways, for example, one metric is split by URL and another by browser.

## OneAgent and ActiveGate diagnostics

OneAgent diagnostics and ActiveGate diagnostics are optional features that enable you to collect and analyze support archives for anomalies.

Support archives are created by Dynatrace OneAgent or Dynatrace ActiveGate and stored in Cassandra, where they are automatically deleted after 30 days. When you allow Dynatrace to analyze an issue, an additional copy of the support archive is stored in the configured AWS S3 bucket. Results of the issue analysis and the support archive are also automatically deleted from the AWS S3 bucket after 30 days. Dynatrace OneAgent and Dynatrace ActiveGate do not keep copies of created support archives.

You can delete OneAgent or ActiveGate diagnostics issues at any time. If you delete an issue, the related support archive and analysis report are deleted from Cassandra and the AWS S3 bucket immediately. The analysis result in Dynatrace Health Control is deleted after 30 days.

## Security data powered by Grail

Depending on the source of the data, Dynatrace stores [security events](/docs/secure/threat-observability/concepts#security-events "Basic concepts related to Threat Observability") in dedicated [Grail buckets](/docs/platform/grail/organize-data#built-in-grail-buckets "Insights on the Grail data model consisting of buckets, tables, and views.") for different periods of time, as follows:

* Security events generated by Dynatrace from your monitored environment are stored in the `default_securityevents_builtin` bucket for **three years**.
* Security events ingested from third-party sources are stored in the `default_securityevents` bucket for **one year**.

## Security data Classic

### Vulnerabilities

* Open [third-party vulnerabilities](/docs/secure/application-security/vulnerability-analytics/third-party-vulnerabilities "Monitor, visualize, analyze, and remediate third-party vulnerabilities, track the remediation progress, and create monitoring rules.") are stored as long as they are open, regardless of the timeframe.
* The storage time for resolved third-party vulnerabilities depends on when vulnerabilities are resolved:

  + If a vulnerability is resolved before 365 days since it was first opened, it's deleted after 365 days.
  + If a vulnerability is resolved after 365 days since it was first opened, it's deleted on its closest anniversary of the date when it was first opened.

  Examples:

  | First opened | First resolved | Reopened | Resolved again | Delete date |
  | --- | --- | --- | --- | --- |
  | 2022-05-12 | 2023-05-06 |  |  | 2023-05-13 |
  | 2022-05-12 | 2023-08-06 |  |  | 2024-05-13 |
  | 2022-05-12 | 2023-08-06 | 2024-01-01 | 2024-02-08 | 2024-05-13 |

### Events

[Third-party vulnerability evolution events](/docs/secure/application-security/vulnerability-analytics/third-party-vulnerabilities/manage-third-party-vulnerabilities#evolution "Monitor the security issues of your third-party libraries.") are stored for 365 days and can only be queried up to the timestamp of when the vulnerability was first detected.

![First detected timestamp](https://dt-cdn.net/images/2023-12-13-09-27-13-602-340a8dff4a.png)


---


## Source: create-scheduled-scan.md


---
title: Create scheduled scan in Sensitive Data Center
source: https://www.dynatrace.com/docs/manage/data-privacy-and-security/data-privacy/sensitive-data-center/create-scheduled-scan
scraped: 2026-02-17T21:32:16.626073
---

# Create scheduled scan in Sensitive Data Center

# Create scheduled scan in Sensitive Data Center

* Latest Dynatrace
* How-to guide
* 4-min read
* Published Dec 16, 2025
* Preview

You can configure scheduled scans in ![Sensitive Data Center](https://dt-cdn.net/images/privacy-rights-highresolution-1024-fa3477e788.png "Sensitive Data Center") **Sensitive Data Center** to continuously monitor your environment for sensitive data. You can choose to monitor specific buckets or the entire environment, select sensitive data types from built-in rules, and define how often the scan runs.

## Configure scans in Sensitive Data Scanner

To create a recurring scan for continuous monitoring

1. Go to ![Sensitive Data Center](https://dt-cdn.net/images/privacy-rights-highresolution-1024-fa3477e788.png "Sensitive Data Center") **Sensitive Data Center**.
2. Go to the **Scanner** tab and select **Create scan**.
3. Choose one or more **Sensitive data types** from the list, such as email address, credit card numbers, or IP addresses.
4. Define the scan interval by selecting the cadence depending on your compliance needs.
5. Select the **Log bucket scope** by either choosing specific buckets from the list or the entire environment.
6. Optional Apply scan policies to refine the scope of the scanâfor example, to exclude known false positives. For details, see [Create a policy in Sensitive Data Center](/docs/manage/data-privacy-and-security/data-privacy/sensitive-data-center/create-policy "Create a policy to enrich or filter request results with Sensitive Data Center.").
7. Provide a meaningful name for the scan.
8. Select **Create scan** to save the configuration.

The scan runs automatically at the defined interval and alerts you when data matching the selected criteria is found.

## Review scan results

The scanner dashboard provides a clear overview of scan statuses and highlights when sensitive data is found. From there, you can drill down into a specific scan to review detailed findings and understand exactly what was detected.

You can review the results and examine the data flow from ingestion to the storage location.

For environments with high log ingest volume, scan results may be sampled. Sampling is adaptive and helps reduce processing costs while maintaining detection accuracy. The sampling rate adjusts automatically based on your current log ingest volume.

## Mitigate potential findings

Based on scan results, you can take immediate action:

* [Configure or adjust masking rules](/docs/manage/data-privacy-and-security/configuration/configure-global-privacy-settings "Learn how to set up data privacy masking for end user IP addresses, geolocations, and user action names.") to prevent similar data ingestion.
* Change access permissions for stored data.
* Update [data retention periods](/docs/manage/data-privacy-and-security/data-privacy/data-retention-periods "Check retention times for various data types.").
* Use [cleanup functionality](/docs/manage/data-privacy-and-security/data-privacy/sensitive-data-center/cleanup-data "Clean up data with Sensitive Data Center cleanup requests.") to delete sensitive data as needed.


---


## Source: sensitive-data-center.md


---
title: Sensitive Data Center
source: https://www.dynatrace.com/docs/manage/data-privacy-and-security/data-privacy/sensitive-data-center
scraped: 2026-02-18T05:52:54.159311
---

# Sensitive Data Center

# Sensitive Data Center

* Latest Dynatrace
* App
* 9-min read
* Updated on Jan 21, 2026

## Prerequisites

### Permissions

The following table describes the required permissions.

Permission

Description

storage:logs:read

Enables the app to query logs

storage:logs:write

Enables the app to write privacy audit logs

storage:buckets:read

Enables the app to list Grail buckets

state:app-states:read

Enables the app to read request data

state:app-states:write

Enables the app to store request data

state:app-states:delete

Enables the app to delete request policies

state:user-app-states:read

Enables the app to read user configuration

state:user-app-states:write

Enables the app to store user configuration

iam:service-users:use

Enables the app to process requests using a service user

email:emails:send

Enables the app to send status updates for requests

10

rows per page

Page

1

of 1

## Before you begin

Some one-time setup is necessary before using ![Sensitive Data Center](https://dt-cdn.net/images/privacy-rights-highresolution-1024-fa3477e788.png "Sensitive Data Center") **Sensitive Data Center**.

### Create service user

![Sensitive Data Center](https://dt-cdn.net/images/privacy-rights-highresolution-1024-fa3477e788.png "Sensitive Data Center") **Sensitive Data Center** uses a service user to continue processing scans and requests while you aren't using the app. See [Create service users](/docs/manage/identity-access-management/user-and-group-management/access-service-users#create-service-users "Service users") to learn how to create the service user. Follow the following instructions to set up the service user:

1. Name the service user `sensitive-data-center`. The name must match exactly.
2. Create a policy with the policy statement below, to grant the service user the required permissions.
3. Create a group to assign the policy to (for example, `sensitive-data-center-service-users`) and assign the service user to this group. For more details, see [Create policies based on a service user](/docs/manage/identity-access-management/user-and-group-management/access-service-users#policy "Service users").
4. This user must also be assigned to the `sensitive-data-center-users` group defined in the next section.

```
ALLOW app-engine:apps:run WHERE shared:app-id = 'dynatrace.sensitive.data.center';



ALLOW state:app-states:read, state:app-states:write, state:app-states:delete WHERE shared:app-id = 'dynatrace.sensitive.data.center';



ALLOW iam:users:read, iam:groups:read;



ALLOW storage:records:delete, storage:logs:write, storage:events:write;



ALLOW storage:fieldsets:read, storage:system:read, storage:logs:read, storage:events:read, storage:bizevents:read, storage:metrics:read, storage:spans:read, storage:buckets:read;



ALLOW email:emails:send;



ALLOW document:documents:read, document:documents:write, document:direct-shares:write, document:documents:delete, document:trash.documents:delete;



ALLOW automation:workflows:read, automation:workflows:write;
```

If you previously used **Privacy Rights**, rename your `privacy-rights` service user to `sensitive-data-center` rather than creating a new service user. Note that the required permissions have changed and you must also update them. Renaming your service user allows ![Sensitive Data Center](https://dt-cdn.net/images/privacy-rights-highresolution-1024-fa3477e788.png "Sensitive Data Center") **Sensitive Data Center** to automatically clean up the workflow used by **Privacy Rights**. Alternatively, a Workflows administrator can delete it manually.

### `sensitive-data-center-users` group

Assign users to this group when you want them to be able to create requests and scans. To view all matching data for requests and scans, these users need unrestricted access to data in [Grail](/docs/platform/grail/dynatrace-grail "Grail is the Dynatrace data lakehouse that's designed explicitly for observability and security data and acts as single unified storage for logs, metrics, traces, events, and more."). For ![Sensitive Data Center](https://dt-cdn.net/images/privacy-rights-highresolution-1024-fa3477e788.png "Sensitive Data Center") **Sensitive Data Center** to function correctly, the group name must match exactly and a [policy](/docs/manage/identity-access-management/permission-management/manage-user-permissions-policies/iam-policy-mgt "Create, edit, copy, and delete IAM policies for managing Dynatrace user permissions.") with the following permissions must be assigned to the group:

```
ALLOW app-engine:apps:run WHERE shared:app-id = 'dynatrace.sensitive.data.center';



ALLOW app-engine:functions:run;



ALLOW state:app-states:read, state:app-states:write, state:app-states:delete WHERE shared:app-id = 'dynatrace.sensitive.data.center';



ALLOW state:user-app-states:read, state:user-app-states:write, state:user-app-states:delete WHERE shared:app-id = 'dynatrace.sensitive.data.center';



ALLOW iam:service-users:use WHERE iam:service-user-email = "YOUR-SERVICE-USER-EMAIL-HERE";



ALLOW iam:users:read, iam:groups:read;



ALLOW storage:logs:write, storage:events:write;



ALLOW storage:fieldsets:read, storage:logs:read, storage:bizevents:read, storage:buckets:read;



ALLOW email:emails:send;



ALLOW document:documents:read;



ALLOW automation:workflows:read, automation:workflows:write;
```

Replace the placeholder value for `iam:service-user-email` with the email of your `sensitive-data-center` service user. To find the email of your service user:

1. In Dynatrace, go to [Account Management](/docs/manage/account-management "Manage your Dynatrace license, subscriptions, and platform adoption and environment health.").
2. Select **Identity & access management** > **Service users**. You will see an overview table with all of your service users.
3. In the **Actions** column, select  >  **Edit**.
4. The service user's email is displayed at the top.

If you previously used **Privacy Rights**, this group is equivalent to the `Privacy Rights request assignees` group. You can edit the group name and reuse the same group, but note that you need to add additional permissions to the policy. These permissions support the Sensitive Data Scanner functionality, which is currently available as a [preview program](/docs/whats-new/preview-releases "Learn about our Preview releases and how you can participate in them.") in ![Sensitive Data Center](https://dt-cdn.net/images/privacy-rights-highresolution-1024-fa3477e788.png "Sensitive Data Center") **Sensitive Data Center**.

### `sensitive-data-center-admins` group

Assign users to this group when you want them to be able to approve requests and delete data from Grail. All users assigned to this group must also be assigned to the `sensitive-data-center-users` group. For ![Sensitive Data Center](https://dt-cdn.net/images/privacy-rights-highresolution-1024-fa3477e788.png "Sensitive Data Center") **Sensitive Data Center** to function correctly, the group name must match exactly and a [policy](/docs/manage/identity-access-management/permission-management/manage-user-permissions-policies/iam-policy-mgt "Create, edit, copy, and delete IAM policies for managing Dynatrace user permissions.") with this permission must be assigned to the group:

```
ALLOW storage:records:delete;
```

If you previously used **Privacy Rights**, this group is equivalent to the `Privacy Rights request reviewers` group. You can edit the group name and reuse the same group, but note that the policy has changed.

### Configure audit logging

By default, audit logs go to the `default_logs` bucket. To change this, you can create a `privacy_audit` bucket to assign audit logs to. The name must match exactly. You can customize the retention period to suit your needs and restrict access to the bucket using IAM policies. You also need to [configure bucket assignment](/docs/analyze-explore-automate/logs/lma-bucket-assignment "Your log data can be stored in data retention buckets based on specific retention periods.") so that logs matching `log.source == "Sensitive Data Center"` are assigned to the `privacy_audit` bucket.

### Restrict access

As sensitive data is visible in ![Sensitive Data Center](https://dt-cdn.net/images/privacy-rights-highresolution-1024-fa3477e788.png "Sensitive Data Center") **Sensitive Data Center**, we recommend you restrict access for users who don't need to create or review requests and scans. To prevent users from accessing ![Sensitive Data Center](https://dt-cdn.net/images/privacy-rights-highresolution-1024-fa3477e788.png "Sensitive Data Center") **Sensitive Data Center**, you can assign them to a group with the following policy:

```
DENY app-engine:apps:run WHERE shared:app-id = 'dynatrace.sensitive.data.center';



DENY state:app-states:read, state:app-states:write, state:app-states:delete WHERE shared:app-id = 'dynatrace.sensitive.data.center';



DENY state-management:app-states:delete WHERE shared:app-id = 'dynatrace.sensitive.data.center';



DENY iam:service-users:use WHERE iam:service-user-email = "YOUR-SERVICE-USER-EMAIL-HERE";
```

They should also be denied read access to audit logs in the `default_logs` or `privacy_audit` buckets (depending on your chosen audit logging configuration).

## Get started

![Sensitive Data Center](https://dt-cdn.net/images/privacy-rights-highresolution-1024-fa3477e788.png "Sensitive Data Center") **Sensitive Data Center** empowers you to address and manage customer requests related to data subject rights under applicable data protection laws (for example, GDPR and CCPA/CPRA).

![Sensitive Data Center](https://dt-cdn.net/images/privacy-rights-highresolution-1024-fa3477e788.png "Sensitive Data Center") **Sensitive Data Center** helps you to:

* [Export personal data](/docs/manage/data-privacy-and-security/data-privacy/sensitive-data-center/export-personal-data "Export personal data with Sensitive Data Center export requests."): Review and export personal data that relates to a specific end user.
* [Delete personal data](/docs/manage/data-privacy-and-security/data-privacy/sensitive-data-center/delete-personal-data "Delete personal data with Sensitive Data Center deletion requests."): Review and delete personal data that relates to a specific end user.
* [Clean up data](/docs/manage/data-privacy-and-security/data-privacy/sensitive-data-center/cleanup-data "Clean up data with Sensitive Data Center cleanup requests."): Delete mistakenly ingested data for a specific timeframe.
* [Schedule scans](/docs/manage/data-privacy-and-security/data-privacy/sensitive-data-center/create-scheduled-scan "Create a scheduled scan to maintain personal data with Sensitive Data Center."): Create scans for mistakenly ingested sensitive data, such as credit card numbers and IBANs, using the Sensitive Data Scanner. This functionality is only available as a [preview](/docs/whats-new/preview-releases "Learn about our Preview releases and how you can participate in them.").

![Sensitive Data Center](https://dt-cdn.net/images/privacy-rights-highresolution-1024-fa3477e788.png "Sensitive Data Center") **Sensitive Data Center** currently supports export, deletion, and cleanup of Grail logs. Other data types are not supported.

![Sensitive Data Center](https://dt-cdn.net/images/privacy-rights-highresolution-1024-fa3477e788.png "Sensitive Data Center") **Sensitive Data Center** uses a multi-party access control model to protect your data. This requires setup of policies, groups, and a service user before first use of the app. See [Prerequisites](#prerequisites) to learn more.

We recommend that you restrict access to the app, app state, service user, and audit logs to a small group of trusted users. The service user has extensive permissions and could be mistakenly or deliberately abused, for example, to delete a large volume of data. Users with access to the app state may be able to modify requests even if they don't have access to the app UI. To learn how to restrict access, see [Prerequisites](#prerequisites).

![Create a request to review and export personal data about a specific end-user. The overview includes details of all requests, including the relevant user identifier, assignees and reviewers, the current status of each request, as well as the defined due date. Audit logs and request policies can be accessed and managed from this page.](https://cdn.hub.central.dynatrace.com/hub/hub1_DVwrUOD.png)![In the export request form, you specify the user details such as user type, a user identifier to search for matching data in Grail, and the scope of the search in Grail (the timeframe and log buckets).](https://cdn.hub.central.dynatrace.com/hub/hub3_qr80Yha.png)![For each created request, the data matching the executed query are returned and can be viewed by number of log records, volume, data residency, as well as number of systems. The reviewer can then approve or reject export of this data.](https://cdn.hub.central.dynatrace.com/hub/hub4-final.png)

1 of 3Create a request to review and export personal data about a specific end-user. The overview includes details of all requests, including the relevant user identifier, assignees and reviewers, the current status of each request, as well as the defined due date. Audit logs and request policies can be accessed and managed from this page.

## Use cases

* Easily filter, query, and review data processed about a specific end-user in Grail.
* Export personal data relating to a specific end-user to respond to an access request (for example, right of access in the GDPR).
* Delete personal data relating to a specific end-user to comply with a deletion request (for example, right of erasure in the GDPR).
* Cleanup any mistakenly ingested data for a specific timeframe.

## Best practices

To limit the scope of requests:

* Use the shortest possible timeframe and select relevant buckets only.
* Make sure you aren't exporting personal data of other individuals or confidential data.
* Use [policies](/docs/manage/data-privacy-and-security/data-privacy/sensitive-data-center/create-policy "Create a policy to enrich or filter request results with Sensitive Data Center.") to help ensure that your organizationâs policies regarding sensitive data are followed.
* Minimize the number of logs you export/delete so it is easier to review the data.

## FAQ

I see a banner informing me that permissions are misconfigured, what should I do?

If you see a banner informing you that permissions are misconfigured, confirm that:

1. Permissions are configured correctly for the service user, to learn more see [Prerequisites](#prerequisites).
2. The simple workflow used by the app has not been mistakenly deleted or switched off. Users with the `automation:workflows:admin` permission can view and edit the workflow in **Workflows** after enabling admin mode. The workflow should be enabled on a schedule and include the appâs **Process deletion requests** workflow action.

I noticed that deletion and cleanup requests in the "Approved" state don't transition into the "Processing" state, what should I do?

If you notice that deletion and cleanup requests in the **Approved** state don't transition into the **Processing** state, confirm that:

1. Permissions are configured correctly for the service user, to learn more see [Prerequisites](#prerequisites).
2. The simple workflow used by the app has not been mistakenly deleted or switched off. Users with the `automation:workflows:admin` permission can view and edit the workflow in **Workflows** after enabling admin mode. The workflow should be enabled on a schedule and include the appâs **Process deletion requests** workflow action.

My request is in "Failed" state, what should I do?

If any deletion error occurs, then your request transitions into the **Failed** state. In the request details, further information will be provided for each failed task. Deletion and cleanup requests are processed in one or more tasks that cover specific timeframes. You can assume that deletion has succeeded for any timeframe not listed in the failed tasks. There are four reasons why a deletion task may fail:

1. **Invalid request:** the request was not accepted because either it uses [DQL that is unsupported for deletion](/docs/platform/grail/organize-data/record-deletion-in-grail "Find out how to delete records in Grail via API.") or it matches too many records. No data has been deleted. You can resolve this by creating a new request with a modified query and attempting deletion again for the failed timeframe(s).
2. **Trigger timeout:** due to a temporary outage, it was not possible to start deletion and the task timed out. No data has been deleted. We recommend you wait 12 hours or longer, then create a new request for the failed timeframe(s) to attempt deletion again.
3. **Processing timeout:** due to a temporary outage during deletion, the task has timed out. Data may have been partially deleted. We recommend you wait 12 hours or longer, then create a new request for the failed timeframe(s) to attempt deletion again.
4. **Internal error:** an internal error occurred during deletion. In this unlikely case, data may have been partially deleted for the timeframe. Please contact Support so we can assist you in resolving the issue.

Why do I get an error when I approve a request?

If you see an error, either you are missing permissions or the app is not yet fully set up. To approve a request, you must be a member of the `sensitive-data-center-admins` group. Confirm that you are in this group, the `sensitive-data-center` service user exists, and both the group and service user are configured as described in [Prerequisites](#prerequisites). The names must match exactly.

Why can't I see my audit logs in the Audit Log tab?

If no audit logs are visible in ![Sensitive Data Center](https://dt-cdn.net/images/privacy-rights-highresolution-1024-fa3477e788.png "Sensitive Data Center") **Sensitive Data Center**, check if bucket assignment is misconfigured.

If the `privacy_audit` bucket exists, bucket assignment must be configured to route ![Sensitive Data Center](https://dt-cdn.net/images/privacy-rights-highresolution-1024-fa3477e788.png "Sensitive Data Center") **Sensitive Data Center** audit logs to it, as ![Sensitive Data Center](https://dt-cdn.net/images/privacy-rights-highresolution-1024-fa3477e788.png "Sensitive Data Center") **Sensitive Data Center** only queries this bucket.

If the `privacy_audit` bucket does not exist, check if any other assignment rules are mistakenly assigning ![Sensitive Data Center](https://dt-cdn.net/images/privacy-rights-highresolution-1024-fa3477e788.png "Sensitive Data Center") **Sensitive Data Center** audit logs to a different bucket than `default_logs`. If this is not the case, then your volume of log ingest is too high to use `default_logs` and you must configure the `privacy_audit` custom bucket (see [Prerequisites](#prerequisites)).

I previously used Privacy Rights. What happened to it?

**Privacy Rights** has been replaced by ![Sensitive Data Center](https://dt-cdn.net/images/privacy-rights-highresolution-1024-fa3477e788.png "Sensitive Data Center") **Sensitive Data Center**, which offers the same privacy rights request functionality combined with additional features for sensitive data management. To support these features, new IAM groups and policies are required, so additional one-time setup is necessary. For customers who previously used **Privacy Rights**, request data is retained in **Privacy Rights**, but requests and policies can no longer be created.

Why do I see failed scans?

The most likely cause of failed scans is misconfigured permissions for the service user. Check that the service user's name, two assigned groups, and the policies assigned to those groups exactly match the description in [Prerequisites](#prerequisites).

## Learning modules

[01Create a policy in Sensitive Data Center

* How-to guide
* Create a policy to enrich or filter request results with Sensitive Data Center.](/docs/manage/data-privacy-and-security/data-privacy/sensitive-data-center/create-policy)[02Export personal data in Sensitive Data Center

* How-to guide
* Export personal data with Sensitive Data Center export requests.](/docs/manage/data-privacy-and-security/data-privacy/sensitive-data-center/export-personal-data)[03Review audit logs in Sensitive Data Center

* How-to guide
* Review Sensitive Data Center audit logs.](/docs/manage/data-privacy-and-security/data-privacy/sensitive-data-center/review-audit-logs)[04Delete personal data in Sensitive Data Center

* How-to guide
* Delete personal data with Sensitive Data Center deletion requests.](/docs/manage/data-privacy-and-security/data-privacy/sensitive-data-center/delete-personal-data)[05Clean up data in Sensitive Data Center

* How-to guide
* Clean up data with Sensitive Data Center cleanup requests.](/docs/manage/data-privacy-and-security/data-privacy/sensitive-data-center/cleanup-data)[06Create scheduled scan in Sensitive Data Center

* How-to guide
* Create a scheduled scan to maintain personal data with Sensitive Data Center.](/docs/manage/data-privacy-and-security/data-privacy/sensitive-data-center/create-scheduled-scan)


---


## Source: user-privacy-for-android.md


---
title: Data safety guidance for Android
source: https://www.dynatrace.com/docs/manage/data-privacy-and-security/data-privacy/user-privacy-for-android
scraped: 2026-02-17T21:30:13.067651
---

# Data safety guidance for Android

# Data safety guidance for Android

* Latest Dynatrace
* 5-min read
* Updated on Sep 15, 2025

Starting July 20, 2022, Google requires you to provide your users with information on how your mobile app collects, protects, and shares their data. This also includes data collected by third-party partners like Dynatrace.

This page can help you with completing the [Data safety formï»¿](https://support.google.com/googleplay/android-developer/answer/10787469#complete_form_steps) in Google Play Console. The questions and data types reflect the Data safety form, but note that the answers reflect the out-of-the-box, default state.

OneAgent might capture additional data through your [manual instrumentation](/docs/observe/digital-experience/mobile-applications/instrument-android-app/instrumentation-via-oneagent-sdk "Learn what OneAgent SDK for Android is."). If you instrument your app to collect additional data, make sure you reflect this in the **Data safety** section in Google Play Console.

To fill out the Data safety form

1. Sign in to Google Play Console, and select the required mobile app.
2. From the menu on the left, go to **Policy** > **App content**.
3. Under **Data safety**, select **Manage**.
4. Complete the Data safety form using the information provided on this page.

## Data collection and security

Use the table below to answer the questions in this section.

Question

Answer

Note

Does your app collect or share any of the required user data types?

![Applicable](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "Applicable")Yes

Is all of the user data collected by your app encrypted in transit?

![Applicable](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "Applicable")Yes

Which of the following methods of account creation does your app support?

![Applicable](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "Applicable") My app does not allow users to create an account

Dynatrace does not provide user accounts

Can users login to your app with accounts created outside of the app?

![Not applicable](https://dt-cdn.net/images/icon-red-cross-1f1142a5dc.svg "Not applicable")No

Do you provide a way for users to request that their data is deleted?

![Not applicable](https://dt-cdn.net/images/icon-red-cross-1f1142a5dc.svg "Not applicable")No

## Data types

Select all types of data that your mobile app collects or shares.

The table below contains all data that OneAgent captures by default.

Category

Data type

Captured by default?

Note

Location

![Not applicable](https://dt-cdn.net/images/icon-red-cross-1f1142a5dc.svg "Not applicable") No

Select **Approximate location** if you've enabled [location monitoring](/docs/observe/digital-experience/mobile-applications/instrument-android-app/instrumentation-via-plugin/monitoring-capabilities#location-monitoring "Configure the Dynatrace Android Gradle plugin to adjust the monitoring capabilities of OneAgent.") and your mobile app has the permission to use the device's geolocation information.

Dynatrace can capture the [approximate location](/docs/manage/data-privacy-and-security/configuration/configure-global-privacy-settings#mask-ip-and-gps "Learn how to set up data privacy masking for end user IP addresses, geolocations, and user action names."), but it never collects a precise location.

Personal info

![Not applicable](https://dt-cdn.net/images/icon-red-cross-1f1142a5dc.svg "Not applicable") No

Select **User IDs** or other personal information data types if you collect your users' personal information via [user tagging](/docs/observe/digital-experience/mobile-applications/instrument-android-app/instrumentation-via-oneagent-sdk/oneagent-sdk-for-android#tag-specific-users "Learn how to enrich mobile user experience monitoring in Android using OneAgent SDK.").

Financial info

![Not applicable](https://dt-cdn.net/images/icon-red-cross-1f1142a5dc.svg "Not applicable") No

Health and fitness

![Not applicable](https://dt-cdn.net/images/icon-red-cross-1f1142a5dc.svg "Not applicable") No

Messages

![Not applicable](https://dt-cdn.net/images/icon-red-cross-1f1142a5dc.svg "Not applicable") No

Photos and videos

![Not applicable](https://dt-cdn.net/images/icon-red-cross-1f1142a5dc.svg "Not applicable") No

Audio files

![Not applicable](https://dt-cdn.net/images/icon-red-cross-1f1142a5dc.svg "Not applicable") No

Files and docs

![Not applicable](https://dt-cdn.net/images/icon-red-cross-1f1142a5dc.svg "Not applicable") No

Calendar

![Not applicable](https://dt-cdn.net/images/icon-red-cross-1f1142a5dc.svg "Not applicable") No

Contacts

![Not applicable](https://dt-cdn.net/images/icon-red-cross-1f1142a5dc.svg "Not applicable") No

App activity

App interactions

![Applicable](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "Applicable") Yes

Dynatrace captures user interactions, for example, app launches or taps, and reports them as user actions.

See [User action monitoring](/docs/observe/digital-experience/mobile-applications/instrument-android-app/instrumentation-via-plugin/monitoring-capabilities#action-monitoring "Configure the Dynatrace Android Gradle plugin to adjust the monitoring capabilities of OneAgent.") and [Lifecycle monitoring](/docs/observe/digital-experience/mobile-applications/instrument-android-app/instrumentation-via-plugin/monitoring-capabilities#lifecycle-monitoring "Configure the Dynatrace Android Gradle plugin to adjust the monitoring capabilities of OneAgent.") for information on how to configure or disable these features.

Web browsing

![Not applicable](https://dt-cdn.net/images/icon-red-cross-1f1142a5dc.svg "Not applicable") No

App info and performance

Crash logs

![Applicable](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "Applicable") Yes

Dynatrace captures information on [crashes](/docs/observe/digital-experience/rum-concepts/user-and-error-events#crash "Learn about user and error events and the types of user and error events captured by Dynatrace."). If you've also enabled [Session Replay on crashes](/docs/observe/digital-experience/session-replay/session-replay-android "Set up Session Replay for your Android apps to learn which actions your users perform."), Dynatrace collects several screenshots before a crash occurs.

Clear **Crash logs** if you've disabled [crash reporting](/docs/observe/digital-experience/mobile-applications/instrument-android-app/instrumentation-via-plugin/monitoring-capabilities#crash-reporting "Configure the Dynatrace Android Gradle plugin to adjust the monitoring capabilities of OneAgent.").

App info and performance

Diagnostics

![Applicable](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "Applicable") Yes

Dynatrace collects some performance information, for example, loading time of applications and activities or travel time of web requests.

App info and performance

Other app performance data

![Applicable](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "Applicable") Yes

Dynatrace captures some app performance data, for example, a device's battery level or screen resolution. In Google Play Console, you cannot specify what app performance data is collected.

App performance data collected by Dynatrace

* Battery level
* Built-in RAM
* Free RAM
* Device model
* CPU type
* Carrier name
* Network connection type, for example, mobile, WiFi, or LAN
* Network technology, for example, 2G, 3G, 4G, 5G, 802.11x
* Screen resolution
* Orientation (portrait or landscape)
* App version
* App name
* User language
* Android version
* New user (for the first session)

Device or other IDs

![Not applicable](https://dt-cdn.net/images/icon-red-cross-1f1142a5dc.svg "Not applicable") No

Dynatrace does not capture or report any device ID. We suggest that you avoid reporting device IDs via manual instrumentation.

## Data usage and handling

You also need to provide the information on how the data is used and handled for each data type that you've selected in the **Data types** section. Select **Start** to proceed.

Use the table below for all data types captured by OneAgent.

Question

Answer

Note

Is this data collected, shared or both?

Collected

Is this data processed ephemerally?

![Not applicable](https://dt-cdn.net/images/icon-red-cross-1f1142a5dc.svg "Not applicable") No

Is this data required for your app, or can users choose whether it's collected?

Data collected is required (users can't turn off this data collection)

Select **Users can choose whether this data is collected** if you've enabled the [user opt-in](/docs/observe/digital-experience/mobile-applications/additional-configuration/configure-rum-privacy-mobile#opt-in-mode-mobile "Leverage privacy settings that Dynatrace provides to ensure that your mobile apps comply with the data-privacy regulations of your region.") for your mobile app.

Why is this user data collected?

Analytics

## Related topics

* [Preparing for Google Play's new safety sectionï»¿](https://android-developers.googleblog.com/2021/07/new-google-play-safety-section.html)
* [Provide information for Google Play's Data safety sectionï»¿](https://support.google.com/googleplay/android-developer/answer/10787469)
* [Configure data privacy settings for mobile applications](/docs/observe/digital-experience/mobile-applications/additional-configuration/configure-rum-privacy-mobile "Leverage privacy settings that Dynatrace provides to ensure that your mobile apps comply with the data-privacy regulations of your region.")


---


## Source: user-privacy-for-ios.md


---
title: User privacy for iOS
source: https://www.dynatrace.com/docs/manage/data-privacy-and-security/data-privacy/user-privacy-for-ios
scraped: 2026-02-16T21:31:43.694447
---

# User privacy for iOS

# User privacy for iOS

* Latest Dynatrace
* 3-min read
* Updated on Nov 21, 2024

Starting December 8, 2020, Apple requires you to provide information about your app's privacy practices, including the practices of third-party partners like Dynatrace.

On this page, you'll find information about what kind of data [Dynatrace OneAgent for iOS](/docs/observe/digital-experience/mobile-applications/instrument-ios-app "Instrument mobile application monitoring for iOS apps, customize the auto-instrumentation, and capture additional data via manual instrumentation.") captures by default. The data categories and types reflect the Apple questionnaire, but note that the answers reflect the out-of-the-box, default state. For a detailed description of individual data types, see [App privacy details on the App Storeï»¿](https://developer.apple.com/app-store/app-privacy-details/) on the Apple developer portal.

OneAgent may capture additional data through your [manual instrumentation](/docs/observe/digital-experience/mobile-applications/instrument-ios-app/customization/oneagent-sdk-for-ios "Enrich mobile user experience monitoring using OneAgent SDK for iOS."). If you instrument your app to capture additional data, make sure you reflect it in your app privacy questionnaire.

Category

Data type

Captured by default?

Notes

Contact Info

![Not applicable](https://dt-cdn.net/images/icon-red-cross-1f1142a5dc.svg "Not applicable") No

Health & Fitness

![Not applicable](https://dt-cdn.net/images/icon-red-cross-1f1142a5dc.svg "Not applicable") No

Financial Info

![Not applicable](https://dt-cdn.net/images/icon-red-cross-1f1142a5dc.svg "Not applicable") No

Location

Precise Location

![Not applicable](https://dt-cdn.net/images/icon-red-cross-1f1142a5dc.svg "Not applicable") No

By default, [location monitoring](/docs/observe/digital-experience/mobile-applications/instrument-ios-app/instrumentation/ios-auto-instrumentation-features#location "Explore the list of features that are available after you instrument your application with OneAgent.") is disabled.

If you've set the [`DTXInstrumentGPSLocation` configuration key](/docs/observe/digital-experience/mobile-applications/instrument-ios-app/customization/ios-configuration-keys#privacy-and-security "With configuration keys, you can fine-tune the auto-instrumentation of your iOS apps.") to `true`, select this data type.

Precise Location

Coarse Location

![Not applicable](https://dt-cdn.net/images/icon-red-cross-1f1142a5dc.svg "Not applicable") No

Sensitive Info

![Not applicable](https://dt-cdn.net/images/icon-red-cross-1f1142a5dc.svg "Not applicable") No

Contacts

![Not applicable](https://dt-cdn.net/images/icon-red-cross-1f1142a5dc.svg "Not applicable") No

User Content

![Not applicable](https://dt-cdn.net/images/icon-red-cross-1f1142a5dc.svg "Not applicable") No

Browsing History

![Not applicable](https://dt-cdn.net/images/icon-red-cross-1f1142a5dc.svg "Not applicable") No

Search History

![Not applicable](https://dt-cdn.net/images/icon-red-cross-1f1142a5dc.svg "Not applicable") No

Identifiers

![Not applicable](https://dt-cdn.net/images/icon-red-cross-1f1142a5dc.svg "Not applicable") No

Purchases

![Not applicable](https://dt-cdn.net/images/icon-red-cross-1f1142a5dc.svg "Not applicable") No

Usage Data

Product Interaction

![Applicable](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "Applicable") Yes

If you use auto-instrumentation for iOS, taps and clicks the users perform in your mobile app are reported as [user actions](/docs/observe/digital-experience/mobile-applications/instrument-ios-app/instrumentation/ios-auto-instrumentation-features#user-actions "Explore the list of features that are available after you instrument your application with OneAgent."). Also, Dynatrace captures [rage taps](/docs/observe/digital-experience/mobile-applications/instrument-ios-app/instrumentation/ios-auto-instrumentation-features#rage-taps "Explore the list of features that are available after you instrument your application with OneAgent."). You can configure the capturing of product interaction data via the [configuration keys related to user actions](/docs/observe/digital-experience/mobile-applications/instrument-ios-app/customization/ios-configuration-keys#user-actions "With configuration keys, you can fine-tune the auto-instrumentation of your iOS apps.").

If you've set the [`DTXInstrumentAutoUserAction`](/docs/observe/digital-experience/mobile-applications/instrument-ios-app/customization/ios-configuration-keys#user-actions "With configuration keys, you can fine-tune the auto-instrumentation of your iOS apps.") and [`DTXDetectRageTaps`](/docs/observe/digital-experience/mobile-applications/instrument-ios-app/customization/ios-configuration-keys#user-actions "With configuration keys, you can fine-tune the auto-instrumentation of your iOS apps.") configuration keys to `false`, don't select this data type.

Usage Data

Advertising Data

![Not applicable](https://dt-cdn.net/images/icon-red-cross-1f1142a5dc.svg "Not applicable") No

Usage Data

Other Usage Data

![Not applicable](https://dt-cdn.net/images/icon-red-cross-1f1142a5dc.svg "Not applicable") No

Diagnostics

Crash Data

![Applicable](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "Applicable") Yes

By default, [crash reposting](/docs/observe/digital-experience/mobile-applications/instrument-ios-app/instrumentation/ios-auto-instrumentation-features#crashes "Explore the list of features that are available after you instrument your application with OneAgent.") is enabled. If you use [Session Replay](/docs/observe/digital-experience/session-replay/session-replay-ios "Prerequisites and the procedure for enabling Session Replay for your iOS apps."), OneAgent also captures masked screenshots and reports several screenshots captured before the crash.

If you've set the [`DTXCrashReportingEnabled` configuration key](/docs/observe/digital-experience/mobile-applications/instrument-ios-app/customization/ios-configuration-keys#privacy-and-security "With configuration keys, you can fine-tune the auto-instrumentation of your iOS apps.") to `false` and disabled Session Replay, don't select this data type.

Diagnostics

Performance Data

![Applicable](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "Applicable") Yes

By default, monitoring of [lifecycle events](/docs/observe/digital-experience/mobile-applications/instrument-ios-app/instrumentation/ios-auto-instrumentation-features#lifecycle "Explore the list of features that are available after you instrument your application with OneAgent."), [web requests](/docs/observe/digital-experience/mobile-applications/instrument-ios-app/instrumentation/ios-auto-instrumentation-features#web-requests "Explore the list of features that are available after you instrument your application with OneAgent."), and [user actions](/docs/observe/digital-experience/mobile-applications/instrument-ios-app/instrumentation/ios-auto-instrumentation-features#user-actions "Explore the list of features that are available after you instrument your application with OneAgent.") is enabled. You can configure the capturing of performance data data via the configuration keys related to [user actions](/docs/observe/digital-experience/mobile-applications/instrument-ios-app/customization/ios-configuration-keys#user-actions "With configuration keys, you can fine-tune the auto-instrumentation of your iOS apps."), [web requests](/docs/observe/digital-experience/mobile-applications/instrument-ios-app/customization/ios-configuration-keys#web-requests "With configuration keys, you can fine-tune the auto-instrumentation of your iOS apps."), and
[lifecycle monitoring](/docs/observe/digital-experience/mobile-applications/instrument-ios-app/customization/ios-configuration-keys#lifecycle-monitoring "With configuration keys, you can fine-tune the auto-instrumentation of your iOS apps.").

If you've set all of the following [configuration keys](/docs/observe/digital-experience/mobile-applications/instrument-ios-app/customization/ios-configuration-keys "With configuration keys, you can fine-tune the auto-instrumentation of your iOS apps.") to `false`, don't select this data type.

* `DTXInstrumentLifecycleMonitoring`
* `DTXInstrumentWebRequestTiming`
* `DTXInstrumentWebViewTiming`
* `DTXInstrumentAutoUserAction`

Diagnostics

Other Diagnostic Data

![Applicable](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "Applicable") Yes

OneAgent captures the following diagnostic data:

* Battery level
* Built-in RAM
* Free RAM
* Device model
* CPU type
* Carrier name
* Network connection type, for example, mobile, WiFi, or LAN
* Network technology, for example, 2G, 3G, 4G, 5G, 802.11x
* Screen resolution
* Orientation (portrait or landscape)
* App version
* App name
* User language
* iOS version
* New user (on the first session)

Diagnostics

`shareLogsFile`

![Not applicable](https://dt-cdn.net/images/icon-red-cross-1f1142a5dc.svg "Not applicable") No

The `shareLogsFile` API allows you to share locally stored log files via an iOS sharing sheet (`UIActivityViewController`). For more information, see [Log sharing](/docs/manage/data-privacy-and-security/data-privacy/personal-data-captured-by-dynatrace#log-sharing "Find out what types of end-user data may be captured during Dynatrace monitoring and the methods that are available for masking personal end-user data.").

Surroundings

![Not applicable](https://dt-cdn.net/images/icon-red-cross-1f1142a5dc.svg "Not applicable") No

Body

![Not applicable](https://dt-cdn.net/images/icon-red-cross-1f1142a5dc.svg "Not applicable") No

Other Data

![Not applicable](https://dt-cdn.net/images/icon-red-cross-1f1142a5dc.svg "Not applicable") No


---


## Source: data-security-controls.md


---
title: Data security controls
source: https://www.dynatrace.com/docs/manage/data-privacy-and-security/data-security/data-security-controls
scraped: 2026-02-17T21:25:09.122702
---

# Data security controls

# Data security controls

* Latest Dynatrace
* 10-min read
* Updated on Sep 29, 2025

## Overview of data security controls

![data-security-overview-saas-v2](https://dt-cdn.net/images/data-security-overview-saas-v2-3982-b71494b7fa.png)

## Data storage

Data is stored in Amazon Web Services (AWS), Microsoft Azure, or Google Cloud data centers. The available regions are listed below.

#### AWS Regions

* US East (N. Virginia)
* US West (Oregon)
* Europe (Ireland)
* Asia Pacific (Sydney)
* Europe (London)[1](#fn-1-1-def)
* Europe (Frankfurt)[1](#fn-1-1-def)
* Canada (Central)[1](#fn-1-1-def)
* South America (SÃ£o Paulo)[1](#fn-1-1-def)
* Asia Pacific (Singapore)[1](#fn-1-1-def)
* Asia Pacific (Mumbai)[1](#fn-1-1-def)
* Asia Pacific (Tokyo)[1](#fn-1-1-def)
* Middle East (Tel Aviv)[1](#fn-1-1-def)

1

Available on request. Talk to your Dynatrace sales contact.

#### Azure regions[1](#fn-2-1-def)

* East US (Virginia)
* West US 3 (Arizona)
* West Europe (Netherlands)
* Canada Central (Toronto)
* UAE (Dubai)
* Switzerland North (Zurich)
* Australia East (Sydney)

1

Available on request. Talk to your Dynatrace sales contact.

#### Google Cloud regions[1](#fn-3-1-def)

* us-east4 (N. Virginia)
* europe-west3 (Frankfurt)

1

Available on request. Talk to your Dynatrace sales contact.

Also see [Data retention periods](/docs/manage/data-privacy-and-security/data-privacy/data-retention-periods "Check retention times for various data types.").

## Dynatrace components

[Dynatrace OneAgent](/docs/platform/oneagent "Learn the monitoring capabilities of OneAgent.") collects all monitoring data within your monitored environment. Optionally, all data collected by OneAgent can be routed through a [Dynatrace ActiveGate](/docs/ingest-from/dynatrace-activegate "Understand the basic concepts related to ActiveGate."), which works as a proxy between Dynatrace OneAgent and the Dynatrace Cluster. In the absence of an ActiveGate, data collected by OneAgent is sent directly to the Dynatrace Cluster.

![saas-dynatrace-components](https://dt-cdn.net/images/saas-dynatrace-components-2690-a37591adb1.png)

## Data segregation between customer environments

Dynatrace SaaS uses a multi-tenant, high-availability architecture. Dynatrace allocates a tenant, a so-called Dynatrace environment, to each customer. Customers can also manage multiple environments within the Dynatrace account management system. Each environment gets its own individual domain.

With the latest Dynatrace, all Dynatrace platform data at rest, including data from Grail, AppEngine, and AutomationEngine, is stored in a separate, dedicated storage space. One single Dynatrace SaaS environment hosted on AWS uses a dedicated AWS S3 bucket as storage space. Environments hosted on Azure use dedicated Azure storage accounts. Other data, such as [Dynatrace Credential vault data](/docs/manage/credential-vault "Store and manage credentials in the credential vault.") or [Dynatrace account data](/docs/manage/account-management "Manage your Dynatrace license, subscriptions, and platform adoption and environment health."), is stored in databases using logical data separation.

The application layer, in which the data is processed before it is stored at rest, is hosted on a highly scalable shared cloud infrastructure.

Separate storage space is currently available for Dynatrace SaaS on AWS and Azure. Support for Dynatrace SaaS on Google Cloud is planned.

![Data separation on the Dynatrace platform](https://dt-cdn.net/images/dynatrace-platform-data-separation-doc-2662-d52d653a45.png)

## Data encryption at rest

All Dynatrace SaaS monitoring data is encrypted at rest using AES-256. With the latest Dynatrace, all Dynatrace platform data, including data from Grail, AppEngine, and AutomationEngine, is stored in a separate, dedicated storage space. Each storage space is encrypted with a unique encryption key, which is rotated every 365 days. Dynatrace manages the encryption keys.

Separate data storage and unique encryption keys are currently available for Dynatrace SaaS on AWS and Azure. Support for Dynatrace SaaS on Google Cloud is planned.

![Dynatrace SaaS platform data encryption at rest](https://dt-cdn.net/images/dynatrace-platform-data-encryption-doc-2772-2da248ac18.png)

## Data encryption in transit

All data exchanged between OneAgent, ActiveGate, and Dynatrace Cluster is encrypted in transit. Data is serialized and deserialized using Google Protocol Buffers.

Dynatrace SaaS supports TLS 1.2 and TLS 1.3 (SSL Labs Grade A+).

![dynatrace-data-security-encryption-in-transit](https://dt-cdn.net/images/dynatrace-data-security-encryption-in-transit-2690-c09d771883.png)

## User authentication

You can manage your users by setting up [user groups and permissions](/docs/manage/identity-access-management/permission-management/role-based-permissions "Role-based permissions") and [SAML](/docs/manage/identity-access-management/user-and-group-management/access-saml "SAML").

![dynatrace-data-security-user-authentication](https://dt-cdn.net/images/dynatrace-data-security-user-authentication-2690-9a645c42f8.png)

## Integrity verification of Dynatrace components

Dynatrace components are signed using code signing certificates within the continuous delivery and integration (CI/CD) pipeline.

Code signing certificates are stored on hardware tokens with Extended Validation (EV) code signing certificates for Windows. Signature verification is performed automatically before an update or installation. When installing a component for the first time, signature verification must be conducted manually.

![dynatrace-data-security-integrity-verification](https://dt-cdn.net/images/dynatrace-data-security-integrity-verification-2905-53a43d8705.png)

## Business continuity and high-availability

Dynatrace SaaS uses a clustered architecture, multiple availability zones (data centers), and automatic fail-over mechanisms to ensure high availability ([99.5% availability SLAï»¿](https://www.dynatrace.com/company/trust-center/sla/saas/)).

![dynatrace-data-security-high-availability](https://dt-cdn.net/images/dynatrace-data-security-high-availability-2772-a154b24478.png)

## Data backups and disaster recovery

* **AWS:** Every 24 hours, Dynatrace SaaS on AWS performs data backups to a different AWS account in the same AWS region. The backup includes the data captured for at least the last 30 days. The maximum recovery point objective (RPO) for a full cluster is 24 hours. The recovery time objective (RTO) takes up to 24 hours, depending on the size of the cluster.
* **Azure:** Every 24 hours, Dynatrace SaaS on Azure performs data backups to a different Azure subscription in the same Azure region. The backup includes the data captured for at least the last 30 days. The maximum recovery point objective (RPO) for a full cluster is 24 hours. The recovery time objective (RTO) takes up to 24 hours, depending on the size of the cluster.
* **Google Cloud:** Every 24 hours, Dynatrace SaaS on Google Cloud performs data backups to a different Google Cloud project in the same Google Cloud region. The backup includes the data captured for at least the last 30 days. The maximum recovery point objective (RPO) for a full cluster is 24 hours. The recovery time objective (RTO) takes up to 24 hours, depending on the size of the cluster.

![dynatrace-data-security-backup](https://dt-cdn.net/images/dynatrace-data-security-backup-2690-e30ecd18aa.png)

## Infrastructure monitoring

A dedicated Dynatrace self-monitoring cluster monitors availability, performance, and security of all SaaS clusters. If a problem is detected, the Dynatrace ACE (Autonomous Cloud Enablement) team, which operates on a 24/7 basis, is notified immediately. Operational status and incidents are always available at [dynatrace.status.ioï»¿](https://dynatrace.status.io/).

![dynatrace-data-security-infrastructure-monitoring](https://dt-cdn.net/images/dynatrace-data-security-infrastructure-monitoring-2612-10a1faea42.png)

## Roll out of updates and hot fixes

Using a fully automated CI/CD pipeline, Dynatrace is able to roll out updates and hot fixes within a few hours. The Dynatrace architecture allows for zero-downtime upgrades of clusters.

New features are delivered every two weeks. Updates of Dynatrace ActiveGates and OneAgents can be performed automatically or manually.

![dynatrace-data-security-rollout-updates](https://dt-cdn.net/images/dynatrace-data-security-rollout-updates-2892-9efe1ac573.png)

## Audit logs

Dynatrace logs security-relevant events such as configuration changes and access to the environment. You can view these audit logs in [Dynatrace](/docs/manage/data-privacy-and-security/configuration/audit-logs-api "Learn how to manage audit logs using an API.") or download them for further use via the [GET audit log](/docs/dynatrace-api/environment-api/audit-logs/get-log "View full audit log via Dynatrace API.") API call.

![dynatrace-data-security-audit-logs](https://dt-cdn.net/images/dynatrace-data-security-audit-logs-2635-7349637e51.png)

## Data access for Dynatrace support

Access to Dynatrace SaaS environments is role-based. Role changes require justification and approval by the Dynatrace ACE (Autonomous Cloud Enablement) team. Access is restricted to the Dynatrace corporate network and requires multi-factor authentication when accessed remotely. Every access and all changes are [audit logged](/docs/manage/data-privacy-and-security/configuration/audit-logs-api "Learn how to manage audit logs using an API.") and fully accessible.

![dynatrace-data-security-data-access-support](https://dt-cdn.net/images/dynatrace-data-security-data-access-support-2791-ebcc4e889e.png)

## Dynatrace secret leak prevention

Dynatrace can detect and prevent the leakage of Dynatrace secrets in source code repositories on GitHub. These secrets may include platform or API tokens that were inadvertently pushed to a source code repository. If a secret leak is detected, we will reach out to you and aid with remediation measures.

For details on reporting a security issue, see [Report a security-related concern](/docs/manage/data-privacy-and-security/data-security/report-a-security-related-concern "Find out how to report vulnerabilities and whom to contact in case of security concerns.").

![dynatrace-data-security-secret-leak-prevention](https://dt-cdn.net/images/dynatrace-data-security-secret-leak-prevention-2575-f100e468bf.png)

## Compliance, certifications, and audits

Dynatrace undergoes annual, independent third-party audits and conducts penetration tests and red team assessments with independent security firms.

Having achieved several global and local certifications and accreditations demonstrates that we adhere to the most recognized international standards for security management.

Dynatrace also benefits from secure Amazon, Azure, and Google data centers that are certified for ISO 27001, PCI-DSS Level 1, and SOC 1/SSAE-16.

For the full list of certifications, see [Trust Centerï»¿](https://www.dynatrace.com/company/trust-center/).

## Runtime protection

Dynatrace SaaS is protected using [Dynatrace Application Securityï»¿](https://www.dynatrace.com/platform/application-security/).

Malicious activity is blocked using Dynatrace's [Runtime Application Protection](/docs/secure/application-security/application-protection "Set up and configure Dynatrace Runtime Application Protection to monitor attacks and attack-generated code-level vulnerabilities.") feature.

Third party and code level vulnerabilities are [detected in real time and automatically reported](/docs/secure/application-security/vulnerability-analytics "Monitor, visualize, analyze, and remediate third-party and code-level vulnerabilities, track the remediation progress, and create monitoring rules.") to the Dynatrace Security team.

![Data security Dynatrace protection](https://dt-cdn.net/images/data-security-dynatrace-protection-1915-5d93f4245d.png)


---


## Source: secure-development-controls.md


---
title: Secure development controls
source: https://www.dynatrace.com/docs/manage/data-privacy-and-security/data-security/secure-development-controls
scraped: 2026-02-18T05:53:10.011374
---

# Secure development controls

# Secure development controls

* Latest Dynatrace
* 4-min read
* Published Jun 04, 2020

This page is an overview of all security controls that are included in the Dynatrace Security Development Lifecycle (SDL). The following sections provide more detail about these controls and practices, which are enforced by Dynatrace across all business-critical product components.

![secure-development-controls-overview](https://dt-cdn.net/images/secure-development-controls-overview-3982-7ad21ab60f.png)

For more information about how Dynatrace secures customer data in production, see [Data security controls](/docs/manage/data-privacy-and-security/data-security/data-security-controls "Learn about data security and operational security controls.").

## Threat modeling

Security-critical application components require a threat model in the design phase. This threat model is created by product and security architects.

![Threat modeling](https://dt-cdn.net/images/threat-modeling-816b44cd90.svg)

## Evaluation of external services and libraries

Security audits are performed on all external third-party vendors and services before they're put to use by the security teams. All third-party libraries are evaluated for quality, performance, licensing, and vulnerabilities and require approval before being used.

![Evaluating external services and libraries](https://dt-cdn.net/images/evaluating-external-services-and-libraries-37cd7a926f.svg)

## Code reviews

Every code change is approved by a peer developer. Changes made to security-critical areas of the product have to be additionally approved by security personnel.

Changes made to the main code line require a pull request that passes through numerous automated tests, including a selected set of static code-analysis security tests.

![Code reviews](https://dt-cdn.net/images/code-reviews-44e39d181b.svg)

## Static code analysis

Static code analysis and static application security testing (SAST) are performed daily. Rules and plugins are actively maintained by the Dynatrace code quality team comprised of software engineers and security experts.

Plugins include pre-defined and self-developed detection rules for security vulnerabilities and bugs.

![Static code analysis](https://dt-cdn.net/images/static-code-analysis-f3bc613a7e.svg)

## Third-party library scans

Third-party libraries are centrally managed with a software composition analysis tool (SCA). Daily scans are performed, security vulnerabilities and license risks are detected, and remediation tickets are created.

![Third-party scans](https://dt-cdn.net/images/third-party-scans-27165fd909.svg)

## Automated security tests

Individual development teams implement automated security tests in the form of unit tests, integration tests, or UI tests that are executed automatically as part of the CI/CD pipeline.

![Security tests](https://dt-cdn.net/images/security-tests-7fbf27eb8b.svg)

## Code signing

Installer packages are automatically signed in the build pipeline using code signing certificates. Windows installers are signed with extended validation (EV) code-signing certificates.

Also, signature verification is performed automatically during installation and updates.

Plugins and extensions built by Dynatrace are signed, and the signature is validated when they're activated on hosts. Any change to their contents invalidates the signature and prevents activation.

![Code signing](https://dt-cdn.net/images/code-signing-d324fdc18a.svg)

## Penetration tests

Dynatrace has a dedicated team of certified penetration testers who regularly test new and existing features using state-of-the-art penetration-testing tools.

![Penetration testing](https://dt-cdn.net/images/penetration-testing-89250f38c6.svg)

## Intrusion detection and incident response

All critical systems are monitored by Dynatrace and intrusion-detection systems. Critical events trigger an incident response process.

![Intrusion detection and incident response](https://dt-cdn.net/images/intrusion-detection-and-incident-response-9847021c64.svg)

## Web-application scans

Weekly web-application vulnerability scans are performed as dynamic application security tests (DAST).

![Web scans](https://dt-cdn.net/images/web-scans-db5c35afb5.svg)

## Vulnerability scans

All public-facing and critical internal systems are scanned weekly using vulnerability-scanning tools.

![Vulnerability scan](https://dt-cdn.net/images/vulnerability-scan-f268ce5b9c.svg)

## Cloud security scans

All critical cloud accounts are regularly checked for security misconfigurations and non-compliant settings.

![Cloud scans](https://dt-cdn.net/images/cloud-scans-3cbd78a229.svg)

## External penetration testing

Annually, an extensive penetration test of all Dynatrace product components is performed by an independent security firm. Additional external penetration tests are scheduled on demand, the results of which are shared with our customers under a non-disclosure agreement (NDA).

![External penetration testing](https://dt-cdn.net/images/external-pen-testing-51ab8c744f.svg)

## Bug bounty program

Dynatrace runs a private [bug bounty program on HackerOneï»¿](https://www.dynatrace.com/news/blog/dynatrace-incorporates-hackerones-bug-bounty-program-into-their-security-playbook/).

![Bug bounty program](https://dt-cdn.net/images/bug-bounty-4eea6046c7.svg)

## Vulnerability tracking and KPIs

All security issues and vulnerabilities are tracked in a central ticketing system, which is also used for all other work-related tasks by other teams. The security teams categorize and rate all vulnerabilities using the Common Vulnerability Scoring System (CVSS). Remediation timelines for each vulnerability severity are defined and continuously monitored.

Central security dashboards and quarterly reports are made available to all teams. For identified hotspots, improvements are planned and implemented.

![Vulnerability tracking and KPIs](https://dt-cdn.net/images/vulnerability-tracking-f59e2fbfc3.svg)

## Security training and onboarding programs

All Dynatrace employees are expected to attend and successfully complete annual security awareness programs, which cover our corporate and product security policies.

For new employees, the annual security awareness program and additional product security training are part of the onboarding program.

![Security training](https://dt-cdn.net/images/security-training-8b0ececa60.svg)


---
