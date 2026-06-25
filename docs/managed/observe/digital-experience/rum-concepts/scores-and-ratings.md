---
title: Dynatrace scores and ratings
source: https://docs.dynatrace.com/managed/observe/digital-experience/rum-concepts/scores-and-ratings
scraped: 2026-05-12T11:31:32.927901
---

# Dynatrace scores and ratings

# Dynatrace scores and ratings

* Overview
* 1-min read
* Published Jul 19, 2017

Dynatrace uses different ratings and scores to measure the performance of your application as well as the user experience it delivers.

These ratings are especially handy when you have a number of applications and want to get a quick overview of their states or compare their performance. There are a number of metrics, such as **Visually complete** or the number of errors produced, to make such comparisons. However, as applications vary in so many ways, it's sometimes not so helpful to make one-to-one comparisons using specific metrics. For example, a median **Visually complete** measurement of 5 seconds for an image gallery application might be fine for its end users, while a 2-second lag for a plain-text news application would be unacceptable.

In such cases, comparing only the raw metrics isn't optimal. Scores and indices give a better picture because they combine different metrics and rules into a single number that factors in the individual thresholds defined for each of your applications. Scores and indices enable you to look at a single number and see if your applications are healthy and your users are satisfied.

* [Apdex ratings](/managed/observe/digital-experience/rum-concepts/scores-and-ratings/apdex-ratings "Learn how Dynatrace uses Apdex to measure user satisfaction with application performance.") are application-level scores used to determine the performance of an application.
* [User experience score](/managed/observe/digital-experience/rum-concepts/scores-and-ratings/user-experience-score "User experience score is a metric used to categorize user sessions as Frustrating, Tolerable, or Satisfying.") is session-based and is used to determine the experience delivered across applications within a single session.