---
title: Context-based Apdex analysis
source: https://www.dynatrace.com/docs/observe/digital-experience/session-segmentation/apdex-analysis
scraped: 2026-02-24T21:30:31.776306
---

# Context-based Apdex analysis

# Context-based Apdex analysis

* How-to guide
* 2-min read
* Published Jan 27, 2023

Dynatrace makes it easy for you to analyze your application's [Apdex](/docs/observe/digital-experience/rum-concepts/scores-and-ratings/apdex-ratings "Learn how Dynatrace uses Apdex to measure user satisfaction with application performance.") from a variety of dimensions. You can check the Apdex rating for a particular user action, location, and application as well as view the Apdex rating for each user action within one user session.

## Location-based analysis

Leverage the **World map** view available for your [web](/docs/observe/digital-experience/web-applications/analyze-and-use/world-map-view "Learn how the World map view offers insights into Apdex ratings, user actions, action durations, and JavaScript errors."), [mobile](/docs/observe/digital-experience/mobile-applications/analyze-and-use/check-usage-metrics-mobile#geo-regions "Learn how to use Dynatrace to check the user experience metrics of your mobile application."), and [custom applications](/docs/observe/digital-experience/custom-applications/analyze-and-use/check-usage-metrics-custom#geo-regions "Learn how to use Dynatrace to check the user experience metrics of your custom application.") to see the color-coded Apdex scores and other performance information.

![Location-based analysis](https://dt-cdn.net/images/apdex-on-worldmap-1903-677a742e2e.png)

## User-action-based analysis

To analyze user satisfaction for a specific user action

1. Go to **Web**, **Mobile**, or **Custom Applications**.
2. Select the application and scroll down to **Top 3 user actions** or **Top 3 actions**.
3. Select **View full details** or **Analyze performance**.
4. Search for the required user action and select it.
   The user action detail page opens. The score is shown on the **Apdex rating** tile.

![User-action-based analysis](https://dt-cdn.net/images/apdex-on-user-action-1902-f7e7545781.png)

## Application-based analysis

To see how user satisfaction evolves over time for a specific application

* **Web applications**

  1. Go to **Web**.
  2. Select the **Apdex rating** tile on the infographic. You can also select **Analyze Apdex** to get even more details.

     ![Application-based analysis](https://dt-cdn.net/images/apdex-on-application-overview-1905-895ba0a0d2.png)
* **Mobile applications**

  The [**Apdex rating** chart](/docs/observe/digital-experience/mobile-applications/analyze-and-use/check-usage-metrics-mobile#apdex-rating "Learn how to use Dynatrace to check the user experience metrics of your mobile application.") is available on the application overview page.
* **Custom applications**

  Access the [**Apdex rating** chart](/docs/observe/digital-experience/custom-applications/analyze-and-use/check-usage-metrics-custom#apdex-rating "Learn how to use Dynatrace to check the user experience metrics of your custom application.") from the application overview page.

## Cross-application user journey analysis

To analyze and understand the areas of struggle for each user action in a user journey

1. On the application overview page, select **Analyze user sessions**, then select a user session.

![User journey analysis](https://dt-cdn.net/images/apdex-on-user-journey-1903-429abf6255.png)

## Apdex for business reporting

You can highlight Apdex as a core metric for your business peers by adding Apdex-related tiles to your Dynatrace dashboard.

![Apdex tiles on dashboard](https://dt-cdn.net/images/apdex-on-dashboards-1920-72e753ae39.png)

## Related topics

* [Apdex ratings](/docs/observe/digital-experience/rum-concepts/scores-and-ratings/apdex-ratings "Learn how Dynatrace uses Apdex to measure user satisfaction with application performance.")
* [Adjust Apdex settings for web applications](/docs/observe/digital-experience/web-applications/additional-configuration/configure-apdex-web "Configure the user-satisfaction performance thresholds for your web application and its key user actions.")
* [Adjust Apdex settings for mobile applications](/docs/observe/digital-experience/mobile-applications/additional-configuration/configure-apdex-mobile "Configure the user-satisfaction performance thresholds for your mobile application and its key user actions.")
* [Adjust Apdex settings for custom applications](/docs/observe/digital-experience/custom-applications/additional-configuration/configure-apdex-custom "Configure the user-satisfaction performance thresholds for your custom application and its key user actions.")