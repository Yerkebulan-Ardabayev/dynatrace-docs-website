---
title: User experience score
source: https://docs.dynatrace.com/managed/observe/digital-experience/rum-concepts/scores-and-ratings/user-experience-score
scraped: 2026-05-12T11:35:17.135687
---

# User experience score

# User experience score

* Explanation
* 3-min read
* Updated on Jan 27, 2023

In Dynatrace, the user experience score is a metric that categorizes every user session recorded with Real User Monitoring.

With the user experience score, Dynatrace can rate each user session as:

* **Frustrating**
* **Tolerable**
* **Satisfying**

To determine these categories, Dynatrace applies performance, error, and usability indicators to each recorded session. These indicators, when combined with the information derived from user flow, are used to calculate the user experience score.

It also takes into account issues such as slow performance, rage clicks and taps, errors, and other usability problems that can lead the user to abandon the session.

## Configure user experience score thresholds

For configuration details, see the following pages.

* [Change user experience score thresholds for web applications](/managed/observe/digital-experience/web-applications/additional-configuration/configure-user-experience-score-web "Adjust the user experience score thresholds to meet the specific requirements of your web application.")
* [Change user experience score thresholds for mobile applications](/managed/observe/digital-experience/mobile-applications/additional-configuration/configure-user-experience-score-mobile "Adjust the user experience score thresholds to meet the specific requirements of your mobile application.")
* [Change user experience score thresholds for custom applications](/managed/observe/digital-experience/custom-applications/additional-configuration/configure-user-experience-score-custom "Adjust the user experience score thresholds to meet the specific requirements of your custom application.")

## Calculate the user experience score

To calculate the user experience score, we assigned a weight and an element Apdex to each element that makes up a session, as shown in the following table:

| Element | Weight | Element Apdex |
| --- | --- | --- |
| [User action](/managed/observe/digital-experience/rum-concepts/user-actions "Learn what user actions are and how they help you understand what users do with your application.") | 3 | Frustrating, Tolerable, or Satisfying |
| [Error](/managed/observe/digital-experience/rum-concepts/user-and-error-events#error "Learn about user and error events and the types of user and error events captured by Dynatrace.") | 1 | Frustrating |
| [Rage event](/managed/observe/digital-experience/rum-concepts/user-and-error-events#rage-event "Learn about user and error events and the types of user and error events captured by Dynatrace.") | 2 | Frustrating |
| [Crash](/managed/observe/digital-experience/rum-concepts/user-and-error-events#crash "Learn about user and error events and the types of user and error events captured by Dynatrace.") | 5000 | Frustrating |

As soon as a session starts being recorded, the following process is applied to calculate its user experience score:

1. Each element of the session is assigned a weight and is classified as **Frustrating**, **Tolerable**, or **Satisfying**. Elements such as crashes, errors, rage clicks, and rage taps are all classified as **Frustrating**.
2. For each of these categories, the total weight of the elements is calculated. For example, **F** is the total weight of **Frustrating** elements, **S** is the total weight of **Satisfying** elements, and **T** is the total weight of **Tolerable** elements.
3. The total weight of all these categories is calculated: **Total**=**F**+**S**+**T**
4. Each of these weights is then divided by this total weight.
5. Depending on the thresholds defined on the **User experience score** page, the session is marked **Frustrating**, **Tolerable**, or **Satisfying**.

A user session is never marked **Satisfying** if there is even one **Frustrating** element in the session. In such cases, the session is determined to be either **Frustrating** or **Tolerable**.

## Score calculation example

To understand the user experience score calculation better, consider the following example.

A session comprises 11 elements, including XHR actions, load actions, errors, and a rage click.
The **Threshold for Frustrating user experience** is set to 30%, and the **Threshold for Satisfying user experience** is set to 50%.

Each element has been assigned an ID to ease the process of calculation.

![User experience score calculation example](https://dt-cdn.net/images/user-xp-score-example-2210-da974c6889.png)

User experience score calculation example

Total weight of **Frustrating** elements (**F**) = 9  
Total weight of **Tolerable** elements (**T**)= 9  
Total weight of **Satisfying** elements (**S**)= 6

Total weight of all the elements (**Total**) = 9 + 9 + 6 = 24

**F/Total** = 9 24 = 0.375 = 37.5% of user session elements are "Frustrating"  
**T/Total** = 9 24 = 0.375 = 37.5% of user session elements are "Tolerable"  
**S/Total** = 6 24 = 0.25 = 25% of user session elements are "Satisfying"

Because more than 30% of user session elements are "Frustrating" (**F/Total** > **30%**), the user experience score of this session is **Frustrating**.

## Related topics

* [Change user experience score thresholds for web applications](/managed/observe/digital-experience/web-applications/additional-configuration/configure-user-experience-score-web "Adjust the user experience score thresholds to meet the specific requirements of your web application.")
* [Change user experience score thresholds for mobile applications](/managed/observe/digital-experience/mobile-applications/additional-configuration/configure-user-experience-score-mobile "Adjust the user experience score thresholds to meet the specific requirements of your mobile application.")
* [Change user experience score thresholds for custom applications](/managed/observe/digital-experience/custom-applications/additional-configuration/configure-user-experience-score-custom "Adjust the user experience score thresholds to meet the specific requirements of your custom application.")