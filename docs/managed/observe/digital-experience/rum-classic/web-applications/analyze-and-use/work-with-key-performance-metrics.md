---
title: Work with key performance metrics in RUM Classic
source: https://docs.dynatrace.com/managed/observe/digital-experience/rum-classic/web-applications/analyze-and-use/work-with-key-performance-metrics
---

# Work with key performance metrics in RUM Classic

# Work with key performance metrics in RUM Classic

* How-to guide
* 3-min read
* Published Jun 05, 2019

Dynatrace offers an expanded selection of [key performance metrics](/managed/observe/digital-experience/rum-classic/rum-concepts/user-action-metrics#kpm "Learn what metrics Dynatrace calculates for user actions and find out what each metric indicates.") on which you can base your Real User Monitoring.

## Choose the right performance metric

For the correct monitoring analytics, it's important to choose the right performance metric for each application condition.

For many traditional web applications, **User action duration** is considered the best metric available for web performance optimization, as this metric focuses on the amount of time from user input to complete page load. But single page applications (SPAs) based on Angular, Ember, React, and other JavaScript frameworks don't depend on the loading of a new page followed by each click. So the race to be fast "above the fold" can lead to high overall user action duration times. As a result, other metrics such as **Visually complete** or **Speed index** can more accurately focus on the actual timings that reflect when the end user can take the next action. From the end user perspective, web applications can be usable after certain elements such as a date picker or autocomplete for a search field are ready to use.

Then there are applications where the UI is not as important as the interaction with the application. An example is a call center application or a documentation desk application where the users are experts and work with shortcuts. For such applications, the time to interact with the application is more important than ensuring that all images are loaded, so the **Long tasks** metric is important and **DOM interactive** may be the best metric to consider.

Choosing the right key performance metric also lets you adjust to varying performance levels of different application features. For example, a customer may be satisfied waiting five seconds after selecting **Confirm booking** but be frustrated waiting five seconds for a search field to appear.

With key performance metrics and [key user actions](/managed/observe/digital-experience/rum-classic/rum-concepts/user-actions#key-user-actions "Learn what user actions are and how they help you understand what users do with your application."), you can pick the ideal performance metric and expected performance goals that best fit each separate user action. Dynatrace key performance metrics enable you to respond to such variable conditions for each application and user action that you monitor.

## Use key performance metrics to monitor application performance

Key performance metrics are available by default, and **Visually complete** is selected as the key performance metric for load and XHR actions. **User action duration** is set as the default metric for custom actions. You can change the key performance metrics for each action type.

To select key performance metrics for your application

1. Go to **Web**.
2. Select the application that you want to configure.
3. In the upper-right corner of the application overview page, select **More** (**…**) > **Edit**.
4. Select **General settings** > **Load actions** / **XHR actions** /**Custom actions**.
5. Under **Key performance metric**, select the key performance metric that best represents the user experience for load and XHR user actions.

For situations where you want to tailor the key performance metric used for different application features, you can select a different key performance metric for your application's key user actions.

To select key performance metrics for key user actions

1. Go to **Web**.
2. Select the application you want to configure.
3. Under **Top 3 user actions**, select **View full details**.
4. Scroll down, and go to the **Key user actions** tab.
5. Select the desired key user action.
6. On the key user action details page, select **More** (**…**) > **Edit**.
7. Select the key performance metric that best represents the user experience for this key user action.

## See key performance metrics information

Several [dashboard tiles](/managed/analyze-explore-automate/dashboards-classic/charts-and-tiles/available-tiles "Find out how to configure your dashboard to track business-critical user-actions and conversion goals.") such as the **World map** and **Key user actions** are affected based on the selected key performance metrics. The metrics are also available for custom charting.

![Key performance metrics in dashboard tiles](https://dt-cdn.net/images/keyperformance-metric-dashboardtiles-1773-83fec3bb1d.png)

Key performance metrics in dashboard tiles

The application overview page shows **Visually complete** by default for load actions and XHR actions. **User action duration** is used for custom actions.

![Application overview showing key performance metric](https://dt-cdn.net/images/keyperformance-appoverview1-1516-cc5c2b0fbe.png)

Application overview showing key performance metric

The user action page, when **Speed index** is selected as the key performance metric, reflects the **Speed index** in all tiles and charts.

![Speed index used in user action - key performance metric](https://dt-cdn.net/images/keyperformance-metric-speedindexinuseraction-2174-fb7a7784f2.png)

Speed index used in user action - key performance metric