---
title: User interactions
source: https://www.dynatrace.com/docs/observe/digital-experience/new-rum-experience/user-interactions
scraped: 2026-02-17T05:06:33.751737
---

# User interactions

# User interactions

* Latest Dynatrace
* How-to guide
* Updated on Jan 21, 2026

Early Access

The New RUM Experience allows you to capture [user interactions](/docs/observe/digital-experience/new-rum-experience/concepts/data-model#user-interactions "Get familiar with the data model at the heart of the New RUM Experience.") such as clicks and scrolls on web frontends, as well as touch events on mobile frontends.

User interactions are currently in Early Access and available for the following technologies:

* Web
* iOS native
* Android native
* SwiftUI
* Jetpack Compose

## Early Access FAQ

What is the cost of ingesting user interactions?

There are no additional charges during the User Interaction Early Access.

What is the cost of querying user interactions?

Raw DEM data queries are currently in Early Access. There are no additional charges during this period. For details, see [Calculate your consumption of Digital Experience Monitoring (DEM) - Query](/docs/license/capabilities/digital-experience-monitoring-query-retain/queries-dem "Learn how your consumption of the DEM-related DQL queries is consumed and billed before and after Early Access.").

What is the data retention period for user interactions?

Like other user events, user interactions have a [default data retention period](/docs/manage/data-privacy-and-security/data-privacy/data-retention-periods#new-rum-user-events-and-sessions "Check retention times for various data types.") of 35 days. You can extend data retention by joining the [Extended Retention for RUM & Synthetic preview](/docs/whats-new/preview-releases#extended-retention-for-rum-and-synthetic "Learn about our Preview releases and how you can participate in them.").

## Types of user interactions

The following table provides an overview of the available types of user interactions. For a detailed specification, see [User interaction](/docs/semantic-dictionary/model/rum/user-events/user-interactions) in the Semantic Dictionary.

User interaction type

Description

Frontend type

Click

When a user clicks or touches an HTML element. Note that a touch on an HTML element is captured as a click.

Web

Touch

When a user touches a mobile component.

Mobile

Key press

When a user presses a key combination involving the `Ctrl`, `Alt`, or `Meta` (`Windows` or `Cmd`) keys, or presses one of the individual keys `Esc`, `Enter`, `Tab`, and `Space`.

Web

Zoom/Resize

When a user zooms in or out, or resizes the viewport.

Web

Focus/Blur

When a user focuses on or leaves an HTML element. This interaction is only captured if the `data-dt-focus` or `data-dt-blur` attributes, respectively, are present on the HTML element.

Web

Change

When a user modifies a value in a form field, for example, by selecting a checkbox.

Web

Scroll

When a user scrolls through a page or view.

Web

Drag/Drop

When a user starts or ends a drag operation. Valid external drop actions are also captured, for example, dropping a file into an upload area. In both cases, the position is recorded.

Web

Mouseover

When a user hovers over an HTML element. This interaction is only captured if the `data-dt-mouse-over=<ms>` attribute is present on the HTML element.

Web

## Activate capturing of user interactions

To capture user interactions for a web or mobile frontend

1. Go to ![Experience Vitals](https://dt-cdn.net/images/experience-vitals-256-9999590b55.png "Experience Vitals") **Experience Vitals** > **Overview**.
2. Select  **Frontends** to view all frontends.
3. Select the frontend you want to configure.
4. Switch to the **Settings** tab.
5. Under **Enablement and cost control**, turn on **User Interactions** .

## Analyze user interactions

There are two primary ways to analyze user interactions:

* The [![Users & Sessions](https://dt-cdn.net/images/users-sessions-149-f84e0b9b20.png "Users & Sessions") **Users & Sessions**](/docs/observe/digital-experience/new-rum-experience/users-and-sessions "The Users & Sessions app delivers insight into individual user journeys and behavior patterns.") app lets you view all user interactions that occurred during a user session. This is particularly helpful for customer support teams and developers who need to understand what happened when troubleshooting customer issues or bugs. After filtering sessions based on your criteria and selecting one, all related user interactions are listed and displayed in the timeline.
* User interaction analysis via DQL supports a wide range of behavioral use cases for product managers and product owners. In these scenarios, user interactions often appear alongside navigation events. For examples of how to derive behavioral insights using DQL, see [DQL examples](/docs/observe/digital-experience/new-rum-experience/use-cases/dql-examples#behavioral-insights "Analyze and explore RUM data in depth by leveraging DQL.").