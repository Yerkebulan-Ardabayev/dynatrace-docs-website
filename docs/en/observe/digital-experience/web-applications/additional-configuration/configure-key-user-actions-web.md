---
title: Configure key user actions for web applications
source: https://www.dynatrace.com/docs/observe/digital-experience/web-applications/additional-configuration/configure-key-user-actions-web
scraped: 2026-03-06T21:27:50.224051
---

# Configure key user actions for web applications


* Classic
* How-to guide
* 1-min read
* Published Jan 27, 2023

Most applications include user actions that are particularly important to the success of your digital business. Examples of these actions are signups, checkouts, and product searches. Such [key user actions](../../rum-concepts/user-actions.md#key-user-actions "Learn what user actions are and how they help you understand what users do with your application.") might take longer to execute than others, or they might have the requirement to be of a shorter-than-average duration.

With the key user action feature, you can [customize the Apdex thresholds](../../rum-concepts/scores-and-ratings/apdex-ratings.md#key-user-actions "Learn how Dynatrace uses Apdex to measure user satisfaction with application performance.") for each of these user actions. You can use this feature to monitor key actions with a dedicated dashboard tile and track historical trends.

## Mark a user action as a key user action

1. Go to **Frontend**.
2. Select the application and scroll down to **Top 3 user actions** or **Top 3 actions**.
3. Select **View full details** or **Analyze performance**.
4. Scroll down to see the list of user actions, and select the required user action.  
   The user action detail page opens.
5. In the upper-right corner of the user action detail page, select **Mark as key user action**.

You can define up to 500 key user actions per environment across all your applications and up to 100 key user actions per application.

When you reach the maximum key user action limit, consider using calculated metrics (available for your web, mobile, and custom applications), which offer similar capabilities.

## Pin a key user action to dashboard

Dashboards Classic

1. Go to **Frontend**.
2. Select the application and scroll down to **Top 3 user actions** or **Top 3 actions**.
3. Select **View full details** or **Analyze performance**.
4. Search for the required key user action and select it.  
   The user action detail page opens.
5. In the upper part of the user action detail page, select **Pin to dashboard**. For details, see Pin tiles to your dashboard.

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

* User actions