---
title: Configure user interaction capturing for mobile frontends
source: https://www.dynatrace.com/docs/observe/digital-experience/new-rum-experience/mobile-frontends/additional-configuration/user-interactions-mobile
scraped: 2026-02-24T21:23:30.441097
---

# Configure user interaction capturing for mobile frontends

# Configure user interaction capturing for mobile frontends

* Latest Dynatrace
* How-to guide
* Published Feb 12, 2026

Early Access

The New RUM Experience allows you to capture [user interactions](/docs/observe/digital-experience/new-rum-experience/concepts/data-model#user-interactions "Get familiar with the data model at the heart of the New RUM Experience.") and turn them into actionable insights:

* You can view all user interactions that occurred during a user session using the [![Users & Sessions](https://dt-cdn.net/images/users-sessions-149-f84e0b9b20.png "Users & Sessions") **Users & Sessions**](/docs/observe/digital-experience/new-rum-experience/users-and-sessions#events "The Users & Sessions app delivers insight into individual user journeys and behavior patterns.") app. This is especially useful for customer support teams and developers when diagnosing customer issues or bugs.
* User interaction analysis via DQL allows you to understand behavioral patterns across a wide range of use cases; see [DQL examples](/docs/observe/digital-experience/new-rum-experience/use-cases/dql-examples#behavioral-insights "Analyze and explore RUM data in depth by leveraging DQL.").

At this point, [touch events](/docs/semantic-dictionary/model/rum/user-events/user-interactions#touch-events) are the supported user interaction type for mobile frontends, and they are captured when a user touches a mobile component.

During the User Interaction Early Access, there are no additional charges for ingesting user interactions. Querying user interactions is also included at no extra cost, because raw DEM data queries are currently in Early Access; see [Calculate your consumption of Digital Experience Monitoring (DEM) - Query](/docs/license/capabilities/digital-experience-monitoring-query-retain/queries-dem "Learn how your consumption of the DEM-related DQL queries is consumed and billed before and after Early Access.").

## Technology support

User interactions are currently available for the following mobile technologies:

* Android native
* Android Jetpack Compose
* iOS native
* iOS SwiftUI

## Activate capturing of user interactions

To capture user interactions

1. Go to ![Experience Vitals](https://dt-cdn.net/images/experience-vitals-256-9999590b55.png "Experience Vitals") **Experience Vitals** > **Overview**.
2. Select  **Mobile** to view all mobile frontends.
3. Select the frontend you want to configure.
4. Switch to the **Settings** tab.
5. Under **Enablement and cost control**, turn on **User Interactions** .