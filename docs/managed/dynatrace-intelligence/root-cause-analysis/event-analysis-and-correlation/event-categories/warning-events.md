---
title: Warning events
source: https://docs.dynatrace.com/managed/dynatrace-intelligence/root-cause-analysis/event-analysis-and-correlation/event-categories/warning-events
---

# Warning events

# Warning events

* Explanation
* 1-min read
* Published Feb 25, 2026

This page provides information about supported warning events and the logic behind raising them.

A `WARNING` event type has a similar purpose to the `INFO` event type: it informs you that something might become a problem in the near future. For example, something is running on an old app version or using a deprecated feature, but it's not an issue yet.

In the UI, warnings are highlighted in yellow. They have the same severity level as info events and don't trigger problems by themselves, but can appear in a problem as an additional info event with severity level 5.

A warning event occurs as a single point in time, so it doesn't have `Active` and `Close` durations.

This event type is supported in all event sources, including anomaly detectors, API, OneAgent event ingest, and OpenPipeline.

### Applicable Dynatrace entities

All Dynatrace entities apply to this event.

## Related topics

* [Unavailable in Dynatrace Managed](/managed/upgrade/unavailable-in-managed "Your selection is unavailable in Dynatrace Managed.")