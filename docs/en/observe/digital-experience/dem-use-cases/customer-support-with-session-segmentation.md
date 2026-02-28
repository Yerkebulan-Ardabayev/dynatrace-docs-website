---
title: Effective customer support with session segmentation
source: https://www.dynatrace.com/docs/observe/digital-experience/dem-use-cases/customer-support-with-session-segmentation
scraped: 2026-02-28T21:12:05.613892
---

# Effective customer support with session segmentation

# Effective customer support with session segmentation

* Tutorial
* 8-min read
* Published Oct 03, 2023

Your customer support department probably receives thousands of support tickets every year, maybe every month. Some of these tickets require detailed insights into the customer's workflow to determine where the problem occurred and solve the case. Drilling into customer issuesâsuch as slowly loading webpages, unresponsive UI, or various request and JavaScript errorsâis cumbersome and takes a long time to resolve, especially when the information is missing.

Thanks to [session segmentation](/docs/observe/digital-experience/session-segmentation "Learn how to use Real User Monitoring to analyze user sessions across your applications."), however, getting your customers out of trouble is easier and quicker.

With session segmentationâalso known as user session analysisâyou get full visibility into how your users experience every digital transaction across web, mobile, and custom applications. You can categorize your application's user sessions into meaningful groups based on shared characteristics, such as an operating system, browser type, or location.You can also find specific users and sessions via advanced filtering attributes, which is very beneficial for resolving customer support requests.

Session segmentation enables your customer support to:

* Reduce the resolution time of customer support tickets.
* Save your time and your customers' time.
* Experience an easier troubleshooting process.
* Prevent customer frustration and improve your customer satisfaction rating.

## Scenario

Let's see how your customer support experts can leverage session segmentation when working on support tickets and resolving customer complaints.

For this use case, imagine that your customer, Daniel Adams, creates a support ticket stating that your website is very slow and that there was some kind of an error. He has neither mentioned the exact page nor provided details on the error.

The sections below explain how to find a specific customer's session, study its details, and get even more insights via waterfall analysis and distributed traces.

