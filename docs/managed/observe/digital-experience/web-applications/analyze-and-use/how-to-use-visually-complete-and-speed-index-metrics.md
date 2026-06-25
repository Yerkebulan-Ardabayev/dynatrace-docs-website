---
title: Use 'Visually complete' and 'Speed index' metrics
source: https://docs.dynatrace.com/managed/observe/digital-experience/web-applications/analyze-and-use/how-to-use-visually-complete-and-speed-index-metrics
scraped: 2026-05-12T11:34:40.134634
---

# Use 'Visually complete' and 'Speed index' metrics

# Use 'Visually complete' and 'Speed index' metrics

* How-to guide
* 9-min read
* Published Jul 03, 2018

To help you gain greater visibility into the user experience of your application, we've [introduced a new, enhanced version of the Visually complete algorithmï»¿](https://www.dynatrace.com/news/blog/more-visibility-into-user-experience-with-new-web-performance-metrics-and-enhanced-visually-complete/) that gives you better control over your Visually complete calculations. Combined with additional performance metrics, the enhanced version of Visually complete gives you accurate, stable measurements and better control over what's included in Visually complete calculations. To migrate to the new version globally across your environment, go to **Web** and select any application from the list. Then scroll down to **Enable Visually complete 2.0 and new web performance metrics** and select **Enable for all applications**.

Support for the earlier version of Visually complete will end with RUM JavaScript version 1.211 for RUM and Synthetic version 1.212.

Visually complete is a point-in-time metric that measures when the visual area of a page has finished loading. Visually complete metrics are typically shorter in duration than comparable metrics (for example, page load time and DOM interactive measures) because users perceive complete page load before 100% of background page elements have loaded. Optimizing visually complete timing is more valuable than optimizing other page load timings in terms of user experience as it reflects the amount of time that your real users spend waiting for above-the-fold content to load completely. Results are sortable based on location, device, operating system, and browser type.

Visually complete means that all elements within the visible area of a web page are 100% loaded:

* Elements
* Images
* IFrames (only images)

