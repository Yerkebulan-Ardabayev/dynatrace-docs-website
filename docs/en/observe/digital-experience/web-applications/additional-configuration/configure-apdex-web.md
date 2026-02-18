---
title: Adjust Apdex settings for web applications
source: https://www.dynatrace.com/docs/observe/digital-experience/web-applications/additional-configuration/configure-apdex-web
scraped: 2026-02-18T05:57:46.904781
---

# Adjust Apdex settings for web applications

# Adjust Apdex settings for web applications

* How-to guide
* 1-min read
* Published Jan 27, 2023

[Apdex](/docs/observe/digital-experience/rum-concepts/scores-and-ratings/apdex-ratings "Learn how Dynatrace uses Apdex to measure user satisfaction with application performance.") is an important score that measures your application performance. You can adjust the Apdex thresholds (Satisfactory, Tolerable, and Frustrating) for your application and for its [key user actions](/docs/observe/digital-experience/rum-concepts/user-actions#key-user-actions "Learn what user actions are and how they help you understand what users do with your application.") to refine the Apdex calculations.

## Configure Apdex settings for your application

1. Go to **Web**.
2. Select the application that you want to configure.
3. In the upper-right corner of the application overview page, select **More** (**â¦**) > **Edit**.
4. Select **General settings** > **Load actions** / **XHR actions** /**Custom actions**.
5. Use the sliders under **Key performance metric thresholds** to select the values that determine a user action as **Satisfactory**, **Tolerable**, and **Frustrating**.
6. Under **Load actions** and **XHR actions**, use the dropdown list to select the key performance metric that should be used for Apdex calculation.

![Configure Apdex ratings](https://dt-cdn.net/images/web-apdex-configuration1-1402-98b17048e0.png)

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