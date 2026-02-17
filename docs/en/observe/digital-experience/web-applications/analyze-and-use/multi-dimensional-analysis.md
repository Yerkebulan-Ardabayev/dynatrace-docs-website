---
title: Multidimensional analysis for web applications
source: https://www.dynatrace.com/docs/observe/digital-experience/web-applications/analyze-and-use/multi-dimensional-analysis
scraped: 2026-02-17T04:49:55.810300
---

# Multidimensional analysis for web applications

# Multidimensional analysis for web applications

* How-to guide
* 8-min read
* Published Jun 28, 2019

Dynatrace Real User Monitoring enables you to dig deep into your [user actions](/docs/observe/digital-experience/rum-concepts/user-actions "Learn what user actions are and how they help you understand what users do with your application.") and perform analysis across numerous dimensions. Multidimensional **User action analysis** pages can be accessed from many entry points throughout Dynatrace. Depending on where you begin your analysis, pre-selected filters can be applied and carried forward as your analysis progresses.

Following are the main entry scenarios for making use of the latest multidimensional **User action analysis** views.

Scenario 1: Analysis based on user action type

Dynatrace differentiates between **Load actions**, **XHR actions**, and **Custom actions** (see below), enabling you to apply the ideal performance metrics for each action type. This provides for focused, in-context analysis of each user action type.

To access multidimensional analysis based on user action type

