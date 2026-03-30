---
title: Data model of the New RUM Experience
source: https://www.dynatrace.com/docs/observe/digital-experience/new-rum-experience/concepts/data-model
scraped: 2026-03-05T21:35:37.839352
---

# Data model of the New RUM Experience


* Latest Dynatrace
* Explanation
* Updated on Mar 03, 2026

The New RUM Experience provides deep visibility into how end users interact with the frontends of your applications. It delivers insights into user behavior and experience, along with performance metrics and error details. This page outlines the underlying data model and how the captured data is organized in Grail.

![New RUM Experience data model](https://dt-cdn.net/images/data-model-2264-a2dd12ab3d.png)

## User Events

In the New RUM Experience, all end-user data is captured as **user events**, which are stored in the `user.events` table. For details, see User events in the Semantic Dictionary.

Each event includes the following attributes:

* Basic attributes such as an ID, start and end time, and duration.
* Contextual details such as operating system, geolocation, device, and browser.
* At least one characteristic that describes the event's natureâfor example, navigations, errors, requests, or user interactions.
* Attributes specific to the event's characteristics.

The following sections outline some important user event characteristics.

### Page summaries, view summaries, and navigations

The concept of **pages** applies only to web frontends, where it represents an HTML page loaded through a full page load.

**Views**, on the other hand, refer to the content displayed to the user at any time. Views are supported on both web and mobile frontends:

* On web, unlike pages, switching to a new view does not require a full page load.
* On mobile, a view represents a specific screen presented to the user.

Data collected for a page or viewâsuch as performance metrics and error countsâis aggregated in page summary or view summary events.

Navigations describe the transitions from one view to another or from one page to another.

To learn more about pages, views, and navigations in web frontends, see Pages, views, and navigations in the New RUM Experience. To learn more about views and navigations in mobile frontends, refer to Concepts for mobile frontends.

### User interactions

Early Access

**User interactions** represent activities performed by an end user on the application's frontend. The specific types of interactions depend on the frontend technology:

* For web applications, this includes events such as clicks, scrolls, and mouseover.
* For mobile applications, it includes mobile touches.

For a complete list of user interactions, see User interactions in the Semantic Dictionary.

Capturing user interactions can be enabled as described in Configure user interaction capturing for web frontends and Configure user interaction capturing for mobile frontends.

In RUM Classic, user interactions were only recorded when they were part of a user action involving a request. In the New RUM Experience, this restriction does not applyâinteractions can be captured independently of any request.

### User actions

A user action represents a significant operation within the frontend and its implications, such as:

* a click followed by an XHR request
* a soft navigation followed by DOM mutations

Currently, user actions are only available for web frontends. For details, see User actions in web frontends.

### Requests

Request events capture requests issued by the browser or mobile app, such as HTTP calls. They include details like the URL, HTTP method, and status code for HTTP requests, along with performance metricsâfor example, values from the [W3C Resource Timingï»¿](https://www.w3.org/TR/resource-timing/) and [W3C Navigation Timingï»¿](https://www.w3.org/TR/navigation-timing-2/) APIs in web frontends.

### Errors

The New RUM Experience captures a wide range of error types, including:

* Failed requests
* Uncaught exceptions
* CSP violations in web frontends
* Crashes in mobile frontends
* Application Not Responding (ANR) errors in mobile frontends

For the full specification of errors, see [Semantic DictionaryâGlobal field referenceâError](../../../../semantic-dictionary/fields.md#error "Get to know the list of global fields that have a well defined semantic meaning in Dynatrace and can be used across different monitoring types.").

## User sessions

**User sessions** summarize all user events from the same end user within a limited time frame. A session ends after a period of inactivity or when the maximum session duration is reached. User sessions are stored in the `user.sessions` table.

Unlike RUM Classic, there is no limit on the number of user actions per session.

You can add a **user identifier** to each session via the [RUM JavaScript APIï»¿](https://www.dynatrace.com/support/doc/javascriptapi/doc-latest/functions/Types.dynatrace.identifyUser.html) or the mobile RUM APIs APIs for mobile frontends, including startup configuration, event reporting, error handling, view tracking, and advanced features for Dynatrace on Grail.") to facilitate analysis based on user context. If your code already calls the RUM Classic API to identify a user, this call is also effective for the New RUM Experience.

To learn more about the user session lifecyle in web frontends, see User sessions in web frontends. For the full specification of user sessions, see User sessions in the Semantic Dictionary.

## Event and session properties

**Event and session properties** are custom key-value pairs you can define to enrich captured user events and sessions. These properties enable, for example, powerful queries, filtering, and the creation of custom metrics.

To learn how to add event and session properties, see Capture event and session properties for web frontends and Capture event and session properties for mobile frontends.

## Related topics

* Concepts for web frontends
* Concepts for mobile frontends
* User events
* User sessions