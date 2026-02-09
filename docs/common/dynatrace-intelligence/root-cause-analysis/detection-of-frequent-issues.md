---
title: "Detection of frequent issues"
source: https://docs.dynatrace.com/docs/dynatrace-intelligence/root-cause-analysis/detection-of-frequent-issues
updated: 2026-02-09
---

# Detection of frequent issues

# Detection of frequent issues

* Latest Dynatrace
* Explanation
* 5-min read
* Updated on Aug 20, 2025

Within large environments, certain aspects of your system may consistently trigger alerts that are unnecessary because they relate to non-severe known issues that don't require a human response. Such alert noise may come from non-critical components or build machines that are low on resources, but aren't in a critical state.

To reduce such alert noise and avoid alert spamming, the Dynatrace AI causation engine automatically detects regularly occurring issues that originate from sub-optimal, though acceptable, conditions. Dynatrace detects such frequent issues by reviewing the problem patterns of monitored entities within specified observation periods of one day and one week.

When the same problem is detected multiple times within these periods, Dynatrace evaluates the problem based on the actual severity of a threshold breach combined with the duration of the problem. It then compares the severities and durations of past problem alerts on the same entity and only alerts if the severity of the problem has increased. The following diagram illustrates this process.

![Problem raised](https://dt-cdn.net/images/frequent-issues-1124-d6a429a551.png)

Problems that are less severe and have a shorter duration than previous alerts are considered to be frequent issues and so alerts are suppressed for these. For details on event severities, see [event types](/docs/dynatrace-intelligence/root-cause-analysis/event-analysis-and-correlation/event-categories "Learn about different categories of events and supported event types, along with their severity levels, and the logic behind raising them.").

This intelligent approach to detection and handling of frequent issues guarantees that you receive alerts for problems that increase in severity over time while simultaneously avoiding alert spamming.

Entity overview pages that are subject to frequent issues include a **Frequent issue** message.

## Frequent issue evaluation

The diagram below shows the classification of issues.

* Green is normal operating state.
* Yellow is an event that reoccurs frequently but is normal for your system. It can be, for example, a slow disk event that relates to a non-mission critical device. These events are unhealthy but no alerting is necessary.
* Red is an event that does affect the normal operation and triggers an alert.

![Frequent issue detection diagram](https://dt-cdn.net/images/frequent-issue-detection-diagram-500-62d4dabc85.png)

The goal of the evaluation process is to classify an incoming event as yellow or red.

The evaluation process is independent for every event type and every monitored entity. For example, if we receive multiple events or events with long durations for the same event type and monitored entity within a reference period, the events will be evaluated together and contribute to the frequent issue detection. In this case, new events for the same event type and monitored entity will also be considered as frequent.

The evaluation begins with two sets of historic events:

* Events for the last 24 hours
* Events for the last 7 days

And goes as follows:

1. The 24-hours set is sorted in two ways:

   * Duration (shortest to longest)
   * Severity (less to more severe)
2. When a new event arrives, it is placed in proper position in each of these sorted sets.
3. From each initial sorted set, a subset is created, consisting of events to the right of the new event (that is, longer and more severe).
4. A **reference set** is created, consisting of events that appear in both of these two subsets.

   1. The **size of the reference set** is calculated as the number of events in the reference set.
   2. The **duration of the reference set** is calculated as the sum of the durations of the events in the reference set.
5. The same reference set is created from the 7-days set.
6. The following criteria are evaluated:

   * If the size of the 24-hours reference set equals or is greater than **3**, the condition is resolved as yellow. Otherwise it is resolved as red.
   * If the duration of the 24-hours reference set is equal to or greater than **50% of 24 hours** (12 hours = 720 minutes = 43,200 seconds), the condition is resolved as yellow. Otherwise it is resolved as red.
   * If the size of the 7-days reference set is equal to or greater than **7**, the condition is resolved as yellow. Otherwise it is resolved as red.
   * If the duration of the 7-days reference set is equal to or greater than **30% of 7 days** (50.4 hours = 3,024 minutes = 181,440 seconds), the condition is resolved as yellow. Otherwise it is resolved as red.
7. If at least one condition is resolved as yellow, the event is classified is yellow.  
   Otherwise it is classified as red and an alert is triggered.

After initial evaluation, every yellow event is evaluated again with a 1-minute interval until it shifts to red or is deactivated.

See the expandable section below for an example of the evaluation process.

Example

For the sake of simplicity, this example only considers the 24-hours set. In this example the event type is [CPU saturation](/docs/dynatrace-intelligence/root-cause-analysis/event-analysis-and-correlation/event-categories/resource-events#cpu-saturation "Learn more about resource events and the logic behind raising them.") on a host.

Historic events for the last 24 hours have the following durations and severities:

Event1â45 seconds, 95.5%  
Event2â15 seconds, 99%  
Event3â35 seconds, 98%  
Event4â30 seconds, 97%  
Event5â60 seconds, 96%

The sorted sets look like this:

Duration: {Event2, Event4, Event3, Event1, Event5}  
Severity: {Event1, Event5, Event4, Event3, Event2}

A new event arrives: EventNEWâ28 seconds, 95%. It takes the following positions in sorted sets:

Duration: {Event2, **EventNEW**, Event4, Event3, Event1, Event5}  
Severity: {**EventNEW**, Event1, Event5, Event4, Event3, Event2}

The subsets, consisting of the events to the right, look like this:

Duration: {Event4, Event3, Event1, Event5}  
Severity: {Event1, Event5, Event4, Event3, Event2}

The following events appear in both subsets and form the refence set: {Event1, Event3, Event4, Event5}.

The size of the reference set is **4**. The condition is resolved as yellow.  
The duration of the reference set is **170** seconds. The condition is resolved as red.

There is one yellow condition, therefore the EventNEW is classified as yellow and doesn't trigger an alert.
