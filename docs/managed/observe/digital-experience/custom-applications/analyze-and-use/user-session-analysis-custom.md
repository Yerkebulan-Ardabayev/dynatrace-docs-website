---
title: Analyze user sessions of custom applications
source: https://docs.dynatrace.com/managed/observe/digital-experience/custom-applications/analyze-and-use/user-session-analysis-custom
scraped: 2026-05-12T11:33:41.440813
---

# Analyze user sessions of custom applications

# Analyze user sessions of custom applications

* How-to guide
* 1-min read
* Published Jan 30, 2023

Having an ability to view and analyze user sessions within your custom applications is imperative in today's digital consumer environment.

By default, user session analysis shows all of the user sessions in your environmentâacross web, mobile, and custom applications. To focus your analysis only on custom applications, you need to add one filters.

To view user sessions captured in custom applications

1. Go to **Session Segmentation**. The **User sessions** page opens.
2. In the **Filter by** box, select **Application type:** `Custom` to get user sessions captured in custom applications.
3. Optional To further focus your analysis, you can add more filters, such as operating system version, manufacturer, error count, and user experience score.
4. Select a timestamp of the required user session to navigate to the user session details page.

Dynatrace captures user sessions from custom applications as mobile user sessions. Built-in metrics are captured without the indication whether it's a mobile or a custom application. For more details, see [Built-in metrics](/managed/analyze-explore-automate/metrics-classic/built-in-metrics "Explore the complete list of built-in Dynatrace metrics.").

For further details, see [New: User session analysis](/managed/observe/digital-experience/session-segmentation/new-user-sessions "Learn about user session segmentation and filtering attributes.").

## Related topics

* [New: User session analysis](/managed/observe/digital-experience/session-segmentation/new-user-sessions "Learn about user session segmentation and filtering attributes.")