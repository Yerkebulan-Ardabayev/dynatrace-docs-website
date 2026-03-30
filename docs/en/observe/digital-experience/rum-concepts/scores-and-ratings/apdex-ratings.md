---
title: Apdex ratings
source: https://www.dynatrace.com/docs/observe/digital-experience/rum-concepts/scores-and-ratings/apdex-ratings
scraped: 2026-03-05T21:27:21.930906
---

# Apdex ratings


* Classic
* Explanation
* 3-min read
* Updated on Jan 27, 2023

Dynatrace calculates [Apdex ratingsï»¿](https://en.wikipedia.org/wiki/Apdex) to provide you with a single metric that tells you about the performance of your application and the errors that impact user experience.

Apdex is calculated for each discrete user action and each application overall. In this way, it provides quick insight into the user experience within your application.

Default Apdex ratings in Dynatrace are based on application-specific thresholds.

| Score | Performance level |
| --- | --- |
| 0.94â1.0 | Excellent |
| 0.85â0.94 | Good |
| 0.7â0.85 | Fair |
| 0.5â0.7 | Poor |
| < 0.5 | Unacceptable |

Apdex ratings can be used as benchmarks for comparing two applications over time, even though the timing thresholds set up for the two applications may be different.

Applications are typically comprised of many different user action types. For example, it might be acceptable to have a complex search that takes up to 6 seconds to complete while the loading of the homepage in the same application might need to take less than 2 seconds to ensure user satisfaction. Such differences can be addressed by configuring different Apdex thresholds for various user action types.

For more details on the Apdex standard, see [Apdex Referencesï»¿](https://www.apdex.org/index.php/documents/).

## Adjust Dynatrace Apdex settings

You can customize Dynatrace Apdex ratings based on the specific requirements of your application. Once configured, they give you a quick and easy way of evaluating the performance of all user actions that you're monitoring: a value of `1.0` is perfect; values below `0.5` are unacceptable. It's recommended that you define appropriate user-satisfaction timing thresholds and error impact configurations for each monitored user action.

You can adjust the Apdex settings for your application and for its key user actions.

### Configure Apdex settings for applications

You can modify the Apdex thresholds for your web, mobile, and custom applications.

### Configure Apdex settings for key user actions

You can also change the Apdex thresholds for a particular key user action for your web, mobile, and custom applications.

## Error impact on Apdex

User actions with JavaScript [errors](../user-and-error-events.md#error "Learn about user and error events and the types of user and error events captured by Dynatrace.") are rated as **Frustrated**. Sometimes, user actions that are, in fact, fast and below the Apdex threshold are displayed in red and rated as **Frustrated** because some of the user actions have JavaScript errors.

The same is true for request errors. An HTTP response code, CSP violation, or resource request that is configured in settings to be captured as an error leads to a **Frustrated** user action.

You can exclude errors from Apdex calculations. See Configure error detection for web applications, Adjust Apdex settings for mobile applications, and Adjust Apdex settings for custom applications for more details.

Example: error rules

![Application rules for errors](https://dt-cdn.net/images/web-app-settings-for-error-rules-1200-9e80202ff2.png)

## Apdex-based analysis

Dynatrace makes it easy for you to analyze your application's Apdex from a variety of dimensions. You can check the Apdex rating for a particular user action, location, and application as well as view the Apdex rating for each user action within one user session.

For more details, see Context-based Apdex analysis.

## Related topics

* Adjust Apdex settings for web applications
* Adjust Apdex settings for mobile applications
* Adjust Apdex settings for custom applications
* Context-based Apdex analysis