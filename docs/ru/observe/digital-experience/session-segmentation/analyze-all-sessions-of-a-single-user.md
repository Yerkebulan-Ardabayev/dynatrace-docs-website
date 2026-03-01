---
title: User details
source: https://www.dynatrace.com/docs/observe/digital-experience/session-segmentation/analyze-all-sessions-of-a-single-user
scraped: 2026-03-01T21:21:23.191234
---

# User details

# User details

* Explanation
* 3-min read
* Updated on Jul 20, 2023

For web applications, Dynatrace can show you all the sessions of an individual user, even when those sessions are anonymous or when a [user tag](/docs/observe/digital-experience/rum-concepts/user-and-error-events#user-tagging "Learn about user and error events and the types of user and error events captured by Dynatrace.") has been changed or gone missing. User identification is achieved by storing a persistent cookie within each user's browser. This cookie contains a unique identifier for the user, which is marked as the **Internal user ID** in the Dynatrace web UI. Cookies enable Dynatrace to assign even anonymous user sessions to known users. As long as a user has logged into your application at least once, you can search for and identify that user, even when the user accesses the application in anonymous, unauthenticated sessions. This is particularly useful for analyzing periods of time when a user might not have been able to log into your application because of issues with your authentication service. Note that if a user disables persistent cookies or clears their cookies, the unique identifier is regenerated.

For mobile applications, user identification is achieved by generating and storing a unique identifier when a user launches an application for the first time. This identifier, marked as the **Internal user ID** in the Dynatrace web UI, is regenerated when the user changes their [privacy settings](/docs/observe/digital-experience/mobile-applications/additional-configuration/configure-rum-privacy-mobile#opt-in-mode-mobile "Leverage privacy settings that Dynatrace provides to ensure that your mobile apps comply with the data-privacy regulations of your region."). It's only possible to view all sessions of a particular user when the [data collection level](/docs/observe/digital-experience/mobile-applications/additional-configuration/configure-rum-privacy-mobile#data-collection-levels "Leverage privacy settings that Dynatrace provides to ensure that your mobile apps comply with the data-privacy regulations of your region.") is set to **User behavior**; when the data collection level is set to **Off** or **Performance**, the unique identifier is regenerated for every session, making it impossible to list several sessions of a particular user.

## Focus on the sessions of a single user

On the **User details** page (available by selecting a user from the **User sessions** page), you can find a list of all the sessions of a particular user, the devices this user has used to access your applications, which applications the user accessed, and an overview of the user's profile.

![User detail](https://dt-cdn.net/images/image001-2540-9a3b332524.png)

You can further refine your analysis of the sessions of an individual user by using filter attributes in the filter field, or by enabling **Extended users**.

Extended users

In Dynatrace, there are two ways to identify a user: through the device identifier or through the [user tag](/docs/observe/digital-experience/rum-concepts/user-and-error-events#user-tagging "Learn about user and error events and the types of user and error events captured by Dynatrace."). The concept of **extended user** covers use cases where multiple users or user tags share one device. Dynatrace creates segments of the clusters where the same user tags or device identifiers meet in different combinations. You can turn on these segments comprising different combinations when looking at a user on the user detail page.

![Extended users](https://dt-cdn.net/images/2021-03-24-09-30-56-1351-151ffe14ea.png)

* When you turn on **Extended users**, all information on the user detail page extends to cover all different combinations of the initial user and the user's relations to other devices and/or user tags.
* When you turn off **Extended users**, information displayed on the user detail page consists exclusively of the data from the specific user tag and the devices used by that user tag. If there's no user tag, then the device identifier is used and only for that particular device. For details on how to configure user tagging, see [User tagging](/docs/observe/digital-experience/rum-concepts/user-and-error-events#user-tagging "Learn about user and error events and the types of user and error events captured by Dynatrace.").

Select any session in the list to view the details of that session, including all user actions and events displayed on a timeline. Here you'll find session details, including **Operating system**, device **Manufacturer**, **User tag**, **IP address**, and more.

![Sess detail](https://dt-cdn.net/images/image003-2540-3f624dde4c.png)

### Analysis chart

* The X-axis of the **Analysis** chart shows when the actions occurred during the session, the duration of the action (how long the "dot" is), and the wait time between each action.
* The Y-axis indicates mobile actions, user identifier, and errors and annoyances (for example, `Crash` or `Rage tap`).

![Xaxis](https://dt-cdn.net/images/image005-2530-db89702f1d.png)

Hover over a specific action to get a quick summary of the action. Select a specific action to start replaying the action (if Session Replay has been recorded on the session) or to see more details as shown below.

![Summary](https://dt-cdn.net/images/image007-2530-9eaa21246f.png)

## Examples

Following are examples of session analysis for a single user.

Analyze the sessions of a specific user

### Understand user behavior

To understand how user behavior analysis relates to customer satisfaction, itâs helpful to look at the distribution of the [user experience score](/docs/observe/digital-experience/rum-concepts/scores-and-ratings/user-experience-score "User experience score is a metric used to categorize user sessions as Frustrating, Tolerable, or Satisfying.")).

![Score](https://dt-cdn.net/images/image009-1260-ce456bd0a5.png)

Identify user sessions that have a high number of actions

You can sort the sessions list by **Action count** to find the sessions with the highest number of actions (the same goes for the other columns).

![Action count](https://dt-cdn.net/images/image011-2492-1f5aa2b022.png)

Find sessions of a specific user that resulted in errors or annoyances

When analyzing the user sessions of an individual user, you might want to know which sessions had an error or annoyance or to look at the sessions that had the highest number of errors and annoyances combined (such as [rage clicks or rage taps](/docs/observe/digital-experience/rum-concepts/user-and-error-events#rage-event "Learn about user and error events and the types of user and error events captured by Dynatrace.")).

Get an overview of user activity during the day

When analyzing a user's behavior, it can be interesting to understand at what time of day the user is most active. For example, if a particular user is connected to both web and mobile applications, you can filter for either and see when they are connected throughout the day for the specific application type.

![Session distrib](https://dt-cdn.net/images/image013-1228-bcebf050f8.png)