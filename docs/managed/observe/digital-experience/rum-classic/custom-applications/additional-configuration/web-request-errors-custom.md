---
title: Ignore web request errors for custom applications in RUM Classic
source: https://docs.dynatrace.com/managed/observe/digital-experience/rum-classic/custom-applications/additional-configuration/web-request-errors-custom
---

# Ignore web request errors for custom applications in RUM Classic

# Ignore web request errors for custom applications in RUM Classic

* How-to guide
* 1-min read
* Published Jan 30, 2023

By default, Dynatrace marks all `4xx` and `5xx` response status codes as web request [errors](/managed/observe/digital-experience/rum-classic/rum-concepts/user-and-error-events#error "Learn about user and error events and the types of user and error events captured by Dynatrace."). However, it's possible that some unsuccessful HTTP codes do not, in fact, indicate an issue with your application. For example, sometimes the `401 Unauthorized` status code simply shows that the user decided not to sign in. Another example is the `429 Too Many Requests` code, which can indicate throttling issues that are not caused by your application.

To ignore certain HTTP status codes, configure which status codes should not be marked as errors. When creating an exclusion rule, you can either add individual HTTP status codes, such as `401`, or status code ranges, such as `400-499`.

To create an exclusion rule

1. Go to **Frontend**.
2. Select the application that you want to configure.
3. Select **More** (**…**) > **Edit** in the upper-right corner of the tile with your application name.
4. From the application settings, select **Request errors**.
5. Select **Add exclusion rule**, and specify the HTTP status code or code range that should be treated as successful.

   ![Configure an exclusion rule](https://dt-cdn.net/images/mobile-exclusion-rules-2124-75133d34c8.png)

   Configure an exclusion rule

After setting up an exclusion rule, web requests with previously erroneous status codes will count as successful web requests against the error rate. This will affect your application Apdex rating, request error rate, and web request error list, as well as some user action and custom metrics.

For example, see the screenshots of the application overview page below and note the drop in the web request error rate. This happened after a rule was configured to ignore the `401 Unauthorized` response status code for this application. Also note the error rate decrease for the application top providers as well as the higher Apdex rating and lower error rate for one of the user actions.

#### Application overview page

Before

After

![Application overview page - before configuring exclusion rules](https://dt-cdn.net/images/app-overview-page-web-requests-before-2134-3ceead505c.png)

Application overview page - before configuring exclusion rules

![Application overview page - after configuring exclusion rules](https://dt-cdn.net/images/app-overview-page-web-requests-after-2134-0dc0ca7d48.png)

Application overview page - after configuring exclusion rules

#### Top providers list

Before

After

![Top providers - before configuring exclusion rules](https://dt-cdn.net/images/top-providers-before-2134-0f17ca6d01.png)

Top providers - before configuring exclusion rules

![Top providers - after configuring exclusion rules](https://dt-cdn.net/images/top-providers-after-2134-283506ceaf.png)

Top providers - after configuring exclusion rules

#### User action detail page

Before

After

![User action detail page - before configuring exclusion rules](https://dt-cdn.net/images/user-action-detail-page-before-2132-f989f87e3b.png)

User action detail page - before configuring exclusion rules

![User action detail page - after configuring exclusion rules](https://dt-cdn.net/images/user-action-detail-page-after-2132-8e9e2e559c.png)

User action detail page - after configuring exclusion rules