1. Go to **Web**.
2. Select the application you want to analyze.
3. In the **Impact of user actions on performance** section of the page, select **Analyze Performance** to open the **User action analysis** view.

   ![Multidimensional analysis](https://dt-cdn.net/images/application-overview-screen-key-performance-filter1-1066-39375d615b.png)

   The upper section of the multidimensional **User action analysis** page provides primary filtering options you can use to focus analysis on specific user action types.
4. From the filter lists at the top of the page, select relevant values for filtering based on **Action type**, **User type**, **Performance metric**, and **Contribution** (see image below).
5. Select a duration for the analysis timeframe from the **Analyze user actions during the pastâ¦** drop list.
6. Select the timeline chart to select the timeframe you want to analyze. The lower section of the view shows the more detailed, multi-dimensional user action analytics view with all the primary filters applied.

![Multi-dimensional analysis](https://dt-cdn.net/images/multi-dimensional-primary-grouping-filter-and-metric-selsection-1600-15378e6362.png)

7. Optional Select **Filtered by** to add additional filters. Filters are available for action duration, Apdex, JavaScript errors, user type, browser, location and more. Further down youâll see a list of all the **Key user actions** that meet your filter criteria, along with the **Top 100 user actions** (this list is initially based on total time consumed, but you can also filter based on JavaScript errors, action count, or duration.

![Multi-dimensional analysis](https://dt-cdn.net/images/multi-dimensional-analytics-screen-analytics-section1-870-aac5976141.png)

8. Select the user action you want to investigate more deeply. This takes you to the **User actions view** of the selected user action (Loading of page `/special-offers.jsp` in the example below). As you can see, the defined filters and analysis time frame are applied to the analysis on this page.

   ![Multi-dimensional analysis](https://dt-cdn.net/images/specific-user-action-with-filters-applied-from-multi-dimensional-user-action-analytics1-1600-e9ba1dc253.png)

   The applied filters and analysis timeframe are even carried over to the [**Waterfall analysis view**](/docs/observe/digital-experience/web-applications/analyze-and-use/waterfall-analysis "Learn how to analyze all user action monitoring data through waterfall analysis.") (see below).

   ![Multi-dimensional analysis](https://dt-cdn.net/images/specific-waterfall-for-user-action-with-filters-applied-from-multi-dimensional-user-action-analytics-screen3-1600-bc8c0f6bd6.png)

Scenario 2: Analysis based on browser type

Sometimes you need to figure out if users that share the same browser type are facing the same performance issues.

To access multidimensional analysis based on browser type

1. Go to **Web**.
2. Select the application you want to analyze.
3. Within the **Performance analysis** infographic, select the **Top browser** tile in the upper-left corner to display the **Browser breakdown** section.
4. Select **Analyze performance** at the bottom of the section.

   ![Multi-dimensional analysis](https://dt-cdn.net/images/1-application-overview-with-top-browser-insights-break-down-1600-f554e6b3c2.png)

   This takes you to the **Multidimensional analysis** view, where the analysis mode is set to **Browsers** (see below).
5. From the filter lists at the top of the page, select relevant values for filtering based on **Action type**, **User / browser type**, **Performance metric**, and **Contribution**.

   ![Multi-dimensional analysis](https://dt-cdn.net/images/browser-breakdown-entry-to-multi-dimensional-user-analytics-screen-1599-5e523dfa54.png)
6. Select a duration from the analysis time range drop list.
7. Select the timeline chart to select the timeframe you want to analyze. From here, you can pinpoint and analyze only those user actions you they relevant to your analysis.

Scenario 3: Analysis based on user type

Sometimes you want to learn more about the bots that crawl your website, perhaps because your company is working toward Search Engine Optimization (SEO), or you just want to see a âclean room requestâ made via Synthetic monitoring.

To access multidimensional analysis based on user type

1. Go to **Web**.
2. Select the application you want to analyze.
3. Within the **Performance analysis** infographic, select the **Top user type** tile in the upper-left corner to display the User type section.
4. Select the **Analyze performance** at the bottom of the section.

   ![Multi-dimensional analysis](https://dt-cdn.net/images/0-application-overview-with-user-type-break-down-1600-652da6c2f1.png)

   This takes you to multi-dimensional **User action analysis** view, which highlights the different user types that have performed the user actions under analysis. The **Analyze by** list in the **Multidimensional analysis** section is preset to **Browsers**.
5. From the filter lists at the top of the page, select relevant values for filtering based on **Action type**, **Performance metric**, and **Contribution**.

   ![Multi-dimensional analysis](https://dt-cdn.net/images/user-type-breakdown-entry-to-multi-dimensional-user-analytics-screen-1599-f2e40b76ae.png)
6. Select a duration from the analysis timeframe range drop list.
7. Select the timeline chart to select the timeframe you want to analyze. From here, you can pinpoint and analyze only those user actions that youâre most interested in.

Scenario 4: Analysis based on geolocation

In this scenario, the focus is on finding user actions from a specific geographic region. Letâs say youâve added a Content Delivery Network (CDN) for a certain region and want insights into how well the new CDN is working.

To access multidimensional analysis based on geolocation

1. Go to **Web**.
2. Select the application you want to analyze.
3. Within the **Performance analysis** infographic, select the **View geolocation breakdown** tile in the lower-left corner to display the **Geolocation breakdown** section.
4. Select **Analyze performance** at the bottom of the section.

   ![Multi-dimensional analysis](https://dt-cdn.net/images/2-application-overview-with-geo-location-break-down-1600-945b822f7e.png)

   This takes you to multidimensional **User action analysis** view, which now shows the top geolocations where your user actions originate from.
5. From the filter lists at the top of the page, select relevant values for filtering based on **Action type**, **User type**, **Performance metric**, and **Contribution**.

![Multi-dimensional analysis](https://dt-cdn.net/images/geo-location-breakdown-entry-to-multi-dimensional-user-analytics-screen-1599-7d2031e084.png)

6. Select a duration from the analysis time range drop list.
7. Select the timeline chart to select the timeframe you want to analyze. From here, you can pinpoint and analyze only those user actions that are relevant to your analysis.

Scenario 5: Analysis based on error type

![Multidimensional analysis](https://dt-cdn.net/images/multidimensional-analysis-5007-e664cf92d9.png)

For web applications, Dynatrace classifies [errors](/docs/observe/digital-experience/rum-concepts/user-and-error-events#error "Learn about user and error events and the types of user and error events captured by Dynatrace.") as **Request**, **Custom**, and **JavaScript** errors, allowing you to apply filters and analyze them categorically. You can therefore conduct a focused and contextual analysis of each type of error detected within a selected timeframe

To access multidimensional analysis based on errors

1. Go to **Web**.
2. Select the application you want to analyze.
3. In the **Performance analysis** infographic, select the **Errors by type** tile at the lower-left corner to view the top **Request**, **Custom**, and **JavaScript** errors.
4. Select **Analyze errors** to go to the **Multidimensional analysis: Errors** page.
5. Apply filters to view specific errors in the selected timeframe by selecting them from the following list boxes:

   * **Error type**: `Request`, `Custom`, and `JavaScript`
   * **Context**: `Errors during user actions` and `Errors between user actions`
   * **Origin**: `1st party errors`, `3rd party errors`, and `CDN errors`
6. Select **Show your errors** by `Type`, `Context`, or `Origin`.
7. Select a time duration from the analysis range list box.
8. Select the timeline chart to select the timeframe and slide along the timeline to select the range you want to analyze. From here, you can narrow down and analyze only the errors that are relevant to your analysis.
9. Optional Select the respective error type in the legend to hide or show the respective error type in the chart.

![Error analysis](https://dt-cdn.net/images/error-analysis-2757-13832acb4e.png)

After using the **Overview** to identify an accumulation of errors, you can also use the **Detail analysis** card for the selected timeframe to further analyze the errors.

1. Select one of the following dimensions by which you want to analyze the timeframe:

   * **Performance over time**
   * **Distribution**
   * **Browsers**
   * **Geolocation**
   * **Errors**
2. Select the option to group the errors by `Type`, `Context`, or `Origin`.
3. Optional Apply a filter by selecting the input field and choosing a desired filter. Use **Enter** and provide a corresponding filter value.

![Analysis by error type](https://dt-cdn.net/images/error-analysis-1873-78a0287859.png)

In this example, we find that we had an `HTTP 500` error on a booking API, which we now want to inspect. When you select this error, the error detail page displays the most basic information related to the error, such as:

* How often the error occurred
* The number of sessions and users that were impacted
* The elements, such as user actions, OS, browser types, and locations that were involved in the error

In the error detail card, you can find additional error information, such as whether the error was detected by the RUM JavaScript or by OneAgent. When you select **Edit detection rules for this error pattern**, you are directed to the page where you can edit the web request error pattern that detected the error. Alternatively, you can select **Create detection rule based on this error pattern** to create an explicit web request error rule for the detected request error.

![Error details](https://dt-cdn.net/images/error-details-5093-27df9761b5.png)

To further investigate the error you can conduct an in-depth session analysis of one of the affected sessions listed under **User sessions affected by the error** to find out more about where and how the error occurred. Features such as [Session Replay](/docs/observe/digital-experience/session-replay "Learn how you can use Session Replay to better understand and troubleshoot errors experienced by your customers.") make it easy to find and communicate the errors of these users throughout your organization.

![User details page](https://dt-cdn.net/images/user-sessions-to-user-details-page-1637-f01f4b8bf0.png)

![Session replay](https://dt-cdn.net/images/session-replay-1917-70e8439a06.png)

Another way to further investigate an error is to look at it from the user action perspective. Use a filter on a certain error found in the **Detail analysis** for the selected timeframe card to refine the errors of interest, and then scroll down to **Key user actions** or **Top 100 user actions** to find related user actions. Select a user action of interest, and select it to analyze individual user actions.

![Analyze errors by user action](https://dt-cdn.net/images/analyze-errors-by-user-action-2880-b1252314fe.png)

As as example, the following page shows that errors can be integrated into a waterfall analysis as either a bar or a marker at the time where an error occurs.

![Waterfall analysis](https://dt-cdn.net/images/waterfall-1863-b48855309b.png)