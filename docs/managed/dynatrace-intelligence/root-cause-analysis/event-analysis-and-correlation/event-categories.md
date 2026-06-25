---
title: Event categories
source: https://docs.dynatrace.com/managed/dynatrace-intelligence/root-cause-analysis/event-analysis-and-correlation/event-categories
scraped: 2026-05-12T11:36:46.762528
---

# Event categories

# Event categories

* Explanation
* 2-min read
* Updated on Feb 25, 2026

Dynatrace supports different categories of Davis events, where each Davis event comes with an event type and a severity (significance) level.

* Resulting problems aggregate all included Davis event severities and are evaluated with the highest severity level of the constituent Davis events.
* During its lifespan, a problem might raise its severity level. For example, a problem might begin in slowdown level and then be raised automatically to availability level when an outage is detected.

In order from most to least severe, the Davis event categories supported in Dynatrace are as follows:

## Monitoring unavailable

[Monitoring unavailable events](/managed/dynatrace-intelligence/root-cause-analysis/event-analysis-and-correlation/event-categories/monitoring-unavailable-events "Learn more about `monitoring unavailable` events and the logic behind raising them.") indicate a widespread monitoring interruption, where the majority of your installed OneAgents lose their connection with the Dynatrace server. This usually manifests itself as a lack of visibility in terms of both availability and performance monitoring.

## Availability

[Availability events](/managed/dynatrace-intelligence/root-cause-analysis/event-analysis-and-correlation/event-categories/availability-events "Learn more about availability events and the logic behind raising them.") indicate high-severity incidents within your environment, such as a complete outage or unavailability of servers or processes.

## Error

[Error events](/managed/dynatrace-intelligence/root-cause-analysis/event-analysis-and-correlation/event-categories/error-events "Learn more about error events and the logic behind raising them.") inform you of increased error rates or other error-related incidents that interfere with the regular operation of your environment.

## Slowdown

[Slowdown events](/managed/dynatrace-intelligence/root-cause-analysis/event-analysis-and-correlation/event-categories/slowdown-events "Learn more about slowdown events and the logic behind raising them.") indicate a decrease of performance in one of your operational services or applications.

* While slowdown events are less severe than error or availability Davis events, they inform you of potential issues with the performance of your services.

## Resource

[Resource events](/managed/dynatrace-intelligence/root-cause-analysis/event-analysis-and-correlation/event-categories/resource-events "Learn more about resource events and the logic behind raising them.") indicate resource contention. Typical examples:

* CPU saturation
* Memory saturation

## Custom

[Custom alerts](/managed/dynatrace-intelligence/root-cause-analysis/event-analysis-and-correlation/event-categories/custom-alerts "Learn more about custom alerts and the logic behind raising them.") are used to enable alerting on any user-defined thresholds.

* Custom alerts for user-defined thresholds can be set for any Dynatrace metric.
* Like other events, custom alerts can be controlled by Davis and are automatically alerted on.

## Info

[Info events](/managed/dynatrace-intelligence/root-cause-analysis/event-analysis-and-correlation/event-categories/info-events "Learn more about informational events and the logic behind raising them.") indicate manually triggered Davis events that don't result in the creation of a new problem, such as:

* Important deployments or configuration changes
* Administrative Davis events (for example, automatic migration of a virtual machine)

Informational Davis events aren't sent out as alerts and no problems are opened, as this category of Davis events doesn't indicate an abnormal situation.

## Warning

[Warning events](/managed/dynatrace-intelligence/root-cause-analysis/event-analysis-and-correlation/event-categories/warning-events "Learn more about warning events and the logic behind raising them.") inform you that something might become a problem in the near future.

* Like info events, warnings don't result in the creation of a new problem.
* Warning events have the same severity level as info events.