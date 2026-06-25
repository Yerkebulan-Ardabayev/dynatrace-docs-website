---
title: Analyze web requests for mobile applications
source: https://docs.dynatrace.com/managed/observe/digital-experience/mobile-applications/analyze-and-use/analyze-web-requests-mobile
scraped: 2026-05-12T11:33:14.912222
---

# Analyze web requests for mobile applications

# Analyze web requests for mobile applications

* How-to guide
* 1-min read
* Published Jul 19, 2017

With Dynatrace client-side monitoring, you can assess the performance of first-party and third-party services in regard to availability, response time, and error occurrences.

To monitor your application's web requests

1. Go to **Frontend**.
2. Select the application that you want to analyze.
3. From the application overview page, select the **Web requests** tile.

The **Web requests** tile shows the overall number of web requests and the web request error rate for the selected timeframe.

![Web requests tile on the application overview page](https://dt-cdn.net/images/web-requests-tile-mobile-app-2-852-01bbe5846b.png)

Web requests tile on the application overview page

The information on the request rate, request duration, and top providers is available in the **Web requests** and **Top providers** sections.

## Web requests - Error rate

This chart compares the web request rateâthe number of web requests per minuteâto the [error](/managed/observe/digital-experience/rum-concepts/user-and-error-events#error "Learn about user and error events and the types of user and error events captured by Dynatrace.") rate for the selected timeframe.

![Web requests - Error rate tab](https://dt-cdn.net/images/web-requests-error-rate-790-fb758ee8a4.png)

Web requests - Error rate tab

## Web requests - Request time

This chart compares the web request rate to the request time for the selected timeframe.

![Web requests - Request time tab](https://dt-cdn.net/images/web-requests-request-time-790-aa8db1c006.png)

Web requests - Request time tab

## Top providers

This list includes the HTTP domains containing the largest number of outgoing requests triggered by your application for the selected timeframe.

![Top providers list](https://dt-cdn.net/images/top-providers-mobile-app-790-bb9125360d.png)

Top providers list

To view additional information on the provider, select it from the list. The provider details page opens where the data on the request rate, request time, and error rate for the selected provider is available.

* Go to the **Web requests** tab to explore the information on a particular web request, such as the request rate, duration, and size as well as error rate and some other details.
* Go to the **Errors** tab to view the list of web request errors for this provider. Select the error that you want to analyze to open the [web request error details page](/managed/observe/digital-experience/session-segmentation/new-user-sessions#error-details-page "Learn about user session segmentation and filtering attributes.").

![Provider details page opened on the Errors tab](https://dt-cdn.net/images/provider-detail-page-2131-734cbce65b.png)

Provider details page opened on the Errors tab