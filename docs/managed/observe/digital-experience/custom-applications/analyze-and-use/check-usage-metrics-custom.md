---
title: Check user experience metrics for custom applications
source: https://docs.dynatrace.com/managed/observe/digital-experience/custom-applications/analyze-and-use/check-usage-metrics-custom
scraped: 2026-05-12T11:33:57.307222
---

# Check user experience metrics for custom applications

# Check user experience metrics for custom applications

* How-to guide
* 1-min read
* Published Jan 30, 2023

Your application user experience metrics provide a quick overview of the number of users who are actively using your application during the selected timeframe.

To access the user experience metrics for your application

1. Go to **Frontend**.
2. Select the application that you want to analyze.
3. Examine the **User experience** tile, which is selected by default.

The **User experience** tile shows the total number of users, overall Apdex rating, and user action rate for the selected timeframe.

![User experience tile on the application overview page](https://dt-cdn.net/images/user-experience-tile-mobile-app-852-0baf6bdc02.png)

User experience tile on the application overview page

The detailed information on your application's Apdex rating trends, active users, new users, and application version distribution is available in the corresponding sections.

## Apdex rating

The **Apdex rating** chart shows your application's average [Apdex rating](/managed/observe/digital-experience/rum-concepts/scores-and-ratings/apdex-ratings "Learn how Dynatrace uses Apdex to measure user satisfaction with application performance.") trends for the selected timeframe.

![User experience section - Apdex rating](https://dt-cdn.net/images/user-experience-apdex-rating-847-ca725a074c.png)

User experience section - Apdex rating

## User actions and Users

The **User actions and Users** chart compares the number of user actions to active users for the selected timeframe.

![User experience section - User actions and Users](https://dt-cdn.net/images/user-experience-user-actions-and-users-848-27d7bac217.png)

User experience section - User actions and Users

## New users

The **New users** chart shows how many users launched your application for the first time during the selected timeframe. This metric only counts the first session following the launch of your instrumented application. Application updates and Dynatrace library updates don't trigger state resets for returning users. This metric is tied to specific devices, so users are counted multiple times if they install the application on multiple devices.

![User experience section - New users](https://dt-cdn.net/images/user-experience-new-users-2-848-df286583cc.png)

User experience section - New users

The **New users** metric doesn't distinguish between multiple users that share the same device and application installation.

## App version distribution

The **App version distribution** chart conveys the rate of version adoption by comparing the number of application sessions that originate from various application versions. This chart is particularly interesting following the release of new application versions, as it enables you to track adoption of the latest version.

![User experience section - App versions](https://dt-cdn.net/images/app-version-distribution-848-03883e6518.png)

User experience section - App versions

## Top 3 actions

The list displays the top three actions based on user action duration and user action rate.

![User experience section - Top 3 actions](https://dt-cdn.net/images/user-experience-top-3-actions-848-b804aa48cd.png)

User experience section - Top 3 actions

### User action overview page

From the **Top 3 actions** list on your application overview page, select a user action to open the user action overview page.

![User action overview page](https://dt-cdn.net/images/user-action-detail-page-2518-a51f30ad70.png)

User action overview page

On this page, you can mark the action as a key user action, perform a waterfall analysis, and view the action Apdex rating and performance.

You can also study the lists of reported errors and web request errors for the current action. Select the error you're interested in to open its [details page](#error-details-page).

### Multidimensional user action analysis

Under the **Top 3 actions** list on your application overview page, select **Analyze performance** to go to the multidimensional **User action analysis** page.

The multidimensional analysis enables you to dig deep into your user actions and view data across numerous dimensions. On the **User action analysis** page, you can create metrics, view your application's key user actions, and examine the top 100 user actions based on different criteria. You can also analyze your application by the operating system, geolocation, application version, and more.

### Web request errors and reported errors

From the multidimensional **User action analysis** page, you can also examine the list of web request errors or reported [errors](/managed/observe/digital-experience/rum-concepts/user-and-error-events#error "Learn about user and error events and the types of user and error events captured by Dynatrace."): Select **Web request errors over time** or **Reported errors over time** from the **Analyze by** text field. The list of errors shows up under the chart. Expand the error you're interested in and then select **Analyze error** to view the error details page.

![Analyze error from MDA section](https://dt-cdn.net/images/analyze-error-from-mda-2518-90cecae0cc.png)

Analyze error from MDA section

#### Error details page

The error details page provides valuable information about your application's errors.

Web request error details page

Reported error details page

![Web request error details page](https://dt-cdn.net/images/web-request-error-details-page-1772-928bb94d69.png)

Web request error details page

![Reported error details page](https://dt-cdn.net/images/reported-error-details-page-new-1644-60289f33a5.png)

Reported error details page

This displays error details such as the estimated error count, provider (for a request error), technology (for a reported error), and more. The page also lists affected user sessions and affected user actionsâselect a user action or user session to view its details. The distribution breakdown displays information on the relative frequencies of operating systems, OS versions, application versions, and devices, while the country breakdown shows all affected countries and their corresponding error rate.

For web request errors, you can also [configure error exclusion rules](/managed/observe/digital-experience/custom-applications/additional-configuration/web-request-errors-custom "Stop treating certain HTTP response codes as errors for your custom applications.") if you don't want Dynatrace to flag a particular HTTP status code as erroneous. Select **Edit error exclusion rules** to go to the corresponding settings page.

## Geographic regions

The **Geographic regions** world map, which is on your application overview page, visualizes all the geographic regions from which your users originate. For each country, you can view the number of active sessions, active users, and crashes, as well as the overall Apdex rating.

![User experience section - Geo regions](https://dt-cdn.net/images/user-experience-geo-regions-848-7ae15779b9.png)

User experience section - Geo regions

If you don't see data on the world map, you might need to [map your internal IP addresses to locations](/managed/observe/digital-experience/custom-applications/additional-configuration/map-internal-ip-addresses-to-locations-custom "Configure Dynatrace to use local addresses to understand where the users of your custom applications are.").