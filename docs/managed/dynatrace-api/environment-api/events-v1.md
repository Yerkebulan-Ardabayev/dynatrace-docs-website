---
title: Events API v1
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/events-v1
scraped: 2026-05-12T12:05:46.151224
---

# Events API v1

# Events API v1

* Reference
* Updated on Jun 13, 2022
* Deprecated

This API is deprecated. Use the [Events API v2](/managed/dynatrace-api/environment-api/events-v2 "Find out what you can do with the Dynatrace Events API v2.") instead.

The **Events** API delivers details about all uncorrelated events that Dynatrace collects within your environment. Information returned for each event includes attributes about the event source, the entity where the event was collected, and other event-specific details.

### Event feed

[Get global feed](/managed/dynatrace-api/environment-api/events-v1/get-events-feed "List events feed via the Dynatrace API.") of **all** uncorrelated events in an environment.

### View an event

[Get parameters](/managed/dynatrace-api/environment-api/events-v1/get-event "View parameters of an event via the Events API v1.") of a specific event by its ID.

### Push events

[Push external events](/managed/dynatrace-api/environment-api/events-v1/post-event "Create a custom event via the Dynatrace API.") to your Dynatrace environment.

### Push Jenkins events

[Implement the automatic export](/managed/dynatrace-api/environment-api/events-v1/push-deployment-events-from-jenkins "Push Jenkins deployment events to Dynatrace.") of deployment events from Jenkins to Dynatrace.

## Related topics

* [Event categories](/managed/dynatrace-intelligence/root-cause-analysis/event-analysis-and-correlation/event-categories "Learn about different categories of events and supported event types, along with their severity levels, and the logic behind raising them.")
* [Event analysis and correlation](/managed/dynatrace-intelligence/root-cause-analysis/event-analysis-and-correlation "Gain an understanding of the Events section on each host, process, and service overview page.")
* [Creating a deployment event via the Dynatrace APIï»¿](https://www.youtube.com/watch?v=LDAiUMdrtvA)