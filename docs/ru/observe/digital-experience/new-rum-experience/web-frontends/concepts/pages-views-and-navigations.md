---
title: Pages, views, and navigations in the New RUM Experience
source: https://www.dynatrace.com/docs/observe/digital-experience/new-rum-experience/web-frontends/concepts/pages-views-and-navigations
scraped: 2026-03-01T21:24:56.561467
---

# Pages, views, and navigations in the New RUM Experience

# Pages, views, and navigations in the New RUM Experience

* Latest Dynatrace
* Explanation
* Updated on Jan 08, 2026

The New RUM Experience uses the concepts of pages, views, and navigations to give you detailed visibility into your application's behavior and help you elevate performanceâwhether you're working with a traditional website or a Single Page Application (SPA).

## Pages

In the New RUM Experience, the concept of a page aligns with the browser's technical definition: It represents the document request, the displayed content, and all events that occur during its lifecycleâending with the next document request.

For a traditional website, pages let you analyze each full-page navigation. For an SPA, pages capture the initial load when the user first opens the application, while [views](#views) provide the complete picture as content changes dynamically.

### Pages and page instances

Each visit to a website generates a **page instance**. The data captured is aggregated into a [page summary event](/docs/semantic-dictionary/model/rum/user-events/navigation-related#page-summary), which is identifiable by its [`page.instance_id`](/docs/semantic-dictionary/model/rum/user-events#page-attributes "User events provide deep visibility and insights into experience, behavior, performance, and errors of your customers and end-users in real-time.").

**Pages** group all visits into one aggregated entry. To analyze the same page over all visits, page instances are grouped under `page.name`. The `page.name` attribute is designed to filter out dynamic URL parts for better grouping. It's derived from `page.detected_name`, which the RUM JavaScript bases on the URL.

The **page load** of each new page instance is captured as an event with the following three [characteristics](/docs/semantic-dictionary/model/rum/user-events#user-event-characteristics "User events provide deep visibility and insights into experience, behavior, performance, and errors of your customers and end-users in real-time."):

* `characteristics.has_request`
* `characteristics.has_navigation`
* `characteristics.has_w3c_navigation_timings`

### Google Web Vitals

[Google Web Vitalsï»¿](https://web.dev/articles/vitals) are critical for understanding the user experience on a page. These metrics are captured with every page summary event. For details, see [Web vitals attributes](/docs/semantic-dictionary/model/rum/user-events/navigation-related#page-summary-web-vitals-attributes) in the Semantic Dictionary. As Google's official Web Vitals specification is page-based, the built-in Web Vitals metrics in the New RUM Experience are based on the values in page summaries, even though Web Vitals are also captured in [view summary events](#views).

Built-in metrics for Web Vitals

### Example DQL query

The following DQL query retrieves the 75th percentile for the Largest Contentful Paint (LCP) Web Vital by page.

```
fetch user.events



| filter characteristics.has_page_summary



| filter isNotNull(web_vitals.largest_contentful_paint)



| summarize {



percentile(web_vitals.largest_contentful_paint, 75)



}, alias:page_LCP, by:{ page.name }



| sort page_LCP desc
```

## Views

On a traditional website, every navigation triggers a full-page load, which makes it straightforward to track individual pages and their Web Vitals, providing the data needed to optimize the site. SPAs, however, work differently. They typically involve a single initial page load and then update content dynamically without reloading the entire page. This requires a different approach to segmenting and aggregating data to optimize specific parts of the application.

The New RUM Experience automatically interprets soft navigations (also called route changes) as changes to a new view. A view refers to the content displayed and all events occurring between two navigations. This concept provides meaningful performance insights for SPAs.

### Views and view instances

Each navigation creates a new **view instance**, whether it's a soft navigation or a hard navigation involving a full-page load. The start of a new page instance always marks the start of a new view instance.

Captured data for a view instance is aggregated into a [view summary event](/docs/semantic-dictionary/model/rum/user-events/navigation-related#view-summary), identified by its [`view.instance_id`](/docs/semantic-dictionary/model/rum/user-events#view-attributes "User events provide deep visibility and insights into experience, behavior, performance, and errors of your customers and end-users in real-time.").

**Views** group all visits into a single aggregated entry. To analyze the same view across multiple visits, view instances are grouped under the `view.name`. This attribute is designed to filter out dynamic parts of the URL for better grouping. It's derived from `view.detected_name`, which the RUM JavaScript bases on the URL.

During the page's lifespan, the `view.sequence_number` attribute is incremented with every navigation to a new view.

Conceptually, if a page loads and no soft navigation occurs before the next page load, the values in the view summary event and the page summary event are identical. When one or more soft navigations occur during the lifecycle of a page instance, the values in the page and view summaries diverge.

### Example of page and view instances

The following diagram shows the page and view instances created during a website visit that involves both hard and soft navigations.

![Pages and page instances](https://dt-cdn.net/images/page-instances-4210-69ed8aa0e8.png)

* When the user visits the start page `/` of a website, the following attributes are captured:

  + `page.instance_id` is a random value that identifies this exact page instance.
  + `page.detected_name` is the name detected by the RUM JavaScript.
  + `page.name` is the name used by the Dynatrace backend to group all instances.
* When the user navigates to the products page `/products` using a hard navigation:

  + `page.instance_id` and `view.instance_id` are newly generated random values.
  + `view.sequence_number` resets to 1.
* When the user views two separate products using soft navigations:

  + The `page.instance_id` remains the same.
  + `view.sequence_number` increments with each soft navigation.
  + `view.instance_id` is newly generated for each soft navigation.
  + `view.detected_name` contains a changing ID (`12345` and `56789`).
  + `view.name` replaces this dynamic ID with `:id:` for better grouping.
* When the user navigates back to the start page `/` with a hard navigation:

  + `page.instance_id` and `view.instance_id` are newly generated random values.
  + `view.sequence_number` resets to 1.

### Google Web Vitals

The New RUM Experience doesnât just capture Web Vitals for pages, it also captures them for views within a page. This is especially important for SPAs.

For example, imagine a page that displays an image gallery. The initial view shows an overview with small thumbnails. When the user navigates to the detail view of an image, a new view starts.

* The first view summary reports the Interaction to Next Paint (INP) value for the initial page load and for clicks on the small thumbnails.
* Subsequent view summary events report the INP value for the detail views, where the user interacts with larger images.
* The page summary event reports the INP value for all clicks occurring across the navigated views.

### Example DQL query

The following query retrieves the 75th percentile for LCP by view.

```
fetch user.events



| filter characteristics.has_view_summary



| filter isNotNull(web_vitals.largest_contentful_paint)



| summarize {



percentile(web_vitals.largest_contentful_paint, 75)



}, alias:view_LCP, by:{ view.name }



| sort view_LCP desc
```

## Navigations

[Navigation events](/docs/semantic-dictionary/model/rum/user-events/navigation-related#navigation) are reported during view changes and/or page changes. How they are reported depends on whether the navigation is hard (full page load) or soft (SPA route change).

### Hard navigations

For a hard navigation or full page load, the navigation event includes the document request and has, among others, the following characteristics:

* `characteristics.has_navigation`
* `characteristics.has_w3c_navigation_timings`

These events also contain full [W3C Navigation Timingï»¿](https://www.w3.org/TR/navigation-timing-2/) data from supporting browsers.

### Soft navigations

For a soft navigation, a standalone navigation event is reported with the characteristic `characteristics.has_navigation`. It includes basic information about the navigation, such as:

* `navigation.type`, which can be `hard` or `soft`.
* Information about the previous view, such as `view.source.name` and `view.source.url.full`.
* Information about the new view, such as `view.name` and `view.url.full`.

### Example of hard and soft navigations

The diagram below illustrates how view and page summaries are reported during hard and soft navigations, along with the corresponding navigation events.

![Pages, views and navigations](https://dt-cdn.net/images/pages-views-navigations-3296-b049928613.png)

* When a new page is loaded (hard navigation), a navigation event is sent with the characteristic `has_w3c_navigation_timing`.
* When a soft navigation occurs, the view summary of the previous view and the navigation event for the new view are sent.
* When the page is left, both the view summary and the page summary are sent together.

### Example DQL query



The following DQL query retrieves the amount of hard and soft navigations.

```
fetch user.events



| filter characteristics.has_navigation



| summarize count(), by: navigation.type
```