![Effective customer support with session segmentation](https://dt-cdn.net/images/effective-customer-support-with-session-segmentation-2500-c91eb011c1.png)

## Find the problematic session

After receiving customer feedback, the first important step is to check the problematic [user session](/docs/observe/digital-experience/rum-concepts/user-session "Learn how a user session is defined, when a user session starts or ends, how user session duration is calculated, and more.") to understand what went wrong. If you've leveraged [user tagging](/docs/observe/digital-experience/rum-concepts/user-and-error-events#user-tagging "Learn about user and error events and the types of user and error events captured by Dynatrace."), it's very easy to find the session of the person who submitted a support ticket. With user tags, which are comprised of a username, nickname, or email, you can analyze a specific user's behavior and experience via [user session analysis](/docs/observe/digital-experience/session-segmentation/new-user-sessions "Learn about user session segmentation and filtering attributes.").

To view problematic user sessions of a particular user

1. In Dynatrace, go to ![Session Segmentation](https://dt-cdn.net/images/session-segmentation-512-5278e8fa16.png "Session Segmentation") **Session Segmentation**.
2. Use the [timeframe selector](/docs/analyze-explore-automate/dashboards-classic/dashboards/dashboard-timeframe "Learn about Dynatrace dashboard timeframe and management zone settings.") in the upper-right corner of the page to set the analysis timeframe to the date and time when the issue occurred.
3. Select the **Filter by** box at the top of the page, and set the following [filtering attributes](/docs/observe/digital-experience/session-segmentation/new-user-sessions#session-segmentation-filters "Learn about user session segmentation and filtering attributes."). Once you select an attribute, the possible values for that attribute are displayed.

   * **Application**: **<your application name>**
   * **User tag**: **<tag of the user who reported the issue>**
   * **User experience score**: **Frustrating** if the user complained of a slow UI
   * **Has errors**: **Yes** if the user reported an error

   The list of user sessions updates to show the sessions that match the filtering attributes that you've set.
4. Select a timestamp of the required user session to navigate to the session details page.

In the example below, you can see a session entry for Daniel Adams. The session started at 15:13 on September 27, 2023, lasted for 25 seconds, and contained one error.

![Session list with a filtered out session](https://dt-cdn.net/images/session-list-3468-904af7eb49.png)

## Explore the session details

The session details page provides valuable information on the user session, for example, the session start time, duration, and [user experience score](/docs/observe/digital-experience/rum-concepts/scores-and-ratings/user-experience-score "User experience score is a metric used to categorize user sessions as Frustrating, Tolerable, or Satisfying."). On this page, you can also find important device-related information such as the screen resolution, browser, operating system, IP address, and more.

![Session details - overview](https://dt-cdn.net/images/session-details-overview-2572-a75b75baba.png)

* Under **Analysis**, check the user session timeline. Errors and annoyances are marked with red color.

  ![Session details - timeline](https://dt-cdn.net/images/session-details-timeline-2572-cb5979cee6.png)
* Scroll down to the **Events and actions** section to see what [actions](/docs/observe/digital-experience/rum-concepts/user-actions "Learn what user actions are and how they help you understand what users do with your application.") the user performed and what [user and error events](/docs/observe/digital-experience/rum-concepts/user-and-error-events "Learn about user and error events and the types of user and error events captured by Dynatrace.") happened during the session.

  ![Session details - events and actions](https://dt-cdn.net/images/session-details-events-and-actions-2572-53614392e0.png)
* Filter actions and events by action type, [Apdex rating](/docs/observe/digital-experience/rum-concepts/scores-and-ratings/apdex-ratings "Learn how Dynatrace uses Apdex to measure user satisfaction with application performance."), [error type](/docs/observe/digital-experience/rum-concepts/user-and-error-events#error "Learn about user and error events and the types of user and error events captured by Dynatrace."), or even [conversion goal](/docs/observe/digital-experience/web-applications/analyze-and-use/define-conversion-goals "Learn how to analyze conversion goals for specific user actions to understand how successfully you're meeting your conversion milestones.").

  ![Session details - filter by different parameters](https://dt-cdn.net/images/session-details-filter-by-2572-c48481918a.png)
* **Expand** ![Expand row](https://dt-cdn.net/images/expand-row-icon-9c4950fc2e.svg "Expand row") the required action or event to view more details.

  In our example, you can see that a request error happened during the `loading of page /cart/checkout` [load action](/docs/observe/digital-experience/rum-concepts/user-actions#load-action "Learn what user actions are and how they help you understand what users do with your application."), and the Apdex rating for this action is **Frustrating**.

  ![Session details - action details](https://dt-cdn.net/images/session-details-action-details-separated-2572-e1bd2d75c9.png)

## Watch the session recording

A [Session Replay](/docs/observe/digital-experience/session-replay "Learn how you can use Session Replay to better understand and troubleshoot errors experienced by your customers.") recording, if available for a user session, offers an enhanced level of insight into your user's journey. Session Replay can capture and visually replay each click or tap made within your application, creating an immersive movie-like experience. This feature helps to resolve customer complaints, reproduce production issues, improve overall usability, or fix application bugs.

To watch a session recording

1. On the session details page, in the **Analysis** section, go to the **Session Replay** tab.
2. Select **Play** ![Replay](https://dt-cdn.net/images/replay-button-optimized-41ad05863e.svg "Replay"), and watch the recording of the user session.
3. Use the Session Replay controls to carefully examine the actions that the user performed in your application. Note that the errors are represented by red dots in the timeline.

![Session details - session replay](https://dt-cdn.net/images/session-details-session-replay-3468-f6b7e8e699.png)

## Check request waterfall graphs

After watching the session recording, let's investigate the issue further using waterfall analysis and identify a specific request to blame.

[Waterfall analysis](/docs/observe/digital-experience/web-applications/analyze-and-use/waterfall-analysis "Learn how to analyze all user action monitoring data through waterfall analysis.") proves to be invaluable in analyzing the performance of a user action and getting detailed information about various requests that comprise a user action. Waterfall graphs come in handy when you want to find a specific request that is responsible for failures or performance violations, while [top findings](/docs/observe/digital-experience/web-applications/analyze-and-use/waterfall-analysis#top-findings "Learn how to analyze all user action monitoring data through waterfall analysis.") streamline the captured data into easily understandable and actionable information, simplifying the troubleshooting process.

To view waterfall graphs for a user action

1. On the session details page, under **Events and actions**, find and expand the action that caused the trouble. Such an action is marked with a red line, and its Apdex rating is usually **Frustrating**.
2. In the lower-right corner of the action details, select **Perform waterfall analysis** to navigate to the action waterfall graphs.
3. On the action waterfall analysis page, study the available information.

   ![Waterfall analysis](https://dt-cdn.net/images/waterfall-analysis-3468-32efcffec9.png)

   * Hover over the requests that happened during the action and check various [user action metrics](/docs/observe/digital-experience/rum-concepts/user-action-metrics "Learn what metrics Dynatrace calculates for user actions and find out what each metric indicates.").
   * Select **Show all findings** to view and analyze all of them at once.
   * Select each finding to get additional information on it. When you select a finding, the associated requests and resources are highlighted in the waterfall.
4. Select the **# Error** finding. The associated erroneous requests and resources are highlighted in the waterfall.

In our example, we've selected the **1 Error** finding and learned that the `/checkout` request failed with the `HTTP 500` error.

![Waterfall analysis - failed request](https://dt-cdn.net/images/waterfall-analysis-failed-request-3468-c8adab59ed.png)

## Explore distributed traces

After you've grasped the summary of the situation from the **Waterfall analysis** view, it's time to drill down to code-level information. Let's view the distributed traces of the failed request to investigate the timing, code-level context, and downstream call details.

[PurePathÂ® technology](/docs/observe/application-observability/distributed-traces "Gain observability into highly distributed, cloud-native architectures to effectively trace and analyze transactions in real time.") traces each web request through your application infrastructure, offering valuable insights into performance factors at the application level. For instance, if you see that one or two requests are consuming most of the action time, you can drill into the distributed trace to discern whether the issue stems from an abundance of database requests or a single slow one. With this data, you can enhance the application performance or conduct in-depth error analysis to optimize your system.

To view distributed traces of a request

1. On the action waterfall analysis page, select the failed request, which is in red, and check the available details.
2. Select **View trace** to navigate to the distributed traces page for that request.
3. In the distributed traces list view, select a resource or request and drill down to the [available details](/docs/observe/application-observability/distributed-traces/use-cases/segment-request#pp-analysis "Enhance your distributed system performance by segmenting requests with slow response time via Service flow and analyzing their distributed traces.").

![Distributed traces for the checkout request](https://dt-cdn.net/images/distributed-traces-3468-4f297a5b46.png)

On the distributed traces page, you can check the response time, processing time, execution breakdown, and [request attributes](/docs/observe/application-observability/services/request-attributes "Understand what request attributes are and learn how to use them across all levels of all service-analysis views."). When required, you can study the trace logs, view the failure details, or navigate to the [**Service flow**](/docs/observe/application-observability/services-classic/service-flow "Find out how Dynatrace can help you trace the sequence of service calls that are triggered by each service request in your environment.") or [**Service backtrace**](/docs/observe/application-observability/services-classic/service-backtrace "Trace the sequence of service calls all the way back up to the browser click that triggered the sequence of calls.") view.

By checking the **Logs** and **Errors** tabs on the distributed traces page, we've finally found out that there was an issue with Daniel Adams's credit card: its details were invalid.

```
failed to charge card: could not charge the card: rpc error: code = Code(400) desc = Credit card info is invalid
```

![Distributed traces - error details](https://dt-cdn.net/images/error-details-2358-41cc3abebe.png)

## Resolve the issue

Now that you know the whole storyâwhat, when, and whereâit's time to eliminate a problem that might have caused your client frustration. Whether it's a broken HTML tag, an outdated JavaScript code, or a user interface issue, your development team now knows where to start.

## Related topics

* [New: User session analysis](/docs/observe/digital-experience/session-segmentation/new-user-sessions "Learn about user session segmentation and filtering attributes.")
* [Session Replay](/docs/observe/digital-experience/session-replay "Learn how you can use Session Replay to better understand and troubleshoot errors experienced by your customers.")
* [Waterfall analysis](/docs/observe/digital-experience/web-applications/analyze-and-use/waterfall-analysis "Learn how to analyze all user action monitoring data through waterfall analysis.")
* [Distributed Traces Classic](/docs/observe/application-observability/distributed-traces "Gain observability into highly distributed, cloud-native architectures to effectively trace and analyze transactions in real time.")