The visible area extends from the top of the page to the bottom of the browser window (user scrolling doesn't affect the page area used for measurement).

Visually complete has the following benefits:

* Lets you see exactly how long it takes your end users to see the information they're looking for.
* Provides a true business-relevant metric from the perspective of the user.
* Gives 100% visibility into actual real user experience, regardless of device.
* Aligns IT and business in connecting user experience with business outcomes.
* Accelerates performance improvements.
* Optimizes decisions across development, operations, and user experience.
* Can be combined with powerful waterfall charts for understanding and improving page rendering times.

Along with Speed index, Visually complete shows the total time taken by an entire page to load. Therefore, these metrics are collected only for main frames, not subframes. In cases where the frames are cross origin, and there is no way of knowing the parent frame, collection of Speed index and Visually complete is attempted for sub frames too.

## Visually complete calculation

#### Visually complete calculation for load actions

Visually complete starts observing DOM content once the RUM JavaScript is injected.

Observation stops when the Load event end is triggered and the last added element of the page is more than one second in the past. If there are recurrent changes on the page, Visually complete automatically times out 3 seconds after the Load event end triggers. All elements that are part of the page at the time Visually complete stops observing the page are used for the calculation.

Visually complete checks if the elements added to a page are visible or within the visible area. If they are, then the time when the last visible element appears on the page is used for Visually complete. For external resources like images, visually complete uses the resource timings API of the browser to get the loading times, and not the time when the `<img>` tag is placed on the page.

#### Visually complete calculation for XHR actions

For XHR actions, the observation of the DOM content starts at the `callback begin` of the XHR action and ends 50 milliseconds after the `callback end`. Any mutations with external resources such as images, stylesheets or IFrames, cause the RUM JavaScript to add a load listener to these resources. This extends the XHR action time to the last resource added within the observed timeframe.

Visually complete is then calculated for these resources. Visually complete can differ from the action end time. But when Visually complete is set to `-1` (default value), such as when no visible resources are added to the DOM, the action end time is used for Visually complete.

The reason why only resources and not all elements are supported for XHR actions is because if there are parallel XHR actions and multiple observations at the same time, the elements appearing on the page canât be correlated to the right action.

## Speed index calculation

Speed index is useful for comparing the user experience of various pages. The lower the number, the better the user experience of the page. See the [WebPagetest documentation pageï»¿](https://dt-url.net/gl03s4g) for a detailed definition of Speed index and a basic description of the Speed index calculation.

The solution within the RUM JavaScript uses the same algorithm as WebPageTest, but it uses the visible elements that are captured from visually complete. These are the "real" page elements. The advantage to screenshot comparison (webpagetest.org) is that Visually complete is aware of the elements on the page and their timings. Screenshot comparison only reflects the visual changes of a page. So, if for example there were a rotating GIF that changes continuously, the Visually complete and Speed index times of webpagetest.org would be inaccurate.

Speed index calculates an index by measuring the progress of the loading of a web page between certain markers, along with the percentage of elements that remain unloaded at a given point in time.

* (200 ms Ã 100%) (nothing is loaded up to 200 ms)
* (200 ms Ã 60%) (already 40% are loaded by the first marker; that is 60% must be loaded to reach 100%)
* (200 ms Ã 40%) (40% must be loaded to reach 100%)
* Speed index = (200 ms Ã 100%) + (200 ms Ã 60%) + (200 ms Ã 40%) = 400

Speed index is only applicable for load actions because it uses the whole page as a reference for calculating the index. For example, if there is a small icon on a page that takes five seconds to load, but the rest of the page is loaded within two seconds, then Visually complete will be five seconds because the icon is the last element on the page. But the Speed index would be near two seconds because the main part of the page loaded within two seconds.

## Configuration settings for enhanced Visually complete

In Dynatrace versions 1.194 and later, the new Visually complete algorithm gives you more control over how the metric is calculated by allowing you to specify the following settings:

* **Threshold**: Use this setting to define the minimum visible area per element (in pixels) for an element to be counted towards Visually complete and Speed index. This means that only elements that have the minimum defined pixel area will be included in the calculations. Use the `vct` property to define the threshold.
* **Inactivity timeout for load actions**: The time the Visually complete module waits for inactivity and no further mutations on the page after the load action. Use the `vcit` property to define the inactivity timeout.
* **Mutation timeout for XHR and custom actions**: The time the Visually complete module waits after an XHR or custom action closes to start the calculation. Use the `vcx` property to define the mutation timeout.
* **Excluded URL list**: Use regular expressions to define URLs for images and iFrames to exclude from detection by the Visually complete module. Use the `iub` property to create the list.
* **Ignored mutation list**: Query CSS selectors to specify mutation nodes (elements that change) to ignore in Visually complete and Speed index calculation. Use the `mb` property to create the list.

To configure these settings

1. Go to **Web**.
2. Select the application that you want to configure.
3. In the upper-right corner of the application overview page, select **More** (**â¦**) > **Edit**.
4. From the application settings, select **Capturing** > **Content capture**.
5. Add your desired setting.

   * `Threshold`:  
     Use a value from 0 to 10000; the default value is 50.
   * `Inactivity timeout for load actions`:  
     The time in millisecondsâ use a value from 0 to 30000; the default value is 1000.
   * `Mutation timeout for XHR and custom actions`:  
     The time in millisecondsâ use a value from 0 to 5000, the default value is 50.
   * `Excluded URL list`:  
     Use a pipe character as a separator between entries, such as `\.dynatrace\.com\/login|\.dynatrace\.com\/logout`. Separation between different protocols of the URLs is not supported; every protocol of the URL is excluded.
   * `Ignored mutation list`:  
     Use a comma character as a separator between entries, such as `#someDomElement@someattribute,.someOtherDomElement`.

### Adding Visually complete and other metrics to your dashboard

Visually complete and other calculated metrics for RUM can be used to create dashboards for the metrics that you are most interested in. You must [create a metric](/managed/observe/digital-experience/web-applications/additional-configuration/rum-calculated-metrics-web "Create calculated metrics as well as custom charts based on calculated metrics for your web applications.") before adding it to the dashboard. Besides our well-known Visually complete metric, here we've also added two of the three "web vitals," **First input delay (FID)** and **Largest contentful paint (LCP)**.

![Dashboard](https://dt-cdn.net/images/dashboard-1920-9461d373e4.png)

Dashboard

## Use Visually complete as a key performance metric

In Dynatrace versions 1.193 and earlier, Visually complete is a default [key performance metric](/managed/observe/digital-experience/web-applications/analyze-and-use/work-with-key-performance-metrics "Learn how to use the right key performance metrics to optimize user experience data for each of your applications.") that's applied for evaluating the performance of all load actions and XHR actions. Visually complete and Speed index timings are captured by default for all applications that have Real User Monitoring enabled.

You can change the key performance metric used for load actions and XHR actions. You can also disable capturing of Visually complete and Speed index timings, however re-enabling capture resets the anomaly detection reference periods defined for the application.

To set the key performance metric for an application

1. Go to **Web**.
2. Select the application that you want to configure.
3. In the upper-right corner of the application overview page, select **More** (**â¦**) > **Edit**.
4. Select **General settings** > **Load actions** / **XHR actions** /**Custom actions**.
5. Under **Key performance metric**, select the key performance metric from the list for each of the user action types.

To disable capturing Visually complete and Speed index timings

1. Go to **Web**.
2. Select the application that you want to configure.
3. In the upper-right corner of the application overview page, select **More** (**â¦**) > **Edit**.
4. From the application settings, select **Capturing** > **Content capture**.
5. Turn off the **Visually complete & Speed index** setting.

### Use Visually complete with single page applications

For single-page application frameworks like Angular, Visually complete gives even more accurate timings for user actions. With Visually complete, timings do not stop when XHR responses are returned. Because of this, you can get additional insight into dynamic resource loading that is triggered by JavaScript-based DOM element changes from the XHR call response.

### Correlate user performance with business metrics

Performance is one of the main drivers of user experience and successful business outcomes. The Visually complete metric provides this analysis out of the box.

### Visually complete for user action analysis

Visually complete and Speed index are captured for each step in a user action.

1. Go to **Web**.
2. Select the application to be analyzed.
3. Under **Performance analysis**, select the actions section to display user action data.
4. In the **Top 3 user actions** tile, select **View full details**.
5. Under **Key user actions** or **Top 100 user actions**, select an action to see its contribution timings and the step's action timeline on the **Contributors breakdown** tile. The action timeline shows timings for all the relevant action stages, including **Speed index** and **Visually complete.** The performance metric used for the step is displayed above the timeline, so you can quickly tell if "User action duration" or "Visually complete" is used as the performance metric.

![Visually complete in user action details](https://dt-cdn.net/images/visually-complete-enduser-analytics-2244-d801ca9488.png)

Visually complete in user action details

### Troubleshooting Visually complete and Speed index

When used as a key performance metric:

* Visually complete is calculated when a visual element on a page changes and the change is propagated with each subsequent load and XHR user action (but not asynchronous web requests that do not affect the DOM).
* Speed index is available only for load actions.

Check one of the following pages in the Dynatrace Community if you don't see accurate Visually complete or Speed index data.

* [Web applications: Visually complete and Speed index metrics not shownï»¿](https://dt-url.net/pw438xh)
* [Web applications: Inaccurate Visually complete and Speed index metricsï»¿](https://dt-url.net/jd638ur)

## Related topics

* [User actions](/managed/observe/digital-experience/rum-concepts/user-actions "Learn what user actions are and how they help you understand what users do with your application.")
* [Troubleshooting RUM for web applications](/managed/observe/digital-experience/web-applications/troubleshooting "Learn how to troubleshoot issues when you use Real User Monitoring for your web applications.")
* [Configure Real User Monitoring to capture XHR actions](/managed/observe/digital-experience/web-applications/initial-setup/configure-dynatrace-real-user-monitoring-to-capture-xhr-actions "Understand why you need to activate specific JavaScript frameworks for XHR-action support and learn how to configure Real User Monitoring for XHR actions.")