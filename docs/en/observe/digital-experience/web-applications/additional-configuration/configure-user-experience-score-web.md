---
title: Change user experience score thresholds for web applications
source: https://www.dynatrace.com/docs/observe/digital-experience/web-applications/additional-configuration/configure-user-experience-score-web
scraped: 2026-02-25T21:28:20.757034
---

# Change user experience score thresholds for web applications

# Change user experience score thresholds for web applications

* How-to guide
* 1-min read
* Published Jan 27, 2023

A [user experience score](/docs/observe/digital-experience/rum-concepts/scores-and-ratings/user-experience-score "User experience score is a metric used to categorize user sessions as Frustrating, Tolerable, or Satisfying.") is an important metric that reflects the overall performance, usability, and detected errors of each session. You can adjust the user experience score thresholds for your applications.

To set up the user experience score thresholds

1. Go to **Settings** > **Web and mobile monitoring** > **User experience score**.

   ![User experience score settings](https://dt-cdn.net/images/user-xp-score-settings-2292-03a4586d9e.png)
2. Optional Turn on **If last user action in a session is classified as Frustrating, classify the entire session as Frustrating** to judge a frustrating session by its last action.
3. Optional Turn on **Consider rage clicks / rage taps in score calculation** to include [rage events](/docs/observe/digital-experience/rum-concepts/user-and-error-events#rage-event "Learn about user and error events and the types of user and error events captured by Dynatrace.") when determining the user experience score.
4. In the **Threshold for Frustrating user experience** box, enter the percentage of **Frustrating** user actions beyond which a user session is considered **Frustrating**.
5. In the **Threshold for Satisfying user experience** box, enter the minimum percentage of **Satisfying** user actions required to consider a session **Satisfying**.

## Related topics

* [User experience score](/docs/observe/digital-experience/rum-concepts/scores-and-ratings/user-experience-score "User experience score is a metric used to categorize user sessions as Frustrating, Tolerable, or Satisfying.")