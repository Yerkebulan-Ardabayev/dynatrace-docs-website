---
title: Configure key user actions for mobile applications
source: https://www.dynatrace.com/docs/observe/digital-experience/mobile-applications/additional-configuration/configure-key-user-actions-mobile
scraped: 2026-03-01T21:22:24.244749
---

# Configure key user actions for mobile applications

# Configure key user actions for mobile applications

* How-to guide
* 1-min read
* Published Jan 30, 2023

Most applications include user actions that are particularly important to the success of your digital business. Examples of these actions are signups, checkouts, and product searches. Such [key user actions](/docs/observe/digital-experience/rum-concepts/user-actions#key-user-actions "Learn what user actions are and how they help you understand what users do with your application.") might take longer to execute than others, or they might have the requirement to be of a shorter-than-average duration.

With the key user action feature, you can [customize the Apdex thresholds](/docs/observe/digital-experience/rum-concepts/scores-and-ratings/apdex-ratings#key-user-actions "Learn how Dynatrace uses Apdex to measure user satisfaction with application performance.") for each of these user actions. You can use this feature to monitor key actions with a dedicated dashboard tile and track historical trends.

## Mark a user action as a key user action

1. Go to **Frontend**.
2. Select the application and scroll down to **Top 3 user actions** or **Top 3 actions**.
3. Select **View full details** or **Analyze performance**.
4. Scroll down to see the list of user actions, and select the required user action.  
   The user action detail page opens.
5. In the upper-right corner of the user action detail page, select **Mark as key user action**.

You can define up to 500 key user actions per environment across all your applications and up to 100 key user actions per application.

When you reach the maximum key user action limit, consider using calculated metrics (available for your [web](/docs/observe/digital-experience/web-applications/additional-configuration/rum-calculated-metrics-web "Create calculated metrics as well as custom charts based on calculated metrics for your web applications."), [mobile](/docs/observe/digital-experience/mobile-applications/additional-configuration/rum-calculated-metrics-mobile "Create calculated metrics as well as custom charts based on calculated metrics for your mobile applications."), and [custom applications](/docs/observe/digital-experience/custom-applications/additional-configuration/rum-calculated-metrics-custom "Create calculated metrics as well as custom charts based on calculated metrics for your custom applications.")), which offer similar capabilities.

## Pin a key user action to dashboard

[Dashboards Classic](/docs/analyze-explore-automate/dashboards-classic "Learn how to create, manage, and use Dynatrace Dashboards Classic.")

1. Go to **Frontend**.
2. Select the application and scroll down to **Top 3 user actions** or **Top 3 actions**.
3. Select **View full details** or **Analyze performance**.
4. Search for the required key user action and select it.  
   The user action detail page opens.
5. In the upper part of the user action detail page, select **Pin to dashboard**. For details, see [Pin tiles to your dashboard](/docs/analyze-explore-automate/dashboards-classic/charts-and-tiles/pin-tiles-to-your-dashboard "Learn to pin tiles to your dashboards.").

## Customize Apdex rating for a key user action

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

* [User actions](/docs/observe/digital-experience/rum-concepts/user-actions "Learn what user actions are and how they help you understand what users do with your application.")