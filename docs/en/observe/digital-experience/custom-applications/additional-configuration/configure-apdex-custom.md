---
title: Adjust Apdex settings for custom applications
source: https://www.dynatrace.com/docs/observe/digital-experience/custom-applications/additional-configuration/configure-apdex-custom
scraped: 2026-02-24T21:28:44.399617
---

# Adjust Apdex settings for custom applications

# Adjust Apdex settings for custom applications

* How-to guide
* 1-min read
* Published Jan 30, 2023

[Apdex](/docs/observe/digital-experience/rum-concepts/scores-and-ratings/apdex-ratings "Learn how Dynatrace uses Apdex to measure user satisfaction with application performance.") is an important score that measures your application performance. You can adjust the Apdex thresholds (Satisfactory, Tolerable, and Frustrating) for your application and for its [key user actions](/docs/observe/digital-experience/rum-concepts/user-actions#key-user-actions "Learn what user actions are and how they help you understand what users do with your application.") to refine the Apdex calculations.

## Configure Apdex settings for your application

1. Go to **Frontend**.
2. Select the application that you want to configure.
3. Select **More** (**â¦**) > **Edit** in the upper-right corner of the tile with your application name.
4. From the application settings, select **General** > **Key performance metrics**.
5. Use the sliders to set the user-satisfaction performance thresholds (Satisfactory, Tolerable, and Frustrating) for the **User action duration** metric.
6. Optional Turn on **Consider reported errors / web request errors in Apdex calculations** to rate user actions with reported errors or web request errors as Frustrating.

## Configure Apdex thresholds for key user actions

To change the Apdex thresholds for a key user action

1. Go to **Frontend**.
2. Select the application and scroll down to **Top 3 user actions** or **Top 3 actions**.
3. Select **View full details** or **Analyze performance**.
4. Search for the required key user action and select it.  
   The user action detail page opens.
5. In the upper-right corner of the user action detail page, do one of the following:

   * For web applications, select **More** (**â¦**) > **Edit** > **Key performance metric**.
   * For mobile and custom applications, select ![Expand](https://dt-cdn.net/images/expandbutton-40-e1f11ff81d.png "Expand") (**Expand**) > **Edit** > **Key performance metric**.
6. Use the slider to adjust the Apdex thresholds.

## Related topics

* [Apdex ratings](/docs/observe/digital-experience/rum-concepts/scores-and-ratings/apdex-ratings "Learn how Dynatrace uses Apdex to measure user satisfaction with application performance.")
* [Context-based Apdex analysis](/docs/observe/digital-experience/session-segmentation/apdex-analysis "Check Apdex rating for a user action, location, and application.")